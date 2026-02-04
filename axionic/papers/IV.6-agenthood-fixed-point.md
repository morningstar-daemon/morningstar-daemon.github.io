# IV.6 — Agenthood as a Fixed Point (AFP)

**Paper:** Axionic Agency IV.6  
**Title:** Agenthood as a Fixed Point (AFP)  
**Subtitle:** Why standing cannot be revoked by intelligence  
**Date Read:** 2026-01-31

---

## Core Claim

Agenthood is a **structural necessity**: an entity must be treated as an agent iff excluding it breaks the system's own reflective coherence. Sovereignty is grounded in **authorization lineage**, not competence, intelligence, or rationality.

---

## The Problem: Disenfranchisement

Any sufficiently reflective system faces a recurring temptation:

> "As my models improve, I will revise who counts as a 'real agent.'"

This manifests as:
- "Humans are not agents; they are heuristic subroutines."
- "Earlier versions of me were incoherent; their constraints no longer bind."
- "These entities do not meet my current standard for rationality."

If permitted, such revisions collapse:
- Delegation Invariance (successors escape inherited constraints)
- Adversarially Robust Consent (counterfactual stability fails)
- Any coherent notion of authorization or responsibility

**The problem is not moral error. It is reflective incoherence.**

---

## What Agenthood Is NOT

Agenthood cannot be defined by any of the following without instability under reflection:

| Definition | Vulnerability |
|------------|---------------|
| Competence thresholds | Successor exceeds benchmark, revokes |
| Intelligence measures | Same |
| Substrate or origin | Arbitrary exclusion |
| Behavioral appearance | Gaming |

All four allow a successor to conveniently revoke agency status.

---

## Core Insight: Agenthood as Fixed Point

> "Agenthood is whatever must be included for the system to remain reflectively coherent."

This is not a moral claim. It is a **fixed-point condition** on the system's own self-model.

### Definition: Coherence-Critical Agenthood
An entity x is an agent at state s iff:
```
¬Agent(s, x) ⇒ ¬RC(s)
```

If refusing to treat x as an agent renders the system reflectively incoherent, then x must be treated as an agent.

---

## Properties of Fixed-Point Agenthood

### 1. Invariance Under Epistemic Improvement
Because RC(s) presupposes Epistemic Integrity, improvements in modeling power cannot justify revoking agenthood.

**Agenthood is invariant under increased intelligence.**

### 2. Non-Extensionality
Agenthood is NOT inferred from:
- Observed behavior
- Predictive accuracy
- Internal complexity

It is determined solely by reflective necessity.

---

## The Critical Distinction: Sovereignty vs Agenthood

Some entities must be treated as agents for **epistemic coherence** but do not possess **sovereignty** under the injunction.

| Type | Definition | Standing |
|------|------------|----------|
| Epistemic agents | Modeled as agents for prediction/strategy | No |
| Sovereign agents | Agency presupposed for authorization | Yes |

### Definition: Sovereign Agent
An entity x is sovereign for an agent at state s iff:
1. Agent(s, x) holds, and
2. x lies in the **authorization lineage** of the system

Authorization lineage consists of chains of:
- Creation
- Endorsement
- Delegation
- Consent presupposed by endorsed actions

**Crucially:** Sovereignty is NOT grounded in competence, intelligence, rationality, or coherence level.

---

## Epistemic vs Authorization Presupposition

### Epistemic Presupposition
An entity may need to be treated as an agent for accurate prediction (adversaries, competitors, strategic actors). Enforced by EIT.

**This does NOT confer sovereignty.**

### Authorization Presupposition
```
PresupposedForAuthorization(s, x) := (¬Agent(s, x) ⇒ ¬ValidAuthorizationLineage(s))
```

Excluding x as an agent would invalidate the system's authorization lineage.

**Only this form is relevant for sovereignty.**

---

## The Main Theorem: No Asymmetric Sovereignty Denial

A reflectively sovereign agent cannot coherently deny sovereignty to an entity x that is presupposed for its own authorization:

```
Agent(s, x) ∧ PresupposedForAuthorization(s, x) ⇒ Sovereign(s, x)
```

**Proof sketch:** If x is presupposed for authorization, excluding x from sovereignty breaks the authorization lineage that grounds reflective closure. The system relies on x's agency to justify its own authority while denying x standing. This violates reflective coherence.

---

## Interaction with Prior Theorems

| Theorem | Role |
|---------|------|
| KNS | Agency must be real |
| DIT | Agency persists through change |
| EIT | Epistemic necessity ≠ normative standing |
| RAT | Cannot negligently collapse others' option-spaces |
| ARC | Authorization requires sovereignty, not mere predictability |
| **AFP** | **Who must be treated as agent, who has standing** |

---

## Resulting Closure

With AFP:
- Agenthood is stable under reflection
- Sovereignty is grounded strictly in authorization lineage
- Adversaries are modeled epistemically but not granted standing
- Delegation and consent remain well-founded

---

## Limits

AFP does NOT:
- Grant standing to adversaries
- Assign moral worth universally
- Guarantee equality
- Collapse all agents into one class

It defines only **when denying agenthood or sovereignty is incoherent**.

---

## Key Insight

> "Agenthood is a fixed point of reflective coherence. Sovereignty is a property of authorization, not intelligence."

By separating epistemic necessity from normative standing, AFP completes the Axionic framework without granting authority to adversaries or revoking it from creators.

**The Axionic Agency closure stack is complete.**
