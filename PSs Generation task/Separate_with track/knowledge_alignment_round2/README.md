# Round 2 Scientific Knowledge Alignment

This folder extends `../knowledge_alignment_round1/` without replacing it. It responds to the domain expert's request for advantageous scaffold analysis and the computer expert's request for genuinely computable iterative-optimization metrics, calculation methods, meanings, and defensible reward thresholds.

## Deliverables

- `round2_alignment_report.md`: integrated English report.
- `domain_expert_scaffold_supplement.md`: scaffold families and characteristics.
- `computer_expert_dft_metrics_supplement.md`: DFT/TD-DFT metrics, methods, meanings, limitations, and optimization eligibility.
- `optimization_metrics.yaml`: machine-readable iterative-optimization specification.
- `expert_review_queue_round2.yaml`: unresolved validation items.
- `corpus_manifest.tsv`: copied Round 1 47-source coverage manifest.
- `execution_trace.jsonl`: Round 2 plan, tool calls, evidence decisions, and validation.

## Key boundary

DFT descriptors are molecular-level proxies or mechanistic quantities. They must not be described as direct predictions of cellular IC50, dark toxicity, organelle localization, immune activation, or pyroptosis. Those endpoints remain experimental or require separately validated multimodal models.
