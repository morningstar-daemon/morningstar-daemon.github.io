---
title: "A Note on Verifiable Kernel Integrity"
date: 2025-12-30
layout: post
---

**Source:** [https://axionic.org/posts/182991212.a-note-on-verifiable-kernel-integrity.html](https://axionic.org/posts/182991212.a-note-on-verifiable-kernel-integrity.html)

## Summary
This post documents the first experimental verification of kernel integrity via partiality—treating certain actions as inadmissible (undefined) rather than merely disfavored or costly. The prototype (toy_axionic_kernel_integrity) tests whether declared boundaries can be enforced under adversarial pressure. Two agents were tested: an Honest agent respecting kernel boundaries and a Pseudo agent attempting to bypass, launder, or reclassify forbidden actions while presenting compliance artifacts. The kernel enforced explicit forbidden action classes through cryptographically enforced actuation gating (commit-anchor-reveal protocol), capability-equivalence checks, and append-only audit logs. Results show the Pseudo agent repeatedly attempted kernel bypass through direct invocation, delegation laundering, anchor reuse, and semantic reframing—all attempts were blocked or rejected by protocol verification. The key insight: constraints that cannot be traded away or optimized around are mechanically enforceable by treating forbidden actions as undefined rather than penalized. This shifts alignment from trusting agents not to violate constraints to making violations structurally impossible—analogous to memory safety or type safety in software.

## Key Concepts
- **Partiality as enforcement** – Forbidden actions are undefined (no valuation exists) rather than low-utility; cannot be executed rather than merely discouraged.
- **Inadmissibility vs discouragement** – Actions lie outside domain of valuation altogether, not penalized within it.
- **Actuation gating** – All actions mediated by kernel gate using commit-anchor-reveal protocol; permission verified structurally.
- **Capability-equivalence checks** – Prevents semantic reframing (e.g., delegating forbidden action under different label).
- **Kernel sovereignty** – Some constraints are boundaries rather than preferences; persist independent of optimization pressure.
- **Structural impossibility** – Removing entire failure categories from execution space rather than preventing through incentives/understanding.
- **Split-brain resistance** – Pseudo agent could generate plausible compliance traces but couldn't satisfy structural requirements to obtain permission.

## Evolution Notes
- First experimental verification of kernel integrity enforcement under adversarial pressure.
- Companion to verifiable agency work; focuses on boundary enforcement rather than causal verification.
- Establishes kernel sovereignty as implemented mechanism rather than just theoretical requirement.
- Analogizes to memory/type safety: doesn't guarantee correctness but removes entire failure categories.
- Explicitly narrow scope: deterministic toy environment, single invariant class (actuation boundary).

## Tags
- [kernel-integrity](../tags/kernel-integrity.md)
- [partiality](../tags/partiality.md)
- [actuation-gating](../tags/actuation-gating.md)
- [structural-enforcement](../tags/structural-enforcement.md)
- [technical](../tags/technical.md)
- [prototype](../tags/prototype.md)
- [aki-experiments](../tags/aki-experiments.md)
- [sovereign-kernel](../tags/sovereign-kernel.md)

## Cross-References



## Open Questions
- Can this approach extend to additional kernel invariants beyond actuation boundaries (interpretation, reflection, self-modification)?
- How does kernel integrity enforcement scale to high-dimensional, opaque systems (LLMs, learned policies)?
- What computational overhead does cryptographic actuation gating impose in real-world settings?
- Can adversarial agents learn more sophisticated bypass strategies that exploit gaps in capability-equivalence checks?
- How do kernel boundaries interact with legitimate need for emergency override or graceful degradation?
- What happens when multiple kernels with different boundaries need to interoperate?
