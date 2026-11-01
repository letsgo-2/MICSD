# Scientific Performance Evaluation — Round 1

## 1. Status, scope and execution boundary
This package establishes a confirmation-ready performance-evaluation workflow based on Execution Orchestration Round 3 and the `SDPD/` repository. The selected metrics are E(S1)−E(T1), charge, and symmetry. The materials expert requested RDKit, ORCA and statistical analysis; the computer expert provided a Slurm runtime environment.

No evaluation jobs, ORCA calculations, SDPD runs, plotting scripts or statistical analyses were executed in this round. No run artifacts were supplied, so all performance records are absent rather than inferred. `execution_authorized` is false.

## 2. Evaluation questions
| concern_id | target_perspective | question | priority | confirmation_status |
|---|---|---|---|---|
| CONC-R1-COMP | computer_expert | Are the SDPD optimization and evaluation outputs convergent, reproducible, resource-efficient and free of metric/predictor failures? | high | unconfirmed |
| CONC-R1-MAT | domain_expert | Do generated candidates preserve chemically valid porphyrin-centered structures, and do ORCA-derived E(S1)-E(T1) values agree with the SDPD proxy within a documented protocol? | critical | unconfirmed |
| CONC-R1-JOINT | cross_domain_team | Which candidates are suitable for experimental follow-up after combining computational proxy, chemical validity, uncertainty, synthesis and model-behavior evidence without collapsing them into one unapproved score? | high | unconfirmed |


## 3. Tool and environment registration
| tool_id | name | role | status | source | access_level | supported_metrics |
|---|---|---|---|---|---|---|
| TOOL-R1-RDKIT | RDKit | data_validator | proposed | {"type": "package", "location": "cluster environment; exact module/package path pending", "version": "pending"} | none | charge, symmetry, MW, candidate validity, uniqueness, novelty, diversity |
| TOOL-R1-ORCA | ORCA | domain_calculator | proposed | {"type": "package", "location": "cluster module/container; exact path pending", "version": "pending"} | none | E(S1)-E(T1), E(S1), E(T1), optional SOCME |
| TOOL-R1-SLURM | Slurm | benchmark_tool | proposed | {"type": "server", "location": "expert-provided Slurm cluster; exact cluster/account pending", "version": "pending"} | none | runtime, throughput, failure rate, resource usage, queue delay |
| TOOL-R1-SCIWORK | Python statistics stack | statistical_analyzer | proposed | {"type": "package", "location": "Pandas/NumPy/SciPy/statsmodels/matplotlib/seaborn; exact versions pending", "version": "pending"} | none | all observed metrics with compatible units |
| TOOL-R1-SDPDPLOT | SDPD plotting scripts | visualization_tool | proposed | {"type": "repository", "location": "SDPD/draw_picture/ and SDPD/configs/", "version": "repository commit pending"} | inspect_only | total_score, st_gap_raw, novelty, diversity, hit count, candidate distributions |


| environment_id | platform | scheduler | access_status | reproducibility_status | restrictions |
|---|---|---|---|---|---|
| ENV-R1-SLURM | cluster | Slurm | unknown | unregistered | ['No job submission without authorization', 'No production code/checkpoint modification', 'Preserve raw outputs'] |


Tools remain proposed because software names and a cluster description do not expose executable paths, versions, resource permissions or parameter authorization. The first authorized action must register those fields and run a tiny validation fixture; it must not submit a full array.

## 4. Metric evaluation protocol
| binding_id | metric_id | evaluation_role | value_types_allowed | direction | threshold | status |
|---|---|---|---|---|---|---|
| BIND-R1-STGAP | E(S1)-E(T1) | proxy_performance | ['predicted', 'computed', 'derived'] | minimize | {'round2_context': '<0.4 eV heuristic is context only', 'evaluation': 'report distributions and agreement; no automatic hard cutoff'} | proposed |
| BIND-R1-CHARGE | charge | constraint_check | ['implementation_score', 'computed'] | context_dependent | {'runtime': 'preserve current discrete scorer semantics', 'analysis': 'report pass-rate and raw formal charge separately'} | proposed |
| BIND-R1-SYMM | symmetry | proxy_performance | ['implementation_score', 'computed'] | maximize | {'runtime': 'rule-based 0/0.25/0.5/1 score', 'analysis': 'label as decoration symmetry, not global point-group symmetry'} | proposed |
| BIND-R1-MODEL | model_behavior | model_behavior | ['derived', 'implementation_score'] | context_dependent | {'status': 'not observed'} | not_observed |


The SDPD implementation score, predicted ST gap, ORCA-computed energy difference and any measured result are separate value types. They must not be merged into one column or treated as equivalent evidence. Charge and symmetry retain their SDPD semantics: formal-charge implementation scoring and decoration symmetry, respectively.

## 5. Evaluation protocols and statistics
| protocol_id | name | question | statistical_methods | missing_data_policy | minimum_sample_requirement | status |
|---|---|---|---|---|---|---|
| EP-R1-INGEST | SDPD result ingestion and provenance audit | Are all generated candidate/run records present, typed, deduplicated and traceable? | ['missingness table', 'duplicate/uniqueness audit', 'schema validation'] | report_missing | 1 | draft |
| EP-R1-MODEL | Model convergence, stability and resource evaluation | Does SDPD improve and stabilize selected metrics across steps and seeds without failure/resource bottlenecks? | ['rolling top-n mean', 'bootstrap CI by run', 'mixed-effects or run-level summaries when replicated', 'effect size', 'failure-rate CI'] | report_missing | 3 | draft |
| EP-R1-CHEM | RDKit candidate quality evaluation | Are generated molecules valid, unique, diverse, scaffold-retaining and chemically traceable? | ['validity/uniqueness rates with Wilson intervals', 'Morgan fingerprint diversity', 'novelty against reference library', 'charge/symmetry pass rates'] | report_missing | 30 | draft |
| EP-R1-ORCA | ORCA recomputation and SDPD proxy agreement | How well does the SDPD ST-gap proxy agree with ORCA calculations under one approved protocol? | ['MAE/RMSE/bias', 'Pearson/Spearman with caution', 'Bland-Altman limits', 'bootstrap CI', 'calibration/slope if sample supports'] | manual_review | 20 | draft |


### Statistical rules
- Use run-level replication for claims about RL behavior; individual generated molecules are not independent model replicates.
- Report median, mean, standard deviation, IQR and bootstrap confidence intervals where sample structure supports them.
- Use MAE, RMSE, bias, correlation with caution, and Bland–Altman analysis for SDPD versus ORCA agreement.
- Use Wilson intervals for validity/pass rates and report denominators.
- Use Benjamini–Hochberg only when multiple exploratory hypotheses are tested; record the tested family.
- Do not impute missing ORCA/Slurm/model values by default. Distinguish missing, failed, out-of-domain and not-authorized states.
- Preserve raw CSV/log/ORCA files; write cleaned tables and plotting data into separate directories.

## 6. Slurm and ORCA workflow
### Planned Slurm stages
1. Validate the environment and tool versions without submitting production jobs.
2. Ingest and standardize generated SMILES with RDKit.
3. Select a stratified ORCA subset by SDPD ST gap, charge score, symmetry score, validity, and failure status.
4. Generate one ORCA input per candidate with recorded charge, multiplicity, coordinates, method, basis, solvent and template hash.
5. Submit an ORCA Slurm job array only after authorization; retain job ID, array index, exit code, stdout/stderr, walltime, memory and ORCA termination status.
6. Parse ORCA outputs into a typed table; failed/non-converged jobs remain explicit missing records.
7. Run statistics and plots on the cleaned tables; never use implementation scores as substitutes for failed ORCA values.

### Required Slurm parameters to register before submission
`account`, `partition`, `time`, `cpus-per-task`, `mem`, `tmp/scratch policy`, `array range`, `module/container versions`, `ORCA executable`, `OMP/MKL thread settings`, `output/error paths`, `email/notification policy`, and `requeue policy`.

### ORCA parameter record
The ORCA method, basis, solvent model, charge/multiplicity policy, geometry source, excited-state roots, SOC settings, convergence thresholds and output parser version are all required fields. They are intentionally left pending because the materials expert requested ORCA but did not provide a scientific input template.

## 7. SDPD plotting-script plan
| visualization_id | title | scientific_question | chart_type | input/data_path | planned_script | figure_path | interpretation_limits |
|---|---|---|---|---|---|---|---|
| VIS-R1-TREND | SDPD reward and component trends by run | Does optimization improve total and selected component scores over steps relative to random sampling? | learning/trend curves with bootstrap bands |  |  | scientific_performance_evaluation_round1/figures/computer/sdpd_trends.png | ['No causal claim from trend', 'run-level replication required', 'implementation scores are not terminal biological performance'] |
| VIS-R1-CHEM | Candidate chemical-quality and metric evidence map | Which candidates are valid, unique, scaffold-retaining and chemically plausible across selected metrics? | candidate evidence matrix plus distribution/threshold panels |  |  | scientific_performance_evaluation_round1/figures/domain/candidate_evidence_matrix.png | ['charge/symmetry are implementation metrics', 'proxy values do not prove photodynamic efficacy', 'no aggregate score unless approved'] |
| VIS-R1-ORCA-AGREE | SDPD ST-gap proxy versus ORCA E(S1)-E(T1) | Is the SDPD ST-gap predictor sufficiently accurate for the generated-candidate domain under the approved ORCA protocol? | scatter with identity/regression and Bland-Altman panels |  |  | scientific_performance_evaluation_round1/figures/domain/orca_stgap_agreement.png | ['agreement is not biological validation', 'correlation is not causation', 'method/protocol scope must be shown'] |
| VIS-R1-PARETO | Joint candidate Pareto and evidence status view | Which candidates remain non-dominated after validity, selected metrics, uncertainty, synthesis and evidence status are retained separately? | Pareto scatter plus evidence matrix |  |  | scientific_performance_evaluation_round1/figures/joint/pareto_evidence.png | ['no unified utility without expert approval', 'Pareto membership is not experimental recommendation', 'missing values are not poor values'] |
| VIS-R1-MATRIX | Run/candidate provenance and missingness matrix | Which conclusions are blocked by missing, failed or non-comparable evidence? | evidence heatmap and missingness table |  |  | scientific_performance_evaluation_round1/figures/joint/evidence_matrix.png | ['coverage is not performance', 'missingness mechanisms require review'] |


Existing SDPD scripts to reuse or wrap after result artifacts exist: `SDPD/draw_picture/total_score_trend.py`, `raincloud.py`, `hit_count.py`, `est_trend.py`, `st_gap_distribution.py`, `radar.py`, `tsne.py`, and `dft_prediction.py`, with configs under `SDPD/configs/`. New adapters should be stored under `scientific_performance_evaluation_round1/scripts/` and must not overwrite SDPD production scripts.

## 8. Audience views
### Computer-expert view
Focus on convergence, seed stability, component-order correctness, validity/uniqueness/diversity, throughput, Slurm failures, ORCA failures, resource use, and reproducibility. Primary figures: trend curves, resource/failure summaries, evidence/missingness matrix, and seed/run distributions.

### Materials-expert view
Focus on RDKit-valid porphyrin-centered candidates, charge and decoration-symmetry semantics, ORCA convergence and E(S1)−E(T1) distributions, agreement between SDPD proxy and ORCA, anomalous structures, and candidates requiring experimental confirmation.

### Cross-domain joint view
Use a metric–candidate evidence matrix, Pareto fronts, candidate decision states, and a follow-up table. Do not compress proxy, computed, implementation-score and experimental values into one unapproved utility score.

## 9. Baselines and comparisons
| benchmark_id | name | source_type | metric_id | comparability | status | comparability_notes |
|---|---|---|---|---|---|---|
| BM-R1-RANDOM | SDPD random-sampling baseline | internal_baseline | st_gap/charge_score/symmetry_score | unknown | registered | ['No baseline output present in current inputs'] |
| BM-R1-TRAIN | Reference training library | internal_baseline | novelty/diversity | unknown | registered | ['Reference path must be confirmed'] |
| BM-R1-ORCA-REF | ORCA reference subset | expert_reference | E(S1)-E(T1) | unknown | registered | ['Protocol not yet supplied'] |


The random-sampling baseline and training reference are registered but not observed in the current inputs. Direct superiority claims are prohibited until paths, versions, conditions and outputs are confirmed. Literature values, if added later, must remain context-only unless recomputed under comparable conditions.

## 10. Adjustment recommendations
| proposal_id | target_stage | target_type | target_id | proposed_change | status | implementation_status |
|---|---|---|---|---|---|---|
| ADJ-R1-001 | execution_orchestration | additional_compute | WF-ORCH-R3 | Run a controlled, replicated SDPD evaluation only after authorization and tool/config confirmation. | proposed | not_started |
| ADJ-R1-002 | execution_orchestration | tool | ORCA | Add an authorized ORCA validation job and parseable provenance archive before evaluating SDPD proxy agreement. | proposed | not_started |


These are Skill-generated proposals, not expert-approved changes. They are reversible: no Round 3 configuration, SDPD source, checkpoint or expert data is modified by this package.

## 11. Review queue and required confirmations
| issue_id | category | question | required_expert | priority | blocking | status |
|---|---|---|---|---|---|---|
| PE-R1-001 | environment | Provide Slurm cluster hostname/account/partition, module or container versions, CPU/memory/time limits, scratch policy and output location. | computer expert | critical | True | open |
| PE-R1-002 | tool | Provide RDKit and ORCA versions, executable/module paths, approved ORCA method/basis/solvent/state protocol, and parameter authorization. | materials expert | critical | True | open |
| PE-R1-003 | results | Provide SDPD run artifacts, including diversity_memory.csv, seed/config metadata, component scores, raw ST-gap and failure logs. | computer expert | critical | True | open |
| PE-R1-004 | protocol | Approve the ORCA recomputation protocol and stratified sampling design for validating the SDPD ST-gap proxy. | materials expert | high | True | open |
| PE-R1-005 | statistics | Confirm independent replicate definition, minimum number of RL seeds/runs, bootstrap policy, missing-data policy and multiple-testing correction. | computer expert and interdisciplinary reviewer | high | True | open |
| PE-R1-006 | comparison | Confirm random-sampling and training-reference paths and conditions before direct baseline comparisons. | computer expert | high | False | open |
| PE-R1-007 | visualization | Approve the separate computer, materials-domain and cross-domain figure sets and evidence-state annotations. | computer and materials experts | medium | False | open |


## 12. Output and data paths
- Report: `scientific_performance_evaluation_round1/performance_evaluation_report_round1.md`
- Machine-readable plan: `scientific_performance_evaluation_round1/performance_evaluation_round1.yaml`
- Review queue: `scientific_performance_evaluation_round1/performance_review_queue_round1.yaml`
- Execution trace: `scientific_performance_evaluation_round1/execution_trace_round1.jsonl`
- Planned raw artifacts: `scientific_performance_evaluation_round1/raw/`
- Planned cleaned tables: `scientific_performance_evaluation_round1/clean/`
- Planned tables: `scientific_performance_evaluation_round1/tables/`
- Planned figures: `scientific_performance_evaluation_round1/figures/computer/`, `domain/`, `joint/`
- Inspected upstream repository, not modified: `SDPD/`

## 13. Confirmation gate
Before execution, confirm Slurm metadata, RDKit/ORCA/statistics versions, ORCA scientific settings, SDPD result paths, independent-run design, plotting approval, and job/resource authorization. Until then, this package contains plans and missing-result states only.