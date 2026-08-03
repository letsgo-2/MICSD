---
title: Differential mitochondrial control of apoptosome versus pyroptosome assembly
summary: The source proposes that MOMP and MPT represent distinct mitochondrial stress states that bias Apaf-1 toward assembling either a caspase-9 apoptosome or a caspase-4 pyroptosome, aided by different ATP conditions and stoichiometries.
sources:
  - apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md
kind: concept
createdAt: "2026-07-17T07:51:00.032Z"
updatedAt: "2026-07-17T07:51:00.032Z"
tags:
  - mitochondria
  - apoptosis
  - pyroptosis
  - Apaf-1
aliases:
  - differential-mitochondrial-control-of-apoptosome-versus-pyroptosome-assembly
  - DMCOAVPA
confidence: 0.97
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# Differential mitochondrial control of apoptosome versus pyroptosome assembly

Differential mitochondrial control of apoptosome versus pyroptosome assembly refers to the study’s model for how distinct forms and intensities of mitochondrial stress bias [[Apaf-1]] toward assembling either an [[apoptosome]] with caspase-9 or a [[pyroptosome]] with caspase-4/11. In this model, [[mitochondrial outer membrane permeabilization|MOMP]] is associated with apoptosome formation and apoptosis, whereas [[mitochondrial permeability transition|MPT]] is associated with pyroptosome formation and pyroptosis. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:522-527, apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:539-542, apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:571-573]

## Core distinction

The source states that low-dose bile acids and doxorubicin, described as conditions that induce MOMP-initiated apoptosis, activated caspase-9 and caspase-3 over time but did not activate caspase-11 or caspase-1. By contrast, high-dose bile acids, characterized as MPT-triggered pyroptotic conditions, rapidly activated caspase-11 and caspase-3, peaking around 60 minutes, while caspase-9 and caspase-1 were not activated in those MPT conditions. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:528-539]

Consistent with those activity profiles, low-dose bile acids promoted assembly of an [[Apaf-1]]/caspase-9 apoptosome, whereas high-dose bile acids promoted assembly of an Apaf-1/caspase-11 pyroptosome. The paper therefore frames mitochondria as controlling cell-death choice by directing Apaf-1 into different signaling complexes under MOMP versus MPT conditions. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:539-542, apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:571-573]

## Pyroptosome assembly under MPT

The paper identifies caspase-4/11 as a general sensor of MPT induced by bile acids, calcium overload, or ANT activators. Under these conditions, MPT activates Apaf-1, which recruits and activates caspase-4/11 rather than caspase-9, and the activated caspase-4/11 then cleaves caspase-3, leading to [[Gasdermin E|GSDME]] cleavage and pyroptosis. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:133-142, apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:347-367, apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:463-467]

Biochemical experiments supported this assembly model. Apaf-1 co-precipitated with caspase-11, Apaf-1 bound caspase-4 through the CARD region, and this interaction persisted even in CASPASE-9 knockout cells, arguing that caspase-9 is not required for formation of the Apaf-1/caspase-4 complex. In APAF-1 knockout HepG2 cells, bile acids and lonidamine failed to activate the caspase-4/caspase-3/GSDME pathway or trigger pyroptotic death, indicating that Apaf-1 is functionally necessary for MPT-triggered pyroptosome signaling. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:356-367, apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:392-417]

In a reconstituted cell-free system, Apaf-1 activated caspase-4 only when ATP and cytochrome c were present, resembling the cofactor dependence of apoptosome signaling. In that same system, caspase-4 activated caspase-3, and the downstream pathway led to GSDMD being cleaved by caspase-3 into an inactive fragment rather than being processed into its pore-forming form. The authors therefore define the MPT-induced Apaf-1/caspase-4 complex as an [[apaf-1-pyroptosome|Apaf-1 pyroptosome]]. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:417-467]

## Mitochondrial signals that bias the choice

The study proposes that both apoptosome and pyroptosome assembly depend on mitochondrial release of cytochrome c and ATP for Apaf-1 activation, but that the timing and magnitude of these signals differ between MOMP and MPT. Time-course analysis showed that MPT caused an earlier increase in cytoplasmic cytochrome c than MOMP and, unlike MOMP, induced an immediate release of ATP into the cytoplasm. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:574-581]

The ATP requirement also differed between the two Apaf-1-dependent complexes. Caspase-4 recruitment to Apaf-1 required a much higher ATP level than caspase-9 recruitment, and under high ATP conditions at or above 2 mM, caspase-4 competitively inhibited caspase-9 activation in the cell-free system. The paper uses these findings to argue that ATP abundance during MPT helps favor pyroptosome assembly over apoptosome assembly. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:582-586]

## Stoichiometric differences

The two Apaf-1 complexes also differed in stoichiometry. Caspase-4 activity on an Apaf-1 scaffold reached a maximum at an approximate caspase:Apaf-1 molar ratio of 2:7, whereas caspase-9 activity peaked at about 4:7. Size-exclusion chromatography further supported a ratio of about 1.8 to 2.1 molecules of caspase-4 per Apaf-1 heptamer, which the authors summarize as a 7:2 Apaf-1:caspase-4 stoichiometry for the pyroptosome, distinct from the 7:4 Apaf-1:caspase-9 stoichiometry of the apoptosome. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:587-609]

The source further reports that the catalytic efficiency `Kcat/Km` of caspase-4 on the [[apaf-1-pyroptosome|Apaf-1 pyroptosome]] scaffold was about 22% higher than that of caspase-9 on the apoptosome scaffold. The authors interpret the different stoichiometries and scaffold properties as part of the mechanism by which mitochondria dictate the choice between apoptosis and pyroptosis. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:594-609]

## Separation from other death pathways

The study presents MPT-driven pyroptosome signaling as distinct from both canonical inflammasome signaling and classical intrinsic apoptosis. In MPT-triggered conditions, CASPASE-4 knockout reduced pyroptotic cell death, whereas CASPASE-9 knockout did not, and the two initiator caspases did not affect each other’s activity. The paper also found that caspase-8 was unlikely to be involved in bile acid-induced MPT-triggered pyroptosis. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:543-561]

Additional experiments separated MPT from MOMP mechanistically. Knockout of [[BAX]] and [[BAK]] had little effect on bile acid- and lonidamine-induced caspase-4/caspase-3 activation, GSDME cleavage, and pyroptosis, but strongly impaired doxorubicin-induced caspase-9/caspase-3/PARP activation and apoptosis. Conversely, blocking MPT with bongkrekic acid affected MPT-linked pyroptotic signaling but not doxorubicin-induced apoptotic signaling. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:562-570]

## Functional interpretation

In the discussion, the authors propose that MPT-triggered pyroptosis represents a faster and higher-threshold response than MOMP-driven apoptosis. They note that MPT-elicited pyroptosis occurs within a narrow window of less than 4 hours, whereas MOMP-induced apoptosis usually takes more than 24 hours, and they suggest that Apaf-1/caspase-4 pyroptosome assembly may serve as an immediate response to severe mitochondrial danger signals. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:717-733]

The paper ultimately argues that mitochondria contain a precise system for sensing different types or extents of stress and routing Apaf-1 into distinct death programs. In that framework, MOMP mainly facilitates Apaf-1/caspase-9 apoptosome assembly, while MPT mainly facilitates Apaf-1/caspase-4 pyroptosome assembly, thereby differentially controlling the choice between [[apoptosis]] and [[pyroptosis]]. ^[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition.md:749-760]

## Related concepts

- [[Apaf-1]]
- [[Apoptosome]]
- [[Pyroptosome]]
- [[Mitochondrial permeability transition]]
- [[Mitochondrial outer membrane permeabilization]]
- [[Caspase-4]]
- [[Caspase-9]]
- [[Caspase-3]]
- [[Gasdermin E|GSDME]]
- [[Apoptosis]]
- [[Pyroptosis]]

## Sources

- [[apaf-1-pyroptosome-senses-mitochondrial-permeability-transition]]
