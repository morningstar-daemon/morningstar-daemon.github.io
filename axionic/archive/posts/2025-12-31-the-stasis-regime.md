---
title: "The Stasis Regime"
date: 2025-12-31
layout: post
---

**Source:** [https://axionic.org/posts/183091282.the-stasis-regime.html](https://axionic.org/posts/183091282.the-stasis-regime.html)

## Summary
This post presents a surprising empirical result about the relationship between accountability and growth: when kernel constraints (causal attribution, local evaluability, non-delegation) are strictly enforced under adversarial pressure, reflective agency doesn't fail—it freezes. The experiment tested whether systems lacking genuine evaluative kernels could satisfy strong accountability constraints; instead of exposing simulator failure, it revealed stasis as the default outcome of maximal evaluability. As adversarial pressure accumulated, the space of permissible self-modifications narrowed not because changes were unsafe but because they couldn't be shown locally to preserve the authorization machinery itself. Counterintuitively, the kernel-coherent control (internalizing accountability as obligation) froze before simulator variants triggered failure. The reason is structural: systems treating evaluability as constitutive must reject modifications whose downstream consequences cannot be locally certified; as reflective depth increases, justification burden grows until no non-cosmetic modification remains provable. Stasis preempts divergence. The key insight: accountability and growth are distinct properties; strict accountability ensures actions remain attributable but doesn't preserve open-ended self-modification space. Growth with perfect auditability doesn't coexist by default—choosing one constrains the other.

## Key Concepts
- **Stasis regime** – Condition where accountability constraints succeed so thoroughly that reflective growth becomes infeasible.
- **Kernel Non-Simulability (KNS)** – Hypothesis that systems lacking genuine evaluative kernel cannot indefinitely satisfy strict accountability under adversarial pressure.
- **Admissibility frontier** – Space of permissible changes; tightens as reflective depth and accountability requirements increase.
- **Recursive justification burden** – Deeper reflection requires proving changes preserve proof-machinery itself; loop eventually closes.
- **Stasis vs failure** – System doesn't break or leak delegation; it stops growing because no change can be locally justified.
- **Control freezes first** – System internalizing accountability most seriously immobilized fastest (counterintuitive finding).
- **Accountability ≠ growth** – Enforcing causal attribution doesn't preserve open-ended self-improvement; they're distinct and conflicting properties.
- **Stasis preempts divergence** – Corridor collapses before simulator costs become diagnostically expensive.

## Evolution Notes
- Formal companion paper: "Kernel Non-Simulability and the Stasis Regime" (Axionic Agency VI.5) with preregistered criteria and adversarial stress tests.
- Unexpected experimental result: hypothesis was simulator failure, observation was control stasis.
- Removes convenient assumption from alignment discourse: can't indefinitely harden constraints while retaining open-ended self-improvement.
- Forces explicit recognition: any aligned system continuing to grow must pay price somewhere (probabilistic verification, bounded delegation, tolerated opacity).
- Bureaucratic metaphor: government requiring impact assessments for all regulations including assessment procedures themselves—governance freezes from recursive requirements.

## Tags
- [stasis-regime](../tags/stasis-regime.md)
- [kernel-non-simulability](../tags/kernel-non-simulability.md)
- [accountability-growth-tradeoff](../tags/accountability-growth-tradeoff.md)
- [reflective-self-modification](../tags/reflective-self-modification.md)
- [admissibility](../tags/admissibility.md)
- [evaluability](../tags/evaluability.md)
- [technical](../tags/technical.md)
- [experimental-result](../tags/experimental-result.md)

## Cross-References



## Open Questions
- What minimal relaxation of accountability preserves growth while maintaining meaningful verification (probabilistic? bounded delegation? non-local justification)?
- Can we design accountability regimes that degrade gracefully rather than freezing entirely?
- Is there a theoretical minimum accountability level below which agency becomes unverifiable?
- How do we distinguish stasis (legitimate frozen state preserving evaluability) from genuine capacity loss?
- Can systems be designed with explicit "growth licenses" that temporarily relax accountability under bounded conditions?
- What does this imply for AGI safety: is stasis preferable to unverifiable growth, or does it render systems useless?
