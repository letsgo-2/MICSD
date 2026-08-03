---
title: LiPOP2a and LiPOP2b as optogenetic pyroptosis actuators based on GSDMD uncaging
summary: "The paper develops two light-activated pyroptosis systems: LiPOP2a uses LOVTRAP-mediated release of GSDMD-NT from GSDMD-CT autoinhibition, while LiPOP2b uses cpLOV2 steric caging of engineered GSDMD-NT to restore pore-forming toxicity upon illumination."
sources:
  - optogenetic-control-of-nonapoptotic-cell-death.md
kind: concept
createdAt: "2026-07-17T09:24:50.097Z"
updatedAt: "2026-07-17T09:24:50.097Z"
tags:
  - pyroptosis
  - GSDMD
  - optogenetics
  - protein-engineering
aliases:
  - lipop2a-and-lipop2b-as-optogenetic-pyroptosis-actuators-based-on-gsdmd-uncaging
  - LiPOP2b as optogenetic pyroptosis actuators based on GSDMD uncaging and LiPOP2a
  - LALAOPABOGU
confidence: 0.98
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# LiPOP2a and LiPOP2b as optogenetic pyroptosis actuators based on GSDMD uncaging

LiPOP2a and LiPOP2b are optogenetic tools from the LiPOP series that were designed to reconstruct key steps in pyroptosis by controlling gasdermin D (GSDMD) activation with light. The paper presents two strategies: LiPOP2a uses light-inducible dissociation of GSDMD-NT from GSDMD-CT via a LOV2-Zdk pair, while LiPOP2b uses a circularly permuted LOV2 module to sterically cage GSDMD-NT until blue light exposure uncages its pore-forming activity. ^[optogenetic-control-of-nonapoptotic-cell-death.md:473-580]

## Design

Pyroptosis is described as a programmed cell death pathway in which inflammatory caspases cleave GSDMD to release its N-terminal pore-forming fragment, GSDMD-NT. LiPOP2a and LiPOP2b were built to mimic this activation step without caspase cleavage: LiPOP2a places GSDMD-NT and GSDMD-CT in a light-sensitive LOV2-Zdk assembly, and LiPOP2b fuses an engineered GSDMD-NT fragment to cpLOV2 so that light-induced conformational change restores pore-forming function. ^[optogenetic-control-of-nonapoptotic-cell-death.md:473-580, optogenetic-control-of-nonapoptotic-cell-death.md:806-821]

## LiPOP2a

LiPOP2a co-expresses GSDMD-NT and GSDMD-CT at about a 1:1 ratio using a P2A-based bicistronic construct. In the dark, the LOV2-Zdk interaction keeps the fragments associated and limits cytotoxicity; after blue light stimulation, dissociation exposes GSDMD-NT and induces pyroptotic cell death. The study reports minimal dark death, a marked increase in double-positive cell-death staining after light, pyroptotic morphology in live imaging, and increased LDH release. ^[optogenetic-control-of-nonapoptotic-cell-death.md:494-533, optogenetic-control-of-nonapoptotic-cell-death.md:696-715]

## LiPOP2b

LiPOP2b is a more compact design based on cpLOV2 fused to an engineered GSDMD-NT fragment. The authors neutralized positive charges in the putative pore-forming region and identified the 4A mutant, R138A/K146A/R152A/R154A, as the version with the least dark activity while retaining strong light-inducible cytotoxicity. LiPOP2b was validated by flow cytometry, time-lapse imaging, and LDH release assays. ^[optogenetic-control-of-nonapoptotic-cell-death.md:534-580, optogenetic-control-of-nonapoptotic-cell-death.md:806-821]

## Mechanistic readouts

For LiPOP2b, lipid-strip assays showed light-dependent interaction with membrane-enriched phospholipids, including PI(3,5)P2, PI(4,5)P2, and PI(3,4,5)P3. The authors note that LiPOP2b also interacted with PI3P and PI4P under blue light, suggesting membrane-perforating activity that may extend to subcellular organelles. ^[optogenetic-control-of-nonapoptotic-cell-death.md:567-580, optogenetic-control-of-nonapoptotic-cell-death.md:959-972]

## Experimental use

The paper further applies LiPOP2a and LiPOP2b in Jurkat CAR T cells, where both constructs induced pyroptotic morphology and LDH release under blue light, with LiPOP2b acting faster than LiPOP2a. This supports their use as light-switchable cell-death actuators for selectively eliminating engineered T cells. ^[optogenetic-control-of-nonapoptotic-cell-death.md:655-671, optogenetic-control-of-nonapoptotic-cell-death.md:824-836]

## Related concepts

- [[Pyroptosis]]
- [[Gasdermin D|GSDMD]]
- [[Caspase-1]]
- [[Optogenetics]]
- [[LOV2]]
- [[HeLa]]
- [[Jurkat T cells]]
- [[CAR T-cell therapy]]

## Sources

- [[optogenetic-control-of-nonapoptotic-cell-death]]
