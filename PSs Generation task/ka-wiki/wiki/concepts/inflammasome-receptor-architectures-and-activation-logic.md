---
title: Inflammasome receptor architectures and activation logic
summary: The source compares the structures and activation mechanisms of major inflammasomes including NLRP3, NLRP1, NLRC4, AIM2, and pyrin, emphasizing their domains, ligands, and ASC/pro-caspase-1 assembly behavior.
sources:
  - pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md
kind: concept
createdAt: "2026-07-17T10:12:11.994Z"
updatedAt: "2026-07-17T10:12:11.994Z"
tags:
  - inflammasome
  - innate-immunity
  - structure
  - signaling
aliases:
  - inflammasome-receptor-architectures-and-activation-logic
  - activation logic and Inflammasome receptor architectures
  - IRAAAL
confidence: 0.96
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# Inflammasome receptor architectures and activation logic

Inflammasomes are cytoplasmic multiprotein complexes that initiate inflammatory responses and activate pyroptosis. In the canonical setting, they are built from a pattern-recognition receptor (PRR), pro-caspase-1, and often the adaptor ASC. The review identifies the major canonical inflammasome receptors as [[NLRP3 inflammasome|NLRP3]], [[NLRP1 inflammasome|NLRP1]], [[NLRC4 inflammasome|NLRC4]], [[AIM2 inflammasome|AIM2]], and [[Pyrin inflammasome|pyrin]]. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:257-264, pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:459-463]

## Core assembly logic

Canonical inflammasome activation begins when PRRs detect [[PAMPs]] or [[DAMPs]]. This detection drives conformational change and oligomerization of receptor monomers, allowing the receptor to serve as the core of the inflammasome complex. Assembly brings pro-caspase-1 molecules into proximity, promoting caspase-1 activation by autoproteolysis. Activated caspase-1 then matures pro-IL-1β and pro-IL-18 and cleaves [[Gasdermin D|GSDMD]], whose N-terminal fragment forms membrane pores that support pyroptosis and mediator release. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:265-299]

ASC functions as the main adaptor for receptors that lack a CARD capable of directly recruiting pro-caspase-1. Because ASC contains both a PYD and a CARD, it bridges PYD-containing receptors such as NLRP3, AIM2, and pyrin to the CARD domain of pro-caspase-1. By contrast, some CARD-containing receptors, including NLRC4 and NLRP1B, can assemble pro-caspase-1 directly through CARD-CARD interactions, reducing or bypassing the need for ASC. The source also notes that NLRP1 can recruit pro-caspase-1 with or without ASC. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:273-285]

## Receptor architectures

[[NLRP3 inflammasome|NLRP3]] is described as a canonical NLR-family inflammasome receptor with an N-terminal PYD, a central NACTH nucleotide-binding and oligomerization domain, and a C-terminal leucine-rich repeat (LRR) region. The source specifically notes that NLRP3 lacks a C-terminal CARD, which explains its dependence on ASC to connect to pro-caspase-1. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:464-468, pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:499-501]

[[NLRP1 inflammasome|NLRP1]] is presented as structurally distinctive within the family. In addition to an N-terminal PYD, central NACTH domain, and C-terminal LRR, it contains a FIIND domain and a CARD at the C terminus. Its FIIND domain undergoes autolytic proteolytic cleavage, which the source states is necessary for NLRP1 activity. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:469-482]

[[NLRC4 inflammasome|NLRC4]] contains an N-terminal CARD, a NACTH domain, and a C-terminal LRR. This CARD-containing architecture fits its ability to recruit pro-caspase-1 directly through CARD-CARD interactions. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:483-484, pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:273-277]

[[AIM2 inflammasome|AIM2]] is distinguished by PYD and CARD-related assembly logic together with a C-terminal HIN-200 domain. The HIN-200 domain binds dsDNA derived from cellular damage or microbial infection, while the PYD connects to ASC to drive inflammasome maturation and pyroptosis. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:485-486, pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:521-528]

[[Pyrin inflammasome|Pyrin]] contains an N-terminal PYD plus a linker region associated with B-box, coiled-coil, and B30.2 domains; its oligomerization is mediated by the coiled-coil and B-box regions. The source further states that pyrin binds ASC through its N-terminal PYD to execute inflammasome function. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:487-490, pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:528-533]

## Receptor-specific activation logic

[[NLRP3 inflammasome|NLRP3]] responds to a broad set of activation-associated inputs, including ATP, reactive oxygen species, potassium efflux, and internal damage signals. Its NACTH-domain ATPase activity is required for oligomer formation after activation. Once activated, the NLRP3 PYD engages the ASC PYD to initiate inflammasome assembly, and the review notes that NLRP3 expression is low in dormant cells but upregulated through [[NF-kappaB|NF-kB]] signaling. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:493-506]

[[NLRP1 inflammasome|NLRP1]] is activated by at least two routes in the source. One route involves anthrax lethal factor cleavage of NLRP1, which drives N-terminal degradation and releases the C-terminal CARD so NLRP1 can directly bind caspase-1 to form an inflammasome. A second route involves ATP hydrolysis by the NACTH domain, which changes NLRP1 conformation and enables integration into an ASC-dependent inflammasome; this route is described in the context of LRR binding to viral dsRNA. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:507-518]

[[NLRC4 inflammasome|NLRC4]] recognizes bacterial type III secretion system proteins and flagellin. The source does not elaborate additional domain-by-domain signaling steps here, but it clearly places these ligands as the core recognition logic for NLRC4 activation. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:519-520]

[[AIM2 inflammasome|AIM2]] is activated by sensing dsDNA associated with cellular disruption and pathogen assault. Binding occurs through the HIN-200 domain, and signaling proceeds through the PYD-ASC connection to induce inflammasome maturation and pyroptosis. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:521-528]

[[Pyrin inflammasome|Pyrin]] detects pathogen-driven modification and silencing of Rho GTPases. After activation, pyrin promotes caspase-1 maturation and IL-1β release, and it uses its N-terminal PYD to bind ASC as part of this signaling logic. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:528-533]

## Functional outcome

Although receptor architectures differ, the downstream logic converges on caspase-1 activation, maturation of IL-1β and IL-18, and gasdermin-mediated pore formation. This shared endpoint links inflammasome sensing to [[pyroptosis]], inflammatory cytokine release, and broader immune regulation. ^[pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:103-108, pyroptosis-and-inflammasomes-in-cancer-and-inflammation.md:287-299]

## Related concepts

- [[Pyroptosis]]
- [[ASC]]
- [[Caspase-1]]
- [[Gasdermin D|GSDMD]]
- [[PAMPs]]
- [[DAMPs]]
- [[NLRP3 inflammasome]]
- [[NLRP1 inflammasome]]
- [[NLRC4 inflammasome]]
- [[AIM2 inflammasome]]
- [[Pyrin inflammasome]]
- [[IL-1beta]]
- [[IL-18]]
- [[NF-kappaB|NF-kB]]

## Sources

- [[pyroptosis-and-inflammasomes-in-cancer-and-inflammation]]
