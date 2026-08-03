---
title: Distinguishing ferroptosis from apoptosis by organelle morphology and CQPP imaging
summary: CQPP-assisted dual-organelle imaging shows LD polarity changes in ferroptosis while nuclear morphology remains largely unchanged, whereas apoptosis produces obvious nuclear condensation and lifetime changes.
sources:
  - polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md
kind: concept
createdAt: "2026-07-17T09:55:33.401Z"
updatedAt: "2026-07-17T09:55:33.401Z"
tags:
  - apoptosis
  - ferroptosis
  - comparative-imaging
aliases:
  - distinguishing-ferroptosis-from-apoptosis-by-organelle-morphology-and-cqpp-imaging
  - CQPP imaging and Distinguishing ferroptosis from apoptosis by organelle morphology
  - DFFABOMACI
confidence: 0.91
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# Distinguishing ferroptosis from apoptosis by organelle morphology and CQPP imaging

[[Ferroptosis]] and [[apoptosis]] can overlap in some single-organelle morphological features, which makes it difficult to distinguish them using only one subcellular readout. The source therefore frames in situ detection of multiple organelles, especially [[lipid droplets]] (LDs) and the nucleus, as important for accurately monitoring the occurrence and progression of ferroptosis. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:119-143]

The paper notes that ferroptotic cells show characteristic subcellular changes documented by electron microscopy: after treatment with ferroptosis inducers such as erastin or RSL3, mitochondria show noticeable morphological alteration and loss of structural integrity, while nuclear structure is retained, with no nuclear condensation or chromatin margination observed after erastin treatment in cancer cells. In contrast, the authors explicitly state that ferroptosis does not involve nucleus change, whereas apoptosis does. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:111-128]

To address this distinction, the study developed `CQPP`, described as the first LD- and nucleus-dual-targeted ratiometric fluorescent probe for monitoring polarity change in the cellular microenvironment. The probe was designed to visualize LDs and the nucleus in separate channels and to report polarity changes through both ratiometric fluorescence emission and [[fluorescence lifetime imaging|FLIM]]. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:46-58, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:154-171, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:446-458]

In living HT-1080 cells, CQPP showed green emission in the cytoplasm that localized mainly to LDs and red emission in the nucleus. Co-localization experiments gave a Pearson correlation coefficient of `0.92` with the LD marker `BODIPY 493/503` for the green channel and `0.91` with `Hoechst 33342` for the red channel, supporting its dual-organelle targeting. The large emission separation also allowed simultaneous dual-color imaging of LDs and nucleus under the same excitation conditions. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:304-339]

Using CQPP in ferroptosis models, the authors observed that LDs had lower polarity than the surrounding cytoplasm under baseline conditions, with a polarity gradient from LD core to surface. After erastin treatment, green LD fluorescence decreased and red cytoplasmic fluorescence increased slightly, indicating increased LD polarity. In a time-dependent `RSL3` model, punctate LD protrusions gradually diffused into the cytoplasm, and the polarity gradient became less obvious as polarity became more homogeneous between LDs and cytoplasm. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:343-385]

At the same time, CQPP-based nucleus monitoring supported discrimination from apoptosis. During erastin- or RSL3-associated ferroptosis imaging, the nucleus morphology and red nuclear fluorescence did not change obviously, and characteristic apoptotic nuclear events such as chromatin agglutination, nuclear membrane fragmentation, and DNA degradation were not observed. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:362-365, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:372-377]

FLIM provided a second, quantitative way to separate the two death states. In untreated cells, CQPP lifetimes formed two regions: `0.5-1.5 ns` in the cytoplasm, corresponding to LD-associated probe, and `1.5-2.5 ns` in the nucleus, corresponding to DNA-bound probe; fitted values for representative LD and nuclear regions were `1.46 ns` and `2.11 ns`, respectively. After `6 h` of erastin treatment, a new short-lifetime peak around `0.79 ns` appeared in the LD-associated region, while the nuclear `1.5-2.5 ns` lifetime region did not change obviously, consistent with increased LD polarity during ferroptosis without major nuclear alteration. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:406-425]

By contrast, in apoptotic cells treated with `cisplatin` for `12 h`, the source reports obvious changes in nuclear morphology and nuclear fluorescence lifetime, attributed to nuclear condensation and chromatin margination, while LD changes were not obvious. The authors therefore used CQPP nuclear lifetime as a reference: ferroptosis was associated with progressive LD polarity increase and relatively stable nuclear readouts, whereas apoptosis produced marked nuclear morphological and lifetime changes. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:426-435]

Overall, the study presents CQPP imaging as a way to distinguish ferroptosis from apoptosis by combining two signals: LD polarity remodeling during ferroptosis and the absence or presence of nuclear change. In this framework, ferroptosis is characterized by increased LD polarity and increasing polarity homogeneity between LDs and cytoplasm while nuclear structure remains largely unchanged, whereas apoptosis is marked by clear nuclear condensation-related changes detectable morphologically and by FLIM. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:123-143, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:380-385, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:446-460]

## Related concepts

- [[Ferroptosis]]
- [[Apoptosis]]
- [[Lipid droplets]]
- [[Fluorescence lifetime imaging|FLIM]]
- [[Ratiometric fluorescence imaging]]
- [[CQPP]]

## Sources

- [[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis]]
