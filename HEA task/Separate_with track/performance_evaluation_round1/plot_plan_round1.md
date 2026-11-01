# Performance Evaluation Plotting Plan (Round 1)

## Scope and evidence labels

The input artifacts are evaluated as AL-derived or provenance-unresolved data. The round2 orchestration record states that no authorized API, model, training, inference, or candidate-generation run was performed. Figures must therefore use labels such as **virtual**, **derived**, or **source unit unavailable** and must not be presented as measured catalyst performance.

## Required figures

1. `power_vs_cost_virtual_round1.png`: scatter plot of `total_pool.csv` power-density labels versus the relative normalized-cost index; report Pearson and Spearman correlations, but do not interpret the cost index as USD/g.
2. `composition_distribution_round1.png`: per-element fraction distributions, preserving the AL source order and showing pool support and possible zero-inflation.
3. `spearman_associations_round1.png`: rank-association heatmap for eight fractions, virtual power density, and normalized cost. Use as diagnostic evidence only; compositional closure creates dependence between fractions.
4. Future approved-run figures: parity/calibration plots for measured versus predicted power density, replicate-aware confidence intervals, iteration learning curves, Pareto fronts, and candidate-versus-baseline comparisons under matched device conditions.

## Statistical protocol

- Validate required columns, numeric coercion, finite/nonnegative fractions, exact closure tolerance, duplicate rows, missing cells, and explicit element-order mapping.
- Report `n`, missing count, mean, sample standard deviation, median, quartiles, minimum, and maximum for each numeric target.
- Report Pearson and Spearman power-cost association, with sample size and provenance labels.
- For approved repeated measurements, add bootstrap confidence intervals, replicate-aware group summaries, calibration error, MAE, RMSE, R², and rank correlation. Do not compute inferential tests until independent replicates and a comparison design are supplied.
- Keep virtual-oracle labels, predictions, measured values, literature values, and implementation scores in separate columns and records.

## Blocking checks before candidate claims

Resolve EO2-001 through EO2-005: canonical order/basis, measurement provenance and units, cost provenance, composition bounds/closure policy, and model validation/uncertainty. A candidate can be ranked for software diagnostics only; it cannot be claimed to outperform a physical baseline from the current evidence.
