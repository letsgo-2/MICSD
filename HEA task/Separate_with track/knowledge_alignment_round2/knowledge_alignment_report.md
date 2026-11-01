# Scientific Knowledge Alignment: Round 2

## 1. Project goal and input evidence

**Goal.** Optimize the formulation of an eight-component HEA catalyst for higher electrochemical-device peak power density while accounting for precious-metal material cost and preserving composition/structure feasibility.

**Round2 changes.** This document supplements, and does not overwrite, round1. It adds: (i) element-level domain context for the explicit octonary example in `26_Zhang_2025...md`, (ii) possible synergies and content-effect hypotheses, (iii) cost as a separate optimization objective, (iv) a canonical computer data contract, and (v) calculation and threshold semantics for iterative metrics.

**Evidence policy.** All 43 uploaded papers remain primary evidence. Authoritative online sources are used for terminology, periodic properties, and price-data provenance only. Direct online retrieval was partially blocked in this run; no current price values or unsupported identifiers are asserted. All element-to-peak-power effects remain hypotheses unless directly measured for the selected device.

## 2. Core concept system

| ID | Concept | Round2 definition | Evidence/status |
|---|---|---|---|
| C201 | Explicit octonary example | `Pd-Pt-Cu-Au-Ir-Ce-Nb-Cr`, the eight-element chemical space reported for formate oxidation by CRESt. The later EO round 1 dialogue adopts these eight elements; this literature example uses a different order from the project interface. | `26...md:11`; eight_element_identity_confirmed_example_order_requires_reconciliation |
| C202 | Eight-element composition vector | Ordered vector `x=[x_Pd,x_Pt,x_Cu,x_Au,x_Ir,x_Ce,x_Nb,x_Cr]`, with each value a non-negative atomic/molar fraction and sum 1. | `33...md:29-35`; `34...md:21-29`; composition_constraint_role_confirmed_mass_basis_reconciliation_required |
| C203 | Nominal vs measured composition | Nominal recipe fractions and measured bulk/surface fractions are distinct data objects; retention, segregation, and surface enrichment must not be silently conflated. | `23...md:12-16`; `26...md:11-13`; accepted_as_working_knowledge_from_dialogue |
| C204 | Precious-metal cost burden | Time-varying raw-material cost contribution from elements such as Pd, Pt, Au, and Ir, calculated from a declared price source, date, purity/form, and mass basis. | `26...md:11-13`; USGS Mineral Commodity Summaries; accepted_as_working_knowledge_from_dialogue |
| C205 | Composition-to-device mapping | A learned or measured mapping from formulation plus process/device conditions to peak power density. It is not established by half-cell activity alone. | `23...md:12-13`; `26...md:11-13`; accepted_as_working_knowledge_from_dialogue |
| C206 | Synergy hypothesis | A proposed non-additive interaction among elements, structure, and reaction intermediates. It becomes a claim only after matched-condition evidence. | `04...md:25-27`; `12...md:15-19`; `21...md:7-13`; accepted_as_working_knowledge_from_dialogue |

## 3. Eight-element domain-expert supplement

### 3.1 Principal characteristics and evidence status

The table uses the explicit octonary order in `26_Zhang_2025...md`. “Likely catalytic role” is a hypothesis or transferable context unless the cited paper measures it in the selected device. Atomic numbers and periodic-table identity are stable descriptors; prices are not stable material constants.

| Element | Principal characteristics relevant to formulation | Possible catalytic/structural contribution | Possible synergy hypotheses | Content-to-peak-power interpretation |
|---|---|---|---|---|
| Pd | Noble transition metal; high catalytic relevance in oxidation/ORR contexts; costly and supply-sensitive relative to base metals. | May provide active sites and electronic interaction with Pt/coinage metals. | Pd-Pt electronic/strain interaction; Pd-Cu/Au surface or ensemble effects. | Increasing Pd may raise activity in a compatible oxidation/ORR device but increases cost; sign and nonlinear optimum unresolved. |
| Pt | Noble transition metal; benchmark electrocatalyst for HER/ORR and a major cost driver. | Strong activity contribution and tunable adsorption/electronic structure. | Pt-Fe/Co/Cu/Ni ordering evidence is reported in `21`; Pt with Pd/Au/Ir may alter adsorption and stability. | More Pt may improve kinetics but can reduce cost-specific performance; optimal fraction is device- and condition-dependent. |
| Cu | Abundant, conductive transition metal; lower raw-material cost than noble metals; can modify electronic structure and dilute precious-metal loading. | Conductivity, alloying, strain/ensemble effects, and cost reduction. | Cu-Pt/Pd/Au may tune adsorption and active-site ensembles; direct octonary power evidence absent. | Increasing Cu may reduce cost and can improve or reduce activity depending on phase/surface; effect must be learned under fixed conditions. |
| Au | Noble coinage metal; chemically stable and costly; electronic/ensemble effects can be important at surfaces. | Stability, surface electronic modification, and possible selective oxidation behavior. | Au-Pd/Pt/Cu surface ensembles are plausible but not proven for peak power. | Higher Au raises cost; any power gain must exceed the cost penalty and be experimentally measured. |
| Ir | Noble platinum-group metal; high catalytic relevance for oxidation/OER contexts; costly and supply-sensitive. | Oxidation stability and electronic modification; exact role depends on reaction. | Ir-Pt/Ru-like oxidation-site interactions are plausible; no project-specific direct claim. | Increasing Ir may help oxidation-side durability/activity but can increase cost; direction unresolved. |
| Ce | Rare-earth element; redox-active oxide chemistry and oxygen-storage/defect associations are common context, but alloy-state behavior is system-specific. | Defect, oxygen-affinity, support/interface, or electronic-modification effects. | Ce with noble metals may tune oxygenated intermediates or stabilize interfaces. | Content effect may be non-monotonic and phase-dependent; no direct peak-power evidence. |
| Nb | Refractory early transition metal; high melting point and alloy/oxide-forming behavior; cost basis depends on product form. | Structural stabilization, lattice/oxide/interface modification, and dilution of noble metals. | Nb-Cr/Ce may alter oxide/defect structure; Nb with Pt-group elements may alter strain/electronic states. | May improve durability or reduce precious-metal fraction, but excessive Nb could lower conductivity/activity; unresolved. |
| Cr | Abundant transition metal; oxide-forming and corrosion/phase behavior must be controlled in the actual electrolyte. | Structural/electronic modification and possible cost dilution; oxidation-state behavior is condition-sensitive. | Cr-Ce/Nb oxide/defect interactions and Cr-Pt-group surface effects are hypotheses. | Increasing Cr could lower raw cost but may change stability, conductivity, and active surface; no validated sign. |

**Evidence boundary.** The uploaded corpus directly supports octonary search and cost-specific improvement (`26`), eight-element active-learning methodology (`23`), multi-element electronic/DFT synergy in other compositions (`04`, `12`), and ordering-dependent performance (`21`). It does **not** establish a universal monotonic relationship between any one of these eight fractions and device peak power density. The element rows above are therefore formulation priors and validation hypotheses, not recommendations.

### 3.2 Possible synergy groups

- **Noble-metal activity group:** Pd-Pt-Ir-Au. Hypothesis: complementary adsorption/electronic effects may improve kinetics or durability, but cost can rise sharply.
- **Precious-metal dilution/conductivity group:** Cu with Pd/Pt/Au. Hypothesis: Cu can lower material cost and alter surface ensembles; the active-surface fraction must be measured.
- **Oxide/interface/defect group:** Ce-Nb-Cr. Hypothesis: these elements may change defect chemistry, oxide interfaces, phase stability, and mass transport; the alloy/oxide state must be characterized.
- **Ordering/strain group:** Any pair or group that changes local chemical ordering, lattice distortion, or surface motif distribution. `21` shows that ordering can matter independently of nominal composition.

These groups are not independent additive effects. Interaction terms should be represented as hypotheses or learned features only when the dataset contains sufficient matched-condition observations.

## 4. Core indicator system for round2

The skill’s scores are retained: importance, computability, and data readiness are 1-5. Thresholds below are **status labels**, not universal scientific limits.

| ID | Metric | Meaning/calculation | Role/direction | Provisional threshold semantics | Data source |
|---|---|---|---|---|---|
| I201 | Peak power density `P_peak` | `max_j [V_j * j_j]` after declaring voltage/current-density signs, active area, device architecture, and operating conditions; report W cm^-2 and raw curve. | Primary objective; maximize | No universal range. Use fixed-device baseline and percentile/replicate uncertainty; target `P_peak > baseline` only after protocol lock. | Device polarization/power curve; project experiments; concept supported as endpoint by user request. |
| I202 | Precious-metal material cost `C_mass` | `C_mass = M_cat * sum_i(x_i * M_i / M_mix * p_i)` or equivalent mass-fraction form, with price `p_i` time-stamped by element/product/form/purity. | Secondary objective or constraint; minimize | No timeless threshold. Use budget ceiling or baseline-relative `C_mass <= C_budget`; report price date and currency. | USGS/official commodity source or procurement quote; `26` supports cost-specific optimization. |
| I203 | Cost-specific power `P_cost` | `P_peak / C_mass` under a declared cost basis; do not confuse with catalyst mass activity. | Secondary objective; maximize | No universal range. Compare to same-basis baseline and uncertainty interval. | Derived from I201/I202 and provenance fields. |
| I204 | Composition fractions `x_Pd...x_Cr` | Eight atomic/molar fractions in fixed order; `0 <= x_i <= 1`, `sum(x_i)=1`. | Design variables with hard feasibility constraint; context-dependent | Exact eight-element support may require `x_i >= epsilon_presence`; epsilon is experimental/detection-limit policy, not universal. | Recipe and measured composition analysis; `33`, `34`, `23`, `26`. |
| I205 | Element support count `K` | `K = count_i(x_i >= epsilon_presence)` using declared epsilon and measured or nominal vector. | Hard composition constraint; target `K=8` if project confirms | `K=8` is a project requirement candidate, not guaranteed by an eight-slot vector. | ICP/OES/XPS/EDS or equivalent plus recipe. |
| I206 | Precious-metal fraction `X_PGM` | `sum(x_i)` over project-defined Pd/Pt/Ir (and optionally Au); classification must be declared. | Cost-control constraint/intermediate; minimize subject to performance | Project-defined upper bound or baseline-relative cap; no universal threshold. | Composition vector and element classification policy. |
| I207 | Phase/ordering feasibility | XRD/SAED/TEM/spectroscopy/CALPHAD/DFT-derived state; categorical plus uncertainty. | Hard/soft constraint; target accepted state | Use expert-defined allowed labels; no universal numerical interval. | `02`, `06`, `21`, `25`, process and characterization records. |
| I208 | Reaction current density `j_ref` | Current density at a fixed reaction, potential, electrolyte, temperature, loading, and reference electrode. | Secondary objective/diagnostic; maximize | Use fixed-condition baseline or percentile bounds; never pool reactions. | Half-cell curve; `04`, `07`, `11`, `12`, `21`, `23`. |
| I209 | Overpotential `eta_ref` | Potential offset from the declared thermodynamic/reference condition at a fixed current density. | Secondary objective; minimize | Fixed reaction/current-density protocol; no cross-reaction universal threshold. | Polarization curve and reference calibration. |
| I210 | Stability retention `R_t` | `100 * y(t)/y(0)` for selected output `y` (power, current, or activity), with time/cycle and failure criteria. | Hard/soft constraint; maximize | Expert-defined minimum retention at fixed duration; report time/cycles, not a free-standing number. | Repeat/long-term device or catalyst tests; `21`, `23`. |
| I211 | ECSA-normalized activity | `j/ECSA` or mass activity under fixed protocol; ECSA method and uncertainty required. | Intermediate/diagnostic; maximize | No universal threshold; use matched-method baseline. | Electrochemical ECSA measurement and loading; cross-paper comparability unresolved. |
| I212 | Configurational entropy `S_mix` | For ideal mixing, `S_mix = -R sum_i x_i ln(x_i)`; calculate from the same composition basis and document whether nominal or measured. | Intermediate/soft constraint; context-dependent | Do not impose a generic HEA cutoff without expert approval; compare to project-defined phase-screening range. | Composition plus `02`, `03`, `25`, `39`. |
| I213 | Adsorption/binding descriptor | DFT or learned energy for named adsorbate/site/coverage/model; target range is reaction-specific. | Intermediate/feature; target_range | No universal interval; use validated reaction-specific reference/uncertainty. | DFT/ML; `04`, `12`, `17`, `39`. |
| I214 | Model predictive uncertainty `U` | Calibrated interval width or posterior standard deviation for each predicted metric. | Diagnostic/selection; minimize while retaining exploration | Calibration target is model-specific; require held-out calibration and uncertainty coverage. | AL/BO model; `14`, `20`, `23`, `26`, `41`. |
| I215 | Synthesis reproducibility `CV_rep` | `100 * sd(y_rep)/mean(y_rep)` for repeated synthesis/device measurements, with replicate count. | Hard/soft constraint; minimize | Project-defined maximum CV; no universal value. | Replicate experiments; currently data-poor. |

### Priority interpretation

- **P0:** I204/I205 (composition feasibility) and I201 once the device protocol is fixed.
- **P1:** I202/I203/I207/I210/I208/I209/I212, because cost, stability, structure, and reaction performance constrain useful formulations.
- **P2:** I211/I213/I214/I215, useful for interpretation, surrogate modeling, or experimental selection but not yet universally comparable.
- **P3:** Any metric whose condition, denominator, product, phase identity, or measurement protocol is missing.

## 5. Computer-expert optimization view

### 5.1 Distinct roles

1. **Peak power density is the primary performance objective.** It asks whether the integrated device delivers more usable power under a fixed protocol. It must be measured or predicted from device-level data.
2. **Cost is a secondary objective or explicit budget constraint.** It penalizes precious-metal loading and must use time-stamped, product-form-specific prices. Cost is not a proxy for activity and cannot replace `P_peak`.
3. **Composition constraints define the feasible design domain.** Closure, non-negativity, support count, allowed elements, phase/ordering, synthesis limits, and measured-retention rules determine which formulations may be proposed. They are not objectives unless the project explicitly chooses a soft penalty.

The default multiobjective interpretation is maximize `(P_peak, P_cost)` subject to composition/phase/stability feasibility. A scalar utility may be used later only after experts provide a cost basis and trade-off policy; this round does not choose weights.

### 5.2 Canonical eight-component representation

**Canonical example order for the explicit CRESt system:**

```text
element_order = ["Pd", "Pt", "Cu", "Au", "Ir", "Ce", "Nb", "Cr"]
```

The order is part of the dataset schema and must be stored in metadata. It must not be inferred from column order.

**Numeric representation:**

```text
x_nominal: [float64, float64, float64, float64, float64, float64, float64, float64]
x_measured_bulk: [float64 x 8] | null
x_measured_surface: [float64 x 8] | null
```

Fractions are atomic or molar fractions in `[0,1]`, serialized as decimal numbers, not percentages; recommended input precision is at least `1e-6`. Required validation is `abs(sum(x_nominal)-1) <= 1e-6` after declared rounding. Mass fractions must use separate named fields. A zero means “zero under the declared representation/detection policy,” not automatically “element absent.”

**Row granularity:** one row is one `candidate_id × synthesis_run_id × test_condition_id × replicate_id`. Do not collapse repeated tests into one row without retaining replicate statistics.

### 5.3 Input/output data contracts

**JSONL input record:**

```json
{"candidate_id":"c0001","element_order":["Pd","Pt","Cu","Au","Ir","Ce","Nb","Cr"],"x_nominal":[0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125],"x_measured_bulk":null,"x_measured_surface":null,"synthesis":{"method":"...","temperature_K":null,"time_s":null},"device":{"device_id":"...","reaction":"...","temperature_K":null,"pressure_Pa":null,"active_area_cm2":null,"loading_mg_cm2":null},"targets":{"peak_power_density_W_cm2":null,"cost_USD_g_cat":null},"provenance":{"source_id":"S026","source_type":"paper|experiment|calculation","run_id":"..."}}
```

**JSONL prediction/output record:**

```json
{"candidate_id":"c0001","predictions":{"peak_power_density_W_cm2":{"mean":null,"lower":null,"upper":null},"material_cost_USD_g_cat":{"mean":null,"lower":null,"upper":null},"cost_specific_power_W_USD":{"mean":null,"lower":null,"upper":null}},"constraint_status":{"closure":true,"support_count":8,"phase_status":"unknown","cost_budget":null},"recommended_action":"measure|reject|review","model_version":"..."}
```

CSV is allowed for flat tables only if a companion metadata file stores `element_order`, units, fraction basis, closure tolerance, detection threshold, price date/source, and condition definitions. JSONL is preferred for nested conditions and provenance.

### 5.4 Metric calculation and data-source rules

For iterative optimization, every target must carry `value`, `unit`, `condition_id`, `uncertainty`, `measurement_or_prediction`, and `source_id`. Derived metrics must retain their operands and formula version. Thresholds are either `validated_hard`, `expert_provisional`, `baseline_relative`, or `data_percentile`; no unmarked number is a universal scientific threshold.

## 6. Structure-property-mechanism-performance relations

- Composition changes phase, ordering, defects, surface motifs, and electronic/adsorption states (`02`, `03`, `06`, `21`, `25`).
- Multi-element interactions can change electronic structure and catalytic behavior (`04`, `12`), but the magnitude and sign depend on reaction and realized structure.
- Active learning can navigate octonary spaces (`23`, `26`), but `23` reports a boundary: HER improvement with limited initial OER predictive accuracy.
- Ordering can improve activity/stability for Pt4FeCoCuNi (`21`), showing why measured structure belongs in the data contract.
- Cost-specific performance was a reported design outcome in the octonary robotic study (`26`), supporting a separate cost metric but not a universal price or objective weight.
- The causal link from any elemental fraction to `P_peak` is unresolved until the selected device, operating conditions, and matched formulation dataset are defined.

## 7. Evidence, online sources, and conflicts

### Uploaded primary evidence

All 43 sources remain registered in `corpus_manifest.jsonl`. The strongest round2 anchors are `26` for explicit octonary identity and cost-specific improvement, `23` for eight-element active learning, `04` and `12` for multi-element/DFT synergy, `21` for ordering-performance dependence, `33` and `34` for simplex representation, `39` and `40` for multiobjective/Pareto reasoning, and `17` for adsorption-energy-to-current-density modeling.

### Authoritative online source classes

- IUPAC Gold Book, `https://goldbook.iupac.org/`, for standardized chemical terminology where an exact term is available; access attempted in this run but some pages returned 403/transport errors.
- NCBI PubChem element records, `https://pubchem.ncbi.nlm.nih.gov/`, for element identity and stable atomic descriptors; direct element-page fetches were blocked in this run.
- USGS Mineral Commodity Summaries, `https://www.usgs.gov/centers/national-minerals-information-center/mineral-commodity-summaries`, for production/supply and commodity context; price basis must still be supplied by a dated market or procurement source.
- NIST Chemistry WebBook, `https://webbook.nist.gov/chemistry/`, for thermochemical/physical reference data where applicable; it does not provide a universal catalyst-price series.

These source classes support definitions and data provenance. They do not establish that a specific fraction increases device peak power.

### Conflicts and non-comparabilities

- The explicit eight-element identity appears in `26`; `23` confirms eight transition-metal elements but does not identify them in the extracted paper text.
- Reaction metrics span HER, OER, ORR, oxidation, and other systems; they cannot be pooled as one target.
- Nominal recipe, bulk composition, surface composition, and active-site composition are different variables.
- Material prices vary by date, purity, chemical form, market, and procurement scale. A static “cost per gram” would be misleading.
- Device peak power density and half-cell current density have different physical levels and denominators.

## 8. Expert validation and round2 decisions

The domain and computer requirements are incorporated as explicit supplements. The later orchestration dialogue supplies the eight-element identity and confirms the core objective and composition-constraint roles. The supplements are accepted as working knowledge; element-specific effect signs, thresholds, cost basis, device mapping, and fraction-basis/order reconciliation remain unresolved. The expert queue identifies the decisions needed before iterative optimization.

## 9. Metrics eligible for subsequent iteration

After protocol confirmation, the minimum usable set is: `x_nominal`/`x_measured_*` under the canonical order; `P_peak` as primary target; `C_mass` and/or `P_cost` as cost objective; closure/support/phase/stability as constraints; and condition-specific current density/overpotential as secondary or diagnostic metrics. The data contract must be satisfied before a record is eligible for model training or candidate recommendation.

## Dialogue-based status reconciliation (2026-10-31)

Current statuses record general knowledge acceptance, working supplements, and explicitly selected objectives and constraints from the saved expert dialogue. Unselected metrics remain candidates. Fraction-basis/order conflicts, numerical thresholds, cost provenance, model validation, and execution authorization remain explicit. Original version-history snapshots and execution traces are unchanged. The accompanying YAML expert_feedback_reconciliation records the source excerpts and scope of each update.
