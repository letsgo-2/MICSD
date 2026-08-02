# Performance Evaluation Report Round 2

## 1. Scope and Provenance

This Round 2 performance evaluation analyzes `AL/catalyst_active_learning_runnable/outputs/total_pool.csv` as one experimental iteration process, following the scientific-performance-evaluator requirement to preserve metric provenance and to keep predicted, computed, measured, and derived values separate.

No active-learning model, LLM provider, oracle training script, or new experimental execution was run. The analysis script only read the existing `total_pool.csv` artifact and wrote derived statistics and plots under `performance_evaluation_round2/`.

The source file has the legacy schema:

```text
id, ratio, power_density, normalized_cost
```

Because the file has no explicit `iteration` column, this report uses `id` / row order as the process sequence. For iteration-level summaries, the first 10 rows are treated as the initial set and the remaining 150 rows are divided into 10 inferred iteration stages based on `config.json`. This inference is used only for analysis and must not be mistaken for an explicit run log.

## 2. Output Inventory

### Tables

| Output | Path | Purpose |
|---|---|---|
| Expanded candidate pool | `performance_evaluation_round2/tables/total_pool_expanded_round2.csv` | Parses the eight-metal `ratio` vector into `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr`, adds inferred process fields and validity flags. |
| Composition distribution summary | `performance_evaluation_round2/tables/composition_distribution_summary_round2.csv` | Mean, standard deviation, min, median, max, and high-performance mean for each metal. |
| Performance and cost summary | `performance_evaluation_round2/tables/performance_cost_summary_round2.csv` | Descriptive statistics for peak power density and normalized cost. |
| Iteration process summary | `performance_evaluation_round2/tables/iteration_process_summary_round2.csv` | Inferred-stage mean/max power density, mean/min cost, high-performance counts, and Pareto counts. |
| Cumulative best process | `performance_evaluation_round2/tables/cumulative_best_process_round2.csv` | Candidate-by-candidate cumulative best peak power density. |
| High-performance formulations | `performance_evaluation_round2/tables/high_performance_formulations_round2.csv` | Top 10 percent formulations by peak power density. |
| High-performance composition features | `performance_evaluation_round2/tables/high_performance_composition_features_round2.csv` | Composition features enriched or depleted in high-performance formulations. |
| Pareto candidates | `performance_evaluation_round2/tables/pareto_front_candidates_round2.csv` | Nondominated candidates for maximizing power density and minimizing normalized cost. |
| Prediction accuracy status | `performance_evaluation_round2/tables/prediction_model_accuracy_status_round2.csv` | Documents that model accuracy is not computable from `total_pool.csv` alone. |
| Analysis manifest | `performance_evaluation_round2/tables/analysis_manifest_round2.json` | Machine-readable paths, summary values, and provenance flags. |

### Figures

| Figure | Path | Purpose |
|---|---|---|
| Eight-metal composition distribution | `performance_evaluation_round2/figures/eight_metal_composition_distribution_round2.png` | Boxplot of composition spread for all eight metals. |
| Composition trajectory | `performance_evaluation_round2/figures/composition_trajectory_round2.png` | Metal fractions across the ordered process sequence. |
| Power density vs normalized cost | `performance_evaluation_round2/figures/power_density_vs_normalized_cost_round2.png` | Cost-performance tradeoff colored by inferred iteration. |
| Cumulative best power density | `performance_evaluation_round2/figures/iteration_cumulative_best_power_density_round2.png` | Process-level model/optimization progress proxy. |
| High-performance composition features | `performance_evaluation_round2/figures/high_performance_composition_features_round2.png` | All-candidate means versus top-10-percent means. |

## 3. Key Statistical Results

The analyzed file contains 160 candidates, and all 160 parsed composition vectors are finite, nonnegative, eight-dimensional, and sum to 1 within numerical tolerance.

Peak power density statistics:

- Minimum: `0.4594`
- Median: `60.0696`
- Mean: `54.7998`
- 90th percentile high-performance threshold: `65.4775`
- Maximum: `68.5811`

Normalized cost statistics:

- Minimum: `0.0172`
- Median: `58.2193`
- Mean: `58.9802`
- 90th percentile: `70.8374`
- Maximum: `111.0067`

The best observed formulation is candidate `id=132`, in inferred iteration `9`, with peak power density `68.5811` and normalized cost `53.7637`:

| Metal | Fraction |
|---|---:|
| Pd | 0.3913 |
| Pt | 0.1579 |
| Cu | 0.1159 |
| Au | 0.0069 |
| Ir | 0.0186 |
| Ce | 0.1669 |
| Nb | 0.1060 |
| Cr | 0.0365 |

## 4. Materials-Expert View

The high-performance set is defined as the top 10 percent by peak power density, corresponding to 16 formulations with `power_density >= 65.4775`.

Compared with the full candidate pool, high-performance formulations show the clearest enrichment in:

- `Pd`: all-candidate mean `0.3619`, high-performance mean `0.4038`, enrichment `+0.0418`.
- `Ce`: all-candidate mean `0.1095`, high-performance mean `0.1251`, enrichment `+0.0156`.

High-performance formulations are depleted most clearly in:

- `Au`: all-candidate mean `0.0629`, high-performance mean `0.0231`, enrichment `-0.0398`.
- `Ir`: all-candidate mean `0.0381`, high-performance mean `0.0306`, enrichment `-0.0074`.

The most useful immediate materials-design region is therefore a Pd-rich, Ce-supported multicomponent region with moderate Pt/Cu/Nb and low Au/Ir. The current best candidate combines approximately `Pd 0.39`, `Pt 0.16`, `Cu 0.12`, `Ce 0.17`, and `Nb 0.11`, while keeping Au and Ir low.

## 5. Computer-Expert View

The process-level statistics show clear improvement after the initial stage. The initial rows have mean peak power density `5.6695` and maximum `49.53`; inferred iteration stages 3 through 10 maintain mean power densities around `56.9951` to `62.6246`.

The strongest stage-level signals are:

- Inferred iteration 8 has the highest mean power density: `62.6246`.
- Inferred iteration 9 contains the best candidate: `68.5811`.
- Inferred iteration 5 contains four high-performance candidates and three Pareto-front candidates, suggesting a useful exploration-exploitation balance in that segment.

Prediction-model accuracy cannot be computed from `total_pool.csv` alone. The file does not contain prediction means, prediction standard deviations, residuals, validation splits, ground-truth-after-prediction pairs, `query_log.csv`, or saved oracle evaluation metrics. The code path in `catalyst_al/model.py` can produce `test_r2`, `test_rmse`, and `test_mae` only when `train_oracle` is executed; this evaluation did not execute it.

## 6. Optimization Recommendations

1. Prioritize a local search around candidate `id=132`: keep Pd near `0.36-0.43`, Ce near `0.12-0.18`, Pt near `0.13-0.18`, Cu near `0.09-0.13`, and Nb near `0.08-0.14`, while holding Au and Ir low unless a targeted ablation requires them.
2. Use the Pareto front as the next candidate shortlist rather than ranking by peak power density alone. Candidate `id=132` is the best high-performance point, while candidates `98`, `74`, `73`, `127`, `138`, and `145` provide lower-cost tradeoff regions.
3. Run a controlled ablation on Au and Ir. Both are low in the high-performance mean and expensive in the cost metric; reducing them further may lower cost without sacrificing power density, but this must be checked experimentally or with a confirmed oracle run.
4. Preserve Ce in the next search. Ce is enriched in the high-performance group and appears in the current best candidate at `0.1669`, so it should not be prematurely pruned.
5. For the computer expert's accuracy concern, generate or recover the missing model-evaluation artifacts: `query_log.csv`, `iteration_log.csv`, `summary.json`, and oracle training metrics. Without these, accuracy claims must remain `not_available` rather than inferred from candidate outcomes.
6. In the next execution round, add explicit `iteration`, `source`, `llm_mean`, `llm_std`, `ucb_score`, oracle prediction, observed/validated power density, and residual columns to the persisted output so iteration dynamics and model accuracy can be evaluated directly.

## 7. Limitations and Review Needs

- The iteration grouping is inferred from row order and `config.json`; it is not an explicit field in `total_pool.csv`.
- `power_density` is treated as the peak power density metric, but physical units and experimental conditions remain unresolved.
- `normalized_cost` is a computed implementation metric and is not an experimental measurement.
- Prediction-model accuracy is not available from the current output file.
- Optimization recommendations are derived from this one artifact and should be reviewed before execution changes are made.
