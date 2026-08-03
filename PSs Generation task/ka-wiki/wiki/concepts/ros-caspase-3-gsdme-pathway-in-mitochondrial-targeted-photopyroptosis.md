---
title: ROS-caspase-3-GSDME pathway in mitochondrial-targeted photopyroptosis
summary: The study supports a mechanism where mitochondrial ROS generated during irradiation activates caspase-3, producing GSDME-N and thereby driving photopyroptotic cell death.
sources:
  - a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md
kind: concept
createdAt: "2026-07-17T07:30:24.162Z"
updatedAt: "2026-07-17T07:30:24.162Z"
tags:
  - ros
  - caspase-3
  - gsdme
  - mechanism
aliases:
  - ros-caspase-3-gsdme-pathway-in-mitochondrial-targeted-photopyroptosis
  - RPIMP
confidence: 0.97
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# ROS-caspase-3-GSDME pathway in mitochondrial-targeted photopyroptosis

The **ROS-caspase-3-GSDME pathway in mitochondrial-targeted photopyroptosis** is the mechanism described in the source for how a mitochondria-localized photosensitizer triggers [[photopyroptosis]] after light irradiation. In this study, the proposed design places cationic moieties onto a photosensitive core so the molecule can target both the inner and outer mitochondrial membranes, maximize local photogenerated reactive oxygen species ([[ROS]]), and thereby activate [[Gasdermin E|GSDME]]-mediated pyroptosis. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:19-31, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:112-134]

The paper explicitly presents the photopyroptotic route as a photoproduced ROS-caspase-3-GSDME pathway. It frames mitochondrial targeting as the upstream requirement: strong electrostatic interactions help the photosensitizer accumulate at mitochondria, where ROS generation is concentrated at the relevant site for triggering pyroptosis rather than other cell-death outcomes. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:98-101, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:106-121]

## Upstream design logic

According to the source, the molecular design relies on cationic groups such as pyridinium or imidazolium attached to one photosensitive core. This arrangement is intended to strengthen electrostatic interactions with mitochondria and support access to both mitochondrial membranes. The authors argue that this localization centralizes ROS photoproduction and improves the efficiency of pyroptosis induction. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:115-129, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:537-547]

Control comparisons are used to support that design logic. Compounds that retained photosensitive cores but lacked the same cationic periphery generated singlet oxygen under irradiation yet did not show the same pyroptotic phenomena, which the authors attribute to weaker mitochondrial targeting. The study therefore links photopyroptosis efficiency not just to ROS generation in general, but to ROS generation from a sufficiently mitochondria-targeted reagent. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:203-214, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:227-242]

## Mitochondrial localization and ROS generation

In the representative molecule `1d`, colocalization experiments showed strong mitochondrial targeting, with a Pearson correlation coefficient of `0.91` relative to Mito-Tracker Red. Higher-resolution HIS-SIM imaging further indicated that `1d` localized simultaneously to the inner and outer mitochondrial membranes. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:243-259]

After irradiation, intracellular ROS increased strongly in the `1d + L` group, where DCFH-DA fluorescence was reported to be more than 16-fold higher than in the non-irradiated `1d` group. The source states that because the molecular structure of `1d` did not change before and after irradiation, ROS photoproduction was the dominant factor, and the substantial mitochondrial targeting caused centralized ROS production from mitochondria that benefited the subsequent pyroptotic trigger. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:260-279]

The study also examined ROS identity during photodynamic treatment. Pretreatment with `NaN3` and `Tiron`, described as scavengers for singlet oxygen and superoxide anion respectively, caused only a slight decrease in cell viability, which the authors interpret to mean that `^1O2` and `·O2−` accounted for the main part of the total ROS induced by `1d`. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:279-284]

## Mitochondrial damage and early cell-death changes

The source reports several changes consistent with mitochondrial injury after irradiation. Bio-TEM showed obvious cell membrane fragmentation in cells treated with `1d` and light, while JC-1 measurements indicated loss of mitochondrial membrane potential. Additional observations included nuclear shrinkage, outflow of cellular contents, and destruction of mitochondrial internal structure. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:318-335]

Biochemical measurements also supported progression toward cell death. Compared with control and dark `1d` groups, the `1d + L` group showed significantly higher LDH release, reduced intracellular ATP activity, and increased extracellular ATP content. The source presents these changes alongside the mitochondrial ROS findings as part of the photopyroptotic process. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:286-293]

## Caspase-3 and GSDME activation

A key mechanistic result in the study is that the irradiated `1d + L` group showed high caspase-3 levels together with obvious `GSDME-N` expression, whereas the control and dark `1d` groups did not show significant differences in caspase-3 or GSDME protein levels. The authors interpret this as evidence that irradiation activates pyroptosis through caspase-3-dependent cleavage of [[Gasdermin E|GSDME]]. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:340-347]

The source further notes that effector caspase-3 can drive explosive feedback amplification of upstream cell-death events and suggests that this may be a key factor underlying the efficiency of the process. It also states that although caspase-3 is commonly regarded as a hallmark of apoptosis, in this system ROS-induced caspase-3 is used to cleave GSDME, and that GSDME cleavage uniquely causes pyroptosis. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:345-347, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:381-388]

## Pyroptotic phenotype and efficiency

Morphologically, the pathway culminated in classic pyroptotic changes. In multiple tumor cell lines, cells treated with `1d` and irradiated with `640 nm` light showed swelling, membrane bubbling, and eventual rupture. Under confocal laser irradiation, bubbling could begin within `10 s`, and the process continued even after the laser was turned off. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:356-363]

Flow-cytometry analysis with annexin V and propidium iodide showed a progressively increasing pyroptotic population after irradiation, with most EMT-6 cells becoming double-positive within `5 h`. The source describes this as evidence that the majority of cells entered pyroptosis under the reported conditions and emphasizes that the required light dosage could be as low as `0.4 J cm−2` for triggering the process under CLSM laser conditions. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:364-380, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:548-549]

The study also visualized the process dynamically through the fluorescence of `1d`. The signal first marked mitochondrial localization, then spread through the cytoplasm after loss of mitochondrial membrane potential, then shifted toward the nucleus as membrane integrity failed, and finally became quenched after loss of cellular contents. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:389-401]

## Immune-related consequences

The source links this pathway to inflammatory and anti-tumor immune effects. HMGB-1 was upregulated in the irradiated group, and the introduction states that pyroptosis-induced inflammation can provoke anti-tumor immune responses. Transcriptomic analysis further showed upregulation of immune-related genes in the `1d + L` group, with enrichment in pathways including `IL-17`, `TNF`, and `NOD-like receptor` signaling. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:55-62, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:335-339, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:402-429]

In vivo, tumor sections from the `1d + L` group showed cleaved caspase-3 and `GSDME` N-terminal signals, while blood and tumor analyses indicated stronger inflammatory and immune activation, including increased white blood cells, granulocytes, lymphocytes, monocytes, and higher proportions of `CD4+` and `CD8+` T cells. The authors present these findings as evidence that the ROS-caspase-3-GSDME photopyroptosis pathway can contribute to effective tumor immunotherapy using the synthetic molecule alone. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:499-523]

## Interpretation in the study

Within this paper, the ROS-caspase-3-GSDME pathway is presented as the mechanistic basis for highly efficient [[mitochondrial-targeted photodynamic therapy]]-driven pyroptosis. The proposed sequence is: mitochondrial localization of the photosensitizer, localized ROS generation upon irradiation, mitochondrial damage and membrane-potential loss, activation of caspase-3, cleavage of GSDME to `GSDME-N`, and rapid pyroptotic membrane disruption with downstream immune activation. ^[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:98-101, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:243-347, a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation.md:537-554]

## Related concepts

- [[Photopyroptosis]]
- [[Reactive oxygen species]]
- [[Caspase-3]]
- [[Gasdermin E|GSDME]]
- [[Mitochondrial-targeted photodynamic therapy]]
- [[Mitochondrial membrane potential]]
- [[HMGB1]]
- [[Antitumor immunity]]

## Sources

- [[a-general-molecular-structural-design-for-highly-efficient-photopyroptosis-that-can-be-activated-within-10-s-irradiation]]
