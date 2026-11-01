# Scientific Performance Evaluation — Round 2

## 1. Scope, inheritance, and provenance

Round 2 updates `../performance_evaluation_round1/` using the cloned repository at `../meloculardftcal/`, its `AGENT_INTERFACE.md` → `AGENT_INTERFACE_EN.md`, machine-readable `config/agent_interface.json`, reference metrics, environment record, and generated 60-molecule tables. The source revision inspected is the checked-out clone from `https://github.com/letsgo-2/meloculardftcal.git`; repository data artifacts include SHA-256 entries in `reports/pic16_s1/metrics.json`.

This is **not** an evaluation of the SDPD `kagnn_3out` prediction model: the inspected `meloculardftcal` workflow calculates molecular electronic properties by ORCA and post-processes them, and no paired model predictions or model checkpoint performance dataset was found. It does provide electronic-property data, pipeline coverage/QC, Pareto summaries, and two generated 60-candidate tables. Conclusions below are scoped accordingly.

The interface is declarative and the generator scripts are authoritative. Read-only interface queries were run (`python3 workflow.py show`, `stages`, `parameters`, `paths --check`). Existing metrics and candidate tables were inspected and summarized locally. No ORCA calculation, Slurm submission, workflow mutation, or script execution that regenerates data was performed in this evaluation. `reports/runs/` contains no JSON run manifests, raw ORCA logs are intentionally absent, and the environment report records ORCA and Slurm commands unavailable in the environment that generated it. Therefore the bundled metrics demonstrate persisted outputs, but do not provide live job accounting or raw-log termination verification.

## 2. Toolchain and parameters registered from the interface

### Software and recorded runtime

| Component | Registered/reference setting | Recorded environment (`reports/environment.json`) |
|---|---|---|
| Python | `>=3.9` | 3.12.2 on Linux x86_64 |
| ORCA | parser target/version 6.0.1; shared OpenMPI 4.1.6 AVX2 build; executable via `ORCA_BIN` | unavailable in recorded runtime; `ORCA_BIN` unset |
| MPI / UCX | OpenMPI 4.1.6 / UCX 1.15.0 | environment report reports `mpirun` Open MPI 4.0.3, so not the reference cluster MPI |
| Scheduler | Slurm | `sbatch` and `squeue` unavailable in recorded runtime |
| Structure/chemistry | Open Babel CLI + RDKit | Open Babel 3.1.0; RDKit 2025.9.3 |
| Analysis | NumPy 1.26.4, pandas 2.2.2, SciPy 1.15.2, Matplotlib 3.8.4, Seaborn 0.13.2, scikit-learn 1.4.2 | matches recorded environment; `umap_learn` unavailable |
| Reference hardware | 2 × AMD EPYC 7H12, 128 physical/256 logical CPU, ~503 GiB, no GPU | environment snapshot instead reports Intel i7-14700K, 28 logical CPUs, 62.48 GiB; not the target HPC host |

The differing local/reference environment is material: do not treat local capability capture as a successful cluster preflight. Resolve the actual ORCA/MPI/UCX/Slurm environment on the calculation cluster before submitting jobs.

### Quantum profiles

| Profile | Registered protocol |
|---|---|
| `opt_standard` | B3LYP/def2-SVP, Opt+Freq, RIJCOSX, CPCM(Water); 64 MPI ranks, 3000 MB `%maxcore` per rank |
| `opt_heavy_zora` | PBE0-D3BJ/ZORA-def2-TZVP/SARC/J, Opt+Freq, RIJCOSX, TightSCF, CPCM(Water); 64 ranks, 3000 MB/rank |
| `td_standard` | wB97X-D3/def2-TZVP, RIJCOSX, TightSCF, CPCM(Water); 10 roots, triplets and SOC enabled, `MORead`, optimized XYZ; 32 ranks, 3000 MB/rank |
| `td_heavy_zora` | wB97X-D3/ZORA-def2-TZVP/SARC/J, RIJCOSX, RI-SOMF(1X), TightSCF, CPCM(Water); 10 roots, triplets and SOC enabled, `MORead`; 32 ranks, 3000 MB/rank |

Reference scheduler defaults: partition `amd_512q`, one node, 64 optimization ranks/32 TD ranks, one OMP thread per rank, maximum 20 concurrent jobs, 1800-second polling interval. The per-rank memory product is 187.5 GiB for optimization and 93.75 GiB for TD. The interface cautions that actual peak memory can exceed `ranks × maxcore`; verify scheduler policy, scratch capacity, molecule size and scaling before changing these values. `SBATCH_PARTITION`, `SBATCH_NODES`, `SBATCH_NTASKS`, `WORK_DIR`, `ORCA_BIN`, `MODULE_INIT`, and `ORCA_MODULE` are site variables; cluster secrets/config are not committed.

### Workflow and analysis interfaces

Stable stages: preflight `S00`; structure preparation `S10`; optimize input generation/submission/QC `S20-S22`; TD input generation/submission/QC `S30-S32`; parsing and DFT merge `S40-S42`; source merge and RDKit enrichment `S50-S51`; validation metrics `S60`; plot analysis `S70`; molecular/scaffold visualization `S80`. Submission stages are external mutations and require `submit_slurm_jobs` authority. Metrics entry point is `07_validation/collect_metrics.py`; plots live under `05_analysis/plotters/`; RDKit enrichment is `04_data_processing/addrdkit.py`. For each change, copy a generator or use a branch, change one protocol dimension per benchmark, regenerate into an isolated directory, inspect generated input and job script, test a small reference subset, then record exact parameters and commit.

Use repository-root-relative paths. Preserve source row ordering because the TD parser maps the ID in log filenames to source row `id - 1`. Do not compare energies or rank molecules across incompatible quantum protocols without protocol labels.

## 3. Available data and quality/performance results

### Core `pic16_s1` reference dataset

The committed metrics snapshot (`reports/pic16_s1/metrics.json`, generated 2026-07-25) records 222 rows at each of input, TD-summary, v20, v21, and v22 stages; all 222 v22 rows complete, all required columns are present, all IDs unique, and all SMILES present. Of these, 191 have `Imaginary=No` (86.04%). Normal optimization/TD termination counts are null because raw ORCA logs are not bundled. Thus v22 table coverage is complete, but the underlying job-log completion rate cannot be independently checked.

Selected distribution summary over 222 rows:

| Metric | Median | Mean | Range |
|---|---:|---:|---:|
| S1 energy (eV) | 1.9905 | 2.0286 | 1.3144–2.2201 |
| T1 energy (eV) | 1.3032 | 1.3475 | 0.3315–1.5792 |
| `S1-T1` (eV) | 0.6610 | 0.6811 | 0.5968–1.6205 |
| Minimum positive S1–Ti gap (eV) | 0.1098 | 0.1351 | 0.0024–0.6202 |
| Max SOCME (cm⁻¹) | 1.5904 | 1.4332 | 0.0224–3.5284 |
| Max SOCME/ΔE (cm⁻¹/eV) | 3.4577 | 6.2596 | 0.0709–110.1646 |
| S1 wavelength (nm) | 622.85 | 614.31 | 558.5–943.2 |
| LogP | 14.0835 | 14.5565 | 3.767–28.006 |
| TPSA (Å²) | 72.88 | 96.60 | 57.36–301.68 |
| SA score | 6.2455 | 6.3105 | 5.022–7.935 |

The SOCME/ΔE mean (6.26) greatly exceeds its median (3.46), with maximum 110.16; this indicates a strong upper tail/outlier sensitivity and supports robust summaries, log/quantile visualization, and candidate-level inspection rather than mean-only optimization. This is a distributional observation, not a claim that these values are experimental outcomes.

### Pareto and reference comparisons

- Two-objective gap-versus-SOCME/ΔE: 2/222 nondominated (0.90%).
- Three-objective gap/SOCME/SOCME/ΔE: 14/222 nondominated (6.31%).
- The configured visualization targeting window LogP 1–5 and TPSA 20–120 Å² matches 0/222. It is explicitly a visualization default, not an expert-approved biological target; the observed zero-hit result argues for application-specific criteria rather than retaining this window by default.
- Against reference row `pic16`, 175/222 (78.83%) are at least as favorable in both minimum positive S1–Ti gap and SOCME/ΔE; among no-imaginary rows, 156/191 (81.68%). Adding a requirement on both SOCME and SOCME/ΔE yields 155/222 (69.82%), or 138/191 (72.25%) after the no-imaginary filter.
- The reference `pic16` row itself has `Imaginary=Yes`; it is an electronic-property comparator, not a validated minimum. Comparisons must remain conditional on protocol compatibility.

### Generated candidate sets (`molecule_figures/02_data`)

Round 1 and Round 2 each contain 60 rows, 60 unique IDs and 60 unique SMILES. They have no shared SMILES, so the comparison is between disjoint generated sets, not paired samples. Each CSV includes SDPD-like component columns (`st_gap`, charge and symmetry scores, raw gap, ring penalty and total score) as well as electronic properties and chemistry descriptors. It is not evidence of predictor accuracy: there is no independent predicted-vs-reference validation table, model split, checkpoint identity, or prediction error analysis.

| Candidate-set descriptor | Round 1 median | Round 2 median | Round 1 mean | Round 2 mean |
|---|---:|---:|---:|---:|
| S1 energy (eV) | 1.9631 | 2.1222 | 2.0011 | 2.0628 |
| T1 energy (eV) | 1.2886 | 1.4706 | 1.3320 | 1.3815 |
| S1−T1 (eV) | 0.6647 | 0.6546 | 0.6690 | 0.6813 |
| Minimum positive S1−Ti gap (eV) | 0.1034 | 0.1013 | 0.1026 | 0.1086 |
| Maximum SOCME (cm⁻¹) | 1.7640 | 1.2626 | 1.6404 | 1.3187 |
| Maximum SOCME/ΔE (cm⁻¹/eV) | 4.7267 | 2.5145 | 9.2357 | 5.1501 |
| S1 wavelength (nm) | 631.6 | 584.25 | 623.82 | 603.93 |
| Molecular weight | 1039.37 | 905.19 | 1049.67 | 920.68 |
| LogP | 15.027 | 12.522 | 15.022 | 13.046 |
| TPSA (Å²) | 100.76 | 72.88 | 114.43 | 83.23 |
| SA score | 6.463 | 6.071 | 6.482 | 6.065 |

`Imaginary=Yes`: 8/60 (13.3%) in Round 1 and 9/60 (15.0%) in Round 2. The Round 2 set has lower median MW, LogP, TPSA, SA score, SOCME and SOCME/ΔE; the median minimum positive S1−Ti gap is marginally lower (0.1013 vs 0.1034 eV), while median S1−T1 is also marginally lower (0.6546 vs 0.6647 eV). These are descriptive differences across non-overlapping sets. No significance test or causal attribution is claimed; generator parameters, selection rules and per-round run manifests are unavailable here, and a better direction is application-dependent.

## 4. Inferred expert concerns

These concerns are Skill-inferred from registered outputs, not real expert feedback: (i) computer/cluster expert—actual target-cluster readiness, missing raw-log termination provenance, memory/concurrency and isolated protocol-specific outputs; (ii) computational chemist—method sensitivity, excited-state coverage, convergence and imaginary modes; (iii) materials expert—very high lipophilicity and lack of validated application-specific property windows; (iv) model/optimization expert—component/reward alignment and absent independent predictive validation; (v) project owner—reference comparability, immutable runs and attributable per-round parameter changes.

## 5. Recommended next optimization step

### Priority 1 — Establish a reproducible, quality-filtered Round 3 baseline

Do not immediately tune the reward or quantum method based on the two small candidate sets. First identify the exact generator/checkpoint/config and selection rule used for both 60-molecule cohorts; register each run manifest, candidate lineage and selection/duplicate rules; verify ORCA convergence and normal termination from raw logs; and join every molecule to its immutable protocol/version. Recompute comparison tables with a strict primary set of valid minima (`Imaginary=No` plus normal termination and valid required fields) and a separately labeled inclusive sensitivity set. The reference `pic16` must be marked as an imaginary-frequency structure in all views.

### Priority 2 — Replace the failed default property window with an expert-approved application target

The configured LogP 1–5/TPSA 20–120 window selects no core molecules, while median LogP is 14.08 in the core and 12.52 in generated Round 2; these are strong warning signals for an overly lipophilic chemical space, not proof of poor biological performance. Materials/formulation experts should set a justified compartment-specific range and decide whether aqueous solubility, aggregation, charge/protonation, molecular size and synthetic accessibility are hard constraints, soft penalties or measured outcomes. Test the revised window against the existing 222 structures before using it in reward optimization.

### Priority 3 — Make objective trade-offs robust and inspect outliers

Use a validation-set-calibrated, multiobjective selection procedure rather than relying on a single weighted score or maximizing a ratio with a long-tailed distribution. Report raw gap, SOCME and SOCME/ΔE components, include robust quantiles/transformations and inspect the high-ratio tail (max 110.16 vs median 3.46). Compare 2D/3D Pareto fronts with no-imaginary and protocol-compatible subsets; retain diversity by scaffold and decoration. Have domain experts approve objective directions and thresholds before turning the Pareto view into an optimization target.

### Priority 4 — Conduct a small, controlled protocol-sensitivity and predictor-validation study

Choose a stratified subset across scaffold, charge state, key metric quantiles and outliers. Compare current standard protocol with an approved alternative one protocol dimension at a time, preserving matched geometries/conditions and recording root/state correspondence, convergence and frequency checks. If the optimization model makes property predictions, evaluate on a scaffold-separated holdout against ORCA values, reporting MAE, RMSE, bias, rank correlation and scaffold-bootstrap confidence intervals. Do not infer surrogate accuracy from the candidate CSV columns alone.

### Priority 5 — Fix cluster provenance and memory controls before scaling

The target profile's 64 × 3 GB and 32 × 3 GB maxcore requests correspond to 187.5 and 93.75 GiB per node, while the recorded environment is not that cluster and its runtime has no ORCA/Slurm. Run site preflight on the actual AMD cluster; measure peak RSS and wall time for representative molecule sizes; then adjust ranks, maxcore and max concurrent jobs from measured scaling and site limits. Capture scheduler job IDs, exit codes, normal-termination markers, memory, wall time, scratch usage and failed-ID retry history in a per-run manifest.

## 6. Round 2 conclusions and limits

The workflow has strong machine-readable stage, profile, parameter, path and quality interfaces, and its 222-row v22 summary is complete with unique IDs/SMILES. The material caveats are missing raw log evidence, no run manifests, non-validated imaginary-frequency reference, zero matches to an unapproved default property window, heavy-tailed SOCME/ΔE, and no independent model validation. Round 1→2 candidate summaries are descriptive only because cohorts are unpaired and run configurations are not recorded. Expert adjustment requests were not found. All recommendations are Skill-generated and provisional; no settings or checkpoints were changed.

## Dialogue-based status reconciliation (2026-10-31)

The current output states have been reconciled with the saved expert dialogue at the user's request. General knowledge acceptance, task inputs, selected metric roles, and the synthesizability requirement are recorded only within their supported scope. Existing disputes, unanswered review questions, missing protocols, numerical thresholds, route validation, model-validation gaps, and execution-authorization requirements remain explicit. No scientific values or execution permissions are newly certified, and the historical execution trace is unchanged. The scope and dialogue excerpts are recorded in the expert_feedback_reconciliation metadata of `performance_evaluation_round2.yaml`.
