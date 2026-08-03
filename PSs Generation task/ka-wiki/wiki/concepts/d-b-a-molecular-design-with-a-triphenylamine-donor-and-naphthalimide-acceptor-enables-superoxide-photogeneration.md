---
title: D-B-A molecular design with a triphenylamine donor and naphthalimide acceptor enables superoxide photogeneration
summary: An electron-donating donor-bridge-acceptor architecture lowers the triplet-ground-state gap and supports selective O2−• production.
sources:
  - photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md
kind: concept
createdAt: "2026-07-17T09:50:15.578Z"
updatedAt: "2026-07-17T09:50:15.578Z"
tags:
  - molecular-design
  - photochemistry
  - superoxide
aliases:
  - d-b-a-molecular-design-with-a-triphenylamine-donor-and-naphthalimide-acceptor-enables-superoxide-photogeneration
  - naphthalimide acceptor enables superoxide photogeneration and D-B-A molecular design with a triphenylamine donor
  - DMDWATDANAESP
confidence: 0.95
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# D-B-A molecular design with a triphenylamine donor and naphthalimide acceptor enables superoxide photogeneration

A donor-bridge-acceptor ([[D-B-A]]) molecular design was used to create `NI-TA`, a photocatalytic [[superoxide radical|superoxide]] generator built from a [[triphenylamine]] donor, a dialkyl fluorene `pi` bridge, and a 1,8-[[naphthalimide]] acceptor. The study presents this architecture as a rational way to modulate the intramolecular triplet-ground state energy splitting so that photoexcitation favors `O2−•` generation. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:17-20, photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:90-95, photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:186-190]

## Design rationale

The authors sought a light-triggered system that would generate superoxide through Type-I photochemistry rather than [[singlet oxygen]] through Type-II energy transfer. Their design logic was that if the triplet-state energy of the photosensitizer were low enough relative to the `3O2/1O2` gap, the singlet-oxygen pathway would be thermodynamically disfavored, while electron transfer from the excited triplet state to oxygen could still proceed. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:171-185]

In `NI-TA`, linking a triphenylamine donor to a naphthalimide acceptor through a conjugated fluorene bridge produced a D-B-A motif with a calculated `ΔET1−S0` of `1.115 eV`, which is below the `1.610 eV` gap required to promote triplet oxygen to singlet oxygen. The paper states that this energetic arrangement, together with fast [[intersystem crossing]], makes `NI-TA` an effective superoxide photogenerator. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:186-195, photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:433-450]

## Molecular and photophysical features

`NI-TA` showed a donor-acceptor charge-transfer absorption shoulder near `425 nm` and a fluorescence emission maximum at `535 nm` with a `180 nm` Stokes shift. Compared with the simpler analogues `NI`, `NI-DF`, and `NI-DPA`, the full D-B-A system showed the strongest evidence of intramolecular charge transfer, which the authors associate with favorable triplet-state formation for photosensitization. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:210-239]

The triphenylamine unit also gave `NI-TA` [[aggregation-induced emission|aggregation-induced emission (AIE)]] behavior. In mixed methanol/water solvent, fluorescence was negligible in pure methanol but increased strongly as the water fraction rose, reaching a `96.8-fold` enhancement at `fw = 90%`. The authors argue that this feature helps address aggregation-caused quenching, a common limitation of previously reported organic superoxide photogenerators in aqueous or biological settings. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:109-118, photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:240-268]

## Evidence for superoxide-selective photogeneration

In aqueous solution, `NI-TA` produced a strong `DHR123` response under white-light irradiation, with about a `50-fold` enhancement after `30 s` relative to probe alone. Its superoxide photogeneration exceeded that of the benzophenothiazine analogue `ENBS` and methylene blue under the reported conditions, and `DMPO` trapping with [[electron paramagnetic resonance|EPR]] detected `DMPO-O2−•` adducts consistent with superoxide formation. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:269-305]

Control-compound comparisons indicated that the full donor-bridge-acceptor arrangement was required for strong activity. Upon photoirradiation, `NI` and `NI-DPA` produced no detectable `DHR123` response, while `NI-DF` generated a signal `11.8-fold` lower than `NI-TA`. Based on these comparisons, the authors conclude that the triphenylamine donor, fluorene bridge, and naphthalimide acceptor all contribute essentially to efficient superoxide production. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:306-333]

The study also tested whether `NI-TA` generated other reactive oxygen species. `ABDA`, `HPF`, and EPR measurements showed little to no evidence of [[singlet oxygen]] or hydroxyl radical production under photoirradiation, supporting the claim that `NI-TA` operates primarily through a Type-I electron-transfer process that produces `O2−•` near-exclusively. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:334-360]

In living `T47D` cells, `NI-TA` plus light generated a strong `DHE` fluorescence signal under normoxia, whereas `NI-DF` gave only limited signal and `SOSG` imaging showed no evidence of singlet-oxygen production. Similar intracellular superoxide signals were also observed in `MDA-MB-231` and `BT474` cells. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:361-377]

## Mechanistic interpretation from theory

DFT and TD-DFT calculations were used to explain why the D-B-A design favors superoxide generation. The `LUMO` of `NI-TA` is mainly localized on the naphthalimide acceptor and the `HOMO` on the triphenylamine donor, giving a calculated `ΔES1−T1` of `1.836 eV`, smaller than the values for `NI` and `NI-DF`. The authors interpret this smaller singlet-triplet gap as promoting more efficient intersystem crossing and triplet formation. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:378-419]

The same calculations support suppression of the singlet-oxygen route. Because the calculated `ΔET1−S0` of `NI-TA` is far below the `3O2/1O2` energy gap, energy transfer from the excited triplet photosensitizer to oxygen is disfavored. The paper therefore concludes from both experiment and theory that `NI-TA` undergoes Type-I photochemistry to generate superoxide. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:420-450]

To test whether this design logic extends beyond one molecule, the authors prepared two additional D-B-A compounds, `NI-TPA` and `NI-DA`, containing alternative `pi` bridges. Both had relatively small calculated `ΔES1−T1` values and `ΔET1−S0` values below `1.610 eV`, and both produced superoxide rather than singlet oxygen under photoirradiation. The paper presents these results as support for the broader idea that appropriately chosen `pi` bridges can tune triplet-ground-state splitting to favor specific superoxide photogeneration. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:451-474]

## Biological context

The superoxide photogenerator `NI-TA` was developed in a study focused on light-triggered [[pyroptosis]] in cancer cells. Under photoirradiation, the generated superoxide was linked to pyroptotic morphology and activation of the `caspase-3/GSDME` pathway rather than the canonical `caspase-1/GSDMD` pathway. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:14-28, photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:482-567]

The paper also emphasizes that superoxide-based photochemistry may be useful under [[hypoxia]], because superoxide can participate in reactions that partially recycle oxygen. Consistent with that rationale, `NI-TA` retained photoinduced anticancer activity and pyroptosis-inducing capability under `2% O2`, with only a modest loss of potency relative to normoxia. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:64-74, photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:568-656]

## Significance

The study describes this as the first rational design in which an electron-donating `pi` bridge was used to tune the triplet-ground-state energy gap so as to favor near-exclusive superoxide photogeneration. In the authors' summary, the donor, acceptor, and spacer combination in `NI-TA` provides a design principle for developing improved photosensitizers that function through superoxide generation rather than singlet-oxygen production. ^[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:447-474, photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells.md:709-751]

## Related concepts

- [[D-B-A]]
- [[Triphenylamine]]
- [[Naphthalimide]]
- [[Superoxide radical|Superoxide]]
- [[Photosensitizer]]
- [[Type-I photochemistry]]
- [[Singlet oxygen]]
- [[Intersystem crossing]]
- [[Aggregation-induced emission]]
- [[Pyroptosis]]
- [[Hypoxia]]

## Sources

- [[photocatalytic-superoxide-radical-generator-that-induces-pyroptosis-in-cancer-cells]]
