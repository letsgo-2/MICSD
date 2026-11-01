#!/usr/bin/env python3
"""Plot round3 adjusted designs against round2 composition evidence."""
from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


HERE = Path(__file__).resolve().parent
PD_API: Any = pd
ELEMENTS = ["Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr"]


def main() -> None:
    figures = HERE / "figures_round3"
    figures.mkdir(exist_ok=True)
    design = PD_API.read_csv(HERE / "adjusted_composition_design_round3.csv")
    stats = PD_API.read_csv(HERE.parent / "performance_evaluation_round2" / "composition_high_performance_stats_round2.csv")
    long = design.melt(id_vars=["design_id", "strategy"], value_vars=ELEMENTS, var_name="element", value_name="fraction")
    sns.set_theme(style="whitegrid", context="talk")

    fig, ax = plt.subplots(figsize=(12, 7))
    sns.lineplot(data=long, x="element", y="fraction", hue="strategy", style="design_id", markers=True, dashes=False, ax=ax)
    ax.set_title("Round3 adjusted composition designs")
    ax.set_ylabel("Mass fraction (AL source order)")
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
    fig.tight_layout()
    fig.savefig(figures / "adjusted_compositions_round3.png", dpi=180)
    plt.close(fig)

    comparison = stats[["element", "pool_mean_fraction", "high_performance_mean_fraction", "top5_mean_fraction"]].melt(id_vars="element", var_name="reference", value_name="fraction")
    selected = design[design["strategy"].isin(["full_pool_control", "high_performance_centroid", "top5_centroid"])].melt(id_vars=["design_id"], value_vars=ELEMENTS, var_name="element", value_name="fraction")
    selected["reference"] = selected["design_id"]
    combined = PD_API.concat([comparison, selected[["element", "reference", "fraction"]]], ignore_index=True)
    fig, ax = plt.subplots(figsize=(12, 7))
    sns.barplot(data=combined, x="element", y="fraction", hue="reference", ax=ax)
    ax.set_title("Round2 composition evidence and round3 anchor designs")
    ax.set_ylabel("Mass fraction")
    ax.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
    fig.tight_layout()
    fig.savefig(figures / "round2_round3_composition_comparison_round3.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 6))
    sns.scatterplot(data=design, x="normalized_cost_index", y="estimated_power_density", hue="strategy", style="strategy", s=120, ax=ax)
    ax.set_title("Round3 design space: cost index and reserved measured outcome")
    ax.set_xlabel("Relative normalized cost index (not USD/g)")
    ax.set_ylabel("Measured P_peak: pending experiment")
    fig.tight_layout()
    fig.savefig(figures / "round3_design_tradeoff_round3.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    main()
