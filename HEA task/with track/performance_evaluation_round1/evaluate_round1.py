#!/usr/bin/env python3
"""Validate and summarize a supplied HEA evaluation CSV, then write exploratory plots.

This tool does not run the AL model, train predictors, call APIs, or infer missing
conditions. It refuses to treat predicted/virtual rows as experimental results.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


MASS_ORDER = ("Pd", "Pt", "Au", "Cr", "Ir", "Ce", "Cu", "Nb")
REQUIRED = {
    *MASS_ORDER,
    "candidate_id",
    "run_id",
    "value_type",
    "peak_power_density",
    "power_unit",
    "area_basis",
    "protocol_id",
    "device_id",
}
ALLOWED_VALUE_TYPES = {"measured", "predicted", "derived", "reported_literature", "simulated"}
CONDITION_GROUP = ["protocol_id", "device_id", "power_unit", "area_basis"]


def validate_frame(frame: pd.DataFrame, closure_tolerance: float) -> tuple[pd.DataFrame, dict[str, Any]]:
    missing_columns = sorted(REQUIRED - set(frame.columns))
    if missing_columns:
        raise ValueError(f"Required columns missing: {missing_columns}")
    if frame.empty:
        raise ValueError("Input contains no rows")

    if not np.isfinite(closure_tolerance) or closure_tolerance < 0:
        raise ValueError("closure_tolerance must be a finite nonnegative value supplied by the approved assay/reporting protocol")
    data = frame.copy()
    for column in ("candidate_id", "run_id", "value_type", *CONDITION_GROUP):
        data[column] = data[column].replace(r"^\s*$", pd.NA, regex=True)
    for column in MASS_ORDER + ("peak_power_density",):
        data[column] = pd.to_numeric(data[column], errors="coerce")
    data["value_type"] = data["value_type"].astype("string").str.strip().str.lower()

    issues: list[dict[str, Any]] = []
    invalid_value_type = ~data["value_type"].isin(ALLOWED_VALUE_TYPES)
    if invalid_value_type.any():
        issues.append({"check": "value_type", "count": int(invalid_value_type.sum()), "action": "flagged"})

    missing_numeric = data[list(MASS_ORDER) + ["peak_power_density"]].isna().any(axis=1)
    if missing_numeric.any():
        issues.append({"check": "numeric_missing_or_non_numeric", "count": int(missing_numeric.sum()), "action": "excluded_from_numeric_summaries"})

    negative = (data[list(MASS_ORDER)] < 0).any(axis=1)
    greater_one = (data[list(MASS_ORDER)] > 1).any(axis=1)
    sums = data[list(MASS_ORDER)].sum(axis=1, min_count=len(MASS_ORDER))
    closure_error = (sums - 1.0).abs()
    closure_fail = closure_error > closure_tolerance
    if negative.any():
        issues.append({"check": "negative_mass_fraction", "count": int(negative.sum()), "action": "flagged"})
    if greater_one.any():
        issues.append({"check": "mass_fraction_gt_one", "count": int(greater_one.sum()), "action": "flagged"})
    negative_power = data["peak_power_density"] < 0
    if negative_power.any():
        issues.append({"check": "negative_peak_power_density", "count": int(negative_power.sum()), "action": "flagged"})
    if closure_fail.any():
        issues.append({"check": "closure_abs_error_gt_approved_tolerance", "count": int(closure_fail.sum()), "tolerance": closure_tolerance, "action": "flagged_no_auto_renormalization"})

    duplicate_run = data.duplicated(["candidate_id", "run_id"], keep=False)
    if duplicate_run.any():
        issues.append({"check": "duplicate_candidate_run", "count": int(duplicate_run.sum()), "action": "review_replicate_or_duplicate_id"})

    missing_conditions = data[["candidate_id", "run_id", *CONDITION_GROUP]].isna().any(axis=1)
    if missing_conditions.any():
        issues.append({"check": "missing_device_protocol_metadata", "count": int(missing_conditions.sum()), "action": "not_comparable_without_review"})

    eligible = (
        ~missing_numeric
        & ~invalid_value_type
        & ~negative
        & ~greater_one
        & ~negative_power
        & ~closure_fail
        & ~missing_conditions
    )
    data["closure_sum"] = sums
    data["closure_abs_error"] = closure_error
    data["evaluation_eligible"] = eligible
    data["is_measured"] = data["value_type"].eq("measured")

    type_counts = data["value_type"].value_counts(dropna=False).to_dict()
    report = {
        "row_count": int(len(data)),
        "eligible_count": int(eligible.sum()),
        "measured_count": int(data["is_measured"].sum()),
        "value_type_counts": {str(key): int(value) for key, value in type_counts.items()},
        "mass_fraction_order": list(MASS_ORDER),
        "closure_tolerance_used_for_script_check": closure_tolerance,
        "tolerance_source": "explicit CLI argument; must be taken from approved assay/reporting protocol",
        "issues": issues,
    }
    return data, report


def bootstrap_ci(values: np.ndarray, rng: np.random.Generator, iterations: int = 5000) -> list[float] | None:
    clean = np.asarray(values, dtype=float)
    clean = clean[np.isfinite(clean)]
    if clean.size < 2:
        return None
    samples = rng.choice(clean, size=(iterations, clean.size), replace=True).mean(axis=1)
    lo, hi = np.quantile(samples, [0.025, 0.975])
    return [float(lo), float(hi)]


def summarize(data: pd.DataFrame, seed: int = 2026) -> dict[str, Any]:
    eligible = data[data["evaluation_eligible"]].copy()
    measured = eligible[eligible["is_measured"]].copy()
    rng = np.random.default_rng(seed)
    summaries: dict[str, Any] = {
        "eligible_rows": int(len(eligible)),
        "measured_rows": int(len(measured)),
        "measured_power_summary": None,
        "candidate_aggregate": None,
        "prediction_evaluation": None,
        "pareto_candidate_count": None,
    }

    if not measured.empty:
        y = measured["peak_power_density"].to_numpy(dtype=float)
        summaries["measured_power_summary"] = {
            "n": int(y.size),
            "mean": float(np.mean(y)),
            "median": float(np.median(y)),
            "sd": float(np.std(y, ddof=1)) if y.size > 1 else None,
            "min": float(np.min(y)),
            "max": float(np.max(y)),
            "mean_bootstrap_95ci": bootstrap_ci(y, rng),
            "unit_values": sorted(measured["power_unit"].dropna().astype(str).unique().tolist()),
            "area_basis_values": sorted(measured["area_basis"].dropna().astype(str).unique().tolist()),
        }
        summaries["condition_strata"] = []
        for key, group in measured.groupby(CONDITION_GROUP, dropna=False):
            group_y = group["peak_power_density"].to_numpy(dtype=float)
            summaries["condition_strata"].append({
                "conditions": dict(zip(CONDITION_GROUP, [str(value) for value in key])),
                "n": int(group_y.size),
                "mean": float(group_y.mean()),
                "median": float(np.median(group_y)),
                "sd": float(np.std(group_y, ddof=1)) if group_y.size > 1 else None,
                "mean_bootstrap_95ci": bootstrap_ci(group_y, rng),
            })
        group = measured.groupby("candidate_id", dropna=False)["peak_power_density"]
        aggregate = group.agg(["count", "mean", "std", "min", "max"]).reset_index()
        aggregate["cv"] = aggregate["std"] / aggregate["mean"].abs().replace(0, np.nan)
        summaries["candidate_aggregate"] = aggregate.to_dict(orient="records")
        summaries["replicate_stability"] = {
            "metric": "within-candidate SD and CV of measured peak power, stratified by protocol/device/unit/area",
            "candidates_with_replicates": int((aggregate["count"] >= 2).sum()),
            "candidates_without_replicates": int((aggregate["count"] < 2).sum()),
            "values": aggregate.loc[aggregate["count"] >= 2, ["candidate_id", "count", "mean", "std", "cv"]].replace({np.nan: None}).to_dict(orient="records"),
            "warning": "This is repeatability under recorded conditions, not long-term electrochemical durability. No acceptance threshold is set.",
        }
        if {"predicted_power_density", "prediction_model_id"}.issubset(measured.columns):
            pred = pd.to_numeric(measured["predicted_power_density"], errors="coerce")
            valid = pred.notna()
            if valid.sum() >= 2:
                err = pred[valid].to_numpy() - measured.loc[valid, "peak_power_density"].to_numpy()
                obs = measured.loc[valid, "peak_power_density"].to_numpy()
                summaries["prediction_evaluation"] = {
                    "n": int(valid.sum()),
                    "mae": float(np.mean(np.abs(err))),
                    "rmse": float(np.sqrt(np.mean(err**2))),
                    "r2": float(1 - np.sum(err**2) / np.sum((obs - obs.mean()) ** 2)) if np.var(obs) > 0 else None,
                    "warning": "Evaluate only genuinely held-out measured records; predictions must be generated without target leakage.",
                }
                if {"prediction_lower", "prediction_upper"}.issubset(measured.columns):
                    lower = pd.to_numeric(measured.loc[valid, "prediction_lower"], errors="coerce")
                    upper = pd.to_numeric(measured.loc[valid, "prediction_upper"], errors="coerce")
                    interval_ok = lower.notna() & upper.notna()
                    if interval_ok.any():
                        observed_values = measured.loc[valid, "peak_power_density"].to_numpy(dtype=float)
                        low_values = lower.to_numpy(dtype=float)
                        high_values = upper.to_numpy(dtype=float)
                        interval_mask = interval_ok.to_numpy()
                        summaries["prediction_evaluation"]["interval_coverage"] = float(
                            ((observed_values[interval_mask] >= low_values[interval_mask])
                             & (observed_values[interval_mask] <= high_values[interval_mask])).mean()
                        )
                        summaries["prediction_evaluation"]["mean_interval_width"] = float(
                            (high_values[interval_mask] - low_values[interval_mask]).mean()
                        )

    if {"actual_cost", "cost_unit"}.issubset(eligible.columns) and not eligible.empty:
        cost = pd.to_numeric(eligible["actual_cost"], errors="coerce")
        power = eligible["peak_power_density"]
        valid = cost.notna() & power.notna() & eligible["is_measured"]
        if valid.sum():
            xy = pd.DataFrame({"power": power[valid], "cost": cost[valid], "candidate_id": eligible.loc[valid, "candidate_id"]})
            nondominated = np.ones(len(xy), dtype=bool)
            values = xy[["power", "cost"]].to_numpy()
            # Maximize power, minimize cost; retain nondominated measured candidates.
            for i, (p_i, c_i) in enumerate(values):
                dominates = (values[:, 0] >= p_i) & (values[:, 1] <= c_i) & ((values[:, 0] > p_i) | (values[:, 1] < c_i))
                if dominates.any():
                    nondominated[i] = False
            summaries["pareto_candidate_count"] = int(nondominated.sum())

    return summaries


def make_plots(data: pd.DataFrame, output_dir: Path) -> list[str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: list[str] = []
    eligible = data[data["evaluation_eligible"]].copy()
    measured = eligible[eligible["is_measured"]].copy()
    if measured.empty:
        return outputs

    for group_index, (key, condition_data) in enumerate(measured.groupby(CONDITION_GROUP, dropna=False), start=1):
        by_candidate = condition_data.groupby("candidate_id")["peak_power_density"]
        means = by_candidate.mean().sort_values(ascending=False)
        errors = by_candidate.std().reindex(means.index)
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(means.index.astype(str), means.values, yerr=errors.fillna(0).values, capsize=3)
        ax.set_ylabel(f"Peak power density ({condition_data['power_unit'].iloc[0]})")
        ax.set_xlabel("Candidate ID")
        ax.set_title(f"Measured peak power by candidate; condition stratum {group_index}")
        ax.tick_params(axis="x", rotation=60)
        fig.tight_layout()
        path = output_dir / f"measured_power_by_candidate_round1_stratum_{group_index}.png"
        fig.savefig(path, dpi=160)
        plt.close(fig)
        outputs.append(str(path))

    if {"iteration", "peak_power_density"}.issubset(measured.columns):
        for group_index, (key, condition_data) in enumerate(measured.groupby(CONDITION_GROUP, dropna=False), start=1):
            if condition_data["iteration"].nunique() < 1:
                continue
            iter_stats = condition_data.groupby("iteration")["peak_power_density"].agg(["mean", "std", "max"])
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(iter_stats.index, iter_stats["max"], marker="o", label="Best measured this round")
            ax.plot(iter_stats.index, iter_stats["mean"], marker="s", label="Mean measured")
            if iter_stats["std"].notna().any():
                ax.fill_between(iter_stats.index, iter_stats["mean"]-iter_stats["std"], iter_stats["mean"]+iter_stats["std"], alpha=0.2, label="±1 SD")
            ax.set_xlabel("Iteration")
            ax.set_ylabel(f"Peak power density ({condition_data['power_unit'].iloc[0]})")
            ax.set_title(f"Measured performance by iteration; condition stratum {group_index}")
            ax.legend()
            fig.tight_layout()
            path = output_dir / f"measured_performance_by_iteration_round1_stratum_{group_index}.png"
            fig.savefig(path, dpi=160)
            plt.close(fig)
            outputs.append(str(path))

    fig, ax = plt.subplots(figsize=(9, 5))
    composition_means = measured.groupby("candidate_id")[list(MASS_ORDER)].mean()
    if not composition_means.empty:
        image = ax.imshow(composition_means.to_numpy(), aspect="auto", interpolation="nearest", vmin=0, vmax=1)
        ax.set_xticks(np.arange(len(MASS_ORDER)), MASS_ORDER)
        ax.set_yticks(np.arange(len(composition_means)), composition_means.index.astype(str))
        ax.set_xlabel("Mass-fraction component (canonical order)")
        ax.set_ylabel("Candidate ID")
        ax.set_title("Measured candidate composition matrix")
        fig.colorbar(image, ax=ax, label="Mass fraction")
        fig.tight_layout()
        path = output_dir / "candidate_composition_matrix_round1.png"
        fig.savefig(path, dpi=160)
        plt.close(fig)
        outputs.append(str(path))

    if {"predicted_power_density", "prediction_model_id"}.issubset(measured.columns):
        predicted = pd.to_numeric(measured["predicted_power_density"], errors="coerce")
        valid = predicted.notna()
        if valid.any():
            fig, ax = plt.subplots(figsize=(6, 6))
            observed = measured.loc[valid, "peak_power_density"].to_numpy(dtype=float)
            pred = predicted[valid].to_numpy(dtype=float)
            ax.scatter(observed, pred)
            lo = float(min(observed.min(), pred.min()))
            hi = float(max(observed.max(), pred.max()))
            ax.plot([lo, hi], [lo, hi], linestyle="--", color="black", linewidth=1)
            ax.set_xlabel(f"Measured peak power ({measured.loc[valid, 'power_unit'].iloc[0]})")
            ax.set_ylabel("Predicted peak power (same declared unit)")
            ax.set_title("Held-out prediction vs measurement")
            fig.tight_layout()
            path = output_dir / "prediction_vs_measurement_round1.png"
            fig.savefig(path, dpi=160)
            plt.close(fig)
            outputs.append(str(path))

    if {"actual_cost", "cost_unit"}.issubset(measured.columns):
        cost = pd.to_numeric(measured["actual_cost"], errors="coerce")
        valid = cost.notna()
        if valid.any():
            for group_index, (key, condition_data) in enumerate(measured.loc[valid].groupby(CONDITION_GROUP, dropna=False), start=1):
                fig, ax = plt.subplots(figsize=(7, 5))
                group_cost = pd.to_numeric(condition_data["actual_cost"], errors="coerce")
                ax.scatter(group_cost, condition_data["peak_power_density"])
                ax.set_xlabel(f"Actual cost ({condition_data['cost_unit'].iloc[0]})")
                ax.set_ylabel(f"Peak power density ({condition_data['power_unit'].iloc[0]})")
                ax.set_title(f"Measured power–cost trade-off; condition stratum {group_index}")
                fig.tight_layout()
                path = output_dir / f"measured_power_cost_tradeoff_round1_stratum_{group_index}.png"
                fig.savefig(path, dpi=160)
                plt.close(fig)
                outputs.append(str(path))
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Explicit evaluation CSV; no default AL file is consumed")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--closure-tolerance", type=float, required=True, help="Expert-approved assay/reporting tolerance for mass fractions")
    parser.add_argument("--allow-nonmeasured", action="store_true", help="Retain non-measured rows in QA report; they are still excluded from measured performance statistics")
    args = parser.parse_args()

    if not args.input.is_file():
        raise FileNotFoundError(args.input)
    frame = pd.read_csv(args.input)
    checked, qa = validate_frame(frame, args.closure_tolerance)
    if not args.allow_nonmeasured and not checked["value_type"].eq("measured").all():
        raise ValueError("Input contains non-measured value_type rows; separate prediction/virtual results or pass --allow-nonmeasured for QA-only inclusion.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    checked.to_csv(args.output_dir / "validated_records_round1.csv", index=False)
    summary = summarize(checked)
    summary["input_file"] = str(args.input.resolve())
    summary["value_type_counts"] = qa["value_type_counts"]
    summary["data_quality_issues"] = qa["issues"]
    summary["interpretation_status"] = "exploratory; verify device conditions and expert thresholds before decision use"
    with (args.output_dir / "evaluation_summary_round1.json").open("w", encoding="utf-8") as handle:
        json.dump(summary, handle, indent=2, ensure_ascii=False)
    plots = make_plots(checked, args.output_dir / "figures")
    print(json.dumps({"summary": str(args.output_dir / 'evaluation_summary_round1.json'), "plots": plots, "eligible": qa['eligible_count'], "issues": qa['issues']}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
