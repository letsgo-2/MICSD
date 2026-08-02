from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

import numpy as np
import pandas as pd
from numpy.typing import NDArray


METAL_ORDER = ("Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Round 2 statistics and plots for catalyst AL total_pool.csv."
    )
    _ = parser.add_argument(
        "--total-pool",
        type=Path,
        default=Path("AL/catalyst_active_learning_runnable/outputs/total_pool.csv"),
        help="Path to total_pool.csv treated as one experimental iteration process.",
    )
    _ = parser.add_argument(
        "--initial-size",
        type=int,
        default=10,
        help="Number of initial rows before generated/iterative candidates.",
    )
    _ = parser.add_argument(
        "--num-iterations",
        type=int,
        default=10,
        help="Number of process stages used to infer iteration groups after initial rows.",
    )
    _ = parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("performance_evaluation_round2"),
        help="Directory for derived round2 outputs.",
    )
    return parser.parse_args()


def parse_ratio(value: object) -> list[float]:
    parsed = ast.literal_eval(str(value))
    if not isinstance(parsed, list) or len(parsed) != len(METAL_ORDER):
        raise ValueError(f"Expected an eight-element ratio vector, got: {value!r}")
    return [float(item) for item in parsed]


def load_total_pool(path: Path, initial_size: int, num_iterations: int) -> pd.DataFrame:
    frame = pd.read_csv(path)
    required = {"id", "ratio", "power_density", "normalized_cost"}
    missing = sorted(required.difference(frame.columns))
    if missing:
        raise ValueError(f"{path} is missing required columns: {missing}")

    ratios = frame["ratio"].map(parse_ratio)
    expanded = pd.DataFrame(ratios.to_list())
    expanded.columns = list(METAL_ORDER)
    result = pd.concat([frame.drop(columns=["ratio"]).copy(), expanded], axis=1)
    result["process_index"] = np.arange(1, len(result) + 1)

    generated_count = max(len(result) - initial_size, 0)
    if generated_count and num_iterations > 0:
        per_iteration = generated_count / num_iterations
        inferred = []
        for index in range(len(result)):
            if index < initial_size:
                inferred.append(0)
            else:
                inferred.append(int((index - initial_size) // per_iteration) + 1)
        result["inferred_iteration"] = np.minimum(inferred, num_iterations)
    else:
        result["inferred_iteration"] = 0

    result["stage"] = np.where(result["inferred_iteration"] == 0, "initial", "iterative")
    result["power_density"] = pd.to_numeric(result["power_density"], errors="raise")
    result["normalized_cost"] = pd.to_numeric(result["normalized_cost"], errors="raise")
    metal_columns = list(METAL_ORDER)
    result["composition_sum"] = result.loc[:, metal_columns].sum(axis=1)
    result["composition_valid"] = (
        np.isfinite(result.loc[:, metal_columns].to_numpy(dtype=float)).all(axis=1)
        & (result.loc[:, metal_columns] >= 0).all(axis=1)
        & np.isclose(result["composition_sum"], 1.0, atol=1e-6)
    )
    return result


def pareto_mask(frame: pd.DataFrame) -> NDArray[np.bool_]:
    points = frame[["power_density", "normalized_cost"]].to_numpy(dtype=float)
    mask = np.ones(len(points), dtype=bool)
    for index, point in enumerate(points):
        dominated = (
            (points[:, 0] >= point[0])
            & (points[:, 1] <= point[1])
            & ((points[:, 0] > point[0]) | (points[:, 1] < point[1]))
        )
        if np.any(dominated):
            mask[index] = False
    return mask


def write_tables(frame: pd.DataFrame, output_dir: Path) -> dict[str, object]:
    table_dir = output_dir / "tables"
    table_dir.mkdir(parents=True, exist_ok=True)

    high_threshold = float(frame["power_density"].quantile(0.90))
    high = frame.loc[frame["power_density"] >= high_threshold].copy()
    frame = frame.copy()
    frame["high_performance_top10pct"] = frame["power_density"] >= high_threshold
    frame["pareto_front"] = pareto_mask(frame)

    expanded_path = table_dir / "total_pool_expanded_round2.csv"
    frame.to_csv(expanded_path, index=False)

    composition_summary = frame.loc[:, METAL_ORDER].agg(["mean", "std", "min", "median", "max"]).T
    composition_summary["high_performance_mean"] = high.loc[:, METAL_ORDER].mean(axis=0)
    composition_summary["high_minus_all_mean"] = (
        composition_summary["high_performance_mean"] - composition_summary["mean"]
    )
    composition_summary = composition_summary.reset_index(names="metal")
    composition_summary_path = table_dir / "composition_distribution_summary_round2.csv"
    composition_summary.to_csv(composition_summary_path, index=False)

    perf_summary = pd.DataFrame(
        [
            {
                "metric": metric,
                "count": int(frame[metric].count()),
                "min": float(frame[metric].min()),
                "p25": float(frame[metric].quantile(0.25)),
                "median": float(frame[metric].median()),
                "mean": float(frame[metric].mean()),
                "p75": float(frame[metric].quantile(0.75)),
                "p90": float(frame[metric].quantile(0.90)),
                "max": float(frame[metric].max()),
            }
            for metric in ("power_density", "normalized_cost")
        ]
    )
    perf_summary_path = table_dir / "performance_cost_summary_round2.csv"
    perf_summary.to_csv(perf_summary_path, index=False)

    iteration_summary = (
        frame.groupby("inferred_iteration")
        .agg(
            rows=("id", "count"),
            stage=("stage", "first"),
            power_density_mean=("power_density", "mean"),
            power_density_max=("power_density", "max"),
            normalized_cost_mean=("normalized_cost", "mean"),
            normalized_cost_min=("normalized_cost", "min"),
            high_performance_count=("high_performance_top10pct", "sum"),
            pareto_count=("pareto_front", "sum"),
        )
        .reset_index()
    )
    iteration_summary_path = table_dir / "iteration_process_summary_round2.csv"
    iteration_summary.to_csv(iteration_summary_path, index=False)

    cumulative_best = frame[["process_index", "id", "inferred_iteration", "power_density", "normalized_cost"]].copy()
    cumulative_best["cumulative_best_power_density"] = np.maximum.accumulate(
        np.asarray(cumulative_best["power_density"], dtype=float)
    )
    cumulative_best["is_new_best"] = cumulative_best["power_density"] == cumulative_best[
        "cumulative_best_power_density"
    ]
    cumulative_best_path = table_dir / "cumulative_best_process_round2.csv"
    cumulative_best.to_csv(cumulative_best_path, index=False)

    high_path = table_dir / "high_performance_formulations_round2.csv"
    high.sort_values("power_density", ascending=False).to_csv(high_path, index=False)

    feature_summary = pd.DataFrame(
        {
            "metal": METAL_ORDER,
            "all_mean": [float(frame[metal].mean()) for metal in METAL_ORDER],
            "high_performance_mean": [float(high[metal].mean()) for metal in METAL_ORDER],
            "top_candidate_fraction": [
                float(frame.loc[frame["power_density"].idxmax(), metal]) for metal in METAL_ORDER
            ],
        }
    )
    feature_summary["high_minus_all_mean"] = (
        feature_summary["high_performance_mean"] - feature_summary["all_mean"]
    )
    feature_path = table_dir / "high_performance_composition_features_round2.csv"
    feature_summary.to_csv(feature_path, index=False)

    pareto_path = table_dir / "pareto_front_candidates_round2.csv"
    frame.loc[frame["pareto_front"]].sort_values(
        ["power_density", "normalized_cost"], ascending=[False, True]
    ).to_csv(pareto_path, index=False)

    accuracy_status = pd.DataFrame(
        [
            {
                "item": "prediction_model_accuracy",
                "status": "not_available_from_total_pool_csv",
                "reason": "total_pool.csv contains power_density and normalized_cost only; no prediction, ground-truth split, residual, query_log, or saved oracle metrics are present.",
                "available_code_path": "AL/catalyst_active_learning_runnable/catalyst_al/model.py can report test_r2, test_rmse, and test_mae when train_oracle is executed, but this evaluation did not train or run the model.",
            }
        ]
    )
    accuracy_path = table_dir / "prediction_model_accuracy_status_round2.csv"
    accuracy_status.to_csv(accuracy_path, index=False)

    top = frame.loc[frame["power_density"].idxmax()].to_dict()
    low_cost_high = frame.loc[
        (frame["power_density"] >= high_threshold)
        & (frame["normalized_cost"] <= frame["normalized_cost"].median())
    ].copy()

    return {
        "paths": {
            "expanded": str(expanded_path),
            "composition_summary": str(composition_summary_path),
            "performance_summary": str(perf_summary_path),
            "iteration_summary": str(iteration_summary_path),
            "cumulative_best": str(cumulative_best_path),
            "high_performance_formulations": str(high_path),
            "high_performance_features": str(feature_path),
            "pareto_front": str(pareto_path),
            "prediction_accuracy_status": str(accuracy_path),
        },
        "summary": {
            "row_count": int(len(frame)),
            "composition_valid_rows": int(frame["composition_valid"].sum()),
            "high_performance_threshold_top10pct": high_threshold,
            "high_performance_count": int(len(high)),
            "low_cost_high_performance_count": int(len(low_cost_high)),
            "pareto_count": int(frame["pareto_front"].sum()),
            "best_candidate": {
                "id": int(top["id"]),
                "process_index": int(top["process_index"]),
                "inferred_iteration": int(top["inferred_iteration"]),
                "power_density": float(top["power_density"]),
                "normalized_cost": float(top["normalized_cost"]),
                "composition": {metal: float(top[metal]) for metal in METAL_ORDER},
            },
            "dominant_high_performance_metals": feature_summary.sort_values(
                "high_performance_mean", ascending=False
            )["metal"].head(4).to_list(),
            "enriched_high_performance_metals": feature_summary.sort_values(
                "high_minus_all_mean", ascending=False
            )["metal"].head(4).to_list(),
        },
    }


def write_figures(frame: pd.DataFrame, output_dir: Path) -> dict[str, str]:
    import matplotlib.pyplot as plt

    figure_dir = output_dir / "figures"
    figure_dir.mkdir(parents=True, exist_ok=True)
    paths: dict[str, str] = {}

    plt.figure(figsize=(9, 5))
    frame.loc[:, METAL_ORDER].boxplot(rot=0)
    plt.ylabel("Mass fraction")
    plt.title("Eight-Metal Composition Distribution")
    path = figure_dir / "eight_metal_composition_distribution_round2.png"
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()
    paths["composition_distribution"] = str(path)

    plt.figure(figsize=(9, 5))
    for metal in METAL_ORDER:
        plt.plot(frame["process_index"], frame[metal], linewidth=1.0, label=metal)
    plt.xlabel("Process index from total_pool.csv")
    plt.ylabel("Mass fraction")
    plt.title("Composition Trajectory Across the Iteration Process")
    plt.legend(ncol=4, fontsize=8)
    path = figure_dir / "composition_trajectory_round2.png"
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()
    paths["composition_trajectory"] = str(path)

    plt.figure(figsize=(8, 5))
    scatter = plt.scatter(
        frame["normalized_cost"],
        frame["power_density"],
        c=frame["inferred_iteration"],
        cmap="viridis",
        alpha=0.8,
    )
    plt.xlabel("Normalized cost")
    plt.ylabel("Peak power density")
    plt.title("Peak Power Density vs Normalized Cost")
    plt.colorbar(scatter, label="Inferred iteration")
    path = figure_dir / "power_density_vs_normalized_cost_round2.png"
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()
    paths["power_density_vs_cost"] = str(path)

    cumulative = frame[["process_index", "power_density"]].copy()
    cumulative["cumulative_best_power_density"] = np.maximum.accumulate(
        np.asarray(cumulative["power_density"], dtype=float)
    )
    plt.figure(figsize=(9, 5))
    plt.plot(cumulative["process_index"], cumulative["power_density"], color="#7f8c8d", alpha=0.55, label="Candidate")
    plt.plot(cumulative["process_index"], cumulative["cumulative_best_power_density"], color="#c0392b", linewidth=2.0, label="Cumulative best")
    plt.xlabel("Process index from total_pool.csv")
    plt.ylabel("Peak power density")
    plt.title("Model Iteration Process: Candidate and Cumulative Best")
    plt.legend()
    path = figure_dir / "iteration_cumulative_best_power_density_round2.png"
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()
    paths["iteration_cumulative_best"] = str(path)

    high_threshold = float(frame["power_density"].quantile(0.90))
    high = frame.loc[frame["power_density"] >= high_threshold, METAL_ORDER]
    feature = pd.DataFrame(
        {
            "metal": METAL_ORDER,
            "all_mean": [frame[metal].mean() for metal in METAL_ORDER],
            "high_performance_mean": [high[metal].mean() for metal in METAL_ORDER],
        }
    )
    x = np.arange(len(METAL_ORDER))
    width = 0.38
    plt.figure(figsize=(9, 5))
    plt.bar(x - width / 2, feature["all_mean"], width=width, label="All candidates")
    plt.bar(x + width / 2, feature["high_performance_mean"], width=width, label="Top 10% power density")
    plt.xticks(x, METAL_ORDER)
    plt.ylabel("Mean mass fraction")
    plt.title("High-Performance Composition Features")
    plt.legend()
    path = figure_dir / "high_performance_composition_features_round2.png"
    plt.tight_layout()
    plt.savefig(path, dpi=180)
    plt.close()
    paths["high_performance_features"] = str(path)

    return paths


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    frame = load_total_pool(args.total_pool, args.initial_size, args.num_iterations)
    table_info = write_tables(frame, args.output_dir)
    figure_paths = write_figures(frame, args.output_dir)
    manifest = {
        "source_total_pool": str(args.total_pool),
        "round": "round2",
        "raw_outputs_modified": False,
        "al_model_executed": False,
        "iteration_inference": "Rows after the initial_size are divided into num_iterations equal stages for analysis because total_pool.csv has no explicit iteration column.",
        "tables": table_info["paths"],
        "figures": figure_paths,
        "summary": table_info["summary"],
    }
    manifest_path = args.output_dir / "tables" / "analysis_manifest_round2.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
