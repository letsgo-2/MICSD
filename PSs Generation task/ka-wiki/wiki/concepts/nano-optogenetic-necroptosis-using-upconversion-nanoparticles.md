---
title: Nano-optogenetic necroptosis using upconversion nanoparticles
summary: The study couples LiPOP1 to NIR-to-blue upconversion nanoparticles so that 980 nm irradiation can wirelessly activate necroptosis and suppress tumor growth in mouse xenografts.
sources:
  - optogenetic-control-of-nonapoptotic-cell-death.md
kind: concept
createdAt: "2026-07-17T09:23:16.897Z"
updatedAt: "2026-07-17T09:23:16.897Z"
tags:
  - nanotechnology
  - optogenetics
  - necroptosis
  - cancer
aliases:
  - nano-optogenetic-necroptosis-using-upconversion-nanoparticles
  - NNUUN
confidence: 0.95
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# Nano-optogenetic necroptosis using upconversion nanoparticles

Nano-optogenetic necroptosis using upconversion nanoparticles is an in vivo optogenetic strategy from *Optogenetic Control of Non-Apoptotic Cell Death* in which the LiPOP1 necroptosis tool is paired with [[upconversion nanoparticles]] (UCNPs) to enable wireless activation by near-infrared (NIR) light. The UCNPs convert NIR light into blue emission that matches the CRY2 photoreceptor used in LiPOP1, allowing light-triggered necroptosis in living animals with deeper tissue penetration than direct blue-light stimulation. ^[optogenetic-control-of-nonapoptotic-cell-death.md:13-23, optogenetic-control-of-nonapoptotic-cell-death.md:134-149, optogenetic-control-of-nonapoptotic-cell-death.md:339-359]

## Mechanism

LiPOP1 is an engineered fusion of the CRY2 photoreceptor module and an optimized N-terminal fragment of [[MLKL]], the membrane-perforating effector in [[necroptosis]]. In the dark, the construct has minimal cytotoxic activity; upon blue-light activation, CRY2 drives multimerization of MLKL-NT and promotes plasma-membrane disruption, producing necroptotic cell death. ^[optogenetic-control-of-nonapoptotic-cell-death.md:152-162, optogenetic-control-of-nonapoptotic-cell-death.md:236-278, optogenetic-control-of-nonapoptotic-cell-death.md:288-310]

To extend this system in vivo, the authors coupled LiPOP1 with UCNPs, described as nano-transducers with NIR-to-blue upconversion luminescence. They used previously developed 40-nm `β-NaYF4:Yb,Tm@β-NaYF4` particles that emit bright blue light under 980 nm irradiation, which in turn activates the CRY2-based tool. ^[optogenetic-control-of-nonapoptotic-cell-death.md:279-280, optogenetic-control-of-nonapoptotic-cell-death.md:339-347]

## In vivo implementation

For the mouse experiments, 150 μg of UCNPs were injected into each tumor site of SCID-beige mice bearing HeLa-LiPOP1 xenografts. The tumors were then exposed to pulsed 980 nm light at 250 mW/cm^2 for 2 hours every three days, with 20 s on and 5 min off pulses. Blue emission was observed from the injection sites after NIR stimulation, confirming local upconversion in tissue. ^[optogenetic-control-of-nonapoptotic-cell-death.md:326-336, optogenetic-control-of-nonapoptotic-cell-death.md:348-353, optogenetic-control-of-nonapoptotic-cell-death.md:998-1004]

Under this regimen, the HeLa-LiPOP1 group showed a substantial reduction in tumor size compared with the mCherry-CRY2 control group. The paper presents this as evidence that the NIR light-tunable nano-optogenetic platform enabled wireless optical control of LiPOP1-mediated necroptosis for tumor killing in vivo. ^[optogenetic-control-of-nonapoptotic-cell-death.md:353-360]

## Context

The authors frame UCNP coupling as one of two wireless optogenetic approaches used to address limited tissue penetration of blue light. The other approach was NanoLuc-based bioluminescence, but the UCNP method specifically preserves optogenetic spatial control while extending activation depth through NIR illumination. ^[optogenetic-control-of-nonapoptotic-cell-death.md:143-149, optogenetic-control-of-nonapoptotic-cell-death.md:738-748]

## Related concepts

- [[Optogenetic Control of Non-Apoptotic Cell Death]]
- [[LiPOP1]]
- [[Necroptosis]]
- [[MLKL]]
- [[CRY2]]
- [[Upconversion nanoparticles]]
- [[NIR light]]

## Sources

- [[optogenetic-control-of-nonapoptotic-cell-death]]
