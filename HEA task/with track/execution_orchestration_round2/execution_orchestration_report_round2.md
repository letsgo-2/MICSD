# Execution Orchestration: Eight-Metal Catalyst Formulation, Round 2

## 1. Purpose and Execution Authorization

This revision updates the prior execution-orchestration proposal using the Round 2 knowledge-alignment files, the new scientist/computer-expert instructions, and read-only inspection of `AL/catalyst_active_learning_runnable/`.

**This is a proposal for confirmation, not a run.** No Python script, model training, LLM/API call, candidate generation, model scoring, experiment, or modification of the AL package was performed. The AL package was inspected only. Model execution and experiment release remain unauthorized until the user confirms the proposed procedure and the blocking expert decisions are resolved.

The exact output paths are:

- [Execution report](</Users/jimmmmmies/Desktop/催化剂案例/execution_orchestration_round2/execution_orchestration_report_round2.md>)
- [Machine-readable configuration](</Users/jimmmmmies/Desktop/催化剂案例/execution_orchestration_round2/execution_orchestration_round2.yaml>)
- [Review queue](</Users/jimmmmmies/Desktop/催化剂案例/execution_orchestration_round2/execution_review_queue_round2.yaml>)
- [Auditable task event log](</Users/jimmmmmies/Desktop/催化剂案例/execution_orchestration_round2/execution_trace_round2.jsonl>)

## 2. Inputs and Actual AL Implementation

The three alignment inputs are [Round 2 YAML](../knowledge_alignment_round2/knowledge_alignment.yaml), [Round 2 report](../knowledge_alignment_round2/knowledge_alignment_report.md), and [Round 2 expert queue](../knowledge_alignment_round2/expert_review_queue.yaml). The materials scientist's latest instruction sets the new canonical representation to mass fractions in the order `[Pd, Pt, Au, Cr, Ir, Ce, Cu, Nb]`, nonnegative, sum one. This is an authoritative override for new orchestration records. Existing source data must retain their original columns/order/basis until each is verified and migrated.

### AL implementation map (read from source; nothing executed)

| Component | Actual implementation and interfaces | Orchestration interpretation / issue |
|---|---|---|
| Entry/config | `AL/catalyst_active_learning_runnable/run.py`; loads `config.json`, supports `--iterations`, `--candidate-pool-size`, `--output-dir`; `.env` loads OpenAI-compatible credentials. | Running invokes the full pipeline and may incur real API calls. Keep prohibited until confirmation. |
| Composition order/normalization | `catalyst_al/costs.py` sets `METAL_ORDER=(Pd,Pt,Cu,Au,Ir,Ce,Nb,Cr)`; `normalize_ratio` rejects negative/nonfinite/zero-total then normalizes any positive sum to 1. `providers.py` prompt also uses this old order. | Must explicitly adapt via a header-based permutation to `[Pd,Pt,Au,Cr,Ir,Ce,Cu,Nb]`. Do not silently reorder positional vectors or normalize experimental measured compositions without retaining raw value and closure error. |
| Training data loader | `catalyst_al/data.py` requires eight old-order symbols plus `power_density`, drops NA, calls `normalize_ratio`, and returns only composition and target arrays. It discards conditions, IDs and provenance. | Current model input has no conditions or uncertainty metadata. Proposed evaluation must use a richer adapter/table; do not treat current loader as production-ready for target-device endpoint. |
| Predictor/oracle | `catalyst_al/model.py`: scikit-learn `GradientBoostingRegressor`; 80/20 random row split; 512 estimators, learning rate 0.03, depth 3, squared-error loss; reports R²/RMSE/MAE; then fits on all rows and serializes with joblib. Loaded as a virtual oracle. | It predicts a single scalar `power_density`, not confidence intervals and not verified actual-device response. Random row split is vulnerable to near-composition/batch leakage. The 120-row target-sorted sample is not an unbiased holdout. This exact method is part of the AL implementation, but its validity for real target data is unverified. |
| LLM provider | `catalyst_al/providers.py`: `DesignProvider` interface `generate_ratio(target_pd,target_cost,references)` and `predict_committee(ratio,similar_examples,size)`; concrete OpenAI-compatible client reads `.env`, generates a vector, repeats prediction prompts; returned vector is normalized. | It is an actual network/API interface. It must not be invoked without explicit run authorization. LLM committee standard deviation is repeat-prompt dispersion, not calibrated predictive uncertainty. |
| Candidate generation | `catalyst_al/pipeline.py`: creates `candidate_pool_size` Dirichlet samples over an 8-simplex; current config 20,000. LLM generates a target ratio. | Candidate vectors are atomically sampled in the software sense but semantic unit is not encoded; treat the new mass-fraction vector as authoritative only after explicit order/unit adapter and AL prompt/config migration. Dirichlet alpha is implicitly all ones in code, not a confirmed scientific prior. |
| Diversity/nearest examples | `sampling.py`: CLR with epsilon 1e-6; AK-DAS weighted relevance/diversity using Gaussian kernel, lambda 0.5→0.7 and sigma 1.5; nearest examples use Euclidean distance in CLR coordinates. | Novelty metric is composition-space distance only. Zero replacement epsilon is implementation-specific and affects distances for boundary recipes. It is not a stability metric. |
| Cost/ranking | `costs.py` uses hard-coded prices with undocumented/legacy basis and reports cost relative to pure Pd ×100. `pareto.py` generates randomized improvement targets from config, Pareto selects on LLM UCB and cost, then applies batch min-max weighted score with performance weight 0.6. | Not actual precursor cost. The min-max normalization is candidate-batch-dependent, so scores can shift as the batch changes. The random target gains and 200 performance stop threshold are configured software defaults, not approved scientific thresholds. |
| Evaluation/feedback | Pipeline queries top candidates through `self.oracle.predict(...)`, which is GBR simulation, retains top 3, appends them with source `oracle_query`, and stops at config threshold. | This loop is a simulation closed loop, not a physical experiment feedback loop. GBR pseudo-labels must be tagged `predicted/simulated`, never appended as measured labels. |
| Outputs | Config default `outputs/llm_experiment`; `total_pool.csv`, `iteration_log.csv`, `query_log.csv`, `generated_ratios.csv`, `summary.json`. | No `llm_experiment` result directory was present during inspection; actual run artifacts are not assumed to exist. These are the AL program's designed output schemas. |

### Existing data inspected

- `data/Data.xlsx`, sheet `Result 1`: 703 records; 396 flagged abandoned and 307 unflagged. Of the abandoned rows, 357 are labeled `sample prep`; the remainder include cable connection, precursor issue, failed test, failure and retest reasons. The sheet has eight old-order fractions and `max_power`, but the extracted worksheet has no device condition metadata; target unit/protocol equivalence is unresolved. Raw composition sums range approximately 0.998–1.002, likely rounded, but assay precision is unknown.
- `data/oracle_training_sample.csv`: 120 examples selected from 307 eligible rows by target-sorting and even downsampling; historical target span about 0.02709–75.45 per local README. It is not a fair independent holdout and should not drive model acceptance alone.
- `data/initial_examples.csv`: ten seed examples, includes compositions with zero-valued components.
- `outputs/total_examples_pool.csv`: 160 records; old-order columns. Source rows and provenance require reconciliation before use. Existing `outputs/total_pool.csv` and `outputs/total_examples_pool.csv` predate this orchestration; this task created no files under AL outputs.
- `README.md` explicitly describes GBR “oracle” results as virtual, not new physical measurements; it says the current approach uses real LLM calls but virtual GBR labels. No output/run directory was present in the inspected package outputs.

## 3. Revised Metric Organization and Ranking

The computer expert now confirms `M_POWER` is the core performance metric. The eight mass-fraction validity rules are hard constraints. Other requested metrics are organized by role below; they are not collapsed into a single score by default.

| Priority | Metric | Proposed role | Definition/use | Status and threshold guidance |
|---:|---|---|---|---|
| 0 | `M_COMP_VALID` | Hard constraint | Ordered vector `[Pd,Pt,Au,Cr,Ir,Ce,Cu,Nb]`; finite numbers; each `w_i >= 0`; sum one. | Expert-approved. Use exact symbolic rules and tolerance from assay/reporting precision; retain raw vector and sum residual. No arbitrary epsilon. |
| 1 | `M_POWER` | Primary objective | Maximum device areal power from polarization curve, `max(V_cell*I/A_geo)` or `max(V_cell*j_geo)`. | Maximize. Device/reaction, units, area and protocol still need approval. No universal threshold. CRESt is a conditional reference only. |
| 2 | `M_COST_ACTUAL` | Secondary objective; possible hard budget if set | Actual precursor/material cost per declared basis from quotes, masses, yield and scale. | Minimize while meeting approved power requirement. No budget/quote supplied. |
| 3 | `M_NORMALIZED_COST` | Diagnostic/secondary until exact definition approved | Existing AL `normalized_cost` is hard-coded price-weighted composition cost relative to pure-Pd price, not actual purchase cost. Round 2 paper's cost-specific formulation is not operationally identical until verified. | Lower is preferable only for the declared proxy; do not use as a hard threshold or substitute for actual cost. |
| 4 | `M_STABILITY_FORMULATION` | Soft constraint / diagnostic | Robustness of high-performing formulations across independent preparations/devices: distribution of measured peak power and failure/validity rate under fixed recipe/protocol. | No evidence-backed cutoff currently. Must distinguish formulation reproducibility from electrochemical durability over time/cycling. Recommend replicate variance/interval and minimum replicate count be set by experiment team. |
| 5 | `M_MODEL_CONFIDENCE` | Screening gate / diagnostic | Predictor's validated uncertainty interval/calibration/applicability flag. Current AL has LLM repeated-prediction mean/std and GBR point predictions; neither is calibrated confidence as implemented. | Do not impose generic confidence percentage. Calibrate on held-out grouped data; high uncertainty or OOD -> hold/review/test, not discard automatically if exploration is desired. |
| 6 | `M_NOVELTY` | Batch diversity / diagnostic | Distance from candidate to measured samples in a declared representation. Current AL implementation: CLR with epsilon 1e-6 then Euclidean distance; AK-DAS relevance-diversity kernel. | No universal cutoff. Expose epsilon and representation; compute distance from measured, not virtual pool; combine with prediction, not replace performance. |
| 7 | `M_ELEMENT_BOUNDS` | Hard constraints only once supplied | Per-element lower/upper mass-fraction bounds and optional all-positive requirement. | Bounds and positivity not supplied; inactive. Do not import atomic-fraction/HEA criteria as mass-fraction constraints. |

**Ranking rationale:** composition validity is evaluated first because invalid proposals cannot enter; measured peak device power ranks highest as the stated outcome; actual cost is kept separate because it is a requested trade-off and the existing proxy is not actual cost; model confidence and novelty govern screening quality/diversity; stability of a recipe requires repeat experiments and is not inferred from one score. If cost cap and minimum power are later confirmed, treat them as explicit constraints; otherwise retain power/cost as separate Pareto objectives.

## 4. Model and Data Interface Update

### Existing AL model stack to expose, not silently replace

The current implementation provides these concrete components:

1. `GradientBoostingRegressor` virtual power surrogate trained from `oracle_training_sample.csv`; its training/evaluation split is random 80/20 by row; settings: 512 estimators, learning rate 0.03, max depth 3, squared-error loss, seed 42.
2. OpenAI-compatible API provider with `generate_ratio(...)` and `predict_committee(...)`; needs `OPENAI_API_KEY`, `OPENAI_MODEL`, optional `OPENAI_BASE_URL`; uses remote LLM, so explicit authorization and cost review are required.
3. Dirichlet(ones) candidate pool (default 20,000), CLR epsilon 1e-6, AK-DAS selection (default select 10, lambda 0.5→0.7, sigma 1.5), three LLM committee calls per selected candidate, GBR virtual evaluation for top 8, retain 3.
4. Cost table is hard-coded in `costs.py`, with no source/vintage documented in code. Do not activate it as actual cost. `performance_weight=0.6`, synthetic target improvement means/stds, and `performance_threshold=200` are software defaults, not validated expert-approved thresholds.

Because user says the AL path is now provided, these components are registered as `available_inspected` or `proposed_adapter_required` where appropriate, but **none is active for this project**. Do not change its source in this task. Required adaptation is: header-based mass-order migration; configurable cost metric and source; label provenance and conditions; confidence calibration; stability/replicate representation; candidate output schema; explicit gating before invoking API or model.

### Proposed canonical candidate input/output

Input candidate record must retain both `composition_mass_raw` with original columns/order/basis and `composition_mass_canonical` in `[Pd,Pt,Au,Cr,Ir,Ce,Cu,Nb]`, plus closure residual, source IDs and conversion provenance. Include intended synthesis/protocol ID. Never send ambiguous-basis source records into predictor.

Output candidate record must include:

- `candidate_id`, `round_id`, mass vector in canonical order, validity result and any per-element bound checks;
- `power_prediction_mean`, `power_prediction_interval`, predictor name/version and `confidence_status` (`uncalibrated`, `calibrated_in_domain`, `out_of_domain`, or `not_available`);
- `actual_cost` and `normalized_cost_proxy` as separate fields, each with currency/unit/source/date/status;
- `nearest_measured_sample_distance` and representation/config version;
- `formulation_stability_status` only after independent replicate measurements; otherwise null/not measured;
- Pareto rank or screen decision with reason codes; no scalar `final_score` unless a weight/scaling policy is approved;
- measured outputs appended separately from predicted/LLM/GBR outputs.

## 5. Revised Workflow and Gates

| Stage | Procedure using inspected AL path | Gate / output |
|---|---|---|
| A. Read-only configuration review | Record `config.json`, code/version, environment expectations, model artifact path and API requirements; do not invoke `run.py` or `check_environment.py` in this orchestration. | `AL_INTERFACE_SNAPSHOT`; no secrets/API values copied. |
| B. Data integrity and migration | Freeze raw workbook/CSVs; map columns by symbol headers; establish each dataset's fraction basis; convert to mass only when verified; reorder into expert order. Keep abandonment/failure tags and row provenance. | Quarantine any unknown-basis, unit-ambiguous, unlinked, duplicate, or invalid composition. Validate nonnegative and sum-to-one with agreed tolerance. |
| C. Label and condition reconciliation | Determine which `max_power`/`power_density` labels are physical device measurements, half-cell proxy, GBR virtual, or other. Link units, area basis, device/reaction and conditions. | Physical primary endpoint dataset only contains verified measured target-compatible labels. Simulated/virtual rows remain separate fidelity/source strata. |
| D. Baseline model training/validation | Existing GBR architecture is the first inspected predictor; do not assume it is suitable. Rebuild evaluation split by batch/device/date or other grouping to reduce leakage. Compare against simple baseline and preserve independent holdout. Record MAE/RMSE and residuals in endpoint units; assess calibration/interval coverage separately. | Human approves acceptance criteria; current 80/20 random row split and target-thinned sample are insufficient alone. |
| E. Metric calculator setup | Replace or wrap hard-coded cost with explicitly sourced `normalized_cost_proxy`; add actual quote cost input; add composition validity, novelty distance, confidence status and repeat stability fields. | No cost score or stability score when source data absent; output null/status rather than fake zero. |
| F. Candidate generation | The implemented path uses LLM-proposed ratio plus Dirichlet candidates and AK-DAS. Preserve this architecture as the current implemented option; adapt order/units/config behind a tested adapter. Add dedup against all measured candidates and optional approved element bounds. | Feasibility checker before predictor/API submission; unknown model/LLM exposure or credentials -> pause. |
| G. Evaluation and ranking | GBR gives a virtual point prediction; LLM committee gives repeated prompt outputs, not calibrated uncertainty. Score power and cost separately, then Pareto-filter; show novelty and confidence as batch-selection signals. | Do not rank uncalibrated model outputs as measured performance. Out-of-domain candidates require explicit exploration policy or manual review. |
| H. Candidate review and authorization | Show evidence card, formulation, predicted power/cost/uncertainty/novelty, constraints, nearest prior sample, and reason for selection. | Human selects candidates and explicitly authorizes model/API calls and experiments. No execution in current task. |
| I. Experiment/feedback | After authorization, measure candidates and controls; log failed prep and test repeats; append measured rows; keep predicted labels separate. Stability metric is computed only from repeated physical measurements of a recipe across defined batches/devices/conditions. | Revalidate model with new measured data; preserve previous versions and rollback; update only allowed parameters. |
| J. Stop or revise | Stop at approved power/cost criterion with confirmation measurements, evaluation budget, or no decision-relevant improvement; pause if data quality, uncertainty, target protocol or expert review fails. | Record stop reason and next expert action. |

## 6. Proposed Screening Logic

No new scalar reward is approved. Proposed screening order:

1. Hard validity: correct mass-fraction basis/order; finite values; nonnegative; sum one; approved bounds only.
2. Data/model applicability: predictor version known; candidate is in-domain or explicitly flagged exploration; confidence status present; conditions match training domain.
3. Cost availability: actual cost if quote available; otherwise leave actual cost unknown and show proxy separately.
4. Performance/cost trade-off: return Pareto-nondominated candidates over peak-power prediction and actual cost (or approved proxy if specifically declared provisional). Do not inherit `performance_weight=0.6` without approval.
5. Batch diversity: among Pareto/competitive candidates, use measured-sample novelty and batch diversity with the AL's CLR/AK-DAS only after the new order/unit/zero handling is verified.
6. Stability gate: identify top formulations for replicate evaluation; do not label formulations “stable” from a single model prediction or one experiment.

## 7. Expert Views

### Domain-expert view

The scientist confirmed the mass-fraction vector order and simplex rules as hard constraints. Peak device power remains the core objective. Cost, high-performance formulation stability, element-bound rules and target-specific thresholds need finer definition. CRESt's DFFC result (60 °C, 2.0 M KOH + 1.0 M HCOOK, 2.0 mg cm⁻² total loading, reported 325 mW cm⁻²) is precedent only; do not assume this is the target system. The domain expert should define the meaning of “stability” (formulation reproducibility, operational durability, or both) and set any required floor only after measurement conditions are fixed.

### Computer-expert view

The existing AL package provides GBR, LLM generation/committee prediction, Dirichlet candidate generation, CLR/AK-DAS diversity selection, Pareto and weighted-rank code, runtime JSON, and CSV outputs. The inspected data loader drops metadata and normalizes any vector; the hard-coded price table has no auditable source; the pipeline's “queries” are GBR virtual evaluations. The computer expert should confirm an adapter/config mechanism for new mass order, add conditions/provenance/status fields, compute nearest-sample distance and calibrated confidence from validated data, and keep actual cost, proxy cost, and measured power separate. The existing model interface has not been execution-tested under the new schema because execution is not authorized.

## 8. Unresolved Decisions and Confirmation Request

Blocking decisions: target device/reaction/protocol; mass-fraction migration and tolerance; label-source reconciliation; model acceptance/uncertainty criteria; actual cost basis and cost cap; metric definition for stability; allowable element bounds; confidence/novelty screen policy; batch size/experimental budget; reward/Pareto selection policy; and permission for API/model execution.

**Confirmation requested:** review and approve or revise the proposed metric roles, the AL adapter/schema work, and the staged execution gates. No run will be started until explicit authorization is given. The `AL` implementation has been inspected only; no training, candidate generation, scoring, API call, or experiment has been executed for this Round 2 orchestration.

## 9. References

- Round 2 alignment artifacts: `knowledge_alignment_round2/`.
- AL implementation snapshot: `AL/catalyst_active_learning_runnable/README.md`, `config.json`, `catalyst_al/costs.py`, `data.py`, `model.py`, `providers.py`, `sampling.py`, `pareto.py`, `pipeline.py`, `run.py`, `check_environment.py`, `tests/test_core.py`.
- Zhang et al. (2025), CRESt, *Nature* 647, 390–396, DOI https://doi.org/10.1038/s41586-025-09640-5.
- Lookman et al. (2019), “Active learning in materials science with emphasis on adaptive sampling using uncertainties for targeted design,” https://doi.org/10.1038/s41524-019-0153-8.
- Borg et al. (2023), “Quantifying the performance of machine learning models in materials discovery,” https://doi.org/10.1039/d2dd00113f.
- Xu et al. (2024), “Discovering High Entropy Alloy Electrocatalysts in Vast Composition Spaces with Multiobjective Optimization,” https://doi.org/10.1021/jacs.3c14486.
- FCTESQA Test Module PEFC SC 5-2 (2010), https://joint-research-centre.ec.europa.eu/system/files/2017-02/polarisation_curve_testprocedure.pdf (PEFC-only protocol; general QA principles only where transferable).


## Dialogue Based Status Update 2026-10-30

Applicable pending fields have been updated directly using the supplied multi_round_dialogue_example_EN.txt. These are retrospective inferences: general knowledge is accepted in principle, named objectives/constraints are accepted for task use, and requested analyses or ratio adjustment are accepted as requirements. This does not certify numerical values, thresholds, prices, causal mechanisms, detailed recipes or model execution. Mass-fraction versus atomic-fraction conflicts remain unresolved. See the accompanying YAML dialogue_status_reconciliation for the source lines and exact dialogue. No original-file backup was created, as requested.
