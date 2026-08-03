---
title: LiPOP1 as a photoswitchable MLKL-NT necroptosis effector
summary: LiPOP1 is an optimized CRY2-fused MLKL N-terminal mutant that minimizes dark toxicity while retaining light-induced plasma-membrane translocation, phosphoinositide binding, calcium influx, phosphatidylserine exposure, and rapid necroptotic killing.
sources:
  - optogenetic-control-of-nonapoptotic-cell-death.md
kind: concept
createdAt: "2026-07-17T09:22:45.494Z"
updatedAt: "2026-07-17T09:22:45.494Z"
tags:
  - necroptosis
  - MLKL
  - optogenetics
  - membrane-biology
aliases:
  - lipop1-as-a-photoswitchable-mlkl-nt-necroptosis-effector
  - LAAPMNE
confidence: 0.98
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# LiPOP1 as a photoswitchable MLKL-NT necroptosis effector

`LiPOP1` is an optogenetic tool designed to trigger [[necroptosis]] by making the N-terminal effector region of [[MLKL]] photoswitchable. In the study, LiPOP1 was created within a broader LiPOP toolkit for light-controlled non-apoptotic cell death, and specifically serves as a light-inducible mimic of MLKL-mediated plasma-membrane disruption. ^[optogenetic-control-of-nonapoptotic-cell-death.md:13-23, optogenetic-control-of-nonapoptotic-cell-death.md:207-216, optogenetic-control-of-nonapoptotic-cell-death.md:286-293]

## Background

In physiological necroptosis, signaling proceeds through `RIPK1` and `RIPK3` to activate MLKL. Activated MLKL is phosphorylated, oligomerizes, and moves to the plasma membrane, where its N-terminal region disrupts the membrane and causes inflammatory cell death. The paper frames LiPOP1 as a way to bypass upstream receptor signaling and directly reconstitute this terminal execution step with light. ^[optogenetic-control-of-nonapoptotic-cell-death.md:56-65, optogenetic-control-of-nonapoptotic-cell-death.md:153-162, optogenetic-control-of-nonapoptotic-cell-death.md:273-277]

## Design

The authors first tested several `MLKL-NT` truncations fused to `mCherry-CRY2` to reproduce MLKL-driven membrane permeabilization. Fragments spanning residues `1-178`, `1-166`, `1-154`, and `1-125` showed high basal cytotoxicity even without illumination, while truncation to residue `98` abolished membrane-disrupting activity, indicating that the structural integrity of the four-helical bundle domain was required. ^[optogenetic-control-of-nonapoptotic-cell-death.md:208-223, optogenetic-control-of-nonapoptotic-cell-death.md:234-235]

To reduce dark activity, the study introduced charge-neutralizing mutations into the `MLKL-NT (1-125)` fragment. Single, double, and triple alanine substitutions reduced basal cytotoxicity, and the triple mutant `H15A/K16A/R17A` showed the lowest dark activity while retaining light-induced plasma-membrane puncturing. This optimized construct was named `LiPOP1`. ^[optogenetic-control-of-nonapoptotic-cell-death.md:236-246, optogenetic-control-of-nonapoptotic-cell-death.md:305-307]

Figure 1 describes LiPOP1 as `CRY2PHR` fused to an optimized `MLKL-NT` fragment. In the dark, the engineered `CRY2-MLKL-NT` construct had minimal cytotoxic activity; upon blue-light illumination, CRY2-driven multimerization caused MLKL-NT to perforate the plasma membrane, mimicking the effect of RIPK1/3-dependent MLKL activation in necroptosis. ^[optogenetic-control-of-nonapoptotic-cell-death.md:289-293]

## Light-triggered necroptotic activity

In HeLa cells, LiPOP1 translocated from the cytosol to the plasma membrane after blue-light stimulation with a reported half-life of `12.8 +/- 1.1 s`. This redistribution was accompanied by progressive Annexin V staining at the plasma membrane, consistent with externalization of phosphatidylserine during necroptotic death, with a reported half-life of `18.0 +/- 4.0 min`. ^[optogenetic-control-of-nonapoptotic-cell-death.md:247-251, optogenetic-control-of-nonapoptotic-cell-death.md:308-314]

Under pulsed blue-light illumination, LiPOP1 killed almost all expressing HeLa cells within `30 min`. The same illumination did not cause overt phototoxicity in cells expressing `mCh-CRY2` alone, and a control construct consisting of `MLKL-NT 3A (H15A/K16A/R17A)-mCh` without the CRY2 module did not show cell death under the same photostimulation conditions. ^[optogenetic-control-of-nonapoptotic-cell-death.md:251-257, optogenetic-control-of-nonapoptotic-cell-death.md:312-314]

LiPOP1 activation was also associated with pronounced `Ca2+` influx caused by plasma-membrane disruption. In HeLa cells co-expressing LiPOP1 and the genetically encoded calcium indicator `GCaMP6m`, the calcium signal rose with a reported half-life of `9.7 +/- 0.3 min` after photostimulation. ^[optogenetic-control-of-nonapoptotic-cell-death.md:258-262, optogenetic-control-of-nonapoptotic-cell-death.md:315-317]

## Membrane-binding properties

The study tested whether LiPOP1 retained the phosphoinositide-binding behavior associated with activated MLKL. In a lipid-strip assay, LiPOP1 showed little appreciable interaction with immobilized phospholipids in the dark, but under blue light it bound most strongly to `PI(3,5)P2`, `PI(4,5)P2`, and `PI(3,4,5)P3`, which the authors note are abundant in the plasma membrane. It bound less strongly to `PI(3,4)P2`, `PI3P`, and `PI4P`, which are more associated with intracellular organelles. ^[optogenetic-control-of-nonapoptotic-cell-death.md:263-272, optogenetic-control-of-nonapoptotic-cell-death.md:317-320]

The authors conclude from these data that LiPOP1 retains MLKL-like phosphoinositide-binding capability and can engage and perforate membranes in a light-dependent manner. This enables photo-triggered necroptosis while bypassing conventional death-receptor activation, and also provides photo-tunable control over calcium influx and necroptotic cell death. ^[optogenetic-control-of-nonapoptotic-cell-death.md:273-278]

## In vivo and chemo-optogenetic extensions

To test LiPOP1 in vivo, the study used HeLa xenografts expressing LiPOP1 and combined the construct with [[upconversion nanoparticles|UCNPs]] that convert near-infrared light to blue emission. After intratumoral UCNP injection and pulsed `980 nm` irradiation, the LiPOP1-expressing tumors showed substantial size reduction relative to the `mCh-CRY2` control group, establishing wireless nano-optogenetic control of LiPOP1-mediated tumor necroptosis in mice. ^[optogenetic-control-of-nonapoptotic-cell-death.md:279-360, optogenetic-control-of-nonapoptotic-cell-death.md:998-1011]

The authors also generated `LiPOP1-NanoLuc`, a fusion that uses NanoLuc bioluminescence to activate the CRY2 module through a chemo-optogenetic `NanoLOGS` strategy. In cultured tumor cells, treatment with furimazine triggered plasma-membrane translocation and necroptotic death, and in `786-O` xenografts repeated `FFz` administration reduced tumor size relative to controls. These experiments extend LiPOP1 from direct blue-light stimulation to wireless luminescence-assisted activation. ^[optogenetic-control-of-nonapoptotic-cell-death.md:381-422, optogenetic-control-of-nonapoptotic-cell-death.md:439-472, optogenetic-control-of-nonapoptotic-cell-death.md:585-607]

## Significance within the study

Within the paper, LiPOP1 is presented as an engineered terminal necroptosis effector that isolates the execution phase of MLKL-dependent cell death from upstream pathway cross-talk. The broader discussion emphasizes that LiPOP tools provide remote control over non-apoptotic cell death with high spatial and temporal precision and may be useful for mechanistic studies, tumor-cell killing, and future immunotherapy-related applications. ^[optogenetic-control-of-nonapoptotic-cell-death.md:131-149, optogenetic-control-of-nonapoptotic-cell-death.md:672-683, optogenetic-control-of-nonapoptotic-cell-death.md:729-763]

## Related concepts

- [[Necroptosis]]
- [[MLKL]]
- [[RIPK1]]
- [[RIPK3]]
- [[CRY2]]
- [[Phosphatidylserine]]
- [[Calcium influx]]
- [[Upconversion nanoparticles]]
- [[NanoLOGS]]
- [[Optogenetics]]

## Sources

- [[optogenetic-control-of-nonapoptotic-cell-death]]
