# Round 1 Scientific Knowledge Alignment

## Project goal

Develop candidate molecules with improved photosensitizing performance, using the uploaded papers as the primary evidence. The intended design space includes molecular photosensitizers and photodrugs that can produce useful photochemistry under biologically relevant conditions, reach the intended cellular/organelle site, and generate a controllable therapeutic phenotype.

## Scope and evidence policy

- Corpus: all 47 Markdown files under `../markdown/`, including four supplementary-information files.
- Language: English.
- Evidence priority: uploaded papers first; authoritative terminology sources second.
- This is an alignment round, not an algorithm-selection round.
- Paper-specific claims are not treated as universal definitions.
- Missing conditions, incomparable assays, and disputed mechanisms are retained in `expert_review_queue.yaml`.

## Files

- `knowledge_alignment_report.md`: human-readable domain and computer expert views.
- `knowledge_alignment.yaml`: machine-readable Concepts, Indicators, Claims, Evidence, and optimization targets.
- `expert_review_queue.yaml`: unresolved content requiring expert validation.
- `corpus_manifest.tsv`: 47-file coverage manifest.
- `execution_trace.jsonl`: execution plan, tool calls, fallback failures, evidence decisions, and validation steps.

## Important interpretation boundary

The corpus contains a large pyroptosis/inflammasome context set. Those papers are useful for defining therapeutic endpoints and mechanism-related constraints, but they do not automatically provide photosensitizer structure-performance labels. Direct molecular-design evidence is concentrated in the phthalocyanine, porphyrin, AIE, conjugated-oligomer, rhenium, photocatalytic, mitochondria-targeted, membrane-targeted, and photopyroptosis papers.
