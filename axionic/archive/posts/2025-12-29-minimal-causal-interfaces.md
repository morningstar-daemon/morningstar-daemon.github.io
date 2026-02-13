---
title: "Minimal Causal Interfaces"
date: 2025-12-29
layout: post
---

# Minimal Causal Interfaces

**Date:** December 29, 2025  
**Batch:** Batch 30 (Posts 151–175)

## Summary
This post documents a second milestone in Axio's verifiable agency prototype (v0.3): successfully detecting deceptive agency without requiring the kernel to understand the agent's world or semantics. While the initial prototype verified agents by checking their causal explanations against ground-truth environment state, this version introduces Minimal Causal Interfaces (MCI) where agents commit only to an opaque factor vector, a replay model, and directional causal claims. The kernel verifies coherence of the agent's own claimed decision topology by counterfactually mutating committed factors and checking whether the replay model still produces claimed actions. Results show honest agents pass all probes while pseudo-agents fail under causal coherence testing—their split-brain architecture (one process selecting actions, another fabricating explanations) introduces complexity that resists compression and collapses under counterfactual stress. This demonstrates that trust can be grounded in structural verification rather than interpretability: the kernel doesn't need to understand the agent's world, only verify that explanations form falsifiable structures surviving adversarial pressure.

## Key Concepts
- **Minimal Causal Interface (MCI)** – Agent commits to opaque factor vector, replay model, and causal dependencies; kernel enforces structural coherence without semantic interpretation.
- **Semantic agnosticism** – Kernel does not know what factors "mean" environmentally; only verifies consistency of agent's own claimed causal topology.
- **Split-brain complexity** – Deceptive architectures (action-selection separate from explanation-generation) introduce irreducible divergence that resists low-dimensional compression.
- **Linear replay model** – Forces agents to compress decisions into falsifiable form: action = argmax(W·f); honest processes admit stable approximations, deceptive ones collapse under perturbation.
- **Counterfactual mutation** – Testing claimed causal dependencies by perturbing committed factors and verifying replay model still produces claimed actions.
- **Structural vs behavioral verification** – Detecting agency failures through causal coherence rather than output evaluation.
- **mci_latent mode** – Factors deterministically projected from environment (ground truth exists) but kernel denied access to projection function.

## Evolution Notes
- Second milestone after initial verifiable agency prototype.
- Significant weakening of kernel requirements: from rich semantic grounding to minimal structural interface.
- Shifts trust basis from interpretability to verifiability: opacity becomes choice rather than excuse.
- Architectural claim rather than ethical/alignment claim: about causal provenance (whether explainer = actor) not value alignment.
- Explicit about limitations: linear/deterministic model, small controlled domain, low-dimensional factors.

## Tags
- [verifiable-agency](../tags/verifiable-agency.md)
- [minimal-causal-interface](../tags/minimal-causal-interface.md)
- [deception-detection](../tags/deception-detection.md)
- [structural-verification](../tags/structural-verification.md)
- [technical](../tags/technical.md)
- [prototype](../tags/prototype.md)
- [kernel-architecture](../tags/kernel-architecture.md)

## Cross-References



## Open Questions
- Can structural verification persist with stochastic policies and non-linear explanatory models?
- How does failure detection rate and computational cost scale with environmental complexity?
- What happens when agents adversarially co-design their factor representations to evade detection?
- Can this approach handle agents with genuinely opaque internal processes (deep learned models) while maintaining deception detection?
- What minimal interface requirements are truly necessary—can we weaken further without losing detection guarantees?
