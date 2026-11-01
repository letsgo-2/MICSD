# Scientific Execution Orchestration — Round 2

This folder updates `execution_orchestration_round1/` in response to the materials scientist's request for a priority ranking of SOCME, HOMO–LUMO gap, E(S1)−E(T1), E(S1), charge, symmetry, SA, logP, TPSA, and molecular weight (MW).

## Outputs

- `execution_orchestration_report_round2.md`: English expert-facing ranking, rationale, threshold guidance, and workflow integration.
- `execution_orchestration_round2.yaml`: machine-readable metric decisions, reward status, interfaces, and update controls.
- `execution_review_queue_round2.yaml`: unresolved protocol and expert-validation items.
- `execution_trace_round2.jsonl`: auditable planning, input reads, ranking decisions, file writes, and validation events.

## Interpretation boundary

The ranking is an execution priority for the existing photosensitizer-generation workflow. It is not a universal ranking of molecular importance. All requested descriptors must be calculated with declared definitions, units, charge states, conformers, protonation states, solvent, and scaffold-family context. No descriptor is treated as a direct prediction of ΦΔ, ROS rate, cellular potency, dark toxicity, localization, photostability, pyroptosis, or immune response.
