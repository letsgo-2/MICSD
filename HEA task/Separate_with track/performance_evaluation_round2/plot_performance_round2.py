#!/usr/bin/env python3
"""Create round2 plots for composition, virtual performance, cost, process, and model diagnostics."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures_round2"
PD_API: Any = pd


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    pool = PD_API.read_csv(HERE / "pool_annotated_round2.csv")
    element_stats = PD_API.read_csv(HERE / "composition_high_performance_stats_round2.csv")
    predictions = PD_API.read_csv(HERE / "oracle_cv_predictions_round2.csv")
    sns.set_theme(style="whitegrid", context="talk")

    long = pool.melt(id_vars=["power_density", "is_high_performance"], value_vars=element_stats["element"].tolist(), var_name="element", value_name="fraction")
    fig, ax = plt.subplots(figsize=(11, 6))
    sns.boxplot(data=long, x="element", y="fraction", hue="is_high_performance", ax=ax)
    ax.set_title("Eight-metal composition distributions: pool vs high-performance subset")
    ax.set_ylabel("Mass fraction (AL source order)")
    ax.legend(title="Top-decile virtual power label")
    fig.tight_layout()
    fig.savefig(FIGURES / "composition_high_performance_round2.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=pool, x="normalized_cost", y="power_density", hue="is_high_performance", size="nonzero_elements", sizes=(30, 180), ax=ax)
    ax.set_title("Virtual peak power density versus normalized cost")
    ax.set_xlabel("Relative normalized cost index (not USD/g)")
    ax.set_ylabel("Power density (source unit unavailable)")
    fig.tight_layout()
    fig.savefig(FIGURES / "power_density_cost_round2.png", dpi=180)
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    sns.lineplot(data=pool, x="id", y="power_density", ax=axes[0], marker="o", linewidth=1)
    axes[0].set_title("Recorded pool sequence: virtual power density")
    axes[0].set_xlabel("Pool record ID (not an exact iteration index)")
    axes[0].set_ylabel("Power density")
    sns.lineplot(data=pool, x="id", y="normalized_cost", ax=axes[1], marker="o", linewidth=1, color="darkorange")
    axes[1].set_title("Recorded pool sequence: relative cost")
    axes[1].set_xlabel("Pool record ID (not an exact iteration index)")
    axes[1].set_ylabel("Normalized cost index")
    fig.tight_layout()
    fig.savefig(FIGURES / "pool_sequence_process_round2.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 6))
    sns.scatterplot(data=predictions, x="observed_power_density", y="cv_predicted_power_density", ax=ax)
    values = pd.concat([predictions["observed_power_density"], predictions["cv_predicted_power_density"]])
    lo = float(values.min())
    hi = float(values.max())
    ax.plot([lo, hi], [lo, hi], linestyle="--", color="black")
    ax.set_title("Five-fold CV: virtual oracle observed vs predicted")
    ax.set_xlabel("Observed oracle-training label")
    ax.set_ylabel("Cross-validated prediction")
    fig.tight_layout()
    fig.savefig(FIGURES / "oracle_cv_parity_round2.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 6))
    sns.barplot(data=element_stats, x="element", y="mean_difference_high_minus_pool", ax=ax, color="steelblue")
    ax.axhline(0, color="black", linewidth=1)
    ax.set_title("High-performance subset composition shift")
    ax.set_ylabel("Mean fraction difference: high subset minus full pool")
    fig.tight_layout()
    fig.savefig(FIGURES / "high_performance_composition_shift_round2.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    main()
