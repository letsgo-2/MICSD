---
title: Reward design based on Robeson upper bound for CO2/N2 separation
summary: The reward function is defined from CO2 permeability and CO2/N2 selectivity using a shifted Robeson upper-bound-based score to guide optimization.
sources:
  - polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md
kind: concept
createdAt: "2026-07-17T09:58:36.844Z"
updatedAt: "2026-07-17T09:58:36.844Z"
tags:
  - reward-design
  - membranes
  - gas-separation
aliases:
  - reward-design-based-on-robeson-upper-bound-for-co2n2-separation
  - RDBORUBFCS
confidence: 0.97
provenanceState: extracted
modelId: gpt-5.4
promptVersion: v1
---

# Reward design based on Robeson upper bound for CO2/N2 separation

Reward design in the PolyRL framework uses the [[Robeson upper bound]] as the benchmark for gas separation performance when optimizing polymers for [[CO2/N2 separation]]. The task is framed to maximize CO2 permeability while maintaining low N2 permeability, and the reward function is defined as a shifted score built from CO2 permeability and selectivity. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:162-168, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:320-331]

The source gives the reward in two equivalent forms. First, it defines a shifted reward using selectivity and CO2 permeability, with Robeson upper bound parameters `a = 2.595` and `b = 0.3464` for CO2/N2 separation. It then rewrites the expression as `R(x) = (b + 1)log PCO2 - log PN2 - a + 2`, making the dependence on both gas permeabilities explicit. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:320-331]

This reward is used inside the reinforcement learning loop as the final performance score for a generated polymer, and that scalar reward is distributed across the trajectory to guide policy optimization. In the study, the reward model was the best-performing random forest, and the framework used this setup to drive multi-objective optimization toward polymers that could exceed the Robeson upper bound. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:236-239, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:293-297, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:425-433, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:459-465]

The paper notes that this design produces a two-phase optimization pattern in some algorithms: early improvements favor CO2 permeability, and later iterations shift toward improving CO2/N2 selectivity as CO2 permeability becomes harder to increase further. It also reports that REINVENT and REINFORCE were able to discover candidates surpassing the Robeson upper bound, while A2C and PPO improved permeability without equally strong selectivity gains. ^[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:477-488, polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery.md:459-465]

## Related concepts

- [[Robeson upper bound]]
- [[CO2/N2 separation]]
- [[Gas separation polymers]]
- [[Reinforcement learning]]
- [[Reward function]]
- [[Selectivity]]
- [[Permeability]]

## Sources

- [[polyrl-reinforcement-learning-guided-polymer-generation-for-multi-objective-polymer-discovery]]
