# Execution Orchestration Report Round 2

## 1. Update Scope

This Round 2 execution-orchestration update revises the Round 1 workflow using the new expert decisions and the implemented `AL/catalyst_active_learning_runnable/` path.

Confirmed by computer expert:

- Peak power density is the core performance metric for formulation optimization.
- The eight element mass fractions are nonnegative and sum to 1.
- A fixed element order is a composition constraint.

Confirmed by inspection of the implemented AL path:

```text
Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr
```

This is the order used in `README.md`, `costs.py`, `data.py`, `providers.py`, and output construction. The user-listed order contains the same element set but is not the implemented run schema.

No model, test, environment check, training script, or AL run was executed in this update. The run procedure below is for confirmation only.

## 2. Input And Evidence Status

| Evidence ID | Source | What It Supports |
|---|---|---|
| EO2-E001 | `knowledge_alignment_round2/knowledge_alignment_round2.yaml` | Upstream metric roles, data contract, peak-power-density objective, cost and composition constraints. |
| EO2-E002 | `execution_orchestration_round1/` | Previous orchestration baseline, metric decisions, proposed workflow. |
| EO2-E003 | `AL/catalyst_active_learning_runnable/README.md` lines 5-15, 44-63, 83-105, 113-186, 198-208 | Implemented workflow, dependencies, API requirements, run commands, default outputs, and boundary that GBR labels are virtual rather than real experiments. |
| EO2-E004 | `AL/catalyst_active_learning_runnable/config.json` | Run parameters and metric/selection settings. |
| EO2-E005 | `catalyst_al/costs.py`, `data.py` | Element order, nonnegative finite normalization, sum-to-1 rule, normalized cost formula, CSV input schema. |
| EO2-E006 | `catalyst_al/model.py`, `train_oracle.py` | GBR virtual-oracle model structure and training method. |
| EO2-E007 | `catalyst_al/providers.py` | OpenAI-compatible LLM provider, composition-generation prompt, committee prediction, output parsing and allowed prediction range. |
| EO2-E008 | `catalyst_al/sampling.py`, `pareto.py`, `pipeline.py` | CLR/Aitchison distance, AK-DAS candidate diversity, UCB score, Pareto/weighted selection, iteration loop, output files. |
| EO2-E009 | `tests/test_core.py` | Non-network software smoke test uses a fake provider, and confirms expected `summary.json` / `total_pool.csv` outputs. |
| EO2-E010 | Local literature: Lookman 2019, Egozcue 2018, Xu 2024, Zhang 2025 | Active learning, uncertainty, compositional distance, multiobjective cost/performance workflow support. |

Background explore/librarian agents were launched as requested, but the fallback sessions again returned no usable synthesis. Direct local reads, grep, AST-grep, and local literature searches supplied the evidence above.

## 3. AL Implementation Audit

### 3.1 Implemented Path

```text
/Users/jimmmmmies/Desktop/催化剂案例/AL/catalyst_active_learning_runnable
```

### 3.2 Entry Points

| File | Purpose | Execution Status In This Update |
|---|---|---|
| `run.py` | Main AL run entrypoint. Accepts `--config`, `--iterations`, `--candidate-pool-size`, `--output-dir`. | Not run |
| `train_oracle.py` | Standalone GBR virtual-oracle training entrypoint. | Not run |
| `check_environment.py` | Dependency, file, and API environment checker. | Not run |
| `tests/test_core.py` | Unit/smoke tests with fake LLM provider to avoid network calls. | Not run |

### 3.3 Dependencies And Environment

`requirements.txt` specifies:

```text
numpy==1.26.4
pandas==2.2.3
scikit-learn==1.6.1
joblib==1.4.2
openai>=1.58.0,<3.0.0
python-dotenv>=1.0.1,<2.0.0
```

README recommends Python 3.10-3.12, preferably Python 3.11.

The real AL run requires `.env` variables:

```text
OPENAI_API_KEY
OPENAI_MODEL
OPENAI_BASE_URL optional
```

### 3.4 Data Interfaces

Required input columns for the initial and oracle-training CSV files:

```text
Pd,Pt,Cu,Au,Ir,Ce,Nb,Cr,power_density
```

Data reader behavior:

- Requires all eight metal columns and `power_density`.
- Drops rows with missing required values.
- Normalizes metal ratios to sum to 1.
- Converts `power_density` to numeric.

Current data files:

| File | Role |
|---|---|
| `data/initial_examples.csv` | 10 initial active-learning samples. |
| `data/oracle_training_sample.csv` | 120-row reduced training data for GBR virtual oracle. |
| `data/Data.xlsx` | Source workbook present in AL folder. |

Important boundary from `data/README.md`: the 120-row file is used to train the GBR virtual oracle and is not new real experimental data.

### 3.5 Model Structure And Training Method

Implemented virtual oracle:

```text
GradientBoostingRegressor
n_estimators = 512
learning_rate = 0.03
max_depth = 3
loss = squared_error
random_state = config.random_seed
```

Training method:

1. Load `oracle_training_sample.csv`.
2. Split train/test with `test_size = 0.2` and `random_state` from config.
3. Train an evaluation GBR model and report `test_r2`, `test_rmse`, `test_mae`.
4. Train a final GBR on all rows.
5. Save model to `artifacts/oracle_gbr.joblib`.

The main `run.py` calls `load_or_train_oracle`: if `artifacts/oracle_gbr.joblib` does not exist, it trains automatically before AL iteration.

### 3.6 Candidate Generation And Screening

Implemented loop:

1. Sort reference examples by Pareto behavior over high `power_density` and low `normalized_cost`.
2. Calculate target `power_density` and target cost from current leader:
   - target PD uses normally sampled improvement around 6% mean, 2% std, capped at 400.
   - target cost uses normally sampled reduction around 3% mean, 1% std, floored at 0.1.
3. Use OpenAI-compatible LLM to generate one target eight-metal ratio.
4. Generate a Dirichlet candidate pool over the eight-element simplex.
5. Use AK-DAS in CLR/Aitchison space to select candidates balancing relevance to the LLM target and batch diversity.
6. For each selected AK-DAS candidate, find similar historical examples by CLR/Aitchison distance.
7. Ask the LLM committee for repeated power-density predictions.
8. Compute:
   - `llm_mean`
   - `llm_std`
   - `ucb_score = llm_mean + ucb_exploration_weight * llm_std`
   - `normalized_cost`
9. Select candidates using Pareto front over high UCB and low cost, then a weighted score.
10. Evaluate selected candidates with GBR virtual oracle.
11. Retain top candidates by batch-local weighted score:

```text
final_score = performance_weight * normalized_power - (1 - performance_weight) * normalized_cost
```

### 3.7 Default Run Parameters

From `config.json`:

| Parameter | Value | Meaning |
|---|---:|---|
| `num_iterations` | 10 | maximum iteration count |
| `candidate_pool_size` | 20000 | Dirichlet candidate pool size per round |
| `kdas_select_size` | 10 | AK-DAS candidates sent to LLM committee |
| `query_top_k` | 8 | candidates evaluated by GBR virtual oracle |
| `retain_top_k` | 3 | candidates retained into online sample pool |
| `committee_size` | 3 | LLM repeated predictions per candidate |
| `similar_examples_k` | 3 | similar examples shown in LLM prediction prompt |
| `lambda_start` / `lambda_end` | 0.5 / 0.7 | AK-DAS relevance weight schedule |
| `kdas_sigma` | 1.5 | CLR-space Gaussian kernel width |
| `ucb_exploration_weight` | 1.0 | UCB uncertainty weight |
| `performance_weight` | 0.6 | final weighted power-vs-cost score |
| `performance_threshold` | 200.0 | stop if global best reaches threshold |
| `target_pd_improvement_mean/std` | 0.06 / 0.02 | target PD improvement sampling |
| `target_cost_reduction_mean/std` | 0.03 / 0.01 | target cost reduction sampling |

### 3.8 Output Result Paths And Formats

Default output directory from `config.json`:

```text
AL/catalyst_active_learning_runnable/outputs/llm_experiment/
```

Can be overridden by CLI `--output-dir`.

Implemented output files:

| Output File | Main Fields / Meaning |
|---|---|
| `total_pool.csv` | `id`, `iteration`, `source`, `Pd`, `Pt`, `Cu`, `Au`, `Ir`, `Ce`, `Nb`, `Cr`, `power_density`, `normalized_cost` in current code path. Earlier existing output examples may use a `ratio` column. |
| `iteration_log.csv` | `iteration`, `lambda`, `target_pd`, `target_cost`, `generated_cost`, `queried_count`, `retained_count`, `best_new_pd`, `best_new_cost`, `global_best_pd`. |
| `query_log.csv` | `iteration`, `query_rank`, `retained`, eight element fractions, `llm_mean`, `llm_std`, `ucb_score`, `power_density`, `normalized_cost`, `final_score`. |
| `generated_ratios.csv` | `iteration`, eight element fractions, `normalized_cost` for LLM-generated target ratio. |
| `summary.json` | `provider`, `iterations_completed`, `initial_samples`, `retained_samples`, `oracle_queries`, `best_power_density`, `output_dir`. |

Recommended first confirmation output path:

```text
AL/catalyst_active_learning_runnable/outputs/api_check/
```

Recommended full-run output path after confirmation:

```text
AL/catalyst_active_learning_runnable/outputs/full_run/
```

## 4. Updated Metric Organization

| Rank | Metric | Role | Direction | Implemented Evaluator / Source | Threshold / Guidance | Status |
|---:|---|---|---|---|---|---|
| 1 | Composition validity | hard_constraint | must pass | `normalize_ratio`, data reader, provider parser | finite, length 8, nonnegative, sum > 0 then normalized to sum 1 | active for AL path |
| 2 | Fixed element order | hard_constraint | must match | README, `METAL_ORDER`, provider prompt, output construction | `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr` | confirmed for AL path |
| 3 | Peak power density | primary_objective | maximize | CSV target, LLM prediction, GBR virtual oracle, summary best | LLM predictions must be 0-500; local training target range 0.02709-75.45; stop threshold 200 in config | core metric |
| 4 | Element content ranges | hard/soft_constraint | target range | config-independent; current code only checks nonnegative and vector length | current AL allows any simplex point; synthesis-specific bounds remain absent | pending expert bounds |
| 5 | Normalized cost | secondary metric / soft_constraint | minimize | `calculate_normalized_cost` | local cost index relative to Pd; source/date of prices still uncertified | implemented, provisional |
| 6 | Candidate difference from existing samples | diagnostic / diversity metric | maximize minimum novelty or balance with relevance | `find_similar_examples`, AK-DAS CLR distance/diversity penalty | use CLR/Aitchison distance; no absolute threshold implemented | implemented as selection behavior |
| 7 | Model prediction credibility | diagnostic / acquisition metric | maximize confidence or manage uncertainty | LLM committee `llm_std`; UCB score | `ucb_score = llm_mean + 1.0 * llm_std`; high std means exploration and lower credibility simultaneously | implemented |
| 8 | High-performance formulation stability | diagnostic | maximize recurrence / robustness | `iteration_log`, retained samples, global best, repeated nearby candidates | no formal stability threshold; track repeated high PD under nearby ratios and stable global best | proposed extension |
| 9 | Final weighted score | batch selection score | maximize | `_score_and_retain` | `0.6 * normalized_power - 0.4 * normalized_cost` with batch-local min-max scaling | implemented but not scientific endpoint |

## 5. Reward And Constraint Update

Round 2 final organization:

```text
Primary objective: maximize peak power density.
Hard constraints: fixed element order, finite nonnegative eight-element vector, normalized sum = 1.
Secondary/cost metric: minimize normalized cost or use cost in Pareto/weighted screening.
Diagnostic metrics: candidate novelty/difference, model prediction credibility, high-performance stability.
```

The implemented AL code already uses a mixed strategy:

- Hard composition validation through `normalize_ratio`.
- Cost-aware target setting and Pareto candidate screening.
- UCB for LLM prediction mean plus uncertainty.
- CLR/Aitchison-space similarity/diversity through `AKDAS`.
- Batch-local final score balancing virtual-oracle performance and normalized cost.

Important interpretation rule:

```text
GBR-predicted power_density is a virtual-oracle value, not a new material experiment.
LLM mean/std/UCB are model outputs, not experimental measurements.
```

## 6. Updated Workflow

### 6.1 Pre-Run Confirmation Workflow

These are the steps to confirm before any execution:

1. Confirm the AL order `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr` as the only run schema.
2. Confirm that `power_density` in current CSV files is acceptable as the core performance target for the simulated AL loop.
3. Confirm that normalized cost can use the local price table provisionally.
4. Confirm whether `performance_weight = 0.6`, `performance_threshold = 200`, and the 6% target-PD improvement setting are acceptable for this round.
5. Confirm `.env` API variables and expected provider/model name.
6. Confirm whether to run only the one-iteration API check first.
7. Confirm output directory for the check run and any later full run.

### 6.2 Run Procedure For User Confirmation Only

I did not run these commands. They are the documented procedure to run after your confirmation.

Working directory:

```bash
cd /Users/jimmmmmies/Desktop/催化剂案例/AL/catalyst_active_learning_runnable
```

Install dependencies in a suitable Python 3.10-3.12 environment:

```bash
python -m pip install -r requirements.txt
```

Prepare `.env` from `.env.example`:

```bash
OPENAI_API_KEY=...
OPENAI_MODEL=...
OPENAI_BASE_URL=...   # optional for compatible API
```

Optional non-API environment check:

```bash
python check_environment.py
```

Recommended first API check run:

```bash
python run.py --iterations 1 --candidate-pool-size 2000 --output-dir outputs/api_check
```

Expected first-check output directory:

```text
/Users/jimmmmmies/Desktop/催化剂案例/AL/catalyst_active_learning_runnable/outputs/api_check/
```

Expected files:

```text
total_pool.csv
iteration_log.csv
query_log.csv
generated_ratios.csv
summary.json
```

Default/full run only after the check is accepted:

```bash
python run.py --output-dir outputs/full_run
```

Expected full-run output directory:

```text
/Users/jimmmmmies/Desktop/催化剂案例/AL/catalyst_active_learning_runnable/outputs/full_run/
```

## 7. Domain Expert View

The updated metric organization satisfies the materials-science request by keeping the core property objective while exposing supporting evidence for economic, validity, novelty, credibility, and stability considerations.

Domain-facing interpretation:

- Peak power density is the optimization endpoint.
- Normalized cost is a formulation-design tradeoff metric, not a replacement for peak power density.
- Element content ranges are composition/synthesis constraints; only nonnegative simplex validity is implemented, so any real synthesis min/max bounds must still be supplied.
- Candidate difference from existing samples is scientifically useful because it avoids repeatedly testing near-duplicate recipes and supports exploration of HEA composition space.
- Prediction credibility separates model-guided exploration from trusted measured performance.
- High-performance formulation stability should be reviewed by checking whether high `power_density` persists across nearby compositions or across iterations, not from a single predicted candidate.

## 8. Computer Expert View

Computer-facing implementation facts:

- Entry command: `python run.py` with optional `--config`, `--iterations`, `--candidate-pool-size`, `--output-dir`.
- Config file: `config.json`.
- Data input schema: `Pd,Pt,Cu,Au,Ir,Ce,Nb,Cr,power_density`.
- Core predictor inside the virtual oracle: `GradientBoostingRegressor` with fixed hyperparameters in `model.py`.
- Candidate generator: LLM target ratio plus Dirichlet candidate pool.
- Diversity/novelty module: CLR transform, Aitchison-like distance, AK-DAS.
- Prediction credibility: LLM committee standard deviation and UCB score.
- Candidate screening: Pareto over high UCB / low cost plus weighted score.
- Final virtual evaluation: GBR oracle prediction.
- Output contract: `total_pool.csv`, `iteration_log.csv`, `query_log.csv`, `generated_ratios.csv`, `summary.json`.

Execution is not authorized yet in this report. The package is now documented as `available_pending_user_confirmation`, not `active`.

## 9. Remaining Review Items

The following should be confirmed before running:

1. Approve the AL element order `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr` as the fixed run schema.
2. Confirm whether the local `power_density` values are acceptable for the first simulated run.
3. Confirm whether local normalized cost values can be used provisionally.
4. Confirm one-iteration API check output path: `outputs/api_check`.
5. Confirm API configuration and expected cost/rate limit.
6. Confirm whether existing `outputs/` files may be overwritten or a new timestamped directory should be used.
7. Confirm whether high-performance stability should be added as a post-processing metric in a later code update or only tracked manually from logs for now.
