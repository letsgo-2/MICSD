# Performance Evaluation Report Round 1

## 1. Evaluation Scope

This Round 1 performance-evaluation package evaluates the available outputs and data contracts for the octonary HEA catalyst active-learning workflow. The active upstream execution context is `execution_orchestration_round2/`, because it registers the implemented AL path and the locked element order used by the runnable package.

No AL model, oracle training, environment check, or new optimization run was executed during this evaluation update. The work here creates a reproducible evaluation workflow, records what can already be assessed from existing artifacts, and separates virtual, predicted, computed, and measured provenance.

## 2. Evaluated Artifacts

| Artifact | Role | Status |
|---|---|---|
| `AL/catalyst_active_learning_runnable/data/initial_examples.csv` | Initial active-learning examples | Available; 10 rows |
| `AL/catalyst_active_learning_runnable/data/oracle_training_sample.csv` | Virtual GBR oracle training sample | Available; 120 rows; not new real experiments |
| `AL/catalyst_active_learning_runnable/outputs/total_pool.csv` | Existing candidate/output pool | Available; legacy ratio-column format; 160 rows |
| `AL/catalyst_active_learning_runnable/outputs/total_examples_pool.csv` | Existing expanded example pool | Available; element-column format; 160 rows |
| `iteration_log.csv`, `query_log.csv`, `generated_ratios.csv`, `summary.json` | Current pipeline run logs | Expected by current code but not present in the inspected output directory |

## 3. Metric Definitions

| Metric ID | Metric | Direction | Value Type Boundary |
|---|---|---|---|
| PE-R1-M001 | Peak power density (`power_density`) | Maximize | Measured or virtual labels in CSVs; model predictions only when from query logs |
| PE-R1-M002 | Composition validity | Constraint | Computed from finite, nonnegative, length-8, sum-to-1 mass fractions |
| PE-R1-M003 | Normalized cost | Minimize / tradeoff | Computed implementation metric from metal prices and Pd-normalized cost formula |
| PE-R1-M004 | Performance-cost Pareto status | Select nondominated candidates | Derived implementation analysis |
| PE-R1-M005 | Novelty / compositional distance | Diagnose exploration | Derived using CLR/Aitchison-style distances when candidate and reference pools are available |
| PE-R1-M006 | Prediction credibility | Diagnose uncertainty | Available only when query logs contain `llm_mean`, `llm_std`, and `ucb_score` |

## 4. Current Data Findings

| Dataset | Rows | Power Density Min | Power Density Max | Power Density Mean | Composition Check |
|---|---:|---:|---:|---:|---|
| Initial examples | 10 | 0.5450 | 39.6100 | 20.9985 | Valid sums; no negatives |
| Oracle training sample | 120 | 0.0271 | 75.4500 | 45.3405 | Valid sums within numerical tolerance; no negatives |
| Existing `total_pool.csv` | 160 | 0.4594 | 68.5811 | 54.7998 | Valid parsed ratio vectors; no negatives |
| Existing `total_examples_pool.csv` | 160 | 1.0070 | 69.7294 | 57.7783 | Valid sums within numerical tolerance; no negatives |

The existing `outputs/total_pool.csv` is a legacy artifact with columns `id, ratio, power_density, normalized_cost`. The current implementation writes expanded element columns plus `iteration` and `source`; therefore the Round 1 evaluation script accepts both schemas.

## 5. Analysis Plan

The reproducible script `scripts/evaluate_al_performance_round1.py` is designed to:

- Load initial examples, virtual oracle training data, existing output pools, and optional current pipeline logs.
- Normalize legacy `ratio` vectors into the canonical element order `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr` without changing raw files.
- Compute data-integrity checks: required columns, numeric validity, vector length, nonnegative values, and composition sum tolerance.
- Summarize `power_density`, `normalized_cost`, candidate counts, high-performance quantiles, and schema coverage.
- Compute Pareto-front membership for performance-cost tradeoffs when both metrics are available.
- Compute CLR-distance novelty statistics between output candidates and the initial examples when composition columns are available.
- Write derived tables to `performance_evaluation_round1/tables/` and figures to `performance_evaluation_round1/figures/`.

## 6. Expert Views

### Computer Expert View

The implemented AL package has enough artifact structure for reproducible offline evaluation without executing the optimizer. The main technical caveat is schema drift between the existing legacy `outputs/total_pool.csv` and the current code path in `catalyst_al/pipeline.py`.

### Catalyst / Electrochemistry View

Peak power density can be ranked and summarized, but physical unit and experimental conditions remain unresolved. Virtual oracle labels must not be interpreted as newly measured catalyst performance.

### Optimization View

The available pools can support Pareto and cost-performance diagnostics. Full prediction credibility analysis requires current `query_log.csv` fields from a confirmed run.

### Cross-Domain View

The next decision should be whether to execute a confirmed AL run, ingest real measured validation results, or use this Round 1 script only as a pre-run audit layer.

## 7. Review Items

- Confirm the physical unit and measurement conditions for `power_density`.
- Confirm whether legacy `outputs/total_pool.csv` should be treated as a prior run result or historical example artifact.
- Confirm whether `oracle_training_sample.csv` should remain limited to virtual oracle training and excluded from candidate performance claims.
- Confirm whether to run the AL pipeline to produce current `iteration_log.csv`, `query_log.csv`, `generated_ratios.csv`, and `summary.json` before deeper model-credibility evaluation.
