---
title: WGCNA- and CMAP-based drug repurposing pipeline for glioblastoma
summary: The study combines TCGA glioblastoma differential expression analysis, WGCNA hub-gene identification, and CMAP querying to nominate existing azole compounds as potential anti-GBM drugs.
sources:
  - benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md
kind: concept
createdAt: "2026-07-17T08:00:19.800Z"
updatedAt: "2026-07-17T08:00:19.800Z"
tags:
  - glioblastoma
  - drug-repurposing
  - bioinformatics
  - network-analysis
aliases:
  - wgcna-and-cmap-based-drug-repurposing-pipeline-for-glioblastoma
  - CMAP-based drug repurposing pipeline for glioblastoma and WGCNA-
  - WACDRPFG
confidence: 0.98
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# WGCNA- and CMAP-based drug repurposing pipeline for glioblastoma

This pipeline refers to the study’s strategy for identifying potential [[drug repurposing]] candidates for [[glioblastoma multiforme|glioblastoma (GBM)]] by combining [[weighted gene co-expression network analysis|WGCNA]] of [[TCGA]] transcriptomic data with the [[Connectivity Map|CMAP]] platform. In the study, GBM hub genes were derived from TCGA data through WGCNA, and the resulting gene signatures were used in CMAP to identify compounds predicted to reverse key GBM-associated expression patterns. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:18-20, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:63-67, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:163-169]

## Rationale

The source frames GBM as the most malignant and lethal primary brain tumor in adults and states that [[temozolomide]] is the only available drug treatment, with frequent resistance and notable side effects. Against that background, the authors present drug repurposing as an efficient and economical way to identify new therapeutic options more quickly than de novo drug development. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:16-18, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:42-50]

The study also describes CMAP as a platform that connects small molecules, genes, and diseases through gene-expression signatures, and WGCNA as a method for identifying clusters of correlated genes, module eigengenes, and intramodular hub genes. These two tools were combined so that GBM-associated network features could guide compound prioritization. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:53-66]

## Input data and preprocessing

The pipeline began with RNA-seq data and clinical information for GBM patients downloaded from [[TCGA]]. After removal of repetitive samples and samples lacking clinical information, the WGCNA analysis used 169 GBM tumors and 5 normal brain samples, with read counts used to represent gene expression levels. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:115-124]

Differentially expressed genes were identified with the `edgeR` R package by comparing tumor and normal samples. The methods section reports a threshold of `|log2 Fold Change| > 1.5` and `FDR < 0.05`, while the results section states that filtering under `log(FC) > 2` and `P < 0.01` produced 2,720 downregulated genes and 3,474 upregulated genes, for a total of 6,194 DEGs used in the downstream network analysis. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:125-130, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:341-343, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:370-372]

## WGCNA stage

Gene co-expression networks were constructed from the GBM DEGs using the WGCNA package. The authors selected an appropriate soft-thresholding power with the `pick soft threshold` function, generated a scale-free topology plot, and built co-expression modules using major parameters including `cutHeight = 0.6` and `min Size = 10`. Module eigengenes were then computed to summarize each module’s expression profile. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:131-142]

To connect network structure with clinical context, the study correlated module eigengenes with input clinical parameters through module clinical trait relationship analysis. In the reported results, nine co-expressed gene modules were identified; the yellow module was negatively correlated with age and the purple module was negatively correlated with living status. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:143-152, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:372-378]

## Hub gene identification

After module construction, WGCNA-generated edge files were exported for protein-protein interaction analysis in [[Cytoscape]]. The authors used the CytoHubba package to identify high-level genes in the network and defined the top 50 genes across modules as hub genes; the protein-protein interaction network was further analyzed with the [[STRING database|STRING]] database. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:153-162, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:378-383]

## CMAP stage

The drug-repurposing step used the GBM differential node genes derived from the WGCNA workflow. The methods state that upregulated and downregulated differential node genes were uploaded to the CMAP database in order to identify potential therapeutic drugs capable of reversing the genes of key GBM nodes. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:163-169]

In the reported output of this CMAP analysis, multiple azole compounds emerged as potential anti-GBM drugs. The table of CMAP results includes compounds such as fenbendazole, clotrimazole, sulfamethoxazole, albendazole, ronidazole, econazole, sertaconazole, mebendazole, parbendazole, niridazole, ketoconazole, sulfamethizole, sulfaphenazole, lansoprazole, and miconazole. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:383-386, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:476-493]

## Experimental follow-up of CMAP hits

To test the computational predictions, the authors selected representative azoles from three structural groups: imidazoles, triazoles, and benzimidazoles. Specifically, they tested econazole, miconazole, and ketoconazole; fluconazole, voriconazole, and posaconazole; and flubendazole, mebendazole, and fenbendazole. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:170-179, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:388-391]

Among the tested azoles, only the three benzimidazole compounds showed strong anti-GBM activity in [[U87-MG]] and [[U251-MG]] cells. The other tested imidazoles and triazoles had half-inhibition values above `10 μmol/L`, whereas flubendazole, mebendazole, and fenbendazole inhibited proliferation in a dose- and time-dependent manner, with 24-hour `IC50` values below `0.26 μmol/L` in both cell lines. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:19-23, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:392-410]

## Downstream biological characterization

RNA sequencing of flubendazole-treated U87 and U251 cells showed differential expression patterns enriched in processes including programmed cell death, regulation of cell proliferation, cell cycle, cell migration, [[NF-kappaB|NF-kB]], and [[p53]] signaling. The paper presents these findings as directions for subsequent mechanistic analysis after the initial repurposing screen. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:411-441]

The study then reports that benzimidazoles inhibited migration and invasion, altered key [[epithelial-mesenchymal transition|EMT]] markers, induced G2/M arrest through the `P53/P21/cyclin B1` pathway, triggered pyroptosis through the `NF-kB/NLRP3/GSDMD` pathway, and might concurrently induce mitochondria-dependent apoptosis. In a nude mouse U87 xenograft model, flubendazole also suppressed tumor growth without obvious adverse effects. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:22-30, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:442-471, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:472-665]

## Interpretation

Within this study, the WGCNA-to-CMAP workflow functioned as a discovery pipeline that narrowed a large GBM transcriptomic dataset into hub-gene-based signatures and then into a focused set of repurposing candidates for experimental validation. The follow-up experiments showed that the most active validated compounds among the tested azoles were benzimidazoles, especially flubendazole, mebendazole, and fenbendazole. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:64-67, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:93-112, benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:675-682]

The authors conclude that benzimidazoles are promising candidates for GBM treatment and suggest their potential development either as alternatives for patients resistant or less responsive to temozolomide, or as combination partners with temozolomide. ^[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle.md:717-755]

## Sources

- [[benzimidazoles-induce-concurrent-apoptosis-and-pyroptosis-of-human-glioblastoma-cells-via-arresting-cell-cycle]]
