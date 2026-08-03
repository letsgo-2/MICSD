---
title: FL/MR dual-modal imaging-guided photodynamic therapy with Gd-PNPs
summary: The study combines fluorescence and magnetic resonance imaging with photodynamic therapy in one nanoparticle system, using the imaging signals to characterize tumor localization and treatment timing before in vivo PDT.
sources:
  - d1nr04489c-110.md
kind: concept
createdAt: "2026-07-17T08:33:48.179Z"
updatedAt: "2026-07-17T08:33:48.179Z"
tags:
  - dual-modal-imaging
  - theranostics
  - MRI
  - fluorescence
aliases:
  - flmr-dual-modal-imaging-guided-photodynamic-therapy-with-gd-pnps
  - FDIPTWG
confidence: 0.98
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# FL/MR dual-modal imaging-guided photodynamic therapy with Gd-PNPs

[[Gd-PNPs]] are gadolinium-porphyrin-based supramolecular nanotheranostics developed for [[fluorescence imaging|fluorescence (FL) imaging]] and [[magnetic resonance imaging|magnetic resonance (MR) imaging]]-guided [[photodynamic therapy]] (PDT). In this study, they were produced by a facile non-covalent electrostatic self-assembly strategy that encapsulated [[Gd-TCPP]] into homogeneous nanoparticles, with the goal of combining FL imaging, T1-weighted MR contrast, and photosensitizing activity in a single platform. ^[d1nr04489c-110.md:19-30, d1nr04489c-110.md:117-126]

The paper frames this approach as a response to limitations of both standalone PDT and single-mode imaging. PDT offers minimal invasiveness and spatiotemporal controllability, but precise irradiation of tumor lesions and identification of suitable treatment windows remain challenging. FL/MR dual-modal imaging is described as attractive because it can provide complementary information for cancer diagnosis and help define tumor boundaries with high soft-tissue resolution. ^[d1nr04489c-110.md:42-60, d1nr04489c-110.md:61-77]

## Platform design

Gd-PNPs were assembled from [[Gd-TCPP]], [[polyethyleneimine|PEI]], and a [[PEGylation|PEGylated]] poly(glutamic acid) layer (`mPEG-PGA`). In this design, Gd-TCPP first served as the gadolinium-chelated porphyrin building block, then mixed with positively charged PEI to form supramolecular particles through electrostatic self-assembly, and finally received a surface coating of negatively charged mPEG-PGA to reduce charge-associated biotoxicity. ^[d1nr04489c-110.md:138-173, d1nr04489c-110.md:277-317]

The resulting nanoparticles were reported as well-dispersed spheres with an average diameter of about 200 nm. Surface modification reduced the zeta potential from `+50.3 mV` to approximately `-0.1 mV`, and spectroscopic analyses indicated the presence of surface amines and carboxyl groups that the authors associate with colloidal stability and cell-membrane permeability. ^[d1nr04489c-110.md:313-317, d1nr04489c-110.md:318-342]

## Imaging properties

Gd-PNPs retained the fluorescence behavior of the gadolinium-porphyrin cargo, with excitation and emission peaks around `430/666 nm`, while showing no obvious fluorescence quenching after encapsulation. The fluorescence lifetime increased markedly from `0.71 ns` for Gd-TCPP to `8.88 ns` after encapsulation, and the reported fluorescence quantum yield of Gd-PNPs was `7.25%`. ^[d1nr04489c-110.md:343-361]

The presence of Gd3+ also gave Gd-PNPs T1-weighted MR imaging capability. Their longitudinal relaxivity (`r1`) was reported as `16.157 mM^-1 s^-1`, with an `r2/r1` ratio of `1.16`, supporting their classification as T1 contrast agents. The authors note that this `r1` value exceeded several commercial MR contrast agents listed for comparison, implying the potential for lower administered contrast doses. ^[d1nr04489c-110.md:362-376]

## Biocompatibility and stability

The study reports negligible Gd3+ leakage from Gd-PNPs over `48 h`, high cell viability in both HeLa and CT 26 cells after nanoparticle exposure, and low hemolysis even at `400 ug mL^-1`. Gd-PNPs also remained colloidally stable in fetal bovine serum for up to `48 h` without obvious size change or precipitation. ^[d1nr04489c-110.md:377-395]

In vivo safety assessments in zebrafish and Balb/c mice also suggested low biotoxicity. Treated zebrafish showed no observed lesion or teratogenesis and maintained survival and hatching rates above `90%` even at the highest tested concentration, while H&E staining of major mouse organs showed no observable damage or inflammation after treatment. ^[d1nr04489c-110.md:396-426]

## Dual-modal imaging in tumor-bearing mice

Using CT 26 tumor-bearing mice, the study evaluated both in vivo FL and MR imaging after intravenous administration. FL imaging showed time-dependent tumor accumulation of Gd-PNPs, with the strongest tumor fluorescence detected at `12 h` after injection and still detectable at `24 h`. Compared with free Gd-TCPP, Gd-PNP-treated mice showed about `1.6-fold` stronger fluorescence signals, and ex vivo imaging at `24 h` showed the strongest fluorescence in tumors rather than in major metabolic organs. ^[d1nr04489c-110.md:446-463]

MR imaging likewise showed time-dependent positive contrast enhancement at tumor sites. For Gd-PNP-treated mice, the strongest MR signal with a sharply defined tumor border was observed at `6 h` after intravenous injection, whereas the comparator [[Gadobutrol]] peaked earlier at `1 h`. The maximum MR signal enhancement at the tumor site reached `3.5-fold` for Gd-PNPs, compared with `2.5-fold` for Gadobutrol in the study, and the authors attribute the stronger and more sustained tumor signal of Gd-PNPs to more efficient tumor accumulation and longer retention. ^[d1nr04489c-110.md:464-510]

## Photodynamic therapy performance

The photodynamic function of Gd-PNPs was linked to concentration-dependent [[singlet oxygen]] generation under `635 nm` laser irradiation, with production increasing over irradiation time until reaching a plateau at `10 min`. The reported singlet oxygen quantum yield of Gd-PNPs was `26%`, comparable to those of TCPP (`25%`) and Gd-TCPP (`29%`), indicating that gadolinium chelation and nanoparticle encapsulation did not substantially impair PDT activity. ^[d1nr04489c-110.md:511-533]

In CT 26 cells, Gd-PNPs produced dose-dependent PDT cytotoxicity under laser irradiation, with more than `90%` of cells killed at `0.4 mg mL^-1` after `10 min` of `635 nm` irradiation at `25 mW cm^-2`. At the animal level, CT 26 tumor-bearing mice were assigned to PBS only, Gd-PNPs only, laser only, or Gd-PNPs plus laser groups. Only the combined Gd-PNPs plus laser treatment produced marked tumor growth inhibition, with reduced tumor volume and tumor weight. ^[d1nr04489c-110.md:243-274, d1nr04489c-110.md:533-564]

Histologic analysis further supported the therapeutic effect. H&E and TUNEL staining of tumors showed the most extensive apoptosis and necrosis in mice treated with Gd-PNPs under laser irradiation, while body weight remained stable across treatment groups during the study period, consistent with the absence of obvious systemic side effects in this model. ^[d1nr04489c-110.md:564-572]

## Significance

The study concludes that Gd-PNPs provide a simple metalloporphyrin-based nanotheranostic platform in which Gd-TCPP serves simultaneously as a fluorescence probe, MR contrast agent, and photosensitizer. In CT 26 tumor-bearing mice, their efficient tumor accumulation, prolonged retention, FL/MR imaging performance, and PDT-associated tumor inhibition support their use as a dual-modal imaging-guided phototherapeutic system. ^[d1nr04489c-110.md:590-609]

## Related concepts

- [[Gd-PNPs]]
- [[Gd-TCPP]]
- [[Photodynamic therapy]]
- [[Fluorescence imaging]]
- [[Magnetic resonance imaging]]
- [[Singlet oxygen]]
- [[PEGylation]]
- [[Gadobutrol]]
- [[CT 26]]

## Sources

- [[d1nr04489c-110]]
