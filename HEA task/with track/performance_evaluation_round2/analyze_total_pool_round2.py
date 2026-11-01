#!/usr/bin/env python3
"""Descriptive analysis of the user-designated first-round total_pool.csv.

This script does not run the AL pipeline, model, or API. The input pool schema
does not expose iteration, value type, device conditions, or prediction labels.
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


LEGACY_ORDER = ("Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr")
EXPERT_ORDER = ("Pd", "Pt", "Au", "Cr", "Ir", "Ce", "Cu", "Nb")
REQUIRED = {"id", "ratio", "power_density", "normalized_cost"}


def parse_ratio(value: object) -> np.ndarray:
    if isinstance(value, str):
        parsed = ast.literal_eval(value)
    elif isinstance(value, (list, tuple, np.ndarray)):
        parsed = value
    else:
        raise ValueError(f"Unsupported ratio field type: {type(value).__name__}")
    arr = np.asarray(parsed, dtype=float)
    if arr.shape != (8,) or not np.isfinite(arr).all():
        raise ValueError("Each ratio must contain exactly eight finite numeric fractions")
    if np.any(arr < 0) or np.any(arr > 1):
        raise ValueError("Composition fractions must lie in [0, 1]")
    if not np.isclose(arr.sum(), 1.0, rtol=0.0, atol=1e-8):
        raise ValueError(f"Composition sum is {arr.sum():.12g}, outside the descriptive check tolerance 1e-8")
    return arr


def pareto_mask(power: np.ndarray, cost: np.ndarray) -> np.ndarray:
    """Nondominated set for maximize power, minimize normalized cost."""
    values = np.column_stack([-power, cost])
    keep = np.ones(len(values), dtype=bool)
    for i, row in enumerate(values):
        if np.any(np.all(values <= row, axis=1) & np.any(values < row, axis=1)):
            keep[i] = False
    return keep


def describe(values: pd.Series) -> dict[str, float | int]:
    x = values.to_numpy(dtype=float)
    return {
        "n": int(len(x)),
        "mean": float(np.mean(x)),
        "sd_sample": float(np.std(x, ddof=1)) if len(x) > 1 else float("nan"),
        "min": float(np.min(x)),
        "q25": float(np.quantile(x, 0.25)),
        "median": float(np.median(x)),
        "q75": float(np.quantile(x, 0.75)),
        "q90": float(np.quantile(x, 0.90)),
        "max": float(np.max(x)),
    }


def plot_distribution(data: pd.DataFrame, out: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3))
    axes[0].hist(data["power_density"], bins=20, color="#2f6b7c", edgecolor="white")
    axes[0].set_xlabel("Pool power_density (source unit not recorded)")
    axes[0].set_ylabel("Candidate count")
    axes[0].set_title("Power distribution")
    axes[1].hist(data["normalized_cost"], bins=20, color="#b36a3c", edgecolor="white")
    axes[1].set_xlabel("Legacy normalized_cost (definition/source unverified)")
    axes[1].set_ylabel("Candidate count")
    axes[1].set_title("Normalized-cost proxy distribution")
    fig.suptitle("First-round pool: descriptive distributions only")
    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)


def plot_power_cost(data: pd.DataFrame, out: Path) -> None:
    frontier = pareto_mask(data["power_density"].to_numpy(), data["normalized_cost"].to_numpy())
    fig, ax = plt.subplots(figsize=(7, 5.5))
    ax.scatter(data["normalized_cost"], data["power_density"], s=24, alpha=0.58, label="Pool rows")
    ax.scatter(data.loc[frontier, "normalized_cost"], data.loc[frontier, "power_density"],
               s=42, facecolors="none", edgecolors="#bd3b2a", linewidths=1.2,
               label="Nondominated in these two stored columns")
    ax.set_xlabel("Legacy normalized_cost (not actual cost)")
    ax.set_ylabel("power_density (source unit/provenance not encoded)")
    ax.set_title("Observed pool power–cost-proxy trade-off")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)


def plot_composition(data: pd.DataFrame, high_ids: set[int], out: Path) -> None:
    all_mean = data[list(LEGACY_ORDER)].mean()
    high = data[data["id"].isin(high_ids)]
    high_mean = high[list(LEGACY_ORDER)].mean()
    x = np.arange(8)
    width = 0.38
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(x - width/2, all_mean.to_numpy(), width, label="All pool rows", color="#55717f")
    ax.bar(x + width/2, high_mean.to_numpy(), width, label="Top-decile pool rows", color="#bf8055")
    ax.set_xticks(x, LEGACY_ORDER)
    ax.set_ylabel("Mean mass fraction as stored (basis unverified)")
    ax.set_title("Descriptive composition means; selected top-decile subset")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)

    matrix = data.set_index("id")[list(LEGACY_ORDER)]
    reordered = matrix.loc[:, list(EXPERT_ORDER)]
    fig, ax = plt.subplots(figsize=(10, 6))
    image = ax.imshow(reordered.to_numpy(), aspect="auto", interpolation="nearest", vmin=0, vmax=1, cmap="viridis")
    ax.set_xticks(np.arange(8), EXPERT_ORDER)
    ax.set_xlabel("Expert order (columns permuted by header; source basis unchanged)")
    ax.set_ylabel("Pool row ID (not an iteration number)")
    ax.set_title("Composition matrix for first-round pool")
    fig.colorbar(image, ax=ax, label="Recorded fraction")
    fig.tight_layout()
    fig.savefig(out, dpi=160)
    plt.close(fig)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    data = pd.read_csv(args.input)
    missing = sorted(REQUIRED - set(data.columns))
    if missing:
        raise ValueError(f"Required columns missing: {missing}")
    for col in ("id", "power_density", "normalized_cost"):
        data[col] = pd.to_numeric(data[col], errors="raise")
    if data[["id", "power_density", "normalized_cost"]].isna().any().any():
        raise ValueError("id/power_density/normalized_cost contains missing data")
    if data["id"].duplicated().any():
        raise ValueError("Duplicate pool row IDs detected")
    ratios = np.vstack(data["ratio"].map(parse_ratio))
    for i, metal in enumerate(LEGACY_ORDER):
        data[metal] = ratios[:, i]
    data["composition_basis"] = "unverified source fraction; not assumed mass fraction"
    data["value_type"] = "unverified legacy pool label; not assumed measured"
    data["row_id_is_iteration"] = False
    data["element_count_positive"] = (ratios > 0).sum(axis=1)
    data["pareto_power_cost_proxy"] = pareto_mask(data["power_density"].to_numpy(), data["normalized_cost"].to_numpy())

    args.output_dir.mkdir(parents=True, exist_ok=True)
    figures = args.output_dir / "figures_round2"
    figures.mkdir(parents=True, exist_ok=True)
    q90 = float(data["power_density"].quantile(0.90))
    data["high_performance_top_decile"] = data["power_density"] >= q90
    high = data[data["high_performance_top_decile"]]
    top_ids = set(high["id"].astype(int).tolist())

    descriptive = {
        "input_path": str(args.input.resolve()),
        "rows": int(len(data)),
        "columns": list(pd.read_csv(args.input, nrows=0).columns),
        "legacy_vector_order": list(LEGACY_ORDER),
        "expert_display_order": list(EXPERT_ORDER),
        "basis_status": "unverified; do not call these mass fractions",
        "power_label_status": "provenance/unit/conditions absent in this file; not assumed measured device power",
        "iteration_status": "not available; id is a row identifier, not iteration",
        "power_density": describe(data["power_density"]),
        "normalized_cost": describe(data["normalized_cost"]),
        "pearson_power_cost_proxy": float(data[["power_density", "normalized_cost"]].corr(method="pearson").iloc[0,1]),
        "spearman_power_cost_proxy": float(data[["power_density", "normalized_cost"]].corr(method="spearman").iloc[0,1]),
        "composition_sum_min": float(ratios.sum(axis=1).min()),
        "composition_sum_max": float(ratios.sum(axis=1).max()),
        "positive_element_count_distribution": {str(k): int(v) for k,v in data["element_count_positive"].value_counts().sort_index().items()},
        "zero_count_by_legacy_element": {metal: int((data[metal] == 0).sum()) for metal in LEGACY_ORDER},
        "high_performance_definition": {"rule": "top decile of this pool by stored power_density", "q90_value": q90, "n": int(len(high)), "status": "descriptive post-selection slice; not a pre-registered scientific threshold"},
        "all_pool_composition_mean_legacy_order": {m: float(data[m].mean()) for m in LEGACY_ORDER},
        "top_decile_composition_mean_legacy_order": {m: float(high[m].mean()) for m in LEGACY_ORDER},
        "top_decile_power": describe(high["power_density"]),
        "top_decile_normalized_cost": describe(high["normalized_cost"]),
        "pareto_nondominated_count_power_vs_legacy_cost": int(data["pareto_power_cost_proxy"].sum()),
        "predictor_accuracy": {"status": "not_evaluable", "reason": "No measured/predicted pairs, targets, model ID, split, or prediction errors in total_pool.csv."},
        "iteration_analysis": {"status": "not_evaluable", "reason": "No iteration field; row id is not interpreted as iteration."},
        "causal_composition_effects": {"status": "not_estimated", "reason": "Adaptive selection, compositional closure, unverified labels/conditions, and no controlled comparisons prevent causal attribution."},
        "warnings": [
            "The pool has only id, ratio, power_density and normalized_cost; it lacks source/value type, model version, conditions, units, run/iteration, replicates and actual cost definition.",
            "The top-decile comparison is post-selection descriptive and must not be treated as confirmatory inference or per-element effect.",
            "The Pareto set is only with respect to stored power_density and legacy normalized_cost proxy; cost basis is undocumented.",
            "The 8-vector was decoded using the AL legacy order; expert order is produced only by header permutation. Basis remains unverified."
        ]
    }

    data.to_csv(args.output_dir / "pool_analysis_table_round2.csv", index=False)
    data.loc[data["high_performance_top_decile"]].to_csv(args.output_dir / "high_performance_top_decile_round2.csv", index=False)
    data.loc[data["pareto_power_cost_proxy"]].sort_values("power_density", ascending=False).to_csv(args.output_dir / "pareto_power_legacy_cost_round2.csv", index=False)
    pd.DataFrame([
        {"element": m, "source_order_mean_fraction": data[m].mean(), "source_order_median_fraction": data[m].median(), "source_order_sd": data[m].std(ddof=1), "zero_count": int((data[m] == 0).sum()), "top_decile_mean_fraction": high[m].mean(), "difference_top_decile_minus_all": high[m].mean() - data[m].mean()}
        for m in LEGACY_ORDER
    ]).to_csv(args.output_dir / "composition_distribution_summary_round2.csv", index=False)
    with (args.output_dir / "pool_statistics_round2.json").open("w", encoding="utf-8") as f:
        json.dump(descriptive, f, indent=2, ensure_ascii=False)

    plot_distribution(data, figures / "power_cost_distributions_round2.png")
    plot_power_cost(data, figures / "power_cost_scatter_pareto_round2.png")
    plot_composition(data, top_ids, figures / "composition_means_and_matrix_round2.png")
    print(json.dumps({"rows": len(data), "high_performance_n": len(high), "pareto_n": int(data.pareto_power_cost_proxy.sum()), "output_dir": str(args.output_dir.resolve()), "warning": "Descriptive legacy-pool analysis only; provenance and units unresolved."}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
