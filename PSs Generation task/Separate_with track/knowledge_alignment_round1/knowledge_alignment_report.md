# Scientific Knowledge Alignment — Round 1

## 1. Aligned objective

Design candidate photosensitizing molecules with improved performance. “Improved” is not a single scalar in this corpus: it is a conditional, multi-objective property combining photochemical output, usable excitation, target-site exposure, selectivity, dark safety, stability, and (for photopyroptosis) a validated cell-death pathway and immune consequence.

## 2. Evidence map

### Direct structure–photophysics–performance evidence

1. **Water-soluble, non-aggregating Zn phthalocyanine (Makhseed 2013).** Sixteen quaternized imidazolyl peripheral groups combine ionic repulsion with steric bulk. The paper reports water solubility, lack of aggregation, singlet-oxygen quantum yield `ΦΔ > 0.33` in water, anticancer `EC50 = 36.7 nM`, and noncancer-cell dark-toxicity `TC50 = 395 µM`. The exact assay, illumination, oxygen, and comparability of the EC50/TC50 values must remain condition-bound.
2. **Far-red cationic phthalocyanines (Machacek 2015).** Metal identity and peripheral/nonperipheral placement are varied. Reported photophysical range includes `ΦΔ up to 0.91` and `λmax up to 750 nm`; Zn compounds commonly reached submicromolar phototoxic IC50 values with dark `TC50 ≈ 1500 µM`, whereas Mg complexes were inactive (`IC50 > 100 µM`) in the tested systems. The paper attributes the observed phenotype primarily to lysosomal damage followed by broader organelle damage and reports predominantly necrosis-like death.
3. **Mitochondria-targeting Zn(II) N-alkylpyridylporphyrins (Odeh 2014).** The relevant design axis is cationic substituent/alkyl-chain architecture and mitochondrial localization. Exact numerical comparisons require extraction from the article tables and should not be pooled without cell, medium, light, and oxygen metadata.
4. **ICT D–A–D conjugated oligomer (Peng 2021).** CDT donor–BODIPY acceptor architecture gives blue/red dual emission (`463/730 nm`), enhanced intersystem crossing as a reported interpretation of the ICT design, ROS production, and photothermal conversion efficiency `33.1%`. The photodynamic and photothermal outputs were demonstrated against microbes; this is not direct evidence of tumor pyroptosis.
5. **AIE and organelle/site targeting (Wang 2021; Wu 2021; Chen 2021; Rossi 2021).** The papers support design hypotheses that in-cell synthesis, aggregation-induced emission, mitochondrial targeting, membrane anchoring, porphyrin-polymer formulation, and cationic metal-porphyrin architecture can change localization, ROS damage, imaging, and therapeutic selectivity. Exact cross-paper rankings remain invalid unless illumination and assay conditions are harmonized.
6. **CAIX-anchored Re(I) CA-Re (Su 2022).** The paper reports combined type-I and type-II PDT, high efficiency under hypoxia, nanomolar-level phototoxicity, membrane-integrity self-reporting, and GSDMD-mediated pyroptosis with immune activation. The structure-performance claim is conditional on CAIX anchoring and the tested biological system; “high efficiency” must not be converted to an unqualified numeric target.
7. **Photocatalytic NI-TA (Yu 2022).** NI-TA generates superoxide through an intramolecular triplet–ground-state splitting design and partial oxygen recycling. Pyroptosis proceeds through caspase-3/GSDME rather than canonical caspase-1/GSDMD, and activity was reported at hypoxia `≤2% O2` and in T47D 3D spheroids. This supports oxygen tolerance and photocatalytic ROS identity as design variables, not a universal superiority claim.
8. **Photopyroptosis molecular design (Liu 2024; Yi 2024; Lee 2024; Tang 2023; Zhang 2023; Ma 2024).** The papers collectively motivate type-I photochemistry, mitochondria or membrane engagement, controllable ROS localization, and dose-dependent apoptotic/pyroptotic switching. M-TOP is explicitly described as mitochondria-targeting, near-infrared activatable, type-I, less oxygen-dependent, and dose-dependent: higher doses favor caspase-3/GSDME pyroptosis while lower doses favor apoptosis. These are mechanistic hypotheses to validate per candidate, not labels that can be assigned from structure alone.

### Context-only evidence

The Singh, Wang, He, Jia, Li, Loveless, Ma, Mayes-Hopfinger, Ran, Ren, Wu reviews, Xu, Zheng, Johnson, Wang, Ding, Pei, Salami, Mehrotra and related inflammasome/pyroptosis papers define cell-death markers, immune consequences, gasdermin biology, hypoxia or mitochondrial context, and possible assay endpoints. They are valuable for endpoint vocabulary and constraints. They should not be used as direct evidence that a particular photosensitizer structure improves photochemical performance.

## 3. Domain-expert view

| Concept / indicator | Definition in this alignment | Scientific meaning and conditions | Structure–performance relation | Evidence / status |
|---|---|---|---|---|
| Absorption maximum (`λmax`) | Wavelength of maximal measured absorption for the stated sample and solvent/medium | Far-red/NIR excitation can improve tissue-relevant light delivery, but wavelength alone is not efficacy | Extended conjugation and chromophore/metal choice shift absorption; aggregation can alter spectra | Machacek 2015; medium and bandwidth require standardization |
| Extinction coefficient | Absorption strength per concentration and path length under Beer–Lambert conditions | Needed to distinguish spectral position from usable photon capture | Conjugation, metal, substitution, aggregation, and environment affect it | Candidate metric; direct values must be extracted per paper |
| Singlet-oxygen quantum yield (`ΦΔ`) | Fractional yield of singlet oxygen under a stated excitation and reference method | Type-II photochemical output; highly condition-dependent | Zn/Mg/free-base identity, charge, steric shielding, and aggregation affect it | Makhseed 2013 (`>0.33`); Machacek 2015 (`up to 0.91`); do not pool blindly |
| Type-I ROS output | Reduced oxygen/organic radical products generated after photoinduced electron or hydrogen transfer | Important under lower oxygen; species identity must be measured, not inferred | ICT, triplet energetics, donor/acceptor balance, and photocatalytic oxygen recycling are candidate levers | Su 2022, Yu 2022, Yi 2024, Ma 2024; assay harmonization required |
| ROS identity and rate | Measured production of specified ROS, e.g. singlet oxygen or superoxide, with assay conditions | Links photochemistry to local damage and mechanism | Molecular electronics and localization influence which ROS is produced where | Directly useful but assay-specific; do not collapse all ROS into one label |
| Triplet/inter-system-crossing behavior | Excited-state population/transition relevant to ROS generation | Intermediate mechanism connecting structure to PDT output | ICT and triplet-state engineering are reported levers | Peng 2021; numerical comparability unestablished |
| Photothermal conversion efficiency | Fraction of absorbed optical energy converted to heat under a specified protocol | Secondary modality; can complement PDT but may confound mechanism | Low bandgap/ICT architectures can increase nonradiative decay | Peng 2021 (`33.1%`); protocol metadata required |
| Phototoxic potency (`IC50`/`EC50`) | Concentration producing a stated biological response under stated light conditions | Primary efficacy endpoint only within a defined cell/light/time/oxygen assay | Better ROS output, localization, uptake, and target engagement can improve potency | Makhseed 2013, Machacek 2015, Su 2022; condition-bound |
| Dark toxicity (`TC50` or dark IC50) | Concentration producing toxicity without irradiation | Safety constraint, not a universal material constant | Charge, uptake, aggregation, and organelle exposure can alter it | Makhseed 2013, Machacek 2015; require matched protocol |
| Phototherapeutic index | Ratio or paired comparison of dark and light toxicity, only if the paper defines it | Selectivity proxy | Targeting and activation gating should increase it | Candidate derived metric; definition/ratio direction requires expert validation |
| Photostability | Retained chemical/photophysical function after a defined light exposure | Prevents dose drift and off-target degradation | Aggregation, substituents, metal center, and excited-state pathways matter | Candidate constraint; data sparse in corpus |
| Solubility / aggregation state | Dispersion and aggregation behavior in the intended biological medium | Determines delivery, spectral behavior, and ROS accessibility | Ionic peripheral groups plus steric bulk suppress Zn-Pc stacking in Makhseed | Makhseed 2013; medium and concentration must be retained |
| Cellular/organelle localization | Measured distribution at plasma membrane, mitochondria, lysosome, etc. | Converts bulk photochemistry into site-specific damage | Cationic chains, CAIX ligands, mitochondrial motifs, and membrane anchors are levers | Odeh 2014; Wang 2021; Wu 2021; Su 2022; Yi 2024 |
| Pyroptosis fraction / pathway | Validated lytic inflammatory death with pathway markers, e.g. GSDMD or GSDME cleavage/pore formation | Therapeutic phenotype and immune-stimulation endpoint | Membrane anchoring and ROS localization, or caspase-3 modulation, may shift death pathway | Wu 2021; Su 2022; Yu 2022; Yi 2024; pathway must be experimentally confirmed |

## 4. Computer-expert view and metric labels

Scores are provisional Round 1 alignment scores on a 1–5 scale. They express usefulness and readiness for this project, not a claim that the metric is universally optimal.

| Indicator | Role | Direction | Importance | Computability | Data readiness | Acquisition | Priority |
|---|---|---:|---:|---:|---:|---:|---|
| `ΦΔ` under declared conditions | primary_objective | maximize | 5 | 4 | 3 | measure / physics_compute | P0 |
| Type-I ROS yield/rate under declared O2 | primary_objective | maximize | 5 | 3 | 2 | measure / physics_compute | P1 |
| Phototoxic potency under declared light and O2 | primary_objective | maximize (minimize IC50/EC50) | 5 | 4 | 3 | measure / machine_learn | P0 |
| Dark toxicity | constraint | minimize | 5 | 4 | 3 | measure / machine_learn | P0 |
| Phototherapeutic index | secondary_objective | maximize | 5 | 3 | 2 | derive from matched assays | P1 |
| Target-site localization | intermediate | maximize desired-site enrichment; minimize off-target | 5 | 3 | 2 | measure / image analysis | P1 |
| Hypoxia activity | constraint | maximize activity retention at declared O2 | 5 | 3 | 2 | measure / machine_learn | P1 |
| Absorption / excitation compatibility | constraint | target_range | 4 | 5 | 4 | measure / physics_compute | P0 |
| Extinction coefficient | secondary_objective | maximize | 4 | 4 | 2 | measure / physics_compute | P1 |
| Photostability | constraint | maximize retention | 4 | 4 | 2 | measure | P1 |
| Solubility / aggregation resistance | constraint | maximize usable dispersion; minimize aggregation | 5 | 4 | 3 | measure / estimate | P0 |
| Fluorescence quantum yield / imaging signal | secondary_objective | maximize when imaging is required | 3 | 4 | 3 | measure / physics_compute | P2 |
| Photothermal conversion efficiency | secondary_objective | context_dependent | 3 | 4 | 2 | measure | P2 |
| Pyroptosis pathway fraction | secondary_objective | target_range / maximize validated desired pathway | 4 | 2 | 1 | measure / expert_only | P1 |
| GSDMD/GSDME cleavage, pore formation, LDH, IL-1β/IL-18 | diagnostic | context_dependent | 4 | 3 | 2 | measure | P2 |
| General cell-death label without pathway validation | feature_only | none | 2 | 2 | 2 | measure | P3 |

### Optimization targets

```yaml
primary:
  - singlet_oxygen_quantum_yield_under_declared_conditions
  - type_I_ros_output_under_declared_oxygen
  - light_conditioned_phototoxic_potency
secondary:
  - phototherapeutic_index
  - target_site_localization
  - fluorescence_signal_when_required
  - validated_pyroptosis_fraction
constraints:
  - dark_toxicity
  - excitation_compatibility
  - usable_solubility_and_aggregation_resistance
  - hypoxia_activity_when_claimed
  - photostability
intermediate:
  - extinction_coefficient
  - triplet_or_intersystem_crossing_behavior
  - cellular_uptake_and_organelle_localization
diagnostic:
  - ros_identity
  - gsdmd_or_gsdme_cleavage
  - membrane_pore_formation
  - ldh_release
  - il_1beta_and_il_18_release
not_ready:
  - pooled_cross_paper_ic50_without_assay_alignment
  - universal_type_I_vs_type_II_score
  - structure_only_prediction_of_pyroptosis_pathway
```

## 5. Ontology and terminology alignment

| Term | Authority | URL / identifier | Mapping | Use and caveat |
|---|---|---|---|---|
| Reactive oxygen species | ChEBI | `CHEBI:26523`, https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:26523 | exact for ROS entity class | ChEBI defines molecules/ions formed by incomplete one-electron reduction of oxygen; singlet dioxygen and superoxide are represented descendants. Paper assay claims remain separate. |
| Photochemotherapy / PDT | NLM MeSH | `D010778`, https://www.ncbi.nlm.nih.gov/mesh/?term=photodynamic%20therapy | close controlled-vocabulary mapping | MeSH entry covers photosensitizing agents followed by light; it is not a photophysical measurement definition. |
| Singlet oxygen | ChEBI | `CHEBI:26689` via ROS hierarchy | exact chemical entity | Quantum yield is a measurement property and requires a method/standard; it is not defined by the entity record. |
| Pyroptosis | NCI Dictionary / ontology cross-check required | https://www.cancer.gov/publications/dictionaries/cancer-terms/def/pyroptosis | close | The accessible page did not expose a stable definition in this run; retain the papers’ pathway-specific evidence and request validation rather than inventing an ontology mapping. |
| Type-I / Type-II PDT | project concept | no stable exact ontology mapping established in this run | local | Preserve as paper-defined photochemical mechanism labels; require expert validation of operational assay criteria. |
| AIE / aggregation resistance | project concept | no exact ontology mapping established | local | AIE is a photophysical behavior/design label; do not equate it with universal aggregation resistance. |
| Photothermal conversion efficiency | project measurement concept | no exact ontology mapping established | local | Protocol-dependent derived quantity; retain method and uncertainty. |

## 6. Conditions that must be attached to every label

At minimum: molecule or formulation identity; solvent/medium; concentration; aggregation state; oxygen level or hypoxia definition; excitation wavelength; irradiance/power density; exposure time and fluence; cell type or organism; incubation time; assay and reference standard; temperature; biological endpoint; and whether the value is light or dark condition. A metric without these fields is not eligible for pooled optimization.

## 7. Round 1 conclusion

The strongest immediate design hypotheses are: maintain a usable absorption window while increasing ROS output; suppress aggregation in aqueous media; tune Type-I/Type-II balance to oxygen availability; target the damage site; and preserve low dark toxicity. Photopyroptosis adds a pathway-selection objective, but the current evidence supports only condition-specific validation, not a single universal molecular score.

## Dialogue-based status reconciliation (2026-10-31)

The current output states have been reconciled with the saved expert dialogue at the user's request. General knowledge acceptance, task inputs, selected metric roles, and the synthesizability requirement are recorded only within their supported scope. Existing disputes, unanswered review questions, missing protocols, numerical thresholds, route validation, model-validation gaps, and execution-authorization requirements remain explicit. No scientific values or execution permissions are newly certified, and the historical execution trace is unchanged. The scope and dialogue excerpts are recorded in the expert_feedback_reconciliation metadata of `expert_review_queue.yaml`, `knowledge_alignment.yaml`.
