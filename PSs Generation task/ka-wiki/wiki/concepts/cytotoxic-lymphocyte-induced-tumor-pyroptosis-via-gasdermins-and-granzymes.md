---
title: Cytotoxic lymphocyte-induced tumor pyroptosis via gasdermins and granzymes
summary: Recent studies summarized in the review show that CTLs, NK cells, and CAR-T cells can trigger tumor-cell pyroptosis through perforin-assisted delivery of granzymes that activate gasdermins such as GSDMB or GSDME, linking immune killing to inflammatory amplification.
sources:
  - pyroptosis-at-the-forefront-of-anticancer-immunity.md
kind: concept
createdAt: "2026-07-17T10:19:50.689Z"
updatedAt: "2026-07-17T10:19:50.689Z"
tags:
  - t-cells
  - nk-cells
  - pyroptosis
  - antitumor-immunity
aliases:
  - cytotoxic-lymphocyte-induced-tumor-pyroptosis-via-gasdermins-and-granzymes
  - granzymes and Cytotoxic lymphocyte-induced tumor pyroptosis via gasdermins
  - CLTPVGAG
confidence: 0.95
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# Cytotoxic lymphocyte-induced tumor pyroptosis via gasdermins and granzymes

Cytotoxic lymphocyte-induced tumor pyroptosis refers to a mode of tumor-cell killing in which [[cytotoxic T lymphocytes|cytotoxic T lymphocytes (CTLs)]], [[natural killer cells]], or [[CAR-T cells]] deliver granzymes into target cells and trigger [[pyroptosis]] through specific [[gasdermins]]. In the reviewed literature, this process is presented as one way pyroptosis can participate in a positive feedback loop in [[anti-tumor immunity]], because immune-cell killing can directly induce inflammatory tumor-cell death that further amplifies immune activation. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:526-548]

## Mechanistic basis

Pyroptosis is a lytic, inflammatory programmed cell death pathway mediated by gasdermin family proteins. Gasdermins contain an N-terminal pore-forming domain and a C-terminal inhibitory domain; cleavage at the linker region by caspases or granzymes releases the N-terminal fragment, which inserts into membranes, oligomerizes, forms pores, and enables release of pro-inflammatory contents such as `IL-1beta` and `IL-18`, ultimately causing cell lysis. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:212-241]

Within the review’s pathway summary, granzymes are included among alternative pyroptosis activators. The article specifically notes reported pathways in which [[granzyme B]] cleaves [[Gasdermin E|GSDME]] and [[granzyme A]] cleaves [[Gasdermin B|GSDMB]], placing cytotoxic-lymphocyte-mediated pyroptosis alongside caspase-driven gasdermin activation as a recognized route to pyroptotic death. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:220-223, pyroptosis-at-the-forefront-of-anticancer-immunity.md:231-239, pyroptosis-at-the-forefront-of-anticancer-immunity.md:323-330]

## GSDMD-related CTL cytotoxicity

One study highlighted in the review examined [[GSDMD]] in CTLs rather than in tumor cells. Across lung adenocarcinoma, lung squamous cell carcinoma, and melanoma cohorts, `GSDMD` expression correlated positively with CTL marker genes including `CD8A`, `CD8B`, `PRF1`, `GZMA`, `GZMB`, and `IFNG`, and activated mouse and human `CD8+` T cells upregulated GSDMD. In activated CTLs, caspase-11 in mice or caspase-4 in humans promoted GSDMD cleavage, and GSDMD knockdown reduced CTL cytotoxicity against tumor cells in co-culture assays. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:624-652]

When activated OT-1 CTLs were co-cultured with `3LL-OVA` tumor cells, GSDMD and `GzmB` co-localized in CTLs near immune synapses. Based on these findings, the review states that it was speculated that delivery of GSDMD together with `GzmB` into effector cancer cells could underlie the observed CTL cytotoxicity. This section presents a proposed mechanism tied to CTL killing, but the review frames it as speculation rather than a fully established tumor-cell gasdermin pathway. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:646-659]

## GSDMB cleavage by granzyme A

The review describes stronger direct evidence for tumor-cell pyroptosis through [[Gasdermin B|GSDMB]] and [[granzyme A]]. In `HEK-293T` cells lacking endogenous gasdermins, forced expression of `GSDMB`, but not other gasdermins, enabled pyroptotic killing by co-cultured human `NK-92MI` cells. This killing appeared caspase-independent, because a pan-caspase inhibitor did not block it, whereas inhibition of granzymes, NK-cell degranulation, or perforin blocked both NK-cell-induced pyroptosis and GSDMB cleavage. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:660-680]

Among the five human granzymes tested in `HEK-293F` cells, only `GzmA` rapidly cleaved GSDMB in a pattern similar to NK-cell killing assays. Electroporation of GzmA into GSDMB-reconstituted cells caused extensive GSDMB cleavage and pyroptotic killing, while a protease-deficient `GzmA S212A` mutant or non-cleavable `GSDMB` mutants markedly reduced pyroptosis. The same requirement for GzmA-mediated GSDMB cleavage was observed under physiological NK-cell killing conditions, indicating that disruption of this cleavage confers resistance to pyroptosis. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:680-694]

The same study extended this mechanism to human cancer cell lines that endogenously expressed `GSDMB`, including `OE19`, `SW837`, and `SKCO1`, where GzmA delivery by electroporation or perforin was sufficient to induce GSDMB-mediated pyroptosis. It also found that some low-GSDMB cell lines, such as `OE33` and `HCC1954`, could increase GSDMB expression after exposure to `IFN-gamma` and `TNF-alpha`, cytokines typically released by activated cytotoxic lymphocytes; IFN-gamma priming then enhanced pyroptotic death in a GzmA-dependent manner. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:694-709]

The review further notes that anti-`CD19` [[CAR-T cells]] induced GSDMB cleavage and pyroptosis in `293T` cells expressing `CD19` and `GSDMB`, but not when tumor cells expressed a non-cleavable GSDMB variant or when `GZMA` was knocked down in the CAR-T cells. In mouse models using human `GSDMB`-expressing tumor cells, blockade of `PD-1`-`PD-L1` interactions markedly improved tumor control, and the review interprets the overall findings to mean that cytotoxic lymphocytes can deliver GzmA into GSDMB-expressing cancer cells to promote anti-tumor immunity. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:710-751]

## GSDME cleavage by granzyme B

The review also summarizes a parallel mechanism centered on [[Gasdermin E|GSDME]] and [[granzyme B]]. In immunocompetent `BALB/c` mice, ectopic expression of mouse `GSDME` in `4T1E` breast cancer cells significantly inhibited tumor growth and increased infiltration of NK cells and tumor-associated macrophages. These tumors also showed increased NK-cell and `CD8+` tumor-infiltrating lymphocyte expression of `GzmB` and perforin, along with increased `CD8+` TIL production of `IFN-gamma` and `TNF`. Non-functional or non-cleavable GSDME constructs blunted these effects, while `GSDME` knockout in `EMT6` tumors produced the opposite pattern. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:752-779]

Additional experiments linked this antitumor effect to immune effector function. In mice implanted with `eGFP`-expressing `4T1E` cells, tumors overexpressing `GSDME` contained more `eGFP-positive CD8+` TILs and more `eGFP-positive` tumor-associated macrophages, consistent with greater tumor-cell phagocytosis. The antitumor effect of GSDME depended on lymphocytes and perforin, based on experiments in `NSG` mice and perforin-deficient `BALB/c` mice, implicating NK cells and `CD8+` T cells in GSDME-associated tumor suppression. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:769-786]

In mechanistic follow-up, the human NK cell line `YT` activated pyroptosis in GSDME-expressing `HeLa` cells, and experiments with the `SH-SY5Y` cell line led the authors to speculate that this occurred through `GzmB`, which both cleaves GSDME at the same site as caspase-3 and indirectly activates caspase-3. The review also states that vaccine/challenge experiments strongly supported pyroptosis as a form of [[immunogenic cell death]], consistent with the enhanced immune infiltration and function observed in GSDME-overexpressing tumors. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:787-797]

The same GSDME-centered theme appears in the review’s discussion of CAR-T-cell-induced pyroptosis. It cites work showing that CAR-T cells can induce GSDME-mediated pyroptosis in B leukemic and solid tumor cells through perforin and GzmB release. In those experiments, supernatants from CAR-T-cell and cancer-cell co-cultures activated macrophage caspase-1, GSDMD cleavage, and `IL-6`/`IL-1beta` release, but these effects were lost when the cancer cells lacked GSDME or when macrophages lacked caspase-1, GSDMD, or `NLRP3`. `ATP` and `HMGB1` present in pyroptotic supernatants were sufficient to drive parts of this macrophage inflammatory response. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:798-819]

## Immunologic consequences

The review frames pyroptosis as potentially immunogenic because dying tumor cells release endogenous `DAMPs` and inflammatory mediators that can amplify immune activation. It contrasts pyroptosis with apoptosis as an immune-tolerant process and states that pyroptosis-mediated tumor clearance is increasingly linked to stronger immune activation and function. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:526-540]

In the context of cytotoxic-lymphocyte-induced pyroptosis, the review highlights several downstream consequences: increased infiltration of NK cells, `CD8+` T cells, and macrophages; increased phagocytosis of tumor material; and macrophage activation driven by pyroptotic tumor-cell supernatants containing `ATP` and `HMGB1`. A separate melanoma study cited in the review also connected `GSDME`- and caspase-3-mediated pyroptosis with `HMGB1` release and infiltration of tumor-associated T cells and activated dendritic cells, supporting a broader link between tumor pyroptosis and immune-cell recruitment and activation. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:776-779, pyroptosis-at-the-forefront-of-anticancer-immunity.md:808-837]

## Context and limitations

The review emphasizes that responses to granzymes and gasdermins are contextual and depend on cell type. It explicitly contrasts the `GzmB`/`GSDMD` interpretation proposed in the CTL study with the `GzmA`/`GSDMB` mechanism described by Zhou and colleagues, noting that different cell types may use different gasdermin-granzyme combinations. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:660-669]

It also places this mechanism within a larger therapeutic landscape in which pyroptosis may help convert immunologically “cold” tumors into “hot” tumors and may synergize with checkpoint blockade such as `PD-1` inhibition. At the same time, the review notes that irregular gasdermin expression or function across cancers is a major barrier to therapeutic use, which is directly relevant to lymphocyte-induced pyroptosis because the pathway depends on tumor cells expressing a cleavable gasdermin substrate. ^[pyroptosis-at-the-forefront-of-anticancer-immunity.md:845-850, pyroptosis-at-the-forefront-of-anticancer-immunity.md:907-949, pyroptosis-at-the-forefront-of-anticancer-immunity.md:950-973]

## Related concepts

- [[Pyroptosis]]
- [[Anti-tumor immunity]]
- [[Gasdermins]]
- [[Gasdermin D|GSDMD]]
- [[Gasdermin B|GSDMB]]
- [[Gasdermin E|GSDME]]
- [[Granzyme A]]
- [[Granzyme B]]
- [[Cytotoxic T lymphocytes]]
- [[Natural killer cells]]
- [[CAR-T cells]]
- [[Immunogenic cell death]]
- [[PD-1]]
- [[PD-L1]]
- [[HMGB1]]
- [[ATP]]
- [[NLRP3 inflammasome]]

## Sources

- [[pyroptosis-at-the-forefront-of-anticancer-immunity]]
