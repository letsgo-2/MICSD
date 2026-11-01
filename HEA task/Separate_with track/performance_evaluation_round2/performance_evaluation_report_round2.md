# Performance Evaluation Report: HEA Optimization Round 2

## Scope and evidence status

This round addresses the materials expert's requests for eight-metal composition distributions, peak power density, normalized cost, and high-performance formulation characteristics, together with the computer expert's requests for iterative-process and predictive-model diagnostics. The analysis uses the round1 evaluation policy and `AL/catalyst_active_learning_runnable/outputs/total_pool.csv`.

The evaluation state remains **partially executed**. The AL README identifies the power-density values as Gradient Boosting virtual-experiment labels, not physical measurements. The normalized cost is a relative implementation index rather than a validated currency value. Therefore all performance and ranking statements below are explicitly virtual/model-derived.

## Main findings

- The pool contains 160 unique records and passes strict compositional closure at a `1e-9` tolerance; the maximum observed closure error is approximately `4.44e-16`.
- The virtual power-density distribution has mean `54.800`, median `60.070`, and maximum `68.581` in the source unit, which is not supplied as a validated device unit.
- The top-decile virtual threshold is `65.477` with 16 formulations. In this subset, mean Pd fraction is `0.404` versus `0.362` in the full pool, mean Ce fraction is `0.125` versus `0.109`, and mean Au fraction is `0.023` versus `0.063`. These are descriptive compositional shifts, not causal elemental effects; closure-induced dependence must be respected.
- Power-cost association is weak: Pearson `r = 0.052` and Spearman `rho = -0.158`. The results do not support treating normalized cost as a reliable performance surrogate or collapsing power and cost into one unvalidated score.
- The first 10 seed/baseline rows have mean virtual power density `5.669`, while the remaining 150 generated/retained rows have mean `58.075`. This is a pool-phase contrast, not a formally reconstructed learning curve, because `iteration_log.csv`, `query_log.csv`, and `generated_ratios.csv` are absent.
- The configured Gradient Boosting virtual oracle gives five-fold cross-validated `R² = 0.870`, `RMSE = 8.564`, `MAE = 6.691`, Pearson `r = 0.935`, and Spearman `rho = 0.828` on the 120-row supplied training sample. These are internal interpolation diagnostics, not external experimental predictive accuracy or calibrated uncertainty.

## Recommended next optimization step

Use a measurement-gated, uncertainty-aware local active-learning batch. Preserve the named-element order adapter, validate approved composition bounds and basis, and select a balanced batch from three strata: high virtual power, favorable power-cost trade-off, and high uncertainty/compositional diversity. Measure each candidate with replicates under a fixed device protocol, recording units, conditions, sample identifiers, and uncertainty. Retrain only after merging measured results with provenance and compare measured versus predicted performance, calibration, rank stability, cost, and composition support.

For computer-side controls, restore per-run `iteration_log.csv`, `query_log.csv`, and `generated_ratios.csv`; add repeated or nested cross-validation, composition-aware splits, baseline models, residual diagnostics, and prediction intervals. Use an external or newly measured holdout before using the model to make a candidate claim.

## Output paths

All outputs are under `performance_evaluation_round2/`.

### Charts

- `figures_round2/composition_high_performance_round2.png`
- `figures_round2/power_density_cost_round2.png`
- `figures_round2/pool_sequence_process_round2.png`
- `figures_round2/oracle_cv_parity_round2.png`
- `figures_round2/high_performance_composition_shift_round2.png`

### Statistical files

- `statistical_metrics_round2.json`
- `predictive_model_accuracy_round2.json`
- `composition_high_performance_stats_round2.csv`
- `process_phase_summary_round2.csv`
- `oracle_cv_predictions_round2.csv`

### Analysis tables and documentation

- `pool_annotated_round2.csv`
- `high_performance_formulations_round2.csv`
- `top5_virtual_formulations_round2.csv`
- `recommendations_round2.md`
- `performance_evaluation_round2.yaml`
- `execution_trace_round2.jsonl`
