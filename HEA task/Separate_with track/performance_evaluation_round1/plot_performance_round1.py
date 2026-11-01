#!/usr/bin/env python3
"""Generate evaluation figures from round1 checked artifacts.

Figures are explicitly labeled as virtual/derived where appropriate; no plot
implies experimental validation.
"""
from __future__ import annotations

import ast
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from typing import Any


HERE = Path(__file__).resolve().parent
POOL = HERE.parent / "AL" / "catalyst_active_learning_runnable" / "outputs" / "total_pool.csv"
FIGURES = HERE / "figures_round1"
AL_ORDER = ["Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr"]
PD_API: Any = pd


def main() -> None:
    FIGURES.mkdir(exist_ok=True)
    pool = PD_API.read_csv(POOL)
    pool["ratio_values"] = pool["ratio"].map(ast.literal_eval)
    ratios = PD_API.DataFrame(pool.pop("ratio_values").tolist(), columns=AL_ORDER)
    frame = PD_API.concat([pool, ratios], axis=1)
    sns.set_theme(style="whitegrid", context="talk")

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(data=frame, x="normalized_cost", y="power_density", alpha=0.65, ax=ax)
    ax.set_title("Virtual AL pool: power density vs relative cost")
    ax.set_xlabel("Relative normalized cost index (not USD/g)")
    ax.set_ylabel("Power density (source unit unavailable)")
    fig.tight_layout()
    fig.savefig(FIGURES / "power_vs_cost_virtual_round1.png", dpi=180)
    plt.close(fig)

    long = frame.melt(id_vars=["power_density"], value_vars=AL_ORDER, var_name="element", value_name="fraction")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=long, x="element", y="fraction", order=AL_ORDER, ax=ax)
    ax.set_title("Element fraction distribution in the virtual AL pool")
    ax.set_ylabel("Mass fraction (AL source order)")
    fig.tight_layout()
    fig.savefig(FIGURES / "composition_distribution_round1.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 6))
    corr = frame[AL_ORDER + ["power_density", "normalized_cost"]].corr(method="spearman")
    sns.heatmap(corr, cmap="vlag", center=0, annot=True, fmt=".2f", ax=ax)
    ax.set_title("Spearman association matrix for virtual AL artifacts")
    fig.tight_layout()
    fig.savefig(FIGURES / "spearman_associations_round1.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    main()
