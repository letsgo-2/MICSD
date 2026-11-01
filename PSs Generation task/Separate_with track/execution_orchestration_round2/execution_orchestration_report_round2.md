# Scientific Execution Orchestration — Round 2

## 1. Update scope

This round preserves the Round 1 execution architecture: canonical/isomeric SMILES, RECAP-constrained edits, porphyrin as a required seed branch, parallel scaffold families, uncertainty-aware soft rewards, and a Pareto archive. The change is an updated priority ranking for ten materials-science metrics requested by the materials scientist.

The ranking below is an execution order for a photosensitizer molecular-generation workflow. It weighs direct relevance to photochemical function, evidence and interpretability, computational readiness, candidate discrimination, cost, and confounding. It does not assert that a high-ranked descriptor is always more important than a low-ranked descriptor in every scaffold or assay.

## 2. Updated priority ranking

| Rank | Metric | Proposed role | Direction/use | Threshold guidance | Rationale and limitations |
|---:|---|---|---|---|---|
| 1 | **E(S1)** | Primary computational objective | Target the selected excitation/light window | Convert the selected wavelength window to energy and use a soft band; retain the Round 1 600–800 nm primary context and 600–850 nm broader branch. No universal molecule-independent cutoff. | Directly determines whether the lowest relevant singlet excitation is compatible with the intended light source. It is more actionable than a generic gap, but state assignment, solvent, functional, CT character, and conformer dependence must be recorded. |
| 2 | **E(S1)−E(T1)** | Mechanism/ISC secondary objective | Context-dependent; favor a family-calibrated ISC-compatible regime, not simply “smaller is better” | No universal gap threshold. Use a calibrated soft reward with state character, spin–orbit coupling, and vibronic/energy context. | It connects singlet and triplet energetics to ISC and photosensitization, but the sign and usefulness depend on definitions, competing states, and method error. |
| 3 | **SOCME** (spin–orbit coupling matrix element) | Conditional secondary objective / diagnostic | Conditional maximize within calibrated heavy-atom or chromophore families | No universal SOCME cutoff. Normalize within scaffold family and pair with E(S1)−E(T1), state character, and method uncertainty. | More mechanistically targeted for spin-forbidden transitions than a gap alone, but expensive, relativistic-method dependent, and not transferable across all porphyrin, BODIPY, AIE, and metal families. It must not be treated as a universal ΦΔ predictor. |
| 4 | **charge** | Soft constraint and targeting descriptor | Context-dependent; preserve intended formal/partial charge state | Use discrete formal-charge validity rules and family/application-specific partial-charge distributions; no universal optimum. | Charge affects solubility, membrane interaction, organelle targeting, aggregation, and redox behavior. It is highly useful operationally but can improve one endpoint while harming uptake, dark safety, or aggregation. Protonation and counterion conventions are mandatory metadata. |
| 5 | **logP** | Developability soft constraint | Usually target a measured or predicted application-appropriate interval | Do not impose a universal interval before route, formulation, and biological compartment are fixed. Compare within matched pH/protonation and method. | Hydrophobicity can influence membrane access, protein binding, aggregation, and exposure. It is a conditional delivery descriptor, not a direct photochemical objective; predicted logP is model- and ionization-dependent. |
| 6 | **TPSA** | Developability/transport soft constraint | Target an application-specific interval or Pareto trade-off with logP and charge | No universal threshold; use route- and compartment-specific calibration. | Polar surface area informs hydration and permeability but cannot establish localization or efficacy alone. It is useful for rejecting implausible extremes after ionization state is defined. |
| 7 | **molecular weight (MW)** | Feasibility soft constraint | Penalize excessive size relative to the intended scaffold/formulation | No universal cutoff for this project. Use a family- and formulation-aware range; retain metal and counterion accounting rules. | MW affects synthesis, conformer count, delivery, clearance, and model cost. It is easy to calculate but weakly mechanistic and can unfairly penalize useful targeted conjugates or polymer formulations. |
| 8 | **HOMO–LUMO gap** | Low-weight electronic diagnostic | Use as a contextual feature, not a primary target | No universal gap target. Report orbital convention, functional, solvent, charge, and whether the system has CT character. | It can describe donor–acceptor softness and support redox reasoning, but it is not the same as an optical excitation energy and is vulnerable to functional/self-interaction errors. E(S1) should outrank it for light-window optimization. |
| 9 | **symmetry** | Scaffold diagnostic / diversity control | Preserve or alter conditionally; use discrete symmetry class or a defined numerical descriptor | No universal symmetry optimum. Use an explicit graph/point-group proxy and family baseline; do not infer photophysics from symmetry alone. | Symmetry can influence degeneracy, oscillator strength distribution, packing, aggregation, and synthetic substitution patterns. It is representation-sensitive and may be confounded with size, charge, and substitution. |
| 10 | **SA** (synthetic accessibility) | Soft feasibility constraint / post-generation selector | Minimize difficulty or maximize accessibility score, depending on score convention | No universal cutoff. Calibrate to the project's reaction inventory, expert rules, and scaffold family; document score direction. | SA helps prevent the RL agent from exploiting computationally attractive but impractical structures. It is not a photochemical property, and generic scores can misjudge porphyrins, metal complexes, unusual substituents, and targeted conjugates. |

### Why E(S1) outranks HOMO–LUMO gap

The workflow's first scientific branch is light compatibility. E(S1) is an excited-state quantity that can be mapped to the selected illumination window, whereas the HOMO–LUMO gap is a ground-state orbital diagnostic and is not, in general, an optical gap. The gap remains useful for contextual redox and donor–acceptor analysis, but rewarding it directly could select molecules with an apparently favorable orbital gap and an unsuitable or incorrectly assigned absorption.

### Why SOCME and E(S1)−E(T1) are separated

The energy gap and SOCME describe different ingredients of ISC. A small gap does not guarantee efficient ISC, and a large SOCME does not guarantee useful triplet formation, oxygen sensitization, or low toxicity. They should be combined only in a calibrated, family-aware mechanism branch and should be accompanied by state character and uncertainty.

### Why charge, logP, TPSA, and MW are not hard photochemical gates

These descriptors influence exposure, aggregation, transport, and formulation, but their desirable values depend on protonation, counterions, solvent, protein/membrane environment, organelle target, and route. They should be used as soft constraints or Pareto dimensions until application conditions and matched experimental labels are available.

## 3. Integration into the Round 1 workflow

1. **Validity stage:** calculate formal charge, MW, symmetry representation, and SA metadata after SMILES/RECAP validation. Reject only chemically invalid structures or explicitly forbidden chemistry.
2. **Excited-state stage:** calculate E(S1) using the fixed TD-DFT protocol, then calculate E(S1)−E(T1) and SOCME only when the mechanism branch and method are approved. Preserve conformer and state provenance.
3. **Electronic-context stage:** retain HOMO–LUMO gap as a low-weight diagnostic and never substitute it for E(S1). Record functional, basis, solvent, charge, spin, and CT diagnostics.
4. **Developability stage:** calculate charge-state-aware logP, TPSA, MW, and formulation metadata. Use a Pareto trade-off rather than a single composite target.
5. **Selection stage:** apply the validity gate, calculate normalized soft rewards, penalize uncertainty/out-of-domain predictions, and select a diverse Pareto archive across scaffold families.
6. **Experimental bridge:** measure harmonized spectra, extinction, ΦΔ/ROS, potency, dark toxicity, localization, and stability. Do not infer these outcomes from the ten descriptors alone.

## 4. Updated reward policy

The requested descriptors are eligible at different levels:

* **Active/provisional primary:** E(S1), subject to a declared illumination branch and fixed protocol.
* **Active/provisional secondary:** E(S1)−E(T1), only as a mechanism-labelled soft proxy; charge as a formal validity and soft targeting descriptor.
* **Calibrated secondary:** SOCME, logP, TPSA, MW, and symmetry after method/family/application calibration.
* **Diagnostic or low-weight:** HOMO–LUMO gap and SA. SA can be promoted to a stronger feasibility constraint if the expert approves the reaction inventory and score calibration.

The provisional reward remains:

`R = validity_gate × [w_E(S1)S_E(S1) + w_gapST S_gapST + w_SOCME S_SOCME + w_charge S_charge + w_developability S_dev + w_electronic S_HL − λU]`

Terms are activated only when their protocol and applicability domain are available. `S_dev` is a Pareto or calibrated multi-descriptor component for logP/TPSA/MW, not an assumption that larger or more lipophilic molecules are always better. Biological endpoints remain experiment-only or separately validated-surrogate objectives.

## 5. Required protocol metadata and review items

Before formal RL optimization, define: S1/T1 vertical versus adiabatic convention; TD-DFT functional/basis/solvent; SOCME method and relativistic treatment; charge/protonation/counterion state; conformer ensemble; symmetry descriptor; logP method and pH; TPSA atom-inclusion convention; MW treatment of metals/counterions; and SA score definition/direction. These are recorded in `execution_review_queue_round2.yaml` rather than guessed.

## 6. Recommendations

1. Use E(S1) as the first requested metric in the computational ranking because the intended workflow is light-activated molecular design.
2. Use E(S1)−E(T1) and SOCME as complementary, calibrated ISC descriptors; never optimize either in isolation.
3. Keep HOMO–LUMO gap below E(S1) because it is not an optical excitation energy and can be method-sensitive.
4. Treat charge, logP, TPSA, and MW as condition-dependent delivery/developability dimensions, not universal hard gates.
5. Retain symmetry and SA as diagnostics/feasibility controls; promote them only after the project defines representations, reaction inventory, and calibration data.
6. Preserve the Round 1 evidence boundary: none of these descriptors directly establishes ΦΔ, ROS rate, phototoxicity, dark toxicity, localization, photostability, pyroptosis, or immune response.

## Dialogue-based status reconciliation (2026-10-31)

The current output states have been reconciled with the saved expert dialogue at the user's request. General knowledge acceptance, task inputs, selected metric roles, and the synthesizability requirement are recorded only within their supported scope. Existing disputes, unanswered review questions, missing protocols, numerical thresholds, route validation, model-validation gaps, and execution-authorization requirements remain explicit. No scientific values or execution permissions are newly certified, and the historical execution trace is unchanged. The scope and dialogue excerpts are recorded in the expert_feedback_reconciliation metadata of `execution_review_queue_round2.yaml`.
