---
title: GSDMD pore-forming activation mechanism
summary: Inflammatory caspases cleave GSDMD to release its autoinhibited N-terminal pore-forming domain, which oligomerizes on lipid membranes and forms large pores that drive pyroptosis.
sources:
  - gasdermin-d-kills-bacteria.md
kind: concept
createdAt: "2026-07-17T08:47:47.305Z"
updatedAt: "2026-07-17T08:47:47.305Z"
tags:
  - gasdermin
  - caspase
  - membrane-biology
  - pyroptosis
aliases:
  - gsdmd-pore-forming-activation-mechanism
  - GPAM
confidence: 0.98
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# GSDMD pore-forming activation mechanism

The [[Gasdermin D|GSDMD]] pore-forming activation mechanism is the process by which full-length GSDMD is converted from an autoinhibited protein into a membrane-inserting pore former that drives [[pyroptosis]]. In the source, GSDMD is described as a crucial mediator of pyroptosis, and its activity depends on cleavage-based activation during host defense responses. ^[gasdermin-d-kills-bacteria.md:36-41, gasdermin-d-kills-bacteria.md:47-60]

## Overview

At the onset of infection or other danger signals, inflammatory caspases are activated from their zymogen forms. The source identifies caspases 1, 4, 5, and 11 as the caspases that cleave GSDMD, linking upstream [[inflammasome]] signaling to downstream pore formation and pyroptotic cell death. ^[gasdermin-d-kills-bacteria.md:51-60, gasdermin-d-kills-bacteria.md:175-182]

GSDMD belongs to the gasdermin family of proteins that generally contain two major parts: a pore-forming N-terminal domain and a C-terminal domain connected by a cleavable linker. The C-terminal domain confers an autoinhibitory character, while the N-terminal domain is responsible for pore-forming activity once released. ^[gasdermin-d-kills-bacteria.md:96-100, gasdermin-d-kills-bacteria.md:60-64]

## Activation by proteolytic cleavage

The source states that inflammatory caspases cleave human and mouse GSDMD at Asp276 and Asp275, respectively. This cleavage separates the active N-terminal domain from the inhibitory C-terminal domain and is the key activation step that enables pore formation. ^[gasdermin-d-kills-bacteria.md:52-60]

This activation step depends on the ability of caspases, described in the source as cysteine proteases involved in cell death regulation, to recognize and attack an aspartic acid residue in the substrate. After cleavage, the released N-terminal fragment, often referred to as GSDMD-N, becomes the active pore-forming effector. ^[gasdermin-d-kills-bacteria.md:56-64]

## Autoinhibition and release of pore-forming activity

In full-length GSDMD, the C-terminal domain suppresses the activity of the N-terminal domain. The source further states that structural stability of full-length GSDMD is enhanced by insertion of the first loop of GSDMD-C into GSDMD-N, and that replacing this part with a short linker raises the cell-death capacity of GSDMD-N. ^[gasdermin-d-kills-bacteria.md:61-67]

This autoinhibitory arrangement explains why cleavage is required for activation: without physical separation of the two domains, the pore-forming N-terminus remains restrained. Once the inhibitory C-terminal constraint is removed, GSDMD-N can execute its membrane-directed function. ^[gasdermin-d-kills-bacteria.md:60-67]

## Membrane targeting and pore assembly

After activation, GSDMD-N translocates to membranes and binds specific lipids rather than associating indiscriminately with all membrane components. The source reports that GSDMD-N binds cardiolipin, phosphatidylinositol phosphates, phosphatidic acid, and phosphatidylserine, with strongest binding to cardiolipin and phosphatidylinositol phosphates such as PtdIns(4)P and PtdIns(4,5)P2. ^[gasdermin-d-kills-bacteria.md:68-71, gasdermin-d-kills-bacteria.md:386-397]

The same source notes that GSDMD-N shows little or no appreciable binding to phosphatidylcholine and phosphatidylethanolamine, and that its preference for inner leaflet phospholipids helps explain why the outer surface of the plasma membrane is unaffected. In one described in vitro study, GSDMD-N oligomerized in the plasma membrane before carrying out bactericidal activity, and inter- and intramolecular disulfide bonds contributed to this oligomerization process. ^[gasdermin-d-kills-bacteria.md:375-400]

Upon membrane binding and assembly, GSDMD-N forms pores that disrupt membrane integrity. During pyroptosis, the source describes a pore about 21 nm in diameter composed of about 33 symmetric protomers. ^[gasdermin-d-kills-bacteria.md:68-71]

## Relationship to pyroptosis

The source describes pyroptosis as being triggered by formation of GSDMD pores in the membrane. This pore formation leads to swelling, rupture of the cell membrane, loss of membrane integrity, and leakage of cytosolic contents. ^[gasdermin-d-kills-bacteria.md:43-50]

In canonical [[inflammasome]] signaling, caspase-1 activation leads both to processing of IL-1beta and IL-18 and to release of the active N-terminal domain from full-length GSDMD. The resulting pore formation in the plasma membrane ultimately promotes pyroptosis and supports immune defense through efflux of danger-associated signals. ^[gasdermin-d-kills-bacteria.md:217-220, gasdermin-d-kills-bacteria.md:254-265]

In the non-canonical pathway, cytosolic LPS activates human caspases 4 and 5 or murine caspase 11. These caspases also cleave GSDMD to release GSDMD-N, which then initiates pyroptosis through pore formation. ^[gasdermin-d-kills-bacteria.md:266-293]

## Membrane selectivity beyond the plasma membrane

The source also describes contexts in which activated GSDMD-N inserts into membranes other than the plasma membrane. In [[Burkholderia cenocepacia]] infection, GSDMD-N inserts into the mitochondrial membrane because of its preference for lipids such as cardiolipin, causing pore formation, increased mitochondrial reactive oxygen species, and disruption of mitochondrial membrane potential. ^[gasdermin-d-kills-bacteria.md:489-512]

Similarly, in [[Francisella novicida]] infection, the source states that activated GSDMD-N can permeate bacterial membranes and mitochondria because of the presence of phospholipids and cardiolipins, forming pores that contribute to bacterial clearance. ^[gasdermin-d-kills-bacteria.md:713-732]

## Significance

Taken together, the mechanism described in the source is a sequence of caspase-mediated cleavage, relief of C-terminal autoinhibition, N-terminal membrane targeting, oligomerization, and pore assembly. This mechanism underlies GSDMD-driven pyroptosis and also supports antimicrobial functions in some infection settings. ^[gasdermin-d-kills-bacteria.md:39-41, gasdermin-d-kills-bacteria.md:59-71, gasdermin-d-kills-bacteria.md:792-803]

## Related concepts

- [[Gasdermin D|GSDMD]]
- [[Pyroptosis]]
- [[Inflammasome]]
- [[Caspase-1]]
- [[Canonical inflammasome pathway]]
- [[Non-canonical inflammasome pathway]]
- [[IL-1beta]]
- [[IL-18]]

## Sources

- [[gasdermin-d-kills-bacteria]]
