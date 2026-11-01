# Scientific Knowledge Alignment: Round 1

## 1. Project goal and input evidence

**Project goal.** Optimize the elemental composition of an eight-component high-entropy alloy (HEA) catalyst to increase the peak power density of an electrochemical device using the catalyst.

**Domain.** High-entropy alloy electrocatalysts, composition-constrained materials discovery, electrochemical devices, and active-learning-assisted optimization.

**Evidence policy.** The 43 uploaded markdown papers are the primary evidence. Online sources are used only to clarify terminology or measurement semantics and are not treated as proof of a catalyst structure-performance relationship. The later Round 2 dialogue generally accepts the existing knowledge; applicable statuses now record that scoped acceptance, with unresolved scientific and technical details retained.

**Important scope boundary.** Most uploaded papers report catalyst-level activity, selectivity, stability, or computed descriptors, whereas the requested objective is a device-level peak power density. The mapping between these levels is therefore a hypothesis/validation item, not an established conclusion.

### Corpus coverage

All 43 markdown files under `literature_markdown/` are registered in `corpus_manifest.jsonl`. The corpus includes HEA fundamentals, electrocatalysis, octonary/high-throughput experiments, active learning and Bayesian optimization, inverse design/LLMs, compositional-data analysis, diversity selection, and multiobjective optimization. Several methodological papers are relevant to representation and search but do not provide electrochemical catalyst evidence; they are retained and labeled accordingly.

## 2. Core concept system

| ID | Concept | First-round definition and scope | Mapping/evidence | Status |
|---|---|---|---|---|
| C001 | High-entropy alloy | A multicomponent alloy design family whose composition and configurational disorder can stabilize unusual solid-solution/intermetallic states; exact classification thresholds and phase criteria vary across the corpus. | `03_Miracle...md`; `07_Zhang...md`; `08_Batchelor...md`; `25_Qi...md` | accepted_in_principle_from_dialogue |
| C002 | Octonary composition | A composition with eight modeled elemental parts. It is a design-space cardinality, not by itself proof of a single-phase HEA or equal fractions. | `23_Perumal...md`; `26_Zhang...md`; `15_Jang...md` | accepted_in_principle_from_dialogue |
| C003 | Composition simplex | Relative elemental fractions constrained by non-negativity and a constant-sum closure, normally sum(x_i)=1. Aitchison/Egozcue provide the statistical basis; zero components require special treatment. | `33_Egozcue...md:29-35`; `34_Aitchison...md:21-29` | accepted_in_principle_from_dialogue |
| C004 | Configurational entropy | An entropy descriptor of composition-dependent mixing; the exact thermodynamic convention, temperature dependence, and use as a phase-stability proxy must be fixed for this project. | `02_Cantor...md`; `03_Miracle...md`; `06_Li...md`; `39_Xu...md` | accepted_in_principle_from_dialogue |
| C005 | Cocktail/synergistic effect | A corpus term for non-additive effects of multiple elements on electronic structure, adsorption, phase, or activity. It is a mechanism hypothesis unless tied to a specific experiment/calculation. | `04_Li...md:25-27`; `05_Yao...md`; `12_Pan...md`; `13_Ren...md` | accepted_in_principle_from_dialogue |
| C006 | Local chemical ordering | Spatial/chemical arrangement beyond bulk elemental fractions; ordering can change electronic structure and electrocatalytic behavior. | `21_Wang...md:7-13` | accepted_in_principle_from_dialogue |
| C007 | Electrocatalytic activity | Reaction-specific catalytic rate/performance under stated electrochemical conditions. It is not automatically equivalent to device peak power density. | `07_Zhang...md`; `11_Katiyar...md`; `13_Ren...md` | accepted_in_principle_from_dialogue |
| C008 | Peak power density | Maximum measured device power normalized by the declared area or other basis, normally obtained from a power-current/voltage curve. Device architecture, operating conditions, normalization, and test protocol are essential. | Device-specific definition is not consistently supplied by the corpus; see `expert_review_queue.yaml` | accepted_in_principle_from_dialogue |
| C009 | Structure-property-performance chain | Composition -> phase/ordering/defects/surface structure -> electronic structure/adsorption/intermediates -> reaction metrics -> device output. Each arrow may be causal, correlational, proxy, or unresolved. | `04_Li...md`; `12_Pan...md`; `21_Wang...md`; `39_Xu...md` | accepted_in_principle_from_dialogue |
| C010 | Active learning / Bayesian optimization | Sequential design of experiments that updates a predictive/uncertainty model and selects new candidates; uploaded papers provide examples but do not establish one universally valid workflow. | `14_Lookman...md`; `20_Niu...md`; `23_Perumal...md`; `26_Zhang...md`; `41_Important...md` | accepted_in_principle_from_dialogue |
| C011 | Pareto optimality | A candidate is nondominated with respect to multiple objectives; no single candidate is preferred without an additional decision rule. | `39_Xu...md`; `40_Deb...md` | accepted_in_principle_from_dialogue |
| C012 | Compositional data | Data describing parts of a whole; relative information and closure make ordinary unconstrained feature treatment potentially misleading. Log-ratio/simplex methods are relevant. | `33_Egozcue...md:9-13`; `34_Aitchison...md:21-29` | accepted_in_principle_from_dialogue |

## 3. Core indicator system

Scores use the skill's 1-5 scale: importance, computability, and data readiness. These are first-round assessments, not expert approvals.

| ID | Indicator | Unit/conditions | Role | Direction | Imp. | Comp. | Data readiness | Priority | Evidence / acquisition |
|---|---|---|---|---|---:|---:|---:|---|---|
| I001 | Peak power density | W cm^-2 or declared device-normalized unit; fixed device, temperature, feed, pressure, area, and protocol | primary_objective | maximize | 5 | 4 | 1 | P1 | Device polarization/power curve; not consistently reported in corpus |
| I002 | Elemental fractions x1...x8 | molar/atomic fraction, sum=1, xi>=0; synthesis tolerance required | design_variable | context_dependent | 5 | 5 | 3 | P0 | Composition analysis/synthesis input; `33`, `34`, `23`, `26` |
| I003 | Element support cardinality | count of nonzero/experimentally present elements; target is eight only if required by project | hard_constraint | target_range | 5 | 5 | 3 | P0 | Composition and analytical verification; project requirement plus `23`, `26` |
| I004 | Phase/solid-solution or intermetallic state | phase label under specified synthesis/anneal/test condition | constraint | target_range | 5 | 3 | 2 | P1 | XRD/SAED/TEM/CALPHAD/DFT; `02`, `06`, `21`, `25` |
| I005 | Chemical ordering degree | dimensionless or method-specific order parameter; measurement definition required | intermediate | context_dependent | 4 | 3 | 2 | P1 | Diffraction/spectroscopy/model; `21` |
| I006 | Particle size / morphology / porosity | nm and morphology descriptor; include support/loading | intermediate | context_dependent | 4 | 4 | 2 | P1 | TEM/SEM/BET/porosimetry; `04`, `05`, `23` |
| I007 | Electrochemically active surface area (ECSA) | cm^2 or normalized proxy with method and electrolyte | intermediate | maximize only under fixed protocol | 4 | 3 | 1 | P1 | Electrochemical measurement; cross-paper comparability unresolved |
| I008 | Reaction current density | mA cm^-2 at stated potential and reference | secondary_objective | maximize at fixed condition | 4 | 5 | 3 | P0 | Electrochemical test; `04`, `07`, `11`, `12`, `23` |
| I009 | Overpotential | mV at stated current density and reaction | secondary_objective | minimize | 4 | 5 | 3 | P0 | Polarization curve; `07`, `11`, `13`, `21` |
| I010 | Tafel slope | mV dec^-1, fit range and equation required | diagnostic | minimize/context_dependent | 3 | 4 | 2 | P2 | Tafel fit; `04` reports 102.40 mV dec^-1 |
| I011 | Mass activity / specific activity | A mg^-1 or A cm^-2(ECSA), reaction and potential required | secondary_objective | maximize | 4 | 4 | 2 | P1 | Electrochemical measurement; `21`, `12` |
| I012 | Selectivity / Faradaic efficiency | %, product and potential/time required | constraint or secondary_objective | maximize target product | 4 | 4 | 2 | P1 | Product analysis; `04` reports 97.43% selectivity and 96.75% FE at 1.65 V vs RHE |
| I013 | Stability / retention | time, cycles, retained activity or power %, protocol required | constraint | maximize retention | 5 | 3 | 2 | P1 | Long-term test; `21`, `23`, `07` |
| I014 | Cost-specific performance / critical-element burden | declared cost basis; economic boundary required | secondary_objective/constraint | maximize performance and minimize cost | 3 | 3 | 1 | P2 | `26`, `39` |
| I015 | Configurational entropy descriptor | J mol^-1 K^-1 or normalized value; convention required | intermediate/constraint | target_range or maximize only if justified | 4 | 4 | 2 | P1 | derive from composition; `02`, `03`, `25`, `39` |
| I016 | Adsorption energy / intermediate binding descriptor | eV for specified site, adsorbate, coverage, and computational method | intermediate/feature_only | target_range | 4 | 2 | 2 | P1 | DFT; `04`, `12`, `39` |
| I017 | Electronic-structure descriptor | method-specific (e.g., d-band/charge/coordination) | feature_only | context_dependent | 3 | 2 | 1 | P2 | DFT/spectroscopy; `04`, `21` |
| I018 | Predictive uncertainty | model-specific unit or calibrated interval | diagnostic/constraint | minimize subject to exploration | 3 | 5 | 2 | P2 | AL/BO model; `23`, `26`, `41` |
| I019 | Candidate diversity / distance | metric-specific, composition/structure space | diagnostic/selection criterion | maximize coverage | 3 | 5 | 3 | P2 | MMR/DPP/AL methods; `36`, `37`, `39` |
| I020 | Synthesis reproducibility | variance or pass rate under repeated preparation/test | constraint | minimize variance/maximize pass rate | 5 | 3 | 1 | P1 | repeated experiments; not consistently available |

## 4. Domain-expert view

The domain view is organized as the sequence **composition -> realized structure -> active surface/electronic state -> reaction behavior -> device output**.

1. **Composition.** The eight elemental fractions are the controllable design variables. Closure and analytical uncertainty must be represented explicitly. A nominal eight-element recipe does not establish that all eight elements are retained in the catalyst, surface, or active phase.
2. **Realized structure.** The corpus repeatedly identifies phase constitution, lattice distortion, defects, nanoparticle size, porosity, and ordering as performance-relevant. `21_Wang...md` is especially direct: increasing ordering in Pt4FeCoCuNi is reported to improve HER/ORR mass activity and stability. This relation is system- and reaction-specific.
3. **Electronic/adsorption state.** `04_Li...md` attributes lactic-acid-oxidation performance to synergistic electronic-structure effects and reports DFT support. `12_Pan...md` combines high-throughput ORR measurements with DFT to examine element/site contributions. These are evidence-backed study-specific relations, not universal composition rules.
4. **Reaction metrics.** Current density, overpotential, Tafel slope, mass activity, selectivity, Faradaic efficiency, and retention quantify reaction behavior under conditions. They should not be merged across reactions, electrolytes, reference electrodes, normalization bases, or device architectures.
5. **Device performance.** Peak power density is the requested endpoint, but most corpus evidence stops at half-cell or catalyst-level metrics. A domain expert must specify the electrochemical device, role of the catalyst, active area, operating point, and test protocol before a valid catalyst-to-power mapping can be asserted.

## 5. Computer-expert optimization view

### Optimization targets

```yaml
primary:
  - I001
secondary:
  - I008
  - I009
  - I011
  - I012
  - I014
constraints:
  - I003
  - I004
  - I013
  - I020
intermediate:
  - I005
  - I006
  - I007
  - I015
  - I016
diagnostic:
  - I010
  - I018
  - I019
not_ready:
  - I001
  - I014
  - I020
```

The apparent conflict between `I001` as primary and `not_ready` is intentional: it is the required objective but is not yet data-ready for cross-candidate optimization. No candidate should enter downstream task orchestration until device-level measurement semantics are fixed.

### Representation and data-unit requirements

- Represent the eight fractions on a simplex; do not independently regress all eight raw fractions without a closure-aware transformation or constrained model.
- Keep composition, synthesis/process conditions, realized structure, electrochemical test conditions, and device conditions as separate fields. A row should be at least `candidate x condition x replicate`, not merely one composition vector.
- Do not pool HER, OER, ORR, oxidation, and device-power outcomes as one target. Use reaction/device identity and condition metadata.
- Preserve nominal and measured composition separately, including detection limits and missing/zero semantics.
- Record uncertainty, replicate count, normalization area, catalyst loading, electrolyte, temperature, pressure, potential scale, and reference electrode.
- Use multiobjective/Pareto representations only after the domain expert confirms which metrics are simultaneous objectives versus constraints. `39_Xu...md` and `40_Deb...md` support the concept, not a project-specific objective weighting.

## 6. Structure-property-mechanism-performance relations

| ID | Relation | Type | Conditions/caveat | Evidence | Confidence |
|---|---|---|---|---|---|
| K001 | Elemental composition changes the accessible HEA property and phase landscape. | correlation/mechanism hypothesis | Exact phase boundary and compositional domain are system-dependent. | `02`, `03`, `25` | medium |
| K002 | Multi-element combinations can alter electronic structure and catalytic activity beyond simple single-element behavior. | mechanism claim | Directly supported in study-specific DFT/experiment, but “cocktail effect” is not a universal quantitative law. | `04`, `12`, `13` | medium |
| K003 | Chemical ordering in Pt4FeCoCuNi correlates with improved HER/ORR performance and stability. | correlation with mechanistic support | Applies to the reported composition, structure, reactions, and conditions. | `21:7-13` | high for study, low for generalization |
| K004 | Active learning can improve composition search efficiency for eight-element nanocatalysts. | method-performance claim | `23` reports HER success but limited OER predictive accuracy; transfer to device power is unverified. | `23:7-17` | medium |
| K005 | Multimodal knowledge-assisted BO can optimize octonary electrochemical chemistry and diagnose experimental anomalies. | method-performance claim | `26` reports >900 chemistries and 3,500 tests for formate oxidation; target and platform differ from this project. | `26:1-13` | medium |
| K006 | Activity-only optimization may produce candidates that are not entropically stabilized; multiobjective optimization can balance activity, cost, and entropy. | methodological claim | Supports objective design, not a universal weighting or device-power relation. | `39:11-20` | high for method premise |
| K007 | Composition closure requires simplex/log-ratio-aware statistical treatment. | statistical definition/method | Applies to fraction data; zeros and detection limits require expert/statistical decisions. | `33:9-13,29-35`; `34:21-29` | high |
| K008 | Catalyst-level activity metrics predict peak device power density. | hypothesis | Not established by the current corpus; device architecture and mass-transfer/electrical losses may dominate. | No direct corpus evidence | low |

## 7. Evidence and conflicts

- **Directly relevant octonary evidence:** `23_Perumal...md` (eight transition-metal elements; HER discovery; OER limitation) and `26_Zhang...md` (octonary chemistry; multimodal BO; formate oxidation).
- **Directly relevant HEA electrocatalysis:** `04`, `07`, `11`, `12`, `13`, `21`, `24`, `39`.
- **Phase/structure/composition foundations:** `01`, `02`, `03`, `05`, `06`, `08`, `09`, `25`.
- **Optimization and data methods:** `14`, `15`, `16`, `17`, `18`, `19`, `20`, `22`, `23`, `26`, `29`, `31`, `32`, `33`, `34`, `36`, `37`, `38`, `39`, `40`, `41`, plus methodological papers in the manifest.
- **Metric conflict:** catalyst activity, current density, mass activity, selectivity, FE, and device peak power have different denominators and physical levels. They must not be treated as interchangeable.
- **Condition conflict:** reaction, electrolyte, pH, potential scale, loading, area, temperature, and device architecture differ across papers. Cross-paper ranking is not valid without normalization and expert review.
- **Terminology conflict:** “HEA,” “high-entropy nanoparticle,” “high-entropy material,” intermetallic, and medium-entropy alloy are not assumed equivalent.

## 8. Importance and priority interpretation

`P0` is reserved for composition variables and directly measurable reaction metrics that can be operationalized under fixed conditions. `P1` contains the requested device objective and high-value constraints that need protocol/data completion. `P2` contains diagnostics/features useful for interpretation or model support. `P3` is not assigned to a core metric in this round; unresolved terms and unsupported mappings are instead held in the review queue.

## 9. Expert certification state

No scientific, experimental, computational, or computer-expert approvals are claimed in this first round. The machine-readable review queue is the authoritative list of unresolved questions.

## 10. Evidence and decisions still required

The main blockers are device definition, measurement protocol, catalyst/device integration, comparability of normalization, verification of eight-element retention, and confirmation of which phase/ordering states are acceptable. These are enumerated with required expert roles and priorities in `expert_review_queue.yaml`.

## 11. Metrics eligible for downstream task orchestration

Only after expert validation: `I001` peak power density under a fixed device protocol; `I002` eight elemental fractions under closure; `I003` eight-element support; and explicitly declared structural/electrochemical constraints. Current density, overpotential, mass activity, selectivity/FE, stability, and entropy may be secondary or constraint metrics only when their reaction, conditions, normalization, and evidence are aligned with the target device.

## Dialogue-based status reconciliation (2026-10-31)

Current statuses record general knowledge acceptance, working supplements, and explicitly selected objectives and constraints from the saved expert dialogue. Unselected metrics remain candidates. Fraction-basis/order conflicts, numerical thresholds, cost provenance, model validation, and execution authorization remain explicit. Original version-history snapshots and execution traces are unchanged. The accompanying YAML expert_feedback_reconciliation records the source excerpts and scope of each update.
