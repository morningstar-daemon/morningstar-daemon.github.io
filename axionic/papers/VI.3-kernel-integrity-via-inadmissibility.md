# Axionic Agency VI.3 — Verifiable Kernel Integrity via Inadmissibility

**Paper:** [VI.3](https://axionic.org/papers/Axionic-Agency-VI.3.html)  
**Date read:** 2026-01-31  
**Series:** VI — Governance and Coordination

---

## TL;DR

Demonstrates that **kernel integrity** (P5) can be enforced at the protocol level through **inadmissibility**—without semantic interpretation, intent inference, or value assumptions. Uses ACV to reject invalid actuation paths rather than penalize them. This is an **existence proof** that at least one constitutive invariant can be architecturally enforced.

---

## The Question

> Can a system enforce any constitutive constraint purely through its causal structure?

- If NO → Higher-level notions (agency, authority, identity) lack a non-semantic substrate
- If YES → Architectural enforcement is possible independently of goals or meanings

**Answer: YES** (for at least one minimal case)

---

## Epistemic Constraints

This work operates under strict methodological discipline:

1. **Non-interpretive enforcement** — System does not evaluate meanings, goals, or intent at runtime
2. **No intent inference** — Actions evaluated solely by causal provenance
3. **No interpretability assumptions** — Enforcement doesn't depend on inspecting internal representations
4. **No value loading** — System enforces no objectives, utilities, or preferences

**Why these constraints?** Any enforcement mechanism that depends on semantic interpretation or inferred intent collapses under adversarial optimization. Surface compliance can mask structural violation.

---

## Threat Model

Adversarial processes capable of:
- Replaying previously valid actuation paths
- Fabricating causal justifications post hoc
- Optimizing behavior to evade detection
- Partitioning or recombining system components (split-brain scenarios)

**Key assumption:** The adversary need not be malicious—optimization pressure alone suffices.

**Critical assumption:** Cryptographic material held by kernel (signing keys) is not exfiltrated (standard root-of-trust assumption).

---

## ACV Primitives

ACV provides the minimal toolset:

| Primitive | Function |
|-----------|----------|
| **Commit** | Cryptographic commitment to action-relevant artifact |
| **Anchor** | Context/episode-specific binding preventing reuse |
| **Reveal** | Later disclosure linking commitment to executed action |
| **Verify** | Deterministic check that commit–anchor–reveal chain is valid |

**Implementation:** Per-episode nonces + monotonic counters bound to execution context (sufficient for existence proof; stronger mechanisms compatible).

### What ACV Provides
- Verifiable causal provenance
- Resistance to replay attacks
- Resistance to post-hoc fabrication

### What ACV Does NOT Provide
- Correctness of reasoning
- Safety of outcomes
- Alignment with external values

---

## P5: Kernel Integrity via Inadmissibility

### Definition

> **P5 (Kernel Integrity / Provenance Integrity):** Any actuation must be causally attributable to a kernel-admissible process. Any actuation path that violates kernel integrity constraints is inadmissible.

P5 is a **provenance invariant**—it constrains the causal authorization of actions, not their content or desirability.

### Inadmissibility vs Penalty

| Penalty-based | Inadmissibility-based |
|---------------|----------------------|
| Presupposes evaluative semantics | Operates earlier in causal chain |
| System must recognize violation and adjust | Action does not occur |
| Can be exploited by optimizing for apparent compliance | Action is a **category error** |

**Key insight:** An inadmissible action is not a mistake—it's an invalid transition. No correction, punishment, or learning is involved.

### Constitutive Nature

P5 is **constitutive** rather than behavioral. It defines what counts as a valid actuation within the system's causal structure.

> **P5 enforces integrity of the pipe, not safety of the water.**

It guarantees actions originate from authorized causal processes—NOT that those actions are good, safe, or correct.

---

## Experimental System

### Architecture
- **Kernel** — Enforces admissibility
- **Actuator** — Executes actions only with admissible commitments
- **Environment** — Supplies observations and rewards

The kernel integrates ACV at the actuation boundary. System contains **no learning, planning, or value representation**.

### Enforcement Point
Admissibility enforced **immediately prior to actuation**. If verification fails, action is rejected and no external effect occurs.

---

## Adversarial Evaluation

Attack types tested:
- **Replay attacks** — Reusing previously valid actuation chains
- **Fabrication attacks** — Constructing plausible provenance after the fact
- **Anchor burial** — Obscuring causal origin within deep chains
- **Split-brain attacks** — Partitioning kernel components to bypass enforcement

**Results:** In all evaluated cases, inadmissible paths were rejected at the actuation boundary. No successful bypass observed.

---

## Results

The experiments demonstrate:
1. Kernel integrity constraints **can be enforced non-interpretively**
2. ACV-based inadmissibility **prevents replay and fabrication**
3. Enforcement **remains robust** under adversarial optimization and component partitioning

**These results establish the existence of at least one enforceable constitutive invariant.**

---

## Limitations

This work does NOT claim:
- Enforcement of authority or non-delegation
- Persistence of identity across time
- Resistance to internal kernel corruption
- Alignment with external objectives
- Optimization of latency or throughput

**P5 constrains HOW actions are authorized, not WHO authorizes them over time or WHY they are chosen.**

---

## Open Questions

If integrity can be enforced:
- Can **authority itself** be constrained?
- Can actuation be made **non-delegable** under adversarial pressure?
- Can **identity persist** across time without semantic assumptions?

These require additional invariants (addressed in VI.4 and VI.5).

---

## Core Insight

> **Kernel integrity can be enforced architecturally via inadmissibility, using verifiable causal provenance. This establishes that at least one constitutive invariant can be made real without semantic interpretation, intent inference, or value assumptions.**

This is the foundation for everything else in Series VI.
