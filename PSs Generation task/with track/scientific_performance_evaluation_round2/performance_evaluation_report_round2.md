# Scientific Performance Evaluation — Round 2

## 1. Revision status and observed evidence
This Round 2 update incorporates the completed `meloculardftcal` pipeline, its English agent interface, recorded environment report, `pic16_s1` metrics snapshot, and Round 1 evaluation plan. Unlike Round 1, observed computed records are now available. No new pipeline execution was initiated by this update; the analysis is based on committed/generated artifacts already present in the repository.

Pipeline artifact scope: `pic16_s1`, 222 input rows, complete v22 row coverage, and source-linked hashes in `reports/pic16_s1/metrics.json`. Raw ORCA logs are not bundled, so normal termination and full scheduler provenance remain unknown.

## 2. Toolchain and parameter update
| tool_id | name | status | version_or_target | entrypoint | key_parameters | observed_limitation |
|---|---|---|---|---|---|---|
| TOOL-R2-PIPELINE | meloculardftcal workflow | validated_outputs_available | repository commit not recorded in reports | meloculardftcal/workflow.py | {} | no raw ORCA logs bundled; no normal-termination counts |
| TOOL-R2-ORCA | ORCA 6.0.1 target environment | unavailable_at_reported_environment | 6.0.1 target | meloculardftcal/01_structure_preparation and 02_cluster_execution | {} | ORCA_BIN unset; sbatch/squeue unavailable in recorded environment |
| TOOL-R2-RDKIT | RDKit 2025.9.3 | available_recorded | 2025.9.3 | meloculardftcal/04_data_processing/addrdkit.py | {} | no direct validation of all descriptor semantics in this review |


Recorded local environment: Python 3.12.2, RDKit 2025.9.3, NumPy 1.26.4, pandas 2.2.2, SciPy 1.15.2, Open Babel 3.1.0, Open MPI 4.0.3. The interface targets ORCA 6.0.1/OpenMPI 4.1.6/UCX 1.15.0 on Slurm, but the recorded capability report found ORCA unavailable because `ORCA_BIN` was unset and `sbatch`/`squeue` unavailable. This discrepancy is now explicit rather than treated as a successful cluster execution.

### Pipeline stage mapping
The completed result path is S10 structure preparation → S20/S21 optimization generation/submission → S30/S31 TD generation/submission → S40/S41 parsing → S42 merge → S50 source merge → S51 RDKit enrichment → S60 metrics → S70 analysis. The artifact contains v20/v21/v22 tables and metrics, but raw logs and run manifests are absent from the inspected reports.

## 3. Observed performance records
| record_id | metric_id | value | unit | value_type | sample_size | data_quality | missing_reason |
|---|---|---|---|---|---|---|---|
| PR-R2-001 | pipeline_coverage | 1.0 | fraction | computed | 222 | high |  |
| PR-R2-002 | no_imaginary_frequency_rate | 0.8603603603603603 | fraction | computed | 222 | high |  |
| PR-R2-003 | pareto_gap_soc_ratio | 2 | candidates | computed | 222 | high |  |
| PR-R2-004 | pareto_gap_soc_ratio_3d | 14 | candidates | computed | 222 | high |  |
| PR-R2-005 | reference_gap_soc_ratio_better_or_equal_no_imaginary | 0.8167539267015707 | fraction | computed | 191 | medium | Reference is flagged imaginary and is not a validated minimum. |
| PR-R2-006 | targeting_window_match_count | 0 | candidates | computed | 222 | high |  |
| PR-R2-007 | S1_wavelength_nm | {'median': 622.85, 'p10': 563.91, 'p90': 657.08} | nm | computed | 222 | high |  |


### Key observed results
- **Coverage:** 222/222 rows reached v22 (100% table coverage); all required columns are present, IDs are unique, and SMILES are present.
- **Geometry/QC:** 191/222 rows have no imaginary frequency (86.0%); 31 rows remain flagged imaginary. Normal termination rates are unavailable because raw logs are intentionally not bundled.
- **Pareto structure:** 2/222 candidates are non-dominated for minimizing `min_positive_S1-Ti` and maximizing `max_SOCME_over_deltaE_S1_Ti_value`; the 3D gap/SOCME/ratio frontier contains 14/222.
- **Reference comparison:** 81.7% of no-imaginary rows are better-or-equal to the selected reference on the 3D comparison, but the reference itself is marked `Imaginary=Yes` and is explicitly not a validated minimum. This is contextual, not a superiority claim.
- **Targeting window:** the generic LogP 1–5 / TPSA 20–120 Å² window matches 0/222 candidates and is explicitly marked unsuitable for this chemical space.
- **Spectral distribution:** median S1 wavelength is 622.85 nm, with p10 563.91 nm and p90 657.08 nm across 222 rows.

## 4. Findings and interpretation boundaries
| finding_id | observation | interpretation | confidence | decision_relevance | expert_status |
|---|---|---|---|---|---|
| FIND-R2-001 | The v22 pipeline has complete row coverage for 222/222 inputs, but ORCA normal-termination rates are null and the recorded environment reports ORCA, sbatch and squeue unavailable. | The data table is coverage-complete but execution provenance is insufficient for confident rerun-level or terminal-DFT claims. | high | blocks environment-dependent optimization changes | pending |
| FIND-R2-002 | 191/222 candidates have no imaginary frequencies; 31/222 are marked imaginary. | The imaginary subset requires QC diagnosis before it is treated as equally valid for ranking or reward calibration. | high | defines a QC gate for next optimization | pending |
| FIND-R2-003 | The 2D gap-vs-SOCME/gap ratio Pareto set contains 2/222 candidates; the 3D set contains 14/222. Reference comparisons are reported, but the reference has Imaginary=Yes and is explicitly not a validated minimum. | The candidate space contains a small trade-off frontier, but the frontier and reference comparison are not sufficient to alter RL rewards without protocol-calibrated validation. | high | supports stratified validation before reward update | pending |
| FIND-R2-004 | The configured LogP 1–5 and TPSA 20–120 Å² targeting window matches zero of 222 candidates and is marked unsuitable for this chemical space. | The generic targeting window should not be used as a hard optimization constraint for this porphyrin-centered chemical space. | high | prevents an all-candidate rejection in the next optimization | pending |


The findings distinguish observed counts from interpretations. The results support a QC and calibration step, not an immediate RL reward change. The 2D/3D Pareto counts show a compact trade-off frontier but do not establish biological efficacy, and the reference comparison cannot validate superiority because the reference has an imaginary frequency.

## 5. Next optimization recommendation
### Recommended next step: evaluation-gated proxy calibration before RL reward modification
1. Restore and document the intended ORCA/Slurm environment: provide `config/cluster.env`, verify ORCA 6.0.1 target, Slurm commands, MPI/UCX versions, and write a run manifest.
2. Diagnose the 31 imaginary-frequency rows. Retain them in raw data, but make no-imaginary status an explicit QC stratifier and report sensitivity of Pareto results to their inclusion/exclusion.
3. Recompute a stratified validation set with the same protocol: all 2D Pareto candidates, 3D frontier candidates, interior candidates, boundary candidates, and representative failures. Compare SDPD ST-gap predictions with ORCA values using MAE, RMSE, bias, Bland–Altman limits and convergence labels.
4. Only if proxy agreement is acceptable should the next RL experiment modify reward weighting or add a calibrated SOCME/gap-ratio component. Use an ablation against the existing reward, preserve the current configuration, and compare replicated seeds.
5. Do not activate the generic LogP/TPSA window as a hard constraint. Replace it with a scaffold-specific, expert-approved target or retain it as context-only until formulation/biological evidence exists.

### Why this is the recommended order
Changing the RL reward before resolving environment provenance, imaginary-frequency QC and predictor-to-ORCA agreement would confound model improvement with evaluation artifacts. The completed pipeline demonstrates data coverage and candidate trade-offs, but not that the proxy is calibrated for the generated chemical space.

## 6. Updated views
### Computer-expert view
The main bottleneck is reproducibility/provenance: ORCA and Slurm are unavailable in the recorded environment, normal termination is unknown, and raw logs are absent. The next engineering task is environment restoration plus a stratified calibration job, followed by a controlled reward ablation.

### Materials-expert view
The v22 table is chemically information-rich: it contains S1/T1 energies, oscillator strength, wavelength, SOCME and SOCME/gap-ratio descriptors, HOMO/LUMO/gap, LogP, TPSA, SA score and imaginary status. The 31 imaginary cases require explicit QC treatment; generic LogP/TPSA windows are not suitable for this porphyrin-centered distribution.

### Cross-domain joint view
The evidence supports `requires_additional_compute` for the selected Pareto candidates and `promising_but_uncertain` only for candidates that pass QC and proxy calibration. No candidate is promoted to experimental recommendation from these artifacts alone.

## 7. Adjustment proposals
| proposal_id | target_type | target_id | proposed_change | status | implementation_status |
|---|---|---|---|---|---|
| ADJ-R2-001 | tool | TOOL-R2-ORCA/TOOL-R2-SLURM | Restore/register the intended cluster environment and rerun capability checks before any new optimization. | proposed | not_started |
| ADJ-R2-002 | additional_compute | imaginary-frequency subset | Run a QC-focused rerun or frequency/geometry diagnosis for the 31 imaginary cases before ranking them as valid optimization candidates. | proposed | not_started |
| ADJ-R2-003 | additional_compute | SDPD-vs-ORCA proxy calibration | Stratify a validation set across ST-gap/SOCME Pareto regions and recompute with the same ORCA protocol; estimate MAE, bias, Bland-Altman limits and calibration before changing RL weights. | proposed | not_started |
| ADJ-R2-004 | metric | LogP/TPSA targeting window | Replace the generic window with a scaffold-specific descriptive range or remove it from reward/selection until a validated biological/formulation target exists. | proposed | not_started |


## 8. Updated review queue
| issue_id | category | question | required_expert | priority | blocking | status |
|---|---|---|---|---|---|---|
| PE-R2-001 | environment | Re-establish the intended ORCA/Slurm environment and produce a fresh capability report with ORCA_BIN, sbatch, squeue and target versions available. | computer expert | critical | True | open |
| PE-R2-002 | protocol | Provide raw ORCA logs or normal-termination counts for the 222-row completed table and confirm whether all values are generated under one protocol. | materials expert | critical | True | open |
| PE-R2-003 | quality | Diagnose the 31 imaginary-frequency candidates and decide the QC inclusion rule for Pareto/ranking. | materials expert | high | True | open |
| PE-R2-004 | calibration | Run stratified SDPD-vs-ORCA agreement analysis for the Pareto candidates and interior/boundary candidates before changing RL reward weights. | materials and computer experts | critical | True | open |
| PE-R2-005 | metric | Approve a scaffold-specific replacement or removal of the generic LogP/TPSA window that produced zero hits. | materials expert | high | True | open |
| PE-R2-006 | optimization | After QC and proxy calibration, select whether the next optimization should alter the ST-gap reward, add SOCME/gap-ratio calibration, or prioritize chemical validity/robustness. | joint computer/materials experts | critical | True | open |


## 9. Output paths
- Report: `scientific_performance_evaluation_round2/performance_evaluation_report_round2.md`
- Machine-readable update: `scientific_performance_evaluation_round2/performance_evaluation_round2.yaml`
- Review queue: `scientific_performance_evaluation_round2/performance_review_queue_round2.yaml`
- Execution trace: `scientific_performance_evaluation_round2/execution_trace_round2.jsonl`
- Completed pipeline inspected: `meloculardftcal/`
- Primary observed metrics: `meloculardftcal/reports/pic16_s1/metrics.json`
- Environment record: `meloculardftcal/reports/environment.json`

## 10. Provenance and limitations
All observed values in this report are labeled computed and linked to local artifacts. The update did not run the pipeline, submit jobs, or fabricate ORCA values. Normal termination, raw-log provenance, protocol commit identity and direct SDPD-vs-ORCA agreement remain unresolved.