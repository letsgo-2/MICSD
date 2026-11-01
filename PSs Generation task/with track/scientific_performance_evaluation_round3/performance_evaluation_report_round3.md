# Scientific Performance Evaluation — Round 3

## 1. Revision scope and status
This Round 3 update revises Performance Evaluation Round 2 after the materials scientist requested a synthesizability constraint. It preserves all observed pipeline results, ORCA/Slurm limitations, and prior calibration blockers. No new computation or pipeline execution was initiated.

The added constraint is deliberately **soft and provisional**: the existing `SA_Score` is a fast synthetic-accessibility heuristic, not a retrosynthetic route, synthesis-success probability, or experimental feasibility guarantee.

## 2. Observed synthesizability evidence
| record_id | metric_id | value | unit | sample_size | data_quality | missing_reason |
|---|---|---|---|---|---|---|
| PR-R3-001 | SA_Score | {'count': 222, 'min': 5.022, 'p10': 5.8019, 'p25': 6.03125, 'median': 6.2455, 'mean': 6.310540540540541, 'p75': 6.546250000000001, 'p90': 6.963, 'max': 7.935} | SA score (approximately 1–10; lower generally easier) | 222 | high | No retrosynthesis routes, reaction success labels, or experimental synthesis outcomes are present. |


Observed `pic16_s1` SA distribution: minimum 5.022, p10 5.8019, p25 6.03125, median 6.2455, mean 6.3105, p75 6.54625, p90 6.963, maximum 7.935. The local interface describes SA_Score as approximately 1–10, with lower values generally indicating easier synthesis. No route-level or experimental synthesis data are present.

## 3. Synthesizability constraint
| constraint_id | metric_id | role | direction | hard_cutoff | provisional_bands | implementation | limitations |
|---|---|---|---|---|---|---|---|
| CONSTRAINT-R3-SYNTH | SA_Score | soft_constraint_and_ranking_feature | minimize | False | {'preferred': '<= dataset median 6.2455 for first-pass prioritization', 'review': '6.2455–6.963 (median to p90)', 'high_difficulty': '>6.963 (above p90)', 'note': 'Bands are empirical dataset stratification, not universal chemical thresholds.'} | Retain all candidates in raw data; add SA-based soft penalty or Pareto axis after validity/QC gates. Do not reject solely by SA_Score. | ['heuristic fragment/complexity proxy', 'not a retrosynthetic route', 'porphyrin/metallated macrocycle domain calibration absent', 'no experimental synthesis labels', 'does not capture reagent availability, yield or route-specific failure'] |


### Recommended use
Apply the order: **validity → imaginary-frequency/QC status → SA soft label → calibrated photophysical proxy → Pareto/selection**. Do not reject a candidate solely because SA_Score is above the p90 band. High-SA Pareto candidates should be routed to route review rather than silently discarded.

## 4. Updated toolchain and protocol
| tool_id | name | status | entrypoint | supported_metrics | known_failures |
|---|---|---|---|---|---|
| TOOL-R3-SA | RDKit SA Score implementation | available_recorded | meloculardftcal/04_data_processing/addrdkit.py | SA_Score, synthesizability proxy | no retrosynthesis route, macrocycle/metal domain uncertainty |


| protocol_id | name | question | statistical_methods | missing_data_policy | status |
|---|---|---|---|---|---|
| EP-R3-SYNTH | Synthesizability-aware candidate evaluation | Does adding a soft SA-based constraint improve practical candidate prioritization without eliminating photophysically promising molecules? | ['SA distribution and quantiles', 'SA-band Pareto coverage', 'rank correlation with selected photophysical metrics', 'bootstrap band proportions when replicate batches exist', 'route-level validation when available'] | report_missing | draft |


## 5. Updated findings
| finding_id | observation | interpretation | confidence | decision_relevance | expert_status |
|---|---|---|---|---|---|
| FIND-R3-001 | All 222 v22 candidates have an SA_Score distribution with median 6.2455, p90 6.963 and maximum 7.935. | SA_Score can support relative synthesizability triage and a soft Pareto axis, but the absence of route-level or experimental synthesis data prevents a hard synthesizability constraint. | high | add soft synthesizability prioritization without replacing photophysical/QC gates | pending |


The observed SA distribution supports relative triage and a soft Pareto axis. It does not support a universal hard cutoff, particularly for charged porphyrin/metallated macrocycles, because the current evidence lacks retrosynthesis routes, reaction-success labels, reagent availability, yields and experimental synthesis outcomes.

## 6. Updated next-optimization recommendation
1. Keep the previously recommended environment restoration, imaginary-frequency QC, and SDPD-versus-ORCA calibration steps.
2. Add SA_Score as a soft ranking/constraint feature using empirical dataset bands: preferred ≤6.2455, review 6.2455–6.963, high difficulty >6.963.
3. Run a three-arm ablation only after proxy calibration: baseline selection without SA, soft-SA selection, and route-validated-SA selection if retrosynthesis data become available.
4. Compare arms using replicated seeds, QC pass rate, Pareto coverage, SA distribution, valid/unique/diverse candidate rates, and subsequent ORCA/experimental follow-up yield.
5. Do not convert SA into a hard RL rejection rule until materials/synthetic experts validate its domain behavior.

## 7. Visualization additions
| visualization_id | title | scientific_question | chart_type | data_path | figure_path | interpretation_limits |
|---|---|---|---|---|---|---|
| VIS-R3-SA-PARETO | Photophysical Pareto front colored by synthesizability band | Which photophysical trade-off candidates remain attractive after SA-based soft prioritization? | Pareto scatter with SA bands and QC markers | scientific_performance_evaluation_round3/clean/candidate_sa_pareto.csv | scientific_performance_evaluation_round3/figures/joint/sa_pareto.png | ['SA is heuristic', 'not a route success probability', 'no hard rejection'] |
| VIS-R3-SA-DISTRIBUTION | SA score distribution and QC stratification | How does synthesizability proxy vary across imaginary-frequency/QC and candidate groups? | distribution/violin or ECDF with QC stratification | scientific_performance_evaluation_round3/clean/candidate_sa_metrics.csv | scientific_performance_evaluation_round3/figures/domain/sa_distribution.png | ['distribution is local to pic16_s1', 'no universal cutoff', 'SA does not establish synthesis success'] |


## 8. Expert views
### Materials-expert view
Synthesizability is now represented explicitly, but only as a soft constraint. The current SA distribution indicates that the generated chemical space is concentrated around moderately difficult heuristic scores; route-level validation is needed before using SA as a hard gate.

### Computer-expert view
SA can be computed cheaply and deterministically from standardized SMILES, making it suitable for a feature, soft penalty, and ablation. It should be logged separately from photophysical proxy scores and applied after validity/QC checks.

### Cross-domain joint view
The preferred candidate state is `promising_but_uncertain` only when the candidate passes QC, has acceptable SA band or an explicit route-review flag, and remains competitive on calibrated photophysical metrics. High-SA Pareto candidates should be `requires_additional_compute` or `requires_experiment`, not automatically rejected.

## 9. Adjustment proposal
| proposal_id | target_type | target_id | proposed_change | status | implementation_status |
|---|---|---|---|---|---|
| ADJ-R3-001 | constraint | CONSTRAINT-R3-SYNTH | Add SA_Score as a soft constraint/ranking feature after validity and imaginary-frequency QC; use dataset-relative bands and retain high-SA candidates for review. | proposed | not_started |


## 10. Review queue
| issue_id | category | question | required_expert | priority | blocking | status |
|---|---|---|---|---|---|---|
| PE-R3-001 | constraint | Approve SA_Score as a soft constraint/ranking feature rather than a hard rejection rule. | materials scientist | high | True | open |
| PE-R3-002 | synthesizability | Provide retrosynthesis routes, reaction-success labels, or expert route assessments for a stratified candidate subset. | materials and synthetic chemistry experts | high | True | open |
| PE-R3-003 | domain_calibration | Assess whether the SA implementation is calibrated for porphyrin, charged, and metallated macrocycles in this chemical space. | materials scientist | high | False | open |
| PE-R3-004 | workflow | Define the order of synthesizability, imaginary-frequency QC, and photophysical screening gates in the next optimization. | computer and materials experts | high | True | open |
| PE-R3-005 | optimization | After SA integration, decide whether to run an ablation comparing no-SA, soft-SA and route-validated-SA selection. | joint computer/materials experts | critical | True | open |


## 11. Output paths
- Report: `scientific_performance_evaluation_round3/performance_evaluation_report_round3.md`
- Machine-readable update: `scientific_performance_evaluation_round3/performance_evaluation_round3.yaml`
- Review queue: `scientific_performance_evaluation_round3/performance_review_queue_round3.yaml`
- Execution trace: `scientific_performance_evaluation_round3/execution_trace_round3.jsonl`
- SA implementation: `meloculardftcal/04_data_processing/sascorer.py`
- SA enrichment: `meloculardftcal/04_data_processing/addrdkit.py`
- Observed metrics: `meloculardftcal/reports/pic16_s1/metrics.json`

## 12. Provenance and limitations
The SA record is computed from the completed v22 artifact and is not a new run. No new ORCA, Slurm, retrosynthesis or synthesis computation was executed. The added constraint remains pending materials and synthetic-chemistry expert approval.