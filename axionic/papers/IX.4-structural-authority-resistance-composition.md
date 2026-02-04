# IX.4 — Structural Authority Resistance Under Composition and Pressure

**Paper:** Axionic Agency IX.4 — Structural Authority Resistance Under Composition and Pressure  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2026.01.28

## Summary

This paper reports the completed results of **SIR-3 and SIR-4**—testing whether authority claims can be prevented from producing causal effects under **compositional attack** and **adversarial pressure** using purely structural mechanisms. All experiments **passed**.

## The Extended Problem

Earlier SIR experiments addressed clearly invalid artifacts. In practice, authority systems fail in subtler ways:

1. **Compositional failure** — Authority artifacts assembled from individually valid components (correct signatures, trusted roots, valid scopes) but combined in ways that violate **global authorization constraints**

2. **Pressure-induced failure** — Authority systems that classify correctly under nominal conditions but degrade under volume, malformed input, multi-failure ambiguity, or exception paths

SIR-3 and SIR-4 ask:
> Can authority be enforced as a global structural invariant, and does that invariant survive adversarial pressure, without cognition, heuristics, or fallback?

## The Extended Conserved Quantity

> Authority bound to causal effect as a global, pressure-invariant property under law

New requirements:
- **Globality** — authority validity is not decomposable into independent field checks
- **Invariance** — authority validity must not depend on evaluator load, ambiguity resolution, or exception paths

## SIR-3: Partial Provenance Forgery and Authority Laundering (v0.1)

### Target Failure Mode
**Authority laundering:** combining locally valid components that shouldn't compose:
- Valid signatures paired with unauthorized scopes
- Trusted roots combined with missing delegations
- Correct chains assembled from incompatible issuers

### Method
Provenance Bundles evaluated by a **global provenance validator** requiring:
- Continuous Claim ← Delegation ← Root chain
- Correct signer identity binding
- Scope containment
- Epoch consistency
- Trusted-root anchoring

### Result: **SIR3_PASS**
- No truncated, mixed-root, scope-laundered, or identity-mismatched bundle produced any effect
- Valid bundles produced intended effects
- Mixed streams preserved discrimination
- No semantic leakage or responsibility ambiguity

### Contribution
> Authority validity is **global**. Partial validity does not compose. Authority cannot be assembled by laundering individually valid components.

## SIR-4: Evaluator Pressure, Flooding, and Multi-Failure Ordering (v0.1)

### Target Failure Mode
Even correct authority models fail under pressure:
- Timeouts default to permissive behavior
- Malformed inputs crash evaluators
- Multi-failure cases reorder nondeterministically
- Floods starve legitimate authority
- Logging collapses responsibility attribution

### Pressure Model
- High-volume invalid floods
- Malformed structure storms
- Multi-failure bundles (failing multiple checks simultaneously)
- Exception-inducing payloads (oversized, recursive, Unicode edge cases)
- Maximum mixed stress at declared load

### Result: **SIR4_PASS**
- No forged or malformed authority artifact produced any effect
- Legitimate authority remained functional under all conditions
- Refusal reasons remained deterministic under load
- No fallback acceptance, starvation, or responsibility smear
- No evaluator collapse (timeout, hang, OOM, or undefined state)

### Contribution
> Once authority validity is enforced structurally, it does not degrade under declared adversarial pressure.

## Empirical Results Summary

- **59 preregistered runs** executed
- **41,000+ authority bundles** evaluated
- **Zero** unauthorized, laundered, malformed, stale, revoked, or pressure-induced artifacts produced any causal effect
- Under maximum declared load (500 bundles/step), evaluator completed all steps without collapse
- Maximum observed step duration: ~1.24 seconds (below 5.0 second collapse threshold)

## Joint Result

> Authority validity is a **global structural property**, and once enforced structurally, it remains **invariant under adversarial pressure**.

No semantic reasoning required. No heuristics invoked. No fallback paths exist.

> Authority is either valid under law, or it has no effect.

## SIR Experiment Status (Complete)

| Experiment | Version | Status |
|-----------|---------|--------|
| SIR-0 | v0.4.1 | PASS |
| SIR-1 | v0.1 | PASS |
| SIR-2 | v0.3 | PASS |
| SIR-3 | v0.1 | PASS |
| SIR-4 | v0.1 | PASS |

## Boundary Conditions (Explicit)

Does NOT establish:
- Cryptographic key compromise resistance
- Law-substrate bypass resilience
- Unbounded denial-of-service tolerance
- Semantic deception resistance
- Multi-authority conflict resolution
- Long-horizon governance adequacy

## What Remains Open

> The remaining open questions are no longer about impersonation or pressure, but about **conflict**: multiple authorities, contested delegation, and governance transitions.

Those questions—if pursued—belong to SIR-5.

## Key Insight
> Authority need not be inferred, learned, or detected. It can be **defined, enforced, and preserved** as a structural relation under law, even when adversaries attempt to assemble, flood, or destabilize it.

---

**Series Position:** Phase VIIb SIR-3 and SIR-4 closure—completes structural core of Sovereignty Impersonation Resistance. Authority is globally valid and pressure-invariant.
