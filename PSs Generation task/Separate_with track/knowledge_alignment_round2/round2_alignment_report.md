# Scientific Knowledge Alignment — Round 2

## 1. Round 2 update

Round 1 correctly identified that photosensitizer performance is conditional and multi-objective. Round 2 adds two missing layers:

1. **Domain layer:** advantageous scaffold families and the structural features that make them useful under particular photochemical, delivery, or biological conditions.
2. **Computer layer:** a strict boundary between DFT-computable molecular quantities, physics-informed proxies, and biological outcomes that require experiments or validated surrogate models.

## 2. Updated domain-expert conclusion

The most useful scaffold families in the evidence are tetrapyrroles (phthalocyanines, porphyrins, chlorins/bacteriochlorin-related designs), donor–acceptor BODIPY/ICT oligomers, AIE photosensitizers, metal/heavy-atom complexes, Type-I radical-generating photodrugs, and targeted/activatable conjugates. Their advantages are complementary:

- tetrapyrroles offer established red/far-red photochemistry and tunable metal/charge/substitution;
- cationic and sterically protected designs can improve aqueous usability and site exposure;
- ICT/AIE architectures can combine excitation, emission, ROS generation, and photothermal functions;
- metal/heavy-atom motifs can alter ISC, redox behavior, and targeting but require relativistic and toxicity-aware treatment;
- Type-I designs are attractive under hypoxia when radical chemistry is demonstrated;
- targeting and activatable groups improve the probability that ROS is generated at the desired biological site.

No family is declared globally best. The scaffold supplement records the relevant structure–property–performance chain and the conditions that could reverse a ranking.

## 3. Updated computer-expert conclusion

An iterative molecular optimization framework can begin with:

1. validity and conformer checks;
2. TD-DFT excitation energy and oscillator strength for light-window compatibility;
3. triplet energy and state character for conditional oxygen/Type-I screening;
4. reaction-specific redox and photoinduced electron-transfer driving force;
5. reorganization energy for electron-transfer kinetics;
6. dispersion-aware dimer/aggregation proxies;
7. SOC or heavy-atom orbital features as family-calibrated secondary descriptors.

The loop must not call DFT-derived values “predicted phototoxicity.” `ΦΔ`, ROS rate, IC50/EC50, dark toxicity, localization, photostability in biological media, and pyroptosis remain experimental or validated-surrogate objectives.

## 4. Reward design decision

Use a validity gate and normalized soft rewards. Thresholds are contextual references, not universal rules:

- conventional PDT excitation context: approximately `600–800 nm`, with `600–850 nm` as a broader review-level context;
- singlet-oxygen energy context: approximately `0.98 eV`, while method-dependent values discussed in the Type-I review extend to approximately `1.75 eV`;
- `ΦΔ`: no DFT threshold; uploaded values `>0.33` and `up to 0.91` remain paper- and assay-specific;
- `εΦ`: approximately `100 M−1 cm−1` and `1,000 M−1 cm−1` are translational review benchmarks for “good” and “excellent” phototherapeutic quantum efficiency, not universal molecular cutoffs;
- redox, reorganization, SOC, and aggregation rewards: reaction- or scaffold-calibrated, with no universal threshold asserted.

## 5. What can enter the next computational task

### Immediately usable with a fixed protocol

`D001` excitation energy, `D002` oscillator strength, `D003` triplet energy, `D006` ET driving force, plus validity/convergence constraints.

### Usable after calibration

`D004` singlet–triplet/state character, `D005` SOC, `D007` reorganization energy, `D008` dimer aggregation energy, and `D009` absorption-weighted capture proxy.

### Not DFT-only objectives

Measured `ΦΔ`, ROS identity/rate, cell potency, dark toxicity, phototherapeutic index, localization, photostability in cells, pyroptosis pathway fraction, cytokines, and immune effects.

## 6. Required next-round data

Before assigning hard reward thresholds, collect matched measurements for wavelength, extinction coefficient, `ΦΔ`, ROS identity, light fluence, oxygen level, cell type, concentration, incubation, aggregation state, and dark/light controls. A model should be trained on molecule–condition records rather than molecule-only records when biological or photophysical outcomes are used.

## Dialogue-based status reconciliation (2026-10-31)

The current output states have been reconciled with the saved expert dialogue at the user's request. General knowledge acceptance, task inputs, selected metric roles, and the synthesizability requirement are recorded only within their supported scope. Existing disputes, unanswered review questions, missing protocols, numerical thresholds, route validation, model-validation gaps, and execution-authorization requirements remain explicit. No scientific values or execution permissions are newly certified, and the historical execution trace is unchanged. The scope and dialogue excerpts are recorded in the expert_feedback_reconciliation metadata of `expert_review_queue_round2.yaml`.
