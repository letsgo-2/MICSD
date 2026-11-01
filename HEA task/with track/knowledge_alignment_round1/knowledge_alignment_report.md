# Scientific Knowledge Alignment: Round 1

## 1. Project Goal and Evidence

**Goal.** Optimize the elemental composition of an eight-component high-entropy-alloy (HEA) catalyst to increase the peak power density of an electrochemical device.

**Scope.** This is a first-round knowledge alignment, not algorithm selection. The user-supplied evidence set is every Markdown document in `literature_markdown/` (43 files, inventoried in `knowledge_alignment.yaml`). Evidence is tiered by relevance: (A) directly relevant HEA electrocatalysis and composition–activity studies; (B) electrochemical catalyst/device methodology and non-HEA comparisons; (C) alloy fundamentals and non-electrochemical HEA studies; (D) optimization, data, and computational-method papers. All are included, but only A/B support direct experimental statements about electrocatalytic activity. Figure assets accompany some Markdown papers and remain referenced in their papers.

The supplied set does not establish the project's target device, reaction, electrode role, permissible fraction ranges, support/morphology, or device operating protocol. One supplied 2025 study does report an octonary Pd–Pt–Cu–Au–Ir–Ce–Nb–Cr catalyst for formate oxidation and direct formate-fuel-cell power density; it is adjacent evidence, not evidence for the unspecified target chemistry/device. A 2023 review also cites direct-ethanol-fuel-cell power-density results, which require primary-source verification. No candidate or predicted improvement for this project is asserted. General acceptance inferred from the later dialogue is recorded separately from itemwise evidence verification.

## 2. Core Concept System

| Concept | Working definition and scope | Mapping/source | Status |
|---|---|---|---|
| High-entropy alloy (HEA) | A compositionally complex alloy class; the literature uses at least five principal elements and/or ideal configurational entropy thresholds, but definitions vary and do not require single-phase structure. | Yeh et al. composition definition (5+ principal elements, commonly 5–35 at.%); Miracle & Senkov review; map as `close`, not a universal standard. | Pending domain expert |
| Eight-component alloy | Project-specific requirement that the designed catalyst contains exactly eight designated components. It does not by itself fix equal fractions or phase structure. | User objective; local concept. | Pending domain expert |
| Composition vector | Fractions of the eight elements, constrained to sum to one (or 100 at.%); component identity and fraction are separate design variables. | Aitchison (1982), Egozcue et al. (2018); local application to catalyst. | Pending data/experiment experts |
| Electrocatalyst | A catalyst that changes the rate of an electrode reaction; the reaction, potential scale, electrolyte, and electrode configuration define the use context. | IUPAC electrochemical nomenclature and supplied electrocatalysis papers. | Pending |
| Current density | Current divided by declared area; geometric/projected and electrochemically active areas are not interchangeable. | IUPAC Gold Book M03776; exact area convention must be stated. | Definition aligned; protocol pending |
| Overpotential | Deviation of electrode potential from its equilibrium value required to cause a stated current to flow. | IUPAC Gold Book O04358; measurement still requires reaction, current, reference, and correction conditions. | Definition aligned; protocol pending |
| Device peak power density | Maximum of areal power over a specified device polarization curve; for a galvanic cell, areal power is cell voltage times current divided by the declared active area. It is a system/device response, not an intrinsic catalyst-only property. | IUPAC electrochemical engineering nomenclature and FCTESQA PEFC single-cell polarization test module; scope must match target device. | Pending device expert |
| Ordering / phase / surface state | Chemical order, phase constitution, surface segregation and morphology affect which sites are exposed; composition alone is insufficient to identify the active surface. | Wang et al. (2023); HEA reviews. | Mechanism/context-dependent |

**Important distinction.** IUPAC defines mean current density with an explicitly declared area basis. The IUPAC electrochemical engineering nomenclature’s *power density* is volumetric (W m⁻³), whereas fuel-cell studies commonly report areal power (e.g., W cm⁻²). The project must name the metric as *areal peak power density* and specify denominator area to avoid conflating these quantities.

## 3. Core Indicator System

Rating scales follow the Skill: importance, computability, and data readiness are 1–5. Ratings are provisional triage, not expert-certified facts. P0 requires a well-defined, condition-bound objective/constraint and sufficient computability; consequently no metric is P0 at this stage.

| ID / Metric | Definition, unit, and required conditions | Role / direction | Importance / computability / readiness | Priority; acquisition; evidence status |
|---|---|---|---|---|
| I01 Areal peak device power density | `max(V_cell × I / A_declared)` across a device polarization curve; W cm⁻² or W m⁻². Requires device architecture, active-area convention, reactants/feeds, temperature, pressure, humidity/electrolyte, conditioning, and sweep protocol. | Primary objective; maximize. | 5 / 4 / 1 | P1; measure from device curve; device-protocol data missing. |
| I02 Device polarization curve | Paired cell voltage and current density across operating points; V vs A cm⁻². | Intermediate; maximize the achievable curve envelope, not each point independently. | 5 / 4 / 1 | P1; measure; target device conditions unresolved. |
| I03 Electrode reaction activity | Reaction-specific current/activity at a stated potential and protocol; A cm⁻², A mg⁻¹, or normalized current. These normalizations are not interchangeable. | Intermediate; context-dependent (higher activity may support device performance). | 5 / 4 / 3 | P1; electrochemical measurement; literature is reaction- and setup-specific. |
| I04 Overpotential at specified current | Potential beyond equilibrium potential for a stated reaction/current density; V or mV, with reference electrode and iR correction declared. | Secondary objective / intermediate; minimize at fixed current. | 4 / 4 / 3 | P1; measure/derive; not equivalent to full-device power. |
| I05 Mass activity | Reaction current per catalyst mass, e.g. A mg_PGM⁻¹ or A mg_cat⁻¹; loading and normalization must be explicit. | Secondary objective; maximize at fixed conditions if resource efficiency is desired. | 4 / 4 / 3 | P2; measure/derive; incompatible denominators across papers. |
| I06 Specific activity / ECSA-normalized activity | Current per electrochemically active surface area; A cm_ECSA⁻². ECSA method must be stated. | Diagnostic/intermediate; maximize only under a defined reaction/protocol. | 3 / 3 / 2 | P2; measure/derive; methods and accessibility vary. |
| I07 Durability / activity retention | Change in activity, potential, or power after a defined time/cycling protocol; unit is protocol-dependent (% retention, mV shift, or time). | Constraint / secondary objective; maximize retention or minimize degradation. | 4 / 3 / 2 | P1; measure; no common lifetime definition across supplied papers. |
| I08 Selectivity / Faradaic efficiency | Fraction of charge/product associated with the desired reaction/product; dimensionless or %. | Constraint/intermediate; target required range or maximize desired product selectivity. | 3 / 3 / 2 | P2; measure; target reaction not specified. |
| I09 Elemental atomic fractions | `x_i` for i=1..8, `x_i >= 0`, sum `x_i=1`; at.%. | Hard constraint / design variables; no individual direction. | 5 / 5 / 2 | P1; synthesis + compositional analysis; element set/bounds missing. |
| I10 Element count | Number of designated alloy components, fixed at 8 by user. | Hard constraint; target exactly 8. | 5 / 5 / 4 | P1; composition specification and assay; user-specified. |
| I11 Phase/chemical ordering | Phase labels, phase fractions, lattice/order descriptors; categorical or fractional, measured/derived by suitable characterization. | Intermediate/diagnostic; context-dependent, no universal direction. | 4 / 3 / 2 | P2; characterization/physics computation; composition alone is insufficient. |
| I12 Particle size, morphology, and accessible surface | Size distribution, shape, support dispersion, and accessible surface area; methods/units vary. | Constraint/intermediate/diagnostic; target range is expert-defined. | 4 / 3 / 2 | P2; microscopy/surface characterization; confounder to composition. |
| I13 Composition descriptors (e.g. ideal configurational entropy) | `S_conf/R = -sum(x_i ln x_i)` under ideal random mixing; dimensionless after dividing by R. Does not establish realized phase or catalytic benefit. | Feature-only/diagnostic; none by default. | 2 / 5 / 3 | P2; derive from composition; definition computable, interpretation uncertain. |
| I14 Adsorption/intermediate binding energies | Energies of reaction intermediates on specified surface sites; eV and computational model conditions. | Intermediate/diagnostic; context-dependent, often a mechanistic proxy. | 3 / 2 / 2 | P2; physics computation/estimate; disordered HEA site distributions complicate transfer. |
| I15 Tafel slope | Slope from specified overpotential vs log current relation; mV dec⁻¹ with fitted region and protocol. | Diagnostic; no direct objective direction without kinetic context. | 2 / 3 / 2 | P2; derive from polarization data; protocol-specific. |

### Optimization-target routing

- **Primary:** I01 areal peak device power density (blocked pending device and test definition).
- **Secondary:** I03 reaction activity; I04 overpotential; I05 mass activity; I07 durability (exact utility/constraints need expert agreement).
- **Constraints:** I10 exactly eight components; I09 fractions sum to 1 and obey yet-to-be-specified element bounds; I07 durability floor and I08 selectivity requirement only after experts define acceptance criteria.
- **Intermediate:** I02 polarization curve; I03/I04 reaction performance; I11 phase/order; I12 morphology/accessibility.
- **Diagnostic:** I06, I13, I14, I15 and characterization data.
- **Not ready for direct optimization:** I01 (no target device protocol/data), I07/I08 as hard bounds (no acceptance criteria), and I11/I12/I14 where methods and input data are absent. These may still be measured as context.

## 4. Domain-Expert View

The most directly transferable evidence is that HEA electrocatalytic performance depends on more than nominal bulk composition. Supplied literature discusses composition-dependent site ensembles, ligand/strain/ensemble effects, phase constitution, chemical ordering, surface state, and reaction-specific conditions. Wang et al. (2023) explicitly compares ordered and disordered Pt₄FeCoCuNi for HER/ORR, reporting ordering-dependent behavior and ORR/HER characterization; it is a five-component composition and cannot establish an eight-component optimum. Banko et al. (2021) and Pan et al. (2024) demonstrate high-throughput composition exploration for electrocatalyst screening, with reaction/electrode-level responses, not proof of device-level power-density transfer. Clausen et al. (2023) and related computational papers model adsorption-site distributions and catalytic activity; those outputs are mechanistic proxies, not measured device outcomes.

Other supplied papers cover HEA definitions and phase behavior, compositional data statistics, electrocatalysis reviews, ORR/HER/OER or other reaction systems, materials synthesis, and optimization methodologies. They provide context but must not be pooled as directly comparable performance observations. CRESt is an important adjacent exception because it demonstrates an octonary composition search tied to device power in a direct formate fuel cell; target-device and reaction equivalence remain unknown. Source-level records and tiering appear in the machine-readable file.

**Structure–property–mechanism–performance map (claims remain provisional):**

1. Element fractions and element identity → local atomic neighborhoods / site ensembles and electronic/strain environments → adsorbate binding and reaction kinetics → electrode polarization behavior → device polarization curve and peak areal power.
2. Composition + synthesis/thermal history → phase and ordering / segregation / morphology → exposed active sites and stability → reaction activity/selectivity and degradation.
3. Device architecture, catalyst layer, loading, support, transport, membrane/electrolyte, feeds, temperature, pressure, humidity, and conditioning → device polarization and peak power independently of (and interacting with) catalyst composition.

The first two links are supported qualitatively by the electrocatalysis papers but are condition-specific and not a universal causal law. The last link is required by device-level measurement practice. Zhang et al. (2025) provides a directly relevant precedent for octonary composition-to-device-power experiments in a direct formate fuel cell, but no supplied evidence establishes that its recipe or a given direction in activity, overpotential, adsorption energy, or entropy monotonically increases peak power in the project's target device.

## 5. Computer-Expert View

Treat the **composition** as an eight-part simplex-valued design, subject to fixed component identities and experimentally feasible bounds. Do not treat eight fractions as independent unconstrained real-valued variables; preserve closure and distinguish true zeros/absence from small positive fractions. Compositional-data papers (Aitchison 1982; Egozcue et al. 2018) establish that naive Euclidean treatment can be inappropriate, but transformation choice is deliberately deferred to a later stage.

The natural observation unit should be an **experiment/device record**, not just a composition: composition + synthesis batch/history + catalyst-layer formulation + electrode/device configuration + protocol/conditions + measured response + uncertainty. Replicates and batch/device identifiers are needed to distinguish composition effects from synthesis and measurement variability. Maintain separate records for half-cell metrics and full-device metrics; they are not interchangeable labels.

No optimization algorithm is selected in this alignment stage. Current readiness for the requested target is low because the corpus has abundant reaction-specific catalyst metrics but no validated, uniform mapping to peak power density for the target device. Candidate features (phase/order, morphology, descriptors, computed binding energies) should be retained with evidence and method provenance rather than prematurely promoted to objectives.

## 6. Structure–Performance Claims and Evidence

| Claim | Type / conditions | Evidence and qualification |
|---|---|---|
| Element composition and local element combinations relate to electrocatalytic activity. | Association/mechanistic interpretation; reaction-, surface-, synthesis-, and electrolyte-dependent. | Banko 2021; Pan 2024; HEA electrocatalysis reviews. No direct universal composition → device-power law. |
| Ordering state can alter HER/ORR behavior in Pt₄FeCoCuNi. | Paper-specific experimental relationship; five-component material and reported test conditions only. | Wang 2023, Results/Figures 5–6 and supporting information references; not transferable quantitatively to eight components without validation. |
| HEA active sites span a distribution; site-specific adsorption energies can be used to reason about expected activity. | Modeling framework/mechanistic proxy; selected surface/site and computational assumptions. | Clausen 2023. Does not make adsorption energy equal to activity or device power. |
| Compositional gradients/source permutations affect sampled-space coverage and attribution. | Experimental design/method claim. | Banko 2021. Supports coverage awareness, not a performance optimum. |
| An octonary composition search can be experimentally linked to full-device power in a direct formate fuel cell. | Paper-specific experimental result; not a universal alloy rule. | Zhang et al. (2025), abstract/Fig. 1 and direct formate fuel-cell result. Exact power values and protocol must be transcribed from the full source/supplements before quantitative reuse. |
| Device power response can be measured on a full electrochemical device and reported against a declared area basis. | Measurement definition/protocol, not a catalyst mechanism. | IUPAC electrochemical engineering nomenclature; FCTESQA PEFC single-cell procedure; adjacent direct formate fuel-cell evidence in Zhang et al. (2025). Target device may not be PEFC or formate fuel cell. |

## 7. Evidence and Conflicts

The HEA term has multiple definitions (element-count/concentration and ideal entropy-based). A fixed eight-element count satisfies a common minimum-element criterion but does not decide concentration bounds, phase count, or whether a strongly non-equiatomic candidate is called an HEA. Preserve both definition families and ask the alloy expert which naming rule governs this project.

Current density and power density depend on normalization basis. Literature activity may be geometric-area normalized, ECSA-normalized, or mass-normalized; these values cannot be merged without metadata. IUPAC electrochemical engineering nomenclature uses volumetric power density, while device papers often report areal power density (for example, Zhang et al. labels maximum power density in mW cm⁻²_geo). I01 explicitly uses areal density, subject to confirmation. Zhang et al.'s octonary alloy and device are a strong adjacent precedent, but not a transferable target or benchmark until reaction and architecture are confirmed.

No evidence conflict is resolved by averaging. Reaction, electrolyte/pH, reference scale, loading, substrate/support, iR correction, scan/rotation conditions, temperature, and durability protocol are stored as condition fields whenever available in source papers; cross-paper comparability remains unverified.

## 8. Importance, Readiness, Priority

Only I01 is the stated primary objective. It is high importance but P1 because direct target-device data and test conditions are absent. P0 is intentionally empty. I09–I10 are design constraints, not performance outcomes; exact element set and bounds need approval. Electrode metrics are P1/P2 proxies and auxiliary criteria only after experts decide their link to the device response. P3 remains reserved for undefined, weakly evidenced concepts and no such uncertain item is silently promoted as a fact.

## 9. Expert-Certification Status

The later Round 2 dialogue generally endorses the existing knowledge, now reflected as acceptance in principle. Atomic-fraction task semantics and individual scientific or numerical validation remain unresolved. See `expert_review_queue.yaml` for the required decisions and accountable disciplines.

## 10. Missing Evidence and Decisions

The queue requests resolution of: electrochemical device and reaction; whether power is full-cell or stack and whether areal or volumetric; electrode role; exact eight elements and composition bounds; measurement area convention; device/catalyst-layer architecture; standard conditions and conditioning; reproducibility/uncertainty; minimum durability/selectivity acceptance; and whether proxy objectives are permitted. Also requested is targeted extraction/verification of quantitative values and conditions from source figures/tables/supplements before constructing comparable training data.

## 11. Indicators Eligible for Task Orchestration

**None yet.** I01 is the eventual primary endpoint but fails the required target-condition and expert-certification gates, despite the adjacent octonary formate-fuel-cell precedent. I09/I10 are clear in broad form but element identity/bounds and analytical assay are pending. Half-cell activity/overpotential may be tracked as supporting measurements only; they are not substitutes for I01. Reassess after expert responses and a target-device protocol are recorded.

## Sources for Terminology (accessed 2026-10-27)

- IUPAC Gold Book, “mean current density” (M03776): https://doi.org/10.1351/goldbook.M03776
- IUPAC Gold Book, “overpotential” (O04358): https://doi.org/10.1351/goldbook.O04358
- IUPAC Gold Book, “electrocatalysis” (09094) and “catalyst” (C00876): https://doi.org/10.1351/goldbook.09094 ; https://doi.org/10.1351/goldbook.C00876
- Gritzner & Kreysa, “Nomenclature, symbols and definitions in electrochemical engineering,” Pure Appl. Chem. 65 (1993): https://doi.org/10.1351/pac199365051009
- FCTESQA, Test Module PEFC SC 5-2, *Testing the voltage and power as function of the current density: Polarisation curve for a PEFC single cell* (2010): https://joint-research-centre.ec.europa.eu/system/files/2017-02/polarisation_curve_testprocedure.pdf (harmonized procedure, not claimed as a formal standard)
- Yeh et al., “High-Entropy Alloys: A Critical Review,” JOM 67 (2015): https://doi.org/10.1007/s11837-015-1583-8 (published online 2014; use the cited version in final bibliography)
- Miracle & Senkov, “A critical review of high entropy alloys and related concepts,” Acta Materialia 122 (2017): https://doi.org/10.1016/j.actamat.2016.08.081
- Aitchison, “The Statistical Analysis of Compositional Data,” JRSS B 44 (1982): https://doi.org/10.1111/j.2517-6161.1982.tb01195.x
- Egozcue et al., “Compositional data analysis in the geosciences: Modelling the unknown,” (2018), as supplied in corpus; confirm exact bibliographic metadata before citation reuse.

Ontology mapping is used for term normalization, not as evidence that a catalyst mechanism is true. No stable domain ontology identifier for project-specific “eight-component HEA catalyst” or “areal peak device power density” is asserted; those remain local/project-scoped concepts.


## Dialogue Based Status Update 2026-10-30

Applicable pending fields have been updated directly using the supplied multi_round_dialogue_example_EN.txt. These are retrospective inferences: general knowledge is accepted in principle, named objectives/constraints are accepted for task use, and requested analyses or ratio adjustment are accepted as requirements. This does not certify numerical values, thresholds, prices, causal mechanisms, detailed recipes or model execution. Mass-fraction versus atomic-fraction conflicts remain unresolved. See the accompanying YAML dialogue_status_reconciliation for the source lines and exact dialogue. No original-file backup was created, as requested.
