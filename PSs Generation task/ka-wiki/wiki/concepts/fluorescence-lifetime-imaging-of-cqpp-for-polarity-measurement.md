---
title: Fluorescence lifetime imaging of CQPP for polarity measurement
summary: CQPP also shows polarity-dependent fluorescence lifetime changes, making it usable for FLIM-based microenvironment sensing.
sources:
  - polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md
kind: concept
createdAt: "2026-07-17T09:54:04.569Z"
updatedAt: "2026-07-17T09:54:04.569Z"
tags:
  - fluorescence-lifetime-imaging
  - polarity-sensing
  - bioimaging
aliases:
  - fluorescence-lifetime-imaging-of-cqpp-for-polarity-measurement
  - FLIOCFPM
confidence: 0.97
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# Fluorescence lifetime imaging of CQPP for polarity measurement

CQPP is a dual-targeted ratiometric fluorescence probe designed to monitor polarity changes in cellular microenvironments, with fluorescence lifetime imaging (FLIM) used alongside emission imaging to quantify polarity in living cells. The probe’s donor-acceptor structure gives it polarity-sensitive fluorescence lifetime and emission responses, and the authors applied this behavior to track lipid droplet (LD) polarity changes during ferroptosis. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:49-59, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:212-215, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:406-410]

## Probe design

CQPP was built as a lipophilic coumarin donor joined to a cationic quinoline acceptor, giving it LD and nucleus dual-targeting properties. The design aimed to combine polarity sensitivity with nucleic-acid binding so the nucleus could serve as an internal reference while LD polarity was measured. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:145-168, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:446-457]

## Fluorescence lifetime response

In mixed 1,4-dioxane/H2O media, CQPP showed a decrease in fluorescence lifetime as polarity increased. The lifetime fell from 1.49 ns in 1,4-dioxane to 0.63 ns in water, and from 1.49 ns to 0.89 ns across the dielectric range tested, supporting its use as a polarity sensor. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:218-267]

CQPP also responded to nucleic acids with a much longer lifetime. In the presence of ds26DNA, the lifetime increased from 0.63 ns to 2.10 ns, and the authors used this nucleus-associated signal as a reference when interpreting cellular FLIM images. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:268-283, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:410-419]

## Cellular FLIM measurement

In HT-1080 cells, FLIM separated CQPP into two lifetime regions: 0.5-1.5 ns in the cytoplasm, corresponding to LDs, and 1.5-2.5 ns in the nucleus, corresponding to DNA-bound probe. The measured lifetimes in untreated cells were 1.46 ns for the LD-associated region and 2.11 ns for the nucleic-acid-associated region. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:406-419]

After erastin treatment, a new short-lifetime peak appeared around 0.79 ns, with the strongest changes in the LD-associated region, indicating increased LD polarity during ferroptosis. Under apoptotic conditions induced by cisplatin, the nucleus lifetime changed markedly while LD changes were less obvious, helping distinguish ferroptosis from apoptosis. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:420-435]

## Interpretation

The study concludes that CQPP can monitor LD polarity changes by both fluorescence emission and FLIM, and that using the nucleus lifetime as a reference makes the LD polarity increase during ferroptosis clearer. The authors also report that CQPP’s nucleic-acid binding helps distinguish ferroptosis from apoptosis. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:445-460]

## Related concepts

- [[Fluorescence lifetime imaging]]
- [[Polarity-sensitive fluorescent probe]]
- [[Lipid droplets]]
- [[Nucleus]]
- [[Ferroptosis]]
- [[Ratiometric fluorescence imaging]]
- [[HT-1080]]
- [[Erastin]]
- [[RSL3]]
- [[Apoptosis]]

## Sources

- [[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis]]
