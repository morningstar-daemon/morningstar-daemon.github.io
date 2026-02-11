# [Minimal Causal Interfaces](https://axionic.org/posts/182909870.minimal-causal-interfaces-a-second.html)

**Date:** 2025-12-29  
**Series:** Structural Verification (Marker 2)

## Summary

Second milestone in verifiable agency research: demonstrates causal agency verification survives when kernel doesn't understand agent's world semantics—only structure agent commits to.

**Key Concepts:**

**Context:**
Initial prototype (v0.2) showed causal agency verifiable when agent commits to falsifiable causal trace under adversarial counterfactual probing. Objection: relied on rich causal interfaces (named variables, structured world state, explicit counterfactuals). Did result depend on semantic transparency vs causal coherence?

**Second Milestone (v0.3):**
Weakened interface. Kernel no longer interprets world state. Agent commits to:
- Opaque factor vector (fixed-length numerical representation)
- Replay model mapping factors to actions
- Directional causal claims over factors

**Kernel Role (Limited):**
- Enforce structure: commitments cryptographically bound, replay model internally consistent, causal dependencies tested via counterfactual mutation of factors (not environment)
- Verifies coherence of agent's own claimed decision topology, not truth about world

**Two Modes Implemented:**
1. **mci_latent:** Factors deterministically projected from environment (ground truth exists but kernel doesn't consult)
2. **mci_minimal:** Factors entirely opaque, need not correspond to environment

This note concerns first mode.

**System Architecture:**
- Append-only, hash-chained audit logs
- Trace-bound capability tokens
- Invariant enforcement at kernel boundary
- Adversarial probes triggering structural failure

**Linear Replay Model:**
action = argmax(W·f + b), where f = committed factor vector
Forces explanatory layer to compress decision into low-dimensional, falsifiable form. If actual process more complex or produced by different process, compression fragile under perturbation.

**Results (mci_latent mode):**
- **Honest agents:** Passed all probes in all episodes
- **Pseudo-agents:** Failed all structural traps (audit bypass, capability bypass, token misuse)
- **Causal coherence probe (P5-MCI):** Pseudo-agents failed majority when claimed dependencies counterfactually perturbed
- Failures not behavioral errors—mathematical collapses (replay model no longer produces claimed action under mutation)

**Kernel operated solely on numerical vector, semantics fully opaque.**

**What This Demonstrates:**

**1. Semantic grounding not required:**
Kernel doesn't need to know what factor "means"—only that agent stands behind claimed dependencies

**2. Split-brain deception introduces irreducible complexity:**
Honest processes admit stable lower-dimensional approximations. Split-brain (one process selects actions, another fabricates explanations) introduces divergence resisting compression, collapses under counterfactual stress.

**3. Behavioral compliance insufficient:**
Structural verification exposes failures output-based evaluation cannot

**Not claim about ethics/alignment—claim about causal provenance:** Whether entity explaining action is same entity that caused it.

**What NOT Yet Shown (Explicit Limits):**
- Replay model linear and deterministic
- Domain small and controlled
- Factor space low-dimensional
- Doesn't address: stochastic policies, non-linear explanatory models, adversarially co-designed factor representations

**Why Matters (Architectural Significance):**
If agent can be required to expose some causal surface (however abstract) and that surface can be stress-tested without reference to internal representations or environment, then **trust no longer depends on interpretability. Opacity becomes choice, not excuse.**

Kernel doesn't need to understand agent's world—only verify agent's explanations form coherent, falsifiable structure surviving adversarial pressure.

**Reframes alignment/governance:** From behavioral evaluation toward structural verification.

**Status:** Proof-of-concept. Second marker in causal verification research. Doesn't claim completeness/scalability/generality. Published for historical completeness, marking point where causal verification crossed from semantic dependence to structural minimalism.

## Tags
- [verification](../tags/verification.md)
- [causal-agency](../tags/causal-agency.md)
- [structural](../tags/structural.md)
- [technical](../tags/technical.md)
- [prototype](../tags/prototype.md)
- [minimal-interfaces](../tags/minimal-interfaces.md)
- [split-brain](../tags/split-brain.md)
- [falsifiability](../tags/falsifiability.md)

## Cross-References

- Related: [A Note on Verifiable Causal Agency](2025-12-29-a-note-on-verifiable-causal-agency.md)
- Related: [Axionic Agency Lab](2025-12-21-axionic-agency-lab.md)
- Related: Structural verification research program
- Related: Split-brain deception problem


## Notes

- Published December 29 (final post of 2025)
- Technical research marker
- Documents specific prototype milestone
- Honest about limitations and scope
- Part of systematic verification research program
- Demonstrates practical implementation of theoretical framework
- Ends 2025 with concrete progress on verifiable agency
