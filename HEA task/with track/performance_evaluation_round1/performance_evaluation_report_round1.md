# Performance Evaluation: Eight-Component HEA Catalyst, Round 1

## 1. Inputs, Versions, and Execution Status

**Input state: `planned_only` for the Round 2 orchestration.** The Round 2 orchestration is explicitly a proposal, no AL model/run was executed for that round, and the AL output directory contains only pre-existing `total_pool.csv` and `total_examples_pool.csv` plus `.gitkeep`. Thus there are no traceable Round 2 candidates, predictions, measured results, or run logs to evaluate. This report defines a reproducible evaluation protocol and provides scripts that will process an explicitly supplied future evaluation CSV. It does not claim current model performance, candidate ranking, convergence, or improvement.

Reviewed inputs:

- [Execution orchestration Round 2](../execution_orchestration_round2/execution_orchestration_round2.yaml), [report](../execution_orchestration_round2/execution_orchestration_report_round2.md), [review queue](../execution_orchestration_round2/execution_review_queue_round2.yaml).
- [Knowledge alignment Round 2](../knowledge_alignment_round2/knowledge_alignment.yaml), report, and expert review queue.
- AL implementation at `../AL/catalyst_active_learning_runnable/`, inspected read-only: README, config, data, model, provider, sampling, Pareto, pipeline, tests and existing CSV/XLSX files.

Current fixed material representation is the expert-specified **mass-fraction** order `[Pd, Pt, Au, Cr, Ir, Ce, Cu, Nb]`, all finite and nonnegative, summing to one within a yet-to-be-approved assay/reporting tolerance. The existing AL code order is `[Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr]`; existing source files cannot be evaluated in the new order until the basis and header mapping are resolved. Preserve raw data and converted data separately.

## 2. Result Coverage and Data Quality

The AL directory has no output from the proposed Round 2 run. Historical assets found:

- `Data.xlsx`, `Result 1`: 703 rows; 396 flagged abandoned and 307 unflagged. The extracted sheet has composition columns and `max_power`, but lacks the device/protocol metadata needed to establish equivalence with target peak areal device power. Raw sums range about 0.998–1.002; do not automatically normalize without assay precision and source-basis confirmation.
- `oracle_training_sample.csv`: 120 points selected from the 307 unflagged rows by sorting on target then evenly downsampling. It is described as GBR virtual-oracle training data, so it is neither a fair independent validation set nor a Round 2 experimental result.
- `initial_examples.csv`: 10 historical seed examples.
- `outputs/total_examples_pool.csv`: 160 rows with old-order fractions and power/timestamp, but row-level measured-versus-predicted provenance and protocol linkage need reconciliation.
- `outputs/total_pool.csv`: 160 rows with list-encoded ratios, `power_density`, and hard-coded `normalized_cost`; provenance and cost basis require reconciliation.

The current AL implementation is a simulation loop: a GradientBoostingRegressor (`512` estimators, learning rate `0.03`, depth `3`, squared-error loss) is trained on the 120-row file using random 80/20 row split; it produces a point `power_density` prediction. The LLM provider generates ratios and repeated prompt predictions; committee standard deviation is prompt dispersion, not calibrated predictive confidence. Candidate proposals use a 20,000-point Dirichlet pool and CLR/AK-DAS diversity (epsilon `1e-6`, sigma `1.5`, lambda `0.5→0.7`); Pareto candidates are then reduced with a batch-relative min-max weighted score (`performance_weight=0.6`). The local cost table has undocumented source units/vintage. These internal values are implementation outputs, not scientific measurements. This skill did not execute these modules.

### Required data validation before evaluation

The plotting script requires an explicit input CSV and expert-approved `--closure-tolerance`; it does not default to historical files. The required fields are: `candidate_id`, `run_id`, eight mass fractions with headers `Pd,Pt,Au,Cr,Ir,Ce,Cu,Nb`, `value_type`, `peak_power_density`, `power_unit`, `area_basis`, `protocol_id`, `device_id`. Additional recommended fields: `iteration`, `batch_id`, `measured/predicted source`, `model_id/version`, `prediction interval`, `actual_cost`, `cost_unit`, `PGM loading`, `conditions_id`, `replicate_id`, `status/failure_reason`, timestamp and source row.

Checks performed by `evaluate_round1.py`:

- Required columns, numeric parseability, finite power/compositions, nonnegative fractions, component values no greater than one, closure residual against passed tolerance.
- Explicit `value_type` classification; non-measured rows are excluded from measured statistics and the default mode rejects mixed measured/non-measured inputs unless `--allow-nonmeasured` is requested for QA only.
- Candidate/run duplicate IDs, missing protocol/device/unit/area metadata, negative power values, missingness, and source-type counts.
- No auto-renormalization, imputation, outlier deletion, or merging across protocol/device/unit/area strata.

## 3. Expert Inputs and Inferred Evaluation Concerns

**Actual expert input inherited from orchestration:** the computer expert confirms peak power density is the core performance metric, with nonnegative mass fractions, sum-to-one, and fixed element order as hard composition constraints. The Round 2 report states execution was not authorized and no target device/protocol was confirmed.

**Skill-inferred domain-expert concerns (unconfirmed):** whether high power is reproducible across independently prepared batches; whether apparent gains depend on device/electrode conditions, loading or morphology; whether trade-offs with actual cost are acceptable; and whether literature DFFC references are comparable to the target device.

**Skill-inferred computer-expert concerns (unconfirmed):** whether the GBR generalizes beyond the target-sorted sample, whether the random row split leaks related compositions/batches, whether LLM dispersion is calibrated, whether composition migration changes distance/feature values, and whether the changing per-batch min-max score distorts cross-round comparisons.

These are analysis questions generated by this Skill, not expert statements.

## 4. Metric Evaluation Protocols

### Scientific performance and candidate metrics

- **Peak areal device power**: primary terminal metric. Calculate `P_A,max=max(V_cell*I/A_geo)` or `max(V_cell*j_geo)` from the device polarization curve. Report canonical units, device, protocol, area basis and replicate uncertainty. Do not infer a device metric from half-cell or GBR values.
- **Cost**: evaluate actual quote/precursor cost separately from the AL normalized-cost proxy. Report currency, date, region, precursor grade, yield, scale and denominator. Do not use hard-coded `normalized_cost` as actual cost.
- **Composition validity**: pass rate for fixed-order mass fractions satisfying nonnegativity and closure tolerance. Report bound violations and basis-migration status. Per-element bounds/all-positive policy are unavailable and must not be invented.
- **Candidate-to-data distance/novelty**: nearest measured-sample distance, explicitly naming feature space and zero treatment. AL's current CLR/Aitchison Euclidean distance uses epsilon `1e-6`; recompute only after mass-basis/order migration and compare sensitivity. Treat as coverage/novelty, not a performance metric.
- **Model confidence**: report prediction residual metrics on genuinely held-out measured data; if intervals exist, interval coverage and mean width. GBR currently emits point predictions only; LLM repeated prompts provide dispersion, not calibrated confidence. Do not label either as calibrated confidence without validation.
- **High-performance formulation stability**: distinguish (a) recipe reproducibility (power spread over independent batches/devices under a fixed protocol) from (b) long-term electrochemical durability (power/activity retention under stress). No replicate or durability results are presently available. Report n, mean, SD, CV and interval per candidate only when replicate records exist; no stability threshold is approved.

### Statistical summaries

For measured candidate performance within one comparable condition stratum, report `n`, mean, median, SD, min/max, and a bootstrap 95% interval for the mean where `n>=2`. For candidate comparisons, prefer paired differences when candidates share matched run/batch/device conditions; report effect size and interval. If observations are independent and assumptions are checked, a suitable group comparison may be proposed, but the analysis script does not auto-select significance tests. Avoid treating technical replicates as independent batches. Report raw points alongside summaries.

For held-out predictor evaluation, report MAE, RMSE, R², residual plots, and interval coverage/width when interval predictions exist. Use group/batch/device/time-aware splits where identifiers permit; never use the target-sorted 120-row sample as an unbiased holdout. Any outlier exclusions, unit conversion and missing-data handling must be logged. No p-values or confidence claims are produced without actual eligible measurements.

### Candidate-set and optimization metrics

- Validity rate, unique candidate rate, duplicate rate, rejected-candidate reasons, zero/presence distribution, and per-element marginal distribution.
- Nearest-measured distance distribution and composition-space coverage (representation disclosed).
- Pareto set over measured/predicted power and actual cost only when both are defined; report measured and predicted Pareto sets separately. Do not compute hypervolume or scalar reward unless objective scaling/reference points are pre-registered.
- Round-by-round best/median measured power and spend/evaluation count only for actual runs with traceable run IDs; predicted/GBR curves shown separately and visibly labeled `virtual/predicted`.

## 5. Analysis and Plotting Plan

The plotting implementation is [evaluate_round1.py](./evaluate_round1.py). It accepts only an explicit future CSV and requires the user to provide closure tolerance; it does not invoke AL or an API. With no eligible measured evaluation file, no figures or statistics are currently generated.

| Figure/Table | Scientific question | Plot/table | Conditions/limits |
|---|---|---|---|
| T1 Data QA | What is evaluable and what is missing/invalid? | QA JSON + validated row CSV; value-type and issue counts | Keep abandoned/virtual/predicted/measured classes distinct. |
| F1 Candidate power | How does measured peak power vary by candidate? | Raw-point bar/dot summary with SD only for replicates | Stratified by protocol, device, unit and area basis; no cross-stratum pooling. |
| F2 Iteration performance | Is measured performance improving across rounds? | Best and mean measured power by iteration with SD band | Requires actual run ID/iteration and measured values; predicted trajectories separate. |
| F3 Power-cost trade-off | Which measured candidates are non-dominated? | Scatter of actual cost vs measured peak power; Pareto overlay may be added after approved definitions | No proxy cost plotted as actual; same cost basis and device conditions required. |
| F4 Composition matrix | Which fractions characterize measured candidate outcomes? | Heatmap of canonical mass-fraction vectors by candidate | Descriptive only; not causal element-effect evidence. |
| F5 Prediction diagnostics | Does the model predict measured held-out outcomes? | Predicted vs measured with identity line, residuals; intervals/calibration only if supplied | Use held-out measured records; source model/version and units visible. |
| F6 Stability | Are high-performing formulations reproducible? | Replicate distributions/intervals by candidate and batch | Only when independent replicate records exist; distinguish preparation variability from durability. |

`evaluate_round1.py` currently implements F1/F2/F3/F4 and a basic QA summary; F5 is supported only if input has explicit prediction columns, and calibration metrics require prediction interval columns. No figures are fabricated in this round. All figures will be exploratory unless conditions and protocol are verified.

## 6. Benchmark Registration

- **CRESt DFFC benchmark**: Zhang et al. (2025) reports 325 mW cm⁻² for an optimized catalyst at 60 °C, 2.0 M KOH + 1.0 M HCOOK, total metal loading 2.0 mg cm⁻², with about 1.2 mg cm⁻² precious metal. Status: `context_only` until target device, area basis, protocol and formulation match; no superiority ratio is currently valid.
- **Pure Pd comparator** in CRESt: article reports relative gains (5.6x power for one listed composition, 9.3x power normalized by catalyst cost for another). Status: `context_only`; composition/cost equation and conditions must be checked in supplement before quantitative comparison.
- **PEFC SC 5-2 polarization procedure**: quality guidance for calibration, conditioning and test metadata; status: `not_comparable` as a direct numerical benchmark for alkaline direct-formate cell unless a PEFC target is confirmed.
- **Internal AL historical pool**: `invalid_or_untraceable` for confirmed device performance until label source, units, conditions and composition basis are reconciled. Legacy GBR values are `predicted`/`simulated`, not measured.

## 7. Computer-Expert View

No actual Round 2 run/model evaluation exists. Before model scoring, require: validated input schema, source/value type, basis migration, conditions, versioned split, grouping against leakage, training configuration, and run IDs. Report performance metrics in physical units, with errors and confidence intervals. Evaluate calibration separately from LLM committee spread. Track runtime/API calls only from actual logs; AL config defaults are not run results. A future evaluation should treat GBR predictions, LLM-generated predictions, measured device responses, derived cost and literature-reported values as different record types.

## 8. Domain-Expert View (`electrochemical_catalysis`)

No domain expert has supplied a specific evaluation request or reviewed results in this round. The Skill-inferred concerns are: comparability of peak power across protocols; replicate variability of high-performing recipes; power/cost/PGM trade-off; contribution of morphology/phase versus composition; and applicability of the CRESt formate device precedent. No mechanistic conclusion or element-specific causal effect can be drawn from the available pool.

## 9. Cross-Domain Joint Judgment

Evaluation readiness is **low/blocked for performance claims**, but **adequate for preparing the analysis protocol and script**. The main bottleneck is not plotting capability; it is the lack of a traceable, condition-compatible measured evaluation set and the unresolved mass-fraction migration. The computer view calls for provenance/split/model calibration checks; the domain view calls for protocol matching and replicate testing. The joint recommendation is to resolve schema and protocol, label historical values by source type, then evaluate measured candidates and virtual predictions in separate panels/tables.

## 10. Skill-Generated Adjustment Recommendations

These are `skill_inference`, not expert decisions:

1. Add a versioned mass-order migration/validation adapter and preserve raw vectors, basis and closure residual.
2. Expand AL candidate/run records to include `value_type`, model/version, conditions, unit, device, area basis, source row, batch and replicate IDs.
3. Keep predicted GBR and LLM outputs out of measured performance statistics; expose calibrated intervals only after separate calibration evidence.
4. Add measured replicate evaluation for high-performing formulations; do not conflate it with electrochemical lifetime/durability.
5. Replace/rename legacy normalized cost after verifying its price source/basis; actual cost requires procurement and yield data.
6. Do not activate statistical testing, literature superiority ratios, or performance thresholds until the protocol/comparability gate is passed.

## 11. Expert Feedback, Gaps, and Next Round

The user provided Ubuntu runtime/API availability, but no endpoint credentials/configuration or permission to call the API; this is recorded as environment availability, not execution authorization. Evaluation scripts are prepared but not run against current ambiguous files. Next round requires a versioned result CSV with measured target-compatible records, approved closure tolerance, source status, device protocol, actual cost fields and replicates, then expert review of thresholds and plots.

## 12. References

- Execution orchestration Round 2 files: `../execution_orchestration_round2/`.
- AL implementation and data: `../AL/catalyst_active_learning_runnable/`.
- Zhang et al., CRESt, *Nature* 647 (2025), DOI https://doi.org/10.1038/s41586-025-09640-5.
- Lookman et al. (2019), active learning in materials science, https://doi.org/10.1038/s41524-019-0153-8.
- Borg et al. (2023), model performance in materials discovery, https://doi.org/10.1039/d2dd00113f.
- Xu et al. (2024), multiobjective HEA electrocatalyst discovery, https://doi.org/10.1021/jacs.3c14486.
- FCTESQA PEFC SC 5-2 test module (2010), https://joint-research-centre.ec.europa.eu/system/files/2017-02/polarisation_curve_testprocedure.pdf. This is PEFC-specific, not a DFFC standard.
