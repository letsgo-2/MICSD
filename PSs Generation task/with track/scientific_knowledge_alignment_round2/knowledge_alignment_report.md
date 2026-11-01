# Scientific Knowledge Alignment — Round 2

## 1. Project goal, revision basis, and evidence
Goal: develop candidate molecules with improved photosensitizing performance. Round 2 is a revision of Round 1, which covered all 47 Markdown files under `markdown/`, including supplementary information. The domain expert accepted the baseline and requested scaffold analysis; the computer expert requested genuinely computable DFT metrics, calculation methods, iterative-optimization eligibility, and threshold guidance for rewards.

Primary evidence remains the supplied paper corpus. External reviews and primary sources are used for scaffold and computational-method supplementation, not as substitutes for the supplied experimental evidence. All new claims remain pending expert certification.

## 2. Domain-expert supplement: advantageous scaffold families
No scaffold is universally best. The selection should be conditional on the intended mechanism, irradiation window, oxygen regime, biological localization, aggregation state, and safety constraints.

| scaffold_id | name | advantageous_characteristics | limitations_or_tradeoffs | design_handles | status |
|---|---|---|---|---|---|
| S001 | Porphyrin | Rich substitution and metal-coordination chemistry; established PDT scaffold; visible absorption and ROS generation. | Hydrophobicity, poor aqueous solubility, limited long-wavelength absorption, aggregation and photobleaching can limit biological use. | meso substitution, central metal, axial/targeting groups, formulation. | candidate scaffold; not universally superior |
| S002 | Chlorin / pheophorbide | Partially reduced porphyrin shifts absorption toward the red/therapeutic window while retaining porphyrinoid chemistry. | Some chlorins are unstable or difficult to synthesize/purify; solubility and selectivity remain application-dependent. | ring reduction, peripheral hydrophilization, targeting conjugation, metalation. | candidate scaffold; validate stability and formulation |
| S003 | Bacteriochlorin / bacteriopheophorbide | Longer-wavelength absorption (often reported in the 700–900 nm region) is attractive for deeper light delivery; high extinction can be useful. | Instability/dehydrogenation and synthetic rigidity can complicate development; long-wavelength absorption does not guarantee ROS or safety. | macrocycle stabilization, fluorophore conjugation, targeting and solubilizing groups. | candidate scaffold; photostability must be screened |
| S004 | Phthalocyanine / naphthalocyanine | Strong, sharp red/NIR absorption, high extinction, metal-tunable triplet/ROS behavior; supplied corpus includes Zn phthalocyanine and far-red cationic phthalocyanines. | Planarity drives aqueous aggregation and poor solubility; metal identity and axial functionalization strongly affect ROS, dark toxicity and localization. | central metal, axial ligands, cationic substituents, steric shielding, formulation. | high-value scaffold family; aggregation is a hard design issue |
| S005 | BODIPY / aza-BODIPY | Synthetically modular, high absorption coefficients and generally good photostability; aza-BODIPY enables longer-wavelength absorption; heavy atoms, sulfur fusion, dimers and donor–acceptor design can enhance ISC/ROS. | Unmodified BODIPY often has high fluorescence and low ISC/ROS; hydrophobicity and solubility remain concerns; heavy atoms can increase dark toxicity. | halogen/heavy atom, sulfur/selenium, aza extension, donor–acceptor substitution, cationic targeting, aggregation control. | highly tunable scaffold; optimize ISC against toxicity |
| S006 | Donor–acceptor / ICT / heavy-atom-free organic scaffold | ICT can reduce singlet–triplet gaps and support ISC without heavy atoms; push–pull systems can be designed for Type-I ROS under hypoxia. | Small gaps can improve ISC but may alter T1 energy, fluorescence, charge separation and nonradiative decay; Type-I/Type-II outcome is context-dependent. | donor/acceptor strength, conjugation, torsion, charge pattern, aggregation and microenvironment. | priority branch for hypoxia; requires mechanism-specific validation |
| S007 | Ruthenium / rhenium / other transition-metal complexes | Heavy-atom SOC can facilitate ISC and long-lived triplet states; coordination geometry and ligands provide targeting and activation handles; supplied corpus includes rhenium photosensitizer. | Metal-dependent dark toxicity, stability, ligand exchange, biodistribution and cost; SOC alone does not establish therapeutic index. | metal identity/oxidation state, ligand field, charge, targeting ligand, photolabile or activatable ligand. | candidate scaffold; screen stability and dark toxicity |
| S008 | Aggregation-induced emission (AIE) / AIE photosensitizer | Restricted intramolecular motion can preserve or enhance emission/photochemistry in aggregates; cationic AIE systems can combine membrane/organelle anchoring with ROS generation. | AIE behavior and ROS pathway depend on packing, environment and concentration; aggregation is not automatically beneficial and must be measured. | rotor restriction, donor–acceptor topology, cationic anchors, amphiphilicity, supramolecular assembly. | candidate scaffold; characterize aggregate-state photophysics |


### Scaffold-level design interpretation
1. Porphyrin/chlorin/bacteriochlorin families offer mature photochemical design space. Reduction of the porphyrin macrocycle can shift absorption toward red/NIR, but stability, solubility and aggregation must be treated as co-objectives.
2. Phthalocyanines are especially attractive when strong red/NIR absorption and metal-tunable triplet behavior are needed. Their planar aromatic surfaces make aggregation and aqueous formulation central design constraints; cationic and axial/steric modifications are not interchangeable solutions.
3. BODIPY/aza-BODIPY provides high synthetic modularity. Unmodified BODIPY often favors fluorescence over ISC, so halogenation, chalcogen substitution, donor–acceptor engineering, dimerization or metal coordination may increase ROS but can introduce dark-toxicity or solubility penalties.
4. Donor–acceptor/ICT and heavy-atom-free scaffolds are priority candidates for hypoxia-oriented Type-I design. A smaller singlet–triplet gap is only useful when the state character, SOC, T1 energy and electron-transfer partner are consistent with the chosen branch.
5. Transition-metal complexes provide a strong SOC/ISC design handle and include rhenium/ruthenium examples in the evidence set. The same metal-centered properties can create stability, biodistribution and dark-toxicity risks.
6. AIE and aggregate-state designs may preserve or enhance photochemistry in condensed environments, but aggregation is not intrinsically beneficial. Packing, concentration and biological medium must be measured or modeled explicitly.

## 3. Core concepts and Round 2 additions
| concept_id | name | definition | expert_status |
|---|---|---|---|
| C001 | Photosensitizer | A light-absorbing molecular agent used in the supplied papers to initiate photochemical or photodynamic effects; the exact operational boundary varies by paper. | pending |
| C002 | Photodynamic therapy | A treatment modality combining a photosensitizer, light, and molecular oxygen or other photochemical reactants to produce biologically active species; condition-specific mechanisms must be retained. | pending |
| C003 | Reactive oxygen species | Reactive oxygen-containing chemical species discussed as photochemical effectors; the corpus includes singlet oxygen and other species, but does not justify treating all ROS as interchangeable. | pending |
| C004 | Type-I and Type-II photochemistry | Two mechanistic labels used in the papers for photochemical generation of reactive species; the exact species and oxygen dependence are system- and condition-dependent. | pending |
| C005 | Pyroptosis | A lytic regulated cell-death phenotype associated in the corpus with gasdermin pores and inflammatory signaling; pathway assignment requires assay-specific confirmation. | pending |
| C006 | Structure-property-mechanism-performance relationship | A project-level relation connecting molecular architecture, photophysical/biological properties, proposed mechanism, and measured outcome under stated conditions. | pending |
| C007 | Photosensitizer scaffold | A recurring molecular core or coordination architecture whose substituents, charge, metalation, conjugation and packing provide a design space for tuning absorption, excited-state dynamics, ROS pathway, localization and safety. | pending |
| C008 | DFT/TD-DFT proxy metric | A computed electronic-structure quantity used as a conditional proxy or feasibility filter for an experimental photophysical or mechanistic property; it is not automatically an observable or biological endpoint. | pending |
| C009 | Mechanism branch | A mutually exclusive optimization context, here primarily Type-II singlet-oxygen sensitization versus Type-I electron-transfer ROS generation, with different energy and reward logic. | pending |


## 4. Computer-expert supplement: DFT/TD-DFT metrics
The following metrics are separated into: (a) computable proxies suitable for iterative screening, (b) mechanism-branch gates, and (c) features/diagnostics that must not be turned into standalone rewards. Every computed value must retain method, basis, solvent, charge, multiplicity, conformer/state identity, and uncertainty metadata.

| metric_id | name | meaning | calculation | optimization_use | reward_rule | limitations |
|---|---|---|---|---|---|---|
| D001 | Vertical S0→S1 excitation energy / λabs | Electronic excitation energy and corresponding wavelength; screens spectral compatibility with the selected light window. | Ground-state geometry optimization followed by TD-DFT vertical excitations with oscillator strengths; report functional, basis, solvent model, state, and geometry. Convert λ(nm)=1239.84/E(eV). | direct proxy objective; maximize oscillator strength within a target wavelength band, not wavelength alone. | Provisional Type-II/clinical-window band: 600–800 nm (1.55–2.07 eV); reward 1 inside the project-selected band, linearly decay outside. Use oscillator strength f≥0.01 only as a literature-derived screening heuristic, not a universal cutoff. | TD-DFT errors can be ~0.2–0.4 eV for porphyrinoid bands in reviewed examples; CT states and aggregation can be misrepresented. |
| D002 | Oscillator strength f | Dimensionless transition intensity proxy for light absorption; higher f can support stronger absorption at the selected transition. | Read TD-DFT transition oscillator strength for the target singlet state; retain state identity and dominant orbital transition. | secondary proxy objective or constraint paired with λabs; do not optimize in isolation. | Use a smooth normalized reward relative to the training-set distribution; f≥0.01 is a provisional literature screen only. | State mixing, functional choice, symmetry and environment affect f; it is not extinction coefficient and not phototoxicity. |
| D003 | T1 energy above/below oxygen sensitization threshold | Triplet-state energy relative to the energy required for 3O2→1O2; selects a mechanistic branch. | Optimize or characterize relevant triplet states with spin-unrestricted DFT/TD-DFT; compare consistently computed T1 and oxygen reference energies. Avoid mixing vertical and adiabatic energies. | branch-specific hard gate: Type-II favors T1 above threshold; indirect Type-I deliberately favors T1 below threshold while requiring ET descriptors. | Literature values: 0.98 eV gas-phase ideal threshold and about 1.13 eV solution estimate; use a 0.05–0.10 eV uncertainty margin and never apply both Type-I and Type-II rewards simultaneously. | Threshold varies with method and environment; low T1 alone does not prove Type-I ROS. |
| D004 | ΔE(S1,Tn) / ΔEST | Singlet–triplet energy separation for a candidate ISC channel; smaller gaps can facilitate ISC but are not sufficient without SOC and state character. | Compute relevant singlet and triplet excited states at a consistent geometry and method; identify Tn, not only T1, when an S1→Tn channel is proposed. | intermediate proxy for ISC; pair with SOC and T1 branch gate. | A provisional screening band ΔE(S1,Tn)<0.4 eV is reported in X006 as favorable; use soft reward toward smaller gaps only within a validated scaffold family. | State ordering, vibronic coupling and functional dependence can reverse simple rankings. |
| D005 | Spin–orbit coupling (SOC) | Electronic coupling that enables spin-forbidden singlet–triplet transitions and informs ISC propensity. | Compute SOC matrix elements between relevant singlet/triplet states using a method/program supporting relativistic or perturbative SOC; report units and state pair. | intermediate proxy objective; especially useful for heavy-atom and metal-complex branches. | A literature-specific screening heuristic SOC>0.24 cm−1 is reported in X010; use it only as a soft branch-local gate, not a universal reward threshold. | SOC is state-pair-specific; ISC also depends on energy gap, vibronic coupling, solvent and nonradiative pathways. |
| D006 | HOMO/LUMO energies and gap | Frontier orbital energies and separation that provide qualitative information about redox propensity, electronic structure and CT tuning. | Ground-state DFT orbital energies; for redox work prefer ΔSCF/adiabatic ionization/electron attachment or calibrated electrochemical model rather than raw orbital values. | feature/intermediate; never a standalone primary reward. | No universal threshold. Reward only relative improvement within a scaffold and require redox alignment or ET validation for Type-I designs. | Orbital energies are functional- and charge-state-dependent and are not directly measured ionization potentials/electron affinities. |
| D007 | Electron-transfer driving-force proxy | Relative favorability of electron transfer between excited PS and oxygen/substrate; relevant to Type-I ROS. | Use excited-state redox potentials or ΔSCF energies, plus donor/acceptor electron affinity and ionization estimates; report sign convention and reference. | Type-I branch intermediate or hard feasibility filter. | No universal numeric cutoff; require exergonic or sufficiently favorable ΔG_ET under the defined solvent/partner model, with a margin set from calibration data. | Biological donor/acceptor identity and solvent microenvironment dominate; DFT proxy cannot establish cellular ROS. |
| D008 | Charge-transfer character / electron-hole separation | Spatial separation and donor-to-acceptor character of an excitation; helps distinguish local excitation from ICT/ET states. | Analyze transition-density matrices, natural transition orbitals, attachment/detachment densities, charge-transfer numbers, and electron–hole distance. | diagnostic/intermediate; constrain against pathological long-range CT or dark states. | Use percentile or scaffold-local targets; no universal threshold. Penalize only if the chosen method identifies a dark/weakly absorbing CT state. | Descriptor definitions and partitioning schemes vary; must be coupled to f and excitation energy. |
| D009 | Reorganization energy λ | Structural relaxation cost for charge transfer; lower values can support faster ET in appropriate Marcus-regime models. | Compute neutral/cation/anion geometries and vertical/adiabatic energy differences; define inner-sphere λ and partner/solvent treatment explicitly. | Type-I intermediate; useful for ranking ET kinetics after mechanism specification. | No universal threshold; reward lower λ only when ΔG_ET, coupling, and partner identity are simultaneously defined. | Outer-sphere reorganization, electronic coupling and biological partners are usually missing from molecule-only DFT. |
| D010 | Dipole moment, polarizability, molecular volume and solvation proxy | Descriptors related to polarity, shape, dispersion and possible solubility/partition behavior. | Ground-state DFT dipole/polarizability; molecular volume and implicit-solvent free energy or calibrated logP/logD model. | feature/constraint; useful for diversity, solubility-risk and scaffold-local models. | Use project-specific ranges or percentile normalization; do not impose a universal solubility cutoff without assay context. | They are not substitutes for aggregation, formulation, membrane uptake or dark-toxicity experiments. |


## 5. Metrics genuinely usable in iterative optimization
### Recommended initial computational reward set
- **D001 excitation wavelength plus oscillator strength:** a practical spectral band-pass objective. Use a smooth reward inside the selected 600–800 nm window and require adequate oscillator strength; do not reward red-shifting alone.
- **D003 triplet-energy branch gate:** choose Type-II or indirect Type-I before scoring. Type-II and Type-I have opposite T1 logic; use separate reward heads or separate optimization runs.
- **D004 ΔE(S1,Tn) and D005 SOC:** soft ISC proxies that should be used together and calibrated within scaffold families. Neither is a direct singlet-oxygen yield.
- **D008 charge-transfer character:** diagnostic/intermediate metric to verify that a low gap corresponds to the intended ICT/ET state rather than an optically dark artifact.
- **D006 HOMO/LUMO and D010 polarity/volume/solvation descriptors:** features or soft constraints, not standalone primary rewards.

### Not yet safe as molecule-only rewards
Biological potency, dark toxicity, photostability, organelle localization, aggregation in biological media, hypoxia performance, electron-transfer driving force without a defined partner, and reorganization energy without a defined donor/acceptor/solvent remain experimental or partner-specific. DFT can support them, but cannot replace their validation assays.

## 6. Reward-threshold information
| metric | target | use | status |
|---|---|---|---|
| λabs | 600–800 nm | band-pass screening | literature-informed provisional |
| oscillator strength | f≥0.01 | weak absorption screen | literature heuristic; not universal |
| T1 energy | >~0.98 eV ideal / ~1.13 eV solution estimate for Type-II; <branch threshold for indirect Type-I | mechanism branch gate | method- and environment-dependent |
| ΔE(S1,Tn) | <0.4 eV favorable ISC screen | soft ISC reward | scaffold-local heuristic |
| SOC | >0.24 cm−1 reported screen | soft ISC reward | state-pair and method specific |


Thresholds are screening bands, not universal laws. The 0.98 eV singlet-oxygen energy and approximately 1.13 eV solution estimate must be interpreted with the same electronic-structure method and oxygen reference. A Type-I design may intentionally place T1 below the Type-II oxygen-sensitization threshold, but then requires independent electron-transfer feasibility evidence. The reported f≥0.01, ΔE(S1,Tn)<0.4 eV, and SOC>0.24 cm−1 values are literature-derived heuristics and must be calibrated rather than hard-coded across all scaffolds.

### Reward construction
`R = validity_gate × (w_abs R_abs + w_isc R_isc + w_branch R_branch + w_et R_et) − uncertainty_penalty`.
Use band-pass rewards for λabs, soft normalized rewards for ISC proxies, branch-specific T1 gates, and explicit penalties for failed convergence, ambiguous state assignment, excessive uncertainty, invalid charge/multiplicity, or out-of-domain scaffold chemistry. Keep experimental objectives in a separate evaluation loop.

## 7. Structure–property–mechanism–performance relationships
| claim_id | subject | relation | object | claim_type | confidence | expert_status |
|---|---|---|---|---|---|---|
| K001 | Cationic substitution / charge pattern | promotes | I007 mitochondrial or organelle localization | correlation | medium | pending |
| K002 | Molecular architecture and electronic/photophysical properties | correlates_with | I001 singlet oxygen or ROS output | mechanism | medium | pending |
| K003 | Mitochondrial localization plus local ROS generation | promotes | C005 pyroptotic or other regulated-cell-death phenotype | causal | medium | pending |
| K004 | Type-I photochemistry | is_proxy_for | I008 lower oxygen dependence | hypothesis | low | pending |
| K005 | Aggregation | tradeoff_with | I001 photochemical output and I003 biological potency | mechanism | medium | pending |
| K006 | Phthalocyanine metalation and axial/steric functionalization | promotes | red/NIR absorption, triplet/SOC tuning or aggregation control | mechanism | medium | pending |
| K007 | ICT / heavy-atom-free design | promotes | smaller ISC-relevant singlet–triplet gaps and potentially Type-I ROS | hypothesis | medium | pending |
| K008 | AIE or aggregation control | correlates_with | preserved aggregate-state photophysics and local ROS generation | correlation | low | pending |


## 8. Evidence, conflicts, and boundaries
The most important conflict is intentional: Type-II and Type-I designs use different triplet-energy logic. A high ΦΔ target is not appropriate for every hypoxia-oriented Type-I design, and a favorable DFT descriptor does not guarantee cellular potency. Literature threshold values vary with method, solvent and state definition; they are retained as conditional screening guidance.

## 9. Expert certification state
Round 2 adds the requested material and computational perspectives but does not mark them approved. Materials/photochemistry experts must validate scaffold advantages and branch definitions; computational experts must validate the calculation protocol, state tracking and reward calibration; experimental experts must connect proxy metrics to matched assays; computer experts must approve the iterative metric subset.

## 10. Pending validation checklist
See `expert_review_queue.yaml`. High-priority questions include scaffold-specific threshold calibration, Type-I versus Type-II branch selection, method/basis/solvent protocol, state tracking, SOC and ΔEST reproducibility, molecular structure normalization, and the relationship between DFT proxies and biological endpoints.

## 11. Metrics eligible for the next computational task stage
Provisionally eligible for computational screening after protocol approval: D001, D003, D004, D005, D006 and D008. D007 and D009 require defined electron-transfer partners and calibration. No biological metric is promoted to a molecule-only DFT reward. Expert approval remains required before task orchestration.

## Appendix A. External authoritative/review sources
| source_id | name | url | use |
|---|---|---|---|
| X001 | Application of TD-DFT Theory to Studying Porphyrinoid-Based Photosensitizers for PDT | https://doi.org/10.3390/molecules26237176 | TD-DFT spectra, S0-T1 energy, SOC/ISC, solvent effects, method limitations |
| X002 | Recent progress in photosensitizers for overcoming the challenges of PDT | https://doi.org/10.1039/D0CS00173B | scaffold design and application-level limitations |
| X003 | Dye Sensitizers for Photodynamic Therapy | https://pmc.ncbi.nlm.nih.gov/articles/PMC5512801/ | porphyrinoid scaffold classes, absorption ranges, clinical context |
| X004 | The unique features and promises of phthalocyanines as advanced photosensitisers | https://doi.org/10.1039/C9CS00129H | phthalocyanine photophysics, metal coordination, aggregation and solubility |
| X005 | Photodynamic Therapy: From the Basics to the Current Progress of N-Heterocyclic-Bearing Dyes | https://doi.org/10.3390/molecules28135092 | porphyrin, chlorin, bacteriochlorin, phthalocyanine and BODIPY scaffold characteristics |
| X006 | The Current Advances in Design Strategy for Type-I Photosensitizers | https://doi.org/10.1002/advs.202413365 | Type-I branch, T1 threshold logic, ICT, SOC and ΔES-T screening |
| X007 | Photodynamic Efficiency: From Molecular Photochemistry to Cell Death | https://pmc.ncbi.nlm.nih.gov/articles/PMC4613217/ | photochemical pathway and distinction between photophysics and cell death |
| X008 | An Emerging Molecular Design Approach to Heavy-Atom-Free Photosensitizers for Enhanced PDT under Hypoxia | https://doi.org/10.1021/jacs.9b09220 | heavy-atom-free Type-I design, ΔEST/SOC and hypoxia evidence |
| X009 | Transition metal complexes as photosensitisers in one- and two-photon PDT | https://eprints.whiterose.ac.uk/id/eprint/130249/1/PDT-Review-pdf.pdf | transition-metal SOC/ISC advantages and toxicity tradeoffs |


## Appendix B. Round 1 continuity
Round 1 source inventory retained: 47 Markdown files. Round 1 evidence excerpts retained: 1016. Round 2 adds scaffold and computational-method supplements without deleting prior evidence or unresolved questions.