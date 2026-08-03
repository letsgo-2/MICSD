---
title: TPATrzPy-3+ as a mitochondria-targeting AIE photosensitizer synthesized from inert precursors
summary: The active product TPATrzPy-3+ is rationally designed as a positively charged donor-acceptor AIE photosensitizer with mitochondrial targeting, whereas its two precursors are largely photochemically inert and weak ROS generators.
sources:
  - cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md
kind: concept
createdAt: "2026-07-17T08:09:23.819Z"
updatedAt: "2026-07-17T08:09:23.819Z"
tags:
  - photosensitizers
  - aggregation-induced-emission
  - mitochondria
  - molecular-design
aliases:
  - tpatrzpy-3-as-a-mitochondria-targeting-aie-photosensitizer-synthesized-from-inert-precursors
  - TAAMAPSFIP
confidence: 0.97
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# TPATrzPy-3+ as a mitochondria-targeting AIE photosensitizer synthesized from inert precursors

TPATrzPy-3+ is a mitochondria-targeting [[aggregation-induced emission|AIE]] photosensitizer developed for precise [[photodynamic therapy|PDT]] through cancer-cell-activated in situ synthesis. In the study, it was designed to be formed selectively inside cancer cells from two photochemically inert precursors, `TPA-alkyne-2+` and `MePy-N3`, via a click reaction catalyzed by Cu(I) generated from glutathione-reduced [[MOF-199]]. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:41-52, cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:156-175]

## Design rationale

The photosensitizer was designed to address two problems in PDT: nonspecific uptake of photosensitizers in normal tissues and the difficulty of combining activatable behavior with mitochondrial targeting. The authors proposed that generating the active photosensitizer only inside cancer cells could reduce off-target phototoxicity, while mitochondrial localization could enhance cell killing because ROS-mediated mitochondrial damage readily induces apoptosis. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:54-85, cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:86-103]

TPATrzPy-3+ was rationally designed to include a diphenylamine donor, a triazole acceptor-related unit, a pyridinium unit, and two propyl chains ending in quaternary ammonium groups. According to the source, this donor-acceptor structure favors HOMO-LUMO separation and a small singlet-triplet energy gap, while the cationic pyridinium and quaternary ammonium groups provide water solubility and support mitochondrial targeting. The triphenylamine-containing structure was also expected to confer AIE behavior. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:177-213]

The precursors were intentionally designed to remain photochemically inert relative to the final product. The source states that `TPA-alkyne-2+` lacks an acceptor and `MePy-N3` lacks a donor, which results in negligible ROS generation by the individual precursors and helps keep toxicity low during delivery to the tumor region. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:208-213]

## Optical and photosensitizing properties

After conjugation of the two precursors, TPATrzPy-3+ showed an absorption peak at `400 nm` and an emission peak at `595 nm` in water, both red-shifted relative to `TPA-alkyne-2+`, which absorbed at `335 nm` and emitted at `440 nm`. Its emission intensity increased with higher toluene-methanol ratios, which the authors used to indicate AIE activity. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:229-243]

Using ABDA as a singlet-oxygen indicator under white light irradiation, the study found that TPATrzPy-3+ degraded ABDA at about `25 uM mL^-1`, similar to chlorin e6 (`Ce6`). By contrast, the two precursors each showed ABDA degradation rates below `5 uM mL^-1`, indicating much lower `^1O2` generation before conversion into TPATrzPy-3+. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:244-264]

## Synthesis from inert precursors

The reported synthesis strategy used [[MOF-199]] as both a carrier for the two precursors and a source of copper catalyst. The precursor-loaded material, `PMOF`, was made by loading `TPA-alkyne-2+` and `MePy-N3` into nanoscale MOF-199, then coating it with `F-127` to form `PMOF NPs` for improved dispersity and biocompatibility. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:45-48, cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:164-175, cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:265-323]

The source reports that glutathione reduced Cu(II) in MOF-199 to Cu(I), as supported by ESR analysis, and that GSH exposure also caused PMOF to lose crystallinity and collapse. This collapse released both precursors and copper ions in similar profiles, enabling Cu(I)-catalyzed click formation of TPATrzPy-3+ under GSH-rich conditions. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:268-277, cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:306-318, cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:342-364]

Only the MOF-loaded, GSH-treated precursor system produced the red emission centered around `595 nm` that matched TPATrzPy-3+, whereas free precursors treated with GSH did not. After GSH treatment, `PMOF NPs` also gained strong singlet-oxygen generation comparable to TPATrzPy-3+, while untreated `PMOF NPs` retained only the modest activity seen for the precursors. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:333-364]

## Cancer-cell-selective intracellular formation

The study used HeLa cells as a cancer-cell model and 3T3 cells as a normal-cell control. Measured intracellular glutathione levels were substantially higher in HeLa cells than in 3T3 cells, and the authors therefore treated GSH as the cancer-cell-specific trigger for PMOF activation. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:378-397]

Confocal imaging showed that TPATrzPy-3+ fluorescence colocalized with MitoTracker in PMOF-NP-treated HeLa cells and in cells directly treated with TPATrzPy-3+, indicating mitochondrial targeting. In contrast, TPATrzPy-3+ signal was almost indiscernible in HeLa cells treated only with free precursors, in HeLa cells pretreated with the GSH scavenger `BSO` before PMOF exposure, and in PMOF-treated or precursor-treated 3T3 cells. The source interprets these results as evidence that TPATrzPy-3+ synthesis is cancer-cell-specific and GSH-triggered. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:398-430]

HPLC analysis of HeLa cell lysates was used to track intracellular click synthesis over time. Based on the maximal endocytosed precursor amount, the reported intracellular TPATrzPy-3+ synthesis yield was `21.4%` at `8 h`, `61.2%` at `12 h`, `70.4%` at `16 h`, and `70.5%` at `24 h`, indicating that in vitro production was essentially complete by `16 h` after PMOF incubation. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:431-460]

## Photodynamic activity and selectivity

Under white-light irradiation, free precursors showed only minor toxicity in both HeLa and 3T3 cells, while TPATrzPy-3+ itself potently ablated both cell types with an `IC50` around `10 uM`. `PMOF NPs` showed a similar `IC50` in HeLa cells but inhibited light toxicity in 3T3 cells, indicating selective killing of cancer cells over normal cells after intracellular activation. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:465-478]

Flow-cytometry analysis indicated that the activated cell ablation proceeded through a mitochondrial apoptotic pathway associated with efficient photosensitization by mitochondria-targeting TPATrzPy-3+. When HeLa cells were pretreated with `BSO` to lower intracellular GSH, the `IC50` of `PMOF NPs` increased to over `50 uM`, further supporting the dependence of activity on GSH-triggered in situ synthesis. No obvious dark toxicity was observed for the tested precursor, PMOF, or TPATrzPy-3+ conditions in either HeLa or 3T3 cells. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:487-498]

## In vivo evidence

In a `krasV12` transgenic zebrafish liver tumor model, red TPATrzPy-3+ fluorescence was absent in precursor-treated embryos but appeared in embryos treated with `PMOF NPs`, direct TPATrzPy-3+, or `TPATrzPy-3+@MOF NPs`. The PMOF-derived TPATrzPy-3+ signal was detected from `1 dpi` and was confined to the tumor region, whereas directly administered TPATrzPy-3+ or TPATrzPy-3+@MOF fluorescence appeared throughout the body. The authors interpret this as tumor-selective in vivo synthesis and delivery of TPATrzPy-3+ by PMOF NPs. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:507-567]

In the same zebrafish model, PDT with `PMOF NPs` reduced liver tumor volume by about `40%` on average, similar to direct TPATrzPy-3+ and `TPATrzPy-3+@MOF NPs`, whereas tumors in precursor-treated, light-only, or untreated groups grew by roughly `40%` to `100%` over two days. Under light exposure, the embryo `LC50` was around `1 mM` for direct TPATrzPy-3+ and `TPATrzPy-3+@MOF NPs`, but `4 mM` for `PMOF NPs`, indicating reduced nonspecific light toxicity for the cancer-cell-activated system. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:568-590]

The study also reports that intravenously injected `PMOF NPs` caused negligible effects on normal organs and blood biochemistry in BALB/c nude mice at the tested dose, and pharmacokinetic analysis suggested degradation over time without a tendency to accumulate in the body. Together with the zebrafish results, the authors present these findings as support for effective and precise PDT with low systemic toxicity. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:591-608]

## Significance

Within this study, TPATrzPy-3+ serves as the active photosensitizer produced only after cancer-cell-triggered conversion of otherwise weakly photosensitizing precursors. Its combination of mitochondrial targeting, AIE fluorescence, efficient singlet-oxygen generation, and selective intracellular synthesis is presented as a way to support image-guided PDT with strong tumor ablation and reduced off-target phototoxicity. ^[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:610-649, cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy.md:760-768]

## Related concepts

- [[Photodynamic therapy]]
- [[Aggregation-induced emission]]
- [[MOF-199]]
- [[Glutathione]]
- [[Click reaction]]
- [[Singlet oxygen]]
- [[Mitochondria-targeting photosensitizers]]
- [[HeLa]]
- [[3T3]]
- [[Zebrafish tumor model]]

## Sources

- [[cancercellactivated-insitu-synthesis-of-mitochondriatargeting-aie-photosensitizer-for-precise-photodynamic-therapy]]
