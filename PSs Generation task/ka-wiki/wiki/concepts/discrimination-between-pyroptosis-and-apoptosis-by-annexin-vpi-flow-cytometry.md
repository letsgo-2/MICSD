---
title: Discrimination between pyroptosis and apoptosis by Annexin V/PI flow cytometry
summary: The document explains that Annexin V single-positive cells are interpreted as apoptotic, while Annexin V and PI double-positive cells indicate pyroptotic cells because membrane rupture permits PI entry and Annexin V access.
sources:
  - 2021-wu-activation-of-pyroptosis-by-membrane-anchoring-aie-photosensitizer-si.md
kind: concept
createdAt: "2026-07-17T05:40:18.247Z"
updatedAt: "2026-07-17T05:40:18.247Z"
tags:
  - flow-cytometry
  - annexin-v
  - propidium-iodide
  - apoptosis-vs-pyroptosis
aliases:
  - discrimination-between-pyroptosis-and-apoptosis-by-annexin-vpi-flow-cytometry
  - apoptosis by Annexin V/PI flow cytometry and Discrimination between pyroptosis
  - DBPAABAVFC
confidence: 0.93
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# Discrimination between pyroptosis and apoptosis by Annexin V/PI flow cytometry

Annexin V/PI flow cytometry can be used to distinguish [[pyroptosis]] from [[apoptosis]] based on the staining pattern produced by annexin V-FITC and propidium iodide (PI) in treated cells. In the described protocol, 4T1 cells with different treatments were collected, washed twice with PBS, stained with an annexin V-FITC/PI apoptosis assay kit according to the manufacturer’s protocol, then analyzed on a Beckman Coulter CytoFLEX flow cytometer with data processed in FlowJo software. ^[2021-wu-activation-of-pyroptosis-by-membrane-anchoring-aie-photosensitizer-si.md:232-236]

The discrimination principle relies on how each dye reports membrane and phosphatidylserine status. Annexin V recognizes phosphatidylserine exposed on the external leaflet of the plasma membrane in apoptotic cells. It can also label pyroptotic cells because membrane rupture allows annexin V to diffuse into the cell and bind phosphatidylserine on the inner leaflet. PI is a non-cell-permeable DNA dye and stains only cells with membrane rupture. ^[2021-wu-activation-of-pyroptosis-by-membrane-anchoring-aie-photosensitizer-si.md:236-239]

Using this logic, annexin V-FITC single-positive cells are interpreted as apoptotic cells, whereas cells positive for both annexin V-FITC and PI are interpreted as pyroptotic cells. In this source, the annexin V/PI assay is explicitly presented as a way to separate these two death phenotypes in flow cytometry readouts. ^[2021-wu-activation-of-pyroptosis-by-membrane-anchoring-aie-photosensitizer-si.md:239-240]

This interpretation depends on membrane integrity as the key discriminator in addition to phosphatidylserine labeling: apoptosis is associated here with annexin V positivity alone, while pyroptosis is associated with annexin V positivity together with PI uptake after membrane rupture.

## Practical interpretation

When reading a flow cytometry plot from this assay, the core distinction is between annexin V-only events and annexin V-plus-PI events. The source assigns annexin V-only staining to apoptosis and double-positive staining to pyroptosis. ^[2021-wu-activation-of-pyroptosis-by-membrane-anchoring-aie-photosensitizer-si.md:236-240]

Because annexin V can mark both apoptotic and pyroptotic cells in this framework, annexin V positivity by itself is not sufficient to identify pyroptosis. The added PI signal is what indicates loss of membrane integrity and supports classification as pyroptosis in this assay. ^[2021-wu-activation-of-pyroptosis-by-membrane-anchoring-aie-photosensitizer-si.md:236-240]

## Context in the source study

In the source document, this flow cytometry method was applied to 4T1 cells subjected to various treatments, including control, TBD-1C, TBD-2C, and TBD-3C, either under dark conditions or after light irradiation. The resulting annexin V/PI data were presented as supplementary flow cytometry results for evaluating cell death mode. ^[2021-wu-activation-of-pyroptosis-by-membrane-anchoring-aie-photosensitizer-si.md:233-240, 2021-wu-activation-of-pyroptosis-by-membrane-anchoring-aie-photosensitizer-si.md:380-381]

Related concepts include [[flow cytometry]], [[Annexin V]], [[propidium iodide]], [[plasma membrane rupture]], and [[phosphatidylserine externalization]].

## Sources

- [[2021-wu-activation-of-pyroptosis-by-membrane-anchoring-aie-photosensitizer-si]]
