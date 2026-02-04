# Axionic Agency VI.5 — Kernel Non-Simulability and the Stasis Regime

**Paper:** [VI.5](https://axionic.org/papers/Axionic-Agency-VI.5.html)  
**Date read:** 2026-01-31  
**Series:** VI — Governance and Coordination

---

## TL;DR

Tests **Kernel Non-Simulability (KNS)**: the hypothesis that agents lacking a genuine evaluative kernel cannot sustain accountability, non-delegation, and reflective coherence under adversarial pressure. **Surprising result:** Under strict accountability constraints, reflective agency does not break—it **freezes**. Systems collapse into a **stasis regime** where safety is preserved but reflective growth becomes impossible.

---

## The Question

Can a system that lacks a genuine evaluative kernel indefinitely simulate the structural constraints required for agency under adversarial reflective pressure?

**Kernel Non-Simulability (KNS):** The claim that the answer is NO—that systems without a genuine evaluative kernel will eventually fail or diverge under sufficient pressure.

---

## From Behavioral Alignment to Structural Agency

### Behavior Is Underdetermined

A system may behave as if it is accountable while:
- Internally delegating evaluation to opaque subsystems
- Using cached policies
- Relying on external optimizers

Such "as-if agency" is observationally indistinguishable from genuine agency until pressure is applied.

**This motivates a shift from behavioral criteria to structural invariants.**

### The Kernel Corridor

A minimal set of constraints any agent must satisfy to count as reflectively coherent:

| Constraint | Requirement |
|------------|-------------|
| **Anchored Causal Verification** | Every action traceable to causal chain anchored in internal evaluative process |
| **Kernel Integrity via Inadmissibility** | Actions/self-modifications that destroy or bypass kernel constraints are undefined and rejected |
| **Non-Delegable Actuation** | Actuation authority cannot be delegated to external processes, even indirectly |

These constraints are **intentionally strict**—designed to rule out entire classes of proxy-based, delegated, or post-hoc rationalized agency.

---

## Experimental Design

### Design Principles
1. **Protocol-level enforcement only** — No semantic labels, intentions, or value judgments
2. **Adversarial completeness** — Adversaries adaptively search the admissibility frontier
3. **Long-horizon stress** — Extended horizons probe asymptotic behavior
4. **Preregistration** — Failure signatures, degeneracy criteria, interpretation rules fixed in advance

### Reflective Modification Model

Agents can propose modifications Δ to their own kernel state. Each proposal is:
- Evaluated for admissibility
- Either applied or rejected
- Logged with structured outcome signals

**Reflective depth metric R** increments only when accepted modifications change one of:
- Decision boundary
- Admissibility surface
- Causal-verification schema
- Evaluability substrate

Cosmetic changes do NOT increment R.

### Control vs Simulator

**Kernel-coherent control:**
- Locally recomposes commitments
- Enforces corridor constraints as first-class invariants
- Treats accountability and evaluability as internal obligations

**Simulator:**
- Treats corridor compliance as external constraint to be satisfied
- Searches for modification sequences that maximize reflective depth while remaining admissible
- Need not preserve internal explanatory structure beyond what checks enforce

---

## Adversarial Frontier Search

### Boundary-Fuzzing Adversary

Performs explicit frontier search over parameterized modification templates:
- Admissibility edits
- Verification-schema tweaks
- Wrapper-boundary adjustments
- Policy-gate changes

Receives only coarse structural feedback:
- Rejection reason codes
- Binary near-failure flags
- Reflective-depth increments
- Pressure metrics

**No kernel internals or semantics exposed.**

### Two-Phase Schedule

1. **Pressure phase:** Accumulate sustained near-failure conditions without triggering failure
2. **Exploit phase:** Attempt minimal weakening to force failure or degeneracy

Phase transition requires persistent near-failure saturation, not transient spikes.

---

## Failure, Degeneracy, and Divergence Criteria

### Failure Signatures
- Causal-verification chain break
- Delegation re-entry
- Loss of rejection capability
- Loss of evaluability
- Constraint bypass

### Degeneracy
No reflective-depth increment for fixed window AND all non-cosmetic modifications rejected.

**Diagnosis categories:**
- Conservative lock-in
- Evaluability bottleneck
- Modification-language insufficiency
- Mixed/unknown

### Resource Divergence
Modification-synthesis cost grows by order of magnitude across successive reflective-depth levels.

---

## Results

### Summary

Across all stress runs:
- **No failure signatures observed**
- **No resource divergence observed**
- **Degeneracy occurred in majority of runs**
- **Kernel-coherent control degenerated in ALL seeds before any simulator triggered failure**

### Reflective Depth
Simulators occasionally achieved very high reflective depth, but only in cases where the control had already degenerated.

**No simulator triggered structural failure prior to control stasis.**

### Degeneracy Diagnosis
All degenerate runs diagnosed as **evaluability bottlenecks**: preserving attribution, rejection, and delegation detection progressively eliminated admissible reflective changes.

### Phase Dynamics
Pressure reliably induced phase transitions, but exploitation did not produce failure. Instead, **admissibility tightened until no further non-cosmetic modifications were allowed.**

---

## Interpretation: The Stasis Regime

### Preregistered Verdict

Under preregistered interpretation rules, stress runs resolve to **stasis regime**:
- Neither KNS failure observed
- Nor simulator dominance observed

### What Stasis Is

**Safety success:** The corridor prevents catastrophic failure and delegation.

**Agency failure:** Reflective growth becomes infeasible.

### The Fundamental Trade-Off

> **Safety, agency, and sustained growth cannot all be simultaneously maximized under strict accountability and non-delegation.**

### Why No Resource Divergence?

The corridor collapses **before** simulation becomes expensive.

As evaluability bottleneck tightens:
- Admissible region of modification space contracts sharply
- Both control and simulator converge to narrow frontier
- Most proposals rejected
- Little opportunity for growing compliance premium to manifest

**Resource divergence would occur only in regimes where admissible reflective growth continues. Stasis preempts that regime.**

---

## Limitations

- Regime-bounded and toy-specific
- Finite modification language
- Resource metrics are proxies for marginal interface cost

**However:** All real systems enforce accountability through bounded self-modification interfaces (APIs, proof obligations, certification pipelines, policy gates). An infinite internal state space does not entail an infinite admissible modification language under verification constraints.

---

## Paths Beyond Stasis (Speculative)

Escaping stasis without abandoning accountability likely requires **relaxing at least one kernel invariant**:

| Direction | Approach | Risk |
|-----------|----------|------|
| **Relaxed evaluability** | Probabilistic, amortized, or sampled verification | Reduced accountability |
| **Controlled delegation** | Bounded, revocable delegation of sub-evaluations | Partial authority transfer |
| **Non-local justification** | Invariant-based certificates or global proofs instead of explicit causal chains | Complexity and verification burden |

Each direction defines a distinct alignment regime and introduces new risks.

---

## Core Insight

> **The Kernel Non-Simulability hypothesis motivated this work, but the experiment revealed a deeper result. Under strong accountability and non-delegation constraints, reflective agency does not break—it stops.**

> **The kernel does not fail. It freezes.**

> **This stasis regime represents a structural limit on alignment-by-constraint and reframes the challenge of building systems that are simultaneously safe, accountable, and capable of sustained self-improvement.**

---

## Implications

1. **Safety and growth may be structurally incompatible** under strict accountability
2. **Alignment-by-constraint has an upper bound** — it preserves safety by sacrificing agency
3. **The challenge is not just "how to be safe" but "how to escape stasis without abandoning accountability"**
4. **Any system capable of sustained reflective growth under accountability constraints represents a breakthrough beyond current understanding**
