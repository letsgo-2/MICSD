# Next Optimization Recommendations (Round 2)

## Evidence status

These recommendations are based on the round2 statistical tables and diagnostic figures generated from `AL/catalyst_active_learning_runnable/outputs/total_pool.csv` and the configured oracle-training sample. The AL README identifies the power-density labels as Gradient Boosting virtual-experiment outputs, not new physical measurements. The recommendations are therefore for the next controlled optimization/evaluation step, not procurement or experimental claims.

## Materials-expert view

1. Preserve the explicit named-element adapter from AL order `[Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr]` to project order `[Pd, Pt, Au, Cr, Ir, Ce, Cu, Nb]`; reject positional vectors and closure failures.
2. Use `composition_high_performance_stats_round2.csv` and `high_performance_formulations_round2.csv` to define a narrow, interpretable local design region around the top virtual formulations. Do not convert mean differences into elemental causal effects because the fractions are compositional and sum to one.
3. Select the next candidates using a diversity-constrained design: include high predicted power candidates, low-cost candidates, and compositionally distinct candidates. Avoid selecting only the high-power/high-cost cluster.
4. Confirm the basis of the eight fractions, allowable per-element bounds, zero/presence policy, and whether octonary support refers to nominal, bulk, or surface composition before the next run.
5. Measure replicate P_peak under a fixed device protocol and record units, operating conditions, batch/sample identifiers, and uncertainty. Replace virtual labels with measured values before asserting a high-performance formulation.

## Computer-expert view

1. Restore and preserve `iteration_log.csv`, `query_log.csv`, and `generated_ratios.csv` for every run. `total_pool.csv` alone cannot reconstruct exact iteration boundaries, query budgets, retention decisions, or learning curves.
2. Benchmark the Gradient Boosting oracle with repeated nested or repeated K-fold cross-validation, a composition-aware split, and a held-out external set. Report MAE, RMSE, R², Spearman rank correlation, residual bias, and prediction intervals.
3. Treat the current five-fold and random holdout metrics as internal virtual-oracle diagnostics only. They should not be presented as physical predictive accuracy or calibrated uncertainty.
4. Add model baselines such as constant mean, linear/ridge compositional regression, random forest/extra trees, and a simplex-aware model. Compare against the same folds and report uncertainty across folds.
5. Log random seeds separately for Dirichlet sampling, model fitting, and any LLM calls. The AL documentation notes that the local seed does not control LLM randomness.
6. Add an explicit stopping rule based on repeated external validation and plateauing measured improvement, not only the maximum virtual label.

## Recommended next optimization step

Run a **measurement-gated, uncertainty-aware local active-learning round**:

1. Validate the composition contract and experimental protocol.
2. Generate a balanced candidate batch from three strata: top virtual power, favorable power-cost trade-off, and high uncertainty/diversity.
3. Validate all candidates with strict closure and approved per-element bounds.
4. Measure each selected formulation with replicates under matched conditions.
5. Retrain only after merging measured results with provenance and preserving the previous model as a baseline.
6. Compare measured versus predicted performance, calibration, rank stability, cost, and composition support before the next acquisition step.

## Output paths

All round2 outputs are under `performance_evaluation_round2/`. Charts are under `performance_evaluation_round2/figures_round2/`; statistical files are `statistical_metrics_round2.json`, `predictive_model_accuracy_round2.json`, and `composition_high_performance_stats_round2.csv`; process and candidate tables are `process_phase_summary_round2.csv`, `pool_annotated_round2.csv`, `high_performance_formulations_round2.csv`, `top5_virtual_formulations_round2.csv`, and `oracle_cv_predictions_round2.csv`.
