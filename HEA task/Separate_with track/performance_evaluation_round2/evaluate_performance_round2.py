#!/usr/bin/env python3
"""Round2 composition, performance, cost, process, and model diagnostics."""
from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_predict, train_test_split


ROOT = Path(__file__).resolve().parents[1]
AL_ROOT = ROOT / "AL" / "catalyst_active_learning_runnable"
OUT = Path(__file__).resolve().parent
AL_ORDER = ["Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr"]
PROJECT_ORDER = ["Pd", "Pt", "Au", "Cr", "Ir", "Ce", "Cu", "Nb"]
PD_API: Any = pd


def describe(series: Any) -> dict[str, Any]:
    values = PD_API.to_numeric(series, errors="coerce").dropna()
    return {
        "n": int(values.size),
        "mean": float(values.mean()),
        "std_sample": float(values.std(ddof=1)) if len(values) > 1 else None,
        "median": float(values.median()),
        "q25": float(values.quantile(0.25)),
        "q75": float(values.quantile(0.75)),
        "min": float(values.min()),
        "max": float(values.max()),
    }


def metric_bundle(y_true: Any, y_pred: Any) -> dict[str, float]:
    return {
        "n": int(len(y_true)),
        "r2": float(r2_score(y_true, y_pred)),
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "pearson_r": float(np.corrcoef(y_true, y_pred)[0, 1]),
        "spearman_r": float(pd.Series(y_true).corr(pd.Series(y_pred), method="spearman")),
        "mean_signed_error": float(np.mean(y_pred - y_true)),
    }


def fit_model() -> tuple[dict[str, Any], Any]:
    data = PD_API.read_csv(AL_ROOT / "data" / "oracle_training_sample.csv")
    x = data[AL_ORDER].to_numpy(dtype=float)
    y = data["power_density"].to_numpy(dtype=float)
    model_config = {"n_estimators": 512, "learning_rate": 0.03, "max_depth": 3, "loss": "squared_error", "random_state": 42}
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)
    holdout = GradientBoostingRegressor(n_estimators=512, learning_rate=0.03, max_depth=3, loss="squared_error", random_state=42)
    holdout.fit(train_x, train_y)
    holdout_pred = holdout.predict(test_x)
    kfold = KFold(n_splits=5, shuffle=True, random_state=42)
    cv_model = GradientBoostingRegressor(n_estimators=512, learning_rate=0.03, max_depth=3, loss="squared_error", random_state=42)
    cv_pred = cross_val_predict(cv_model, x, y, cv=kfold)
    metrics = {
        "training_rows": int(len(y)),
        "model": "GradientBoostingRegressor",
        "configuration": model_config,
        "random_split_holdout": metric_bundle(test_y, holdout_pred),
        "five_fold_cross_validated": metric_bundle(y, cv_pred),
        "interpretation": "virtual-oracle accuracy on supplied training data; not experimental predictive validity",
    }
    predictions = PD_API.DataFrame({"observed_power_density": y, "cv_predicted_power_density": cv_pred, "residual": cv_pred - y})
    return metrics, predictions


def main() -> None:
    pool = PD_API.read_csv(AL_ROOT / "outputs" / "total_pool.csv")
    pool["ratio_values"] = pool["ratio"].map(ast.literal_eval)
    ratios = PD_API.DataFrame(pool["ratio_values"].tolist(), columns=AL_ORDER)
    pool = PD_API.concat([pool.drop(columns=["ratio_values"]), ratios], axis=1)
    pool["composition_sum"] = pool[AL_ORDER].sum(axis=1)
    pool["closure_error"] = (pool["composition_sum"] - 1.0).abs()
    pool["nonzero_elements"] = (pool[AL_ORDER] > 0).sum(axis=1)
    pool["is_octanary_strict"] = pool["nonzero_elements"] == 8
    pool["is_high_performance"] = pool["power_density"] >= pool["power_density"].quantile(0.90)
    pool["is_top5"] = pool["power_density"] >= pool["power_density"].nlargest(min(5, len(pool))).min()
    pool["pool_phase"] = np.where(pool["id"] <= 10, "seed_or_baseline_rows", "generated_or_retained_rows")

    high = pool.loc[pool["is_high_performance"]].copy()
    top5 = pool.loc[pool["is_top5"]].copy()
    element_stats = PD_API.DataFrame({
        "element": AL_ORDER,
        "pool_mean_fraction": [pool[e].mean() for e in AL_ORDER],
        "pool_median_fraction": [pool[e].median() for e in AL_ORDER],
        "pool_nonzero_rate": [(pool[e] > 0).mean() for e in AL_ORDER],
        "high_performance_mean_fraction": [high[e].mean() for e in AL_ORDER],
        "high_performance_median_fraction": [high[e].median() for e in AL_ORDER],
        "top5_mean_fraction": [top5[e].mean() for e in AL_ORDER],
        "mean_difference_high_minus_pool": [high[e].mean() - pool[e].mean() for e in AL_ORDER],
    })
    element_stats.to_csv(OUT / "composition_high_performance_stats_round2.csv", index=False)
    pool.to_csv(OUT / "pool_annotated_round2.csv", index=False)
    high.to_csv(OUT / "high_performance_formulations_round2.csv", index=False)
    top5.to_csv(OUT / "top5_virtual_formulations_round2.csv", index=False)

    phase = pool.groupby("pool_phase", as_index=False).agg(
        rows=("id", "count"),
        mean_power_density=("power_density", "mean"),
        median_power_density=("power_density", "median"),
        max_power_density=("power_density", "max"),
        mean_normalized_cost=("normalized_cost", "mean"),
        median_normalized_cost=("normalized_cost", "median"),
        mean_nonzero_elements=("nonzero_elements", "mean"),
    )
    phase.to_csv(OUT / "process_phase_summary_round2.csv", index=False)

    model_metrics, predictions = fit_model()
    predictions.to_csv(OUT / "oracle_cv_predictions_round2.csv", index=False)
    model_metrics["pool_process_coverage"] = {
        "pool_rows": int(len(pool)),
        "id_min": int(pool["id"].min()),
        "id_max": int(pool["id"].max()),
        "unique_ids": int(pool["id"].nunique()),
        "iteration_log_available": (AL_ROOT / "outputs" / "iteration_log.csv").exists(),
        "query_log_available": (AL_ROOT / "outputs" / "query_log.csv").exists(),
        "generated_ratios_log_available": (AL_ROOT / "outputs" / "generated_ratios.csv").exists(),
        "exact_iteration_reconstruction": False,
    }

    stats = {
        "round": 2,
        "evaluation_state": "partially_executed",
        "source_type": "AL-derived pool with virtual/model-labeled power density",
        "composition_order": {"al_order": AL_ORDER, "project_order": PROJECT_ORDER, "mapping_policy": "named elements only"},
        "pool_rows": int(len(pool)),
        "strict_closure": {"tolerance": 1e-9, "failures": int((pool["closure_error"] > 1e-9).sum()), "max_error": float(pool["closure_error"].max())},
        "performance": {"power_density": describe(pool["power_density"]), "normalized_cost": describe(pool["normalized_cost"]), "high_performance_threshold_q90": float(pool["power_density"].quantile(0.90)), "high_performance_count": int(len(high)), "top5_count": int(len(top5))},
        "correlations": {"power_cost_pearson": float(pool[["power_density", "normalized_cost"]].corr(method="pearson").iloc[0, 1]), "power_cost_spearman": float(pool[["power_density", "normalized_cost"]].corr(method="spearman").iloc[0, 1])},
        "high_performance_composition": {row["element"]: {"pool_mean": float(row["pool_mean_fraction"]), "high_mean": float(row["high_performance_mean_fraction"]), "difference": float(row["mean_difference_high_minus_pool"])} for _, row in element_stats.iterrows()},
        "iterative_process": {"available_ids": [int(pool["id"].min()), int(pool["id"].max())], "phase_summary": phase.to_dict(orient="records"), "missing_logs": ["iteration_log.csv", "query_log.csv", "generated_ratios.csv"]},
        "predictive_model": model_metrics,
        "recommendations_basis": ["composition_high_performance_stats_round2.csv", "process_phase_summary_round2.csv", "oracle_cv_predictions_round2.csv", "pool_annotated_round2.csv"],
        "limitations": ["No measured P_peak unit, device protocol, conditions, or replicate metadata.", "Power-density labels are virtual/model-derived according to the AL README.", "The pool does not retain iteration labels; IDs are not sufficient to reconstruct exact iteration behavior.", "Cross-validation evaluates interpolation on the supplied oracle-training sample, not external predictive validity.", "Normalized cost is a relative index with unresolved price provenance."],
    }
    (OUT / "statistical_metrics_round2.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    (OUT / "predictive_model_accuracy_round2.json").write_text(json.dumps(model_metrics, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
