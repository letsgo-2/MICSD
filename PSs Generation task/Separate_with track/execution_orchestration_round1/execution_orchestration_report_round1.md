# Scientific Execution Orchestration — Round 1

## 1. Objective and execution boundary

The task is to generate and optimize photosensitizer candidates whose electronic structure supports condition-specific photochemistry while retaining experimental safety and targeting constraints. The workflow is deliberately multi-objective: no scaffold is declared globally best, and no DFT descriptor is called predicted phototoxicity.

The generator uses canonical/isomeric SMILES and a RECAP-compatible edit vocabulary. Porphyrin is a required seed family because it is explicitly identified by the materials expert as a commonly used scaffold; phthalocyanine, chlorin/bacteriochlorin, BODIPY/ICT, AIE, metal/heavy-atom, Type-I, and targeting/activatable families remain parallel branches. Family labels, metal identity, charge, substituent position, and targeting motif are retained as metadata so that conditional advantages are not pooled incorrectly.

## 2. Ranked metrics and roles

The rank is an execution priority, not a claim that one observable is scientifically more important in every application. It combines direct relevance, evidence, readiness, discrimination, cost, and uncertainty.

| Rank | Metric | Primary execution role | Direction | Threshold guidance | Why this rank |
|---:|---|---|---|---|---|
| 1 | Validity, chemistry, conformer/convergence checks | Hard constraint | pass/fail | Reject invalid SMILES, chemically impossible valence, failed geometry/frequency/convergence, and missing required metadata | Prevents reward hacking and makes every downstream value interpretable; directly computable and cheapest gate. |
| 2 | D001 vertical excitation energy | Soft primary objective | Target range | Start with a soft 600–800 nm band; retain 600–850 nm as a broader context branch. These are design windows, not universal cutoffs. | Directly tied to the selected light source and available with a fixed TD-DFT protocol; Round 2 marks it P0. |
| 3 | D002 oscillator strength | Coupled soft objective | Maximize conditionally | No universal numerical cutoff. Reward the relevant transition only when its state character and wavelength pass the D001 context check. | Supports light capture but avoids rewarding a bright, irrelevant, or charge-transfer-misassigned state. |
| 4 | D003 triplet-state energy and D004 state character | Mechanism branch proxy | Context-dependent | Use a soft compatibility score around the approximately 0.98 eV singlet-oxygen energy context for Type-II branches; retain the method-dependent approximately 0.98–1.75 eV context as evidence, not a hard band. | Mechanistically relevant but sensitive to vertical/adiabatic definitions and method error; requires protocol calibration. |
| 5 | D006 redox potential / photoinduced ET driving force | Type-I branch objective | Reaction-specific target range | No universal cutoff. Define donor/acceptor, solvent, electrode reference, and radical endpoint before scoring; use matched-regime quantiles. | High importance for hypoxia-oriented Type-I design, but the Round 2 queue shows the reaction protocol is unresolved. |
| 6 | D008 dimer aggregation energy | Relative soft constraint | Penalize excessive binding relative to family controls | No universal binding-energy cutoff. Use multiple dimer geometries, solvent, and a scaffold-family control; reject only by an approved relative rule. | Aggregation can invalidate isolated-molecule photophysics; evidence supports anti-aggregation as conditional, not absolute. |
| 7 | D007 reorganization energy | Calibrated Type-I proxy | Usually minimize within a matched regime | No universal cutoff; use a four-point calculation and preserve Marcus-regime context. | Can distinguish ET kinetics but is not monotonically beneficial across all reactions and is not ready for uncalibrated weighting. |
| 8 | D005 spin–orbit coupling | Secondary family-specific proxy | Conditional maximize | No universal cutoff. Use only for calibrated metal/heavy-atom branches and pair with energy gaps/vibronic context. | Potentially useful for ISC, but low readiness and family-transfer risk are explicit Round 2 concerns. |
| 9 | D009 absorption-weighted capture proxy | Calibrated secondary objective | Maximize | Use an explicit spectrum and soft weighted integral; do not equate it with experimental extinction coefficient. | Useful after calibration, but its protocol and measured-extinction mapping are not yet available. |
| 10 | E001 measured singlet-oxygen quantum yield | Experimental objective / validation label | Maximize | Do not transfer `>0.33` or `up to 0.91` across assays. The values are source-specific; use only with wavelength, medium, oxygenation, standard, concentration, and aggregation metadata. | Direct endpoint but not DFT-computable; required for calibration and later active learning. |
| 11 | E002 cellular phototoxicity and dark toxicity | Experimental Pareto objective / safety constraint | Minimize light IC50 and dark toxicity, assay-specific | Do not pool IC50/EC50/TC50 across cell lines or protocols. A phototherapeutic-index objective is deferred until ratio direction and assay normalization are approved. | Closest to application value but most confounded and least ready for molecule-only RL. |
| 12 | Localization, photostability, pyroptosis, cytokines/immune response | Deferred experimental endpoints | Context-dependent | No threshold until validated assays or validated multimodal surrogates exist. Pyroptosis requires pathway evidence, not LDH or morphology alone. | Important outcomes cannot be inferred from DFT and require biology-specific designs and controls. |

### Evidence-backed threshold guidance

* **600–800 nm**, with a broader **600–850 nm** branch, is inherited from the Round 2 report and scaffold supplement as a contextual PDT design window. It should be implemented as a soft distance-to-window score, not a universal rejection rule, because tissue optics, extinction coefficient, quantum yield, oxygen, pharmacokinetics, and photobleaching can reverse a ranking.
* **Approximately 0.98 eV** is the singlet-oxygen energy context used for Type-II compatibility. The Round 2 report also records method-dependent values extending to approximately **1.75 eV**. Use these as mechanism- and method-labeled soft references only; first standardize vertical versus adiabatic triplet definitions.
* Experimental `ΦΔ` values such as **>0.33** and **up to 0.91** are paper- and assay-specific observations, not universal thresholds. The same rule applies to the review-level `εΦ` guidance of approximately **100 M−1 cm−1** (“good”) and **1,000 M−1 cm−1** (“excellent”): these are translational benchmarks requiring matched measurement definitions, not molecular hard cutoffs.
* Redox, reorganization, SOC, and aggregation thresholds remain protocol-specific or relative-to-control because Round 2 leaves partners, solvent, reference electrode, dimer ensembles, and family calibration unresolved.

## 3. Reinforcement-learning execution workflow

### Stage A — Prepare and gate the state

1. Load seed molecules with canonical/isomeric SMILES, scaffold-family label, charge, metal, targeting motif, and provenance.
2. Validate syntax, valence, charge, ring closures, stereochemistry policy, and duplicate identity.
3. Enumerate low-energy conformers with a fixed method; reject failed optimization, frequency, or convergence checks.
4. Apply expert-defined forbidden chemistry and preserve a parent/child edit ledger.

### Stage B — Generate RECAP-constrained proposals

1. Apply RECAP fragmentation to permitted seed molecules.
2. Recombine only compatible fragments and attach permitted substitutions, metal/charge variants, and targeting motifs.
3. Emit canonical/isomeric SMILES, edit operations, scaffold family, and novelty/similarity descriptors.
4. Maintain branch quotas so porphyrin is represented while other families remain available for Pareto comparison.

### Stage C — Calculate and score molecular proxies

1. Run geometry/conformer checks, then TD-DFT excitation and oscillator calculations with a fixed solvent and functional protocol.
2. For candidates entering a mechanism branch, calculate triplet/state character; Type-I branches additionally calculate reaction-defined redox/ET and reorganization quantities.
3. Use calibrated dimer calculations for aggregation and calibrated SOC only for relevant heavy-atom families.
4. Store raw values, units, method versions, uncertainty, applicability-domain flags, and failure reasons.

### Stage D — Reward, select, and update

Use hard validity gates first, then normalized uncertainty-aware soft rewards. Select a Pareto archive rather than collapsing all goals into one scalar. The RL agent may optimize generator/policy parameters only after the executable and parameter interfaces are explicitly authorized; otherwise it proposes changes for expert review.

For candidate `x`, a provisional computational reward is:

`R(x) = gate(x) × [w1*S_window(D001,D002) + w2*S_mechanism(D003,D004) + w3*S_ET(D006,D007) + w4*S_antiagg(D008) + w5*S_capture(D009) − λ*U(x)]`

where inactive branch terms are omitted, `gate(x)` is zero for invalid/failed candidates, and `U(x)` is uncertainty plus out-of-domain penalty. No E001/E002 value enters this formula unless it is measured under harmonized conditions or comes from a separately validated surrogate with uncertainty and applicability-domain reporting.

### Stage E — Experimental bridge and active learning

Select a diverse batch from the Pareto archive, stratified by scaffold family and mechanism branch. Measure matched wavelength, fluence/irradiance, oxygen, medium, concentration, incubation, aggregation, extinction coefficient, `ΦΔ`/ROS identity, light efficacy, dark toxicity, and localization metadata. Add biological endpoints only after a held-out validation protocol demonstrates surrogate performance and calibrated uncertainty. Feed results back as molecule–condition records, not molecule-only labels.

## 4. Model interfaces and authorization

The current project supplies goals and metrics, but does not supply executable generator, DFT, or RL scripts. Therefore all interfaces are `proposed`, not falsely marked available. Adapters and run records must be separate from expert source scripts. The minimum interface contract is documented in `execution_orchestration_round1.yaml`.

## 5. Recommended pilot and stopping rules

Run a small pilot before formal optimization: 20–50 candidates, balanced across at least porphyrin plus two comparison families, with 2–3 RECAP edits per parent and duplicate removal. Verify units, missing-value handling, reward direction, threshold behavior, and failure recovery. Do not use pilot statistics as universal thresholds.

Pause for review when the invalid rate exceeds 20%, any metric has systematic method failure, uncertainty is above the approved limit for a branch, or one family dominates solely because other families have missing evaluations. Stop a round when the Pareto archive has no meaningful improvement for three evaluation batches, the compute budget is exhausted, or safety/assay evidence conflicts with the current reward. Resume only after recording the change and rollback value.

## 6. Main recommendations

1. Keep the search multi-family and Pareto-based; use porphyrin as a required branch, not a universal winner.
2. Rank validity, light-window compatibility, and relevant transition intensity before expensive mechanistic descriptors.
3. Use branch-specific Type-II and Type-I rewards; never combine contradictory mechanism assumptions in one reward without labels.
4. Treat `ΦΔ`, ROS, IC50/EC50, dark toxicity, localization, photostability, pyroptosis, and immune effects as experimental or validated-surrogate endpoints.
5. Resolve the Round 2 expert queue before assigning hard thresholds or enabling automatic RL parameter adjustment.

## Dialogue-based status reconciliation (2026-10-31)

The current output states have been reconciled with the saved expert dialogue at the user's request. General knowledge acceptance, task inputs, selected metric roles, and the synthesizability requirement are recorded only within their supported scope. Existing disputes, unanswered review questions, missing protocols, numerical thresholds, route validation, model-validation gaps, and execution-authorization requirements remain explicit. No scientific values or execution permissions are newly certified, and the historical execution trace is unchanged. The scope and dialogue excerpts are recorded in the expert_feedback_reconciliation metadata of `execution_orchestration_round1.yaml`, `execution_review_queue_round1.yaml`.
