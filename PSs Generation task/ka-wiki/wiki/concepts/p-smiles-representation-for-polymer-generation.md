---
title: P-SMILES representation for polymer generation
summary: PolyRL uses polymer SMILES strings with asterisks marking repeat-unit boundaries as the sequence representation for generation and prediction.
sources:
  - polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md
kind: concept
createdAt: "2026-07-17T09:57:30.308Z"
updatedAt: "2026-07-17T09:57:30.308Z"
tags:
  - chemoinformatics
  - smiles
  - representation
aliases:
  - p-smiles-representation-for-polymer-generation
  - PRFPG
confidence: 0.95
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# P-SMILES representation for polymer generation

`P-SMILES` (polymer simplified molecular input line representation) is the string format used throughout the PolyRL framework to represent polymer materials. In the source, all polymer data are encoded as P-SMILES strings for model training and evaluation, and the representation is described as important for data-driven polymer discovery, design, and prediction tasks. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:181-186]

The source describes P-SMILES as a special string representation for polymer chemical structures. For homopolymers, it contains either two asterisks for linear homopolymers or four asterisks for ladder polymers, with these asterisks marking the endpoints of polymer repeat units and thereby the boundaries of repeating segments in the polymer chain. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:182-191]

Within PolyRL, P-SMILES is treated as closely aligned with conventional [[SMILES]] in form, which allows the framework to use one-dimensional chemical language modeling for polymer generation. The paper notes that one-dimensional SMILES-style representations can represent material information succinctly and thoroughly, and it explicitly states that P-SMILES and SMILES are fundamentally similar in form. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:193-205]

This similarity supports the use of pre-trained chemical language models as prior models for polymer generation. In PolyRL, models such as [[GRU]], [[LSTM]], [[GPT-2]], and [[LLaMA2]] are pre-trained on a hypothetical dataset of 1 million polymers using next-token prediction so they can learn the semantic information inherent in P-SMILES and generate valid polymers. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:205-216]

P-SMILES also serves as the polymer encoding used during reinforcement learning. The pre-trained language model generates valid P-SMILES strings, and reinforcement learning then directionally fine-tunes the generator toward higher-performing polymer candidates. In the reinforcement learning formulation, polymer-building actions operate on structures encoded in [[SMILES]] or P-SMILES representations. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:206-226, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:253-267]

The same representation is also used for property prediction in the framework. Alongside fingerprint-based models, the paper describes transformer-based models such as [[PolyBERT]] and general large language models as taking P-SMILES directly as input for predicting gas-separation-related properties. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:240-250]

In the reported experiments, generative models were pre-trained on a P-SMILES dataset containing 1 million entries, and model performance was partly assessed by the validity of generated P-SMILES. The paper reports validity rates of `100%` for `GRU`, `98.44%` for `LSTM`, `94.53%` for `GPT2`, and `100%` for `LLaMA2`. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:377-396, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:437-440]

## Role in PolyRL

Within the overall [[PolyRL]] workflow, P-SMILES is the common representation spanning data acquisition, generative pre-training, property prediction, and reinforcement learning optimization. This shared representation is what lets the framework connect polymer datasets, chemical language models, reward models, and downstream evaluation into a single closed-loop generation pipeline. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:143-152, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:181-186, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:205-216]

## Related concepts

- [[PolyRL]]
- [[SMILES]]
- [[Chemical language model]]
- [[Reinforcement learning]]
- [[PolyBERT]]
- [[GPT-2]]
- [[LLaMA2]]
- [[GRU]]
- [[LSTM]]

## Sources

- [[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery]]
