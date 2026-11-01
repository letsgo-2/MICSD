# Scientific Performance Evaluation — Round 1

## 1. Scope and execution status

This evaluation plan is based on `execution_orchestration_round3/` and the local `SDPD/` repository. Round 3 is a proposed workflow with `execution_authorized: false`; its report states that prediction, training, sampling, RL, dependency installation, and checkpoint changes were not performed. No generated candidate SMILES, execution result bundle, prediction table, model-run log, or ORCA result was located in that round's deliverables. Consequently, this round defines a reproducible evaluation workflow and required parameters, but reports no molecule-level scores, inferential statistics, model-performance estimates, or figures. Do not treat the plan as authorization to run SDPD, ORCA, or Slurm jobs.

## 2. Upstream subjects, metrics, and evidence boundary

| Subject | Evidence/status | Evaluation target |
|---|---|---|
| Generated porphyrin photosensitizers | Candidate result files absent from Round 3 | Validate and deduplicate canonical/isomeric SMILES; preserve candidate ID, decoration, scaffold, edit provenance, charge/protonation and conformer metadata. |
| SDPD runtime predictor `kagnn_3out` | Contract identified; inference not run | Outputs S1, T1, and ST gap (selected output index 2). Compare prediction to ORCA calculations on a held-out, chemically grouped validation set. |
| `decorator_prior` / RL actor | Startup checkpoint only; no round-3 pilot and no exported updated actor | Evaluate generation validity, uniqueness, scaffold/decoration coverage, metric distributions and resource use only when run artifacts exist. `run_rl.py` does not automatically save the updated actor. |
| Metric scorer | Source contract identified; not run | Components in order `[st_gap, charge_score, symmetry_score]`; current configured weights `[0.1, 0.3, 0.6]`. Charge and symmetry are proxies with unresolved semantics. |

Selected metrics inherited from Round 3: (1) E(S1)-E(T1)/ST gap, minimized conditionally on mechanism and method; (2) charge as application-specific descriptor/soft constraint; (3) decoration symmetry proxy, maximized conditionally. Round 3 states no universal thresholds. Preserve its unresolved questions on authorization, metric semantics, weight ordering, protonation/counterions, symmetry definition and fixtures.

## 3. Tool and environment registration

| Tool | Planned interface | Conditions / status |
|---|---|---|
| RDKit | Python data-validation/descriptors/conformer preparation; `Chem.MolFromSmiles`, canonical SMILES, `Descriptors`, Morgan fingerprints, ETKDG conformers | Installed version and available modules must be captured in a preflight; no environment was provided beyond Slurm availability. RDKit supports descriptors/structure checks, not reliable excited-state energies. |
| SDPD predictor | From `SDPD/data_preparation/prediction_model/rl_compatible_2025`: `python main.py`; input SMILES, expected S1/T1/ST_Gap | Contract only; confirm input/output file interface from script and config before execution; source/checkpoint immutable. |
| SDPD scorer | `multiple_score(smiles_list, weights, config, decorations)` in `data_preparation/scoring_strategy/score_function.py` | Use only after preflight and semantic approval. Preserve raw outputs and all components, not only weighted reward. |
| ORCA | Version-pinned executable and method/basis/input templates; evaluate S1 and T1 at the same declared geometry and calculate gap consistently | Expert requested ORCA; cluster ORCA installation/version/license/module and job limits are unknown and must be confirmed by the computer expert. No calculation submitted. |
| Slurm | `sbatch` array jobs, one candidate/conformer per task or bounded batches | Partition, account, QoS, walltime, memory, CPU/GPU policy, scratch location, ORCA module and maximum array size are not provided. Populate from cluster site configuration; no guessed account/partition. |
| Statistics/plots | Python + pandas/numpy/scipy/scikit-learn/matplotlib/seaborn (versions recorded) | Validate availability in the analysis environment. Use paired/grouped comparisons and uncertainty intervals; do not infer from generated candidates alone. |

## 4. Proposed gated workflow

1. **Authorization and immutable snapshot:** resolve Round 3 blocking review items; record SDPD git commit, hashes of source configs/checkpoints, software versions and cluster settings. Keep all outputs outside `SDPD/` in this round folder. Do not install packages or alter SDPD files/checkpoints without approval.
2. **Collect inputs:** after authorized generation, ingest a candidate CSV/JSONL containing stable `candidate_id`, SMILES, decoration, scaffold/family, generation run/seed, model checkpoint ID and provenance. Collect predictor outputs, raw component scores, run logs and resource records. Preserve missing values explicitly.
3. **RDKit structure preflight:** parse SMILES; record parse/sanitization failure reason; canonicalize and detect duplicates; retain isomeric SMILES; calculate formal charge, atom/bond counts, MW, cLogP, TPSA, HBD/HBA and rotatable bonds; Morgan fingerprint/ECFP4 and scaffold/decoration coverage; apply the agreed protonation/tautomer policy. Build explicit-H 3D conformers via ETKDGv3 (fixed recorded seed, e.g. 20261101) and MMFF94s minimization; record embedding/minimization status, conformer count and energy. RDKit conformer energies are preparation/QC only, not photophysical results.
4. **SDPD model and scorer evaluation:** after authorization, run the fixed checkpoint on exactly the same valid candidate set as ORCA; retain S1, T1, ST_Gap, raw and normalized values, charge/symmetry components, invalid reason and ring penalty. Confirm exact predictor input/output contract before invocation. Freeze checkpoint and configs for the evaluation cohort.
5. **ORCA reference calculations:** select a pre-registered, stratified subset spanning scaffold, charge state, decoration symmetry, and predictor range; include reference/known molecules if available and report selection. Use the same charge, multiplicity, protonation, tautomer and conformer protocol across candidates. Optimize ground-state geometry, frequency-check minima, then compute vertical singlet and triplet excited states at that geometry using a declared TD-DFT method/basis and solvent model. Initial proposal for expert review: `! PBE0 def2-TZVP TightSCF RIJCOSX`; `CPCM(water)` only if water is the declared environment. Request at least enough singlet/triplet roots to identify S1/T1; set `NRoots` and triplet treatment explicitly in ORCA blocks after version compatibility review. Benchmark a representative subset against a range-separated functional (e.g. CAM-B3LYP) and larger basis or higher-level reference before interpreting absolute gaps. These are proposed settings, not validated universal choices. Record ORCA version, full input/output, convergence, warnings, geometry, charge/multiplicity, functional, basis, solvent, roots, energies in eV and failed-job reason. Compute `gap = E(S1)-E(T1)` only when both states are valid and use the same geometry/method/units.
6. **Statistics:** primary model metric on the ORCA-evaluated holdout: MAE, RMSE, signed bias, Pearson r and Spearman rho for S1, T1 and ST gap; report 95% bootstrap CIs resampling by scaffold (not molecule) and counts. Provide calibration/regression plots and residuals. For generated-vs-reference cohorts, report descriptive distributions, median/IQR and bootstrap intervals; compare only matched chemistry/conditions, and distinguish exploratory from confirmatory tests. Correct multiple testing where multiple hypotheses are tested. Report validity/completion rates with denominators and confidence intervals. No p-values or rankings until actual observations exist.
7. **Reproducibility and synthesis:** save a row-level data table, QC/exclusion ledger, summary statistics, figures, Slurm scripts/logs and checksums; register each in `artifact_manifest`. Produce computer, computational-photochemistry/materials, and cross-domain summaries, separating expert-provided statements from Skill-inferred concerns. Update the review queue and propose reversible changes only after evidence exists.

## 5. Initial parameter contract

| Parameter | Initial planned value / required capture |
|---|---|
| Input identity | `candidate_id` unique; `smiles_isomeric`, canonical SMILES, `decoration`, scaffold family, generation seed/run ID, checkpoint hash |
| RDKit | Version; sanitization; tautomer/protonation policy; Morgan radius 2, 2048 bits; ETKDGv3 fixed seed; explicit hydrogens; MMFF94s status/energy |
| Predictor | `kagnn_3out`; outputs `[S1,T1,ST_Gap]`; selected index 2; checkpoint `SDPD/data_preparation/prediction_model/pretrained_models/best.pth` checksum; `c_path.yaml` copy/hash |
| Scorer | Current weights `[0.1,0.3,0.6]` recorded as inherited, not endorsed; scale `1.0`; invalid value `0.0`; capture every raw component and effective weight |
| ORCA | Version; PBE0/def2-TZVP/TightSCF/RIJCOSX proposal; solvent only after conditions approved; same-geometry singlet/triplet TD-DFT; explicit roots; convergence and failures retained |
| Slurm | `--array` bounds based on approved sample count; `--ntasks=1`; CPU/memory/time/partition/account/QoS/module/scratch filled from site configuration; ORCA parallelism matched to allocated CPUs |
| Statistical split | Scaffold-grouped train/calibration/test if training or recalibration is approved; never random molecule leakage across scaffold groups; freeze holdout before model tuning |
| Reproducibility | random seeds, UTC timestamps, git commit, file checksums, package versions, complete stdout/stderr, job ID and exit code |

## 6. Slurm/ORCA command template (not submitted)

The following is a parameter template only. Replace all `SITE_*` values with cluster-approved values, inspect ORCA syntax against the installed version, and obtain authorization before submission. Each array task should resolve candidate index to immutable input and write to a per-candidate scratch/output path.

```bash
#!/usr/bin/env bash
#SBATCH --job-name=ps_orca_round1
#SBATCH --array=0-SITE_ARRAY_MAX%SITE_CONCURRENCY
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=SITE_CPUS
#SBATCH --mem=SITE_MEMORY
#SBATCH --time=SITE_WALLTIME
#SBATCH --partition=SITE_PARTITION
#SBATCH --account=SITE_ACCOUNT
set -euo pipefail
module load SITE_ORCA_MODULE
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK}"
python prepare_orca_input_round1.py --index "${SLURM_ARRAY_TASK_ID}" \
  --manifest candidates_round1.csv --outdir "${SLURM_SUBMIT_DIR}/orca_inputs_round1"
orca "${SLURM_SUBMIT_DIR}/orca_inputs_round1/${SLURM_ARRAY_TASK_ID}.inp" \
  > "${SLURM_SUBMIT_DIR}/orca_outputs_round1/${SLURM_ARRAY_TASK_ID}.out"
```

The `SITE_*` placeholders intentionally prevent accidental submission with invented cluster settings. Add robust signal handling, scratch staging/cleanup, output existence checks, and retry policy in an implementation script after site paths are confirmed. Do not launch an array before confirming sample count and resource limits.

## 7. Plotting-script plan

Planned script: `plot_performance_round1.py`; input normalized `performance_records_round1.csv` plus `model_validation_round1.csv`; output `figures_round1/` and `tables_round1/`. Use deterministic style, explicit units, confidence intervals, sample counts and provenance captions; save PNG (review) and SVG/PDF (publication/editable) with filenames suffixed `round1`.

| Figure/table | Purpose / encoding |
|---|---|
| `fig01_metric_distributions_round1.png` | ST-gap, S1, T1 and descriptor distributions by scaffold/charge class; show n and missingness; no synthetic data. |
| `fig02_predicted_vs_orca_stgap_round1.png` | Predictor vs ORCA ST gap; identity line, fitted trend, MAE/RMSE and scaffold-bootstrap CI; separate calibration/test if relevant. |
| `fig03_residuals_round1.png` | Residual vs ORCA value and residual distribution; annotate bias and outliers with candidate IDs in accompanying table. |
| `fig04_metric_tradeoffs_round1.png` | ST-gap vs charge and symmetry descriptors; color by scaffold, mark Pareto set only after metric directions/definitions are approved. |
| `fig05_generation_qc_round1.png` | Valid/invalid, unique/duplicate, scaffold coverage and ORCA completion rates with denominators. |
| `fig06_resource_performance_round1.png` | Slurm walltime/CPU/memory vs molecule size or conformer count and completion status; only if job accounting data available. |
| `table01_candidate_metrics_round1.csv` | Per-candidate identity, chemistry, model outputs, ORCA reference, scorer components, provenance, QC/failure fields. |
| `table02_model_statistics_round1.csv` | n, MAE, RMSE, bias, Pearson/Spearman, scaffold-bootstrap 95% CIs per target and split. |
| `table03_run_summary_round1.csv` | validity, uniqueness, coverage, completion, resource summaries; no inferential claims absent sample sizes. |

Audience views: computer expert—checkpoint/config hashes, predictive validation, runtime/resource/failure data; photochemistry/materials—conditioned S1/T1/gap with method uncertainty and charge/symmetry caveats; joint view—Pareto and trade-offs only after definitions are approved. All should state that TD-DFT values are method-dependent and are not experimental validation.

## 8. Inferred concerns and provisional adjustment guidance

These are Skill-inferred priorities, not opinions supplied by named experts: computational chemist—surrogate calibration and scaffold leakage; materials expert—charge/protonation, solvent, aggregation and meaningful symmetry definition; computer expert—checkpoint identity, invalid rate, sampling coverage and Slurm cost; project owner—authorization and reproducibility. Current evidence supports no performance-driven model/weight changes. First priority is obtain candidate/run artifacts, resolve blocking review items, then run the authorized paired validation. Preserve weight `[0.1,0.3,0.6]` only as a snapshot; do not recommend it scientifically until component dominance and proxy validity are measured. Any later changes should be logged as reversible proposals with evidence and expert status.

## 9. Limitations and review gates

No actual candidates or result data were available; no tool execution, ORCA calculation, Slurm submission, SDPD command, statistical test or figure generation was performed. Required gates: authorize the evaluation scope; confirm candidate data and model/checkpoint; approve charge/protonation/counterion and symmetry definitions; approve ORCA conditions/method and cluster parameters; approve holdout selection and fixtures. See `performance_review_queue_round1.yaml`.

## Dialogue-based status reconciliation (2026-10-31)

The current output states have been reconciled with the saved expert dialogue at the user's request. General knowledge acceptance, task inputs, selected metric roles, and the synthesizability requirement are recorded only within their supported scope. Existing disputes, unanswered review questions, missing protocols, numerical thresholds, route validation, model-validation gaps, and execution-authorization requirements remain explicit. No scientific values or execution permissions are newly certified, and the historical execution trace is unchanged. The scope and dialogue excerpts are recorded in the expert_feedback_reconciliation metadata of `performance_evaluation_round1.yaml`.
