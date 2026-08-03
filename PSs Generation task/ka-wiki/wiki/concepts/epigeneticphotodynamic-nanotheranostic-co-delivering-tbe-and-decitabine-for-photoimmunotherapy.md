---
title: Epigenetic/photodynamic nanotheranostic co-delivering TBE and decitabine for photoimmunotherapy
summary: The study builds a two-part nanotheranostic system in which ROS-responsive NP1 carries the photosensitizer TBE and liposomal NP2 carries decitabine, combining NIR imaging, photodynamic therapy, and epigenetic reprogramming for tumor-targeted photoimmunotherapy.
sources:
  - simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md
kind: concept
createdAt: "2026-07-17T10:50:07.874Z"
updatedAt: "2026-07-17T10:50:07.874Z"
tags:
  - nanotheranostics
  - photodynamic-therapy
  - epigenetics
  - cancer-immunotherapy
aliases:
  - epigeneticphotodynamic-nanotheranostic-co-delivering-tbe-and-decitabine-for-photoimmunotherapy
  - decitabine for photoimmunotherapy and Epigenetic/photodynamic nanotheranostic co-delivering TBE
  - ENCTADFP
confidence: 0.99
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# Epigenetic/photodynamic nanotheranostic co-delivering TBE and decitabine for photoimmunotherapy

This study describes a tumor-specific nanotheranostic platform that combines [[photodynamic therapy]], [[epigenetic therapy]], and near-infrared fluorescence imaging to enhance tumor [[photoimmunotherapy]]. The system uses two components: `NP1`, an oxidation-sensitive nanoparticle loaded with the photosensitizer `TBE`, and `NP2`, a liposomal carrier loaded with the DNA methyltransferase inhibitor `decitabine`. The stated goal was to convert immunologically "cold" breast tumors into more immunogenic "hot" tumors through light-controlled activation of [[pyroptosis]] and the [[cGAS-STING pathway]]. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:59-72, simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:110-132]

## Rationale

The paper frames the approach around two limits in solid-tumor immunotherapy: immunosuppressive tumor microenvironments and insufficient tumor immunogenicity. It presents [[pyroptosis]] as an immunogenic cell-death program driven by caspase-mediated cleavage of gasdermins, and the [[cGAS-STING pathway]] as an innate immune DNA-sensing pathway activated by cytosolic double-stranded DNA, including DNA released from dysfunctional mitochondria. The authors argue that existing pyroptosis inducers and STING agonists are constrained by issues such as poor bioavailability, systemic side effects, instability, or inadequate intracellular expression of `GSDME` and `STING`. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:74-109]

## Platform design and mechanism

In the proposed mechanism, decitabine released from `NP2` reverses promoter hypermethylation and restores intracellular expression of `GSDME` and `STING`. After light exposure, `TBE` released from `NP1` drives photodynamic reactive oxygen species production, which causes mitochondrial dysfunction and cytosolic release of mitochondrial DNA to stimulate [[cGAS-STING pathway|cGAS-STING signaling]]. The same photodynamic stress also activates caspase-3, which cleaves upregulated `GSDME` into the pore-forming `GSDME-N` fragment and thereby promotes pyroptosis. The study links these events to release of proinflammatory cytokines, maturation of [[dendritic cell|dendritic cells]] and [[natural killer cell|NK cells]], subsequent T-cell-mediated antitumor immunity, and long-term immune memory. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:122-132, simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:595-621]

## TBE and `NP1`

`TBE` was designed as a degradable pseudo-semiconducting polymer photosensitizer with broad absorption extending through the NIR-I region, a characteristic absorbance peak at `616 nm`, a minor peak at `741 nm`, and fluorescence emission in the NIR-II region peaking at `1037 nm`. Under `808 nm` irradiation, it efficiently generated singlet oxygen, with a reported singlet-oxygen yield `2.5-fold` higher than the commercial photosensitizer `ICG`, while showing negligible photobleaching in the reported photostability test. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:149-189]

To build `NP1`, the authors assembled `TBE` with a ROS-sensitive polymer. `NP1` had a measured drug loading efficiency of `33.6 +/- 4.1%`, a uniform spherical morphology, and an average hydrodynamic diameter of `93.3 +/- 7.7 nm`. It remained stable for 7 days under physiological conditions but showed marked morphology changes after incubation in `10 mM H2O2`, consistent with ROS-responsive degradation. In `MCF-7` cells, `NP1` showed time-dependent uptake that plateaued after `7 h`. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:202-223]

Under `808 nm` irradiation, `NP1` increased intracellular ROS, reduced mitochondrial membrane potential, increased cleaved caspase-3 and cytosolic cytochrome c, and caused mitochondrial membrane permeabilization with cytosolic escape of mitochondrial DNA in `MCF-7` cells. `NP1` alone showed negligible cytotoxicity up to `20 ug/mL`, whereas `NP1` plus light produced marked tumor-cell growth inhibition with an `IC50` of `7.5 ug/mL` and increased apoptosis. However, despite caspase-3 activation and cytosolic DNA release, `NP1` plus light alone did not significantly upregulate the key proteins of pyroptosis or the cGAS-STING pathway. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:224-257]

## Why decitabine was added

The study analyzed breast cancer datasets and reports that `DFNA5` (`GSDME`) and `TMEM173` (`STING`) were downregulated in breast cancer tissues relative to normal tissues, with this downregulation strongly associated with promoter methylation. Based on that observation, the authors tested three DNA methyltransferase inhibitors in `MCF-7` cells and found that `20 uM` decitabine increased `GSDME` expression by `70.3%` and `STING` expression by `40.8%`, whereas azacytidine and `gamma-oryzanol` did not show evident effects. Decitabine was therefore selected for combination with `NP1`. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:284-316]

## `NP2`

To reduce systemic side effects and optimize epigenetic therapy, decitabine was incorporated into `DSPE-PEG2000` micelles to generate `NP2`. `NP2` had an encapsulation efficiency of `63.3 +/- 16.9%`, a uniform spherical morphology, and an average diameter of `155.5 +/- 2.7 nm`. It remained stable over 7 days and released substantially more decitabine at acidic `pH 5.0` (`84.37%`) than at `pH 7.4` (`38.15%`), which the authors attribute to protonation of amine groups and interpret as tumor-microenvironment-responsive release. Cellular uptake of labeled `NP2` increased over time and plateaued after `12 h`, and its capacity to restore `GSDME` and `STING` was reported to be similar to free decitabine. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:345-366]

## In vitro combined effects

In `MCF-7` cells, combining `NP2` with `NP1` plus light did not materially increase overall growth inhibition relative to `NP1` plus light alone, but it changed the mode of cell death. Compared with `NP1+L`, the `NP1+NP2+L` condition produced fewer apoptotic `Annexin V+ PI-` cells, more `Annexin V- PI+` cells interpreted as pyroptotic, and morphology characterized by cell swelling and large plasma-membrane bubbles rather than cell shrinkage and rounding. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:364-385]

This combination also increased `GSDME-N`, extracellular ATP, and released LDH, which the authors interpret as evidence that decitabine-enabled `NP2` converted `NP1+L`-induced apoptosis into pyroptosis. At the same time, phosphorylation of `STING`, `TBK1`, and `IRF3` increased, and flow cytometry plus confocal analysis supported activation of the [[cGAS-STING pathway]]. Conditioned effects from `NP1+NP2+L` also increased the proportion of `CD80+ CD86+` mature dendritic cells, consistent with enhanced tumor-cell immunogenicity. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:375-406]

## In vivo distribution and antitumor activity

In orthotopic `4T1` tumor-bearing `BALB/c` mice, `NP1` accumulated progressively in tumors after injection and reached a fluorescence plateau at `24 h`, which was then used as the irradiation time point. Ex vivo imaging showed tumor fluorescence greater than spleen and kidney fluorescence, while the liver showed the highest signal overall, suggesting it was the main site of metabolism and clearance. Pharmacokinetic testing further indicated that `NP1` circulated longer than free `TBE`, with an `AUC0-48` `2.99-fold` higher than free `TBE`. `NP2` showed a different profile, reaching a tumor fluorescence plateau by `1 h` and then remaining retained, with the liver and kidneys identified as major clearance sites. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:434-462]

For efficacy testing, mice were assigned to `PBS`, `NP1`, `NP1+L`, `NP1+NP2`, or `NP1+NP2+L`. After `15` days, `PBS` and `NP1` groups showed about `5.7-fold` tumor-volume increase, and `NP1+NP2` still showed strong growth (`4.8-fold`). `NP1+L` achieved `29.8%` tumor inhibition, while `NP1+NP2+L` showed the strongest response, with a reported tumor regression rate of `70.9%`. Tumor weight, tumor photographs, TUNEL staining, and H&E staining supported the superior antitumor effect of `NP1+NP2+L`, while body weight, serum biochemistry, and organ histology did not show evident safety signals in the reported experiments. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:463-490]

## In vivo immune effects

Tumor analysis after treatment showed that `NP1+NP2+L` increased phosphorylation of `STING`, `TBK1`, and `IRF3` and increased tumor `GSDME-N` expression relative to comparison groups. Immunofluorescence also showed increased phosphorylation and nuclear translocation of `IRF3`. Serum `TNF-alpha`, `IL-6`, and `IFN-beta` were all higher in the `NP1+NP2+L` group, including a higher level of `IFN-beta`, which the paper identifies as a key downstream product of STING signaling. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:514-535]

The same treatment increased mature dendritic cells in tumor-draining lymph nodes and tumors, increased tumor-infiltrating [[natural killer cell|NK cells]], and raised both `CD8+` and `CD4+` tumor-infiltrating T-cell percentages. It also produced a `12.8-fold` increase in tumor-infiltrating `IFN-gamma+ CD8+` T cells relative to `PBS`, while reducing [[myeloid-derived suppressor cell|MDSCs]] and [[regulatory T cell|Treg]] infiltration. In spleen, the percentages of [[effector memory T cell|TEM]] and [[central memory T cell|TCM]] populations increased, which the authors interpret as evidence of long-term antitumor immune memory. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:536-571]

## Significance

The paper presents the co-delivery of `TBE` and decitabine as a photo-controllable strategy that links [[photodynamic therapy]], [[epigenetic therapy]], [[pyroptosis]], and [[cGAS-STING pathway|STING signaling]] in a single nanotheranostic framework. In the authors' interpretation, restoring `GSDME` and `STING` expression with decitabine allows photodynamic mitochondrial damage and caspase-3 activation to translate into coordinated pyroptosis, innate immune activation, T-cell-mediated antitumor immunity, and immune memory, while `TBE` also supports NIR fluorescence imaging guidance. ^[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:595-621, simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy.md:781-785]

## Related concepts

- [[Photodynamic therapy]]
- [[Photoimmunotherapy]]
- [[Epigenetic therapy]]
- [[Pyroptosis]]
- [[cGAS-STING pathway]]
- [[Decitabine]]
- [[GSDME]]
- [[STING]]
- [[Dendritic cell]]
- [[Natural killer cell|NK cell]]
- [[Cytotoxic T cell]]
- [[Myeloid-derived suppressor cell|MDSC]]
- [[Regulatory T cell|Treg]]
- [[Effector memory T cell|TEM]]
- [[Central memory T cell|TCM]]
- [[4T1]]
- [[MCF-7]]
- [[BALB/c]]

## Sources

- [[simultaneous-activation-of-pyroptosis-and-cgassting-pathway-with-epigenetic-photodynamic-nanotheranostic-for-enhanced-tumor-photoimmunotherapy]]
