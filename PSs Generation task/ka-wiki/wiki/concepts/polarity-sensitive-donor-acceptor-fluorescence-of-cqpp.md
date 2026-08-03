---
title: Polarity-sensitive donor-acceptor fluorescence of CQPP
summary: CQPP uses a donor-π-acceptor structure that shifts from green to red emission as polarity increases, enabling ratiometric fluorescence readout.
sources:
  - polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md
kind: concept
createdAt: "2026-07-17T09:53:43.369Z"
updatedAt: "2026-07-17T09:53:43.369Z"
tags:
  - photophysics
  - polarity-sensing
  - donor-acceptor
aliases:
  - polarity-sensitive-donor-acceptor-fluorescence-of-cqpp
  - PDFOC
confidence: 0.98
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# Polarity-sensitive donor-acceptor fluorescence of CQPP

`CQPP` is a polarity-sensitive fluorescent probe built around a donor-π-acceptor (`D-π-A`) architecture. In the reported design, a coumarin unit serves as the donor and a cationic quinolinium unit serves as the acceptor, enabling the probe to respond to microenvironment polarity while also supporting dual targeting of [[lipid droplets]] and the [[cell nucleus|nucleus]]. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:154-168]

## Design principle

The source states that fluorophores with `D-π-A` molecular structures are sensitive to solvent polarity changes, and that increasing environmental polarity usually produces a red shift in fluorescence emission. CQPP was designed on this basis so that its donor-acceptor structure could translate polarity changes into measurable optical changes. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:154-159]

In CQPP, the coumarin and cationic quinolinium units were combined to create a `D-π-A` probe for simultaneous visualization of lipid droplets and the nucleus and for monitoring polarity changes in the cellular microenvironment. The design also included an extended aromatic system with a `1-(pyridin-4-yl)piperazine` group, which the authors state may improve nucleic-acid binding and enhance ratiometric fluorescent behavior for sensitive polarity detection. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:160-168]

## Fluorescence behavior

CQPP showed similar absorption peaks near `295 nm` and `540 nm` in both `1,4-dioxane` and `DMSO`, but very different emission maxima under the same excitation (`405 nm`): about `467 nm` in `1,4-dioxane` and `671 nm` in `DMSO`. As solvent polarity increased, the emission near `470 nm` decreased while a new emission near `670 nm` appeared and strengthened, indicating polarity-dependent spectral redistribution. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:190-197]

The paper attributes the long-wavelength absorption band to strong [[intramolecular charge transfer]] (`ICT`) from the coumarin donor to the cationic quinolinium acceptor, based on `DFT` calculations. It further states that the dual fluorescence observed in different media arises from an equilibrium between a locally excited (`LE`) state and an `ICT` state. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:204-215]

Because CQPP contains a polarity-sensitive donor-acceptor unit, increasing polarity reduces `LE` emission and enhances `ICT` emission, producing a ratiometric fluorescence response. In mixed `H2O/1,4-dioxane` solvents, increasing water content from `0%` to `20%` gradually quenched the `~470 nm` signal and increased the `~670 nm` signal, with a noticeable color transition from green to red and a reported Lorentz-function correlation between the intensity ratio `I470/I670` and solvent polarity. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:212-215, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:223-250]

The authors also report that this ratiometric response was not sensitive to different ions, viscosity, or pH under the tested conditions. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:249-250]

## Fluorescence lifetime sensitivity

CQPP also displayed polarity-dependent [[fluorescence lifetime imaging|fluorescence lifetime]] behavior. When the medium changed from dioxane to water, the fluorescence lifetime decreased from `1.49 ns` to `0.63 ns`; within the polarity range corresponding to `1,4-dioxane` through `20% H2O` in dioxane, the lifetime decreased from `1.49 ns` to `0.89 ns`. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:251-257]

The paper notes that this lifetime range overlaps the expected polarity range for [[lipid droplets]], whose oily core is composed mainly of triglycerides and cholesterol esters and is coated by a phospholipid monolayer membrane. On that basis, the authors conclude that both the ratiometric emission shift and the lifetime shift provide a way to track polarity changes of lipid droplets and the nucleus in living cells. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:258-267]

## Cellular context

In live `HT-1080` cells, CQPP produced dotted green fluorescence in the cytoplasm and bright red fluorescence in the nucleus after incubation. Co-localization experiments showed that the green emission was mainly distributed in lipid droplets, while the red emission co-localized with `Hoechst 33342` in the nucleus, consistent with the probe's dual-targeting design. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:304-339]

The source attributes this dual-targeting behavior in part to CQPP's balanced lipophilicity and hydrophilicity. It also notes that the large emission separation of about `200 nm` between the green and red channels helps minimize crosstalk during imaging. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:330-339]

## Use in ferroptosis monitoring

Using CQPP in ferroptosis models, the authors report that lipid droplets initially exhibited lower polarity than the surrounding cytoplasm, with a polarity gradient from the droplet core to the surface. After treatment with `erastin`, green emission in lipid droplets decreased and red fluorescence in the cytoplasm increased slightly, which the authors interpret as evidence of increased lipid-droplet polarity. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:343-365]

In a time-response model using `RSL3`, the green signal gradually decreased, punctate lipid-droplet features became more diffuse in the cytoplasm, and ratiometric imaging showed that the polarity gradient from droplet core to surface became less distinct over time. The study describes this as gradual homogenization of polarity between lipid droplets and cytoplasm during ferroptosis. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:366-385]

`FLIM` measurements supported the same interpretation. In untreated cells, CQPP lifetimes in the cytoplasm and nucleus formed two distinct regions, whereas after `erastin` treatment a new shorter lifetime peak appeared in the lipid-droplet-associated region while the nuclear lifetime region remained largely unchanged. The authors therefore used nuclear fluorescence as a reference and concluded that lipid-droplet polarity increases significantly during ferroptosis. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:406-435]

## Significance

The paper presents CQPP as a probe whose donor-acceptor structure enables both ratiometric fluorescence and fluorescence lifetime responses to polarity. In the authors' summary, this made it possible, for the first time, to apply a dual-targeted lipid droplet/nucleus probe to observe increased lipid-droplet polarity and polarity homogenization between lipid droplets and cytoplasm during ferroptosis, while nucleic-acid binding in the nucleus provided a reference for distinguishing ferroptosis from [[apoptosis]]. ^[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:445-460, polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis.md:584-588]

## Related concepts

- [[Lipid droplets]]
- [[Cell nucleus]]
- [[Ferroptosis]]
- [[Apoptosis]]
- [[Ratiometric fluorescence imaging]]
- [[Fluorescence lifetime imaging]]
- [[Intramolecular charge transfer]]

## Sources

- [[polaritysensitive-ratiometric-fluorescence-probe-for-monitoring-lipid-dropletsnucleus-change-during-ferroptosis]]
