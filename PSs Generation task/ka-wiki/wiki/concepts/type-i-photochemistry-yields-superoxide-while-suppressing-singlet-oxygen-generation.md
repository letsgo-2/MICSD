---
title: Type-I photochemistry yields superoxide while suppressing singlet oxygen generation
summary: Photoexcited NI-TA preferentially undergoes electron transfer to oxygen to make O2−•, with little detectable 1O2 or OH•.
sources:
  - photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md
kind: concept
createdAt: "2026-07-17T09:50:59.178Z"
updatedAt: "2026-07-17T09:50:59.178Z"
tags:
  - type-I-photochemistry
  - ROS
  - photodynamic-therapy
aliases:
  - type-i-photochemistry-yields-superoxide-while-suppressing-singlet-oxygen-generation
  - TPYSWSSOG
confidence: 0.98
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# Type-I photochemistry yields superoxide while suppressing singlet oxygen generation

This study describes a photosensitizer design strategy intended to favor [[Type-I photochemistry]] over [[Type-II photochemistry]]. The authors argue that if electron transfer from an excited triplet photosensitizer to ground-state oxygen is faster than the competing energy-transfer pathway, the system can efficiently produce superoxide radical (`O2−•`) while limiting formation of [[singlet oxygen]] (`1O2`). ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:171-185]

Using the compound `NI-TA` as their example, the authors attribute this behavior to modulation of the triplet-ground-state energy gap. `NI-TA` was designed with a donor-bridge-acceptor architecture and calculated to have a low `T1` energy, with `ΔET1−S0 = 1.115 eV`, which is below the `3O2/1O2` energy gap of `1.610 eV`. The paper states that this makes the energy-transfer route needed to generate singlet oxygen thermodynamically unfavorable while still permitting Type-I electron transfer to oxygen and thus superoxide formation. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:179-195, photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:420-450]

The experimental data support selective superoxide generation by `NI-TA` under photoirradiation. In aqueous solution, `NI-TA` produced a strong response with the superoxide probe `DHR123`, and electron paramagnetic resonance detected `DMPO-O2−•` adducts. In contrast, assays for singlet oxygen and hydroxyl radicals showed little change: `ABDA` absorption and `HPF` fluorescence were barely perturbed, and EPR did not detect `TEMP-1O2` or `DMPO-OH•` adducts. The authors interpret these results as evidence that `NI-TA` generates little, if any, singlet oxygen or hydroxyl radical under the tested irradiation conditions. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:269-305, photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:334-360]

Cell-based imaging gave the same qualitative pattern. In `T47D` cells, photoirradiated `NI-TA` produced a superoxide-associated `DHE` signal, whereas experiments using the singlet oxygen probe `SOSG` showed no evidence of intracellular singlet oxygen generation under normoxic conditions. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:361-377]

The paper connects this selectivity to two photophysical requirements: efficient intersystem crossing to populate the triplet state, and a triplet-state energy too low to support Type-II sensitization of oxygen. `NI-TA` was calculated to have a smaller `ΔES1−T1` than the control compounds, which the authors cite as favorable for intersystem crossing, and a `ΔET1−S0` below the threshold needed to convert triplet oxygen into singlet oxygen. On that basis, the study concludes that photoexcited `NI-TA` undergoes a Type-I process that yields superoxide while suppressing singlet-oxygen generation. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:378-450]

The authors further tested the generality of this design logic with related donor-bridge-acceptor compounds, `NI-TPA` and `NI-DA`. Both were calculated to have `ΔET1−S0` values below the `1.610 eV` oxygen singlet-triplet gap, and both were reported to generate superoxide rather than singlet oxygen under photoirradiation. The study presents this as additional support for the idea that tuning the intramolecular triplet-ground-state splitting energy can bias a photosensitizer toward selective superoxide photogeneration. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:451-474]

## Related concepts

- [[Type-I photochemistry]]
- [[Type-II photochemistry]]
- [[Superoxide]]
- [[Singlet oxygen]]
- [[Photosensitizer]]
- [[Intersystem crossing]]
- [[Photodynamic therapy]]
- [[Hypoxia-compatible photodynamic therapy]]

## Sources

- [[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells]]
