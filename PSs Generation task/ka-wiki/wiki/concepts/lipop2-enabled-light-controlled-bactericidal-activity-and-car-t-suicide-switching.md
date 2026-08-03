---
title: LiPOP2-enabled light-controlled bactericidal activity and CAR-T suicide switching
summary: LiPOP2 tools are applied beyond basic pathway reconstruction to kill E. coli after induced expression and blue light exposure, and to trigger pyroptotic suicide of engineered Jurkat CAR T cells as a potential controllable safety switch.
sources:
  - optogenetic-control-of-nonapoptotic-cell-death.md
kind: concept
createdAt: "2026-07-17T09:25:32.397Z"
updatedAt: "2026-07-17T09:25:32.397Z"
tags:
  - bactericidal
  - cell-therapy
  - pyroptosis
  - applications
aliases:
  - lipop2-enabled-light-controlled-bactericidal-activity-and-car-t-suicide-switching
  - CAR-T suicide switching and LiPOP2-enabled light-controlled bactericidal activity
  - LLBAACSS
confidence: 0.95
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# LiPOP2-enabled light-controlled bactericidal activity and CAR-T suicide switching

`LiPOP2` is an optogenetic pyroptosis tool derived from engineered [[Gasdermin D|GSDMD]] modules that the study applied in two downstream use cases: light-controlled killing of bacteria and light-triggered suicide of engineered [[CAR-T cell therapy|CAR-T]]-like T cells. In this work, the authors specifically tested `LiPOP2b` as a genetically encoded bactericidal module in *E. coli* and tested both `LiPOP2a` and `LiPOP2b` as suicide switches in Jurkat CAR T cells under blue-light stimulation. ^[optogenetic-control-of-nonapoptotic-cell-death.md:581-585, optogenetic-control-of-nonapoptotic-cell-death.md:618-635, optogenetic-control-of-nonapoptotic-cell-death.md:655-671]

## LiPOP2 context

Earlier in the study, the authors developed two light-responsive pyroptosis constructs, `LiPOP2a` and `LiPOP2b`, to recapitulate key steps of GSDMD-mediated pyroptosis. `LiPOP2a` used light-induced dissociation between `GSDMD-NT` and `GSDMD-CT` to release the pore-forming N-terminal domain, while `LiPOP2b` used a circularly permuted `LOV2` photoswitch to cage an engineered `GSDMD-NT` in the dark and restore cytotoxicity after illumination. Both constructs showed low or limited dark-state activity relative to their lit-state killing activity in HeLa-cell assays. ^[optogenetic-control-of-nonapoptotic-cell-death.md:487-503, optogenetic-control-of-nonapoptotic-cell-death.md:515-531, optogenetic-control-of-nonapoptotic-cell-death.md:534-566, optogenetic-control-of-nonapoptotic-cell-death.md:698-715]

## Light-controlled bactericidal activity

The bactericidal application was based on prior evidence, cited by the authors, that `GSDMD-NT` can bind cardiolipin, a major lipid in bacterial membranes, and kill bacteria. On that basis, the study tested whether inducible expression of `LiPOP2b` in the host bacterial strain would confer light-dependent antibacterial activity. ^[optogenetic-control-of-nonapoptotic-cell-death.md:618-623]

To do this, the authors subcloned `LiPOP2b` into an `IPTG`-inducible `pTriEx` vector and transformed it into `BL21(DE3)` *Escherichia coli* cells. During overnight growth, the transformed bacteria were either protected from light or exposed to blue light, allowing the investigators to compare the effects of induced `LiPOP2b` expression with and without photostimulation. ^[optogenetic-control-of-nonapoptotic-cell-death.md:623-626, optogenetic-control-of-nonapoptotic-cell-death.md:822-824, optogenetic-control-of-nonapoptotic-cell-death.md:973-987]

Under these conditions, bacterial colony-forming units were significantly reduced when `IPTG` was used to induce `LiPOP2b` expression, and bacterial growth in liquid `LB` medium was blocked in response to blue-light stimulation after induction. The control group did not show light-dependent effects, leading the authors to conclude that `LiPOP2b` can function as a genetically encoded bactericide that eliminates bacteria in a light-dependent manner. ^[optogenetic-control-of-nonapoptotic-cell-death.md:627-635, optogenetic-control-of-nonapoptotic-cell-death.md:826-829]

## CAR-T suicide switching

The study frames this application against the broader need for controllable suicide systems in adoptive cell therapy and transplantation. It notes that pathological immune responses and toxicities can limit engineered-cell therapies, and that existing suicide genes such as inducible caspase-9 (`iCasp9`) and `HSV-TK` require an additional drug, which may penetrate solid tumors inefficiently or cause unwanted effects on endogenous signaling and immune responses. ^[optogenetic-control-of-nonapoptotic-cell-death.md:636-654]

As an alternative, the authors introduced the light-inducible suicide gene `LiPOP2` into Jurkat T cells engineered to express chimeric antigen receptors. They then evaluated whether blue light could trigger cell death in `LiPOP2a`- or `LiPOP2b`-expressing Jurkat CAR T cells. ^[optogenetic-control-of-nonapoptotic-cell-death.md:655-658, optogenetic-control-of-nonapoptotic-cell-death.md:830-836]

In both `LiPOP2a`- and `LiPOP2b`-expressing Jurkat CAR T cells, blue-light stimulation efficiently induced cell death with pyroptotic morphology. This was accompanied by time-dependent `LDH` release, interpreted as increasing release of cellular contents during light-triggered membrane damage. The reported half-times were `4.0 +/- 0.3 h` for `LiPOP2a` and `3.0 +/- 0.3 h` for `LiPOP2b`. ^[optogenetic-control-of-nonapoptotic-cell-death.md:658-663, optogenetic-control-of-nonapoptotic-cell-death.md:830-832]

Flow-cytometry analysis using `SYTOX Blue` and `Annexin V` quantitatively confirmed the suicide-switch behavior. After 6 hours of pulsed blue-light exposure, the lit group showed an approximately fourfold to fivefold increase in cell death, whereas the control constructs showed no significant light-inducible effects across imaging, `LDH`, and flow-cytometry assays. ^[optogenetic-control-of-nonapoptotic-cell-death.md:663-668, optogenetic-control-of-nonapoptotic-cell-death.md:833-836]

## Interpretation

Within this paper, `LiPOP2` is presented as a light-gated pyroptotic effector that can be repurposed beyond mammalian model-cell assays. The bacterial experiments support its use as a genetically encoded, light-dependent bactericide, while the Jurkat CAR T-cell experiments support its use as a candidate optical suicide switch for selective elimination of engineered therapeutic T cells. ^[optogenetic-control-of-nonapoptotic-cell-death.md:633-635, optogenetic-control-of-nonapoptotic-cell-death.md:669-671, optogenetic-control-of-nonapoptotic-cell-death.md:759-763]

## Related concepts

- [[Pyroptosis]]
- [[Gasdermin D|GSDMD]]
- [[Optogenetics]]
- [[CAR-T cell therapy]]
- [[Suicide gene]]
- [[Jurkat]]
- [[Escherichia coli]]
- [[LDH release assay]]

## Sources

- [[optogenetic-control-of-nonapoptotic-cell-death]]
