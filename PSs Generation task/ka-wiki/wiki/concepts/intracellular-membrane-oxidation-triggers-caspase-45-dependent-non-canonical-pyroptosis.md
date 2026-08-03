---
title: Intracellular membrane oxidation triggers caspase-4/5-dependent non-canonical pyroptosis
summary: The central mechanism proposed is that BTP-driven intracellular membrane oxidation activates non-canonical inflammasome caspases 4 and 5 rather than caspase-1, leading to GSDMD cleavage, ATP release, lytic morphology, and pyroptotic death.
sources:
  - oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md
kind: concept
createdAt: "2026-07-17T09:28:52.676Z"
updatedAt: "2026-07-17T09:28:52.676Z"
tags:
  - pyroptosis
  - caspase-4
  - gasdermin-d
aliases:
  - intracellular-membrane-oxidation-triggers-caspase-45-dependent-non-canonical-pyroptosis
  - IMOTCNP
confidence: 0.99
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# Intracellular membrane oxidation triggers caspase-4/5-dependent non-canonical pyroptosis

Intracellular membrane-focused oxidation was reported in this study to trigger [[non-canonical pyroptosis]] through activation of [[caspase-4]] and [[caspase-5]], leading to [[Gasdermin D|GSDMD]] cleavage and lytic cell death. The authors used an amphiphilic organic photocatalyst, `BTP`, that localizes near intracellular membranes and generates reactive oxidizing species under light exposure to examine how oxidative damage to membrane proteins affects cell-death signaling. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:29-45, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:116-170]

## Overview

The paper presents intracellular membrane oxidation as a stimulus that primarily damages membrane proteins rather than driving strong cellular lipid oxidation. In the authors' model, this oxidation particularly affects proteins linked to [[protein quality control]], aggravates stress in the [[endoplasmic reticulum]], [[Golgi apparatus]], and [[mitochondria]], mobilizes intracellular cations, and ultimately activates caspase-4/5-dependent pyroptotic execution. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:39-45, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:154-170, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:459-494, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:495-527, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:678-692]

## Experimental basis

To induce intracellular membrane-focused oxidation, the study developed `BTP`, an amphiphilic photocatalyst with a fatty acid-like design. BTP localized in intracellular membrane environments and, upon light activation, generated `H2O2` and hydroxyl radicals from water oxidation; this process was reported to be enhanced under hypoxia. The authors state that BTP did not produce singlet oxygen in their assays. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:116-125, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:149-160, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:183-246]

Cellular localization experiments in HeLa cells placed BTP initially in the [[Golgi apparatus]] and [[endoplasmic reticulum]], with emission behavior consistent with proximity to intracellular membranes. ROS-sensitive assays further indicated increased oxidative stress and superoxide generation after BTP photocatalysis. In contrast, lipid analysis did not detect newly generated oxidized lipid peaks and did not show a changed oxidation ratio for `15:0-18:1 phosphatidylcholine`, leading the authors to conclude that lipid oxidation was comparatively inefficient in this cellular context. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:251-286, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:292-313]

## Membrane protein oxidation and proteostasis stress

The study directly tested membrane protein damage using the model membrane protein `GlpG`. Under BTP plus blue light, gel-band intensity for GlpG decreased while higher-molecular-weight aggregates increased, and thermal denaturation resistance dropped markedly, with the transition midpoint temperature decreasing from `75 °C` to `35 °C` at `150 uM` BTP. Single-molecule magnetic tweezer measurements further showed a sharp drop in unfolding force after photocatalysis that did not recover with fresh bicelles, which the authors interpret as irreversible oxidative destabilization of the membrane protein fold. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:314-411]

Proteomic analysis in HeLa cells supported a membrane-centered pattern of oxidation. In the initial methionine-oxidation screen, oxidized proteins were more common among membrane-specific proteins than cytosolic proteins (`339` versus `40`; `24.5%` versus `3.6%`). A broader search across oxidized amino acids again found membrane-specific proteins to be the most oxidized class. Among a conservatively defined set of `250` oxidized membrane proteins, many localized to the ER, mitochondria, nucleus, and Golgi, and `58.1%` belonged to the ER, Golgi, and mitochondria, organelles highlighted as central to protein quality control. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:414-474]

Within those oxidized proteins, the authors emphasize functional networks related to unfolded protein response and ER-associated degradation, ER-Golgi transport, mitochondrial trafficking and transport, and lipid metabolism. They interpret this pattern as evidence that oxidation of membrane proteins disrupts [[protein quality control]], promotes misfolded-protein accumulation, and escalates [[unfolded protein response|UPR]] stress. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:469-494]

## Cation mobilization and organelle dysfunction

The source links this proteostasis disruption to cation mobilization. After BTP photocatalysis, mitochondrial `Ca2+` increased as measured with Rhod-2, mitochondrial swelling with fission and fusion was observed, and `TMRE` fluorescence fell, indicating loss of mitochondrial membrane potential. The study also detected intracellular `K+` efflux by flow cytometry. The authors summarize these changes as maladaptive UPR and cation mobilization in response to oxidative damage on intracellular membranes. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:495-527]

## Evidence for pyroptotic cell death

BTP photocatalysis caused extensive cell death in HeLa cells within `24 h` and was also strongly toxic in hypoxic pancreatic cancer cell lines, which the paper attributes to increased hydroxyl-radical generation under hypoxia. Morphologically, treated cells showed lytic swelling and abnormal blebbing consistent with [[pyroptosis]], and LDH release exceeded that seen with `LPS + nigericin` or the photosensitizer `Ce6`. Early propidium iodide entry into cells without immediate nuclear-envelope collapse further supported rapid plasma-membrane damage. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:566-585]

The authors distinguished this death program from [[ferroptosis]] by inhibitor testing. The pan-caspase inhibitor `z-VAD-fmk` reduced LDH release and suppressed blebbing and propidium iodide penetration, whereas `Liproxstatin-1` was less effective. Based on these results, the paper concludes that BTP-triggered lytic death depends on caspase activation more than lipid peroxidation. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:639-652]

## Caspase-4/5-dependent non-canonical pyroptosis

Mechanistically, the core pyroptotic evidence was [[Gasdermin D|GSDMD]] activation. BTP photocatalysis increased detection of the pore-forming `GSDMD-NT` fragment in both cell lysates and cell media. In immortalized bone marrow-derived macrophages, pyroptotic morphology and LDH release were abolished in `GSDMD-/-` cells compared with wild-type controls, showing that the lytic response required GSDMD. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:653-662, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:720-738]

Western blot analysis showed cleavage of caspase-4/5 rather than caspase-1 after BTP photocatalysis. Consistent with this, the study confirmed ATP secretion associated with caspase-4/5 and GSDMD activation, but did not observe efficient secretion of cleaved `IL-18` or `IL-1beta`, which the authors attribute to the lack of active caspase-1. On that basis, the paper identifies the response as caspase-4/5-dependent [[non-canonical pyroptosis]]. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:663-676]

## Proposed mechanism

In the authors' proposed sequence, BTP-driven oxidation damages membrane proteins and destabilizes their folding, especially in protein quality control-related membranes of the ER, Golgi, and mitochondria. This promotes accumulation of misfolded proteins, ER stress, maladaptive UPR, mitochondrial dysfunction, and cation mobilization, which are then linked to activation of caspase-4/5, GSDMD cleavage, and pyroptosis. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:495-527, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:673-676, oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:678-692]

The discussion further frames this pathway as an endotoxin-independent route to pyroptosis initiated by intracellular membrane-focused oxidative stress rather than microbial stimuli. The authors also note that the effect remains operative under hypoxia, which they highlight as potentially relevant for cancer settings. ^[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis.md:693-750]

## Related concepts

- [[Pyroptosis]]
- [[Non-canonical pyroptosis]]
- [[Caspase-4]]
- [[Caspase-5]]
- [[Gasdermin D|GSDMD]]
- [[Protein quality control]]
- [[Unfolded protein response|UPR]]
- [[Endoplasmic reticulum stress]]
- [[Mitochondrial dysfunction]]
- [[Oxidative stress]]
- [[Ferroptosis]]

## Sources

- [[oxidative-photocatalysis-on-membranes-triggers-non-canonical-pyroptosis]]
