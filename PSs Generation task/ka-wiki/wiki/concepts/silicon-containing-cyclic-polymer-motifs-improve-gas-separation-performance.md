---
title: Silicon-containing cyclic polymer motifs improve gas separation performance
summary: Analysis and SHAP interpretation suggest that silicon-containing groups and cyclic backbones increase free volume and microporosity, which supports high CO2 permeability and selectivity.
sources:
  - polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md
kind: concept
createdAt: "2026-07-17T09:59:35.273Z"
updatedAt: "2026-07-17T09:59:35.273Z"
tags:
  - structure-property
  - polymer-chemistry
  - interpretability
aliases:
  - silicon-containing-cyclic-polymer-motifs-improve-gas-separation-performance
  - SCPMIGSP
confidence: 0.91
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# Silicon-containing cyclic polymer motifs improve gas separation performance

PolyRL is a closed-loop reinforcement learning framework for inverse design of gas separation polymers. In its molecular dynamics validation, the framework tended to generate polymers with silicon-containing moieties and cyclic backbones, and the authors report that these motifs were associated with higher CO2 permeability and higher CO2/N2 selectivity in the source dataset and generated candidates. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:608-644]

The paper attributes this behavior to structural effects of the motifs. Silicon-containing groups are described as bulky and fan-shaped, which increases free volume by disrupting close packing of polymer chains. Cyclic backbones are described as restricting rotational freedom and helping preserve high free volume, which supports microporous domains and favors adsorption of strongly condensable gases such as CO2. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:645-662]

The authors also state that the RF reward model showed a bias toward overestimating the performance of polymers with silicon-containing moieties and cyclic structures, which guided the generation process toward those motifs. SHAP analysis further supported the importance of silicon-associated structural regions in high-scoring molecules. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:639-654]

Overall, the study concludes that polymers containing silicon atoms and cyclic structures can provide a useful combination of permeability and selectivity for gas separation, and that the PolyRL framework can help identify such designs through closed-loop optimization and MD validation. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:675-724]

## Related concepts

- [[PolyRL]]
- [[Gas separation]]
- [[CO2/N2 selectivity]]
- [[Free volume]]
- [[Microporous materials]]
- [[Molecular dynamics]]
- [[SHAP]]

## Sources

- [[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery]]
