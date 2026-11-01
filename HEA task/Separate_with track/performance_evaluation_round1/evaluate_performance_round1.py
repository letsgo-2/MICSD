#!/usr/bin/env python3
"""Reproducible round1 checks and statistics for the HEA AL artifacts.

The script never silently reorders or normalizes source compositions. It reports
the AL order as observed and creates a separately mapped project-order view only
when the named-element mapping is explicit.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
AL_ROOT = ROOT / "AL" / "catalyst_active_learning_runnable"
OUT = Path(__file__).resolve().parent
AL_ORDER = ["Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr"]
PROJECT_ORDER = ["Pd", "Pt", "Au", "Cr", "Ir", "Ce", "Cu", "Nb"]
EXPECTED = set(AL_ORDER)
PD_API: Any = pd


def summary(values: Any) -> dict[str, Any]:
    numeric: Any = PD_API.to_numeric(values, errors="coerce").dropna()
    return {
        "n": int(numeric.size),
        "missing": int(values.size - numeric.size),
        "mean": float(numeric.mean()) if len(numeric) else None,
        "std_sample": float(numeric.std(ddof=1)) if len(numeric) > 1 else None,
        "median": float(numeric.median()) if len(numeric) else None,
        "min": float(numeric.min()) if len(numeric) else None,
        "max": float(numeric.max()) if len(numeric) else None,
        "q25": float(numeric.quantile(0.25)) if len(numeric) else None,
        "q75": float(numeric.quantile(0.75)) if len(numeric) else None,
    }


def check_frame(frame: Any, source: str, composition_columns: list[str], target: str) -> tuple[dict[str, Any], Any]:
    values = frame[composition_columns].apply(PD_API.to_numeric, errors="coerce")
    sums = values.sum(axis=1, skipna=False)
    finite = np.isfinite(values.to_numpy()).all(axis=1)
    nonnegative = (values.to_numpy() >= 0).all(axis=1)
    closure_error = (sums - 1.0).abs()
    valid = finite & nonnegative & (closure_error <= 1e-9)
    report = {
        "source": source,
        "rows": int(len(frame)),
        "columns": list(frame.columns),
        "composition_order_observed": composition_columns,
        "required_elements_present": set(composition_columns) == EXPECTED,
        "duplicate_rows": int(frame.duplicated().sum()),
        "missing_cells": int(frame.isna().sum().sum()),
        "non_numeric_composition_rows": int((~np.isfinite(values.to_numpy())).any(axis=1).sum()),
        "negative_composition_rows": int((values.to_numpy() < 0).any(axis=1).sum()),
        "closure_tolerance": 1e-9,
        "closure_error_max": float(closure_error.max()) if len(frame) else None,
        "closure_failures": int((closure_error > 1e-9).sum()),
        "valid_composition_rows": int(valid.sum()),
        "target_summary": summary(frame[target]) if target in frame else None,
    }
    checked = frame.copy()
    checked["composition_valid_strict"] = valid
    checked["closure_error"] = closure_error
    checked["source_file"] = source
    return report, checked


def map_explicitly(frame: pd.DataFrame) -> pd.DataFrame:
    mapped = frame.copy()
    for element in PROJECT_ORDER:
        mapped[element] = frame[element]
    return mapped


def main() -> None:
    initial_path = AL_ROOT / "data" / "initial_examples.csv"
    oracle_path = AL_ROOT / "data" / "oracle_training_sample.csv"
    pool_path = AL_ROOT / "outputs" / "total_pool.csv"
    examples_path = AL_ROOT / "outputs" / "total_examples_pool.csv"

    initial = PD_API.read_csv(initial_path)
    oracle = PD_API.read_csv(oracle_path)
    examples = PD_API.read_csv(examples_path)
    pool = PD_API.read_csv(pool_path)
    pool["ratio_values"] = pool["ratio"].map(ast.literal_eval)
    pool_ratios = PD_API.DataFrame(pool["ratio_values"].tolist(), columns=AL_ORDER)
    pool_checked = PD_API.concat([pool.drop(columns=["ratio_values"]), pool_ratios], axis=1)

    reports = []
    checked_frames = []
    for name, frame in [("initial_examples.csv", initial), ("oracle_training_sample.csv", oracle), ("total_examples_pool.csv", examples), ("total_pool.csv", pool_checked)]:
        target = "power_density"
        report, checked = check_frame(frame, name, AL_ORDER, target)
        reports.append(report)
        checked_frames.append(checked)

    metrics = {
        "evaluation_state": "partially_executed",
        "primary_metric": "power_density",
        "primary_metric_status": "not_validated_as_measured",
        "source_type_policy": {
            "initial_examples": "unclassified_source_data; measurement provenance missing",
            "oracle_training_sample": "virtual_or_training_data unless provenance is supplied",
            "total_pool": "derived/model-labeled AL artifact",
            "total_examples_pool": "derived/model-labeled AL artifact",
        },
        "composition_contract": {
            "al_order": AL_ORDER,
            "project_order": PROJECT_ORDER,
            "explicit_mapping": {element: element for element in PROJECT_ORDER},
            "silent_normalization": False,
            "closure_tolerance": 1e-9,
        },
        "dataset_checks": reports,
        "statistical_metrics": {
            "initial_power_density": summary(initial["power_density"]),
            "oracle_training_power_density": summary(oracle["power_density"]),
            "total_examples_pool_power_density": summary(examples["power_density"]),
            "total_pool_power_density": summary(pool["power_density"]),
            "total_pool_normalized_cost": summary(pool["normalized_cost"]),
            "total_pool_power_cost_pearson": float(pool[["power_density", "normalized_cost"]].corr(method="pearson").iloc[0, 1]),
            "total_pool_power_cost_spearman": float(pool[["power_density", "normalized_cost"]].corr(method="spearman").iloc[0, 1]),
            "top_10_percent_power_threshold": float(pool["power_density"].quantile(0.90)),
            "top_10_percent_count": int((pool["power_density"] >= pool["power_density"].quantile(0.90)).sum()),
        },
        "blocking_data_gaps": [
            "P_peak unit, device protocol, operating conditions, assay basis, and replicate metadata are absent.",
            "Round2 execution was not authorized or performed; no live API/model run is attributable to this evaluation.",
            "The AL element order differs from the project order; project mapping is explicit but requires independent validation.",
            "Normalized cost has no dated price provenance and is a relative index, not USD/g.",
            "No uncertainty intervals or repeated measurements are available for candidate performance.",
        ],
    }
    (OUT / "data_checks_round1.json").write_text(json.dumps({"reports": reports}, indent=2) + "\n", encoding="utf-8")
    (OUT / "statistical_metrics_round1.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    for name, checked in zip(["initial", "oracle_training", "examples_pool", "total_pool"], checked_frames):
        checked.to_csv(OUT / f"checked_{name}_round1.csv", index=False)

    ranked = pool.sort_values(["power_density", "normalized_cost"], ascending=[False, True]).copy()
    ranked.insert(0, "rank_by_power_density", range(1, len(ranked) + 1))
    ranked.to_csv(OUT / "candidate_ranking_virtual_round1.csv", index=False)


if __name__ == "__main__":
    main()
