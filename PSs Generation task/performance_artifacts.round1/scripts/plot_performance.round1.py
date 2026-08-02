#!/usr/bin/env python3
"""Create auditable SDPD parity/residual plots and a metrics table from stored predictions."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def metric_rows(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows, long = [], []
    labels = [c for c in df.columns if c.endswith("_label")]
    for label in labels:
        root = label[:-6]
        candidates = [f"{root}_pred", f"{root}_pred_head"]
        pred = next((c for c in candidates if c in df.columns), None)
        if pred is None:
            continue
        pair = df[[label, pred]].apply(pd.to_numeric, errors="coerce").dropna()
        if pair.empty:
            continue
        obs, est = pair[label].to_numpy(), pair[pred].to_numpy()
        residual = est - obs
        ss_tot = np.sum((obs - obs.mean()) ** 2)
        rows.append({"target": root, "n": len(pair), "mae": np.mean(abs(residual)), "rmse": np.sqrt(np.mean(residual**2)), "bias": residual.mean(), "r2": 1 - np.sum(residual**2) / ss_tot if ss_tot else np.nan})
        long.extend({"target": root, "observed": x, "predicted": y, "residual": y-x} for x, y in zip(obs, est))
    return pd.DataFrame(rows), pd.DataFrame(long)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    metrics, long = metric_rows(pd.read_csv(args.predictions))
    if long.empty:
        raise ValueError("No paired *_label and *_pred/_pred_head columns found")
    metrics.to_csv(args.output_dir / "model_metrics.round1.csv", index=False)
    sns.set_theme(style="whitegrid")
    g = sns.FacetGrid(long, col="target", col_wrap=3, sharex=False, sharey=False, height=3)
    g.map_dataframe(sns.scatterplot, x="observed", y="predicted", alpha=.65, s=20)
    for ax in g.axes.flat:
        lim = [min(ax.get_xlim()[0], ax.get_ylim()[0]), max(ax.get_xlim()[1], ax.get_ylim()[1])]
        ax.plot(lim, lim, "k--", lw=1); ax.set_xlim(lim); ax.set_ylim(lim)
    g.figure.savefig(args.output_dir / "model_parity.round1.png", dpi=300, bbox_inches="tight")
    plt.close(g.figure)
    g = sns.FacetGrid(long, col="target", col_wrap=3, sharex=False, sharey=False, height=3)
    g.map_dataframe(sns.scatterplot, x="observed", y="residual", alpha=.65, s=20)
    for ax in g.axes.flat: ax.axhline(0, color="k", ls="--", lw=1)
    g.figure.savefig(args.output_dir / "model_residuals.round1.png", dpi=300, bbox_inches="tight")
    plt.close(g.figure)


if __name__ == "__main__":
    main()
