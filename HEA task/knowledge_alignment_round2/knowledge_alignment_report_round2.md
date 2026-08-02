# Knowledge Alignment Report Round 2

## 1. Round 2 Scope And Evidence Status

Round 2 keeps the Round 1 knowledge base as confirmed by domain experts and adds two requested supplements:

1. A clearer domain-expert supplement on the eight metals in the Pd-Pt-Cu-Au-Ir-Ce-Nb-Cr catalyst system, including main catalytic characteristics, possible synergistic roles, and plausible element-content effects on peak power density.
2. A clearer computer-expert supplement on data representation, target/constraint roles, computable indicators, calculation methods, optimization directions, reasonable ranges, and input/output forms for iterative formulation optimization.

Primary evidence remains Zhang et al., "A multimodal robotic platform for multi-element electrocatalyst discovery", Nature 647, 390-396 (2025), DOI: https://doi.org/10.1038/s41586-025-09640-5. The most relevant primary-paper evidence is:

- CRESt discovered catalysts in the octonary Pd-Pt-Cu-Au-Ir-Ce-Nb-Cr chemical space and reported 9.3-fold improvement in cost-specific performance versus pure Pd benchmark.
- The target was maximum power density of a fuel-cell device using synthesized catalyst for formate oxidation, with ORR at the counter electrode.
- The paper used three-electrode current/potential data as a simplified proxy, assuming formate oxidation half-cell behavior and constant ORR overpotential, and stated that this gave relatively consistent catalyst ranking versus fuel-cell experiments.
- The optimized compositions include Pd0.487Pt0.185Cu0.018Ir0.037Ce0.106Nb0.168 with 5.6x power density and Pd0.381Pt0.080Cu0.009Au0.004Ir0.020Ce0.086Nb0.338Cr0.082 with 9.3x cost-normalized performance versus pure Pd.
- Fuel-cell comparison conditions: 60 C, 2.0 M KOH, 1.0 M HCOOK, total catalyst loading 2.0 mg cm^-2.
- Fast screening conditions: three-electrode setup under nitrogen sparging at ambient conditions, 10 ul cm^-2 precursor loading, about 0.05 mg cm^-2 for pure Pd, scan rate 50 mV s^-1.
- Mechanistic analysis states that Pd and Pt serve as primary active elements for formate oxidation; Au and Ir have prior use in direct formate fuel cells; Cu, Ce, Nb, and Cr could alloy with primary elements to tailor coordination environments and reduce catalyst cost.
- The optimized octonary catalyst showed a single FCC phase by XRD/Rietveld, Pd and Pt retained metallic states during formate oxidation, and DFT indicated lower direct/indirect pathway barriers and stronger resistance to hydrogen/CO poisoning relative to pure Pd.

Supporting local evidence remains the active-learning package under `AL/catalyst_active_learning_runnable/`:

- `data/README.md` defines CSV columns: `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr, power_density`.
- Eight metal fractions are normalized to sum to 1.
- The 120-row `oracle_training_sample.csv` is for a GBR virtual experimental oracle and is not new real experimental evidence.
- `costs.py` defines element order and a local normalized-cost formula using fixed metal price weights relative to Pd.
- `pipeline.py` outputs `total_pool.csv`, `iteration_log.csv`, `query_log.csv`, and `generated_ratios.csv`; query logs include `llm_mean`, `llm_std`, `ucb_score`, `power_density`, `normalized_cost`, and `final_score`.

External authoritative evidence added in Round 2:

- PubChem PUG-View element records for Pd, Pt, Cu, Au, Ir, Ce, Nb, and Cr were used only to confirm formal element names, symbols, atomic numbers, and InChI element identifiers.
- USGS official `.gov` mineral information pages were used as authoritative source categories for platinum-group metals, copper, and rare earth cost/supply context. Exact current prices were not inserted because the accessible pages did not provide a single project-ready price table for all eight elements.
- IUPAC Gold Book and EMMO/ECHO terminology evidence from Round 1 remains valid for catalyst/electrode-reaction/electrochemistry concept alignment.

## 2. Confirmed Round 2 Concept Updates

| Concept ID | Concept | Round 2 Confirmation / Update | Evidence | Status |
|---|---|---|---|---|
| C001 | Octonary Pd-Pt-Cu-Au-Ir-Ce-Nb-Cr catalyst | Confirmed as the design object. The optimization variable is an eight-component composition vector over this fixed element set. | Zhang 2025; local AL README/code | expert-confirmed base, representation clarified |
| C006 | Composition vector | Confirmed as numeric fractions in fixed order `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr`. Each row must be non-negative and normalized to sum to 1. | `data.py`, `costs.py`, CSV audit | confirmed for computer use |
| C011 | Element role profile | New Round 2 local concept: a per-element record containing catalytic role, cost role, expected content-change effect, and evidence strength. | Zhang 2025 plus PubChem/USGS | pending expert certification |
| C012 | Formula-design objective system | New Round 2 local concept: separates primary performance objective, secondary economic objective, and hard composition/experiment constraints. | Zhang 2025 plus local AL code | pending computer expert certification |
| C013 | Virtual-oracle prediction | New Round 2 local concept: GBR/LLM-derived candidate evaluation used for iteration, not a replacement for experimental measurement. | local README/model/pipeline | confirmed as non-experimental |

## 3. Eight-Element Domain Expert Supplement

The table below distinguishes primary-paper statements, data-derived local trends, and hypotheses. Content-effect statements must not be read as causal laws until confirmed by additional experiments or controlled model interpretation.

| Element | Authoritative Identity | Main Role In This Catalyst System | Possible Synergy | Plausible Content-Change Effect On Peak Power Density | Cost Role | Evidence Strength | Certification Status |
|---|---|---|---|---|---|---|---|
| Pd | Palladium, Pd, atomic number 46, PubChem element record | Primary active element for formate oxidation; pure Pd is the benchmark. | Works with Pt as active-element backbone; alloying with Cu/Ce/Nb/Cr can tune local coordination/electronic environment. | Increasing Pd from very low values is likely beneficial because top local samples are Pd-rich and paper uses Pd/Pt active sites. Excess Pd may raise cost and reduce benefit from alloy tuning; optimal region is not pure Pd. | Precious metal; local cost basis normalizes all costs to Pd = 100. | Strong for active role; medium for content trend; causal threshold pending. | pending |
| Pt | Platinum, Pt, atomic number 78, PubChem element record | Primary active element for formate oxidation; investigated by in situ XAS with Pd. | Pd-Pt electronic/coordination interaction may tune activity; EXAFS indicates Pd-Pt coordination peaks. | Moderate Pt appears favorable in high-performing local samples and paper's optimized HEA-1. Increasing Pt likely helps active-site performance up to a composition-dependent optimum, but cost and site-balance tradeoffs apply. | Precious metal; expensive but below Pd in local price table. | Strong for active role; medium for content trend. | pending |
| Cu | Copper, Cu, atomic number 29, PubChem element record | Secondary alloying/cost-reduction element; paper says Cu could alloy with primary elements to tailor coordination and reduce cost. | May alter coordination/electronic structure around Pd/Pt and contribute to high-entropy local environments. | Paper optimized recipes use low Cu (~0.009-0.018). Local 120-row trend has weak negative simple correlation with power density; likely beneficial only at low/tuning levels rather than high fraction. | Low-cost base metal in local price table. | Medium for alloying/cost role; low for monotonic content effect. | pending |
| Au | Gold, Au, atomic number 79, PubChem element record | Minor noble-metal additive; paper notes Au has previous use in direct formate fuel cells. | Could modify surface adsorption/electronic properties with Pd/Pt; exact mechanism not isolated in the paper. | Paper's 9.3x cost-specific recipe includes very low Au (0.004), while HEA-1 omits Au. Increasing Au likely raises cost sharply and should be constrained unless predictive evidence shows performance gain. | Highest local price weight; strong cost penalty. | Medium for prior-use role; low for content effect. | pending |
| Ir | Iridium, Ir, atomic number 77, PubChem element record | Minor noble-metal additive; paper notes Ir has previous use in direct formate fuel cells. | Could assist electronic tuning or durability in alloyed Pd/Pt environments; exact isolated role not proven. | Paper optimized recipes use low Ir (~0.020-0.037). Local 120-row simple correlation is negative; likely a low-level modifier rather than high-fraction target. | Expensive platinum-group metal; strong cost penalty. | Medium for prior-use role; low for monotonic content effect. | pending |
| Ce | Cerium, Ce, atomic number 58, PubChem element record | Secondary alloying/cost-reduction element; paper says Ce could tailor coordination environment and reduce cost. | May perturb local coordination/electronic environment around Pd/Pt; could contribute to single FCC/high-entropy structure. | Paper optimized recipes use moderate Ce (~0.086-0.106). Local top samples also have Ce around 0.10. Increasing Ce from zero may be useful as a modifier, but high Ce fractions have poor local target values and should be bounded. | Low-cost rare earth in local price table; useful cost reducer. | Medium for composition role; medium-low for content trend. | pending |
| Nb | Niobium, Nb, atomic number 41, PubChem element record | Secondary alloying/cost-reduction element; paper optimized cost-specific catalyst contains high Nb (0.338). | May strongly tune coordination environment and reduce precious-metal fraction while maintaining performance. | Moderate-to-high Nb appears compatible with strong performance in paper recipes and local top rows (~0.10-0.20 for top power-density rows, 0.338 for cost-specific recipe). Excess Nb-only or Pd-poor compositions perform poorly locally. | Low cost relative to noble metals; strong cost-reduction lever. | Medium for paper role; medium for content trend; exact optimum pending. | pending |
| Cr | Chromium, Cr, atomic number 24, PubChem element record | Secondary alloying/cost-reduction element; included in cost-specific optimized catalyst at 0.082. | May contribute to alloy complexity and coordination tuning; isolated catalytic role not shown. | Paper's cost-specific recipe contains low Cr, but the local top-10 power-density rows have Cr = 0 on average; use as optional low-level cost/structure modifier until more evidence is available. | Low-cost base metal in local price table. | Medium for inclusion/cost role; low for content effect. | pending |

## 4. Possible Synergistic Mechanisms

| Synergy | Proposed Mechanism | Optimization Implication | Evidence | Confidence |
|---|---|---|---|---|
| Pd-Pt active-site backbone | Pd and Pt are stated as primary active elements; in situ XAS focuses on Pd/Pt and EXAFS shows Pd-Pd/Pd-Pt coordination peaks. | Keep Pd and Pt as core active-site features. Allow optimization to vary both rather than replacing them entirely with low-cost metals. | Primary paper mechanistic section | medium-high |
| Noble-active + low-cost modifier synergy | Cu, Ce, Nb, and Cr may alloy with Pd/Pt, tailoring coordination environments while reducing cost. | Treat Cu/Ce/Nb/Cr as cost/coordination modifiers with bounded ranges and interaction features, not as direct substitutes without performance validation. | Primary paper mechanistic wording | medium |
| Low-level Au/Ir modifier synergy | Au and Ir have prior direct formate fuel-cell use and appear in low amounts in optimized recipes. | Use Au/Ir sparingly; include cost penalties and test whether very low fractions improve performance. | Primary paper composition and mechanism text | medium-low |
| Single FCC solid-solution synergy | Optimized catalyst showed singular FCC phase and robust atomic structure during operation. | Consider single FCC phase as a diagnostic or soft constraint until expert confirms it as hard constraint. | XRD/Rietveld and in situ XAS | medium |
| Poisoning-resistance synergy | HEA model reduces direct and indirect pathway barriers and is reported to resist hydrogen/CO poisoning relative to pure Pd. | Use DFT-derived activation/adsorption descriptors as optional intermediate metrics where available. | Primary paper DFT mechanism | medium |

## 5. Local Data-Derived Element Trends

The following are simple descriptive trends from `oracle_training_sample.csv`. They are useful for computational priors and sanity checks, but they are not independent experimental causal proof because this file is a sampled dataset for training a virtual oracle.

| Quantity | Value / Trend |
|---|---|
| Rows | 120 |
| Columns | `Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr, power_density` |
| Composition sum | Min approximately 1.000000, max approximately 1.000000 |
| `power_density` range | 0.02709 to 75.45 |
| Top observed row | Pd 0.486513, Pt 0.184815, Cu 0.017982, Au 0, Ir 0.036963, Ce 0.105894, Nb 0.167832, Cr 0, power_density 75.45 |
| Top-10 mean composition | Pd 0.484445, Pt 0.190515, Cu 0.0170066, Au 0.0255, Ir 0.0290984, Ce 0.105816, Nb 0.147619, Cr 0 |
| Simple correlation with `power_density` | Pd +0.817, Pt +0.083, Nb +0.073, Cu -0.161, Au -0.231, Cr -0.284, Ce -0.326, Ir -0.387 |

Interpretation for experts:

- Pd-rich compositions dominate the local high-power-density rows, but pure Pd is not the best reported design in the primary paper.
- Pt appears as a moderate active co-component rather than a purely monotonic driver in the sampled local data.
- Ce and Nb appear in meaningful amounts in high-performing local rows, consistent with the paper's coordination/cost-modifier explanation.
- Cu, Au, Ir, and Cr should be treated as low-level modifiers unless new evidence supports broad high-fraction use.
- Correlation values are compositional-data artifacts because all fractions sum to 1; future modeling should use simplex-aware representations such as CLR/ILR/Aitchison geometry or constrained mixture models.

## 6. Computer Expert Data Representation Supplement

### 6.1 Canonical Input Row

Each catalyst formulation row must use this exact element order and numeric format:

```text
Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr
```

Data type: finite floating-point numbers.

Required constraints:

```text
0 <= x_i <= 1 for every element fraction
sum(Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr) = 1
row length = 8
```

Canonical supervised-learning CSV input/output format:

```text
Pd,Pt,Cu,Au,Ir,Ce,Nb,Cr,power_density
0.486513,0.184815,0.017982,0,0.036963,0.105894,0.167832,0,75.45
```

Recommended candidate-generation input object:

```yaml
candidate:
  composition:
    Pd: 0.486513
    Pt: 0.184815
    Cu: 0.017982
    Au: 0.0
    Ir: 0.036963
    Ce: 0.105894
    Nb: 0.167832
    Cr: 0.0
  metadata:
    source: generated|measured|literature|virtual_oracle
    protocol_id: pending
```

Recommended evaluation output object:

```yaml
evaluation:
  predicted_power_density: float
  predicted_power_density_unit: pending_or_W_cm^-2_geo
  normalized_cost: float
  precious_metal_fraction: float
  constraint_status:
    simplex_valid: true|false
    element_bounds_valid: true|false
    cost_valid: true|false
  uncertainty:
    model_std: float|null
    evidence_type: experimental|proxy|virtual_oracle|prediction
```

### 6.2 Do Not Merge These Without Mapping

| Variable | Why It Must Stay Separate |
|---|---|
| Three-electrode potential vs Hg/HgO | Electrode potential is not identical to fuel-cell device voltage. |
| Three-electrode proxy power ranking | Proxy uses assumptions and should be flagged separately from direct fuel-cell peak power density. |
| Experimental `power_density` | Real measurement; can train/evaluate models after protocol harmonization. |
| GBR/LLM predicted `power_density` | Virtual or predicted value; useful for screening but not experimental evidence. |
| Total catalyst loading | Controls geometric performance comparability. |
| Precious-metal loading/fraction | Controls cost/material-efficiency comparison. |

## 7. Optimization Indicators For Iterative Formulation Design

| Indicator ID | Name | Role | Calculation / Data Source | Optimization Direction | Reasonable Round 2 Range / Threshold | Evidence / Caveat | Priority |
|---|---|---|---|---|---|---|---|
| I001 | Peak / maximum power density | Primary objective | Measured from fuel-cell polarization curve or approved three-electrode proxy. Local ML target column is `power_density`. | Maximize | Local virtual-oracle sample range: 0.02709-75.45. Paper figure uses W cm^-2_geo; exact local unit pending. Use current best +5-10% as iterative target, or paper benchmark-relative target if protocol certified. | Primary paper target; local dataset target. | P0 |
| I002 | Cost-specific performance | Secondary objective | `power_density / catalyst_cost_index` or paper-certified cost-normalized metric. | Maximize | Benchmark-relative target: exceed pure Pd; paper reports 9.3x cost-specific performance. Exact formula pending. | Primary paper emphasizes cost-specific performance. | P0 |
| I003 | Normalized catalyst cost | Constraint / secondary minimization | Local code: dot(normalized_ratio, element_price) / price(Pd) * 100. | Minimize or constrain | Local initial/reference values depend on price table. Recommended threshold: no higher than current best-performing candidate unless expert chooses performance-first mode. | Local price table lacks source/date; certify before final use. | P1 |
| I015 | Precious-metal fraction | Constraint / cost proxy | Pd + Pt + Au + Ir fractions. | Minimize subject to performance | Suggested soft range for exploration from local top-10: around 0.65-0.75 total precious-metal fraction; lower values should be explored only if predicted performance remains high. | Derived from composition; not a direct paper threshold. | P1 |
| I016 | PGM-heavy cost fraction | Constraint / diagnostic | Weighted contribution from Pd, Pt, Au, Ir to normalized cost. | Minimize | No fixed threshold; report for every candidate and compare to pure Pd = 100 index. | Uses local cost table and USGS PGM cost context. | P1 |
| I017 | Low-cost modifier fraction | Feature / diagnostic | Cu + Ce + Nb + Cr fractions. | Context-dependent | Local top-10 mean about 0.27; paper optimized cost-specific recipe uses about 0.515 for Cu+Ce+Nb+Cr. | Useful as exploration axis, not direct objective. | P2 |
| I018 | Simplex validity | Hard constraint | Check finite, non-negative, length 8, sum within tolerance of 1. | Must satisfy | Tolerance recommended: abs(sum - 1) <= 1e-6 after normalization; raw user input may be normalized only if all entries non-negative and sum > 0. | Local `normalize_ratio` implements this. | P0 |
| I019 | Element-wise bounds validity | Hard or soft constraint | Check each element against expert-certified synthesis lower/upper bound. | Must satisfy | Round 2 provisional computational bounds: 0 <= each <= 1. Expert must provide synthesis bounds before robotic execution. | Local code lacks real synthesis bounds. | P1 |
| I008 | Activation barrier | Intermediate mechanism | DFT reaction-path barrier for direct/indirect pathways. | Minimize | Paper values: Pd direct 0.706 eV, HEA direct -0.005 eV; Pd indirect 1.318 eV, HEA indirect 0.487 eV. | Costly; not available for every candidate. | P1 |
| I009 | Single FCC phase status | Soft constraint / diagnostic | XRD/Rietveld measurement or phase-prediction model. | Target true if certified | No universal threshold. Candidate should be flagged as unknown until measured/predicted. | Paper optimized catalyst is single FCC. | P1 |
| I011 | Morphology descriptors | Intermediate features | SEM image model: particle distribution slope, bias, coverage ratio, particle count per area. | Context-dependent | Must be standardized by imaging protocol; no threshold extracted. | Paper used these in CRESt latent representation. | P2 |
| I014 | Surrogate predicted power density | Diagnostic / acquisition score input | GBR prediction or LLM committee mean/UCB. | Maximize for screening only | Use with uncertainty; not an experimental value. | Local README explicitly says oracle sample is not new real data. | P2 |
| I020 | UCB acquisition score | Candidate-selection diagnostic | `llm_mean + exploration_weight * llm_std`; local config exploration weight = 1.0. | Maximize | Relative within a candidate batch only. | Local pipeline implementation. | P2 |
| I021 | Final retained score | Batch-retention score | `performance_weight * normalized_power - (1-performance_weight) * normalized_cost`; local config performance weight = 0.6. | Maximize | Relative within queried batch only. | Local pipeline implementation. | P2 |

## 8. Roles Of Power Density, Cost, And Composition Constraints

| Design Aspect | Optimization Role | What It Means For Formulation Design |
|---|---|---|
| Peak / maximum power density | Primary objective | The model/generator should search for compositions expected to increase device-relevant power output. It is the main success metric and should not be replaced by cost unless the project switches to economic optimization. |
| Cost-specific performance | Secondary objective | Used when two candidates have similar power density or when expensive noble metals dominate. It favors formulations that achieve high power with lower material cost. |
| Normalized catalyst cost | Constraint or secondary minimization | Prevents the optimizer from solving the task only by increasing expensive Pd/Pt/Au/Ir. It can be a soft penalty, hard upper bound, or Pareto objective. |
| Composition simplex | Hard constraint | Every generated candidate must be a valid eight-element mixture: fixed order, non-negative finite values, sum 1. |
| Element bounds / synthesis feasibility | Hard constraint after certification | Real robotic synthesis may impose minimum dispense amounts, solubility constraints, precursor compatibility, and max/min fractions. These must be certified before execution. |
| Phase / structure constraints | Soft constraint until certified | Single FCC phase is supported for the optimized catalyst, but should not be a hard filter until experts confirm it is required for performance. |
| Mechanistic descriptors | Intermediate / diagnostic | Activation barriers, metallic Pd/Pt state, poisoning tolerance, and morphology help explain or rank candidates, but are not yet universal targets. |

## 9. Updated Evidence Table

| Evidence ID | Source Type | Source | Use In Round 2 | Quality |
|---|---|---|---|---|
| E001-R2 | paper | Zhang et al. 2025 Nature, DOI 10.1038/s41586-025-09640-5 | Primary catalyst system, target, optimized compositions, mechanism, testing conditions. | high |
| E002-R2 | local data/code | `AL/catalyst_active_learning_runnable/data/README.md`, `data.py`, `costs.py`, `pipeline.py` | Data columns, element order, normalization, virtual-oracle status, outputs, cost calculation. | high |
| E003-R2 | local data audit | `oracle_training_sample.csv`, computed Round 2 audit | Local target range, top-row composition, top-10 composition, simple correlations. | medium; non-causal |
| E004-R2 | ontology/database | PubChem element PUG-View records for atomic numbers 46, 78, 29, 79, 77, 58, 41, 24 | Formal element names/symbols/atomic identities. | high for identity only |
| E005-R2 | government source | USGS mineral information pages for platinum-group metals, copper, and rare earths | Authoritative source category for cost/supply context. | medium; no full eight-element price table extracted |
| E006-R2 | ontology | IUPAC Gold Book and EMMO/ECHO from Round 1 | Catalyst/electrode-reaction/electrochemistry terminology. | high for definitions |

## 10. Remaining Expert Certification Queue

| Object | Question | Required Expert | Priority |
|---|---|---|---|
| Element roles | Are Pd/Pt confirmed as mandatory active backbone for all future candidates, or may low-Pd/low-Pt regions be explored? | domain expert | high |
| Element bounds | What are experimentally feasible min/max and resolution constraints for each of Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr? | synthesis expert | high |
| Cost formula | Should the local price table be used, or replaced with a dated USGS/market/project procurement table? | project owner / cost expert | high |
| Target unit | What is the unit and protocol identity for local `power_density` values? | electrochemistry expert | high |
| Proxy merging | Can three-electrode proxy data and fuel-cell peak power density be trained together? | electrochemistry expert | high |
| Single FCC | Is single FCC phase a hard constraint, soft constraint, or diagnostic? | materials expert | medium |
| Poisoning scalar | Which scalar represents H/CO poisoning tolerance for computation? | computational chemistry expert | medium |
| Au/Ir use | Should Au and Ir be allowed only at low fractions due to cost, or freely explored if predicted performance improves? | domain/cost experts | medium |

## 11. Round 2 Task-Orchestration-Ready Knowledge

Ready after expert sign-off on unit/cost protocol:

```yaml
formulation_input:
  type: normalized_composition_vector
  element_order: [Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr]
  numeric_format: float64
  constraints:
    - all_values_finite
    - all_values_non_negative
    - sum_equals_1
primary_objective:
  indicator: peak_or_maximum_power_density
  direction: maximize
secondary_objective:
  indicator: cost_specific_performance
  direction: maximize
cost_constraint:
  indicator: normalized_catalyst_cost
  direction: minimize_or_upper_bound
initial_data_schema:
  columns: [Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr, power_density]
iteration_outputs:
  candidate_columns: [Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr]
  evaluation_columns: [power_density, normalized_cost, llm_mean, llm_std, ucb_score, final_score]
uncertainty_rules:
  - predicted_values_are_not_experimental_values
  - proxy_power_density_must_be_flagged_separately_from_direct_fuel_cell_power_density
  - composition_correlations_are_not_causal_element_effects
```
