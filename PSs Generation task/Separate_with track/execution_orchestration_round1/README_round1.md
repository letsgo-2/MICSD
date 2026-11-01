# Scientific Execution Orchestration — Round 1

This folder is the first execution-orchestration round downstream of `knowledge_alignment_round2/`.

## Inputs

The workflow inherits the three required Round 2 outputs:

1. `round2_alignment_report.md` — integrated domain and computer conclusions.
2. `optimization_metrics.yaml` — structured metrics, computability boundaries, evidence, and provisional reward guidance.
3. `expert_review_queue_round2.yaml` — unresolved decisions and evidence requests.

The scaffold and DFT supplements were used as supporting context. No unresolved Round 2 item was silently promoted to an approved fact.

## Outputs

- `execution_orchestration_report_round1.md` — expert-facing workflow, metric ranking, threshold guidance, and operating recommendations.
- `execution_orchestration_round1.yaml` — machine-readable workflow, interfaces, reward components, controls, and decisions.
- `execution_review_queue_round1.yaml` — inherited and execution-specific questions requiring review.
- `execution_trace_round1.jsonl` — auditable plan, input reads, decisions, file writes, and validation events.

## Core design decision

Use a multi-family Pareto search with SMILES as the molecule representation, RECAP as the fragmentation/editing rule, and porphyrin as a required seed family. A DFT/TD-DFT screening tier ranks molecular proxies; experimental or separately validated surrogate endpoints are not claimed by DFT and enter only after assay harmonization and model validation.
