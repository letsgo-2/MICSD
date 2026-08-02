# Round 1 Performance Evaluation Scripts

`evaluate_al_performance_round1.py` is a reproducible offline evaluator for the catalyst AL artifacts. It reads local CSV/JSON files from `AL/catalyst_active_learning_runnable`, handles both legacy ratio-vector and current expanded-element schemas, and writes derived tables and figures under `performance_evaluation_round1/`.

The script does not run the AL optimizer, train the virtual oracle, call an LLM, or overwrite raw AL outputs.

Example syntax after dependencies are installed:

```bash
python3 performance_evaluation_round1/scripts/evaluate_al_performance_round1.py \
  --al-root AL/catalyst_active_learning_runnable \
  --output-dir performance_evaluation_round1
```

Expected derived outputs include:

- `tables/data_integrity_round1.csv`
- `tables/performance_summary_round1.csv`
- `tables/pareto_candidates_round1.csv`
- `tables/novelty_summary_round1.csv`
- `figures/power_density_vs_cost_round1.png`
- `figures/power_density_distribution_round1.png`
- `figures/novelty_distribution_round1.png`
