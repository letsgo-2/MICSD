---
title: Transformer-based generative models outperform simpler sequence models in PolyRL
summary: GPT-2 and LLaMA-2 produced better late-stage selectivity, permeability, novelty, and top scores than GRU and LSTM in the reinforcement learning loop.
sources:
  - polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md
kind: concept
createdAt: "2026-07-17T09:58:54.823Z"
updatedAt: "2026-07-17T09:58:54.823Z"
tags:
  - transformers
  - generative-models
  - benchmarking
aliases:
  - transformer-based-generative-models-outperform-simpler-sequence-models-in-polyrl
  - TGMOSSMIP
confidence: 0.93
provenanceState: merged
modelId: gpt-5.4
promptVersion: v1
---

# Transformer-based generative models outperform simpler sequence models in PolyRL

In PolyRL, the authors compared four autoregressive generative architectures for gas-separation polymer generation under the same reinforcement-learning setup: [[GPT-2]], [[LLaMA-2]], [[LSTM]], and [[GRU]]. The comparison was conducted using [[Random Forest]] as the reward model and [[REINVENT]] as the reinforcement-learning algorithm. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:561-566]

The reported result is that the transformer-based models, GPT-2 and LLaMA-2, achieved stronger multi-objective generation performance than the simpler recurrent sequence models, LSTM and GRU. In later stages of reinforcement-learning optimization, GPT-2 and LLaMA-2 generated polymers with higher [[CO2 permeability]] and higher [[CO2/N2 selectivity]], whereas LSTM and GRU mainly improved CO2 permeability and did not significantly improve selectivity. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:567-574]

Across the broader generation metrics, GPT-2 and LLaMA-2 also produced the best `Top100` scores and maximum scores, and both had the highest molecule and scaffold novelty among the four tested generators. The paper interprets this as evidence that transformer models, through their global attention mechanism, can better focus on relevant substructure information and explore the gas-separation polymer search space more comprehensively, improving both novelty and overall score. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:574-583]

This advantage appears in the study’s final conclusions as well. The authors state that integrating transformer-based generative models, especially GPT-2 and LLaMA-2, significantly enhanced the quality and novelty of the generated polymers within the PolyRL framework. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:678-691]

The source also reports that all four generators were first pre-trained on next-token prediction over a dataset of 1 million P-SMILES strings. On the validity metric used during pre-training evaluation, GRU and LLaMA2 reached 100% validity, LSTM reached 98.44%, and GPT2 reached 94.53%. Even so, the later reinforcement-learning experiments favored the transformer-based models on the more important downstream generation objectives rather than raw validity alone. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:377-396, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:437-440, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:567-583]

## Related concepts

- [[PolyRL]]
- [[Reinforcement learning]]
- [[Generative model]]
- [[GPT-2]]
- [[LLaMA-2]]
- [[LSTM]]
- [[GRU]]
- [[REINVENT]]
- [[Random Forest]]
- [[CO2 permeability]]
- [[CO2/N2 selectivity]]
- [[P-SMILES]]

## Sources

- [[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery]]
