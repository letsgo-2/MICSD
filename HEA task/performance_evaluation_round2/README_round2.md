# Performance Evaluation Round 2

This directory contains English Round 2 performance-evaluation outputs for `AL/catalyst_active_learning_runnable/outputs/total_pool.csv`.

Primary outputs:

- `performance_evaluation_report_round2.md`
- `performance_evaluation_round2.yaml`
- `performance_review_queue_round2.yaml`
- `scripts/evaluate_total_pool_round2.py`
- derived tables under `tables/`
- derived figures under `figures/`

The analysis reads the existing `total_pool.csv` artifact only. It does not execute the AL model, train the virtual oracle, call an LLM, or modify raw outputs.
