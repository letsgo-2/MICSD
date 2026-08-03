---
title: Light-driven reconstruction of the RIPK1→RIPK3→MLKL necroptosis cascade
summary: By fusing CRY2 to RIPK1 or RIPK3, the study uses blue light to induce necrosome assembly, RIPK3 and MLKL phosphorylation, and supports the ordered signaling sequence RIPK1 to RIPK3 to MLKL in necroptosis.
sources:
  - optogenetic-control-of-nonapoptotic-cell-death.md
kind: concept
createdAt: "2026-07-17T09:22:01.280Z"
updatedAt: "2026-07-17T09:22:01.280Z"
tags:
  - necroptosis
  - signaling
  - optogenetics
  - RIPK3
aliases:
  - light-driven-reconstruction-of-the-ripk1ripk3mlkl-necroptosis-cascade
  - LROTRNC
confidence: 0.96
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# Light-driven reconstruction of the RIPK1→RIPK3→MLKL necroptosis cascade

The study describes necroptosis as a regulated, proinflammatory cell-death pathway that is commonly initiated downstream of [[TNFR1]], followed by successive activation of [[RIPK1]], [[RIPK3]], and [[MLKL]]. Activated MLKL then oligomerizes and moves to the [[plasma membrane]], where it disrupts membrane integrity and promotes release of intracellular contents that induce inflammatory responses. ^[optogenetic-control-of-nonapoptotic-cell-death.md:56-65]

This work used optogenetic tools to reconstruct early necroptotic signaling with light, bypassing death-receptor stimulation. The authors engineered photoswitchable versions of key pathway components so they could test whether light-induced assembly at one step was sufficient to drive the next step in the cascade. ^[optogenetic-control-of-nonapoptotic-cell-death.md:137-149, optogenetic-control-of-nonapoptotic-cell-death.md:153-168]

## Experimental strategy

To initiate the pathway at the level of RIPK1, the authors fused RIPK1 to the photosensory oligomerization module `CRY2PHR`. In [[HeLa]] cells, which the paper identifies as lacking endogenous RIPK3 expression, both `mCh-CRY2-RIPK1` and `RIPK3-GFP` were diffusely cytosolic in the dark. After brief `470 nm` illumination, `mCh-CRY2-RIPK1` rapidly oligomerized and `RIPK3-GFP` co-clustered with it, indicating light-dependent recruitment of RIPK3 by oligomerized RIPK1. ^[optogenetic-control-of-nonapoptotic-cell-death.md:164-180]

The RIPK1-to-RIPK3 step was further supported by co-immunoprecipitation and phosphorylation analysis. With increasing durations of blue-light exposure, the amount of `RIPK3-GFP` immunoprecipitated by RIPK1 increased, and phosphorylation of RIPK3 at serine 277 also increased, consistent with light-induced necrosome formation and RIPK3 activation. ^[optogenetic-control-of-nonapoptotic-cell-death.md:178-182, optogenetic-control-of-nonapoptotic-cell-death.md:297-299]

Because physiological necroptosis downstream of TNFR1 can cross-talk with apoptotic regulators including [[FADD]] and [[caspase-8]], the authors also tested the next step directly by bypassing RIPK1. They note that oligomerized RIPK1 can recruit caspase-8, which cleaves RIPK1 and RIPK3 and can shift signaling away from necroptosis, so they used light to trigger RIPK3 oligomerization without involving upstream RIPK1. ^[optogenetic-control-of-nonapoptotic-cell-death.md:183-193]

## RIPK3-to-MLKL activation

Using the same design logic, the authors generated `mCh-CRY2-RIPK3` to test whether RIPK3 oligomerization is sufficient to activate MLKL. Upon blue-light stimulation, they observed formation of `mCh-CRY2-RIPK3` puncta together with co-clustering of `MLKL-Venus`, followed by increased MLKL phosphorylation, which the paper presents as a clear indication of MLKL activation. ^[optogenetic-control-of-nonapoptotic-cell-death.md:191-199, optogenetic-control-of-nonapoptotic-cell-death.md:300-304]

The source also summarizes the biochemical logic of this step: oligomerized RIPK1 recruits RIPK3, RIPK3 undergoes auto-phosphorylation, and activated RIPK3 phosphorylates MLKL at threonine 357 and serine 358. These modifications expose the N-terminal four-helical bundle domain of MLKL, enabling the membrane-disruptive phase of necroptosis. ^[optogenetic-control-of-nonapoptotic-cell-death.md:153-162]

## Conclusion of the reconstruction

Across these optogenetic reconstitution experiments, the authors report similar phenotypes not only in HeLa cells but also in human `786-O` renal carcinoma cells and rodent `B16` melanoma cells. They conclude that light-driven assembly of pathway components provides evidence that the initial steps of necroptosis proceed in the order `RIPK1→RIPK3→MLKL` across multiple mammalian cell lines. ^[optogenetic-control-of-nonapoptotic-cell-death.md:198-206]

In this framework, light serves as a precise trigger for necrosome reconstruction rather than as a nonspecific injury stimulus. The paper presents this approach as a way to dissect necroptotic signaling without co-activating upstream death-receptor programs that can overlap with apoptosis. ^[optogenetic-control-of-nonapoptotic-cell-death.md:131-149, optogenetic-control-of-nonapoptotic-cell-death.md:202-206]

## Related concepts

- [[Necroptosis]]
- [[RIPK1]]
- [[RIPK3]]
- [[MLKL]]
- [[Necrosome]]
- [[TNFR1]]
- [[HeLa]]
- [[Plasma membrane]]
- [[Optogenetics]]

## Sources

- [[optogenetic-control-of-nonapoptotic-cell-death]]
