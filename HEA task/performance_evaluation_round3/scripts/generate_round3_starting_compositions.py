from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


METAL_ORDER = ("Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate proposed Round 3 starting compositions from Round 2 evidence."
    )
    _ = parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("performance_evaluation_round3"),
        help="Round 3 output directory.",
    )
    return parser.parse_args()


def normalize(values: list[float]) -> list[float]:
    total = sum(values)
    if total <= 0:
        raise ValueError("Composition sum must be positive")
    return [value / total for value in values]


def main() -> None:
    args = parse_args()
    table_dir = args.output_dir / "tables"
    table_dir.mkdir(parents=True, exist_ok=True)

    rows = [
        {
            "proposal_id": "R3-S01",
            "proposal_role": "best_candidate_anchor",
            "basis": "Round 2 best candidate id 132",
            "rationale": "Preserve the observed best composition as the central starting point for the next experiment.",
            "Pd": 0.39129020571980316,
            "Pt": 0.15790583472139091,
            "Cu": 0.1159081298431437,
            "Au": 0.006938169468729498,
            "Ir": 0.018589882073195983,
            "Ce": 0.16687310212385884,
            "Nb": 0.10601752062279259,
            "Cr": 0.03647715542708525,
        },
        {
            "proposal_id": "R3-S02",
            "proposal_role": "high_performance_mean_anchor",
            "basis": "Round 2 top-decile high-performance mean",
            "rationale": "Use the average composition of high-performance candidates to reduce dependence on a single best point.",
            "Pd": 0.40377211827279624,
            "Pt": 0.15885849346937575,
            "Cu": 0.09532335454399685,
            "Au": 0.023088434014890684,
            "Ir": 0.03063778149523799,
            "Ce": 0.1250667107510007,
            "Nb": 0.09361162120294275,
            "Cr": 0.06964148624975902,
        },
        {
            "proposal_id": "R3-S03",
            "proposal_role": "pd_ce_enriched_low_au_ir",
            "basis": "Round 2 enrichment: Pd and Ce positive; Au and Ir depleted",
            "rationale": "Increase Pd/Ce while keeping Au and Ir very low to probe lower-cost high-performance behavior.",
            "Pd": 0.42,
            "Pt": 0.16,
            "Cu": 0.10,
            "Au": 0.005,
            "Ir": 0.01,
            "Ce": 0.17,
            "Nb": 0.10,
            "Cr": 0.035,
        },
        {
            "proposal_id": "R3-S04",
            "proposal_role": "pd_ce_nb_rich_low_au_ir",
            "basis": "Pareto candidates 127/138/145 and Ce/Nb retention",
            "rationale": "Probe whether Ce/Nb support can preserve performance while reducing high-cost Au/Ir.",
            "Pd": 0.40,
            "Pt": 0.14,
            "Cu": 0.09,
            "Au": 0.005,
            "Ir": 0.005,
            "Ce": 0.18,
            "Nb": 0.15,
            "Cr": 0.03,
        },
        {
            "proposal_id": "R3-S05",
            "proposal_role": "pd_pt_cu_balanced_ce",
            "basis": "Best candidate id 132 with moderate Pt/Cu and Ce",
            "rationale": "Maintain the best candidate's Pd/Pt/Cu/Ce balance while testing a slightly lower Pd level.",
            "Pd": 0.38,
            "Pt": 0.18,
            "Cu": 0.13,
            "Au": 0.005,
            "Ir": 0.015,
            "Ce": 0.16,
            "Nb": 0.09,
            "Cr": 0.04,
        },
        {
            "proposal_id": "R3-S06",
            "proposal_role": "lower_pd_ce_nb_tradeoff",
            "basis": "Lower-cost Pareto neighborhood near candidates 138 and 145",
            "rationale": "Reduce Pd slightly and compensate with Ce/Nb to explore cost-performance robustness.",
            "Pd": 0.35,
            "Pt": 0.15,
            "Cu": 0.10,
            "Au": 0.005,
            "Ir": 0.005,
            "Ce": 0.18,
            "Nb": 0.16,
            "Cr": 0.05,
        },
        {
            "proposal_id": "R3-S07",
            "proposal_role": "ce_high_ablation",
            "basis": "Ce enrichment in high-performance formulas",
            "rationale": "Stress-test the Ce contribution while keeping Au/Ir minimized.",
            "Pd": 0.37,
            "Pt": 0.15,
            "Cu": 0.10,
            "Au": 0.005,
            "Ir": 0.005,
            "Ce": 0.21,
            "Nb": 0.12,
            "Cr": 0.04,
        },
        {
            "proposal_id": "R3-S08",
            "proposal_role": "nb_high_ablation",
            "basis": "Pareto candidates with elevated Nb at lower normalized cost",
            "rationale": "Probe whether a higher Nb fraction helps retain performance with lower precious-metal burden.",
            "Pd": 0.36,
            "Pt": 0.14,
            "Cu": 0.10,
            "Au": 0.005,
            "Ir": 0.005,
            "Ce": 0.16,
            "Nb": 0.19,
            "Cr": 0.04,
        },
        {
            "proposal_id": "R3-S09",
            "proposal_role": "cr_retention_check",
            "basis": "Cr is lower in best candidate but present in Pareto lower-cost candidates",
            "rationale": "Check whether moderate Cr is beneficial in lower-cost Pareto-like formulations.",
            "Pd": 0.35,
            "Pt": 0.15,
            "Cu": 0.11,
            "Au": 0.005,
            "Ir": 0.005,
            "Ce": 0.16,
            "Nb": 0.12,
            "Cr": 0.10,
        },
        {
            "proposal_id": "R3-S10",
            "proposal_role": "low_cost_guardrail",
            "basis": "Pareto lower-cost neighborhood while preserving Pd/Ce",
            "rationale": "Provide one aggressive low-Au/Ir, lower-Pd guardrail candidate for cost-performance comparison.",
            "Pd": 0.33,
            "Pt": 0.13,
            "Cu": 0.12,
            "Au": 0.002,
            "Ir": 0.003,
            "Ce": 0.18,
            "Nb": 0.17,
            "Cr": 0.065,
        },
    ]

    normalized_rows = []
    for row in rows:
        values = normalize([float(row[metal]) for metal in METAL_ORDER])
        normalized = {**{key: value for key, value in row.items() if key not in METAL_ORDER}}
        normalized.update({metal: values[index] for index, metal in enumerate(METAL_ORDER)})
        normalized["composition_sum"] = sum(values)
        normalized["value_type"] = "proposed_starting_ratio"
        normalized["not_a_measured_result"] = True
        normalized_rows.append(normalized)

    frame = pd.DataFrame(normalized_rows)
    csv_path = table_dir / "adjusted_starting_compositions_round3.csv"
    frame.to_csv(csv_path, index=False)

    manifest = {
        "round": "round3",
        "artifact": "adjusted_starting_compositions",
        "output_csv": str(csv_path),
        "source_evidence": [
            "performance_evaluation_round2/tables/high_performance_composition_features_round2.csv",
            "performance_evaluation_round2/tables/pareto_front_candidates_round2.csv",
            "performance_evaluation_round2/tables/analysis_manifest_round2.json",
        ],
        "proposal_count": len(frame),
        "provenance": "Proposed adjustment set derived from Round 2 statistics and materials-expert suggestion; not experimental measurements.",
    }
    manifest_path = table_dir / "adjustment_manifest_round3.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
