# Performance Evaluation Report: Eight-Component HEA Catalyst (Round 1)

## Executive status

The evaluation is **partially executed**. Existing CSV artifacts from the AL folder were checked and summarized, but `execution_orchestration_round2` explicitly records that no authorized API call, model training, inference, candidate generation, or execution run was performed. The present results are therefore data-quality checks and diagnostics on source/derived artifacts, not evidence that any candidate has experimentally improved device peak power density.

## Inputs and provenance

- Upstream orchestration: `../execution_orchestration_round2/`
- AL implementation: `../AL/catalyst_active_learning_runnable/`
- Checked data: `initial_examples.csv`, `oracle_training_sample.csv`, `outputs/total_examples_pool.csv`, and `outputs/total_pool.csv`.
- Primary metric requested by orchestration: device peak power density.
- Cost is retained as the implementation's relative normalized index; it is not interpreted as USD/g.

## Data checks

All four inspected datasets contain the eight required named elements in the AL order `[Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr]`. Strict checks use finite, nonnegative fractions and a closure tolerance of `1e-9`; the generated `data_checks_round1.json` and checked CSVs contain row counts, missing cells, duplicate rows, closure errors, and target summaries. The checked artifacts had no missing composition cells, negative fractions, or duplicate rows, and all rows passed the strict closure test.

The project order is `[Pd, Pt, Au, Cr, Ir, Ce, Cu, Nb]`. The evaluator records this mismatch explicitly and maps by element name only. It does not perform positional pass-through or silent normalization. EO2-001 remains a blocking review item until this mapping and composition basis are independently approved.

## Statistical evaluation

`statistical_metrics_round1.json` reports sample size, missing count, mean, sample standard deviation, median, quartiles, minimum, and maximum for each target/cost field. It also reports Pearson and Spearman associations between virtual power-density labels and relative cost, plus the top-decile threshold and count for the AL pool. These statistics describe the supplied artifacts only; they do not establish calibrated uncertainty, causal effects, or experimental superiority.

The AL oracle labels and pool labels are kept separate from measured values. The source documentation describes the oracle as a GradientBoostingRegressor virtual experimenter, so all candidate rankings are labeled `virtual` and must not be used as measured performance claims.

## Plotting workflow

Run:

```bash
python3 evaluate_performance_round1.py
python3 plot_performance_round1.py
```

The plotting script creates `figures_round1/power_vs_cost_virtual_round1.png`, `composition_distribution_round1.png`, and `spearman_associations_round1.png`. The detailed future-run plan is in `plot_plan_round1.md`; it includes parity/calibration plots, replicate-aware intervals, iteration learning curves, Pareto fronts, and matched-condition baseline comparisons.

## Blocking gaps and next evaluation gate

EO2-001 through EO2-005 must be resolved before physical candidate claims: canonical element order and basis, P_peak unit/device protocol/conditions/replicates, dated cost provenance and price basis, approved composition bounds and closure policy, and model validation/uncertainty. The current output supports software-level inspection and reproducibility, but not a claim that the model has converged or that a candidate is experimentally better.
