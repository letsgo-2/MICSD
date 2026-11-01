#!/usr/bin/env python3
"""Generate a provisional, closure-validated composition design for experimental round 3."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
R2 = ROOT / "performance_evaluation_round2"
OUT = Path(__file__).resolve().parent
AL_ORDER = ["Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr"]
PROJECT_ORDER = ["Pd", "Pt", "Au", "Cr", "Ir", "Ce", "Cu", "Nb"]
PD_API: Any = pd


def normalize(values: dict[str, float]) -> dict[str, float]:
    total = sum(values.values())
    if total <= 0 or not np.isfinite(total):
        raise ValueError("Composition must have a finite positive sum")
    result = {element: value / total for element, value in values.items()}
    if any(value < 0 for value in result.values()):
        raise ValueError("Composition cannot contain negative fractions")
    if abs(sum(result.values()) - 1.0) > 1e-12:
        raise ValueError("Composition closure failed")
    return result


def as_row(composition: dict[str, float], design_id: str, strategy: str, rationale: str) -> dict[str, Any]:
    ordered = normalize(composition)
    row: dict[str, Any] = {"design_id": design_id, "strategy": strategy, "rationale": rationale}
    row.update({element: ordered[element] for element in AL_ORDER})
    row["composition_sum"] = sum(ordered.values())
    row["closure_error"] = abs(row["composition_sum"] - 1.0)
    row["source_type"] = "provisional_design_not_measured"
    return row


def main() -> None:
    stats = PD_API.read_csv(R2 / "composition_high_performance_stats_round2.csv")
    pool = PD_API.read_csv(R2 / "pool_annotated_round2.csv")
    high = stats.set_index("element")["high_performance_mean_fraction"].to_dict()
    pool_mean = stats.set_index("element")["pool_mean_fraction"].to_dict()
    top5 = stats.set_index("element")["top5_mean_fraction"].to_dict()
    rows = [
        as_row(pool_mean, "R3-CONTROL-CENTROID", "full_pool_control", "Control at the round2 full-pool centroid."),
        as_row(high, "R3-HIGH-CENTROID", "high_performance_centroid", "Exploitation center at the descriptive round2 top-decile centroid; not a causal optimum."),
        as_row(top5, "R3-TOP5-CENTROID", "top5_centroid", "Center of the round2 top-five descriptive composition."),
    ]
    high_vector = np.array([high[e] for e in AL_ORDER], dtype=float)
    pool_vector = np.array([pool_mean[e] for e in AL_ORDER], dtype=float)
    top5_vector = np.array([top5[e] for e in AL_ORDER], dtype=float)
    for index, fraction in enumerate([0.25, 0.50, 0.75], start=1):
        vector = (1.0 - fraction) * high_vector + fraction * pool_vector
        rows.append(as_row(dict(zip(AL_ORDER, vector)), f"R3-GRADIENT-{index}", "high_to_pool_gradient", f"Interpolation fraction {fraction:.2f} from high-performance centroid toward full-pool centroid."))
    for index, vector in enumerate([high_vector, top5_vector], start=1):
        perturbed = vector.copy()
        perturbed[AL_ORDER.index("Pd")] += 0.03
        perturbed[AL_ORDER.index("Au")] -= 0.02
        perturbed[AL_ORDER.index("Ce")] -= 0.01
        rows.append(as_row(dict(zip(AL_ORDER, perturbed)), f"R3-PD-AU-CONTRAST-{index}", "Pd_Au_contrast", "Perturbation to test the descriptive Pd-high/Au-low association while preserving other composition structure."))
    rng = np.random.default_rng(43)
    for index in range(1, 4):
        noise = rng.normal(0.0, 0.015, size=len(AL_ORDER))
        vector = np.clip(high_vector + noise, 0.005, None)
        rows.append(as_row(dict(zip(AL_ORDER, vector)), f"R3-DIVERSE-{index}", "local_diversity", "Small perturbation around the high-performance centroid for uncertainty and local sensitivity coverage."))

    design = PD_API.DataFrame(rows)
    design["normalized_cost_index"] = (design["Pd"] * 26393.0 + design["Pt"] * 20325.0 + design["Cu"] * 4.53 + design["Au"] * 29298.0 + design["Ir"] * 23926.0 + design["Ce"] * 5.37 + design["Nb"] * 32.22 + design["Cr"] * 5.86) / 26393.0 * 100.0
    design["estimated_power_density"] = np.nan
    design.to_csv(OUT / "adjusted_composition_design_round3.csv", index=False)
    with (OUT / "composition_validation_round3.jsonl").open("w", encoding="utf-8") as handle:
        for _, row in design.iterrows():
            handle.write(json.dumps({"design_id": row["design_id"], "closure_error": row["closure_error"], "nonnegative": bool((row[AL_ORDER] >= 0).all()), "valid_strict": bool(row["closure_error"] <= 1e-9)}, allow_nan=False) + "\n")
    summary = {
        "design_count": int(len(design)),
        "strategies": design["strategy"].value_counts().to_dict(),
        "closure_failures": int((design["closure_error"] > 1e-9).sum()),
        "negative_fraction_rows": int((design[AL_ORDER].to_numpy() < 0).any(axis=1).sum()),
        "al_order": AL_ORDER,
        "project_order": PROJECT_ORDER,
        "provisional_guardrail": "No expert-approved element-specific bounds were supplied; only nonnegativity and closure were enforced.",
    }
    (OUT / "composition_design_summary_round3.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
