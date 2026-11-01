# Execution Orchestration: Octonary HEA Catalyst Formulation (Round 1)

## 1. Purpose and input status

This draft converts `knowledge_alignment_round2/` into an auditable, iterative workflow for optimizing an eight-metal catalyst against device peak power density and material cost. It is a workflow specification, not an assertion that a model, experiment script, price feed, or device protocol is currently runnable. The saved dialogue confirms the performance-cost tradeoff and composition-constraint requirements; detailed thresholds, schema reconciliation, and operating conditions still require review.

Inputs read: `knowledge_alignment.yaml`, `knowledge_alignment_report.md`, and `expert_review_queue.yaml`; the corpus manifest and prior execution trace were also inspected for provenance. The literature corpus supplies methodological support: octonary catalyst search and cost-specific performance (E201), active learning for HEA nanocatalysts (E204), compositional-data treatment (E202/E203), interactions and ordering effects (E207-E209/E213), and multiobjective/Pareto methods (round2 report, sources 39-40). These sources motivate a workflow, not a universal prediction law.

### Representation conflict to resolve

The project brief specifies **mass fractions** in order `[Pd, Pt, Au, Cr, Ir, Ce, Cu, Nb]`. Round2's literature-derived example uses **atomic/molar fractions** in order `[Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr]`. These are not interchangeable. This draft treats the user-provided mass fraction basis and order as the requested design interface, while requiring a distinct field, explicit basis metadata, and expert approval before activation. Do not feed round2 atomic/molar vectors into a mass-fraction model as if they were identical. If existing data are atomic/molar fractions, retain them as such and convert only with documented atomic weights and conversion provenance; never overwrite the source vector.

## 2. Metric ranking and threshold guidance

Ranking is a proposed operational order, not a final expert decision. It prioritizes goal relevance, evidence and condition comparability, measurement/model readiness, feasibility, and decision value. There is no evidence-supported universal absolute performance threshold for this device.

| Rank | Metric | Proposed role and direction | Threshold / screen guidance | Rationale and evidence |
|---|---|---|---|---|
| 1 | I204: Eight mass fractions | Hard feasibility; each in `[0,1]`, sum to 1 | Use decimal mass fractions; candidate validator tolerance provisionally `abs(sum-1) <= 1e-6` after declared rounding. Keep this explicitly subject to computer/materials approval. | Non-negativity and closure are mathematical constraints; round2 E202/E203 support simplex-aware composition handling but on atomic/molar basis. User brief defines mass basis and order. |
| 2 | I201: Device peak power density, `P_peak` | Primary objective; maximize | Lock a single device, reaction, active area, loading, temperature, pressure, voltage/current sign convention, and polarization protocol. Screen against a matched reference/baseline under the same conditions; require replicate uncertainty and only claim improvement when the pre-agreed comparison rule is met. No universal numeric cutoff. | Direct project endpoint (E212); octonary electrocatalysis context E201. Round2 says half-cell activity cannot substitute for device power. Highest goal relevance, but data readiness is low until protocol and existing-data coverage are checked. |
| 3 | I202: Catalyst material cost | Secondary objective or budget constraint; minimize | Declare currency, quote date, metal product form, purity, scale, and catalyst-mass basis. Until an approved budget exists, report the cost and compare only with a same-basis baseline; do not exclude candidates by an invented ceiling. | E201/E205/E206; commodity context is not a current procurement price. Highly computable once price inputs and mass basis are fixed. |
| 4 | I203: Cost-specific peak power, `P_peak / C_mass` | Secondary objective; maximize, or diagnostic if experts prefer | Use only when both operands share the same candidate, device protocol, and declared cost basis. Compare to matched baseline with uncertainty; do not substitute it for either objective. | Round2 E201 reports cost-specific improvement; no universal unit basis or threshold. It is mathematically coupled to ranks 2-3, so show Pareto trade-offs and avoid double-counting without approval. |
| 5 | I205: Element support count | Conditional hard constraint; target 8 only after confirmation | Define detection/presence epsilon from analytical method, uncertainty, and intended nominal-vs-measured rule. Do not equate a positive recipe entry with retained/measurable presence. Until set, mark support status unknown and send to expert review. | E204 and round2 indicate nominal, bulk, and surface composition differ; `K=8` is provisional. |
| 6 | I207: Phase/ordering feasibility | Hard or soft constraint after allowed states are approved | Use expert-defined accepted state labels plus characterization uncertainty. Unknown state is `review`, not silently feasible. No generic entropy/phase number. | E209/E213 show ordering and structure can change electrocatalytic behavior; transfer to this composition/device is uncertain. |
| 7 | I210: Stability retention | Hard/soft constraint; maximize | Define response variable, time/cycle protocol, failure rule, and minimum retention with domain experts; compare only matched tests. No free-standing percentage threshold. | Stability is a project-relevant constraint; threshold and test duration require expert definition (E209). |
| 8 | I215: Synthesis reproducibility | Hard/soft constraint; minimize CV | Estimate from independent synthesis/device replicates; set maximum CV only after estimating measurement noise and process capability. Report replicate count and interval. | Round2 flags this as important but data-poor (E218). |
| 9 | I208/I209: Fixed-condition current density / overpotential | Secondary or diagnostic; maximize current, minimize overpotential | Fix reaction, electrolyte, reference, potential/current, temperature, loading, and method; use matched-condition baseline or training-data percentile for triage only. Never pool incompatible reactions. | E214 and round2 review; these are not device-level `P_peak`. |
| 10 | I214: Predictive uncertainty | Diagnostic and candidate-selection signal | Calibrate on held-out data; require measured interval coverage to meet the validation protocol selected for the model. No numeric coverage target is imposed here; choose it before model comparison. High uncertainty triggers review/measurement, not fabricated precision. | Active-learning and BO evidence E217; uncertainty supports exploration and guards against out-of-domain ranking. |
| 11 | I212/I211/I213: Entropy, ECSA activity, adsorption descriptor | Intermediate/feature/diagnostic, not primary objective by default | Entropy has no generic HEA cutoff; ECSA/adsorption metrics require method/reaction-specific matched references. Use only when reliable and separately labeled. | Round2 E208/E215/E216; mechanistic and cross-reaction transfer is unresolved. |

Threshold policy: every threshold must carry a status (`validated_hard`, `expert_provisional`, `baseline_relative`, `data_percentile`, or `unresolved`), source, condition, units, and approver. Baseline-relative thresholds require the same device and test protocol. Data-percentile thresholds are exploratory triage derived only from a documented, condition-matched training set; they are not scientific acceptance limits. Set no scalar reward weights until experts decide whether cost is a co-objective, cap, or reporting metric.

## 3. Data and model workflow

### Step A: Intake and data organization

1. Freeze raw inputs as immutable records. Preserve paper/source/run identifiers, original units, original fraction basis and element order, raw polarization curves, synthesis conditions, device metadata, and replicate identity.
2. Normalize into JSONL records at one row per `candidate_id × synthesis_run_id × test_condition_id × replicate_id`. Use separate named fields `x_nominal_mass`, `x_measured_bulk_mass`, and `x_measured_surface_mass` in the user-requested order. Keep any original atomic/molar vectors in separate fields with their own basis and order. Never merge nominal, bulk, and surface composition.
3. Attach `condition_id`, reaction, device architecture, active area, catalyst role/loading, temperature, pressure, electrolyte, reference electrode, test protocol, raw curve location, instrument, date, and provenance. Record every target as `{value, unit, condition_id, uncertainty, status: measured|derived|predicted, source_id}`. Preserve replicates; calculate summary statistics without deleting raw values.
4. Validate schema, numeric types, non-negativity, closure, missingness, duplicate keys, units, outliers against raw records, and categorical consistency. Mark invalid rows and reasons; do not silently repair compositions or impute targets. Convert atomic/molar to mass basis only through a versioned, reproducible transformation while retaining both source and derived values.
5. Compute cost from the selected cost basis and time-stamped element prices/quotes. If cost inputs are unavailable, label cost missing and do not train or rank on a guessed value. Partition evaluation by candidate/synthesis group where possible to prevent replicate leakage.

### Step B: Establish protocol and baseline

Before training a model used to rank candidates, confirm which rows measure the same device endpoint and condition. Build a matched-condition baseline from existing data and identify the eligible training set, target coverage, replicate structure, and gaps. Hold out groups (not individual replicates from the same group) for evaluation. If existing data do not contain sufficient comparable device-level `P_peak`, the workflow may organize data and run diagnostics, but must not claim a reliable `P_peak` predictor; collect baseline/replicate experiments first.

### Step C: Model registration and training

No specific model or optimizer is selected in this round. The registered interfaces are abstract slots: composition/condition-to-metric predictor or surrogate, uncertainty estimator, candidate generator, cost calculator, and constraint checker. Computer expert must supply model identity, version, script/repository, environment, entrypoint, input/output schema, parameter exposure, and execution authorization. Until then, each is `proposed`, with no claim of availability or execution.

After data audit, compare suitable candidate approaches against simple baselines using grouped validation and condition-aware splits. Choose model family only after sample size, noise, missingness, feature schema, and extrapolation needs are assessed. Track metrics per target (e.g., error and calibration), not only a composite score. Record training-data IDs, preprocessing version, random seed where applicable, validation results, applicability domain, and failure cases. Keep predicted, calculated, and experimental values distinct. Do not autonomously alter model parameters unless an executable and parameter interface, authorized parameter list/ranges, and rollback are explicitly provided.

### Step D: Candidate generation and evaluation

Generate candidates in the eight-part mass-fraction simplex, in the fixed user-provided order. Enforce non-negativity and closure at generation, preserve precision, and apply only expert-approved per-element bounds, support rules, synthesis limits, and allowed phase constraints. Until the exact-eight presence policy is approved, retain feasible nominal recipes but label support constraint unresolved. Candidate generation is an interface, not a specified algorithm: it may later be replaced with an expert-approved design-of-experiments, search, or active-learning strategy.

For each candidate, run deterministic checks first: schema/order/basis, closure, support when defined, price availability, and approved synthesis constraints. Then request registered predictors/calculators. Evaluate each objective separately with uncertainty and applicability-domain status. Reject only hard-constraint violations; route uncertain/out-of-domain, unknown-phase, missing-cost, or poorly supported predictions to review/measurement. Rank feasible candidates by Pareto dominance on `P_peak` and the approved cost representation (cost minimization or cost-specific power), rather than inventing weights. Preserve the Pareto set and show uncertainty and constraint status alongside every candidate.

### Step E: Screening, experiment, feedback

1. Screen candidate table for valid composition, complete conditions, model domain, uncertainty, phase feasibility, and price provenance. Emit `measure`, `review`, or `reject` with explicit reason codes.
2. Select a small pilot batch using expert-approved balance of predicted performance, cost trade-off, uncertainty, and practical synthesis/measurement budget. Batch size and acquisition strategy remain configurable, not assumed. Include suitable reference/control and replicate candidates as defined by experimental experts.
3. After synthesis, measure realized bulk and (when appropriate) surface composition and characterize phase/ordering. Run the locked device protocol. Capture raw curves, technical metadata, replicate outcomes, failures, and cost quote date. A failed synthesis remains data with failure status, not a deleted row.
4. Compare predicted vs measured values; update calibration, applicability domain, and residual diagnostics. Append new observations with immutable provenance, retrain/revalidate only under approved model controls, and re-score the Pareto set. Log which candidates were selected, why, actual resource use, and whether predicted gains replicated.
5. Domain expert can approve/revise/reject metrics, thresholds, feasibility labels, and scientific interpretation. Computer expert can approve/revise model interface, validation, data transforms, generation, and resource settings. Preserve both contributions and conflicting feedback; rerun a small regression/pilot check after any change affecting a live workflow.

## 4. Reward, controls, and stopping

Initial reward is intentionally multiobjective and unweighted: maximize `P_peak`, minimize `C_mass` or maximize `P_cost` only after its status is selected, subject to approved feasibility. Hard constraints precede objectives. Report Pareto candidates; do not scalarize until an approved policy and normalization are available. Prediction uncertainty can affect selection priority, but not be interpreted as observed performance.

Automated parameter adjustment is disabled. In a future approved run, each tunable parameter needs allowed values/range, maximum change per round, trigger, rollback value, and change history. Never change the scientific objective, unapproved hard thresholds, raw data, production scripts, or model applicability domain automatically. Stop or pause when a critical input/protocol conflict remains, model output cannot map to a metric, data are out-of-domain, uncertainty is uncalibrated, hard constraints conflict, an expert pauses, or budget/stopping criteria are reached. A pilot must test units, missing values, closure and support checks, constraint triggers, reward directions, and export schema before scaled use.

## 5. Specialist views

### Domain expert view

Contribution recorded from the materials expert: the eight elements are Pd, Pt, Au, Cr, Ir, Ce, Cu, and Nb; recipes are mass-fraction vectors in fixed order; entries are nonnegative and sum to one; objectives trade off device peak power and cost. This is applied as the requested draft interface, with basis/order conflict against round2 raised rather than concealed. The domain expert must approve device endpoint and test conditions, nominal vs measured support rule and detection threshold, accepted structure states, precious-metal set, stability/reproducibility limits, and cost policy. Element-specific performance signs remain hypotheses; no fraction direction is prescribed.

### Computer expert view

Contribution recorded from the computer expert: construct an iterative workflow from existing composition-performance data. This draft supplies immutable data contracts, validation, grouped evaluation, abstract model/generator/evaluator interfaces, Pareto-based candidate screening, experiment ingestion, and a feedback loop. No model, package, script location, compute environment, authorized parameter, or optimizer was provided, so none is treated as callable. The computer expert must register interfaces and access permissions before execution; parameter automation remains disabled.

## 6. Unresolved decisions and next round

Resolve high-priority composition basis/order, device protocol and target coverage, cost basis and role, detection epsilon/exact-eight semantics, phase acceptance, and model availability/authorization before candidate ranking. Then run schema-only validation and a small end-to-end pilot before enabling any formal iterative optimization. All threshold changes and expert feedback must be versioned and linked to downstream model/reward/workflow changes.

## 7. Evidence references

- Round2 `E201`: Zhang 2025 multimodal robotic electrocatalyst discovery; explicit octonary system and cost-specific design context.
- Round2 `E202`/`E203`: compositional data and simplex-aware statistical treatment; supports explicit fraction basis and closure semantics, not interchangeability of atomic and mass fractions.
- Round2 `E204`: Perumal 2025 active learning for high-entropy nanocatalysts; supports iterative exploration while noting transfer/prediction limitations.
- Round2 `E207`/`E208`: multi-element electrocatalysis and high-throughput Pt-based HEA screening; synergy evidence is composition/reaction specific.
- Round2 `E209`/`E213`: ordering and phase dependence in HEA electrocatalysis; motivates realized structure fields and feasibility review.
- Round2 `E205`/`E206`: cost burden and USGS commodity context; requires dated, product-specific procurement inputs rather than assumed universal prices.
- Round2 `E217`: uncertainty/active-learning methods; supports calibrated uncertainty and review routing.
- Literature source map in round2 report, section 5: sources 39-40 motivate Pareto/multiobjective treatment; exact objective scalarization remains an expert decision.

Working-knowledge acceptance and confirmed task roles are recorded in the reconciled upstream YAML; evidence-level verification and unanswered review questions remain unresolved. No new numeric scientific cutoff or current market price is asserted.

## Dialogue-based status reconciliation (2026-10-31)

Current statuses record general knowledge acceptance, working supplements, and explicitly selected objectives and constraints from the saved expert dialogue. Unselected metrics remain candidates. Fraction-basis/order conflicts, numerical thresholds, cost provenance, model validation, and execution authorization remain explicit. Original version-history snapshots and execution traces are unchanged. The accompanying YAML expert_feedback_reconciliation records the source excerpts and scope of each update.
