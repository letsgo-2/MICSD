---
title: Tumour-selective nanoparticle protein release via overlapping NP and Phe-BF3 biodistribution
summary: Gold nanoparticle conjugates carrying proteins such as GFP, mNeonGreen-NLS, or GSDMA3 can accumulate in tumours, and because Phe-BF3 also enriches in tumours, their overlapping distribution enables selective intratumoural protein release in vivo.
sources:
  - a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md
kind: concept
createdAt: "2026-07-17T07:19:39.524Z"
updatedAt: "2026-07-17T07:19:39.524Z"
tags:
  - nanoparticles
  - tumor-targeting
  - protein-delivery
aliases:
  - tumour-selective-nanoparticle-protein-release-via-overlapping-np-and-phe-bf3-biodistribution
  - Phe-BF3 biodistribution and Tumour-selective nanoparticle protein release via overlapping NP
  - TNPRVONAPB
confidence: 0.95
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# Tumour-selective nanoparticle protein release via overlapping NP and Phe-BF3 biodistribution

Tumour-selective nanoparticle protein release via overlapping NP and Phe-BF3 biodistribution refers to a [[bioorthogonal]] delivery strategy in which a protein is first carried to tumours by a [[nanoparticle]] conjugate and then released inside tumour cells by [[Phe-BF3]]-mediated desilylation. In the source study, the authors combined a Phe-BF3-responsive silyl-ether carbamate linker with gold nanoparticle protein conjugates so that release occurred where nanoparticle accumulation and Phe-BF3 tumour uptake overlapped. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:30-32, a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:315-338, a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:339-355]

## Overview

The study established that Phe-BF3, a cancer PET imaging probe, can catalyse desilylation of a designed silyl-phenolic ether system in live cells. After optimization of the silyl group, the authors identified the triethylsilyl (TES) version as the most effective choice for this bioorthogonal release system and adapted it from small-molecule cargo to nanoparticle-bound proteins. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:42-64, a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:298-314]

For the nanoparticle implementation, the authors attached the silyl-phenolic ether linker to gold nanoparticles and replaced coumarin with [[GFP]] to create NP-GFP. In mammalian cells, TES-linked NP-GFP released GFP completely in response to Phe-BF3 or sodium fluoride in vitro, but only Phe-BF3 triggered release in cells because sodium fluoride was not cell-permeable. Released GFP regained fluorescence because separation from the nanoparticle removed quenching. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:320-338]

## Basis for tumour selectivity

The tumour selectivity of the system depended on two biodistribution features described in the study. First, nanoparticles were used because they have tumour preference owing to the enhanced permeability and retention effect and more efficient internalization by cancer cells. Second, Phe-BF3 itself showed tumour uptake and retention in mouse tumour models. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:315-320, a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:77-86, a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:339-342]

In BALB/c mice bearing subcutaneous [[4T1]] tumours, PET imaging showed tumour enrichment of [18F]Phe-BF3, while the remaining Phe-BF3 was rapidly cleared through renal excretion. In the same model, nanoparticle-conjugated [89Zr]GFP began accumulating in tumours by 6 hours after injection and reached a plateau by 18 hours. Although NP-[89Zr]GFP was also highly enriched in the liver, the study states that the distributions of NP-GFP and Phe-BF3 overlapped only in the tumour. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:339-347]

This overlap in biodistribution is presented as the reason protein release becomes tumour-selective. Because both components converge in the tumour, but not together in other tissues, the desilylation-triggered cleavage of the nanoparticle-protein conjugate is spatially favoured at the tumour site. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:345-355]

## In vivo demonstration of protein release

To detect release in tumours directly, the authors replaced GFP with the brighter fluorescent protein mNeonGreen and added a nuclear localization signal, generating NP-mNeonGreen-NLS. This design concentrated released fluorescence in nuclei after cleavage, making in vivo release easier to visualize in tumour sections. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:347-350, a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:1262-1273]

Control 4T1 tumours showed no mNeonGreen fluorescence, whereas tumours from mice given Phe-BF3 displayed nuclear mNeonGreen signal in about 15% of tumour cells. The authors conclude from these data that the Phe-BF3 desilylation system is compatible with nanoparticle-mediated delivery and shows tumour selectivity. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:351-355]

## Experimental implementation

The nanoparticle carrier in the study was a 60 nm water-soluble spherical gold nanoparticle decorated with PEG and DBCO groups. Protein cargoes were modified with an azide-bearing TESO-maleimide linker and then conjugated to the nanoparticles through the DBCO-PEG nanoparticle platform. The study prepared NP-GFP, NP-mNeonGreen-NLS, and NP-GSDMA3 using this approach. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:1159-1196]

For the in vivo mNeonGreen-NLS release assay, 4T1 tumour-bearing mice received intravenous NP-mNeonGreen-NLS on days 6, 9, and 12, followed by intravenous Phe-BF3 on days 7, 8, 10, 11, 13, and 14. Tumours were collected on day 15 and analysed by confocal microscopy after sectioning and staining. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:1262-1273]

## Relation to functional cargo delivery

The same tumour-selective release logic was then applied to a functional protein cargo, [[Gasdermin A3|GSDMA3]]. The study reports that NP-GSDMA3 showed biocompatibility and selective tumour targeting similar to NP-[89Zr]GFP, and transmission electron microscopy confirmed uptake and cytosolic distribution in 4T1 tumours. The authors state that the distributions of NP-GSDMA3 and Phe-BF3 also converged onto the tumour. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:493-500, a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:1628-1639]

After release from NP-GSDMA3 by Phe-BF3 desilylation, the gasdermin cargo remained capable of pore formation and induced [[pyroptosis]] in cultured cells and in tumours. In the 4T1 model, this application linked tumour-selective protein release to tumour regression and immune activation, showing the system’s utility beyond fluorescent reporting cargoes. ^[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:475-491, a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:502-516, a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis.md:633-652]

## Related concepts

- [[Bioorthogonal chemistry]]
- [[Phe-BF3]]
- [[Nanoparticle-mediated protein delivery]]
- [[Enhanced permeability and retention effect]]
- [[4T1]]
- [[GFP]]
- [[mNeonGreen]]
- [[Pyroptosis]]
- [[Gasdermin A3|GSDMA3]]

## Sources

- [[a-bioorthogonal-system-reveals-antitumour-immune-function-of-pyroptosis]]
