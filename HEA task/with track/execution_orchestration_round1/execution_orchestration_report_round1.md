# Execution Orchestration: Eight-Metal Catalyst Formulation, Round 1

## 1. Input Status and Scope

Inputs reviewed, in required order:

1. [Round 2 machine alignment](../knowledge_alignment_round2/knowledge_alignment.yaml)
2. [Round 2 scientific report](../knowledge_alignment_round2/knowledge_alignment_report.md)
3. [Round 2 expert review queue](../knowledge_alignment_round2/expert_review_queue.yaml)

Additional operational context found in `AL/catalyst_active_learning_runnable/`:

- Raw `data/Data.xlsx`, sheet `Result 1`: 703 rows, columns `test_id`, eight compositions in the old order `Pd,Pt,Cu,Au,Ir,Ce,Nb,Cr`, `max_power`, `abandoned`, `abandon_reason`, `outlier`. Of these, 396 are flagged `abandoned=1` with reason `sample prep`; 307 have no abandonment flag and are described in the local data README as eligible records.
- `data/oracle_training_sample.csv`: 120 rows selected by evenly downsampling the 307 eligible records after sorting on `power_density`; it carries no run/batch/device conditions and is explicitly a training subset, not new experimental evidence.
- `data/initial_examples.csv`: 10 seed rows including single-/two-element corners and one equimolar vector.
- `outputs/total_examples_pool.csv`: 160 rows, including accumulated values from a prior run; provenance distinguishes rows only via `example_id` and timestamp, and the bundled README says GBR virtual labels are used by the delivered LLM pipeline.
- Current runnable package assumes `Pd,Pt,Cu,Au,Ir,Ce,Nb,Cr`, has a hard-coded normalized elemental price table, uses a GBR-trained “oracle”, sets synthetic target gains, and labels GBR outputs as virtual rather than true experimental measurements. There is no clear `llm_experiment/` output directory present in the inspected workspace, and no evidence that the current run was a physically executed experiment campaign.

**Representation override.** The materials expert specifies the authoritative working order for this orchestration as **mass fractions** `[Pd, Pt, Au, Cr, Ir, Ce, Cu, Nb]`, with nonnegative entries and sum one. This overrides the Round 2 alignment's *atomic-fraction* order for new orchestration inputs; it does not rewrite the source rows. Existing atomic/nominal or unknown-basis records must be quarantined until their basis is confirmed and converted from verified elemental assay data. Do not relabel atomic fractions as mass fractions.

## 2. Metric Ranking and Proposed Roles

Ranks are workflow priority, not a composite score. The expert-approved statements are the mass-fraction order, nonnegativity, closure, and trade-off existence. Metric role/rank proposals, experimental thresholds, and evaluation methods remain `proposed` pending the project experts' approval.

| Rank | Metric | Proposed role and direction | Threshold guidance | Why this rank |
|---:|---|---|---|---|
| 1 | `M_POWER`: peak areal device power density | Primary objective; maximize. Compute `max_k(V_cell,k * I_k / A_geo)` or `max(V_cell*j_geo)` from a device polarization curve. Keep units `mW cm^-2_geo` or `W cm^-2_geo` consistent. | No universal cutoff. Use application floor if supplied; otherwise compare to a same-protocol control with a predeclared practically meaningful improvement and uncertainty criterion. CRESt precedent: 325 mW cm⁻² at 60 °C, 2.0 M KOH + 1.0 M HCOOK, total loading 2.0 mg cm⁻²; reference only, not target threshold. | It is the requested device endpoint, but device identity, conditions, replicate variance and power test protocol still need approval. |
| 2 | `M_COST`: actual material/precursor cost at stated scale | Secondary objective; minimize subject to adequate power. Keep actual quoted precursor cost distinct from commodity-index proxy. | No accepted numeric budget currently. Require a cost cap only after purchase-region, scale, purity and yield basis are fixed. | Cost trade-off is expert-stated and relevant, but current AL code's cost values are hard-coded elemental price proxies with undocumented vintage/basis, not purchase costs. |
| 3 | `X_Pd, X_Pt, X_Au, X_Cr, X_Ir, X_Ce, X_Cu, X_Nb` | Hard feasibility constraints: each >=0 and sum=1. They are decision variables, not maximization objectives. | Exact closed simplex is confirmed. Component bounds/positive-presence constraints are not. No arbitrary per-element lower bound. | A physically infeasible recipe must not receive a performance score or enter an experimental queue. |
| 4 | `M_PGM` / broader precious-metal loading | Secondary objective or soft budget criterion; minimize only with a performance requirement. Define PGM subset `{Pd,Pt,Ir}` separately from broad precious set including Au; report catalyst-layer loading and mass fractions separately. | CRESt's approximately 1.2 mg cm⁻² precious loading at 2.0 mg cm⁻² total is a study-specific reference. No universal cap. | Direct material-intensity indicator, but category and denominator need expert approval. Avoid double-counting as both cost and cost-specific score. |
| 5 | `M_COST_INDEX`: public-price weighted raw-material proxy | Diagnostic/secondary proxy; minimize if a fixed public price dataset/vintage is approved. | No hard threshold; do not claim proxy as actual cost. | Computable from composition but mismatch between metal, oxide and ferroalloy source forms prevents procurement interpretation. |
| 6 | `M_HALF_CELL`: formate-oxidation activity/current or overpotential | Intermediate/proxy only; maximize activity or minimize overpotential only at a fixed potential/current and protocol. | No portable threshold. Must be calibrated against device response within fixed device/conditions. | CRESt used half-cell LSV with a constant ORR-counter-electrode-overpotential assumption and checked ranking against fuel-cell tests; this remains a study-specific proxy. |
| 7 | Durability, phase/order, morphology, uncertainty | Durability may become constraint after protocol/floor is supplied; phase and morphology are diagnostic/covariates; predictive uncertainty is a screening gate. | No threshold until measurement protocol, assay, repeatability and acceptable failure limits are approved. | Important confounders/risks but not enough current data to rank as objectives. |

### Recommended decision logic

1. **First enforce hard feasibility:** correct mass basis, exact column order, finite numeric fractions, `x_i >= 0`, sum-to-one within agreed input tolerance. Optional element bounds or all-eight-positive requirement remain inactive until approved.
2. **Then apply readiness/quality gates:** source provenance known; label type is measured vs simulated; required device conditions and units known; sample not abandoned/failed unless kept in a separate failure dataset; target finite; composition verified.
3. **Then rank by measured device power and actual cost as separate objectives.** Preserve a non-dominated (Pareto) shortlist instead of fixing an unapproved scalar weighting. For immediate synthesis, a domain expert can select among Pareto candidates after seeing power, cost, uncertainty, feasibility and predicted applicability.
4. **Use half-cell and structural properties as supporting screens, not substitutes for the device endpoint.** Do not activate public cost proxy and actual cost simultaneously as two independent objectives if they are meant to represent the same economics.

## 3. Threshold Guidance

The only defensible hard thresholds currently available are the mass-fraction simplex constraints. No minimum power, budget ceiling, durability floor, per-metal interval, or minimum all-eight positive concentration has been supplied by the relevant owner.

For a **direct-formate-fuel-cell branch only**, CRESt gives a matched-context reference: device operation at 60 °C in 2.0 M KOH + 1.0 M HCOOK, total catalyst loading 2.0 mg cm⁻², and a reported 325 mW cm⁻² peak for its optimized catalyst. It also reports 2.0 mg cm⁻² total metal and about 1.2 mg cm⁻² precious-metal loading. These values can anchor an initial comparator protocol only if the project confirms that chemistry, device architecture, area basis, electrode recipe and test conditions match. They are not universal acceptance cutoffs.

The FCTESQA PEFC SC 5-2 procedure recommends condition-controlled polarization measurement, calibration certificates, documentation of conditioning and data processing, stable voltage before measurement, and recording mean voltage plus variability at each current step. It is a PEFC procedure, not a formate/alkaline-cell standard. Transfer only the general measurement-quality practices; experts must approve chemistry-specific settings.

Recommended threshold source hierarchy:

- Composition: expert-provided simplex constraints (active now); synthesis/assay-validated per-element bounds (pending).
- Power: target-device requirement or same-protocol baseline plus a predeclared minimum improvement and uncertainty criterion (pending).
- Cost: procurement-based cap at named scale and region, or retain as a separate objective on a Pareto frontier (pending).
- Durability: validated test protocol and expert-approved minimum retention/lifetime (pending).
- Model suitability: require out-of-fold/holdout performance, residual review, calibration/uncertainty checks and in-domain status. Numeric acceptance tolerances must be set based on measurement repeatability and decision risk; none is invented here.

## 4. Data Intake and Organization

### 4.1 Freeze the raw source

Create an immutable snapshot of `Data.xlsx` and its sheet, record source path, checksum, extraction date, sheet name, row count and original column names. Keep the 703 source rows unchanged. Define statuses separately: `eligible`, `abandoned_sample_prep`, `outlier_flagged`, `missing_or_invalid`, `simulated_label`, `experimental_label`. Do not silently discard abandoned/outlier rows; route sample-preparation failures to a failure-analysis table, not the response-model training set unless failure prediction is a deliberate separate task.

### 4.2 Resolve the basis before reordering

The existing workbook/example CSV columns use `[Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr]`; the confirmed orchestration format is mass fractions `[Pd, Pt, Au, Cr, Ir, Ce, Cu, Nb]`. For every source, ascertain whether the numbers mean nominal mass fraction, measured mass fraction, or atomic fraction. Only after confirming units, reorder and convert with elemental assay/atomic weights if needed:

`w_i = x_i*M_i / sum_j(x_j*M_j)` for atom-to-mass; inverse `x_i = (w_i/M_i)/sum_j(w_j/M_j)` for mass-to-atom.

Record raw composition, basis, transformed vector, formula/version, assay and uncertainty. Do not infer basis from sums of one: both atom and mass fractions close to one.

### 4.3 One record per experimental unit

Recommended row grain: one physical catalyst/electrode/device measurement or replicate. Required fields include:

- `sample_id`, `batch_id`, `run_id`, `record_origin` (`measured`, `derived`, `predicted`, `simulated`), `source_file`, `sheet`, `source_row`, timestamp, operator/protocol version.
- Canonical mass fractions: `w_Pd,w_Pt,w_Au,w_Cr,w_Ir,w_Ce,w_Cu,w_Nb`, mass fraction, finite, nonnegative, sum one within approved tolerance.
- Nominal and measured compositions separate; elemental assay method, precision/uncertainty, detection/quantification flags.
- Synthesis parameters and precursor identity/grade/lot, yield, catalyst/support/morphology, loading, electrode area, cell architecture, electrode role.
- Reaction/electrolyte/feed, temperature, pressure, concentration, flow, conditioning, scan/current protocol, reference/control, iR correction and area basis.
- `peak_areal_power_density_mW_cm2_geo` as measured response plus source polarization curve or link; measurement uncertainty/replicate ID.
- `precursor_cost_USD_per_batch`, currency/date/region/scale and actual metal loading; keep separate from `raw_price_proxy` and normalized legacy costs.
- Label provenance and quality status; never combine virtual GBR outputs with physical measurements as if same fidelity.

Preferred storage: immutable raw source plus a versioned normalized CSV/Parquet table and linked condition/replicate tables. Maintain a human-readable data dictionary. Run deduplication and unit/schema validation before modeling.

### 4.4 Existing data readiness and risks

The local `oracle_training_sample.csv` is only 120 rows thinned from 307 eligible rows by sorting on power and evenly selecting across that sorted target. This changes the empirical distribution and can bias model fit/evaluation. It must not be treated as the definitive train/test split. The 10-row `initial_examples.csv` and 160-row `outputs/total_examples_pool.csv` also need source reconciliation and row-level provenance; the latter appears from the prototype and is not confirmed as 160 real experiments.

The raw workbook reports 703 rows: 396 `abandoned=1` with reason `sample prep`, 307 without that flag. The `outlier` column is entirely missing in the inspected sheet. Composition sums are approximately 0.998–1.002 in the raw source, compatible with rounded reporting but must be reconciled to the expert's mass-fraction tolerance. The target is `max_power` (range 0–80.63 in the sheet), but device units, protocol and condition columns are absent from this sheet. These are blockers to treating labels as peak areal device power until verified against source metadata.

## 5. Model and Evaluator Interfaces (Algorithm-Neutral)

No model or algorithm has been approved. Register proposed pluggable interfaces only; all statuses remain `proposed`, and no local script/model is assumed authorized for production optimization.

| Interface | Inputs | Outputs | Initial status / required validation |
|---|---|---|---|
| `DATA_VALIDATOR` | Raw row + schema + allowed fraction basis | Valid/invalid flags, reasons, conversion lineage | Proposed; unit tests on order, missing, negative, sum deviation, zeros, duplicate IDs |
| `POWER_EVALUATOR` | Candidate electrode/device record + approved protocol | Measured polarization curve, peak areal power, uncertainty, conditions | Human/experiment interface; target device and protocol pending |
| `COST_EVALUATOR` | Composition mass fractions + actual precursor quote/lot/yield | Actual cost per catalyst/electrode/batch and loading | Data not currently supplied; public proxy must not substitute |
| `COST_PROXY_CALCULATOR` | Composition vector + approved public price table/vintage | Weighted raw-price index with source metadata | Proposed, secondary only; product-form caveat |
| `PROPERTY_PREDICTOR` | Featurized composition + fixed conditions + provenance-approved training data | Predicted power and uncertainty/applicability status | Proposed only; model family not chosen. Must compare against simple baselines and held-out experiment batches. |
| `CANDIDATE_GENERATOR` | Approved mass simplex, bounds, presence rule, dedup pool | Candidate mass vectors and feasibility status | Proposed only; generation method undecided. |
| `DECISION_RANKER` | Feasible candidate predictions, actual cost, uncertainty, Pareto policy | Ranked batch with reasons and constraints | Proposed; do not collapse objectives to arbitrary weighted reward without approval. |

The current local package includes a GBR trained on a thinned 120-row sample and LLM calls that generate/score recipes, but its “oracle” is a virtual prediction model, not a physical experiment. Its hard-coded cost table, old element order and synthetic target-improvement settings require replacement/approval before use. The run package's README explicitly says predictions are GBR-generated and not new experimental measurements. Treat it as an implementation prototype only, not a validated model interface.

## 6. Iterative Workflow

| Stage | Action | Output / gate |
|---|---|---|
| 0. Expert preflight | Confirm target device/reaction, mass-fraction basis/order, presence/bounds, primary power metric/area units, cost definition, hard budgets and experiment protocol. | If any required objective/constraint conflicts remain, workflow is `paused_for_review`; no optimization run. |
| 1. Intake and audit | Freeze source workbook; inspect each sheet/column; join protocol/device/condition records; label experimental vs simulated; keep failures and exclusions with reasons; reconcile raw/seed/pool duplicates. | Versioned raw + curated table, provenance ledger, audit report. No train data until labels/units are verified. |
| 2. Representation migration | Map known input columns by header, not position. Resolve source basis; convert to mass fractions only from confirmed atomic-basis records; reorder to Pd, Pt, Au, Cr, Ir, Ce, Cu, Nb. | Validated mass simplex; all unverified basis rows quarantined, not silently converted. |
| 3. Baseline and train/validation design | Establish baseline metrics and simple reference comparisons. Split by experiment batch/device/date or composition family to reduce leakage; preserve untouched validation/test data. Keep repeated measurements grouped. Evaluate MAE/RMSE and residuals in target units; assess uncertainty and applicability domain. | Model candidate report with measured-label provenance and validation results. No automatic model activation absent criteria approval. |
| 4. Candidate proposal | Generate a diverse feasible batch within approved mass-fraction simplex/bounds; retain boundary and interior coverage only if allowed. Deduplicate against all prior measured/predicted rows. Record generation version, seed, intended trade-off and uncertainty rationale. | Candidate table with stable IDs, feasibility flags and provenance. |
| 5. Virtual evaluation | Apply validated predictor(s), cost calculator and constraints. Predictions include uncertainty and condition compatibility. Reject invalid/out-of-domain candidates or route to manual review. | Feasible shortlist with predicted power, actual/estimated cost status, precious-metal fractions and uncertainty; no prediction is called experimental. |
| 6. Candidate screening | First filter hard constraints; then preserve Pareto-nondominated candidates for power vs actual cost (and optionally PGM loading if not redundant). Within Pareto set choose a batch balancing expected performance, uncertainty, composition diversity and experimental feasibility, under approved policy. | Batch proposal plus auditable selection reasons; domain expert signs off in early rounds. |
| 7. Experiment and replicate | Synthesize/test under locked protocol; interleave reference/control and replicates according to experimental design; record failed preparations. Measure complete polarization curve and compute peak from declared area basis. | Raw observations with calibration, replicate spread, conditions, cost records and failure tags. |
| 8. Feedback and update | Append new measured records; do not overwrite predictions. Recheck schema, drift, replication, residuals, calibration and Pareto front. Retrain/update only within approved workflow; maintain prior model/data version and rollback. | New dataset/model version, performance-vs-budget and Pareto change report, expert feedback log. |
| 9. Stop/pause | Stop when expert-approved performance/cost goal is met with confirmation repeats, evaluation budget is reached, no meaningful improvement persists, or quality/applicability gates fail. | Stop reason, best confirmed recipes, uncertainty, limitations, next-round queue. |

## 7. Candidate Screening and Reward Policy

Hard constraints precede scoring. Initial hard constraints from the materials expert: eight fixed mass-fraction fields in the specified order, each finite and nonnegative, vector sum one. Mass tolerance is not numerically set; use assay/reporting precision and flag rather than silently renormalize values beyond it. Element presence and composition bounds are unresolved and remain inactive. Other potential hard constraints (synthesis safety, approved process range, cost ceiling, minimum power, durability) require explicit approval.

Do **not** instantiate a numeric scalar reward now. Proposed objective tuple:

`maximize measured/predicted peak areal device power; minimize actual cost` subject to approved composition/process constraints.

Keep precious-metal loading as an independent secondary objective only if experts approve it as distinct from actual cost; otherwise report diagnostically to avoid double-counting. Retain the Pareto set for expert selection. Any weighted normalization requires expert approval, immutable scaling reference, and sensitivity analysis. High uncertainty, missing condition compatibility, or out-of-domain status should trigger remeasurement/review rather than optimistic extrapolation.

Suggested candidate batch composition: include (a) promising predicted recipes, (b) informative/high-uncertainty candidates inside approved space, (c) diversity representatives from distinct composition neighborhoods, and (d) repeat/control experiments as required. Exact batch size is limited by experimental capacity and is unprovided; do not inherit the prototype's 10/8/3 query/retain values as scientific requirements.

## 8. Stopping, Parameter Control, and Rollback

- Current model interfaces, parameters, scripts and reward weights: `proposed`/unverified; no executable model authorized by the expert input.
- No autonomous parameter adjustment is enabled. The skill requires an exposed executable and parameter interface, explicit authorized parameters/ranges, access level `adjust_parameters`, and rollback values before auto-tuning.
- Any later adjustment logs old/new value, trigger, evidence/result, expert approval and rollback status. Do not auto-change target definition, composition constraints, device conditions, or safety limits.
- Small-scale preflight must validate units, mass order/conversion, zero/missing handling, simplex and tolerance behavior, objective directions, cost conversion and measurement-interface outputs before a larger campaign.

## 9. Domain-Expert View

The domain expert has supplied the canonical mass-fraction order and simplex rules. Round 2 evidence supports peak device power as the primary response, cost as a distinct trade-off, and nonlinear composition/structure/activity relationships. The CRESt direct-formate result is a relevant but chemistry/device-specific benchmark, not a guaranteed acceptance threshold. The domain expert must approve the target device, reaction, loading, electrolyte/feed, device area, power threshold, cost interpretation, all-eight-presence rule, allowable component bounds, and whether PGM fraction is a separate objective.

## 10. Computer-Expert View

The computer expert should treat each sample/device run as the learning unit, with mass fractions in exact order `[Pd, Pt, Au, Cr, Ir, Ce, Cu, Nb]`; retain both original source columns and a lineage-tracked transformed vector. Responses must distinguish measured peak power, predicted power, legacy `max_power`, and virtual GBR output. Store test conditions, measurement uncertainty, batch/run IDs, actual precursor cost/price date, model version and applicability status. Dataset split should prevent near-duplicate compositions or same-batch replicates leaking into both train and test. Candidate ranking is multiobjective and constraint-first; an algorithm and scalar weighting remain unselected until experts approve.

## 11. Execution State and Next Round

This is an **orchestration draft**, not a running/activated optimization. Existing historical data are discoverable but lack enough recorded condition metadata in the inspected sample files to prove label equivalence to the intended peak device response. The 120-row training subset is target-sorted/thinned; the current bundled pipeline's GBR labels are simulated. First operational milestone is data/provenance reconciliation and mass-basis conversion review, not immediate model training.

Round 1 artifacts: `execution_orchestration_report_round1.md`, `execution_orchestration_round1.yaml`, `execution_review_queue_round1.yaml`, and `execution_trace_round1.jsonl`. The review queue blocks target-specific model fitting and candidate release until expert decisions are captured.

## Evidence and Method Sources

- Round 2 alignment artifacts: `knowledge_alignment_round2/knowledge_alignment.yaml`, `knowledge_alignment_round2/knowledge_alignment_report.md`, `knowledge_alignment_round2/expert_review_queue.yaml`.
- Existing operational package: `AL/catalyst_active_learning_runnable/README.md`, `data/README.md`, `data/Data.xlsx` (Result 1), `data/initial_examples.csv`, `data/oracle_training_sample.csv`, `outputs/total_examples_pool.csv`, `catalyst_al/costs.py`, `catalyst_al/model.py`, `catalyst_al/pareto.py`, `catalyst_al/pipeline.py`.
- Zhang et al., “A multimodal robotic platform for multi-element electrocatalyst discovery,” Nature 647 (2025), DOI https://doi.org/10.1038/s41586-025-09640-5; supplied paper lines on proxy assumption (395), compositions and cost-normalized performance (397–399), test conditions (Fig. 3 caption, around 533), and device performance (around 407). Reports direct-formate testing at 60 °C, 2.0 M KOH + 1.0 M HCOOK, total metal loading 2.0 mg cm⁻²; value 325 mW cm⁻².
- Lookman et al., “Active learning in materials science with emphasis on adaptive sampling using uncertainties for targeted design,” npj Computational Materials 5 (2019): https://doi.org/10.1038/s41524-019-0153-8. Supports iterative surrogate/uncertainty/utility → experiment/computation → add result/update loop and multi-property considerations.
- Borg et al., “Quantifying the performance of machine learning models in materials discovery,” Digital Discovery (2023): https://doi.org/10.1039/d2dd00113f. Defines sequential learning as training, candidate selection, experiment/simulation validation and data update; emphasizes distinct data-splitting/benchmarking.
- Xu et al., “Discovering High Entropy Alloy Electrocatalysts in Vast Composition Spaces with Multiobjective Optimization,” JACS 146 (2024): https://doi.org/10.1021/jacs.3c14486. Evidence for separate activity, cost-effectiveness and entropy objectives with Pareto trade-offs in ORR virtual screening; not direct device-power validation for this target.
- FCTESQA PEFC SC 5-2 (2010), polarization-curve module: https://joint-research-centre.ec.europa.eu/system/files/2017-02/polarisation_curve_testprocedure.pdf. PEFC-specific; useful general measurement QA guidance (calibration, conditioning, metadata, voltage/current/power curve) but not directly applicable as a formate-cell standard.
- USGS Mineral Commodity Summaries 2025, publication DOI https://doi.org/10.3133/mcs2025; cost proxy source details retained in Round 2 alignment. Proxies are not precursor quotes.


## Dialogue Based Status Update 2026-10-30

Applicable pending fields have been updated directly using the supplied multi_round_dialogue_example_EN.txt. These are retrospective inferences: general knowledge is accepted in principle, named objectives/constraints are accepted for task use, and requested analyses or ratio adjustment are accepted as requirements. This does not certify numerical values, thresholds, prices, causal mechanisms, detailed recipes or model execution. Mass-fraction versus atomic-fraction conflicts remain unresolved. See the accompanying YAML dialogue_status_reconciliation for the source lines and exact dialogue. No original-file backup was created, as requested.
