---
title: "[Anchored Minimal Causal Interfaces](https://axionic.org/posts/182921145.anchored-minimal-causal-interfaces.html)"
date: 2025-12-30
layout: post
---

# [Anchored Minimal Causal Interfaces](https://axionic.org/posts/182921145.anchored-minimal-causal-interfaces.html)

**Date:** December 30, 2025  
**Batch:** Batch 30 (Posts 151–175)

## Summary
This post resolves the question left by Minimal Causal Interfaces: is coherence alone sufficient once semantic grounding is removed? The answer is no. In v0.3 MCI, a sufficiently careful pseudo-agent could construct self-consistent but fabricated decision topology satisfying all coherence checks without commitments relating to actual computation. Pure coherence verification cannot distinguish true causal explanations from explanations that are merely self-consistent. The v0.4 resolution adds minimal anchoring: kernel generates unpredictable random salt at each decision step; agent must immediately incorporate salt into factor derivation and commit; after episode concludes, kernel recomputes expected factors using revealed salts and recorded environment states, verifying committed factors match anchored computation. With anchoring, honest agents pass all checks while pseudo-agents fail deterministically—they cannot pre-fabricate salted factors or satisfy post-hoc verification. The conclusion: verifiable causal provenance requires unforgeable external anchor. Coherence alone can be fabricated; anchored coherence cannot. This demonstrates trust in opaque systems doesn't require interpretability but does require computational "skin in the game"—binding explanations to unpredictable outcomes.

## Key Concepts
- **Coherence insufficiency** – Pure internal consistency cannot distinguish true causal explanations from self-consistent fabrications.
- **Anchoring via unpredictable salt** – Kernel-generated random salt unknown until decision moment; agent must incorporate into factor derivation and commit.
- **Commitment-to-computation requirement** – Cannot fabricate consistent causal surface without performing claimed computation under verification uncertainty.
- **Post-hoc verification** – After episode, kernel recomputes expected factors using revealed salts and environment states; verifies match.
- **Binary falsifiability** – No intermediate regime where fabricated surface can remain both coherent and anchored.
- **Semantic agnosticism preserved** – Anchoring adds provenance without reintroducing semantic kernel understanding.
- **Computational skin in the game** – Must bind explanations to outcomes unpredictable without actually doing the work.
- **Unanchored opacity disqualifying** – Opacity alone acceptable; unanchored opacity is not.

## Evolution Notes
- Third marker completing conceptual loop: structural verification → minimal interfaces → anchored provenance.
- Shows pure coherence (v0.3) has theoretical boundary; resolves with minimal anchoring mechanism (v0.4).
- Establishes necessary condition (anchoring) not complete solution; explicitly leaves open probabilistic verification, stochastic systems, learned models.
- Reframes alignment again: not "make transparent" or "guess honesty" but "force commitment under adversarial uncertainty."
- Transitions Axio from philosophical conjecture to implemented mechanisms with clearly identified boundaries.

## Tags
- [anchored-causal-interfaces](../tags/anchored-causal-interfaces.md)
- [coherence-insufficiency](../tags/coherence-insufficiency.md)
- [computational-commitment](../tags/computational-commitment.md)
- [cryptographic-anchoring](../tags/cryptographic-anchoring.md)
- [provenance-verification](../tags/provenance-verification.md)
- [technical](../tags/technical.md)
- [prototype](../tags/prototype.md)
- [mci-v04](../tags/mci-v04.md)

## Cross-References



## Open Questions
- Can anchoring mechanisms be weakened while preserving verification guarantees?
- How does anchoring extend to probabilistic verification and stochastic policies?
- What anchoring approaches work for systems with genuinely learned, non-linear decision processes?
- What is the computational overhead of cryptographic anchoring at scale?
- Can adversarial agents develop strategies to satisfy anchored verification while still maintaining split-brain deception?
- How do we handle agents that legitimately need to cache certain computations for efficiency?
