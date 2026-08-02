# Performance Evaluation Report Round 3

## 1. Update Scope

Round 3 records the materials expert's adjustment request: revise the starting composition ratios and prepare for another experimental round. This update does not report new experimental performance, does not execute the AL model, does not train the virtual oracle, and does not modify raw AL output files.

The Round 3 adjustment is derived from Round 2 evidence:

- High-performance compositions were enriched in `Pd` and `Ce`.
- High-performance compositions were depleted in `Au` and `Ir`.
- The best Round 2 candidate was `id=132`, with peak power density `68.5811`, normalized cost `53.7637`, and composition approximately `Pd 0.3913`, `Pt 0.1579`, `Cu 0.1159`, `Au 0.0069`, `Ir 0.0186`, `Ce 0.1669`, `Nb 0.1060`, `Cr 0.0365`.
- Pareto-front neighbors suggested useful lower-cost regions with retained `Ce`/`Nb` support.

## 2. Round 3 Output Paths

| Output | Path | Purpose |
|---|---|---|
| Proposed starting compositions | `performance_evaluation_round3/tables/adjusted_starting_compositions_round3.csv` | Ten normalized starting ratios for the next experimental/AL round. |
| Adjustment manifest | `performance_evaluation_round3/tables/adjustment_manifest_round3.json` | Machine-readable provenance and source evidence list. |
| Generation script | `performance_evaluation_round3/scripts/generate_round3_starting_compositions.py` | Reproducible script that generated the proposed ratios. |
| Round 3 evaluation YAML | `performance_evaluation_round3/performance_evaluation_round3.yaml` | Structured skill-style record of subjects, records, recommendations, and limitations. |
| Round 3 review queue | `performance_evaluation_round3/performance_review_queue_round3.yaml` | Expert confirmations needed before execution. |
| This report | `performance_evaluation_round3/performance_evaluation_report_round3.md` | Human-readable adjustment summary and next-step plan. |

## 3. Proposed Starting Composition Set

All proposed rows use the canonical element order:

```text
Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr
```

Each row sums to 1 and is labeled as `proposed_starting_ratio`, not as a measured or predicted performance result.

| Proposal | Role | Main Purpose |
|---|---|---|
| `R3-S01` | Best candidate anchor | Preserve Round 2 best candidate `id=132` as the center point. |
| `R3-S02` | High-performance mean anchor | Use the top-decile mean to reduce reliance on one candidate. |
| `R3-S03` | Pd/Ce enriched, low Au/Ir | Probe higher Pd/Ce with minimized Au/Ir. |
| `R3-S04` | Pd/Ce/Nb rich, low Au/Ir | Test Ce/Nb support while reducing high-cost metals. |
| `R3-S05` | Pd/Pt/Cu balanced with Ce | Preserve the best candidate's Pd/Pt/Cu/Ce balance with slightly lower Pd. |
| `R3-S06` | Lower-Pd Ce/Nb tradeoff | Explore cost-performance robustness with less Pd. |
| `R3-S07` | Ce-high ablation | Stress-test the Ce contribution. |
| `R3-S08` | Nb-high ablation | Test whether increased Nb supports lower precious-metal burden. |
| `R3-S09` | Cr retention check | Check whether moderate Cr helps in lower-cost Pareto-like formulas. |
| `R3-S10` | Low-cost guardrail | Aggressive low-Au/Ir and lower-Pd guardrail candidate. |

## 4. Adjustment Logic

The proposed Round 3 starting set is deliberately not a broad random restart. It is a local refinement around the Round 2 high-performing region, with controlled perturbations for mechanism and cost sensitivity:

1. Keep `Pd` as the dominant metal because it is both high in the best candidate and enriched in the high-performance group.
2. Preserve or increase `Ce` because it is positively enriched in the top-decile group and appears strongly in the best candidate.
3. Keep `Au` and `Ir` low because both are depleted in high-performance formulas and add cost pressure.
4. Use `Nb`, `Cr`, `Pt`, and `Cu` as structured perturbation axes rather than removing them entirely.
5. Include both high-performance anchors and lower-cost guardrail candidates so the next round can distinguish performance maximization from cost-performance robustness.

## 5. Next Experiment Recommendation

Use `adjusted_starting_compositions_round3.csv` as the starting composition set for the next round only after expert confirmation. The next execution should persist explicit model and experimental provenance fields:

- `iteration`
- `source`
- `proposal_id`
- `predicted_power_density`
- `prediction_uncertainty` or `llm_std`
- `ucb_score` if used
- `observed_power_density` after validation
- `prediction_residual` after validation
- `normalized_cost`
- full eight-metal composition columns

These fields are needed because Round 2 could not support model-accuracy analysis from `total_pool.csv` alone.

## 6. Review Needs Before Execution

- Materials expert should approve whether the Pd/Ce-enriched, low-Au/Ir direction is chemically acceptable.
- Computer expert should confirm how the proposed starting ratios will be injected into the AL workflow without overwriting raw Round 2 artifacts.
- Optimization expert should decide whether all 10 proposed starts are used directly or whether they seed a local candidate generator.
- Experimental expert should confirm feasibility, synthesis constraints, and whether any composition requires practical rounding.

## 7. Provenance Boundary

The Round 3 files are an adjustment plan. They do not contain new peak power density, normalized cost, or model-accuracy results. Any future measured or predicted values must be stored as new Round 3 execution results with explicit provenance.
