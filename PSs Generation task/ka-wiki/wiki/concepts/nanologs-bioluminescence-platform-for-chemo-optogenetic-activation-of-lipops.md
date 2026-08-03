---
title: NanoLOGS bioluminescence platform for chemo-optogenetic activation of LiPOPs
summary: A NanoLuc-based luminescence-aided optogenetic stimulation system activates CRY2-linked LiPOP constructs with luciferase substrates, enabling chemical control of necroptotic tumor killing in vitro and in vivo.
sources:
  - optogenetic-control-of-nonapoptotic-cell-death.md
kind: concept
createdAt: "2026-07-17T09:23:50.994Z"
updatedAt: "2026-07-17T09:23:50.994Z"
tags:
  - bioluminescence
  - optogenetics
  - NanoLuc
  - cancer
aliases:
  - nanologs-bioluminescence-platform-for-chemo-optogenetic-activation-of-lipops
  - NBPFCAOL
confidence: 0.97
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# NanoLOGS bioluminescence platform for chemo-optogenetic activation of LiPOPs

The [[NanoLOGS]] platform is a NanoLuc-mediated luminescence-aided optogenetic stimulation system developed to activate [[LiPOPs]] through bioluminescence rather than external light delivery. In the study introducing LiPOPs, the authors designed NanoLOGS to test whether the NanoLuc substrate furimazine could drive CRY2 oligomerization and thereby activate the necroptosis effector construct [[LiPOP1]] for chemo-optogenetic tumor cell killing. ^[optogenetic-control-of-nonapoptotic-cell-death.md:381-390]

## Rationale

The platform was developed as an alternative to NIR/[[upconversion nanoparticles]]-based activation. The paper states that UCNP-assisted activation improves penetration depth to about 2-3 cm, but may still be less effective for deeply buried tissues. Because NanoLuc emits light at 460 nm during conversion of furimazine to furimamide, overlapping the 450-470 nm activation window of blue light-responsive optogenetic devices, the authors explored bioluminescence as a compatible internal light source for LiPOPs. ^[optogenetic-control-of-nonapoptotic-cell-death.md:363-380]

## Design

NanoLOGS was implemented by fusing NanoLuc to LiPOP1 to create `LiPOP1-NanoLuc`. In this configuration, NanoLuc-generated photons activate the CRY2 module, causing oligomerization of LiPOP1 and plasma-membrane perforation that induces necroptosis. The study also used `mCh-NanoLuc-CRY2` as a control construct for NanoLuc-dependent CRY2 activation without the LiPOP1 killing module. ^[optogenetic-control-of-nonapoptotic-cell-death.md:389-402, optogenetic-control-of-nonapoptotic-cell-death.md:585-587, optogenetic-control-of-nonapoptotic-cell-death.md:799-804]

## In vitro activation with furimazine

In NanoLuc- or `LiPOP1-NanoLuc`-expressing cells, furimazine treatment produced a dose-dependent bioluminescence signal that was strong enough to be seen by eye in a dark room. Confocal imaging showed that `mCh-NanoLuc-CRY2` could be activated by `10 uM` furimazine, evidenced by oligomerization of the hybrid protein. ^[optogenetic-control-of-nonapoptotic-cell-death.md:391-403]

Using this approach, the authors observed furimazine-triggered plasma-membrane translocation of `LiPOP1-NanoLuc` and necroptosis in multiple cancer cell lines, including [[HeLa]], [[B16]], and [[786-O]] cells. In 786-O cells, `10 uM` furimazine induced membrane translocation with a half-time of `46.1 +/- 17.3 s` and caused necroptotic cell death within 30 minutes, while the `mCh-NanoLuc-CRY2` control did not cause cell death over the same interval. ^[optogenetic-control-of-nonapoptotic-cell-death.md:404-415, optogenetic-control-of-nonapoptotic-cell-death.md:588-593]

The paper reports that NanoLOGS activation was slower than direct blue-light stimulation but achieved a comparable extent of membrane translocation. Specifically, the half-time for NanoLOGS-induced translocation was about fourfold longer than with direct blue light (`46.1 s` versus `12.8 s`), which the authors attribute to lower bioluminescence power density, while concluding that the overall effectiveness of activation remained comparable. ^[optogenetic-control-of-nonapoptotic-cell-death.md:416-422]

## Substrate optimization with fluorofurimazine

For in vivo use, the study emphasizes the importance of substrate solubility and safety. The authors note that furimazine has limited brightness in mice because of poor solubility and bioavailability, and cite prior evidence of liver toxicity after repeated dosing. They therefore evaluated [[fluorofurimazine|FFz]] as an improved NanoLuc substrate. ^[optogenetic-control-of-nonapoptotic-cell-death.md:423-430]

In side-by-side ex vivo comparisons, FFz showed a longer bioluminescence decay half-life than furimazine (`64.2 +/- 2.1 min` versus `38.74 +/- 1.43 min`) and approximately `1.5-1.8-fold` greater brightness at the same concentration. Based on these properties, the authors selected FFz for in vivo chemo-optogenetic activation of `LiPOP1-NanoLuc`. ^[optogenetic-control-of-nonapoptotic-cell-death.md:431-440]

The paper also reports favorable biocompatibility for FFz. FFz showed no appreciable in vitro cytotoxicity to mammalian cells up to `20 uM`, and mice receiving `1.3 umol` per 25 g body weight every three days for seven doses showed no noticeable tissue damage or inflammatory lesions on histopathology; most complete blood count parameters remained within normal ranges. The authors therefore describe FFz as an improved NanoLOGS substrate with greater solubility, higher brightness, prolonged luminescence, and good in vivo biocompatibility. ^[optogenetic-control-of-nonapoptotic-cell-death.md:441-459]

## In vivo tumor-cell killing

To test NanoLOGS in vivo, the study used immunodeficient mice bearing subcutaneous 786-O xenografts expressing either `LiPOP1-NanoLuc` or `mCh-NanoLuc-CRY2`. After 9 days of tumor establishment, mice received intratumoral or systemic FFz dosing every three days through day 30, and tumors were assessed by bioluminescence imaging and caliper measurement. ^[optogenetic-control-of-nonapoptotic-cell-death.md:460-468, optogenetic-control-of-nonapoptotic-cell-death.md:600-607, optogenetic-control-of-nonapoptotic-cell-death.md:988-1011]

At the endpoint, the `LiPOP1-NanoLuc` group showed significantly reduced tumor size relative to the control group. The authors interpret these data as establishing NanoLOGS as a safe wireless method for activating CRY2-based optogenetic devices to kill tumor cells both in cultured cells and in living animals. ^[optogenetic-control-of-nonapoptotic-cell-death.md:468-472]

## Relationship to LiPOPs

Within the broader LiPOP study, NanoLOGS is presented as one of two wireless activation strategies for optogenetic control of non-apoptotic cell death, alongside UCNP-mediated NIR-to-blue conversion. The discussion notes that bioluminescence-based activation may sacrifice some spatial resolution compared with externally directed optical stimulation, but it extends LiPOP activation to tissues or organs reachable by substrate delivery. ^[optogenetic-control-of-nonapoptotic-cell-death.md:738-748]

## Related concepts

- [[LiPOPs]]
- [[LiPOP1]]
- [[Necroptosis]]
- [[CRY2]]
- [[NanoLuc]]
- [[Furimazine]]
- [[Fluorofurimazine|FFz]]
- [[Upconversion nanoparticles]]
- [[Chemo-optogenetics]]
- [[786-O]]
- [[HeLa]]
- [[B16]]

## Sources

- [[optogenetic-control-of-nonapoptotic-cell-death]]
