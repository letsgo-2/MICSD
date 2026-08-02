from __future__ import annotations

# pyright: reportMissingTypeStubs=false, reportMissingTypeArgument=false, reportUnknownMemberType=false, reportAttributeAccessIssue=false, reportArgumentType=false, reportUnusedCallResult=false

import argparse
import ast
import json
import math
from pathlib import Path
from typing import cast

import numpy as np
import pandas as pd


METAL_ORDER = ("Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate catalyst AL performance artifacts without running the AL pipeline."
    )
    _ = parser.add_argument(
        "--al-root",
        type=Path,
        default=Path("AL/catalyst_active_learning_runnable"),
        help="Path to the catalyst_active_learning_runnable directory.",
    )
    _ = parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("performance_evaluation_round1"),
        help="Directory where derived tables and figures are written.",
    )
    _ = parser.add_argument(
        "--composition-tolerance",
        type=float,
        default=1e-6,
        help="Allowed absolute deviation from composition sum of 1.",
    )
    return parser.parse_args()


def read_csv_if_exists(path: Path) -> pd.DataFrame | None:
    if not path.exists():
        return None
    return pd.read_csv(path)


def parse_ratio(value: object) -> list[float] | None:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return None
    if isinstance(value, str):
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return None
    else:
        parsed = value
    if not isinstance(parsed, (list, tuple)) or len(parsed) != len(METAL_ORDER):
        return None
    try:
        numbers = [float(item) for item in parsed]
    except (TypeError, ValueError):
        return None
    return numbers


def normalize_frame_schema(frame: pd.DataFrame, source_name: str) -> pd.DataFrame:
    result = frame.copy()
    result["artifact_source"] = source_name

    if set(METAL_ORDER).issubset(result.columns):
        for metal in METAL_ORDER:
            result[metal] = pd.to_numeric(result[metal], errors="coerce")
        return result

    if "ratio" in result.columns:
        parsed = result["ratio"].map(parse_ratio)
        for index, metal in enumerate(METAL_ORDER):
            result[metal] = parsed.map(
                lambda vector, i=index: vector[i] if vector is not None else np.nan
            )
    return result


def composition_diagnostics(frame: pd.DataFrame, tolerance: float) -> dict[str, object]:
    has_composition = set(METAL_ORDER).issubset(frame.columns)
    diagnostics: dict[str, object] = {
        "has_composition": has_composition,
        "rows": int(len(frame)),
    }
    if not has_composition:
        diagnostics.update(
            {
                "finite_rows": 0,
                "negative_entries": None,
                "sum_min": None,
                "sum_max": None,
                "invalid_sum_rows": None,
            }
        )
        return diagnostics

    values = frame.loc[:, METAL_ORDER].apply(pd.to_numeric, errors="coerce")
    finite_mask = np.isfinite(values.to_numpy(dtype=float)).all(axis=1)
    sums = values.sum(axis=1)
    diagnostics.update(
        {
            "finite_rows": int(finite_mask.sum()),
            "negative_entries": int((values < 0).sum().sum()),
            "sum_min": float(sums.min()) if len(sums) else None,
            "sum_max": float(sums.max()) if len(sums) else None,
            "invalid_sum_rows": int((np.abs(sums - 1.0) > tolerance).sum()),
        }
    )
    return diagnostics


def numeric_series(frame: pd.DataFrame, column: str) -> pd.Series:
    raw = cast(pd.Series, frame[column])
    converted = pd.Series(pd.to_numeric(raw, errors="coerce"), index=frame.index, dtype="float64")
    return converted.dropna()


def numeric_summary(frame: pd.DataFrame, dataset: str, column: str) -> dict[str, object] | None:
    if column not in frame.columns:
        return None
    series = numeric_series(frame, column)
    if series.empty:
        return None
    return {
        "dataset": dataset,
        "metric": column,
        "count": int(series.count()),
        "min": float(series.min()),
        "p25": float(series.quantile(0.25)),
        "median": float(series.median()),
        "mean": float(series.mean()),
        "p75": float(series.quantile(0.75)),
        "max": float(series.max()),
    }


def pareto_mask_max_power_min_cost(frame: pd.DataFrame) -> np.ndarray:
    values = frame[["power_density", "normalized_cost"]].apply(pd.to_numeric, errors="coerce")
    valid = values.notna().all(axis=1).to_numpy()
    mask = np.zeros(len(frame), dtype=bool)
    if not valid.any():
        return mask
    points = values.loc[valid].to_numpy(dtype=float)
    local_mask = np.ones(len(points), dtype=bool)
    for index, point in enumerate(points):
        dominates = (points[:, 0] >= point[0]) & (points[:, 1] <= point[1])
        strictly = (points[:, 0] > point[0]) | (points[:, 1] < point[1])
        if np.any(dominates & strictly):
            local_mask[index] = False
    mask[np.flatnonzero(valid)] = local_mask
    return mask


def clr_transform(values: np.ndarray, epsilon: float = 1e-6) -> np.ndarray:
    array = np.asarray(values, dtype=float)
    array = np.maximum(array, epsilon)
    array = array / array.sum(axis=1, keepdims=True)
    logged = np.log(array)
    return logged - logged.mean(axis=1, keepdims=True)


def novelty_against_reference(frame: pd.DataFrame, reference: pd.DataFrame) -> pd.Series | None:
    if not set(METAL_ORDER).issubset(frame.columns) or not set(METAL_ORDER).issubset(reference.columns):
        return None
    target = frame.loc[:, METAL_ORDER].apply(pd.to_numeric, errors="coerce").dropna()
    ref = reference.loc[:, METAL_ORDER].apply(pd.to_numeric, errors="coerce").dropna()
    if target.empty or ref.empty:
        return None
    target_clr = clr_transform(target.to_numpy(dtype=float))
    ref_clr = clr_transform(ref.to_numpy(dtype=float))
    distances = []
    for row in target_clr:
        distances.append(float(np.linalg.norm(ref_clr - row, axis=1).min()))
    return pd.Series(distances, index=target.index, name="min_clr_distance_to_initial")


def try_write_figures(output_dir: Path, frames: dict[str, pd.DataFrame], novelty_tables: list[pd.DataFrame]) -> list[str]:
    written: list[str] = []
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return written

    figure_dir = output_dir / "figures"
    figure_dir.mkdir(parents=True, exist_ok=True)

    for name, frame in frames.items():
        if {"power_density", "normalized_cost"}.issubset(frame.columns):
            data = frame[["power_density", "normalized_cost"]].apply(pd.to_numeric, errors="coerce").dropna()
            if not data.empty:
                plt.figure(figsize=(7, 5))
                plt.scatter(data["normalized_cost"], data["power_density"], alpha=0.75)
                plt.xlabel("Normalized cost")
                plt.ylabel("Power density")
                plt.title(f"Power Density vs Cost - {name}")
                path = figure_dir / f"power_density_vs_cost_{name}_round1.png"
                plt.tight_layout()
                plt.savefig(path, dpi=160)
                plt.close()
                written.append(str(path))
        if "power_density" in frame.columns:
            values = numeric_series(frame, "power_density")
            if not values.empty:
                plt.figure(figsize=(7, 5))
                plt.hist(values, bins=min(20, max(5, len(values) // 5)), alpha=0.8)
                plt.xlabel("Power density")
                plt.ylabel("Count")
                plt.title(f"Power Density Distribution - {name}")
                path = figure_dir / f"power_density_distribution_{name}_round1.png"
                plt.tight_layout()
                plt.savefig(path, dpi=160)
                plt.close()
                written.append(str(path))

    if novelty_tables:
        combined = pd.concat(novelty_tables, ignore_index=True)
        if "min_clr_distance_to_initial" in combined.columns:
            values = pd.to_numeric(combined["min_clr_distance_to_initial"], errors="coerce").dropna()
            if not values.empty:
                plt.figure(figsize=(7, 5))
                plt.hist(values, bins=min(20, max(5, len(values) // 5)), alpha=0.8)
                plt.xlabel("Minimum CLR distance to initial examples")
                plt.ylabel("Count")
                plt.title("Candidate Novelty Distribution")
                path = figure_dir / "novelty_distribution_round1.png"
                plt.tight_layout()
                plt.savefig(path, dpi=160)
                plt.close()
                written.append(str(path))
    return written


def main() -> None:
    args = parse_args()
    output_dir = args.output_dir
    table_dir = output_dir / "tables"
    table_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "figures").mkdir(parents=True, exist_ok=True)

    artifact_paths = {
        "initial_examples": args.al_root / "data" / "initial_examples.csv",
        "oracle_training_sample": args.al_root / "data" / "oracle_training_sample.csv",
        "total_pool": args.al_root / "outputs" / "total_pool.csv",
        "total_examples_pool": args.al_root / "outputs" / "total_examples_pool.csv",
        "iteration_log": args.al_root / "outputs" / "iteration_log.csv",
        "query_log": args.al_root / "outputs" / "query_log.csv",
        "generated_ratios": args.al_root / "outputs" / "generated_ratios.csv",
    }

    frames: dict[str, pd.DataFrame] = {}
    integrity_rows: list[dict[str, object]] = []
    summary_rows: list[dict[str, object]] = []

    for name, path in artifact_paths.items():
        frame = read_csv_if_exists(path)
        if frame is None:
            integrity_rows.append({"dataset": name, "path": str(path), "exists": False, "rows": 0})
            continue
        normalized = normalize_frame_schema(frame, name)
        frames[name] = normalized
        diagnostics = composition_diagnostics(normalized, args.composition_tolerance)
        integrity_rows.append(
            {
                "dataset": name,
                "path": str(path),
                "exists": True,
                "columns": ";".join(frame.columns),
                **diagnostics,
            }
        )
        for column in ("power_density", "normalized_cost", "llm_mean", "llm_std", "ucb_score"):
            summary = numeric_summary(normalized, name, column)
            if summary is not None:
                summary_rows.append(summary)

    pd.DataFrame(integrity_rows).to_csv(table_dir / "data_integrity_round1.csv", index=False)
    pd.DataFrame(summary_rows).to_csv(table_dir / "performance_summary_round1.csv", index=False)

    pareto_rows: list[pd.DataFrame] = []
    for name, frame in frames.items():
        if {"power_density", "normalized_cost"}.issubset(frame.columns):
            result = frame.copy()
            result["pareto_front"] = pareto_mask_max_power_min_cost(result)
            result["pareto_dataset"] = name
            pareto_rows.append(result[result["pareto_front"]].copy())
    if pareto_rows:
        pd.concat(pareto_rows, ignore_index=True).to_csv(
            table_dir / "pareto_candidates_round1.csv", index=False
        )
    else:
        pd.DataFrame(columns=["pareto_dataset", "pareto_front"]).to_csv(
            table_dir / "pareto_candidates_round1.csv", index=False
        )

    novelty_tables: list[pd.DataFrame] = []
    reference = frames.get("initial_examples")
    if reference is not None:
        for name, frame in frames.items():
            if name == "initial_examples":
                continue
            novelty = novelty_against_reference(frame, reference)
            if novelty is None:
                continue
            table = pd.DataFrame(
                {
                    "dataset": name,
                    "row_index": novelty.index,
                    "min_clr_distance_to_initial": novelty.to_numpy(dtype=float),
                }
            )
            novelty_tables.append(table)
    if novelty_tables:
        novelty_combined = pd.concat(novelty_tables, ignore_index=True)
        novelty_summary = (
            novelty_combined.groupby("dataset")["min_clr_distance_to_initial"]
            .agg(["count", "min", "median", "mean", "max"])
            .reset_index()
        )
        novelty_summary.to_csv(table_dir / "novelty_summary_round1.csv", index=False)
        novelty_combined.to_csv(table_dir / "novelty_by_candidate_round1.csv", index=False)
    else:
        pd.DataFrame(
            columns=["dataset", "count", "min", "median", "mean", "max"]
        ).to_csv(table_dir / "novelty_summary_round1.csv", index=False)

    figures = try_write_figures(output_dir, frames, novelty_tables)
    manifest = {
        "round": "round1",
        "al_root": str(args.al_root),
        "output_dir": str(output_dir),
        "tables": sorted(str(path) for path in table_dir.glob("*_round1.csv")),
        "figures": figures,
        "raw_outputs_modified": False,
        "al_pipeline_executed": False,
    }
    (output_dir / "tables" / "evaluation_manifest_round1.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
