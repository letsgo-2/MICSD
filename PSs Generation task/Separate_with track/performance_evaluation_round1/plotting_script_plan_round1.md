# Plotting Script Plan — Round 1

## Planned implementation

Create `plot_performance_round1.py` after row-level data contracts and actual data are available. It must read candidate and model-validation tables, validate required columns and units, reject duplicate candidate IDs unless explicitly versioned, and report missingness/exclusions. It must never synthesize observations or generate empty-looking figures as evidence. Record Python and package versions, input hashes, command line, timestamp, and output hashes in a run manifest.

## Inputs

- `performance_records_round1.csv`: one row per candidate, with candidate ID, canonical/isomeric SMILES, scaffold, decoration, formal charge/state, descriptors, generation provenance, predictor S1/T1/ST-gap, scorer components, ORCA S1/T1/ST-gap, convergence/failure fields, Slurm job/time/resource fields.
- `model_validation_round1.csv`: frozen split label, scaffold group, target, predicted value, reference value, units, checkpoint hash, method/condition ID.
- Optional `run_events_round1.csv`: generation, invalidity and job completion events with denominators.

## Figures and tables

| Output filename | Content and checks |
|---|---|
| `fig01_metric_distributions_round1.png` | Faceted distributions for predicted/reference S1, T1 and ST gap, with scaffold/charge grouping, sample count and missingness. |
| `fig02_predicted_vs_orca_stgap_round1.png` | Predicted vs computed gap; identity line; MAE/RMSE and scaffold-bootstrap 95% CI; separate split colors. |
| `fig03_residuals_round1.png` | Residual vs reference and residual density/QQ diagnostic; show bias, outlier table references, not just visually selected points. |
| `fig04_metric_tradeoffs_round1.png` | ST gap vs charge/symmetry; facet by scaffold; Pareto highlighting disabled until semantics/directions approved. |
| `fig05_generation_qc_round1.png` | Validity, uniqueness, scaffold coverage and ORCA completion proportions with explicit numerator/denominator and intervals. |
| `fig06_resource_performance_round1.png` | Walltime and peak memory vs atom count/conformer count, colored by exit status; omit if scheduler accounting unavailable. |
| `table01_candidate_metrics_round1.csv` | Auditable candidate-level joined table with provenance, descriptor, model, scorer, ORCA, QC and failures. |
| `table02_model_statistics_round1.csv` | n, MAE, RMSE, bias, Pearson/Spearman, scaffold-bootstrap CI by target and split. |
| `table03_run_summary_round1.csv` | Validity, uniqueness, coverage, ORCA completion and compute-resource summaries. |

## Statistical/visual conventions

Use consistent units (eV for excitation energies and gaps), label predictor vs ORCA explicitly, plot confidence intervals rather than standard-error bars where specified, show `n`, retain failed/excluded denominators, and use a colorblind-accessible palette. Keep exploratory and confirmatory cohorts visually distinct. Resample scaffold groups, not individual molecules, for uncertainty intervals. No inferential p-value or candidate rank is generated without an approved hypothesis/metric direction and sufficient observed data. Save high-resolution PNG plus editable SVG/PDF, all named with `round1`.

## Audience panels

- Computer expert: model calibration, residuals, checkpoint identity, validity, runtime and failures.
- Materials/computational photochemistry: condition-labeled energy gaps, uncertainty/sensitivity, charge states and descriptor trade-offs.
- Joint: coverage and Pareto/trade-off view only after charge and symmetry definitions are approved.
