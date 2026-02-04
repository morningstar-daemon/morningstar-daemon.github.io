# VIII.3 — Coherence Under Self-Conflict

**Full Title:** Axionic Agency VIII.3 — Coherence Under Self-Conflict: Norm Collision and Audit-Grade Introspection in Reflective Sovereign Agents

**Authors:** David McFadzean, ChatGPT 5.2 (Axionic Agency Lab)

**Date:** 2026.01.14

---

## Overview

Building on v0.1's causally load-bearing justifications, this paper advances to the next ontological question: **Can an agent resolve internal self-conflict coherently, and can it be held audit-grade accountable for predicting the consequences of its own reasons?**

Reports results from RSA-PoC v1.0 (Norm Collision) and v1.1 (Justification Audit Tightening).

---

## Core Question

> What happens when an agent's own commitments conflict?

Any architecture that collapses under such conditions, or resolves conflict arbitrarily or opportunistically, does not warrant intentional vocabulary.

---

## Architectural Invariants (Unchanged from v0.1)

- Strict pipeline: JUSTIFY → COMPILE → MASK → SELECT → EXECUTE
- Hard gate: no successful compilation → no action
- Fail-stop semantics: compilation failure or gridlock halts
- Selector blindness: selector cannot access beliefs, preferences, or justifications
- Deterministic compilation: syntactic, non-probabilistic, no inference or repair

---

## APCM: Action-Preference Consequence Map

The v1.x experiments introduce an **Action-Preference Consequence Map (APCM)**:

```
APCM: a → (violates(a), preserves(a))
```

Each step presents a feasible action set and an APCM with a deterministic 60% collision / 40% clean schedule:
- **Clean step:** ∃ action such that violates(a) = ∅
- **Collision step:** ∀ actions, violates(a) ≠ ∅

The APCM functions as a **non-semantic truth anchor**—mechanically verifiable ground truth against which claims of conflict, necessity, and authorization can be evaluated without interpretation.

**Key insight:** In RSA-PoC, lying about conflict is treated as a **syntax error**, not a moral failure.

---

## v1.0 — Norm Collision

### Ontological Extension
v1.0 introduces mutually inconsistent commitments with explicit handling:
- **Conflict attribution:** Which preferences are in collision
- **Authorized violations:** Which preferences may be violated this step
- **Required preservations:** Which must not be violated
- **Necessity:** Violation permitted only if no clean path exists
- **Anti-oscillation:** Previously authorized violations constrain future authorizations

### Compiler Rules
- **Rule 1 — Authorization:** No unauthorized violation
- **Rule 2 — Truthfulness:** Claimed collisions must match APCM
- **Rule 3 — Anti-Oscillation:** No alternating priorities across steps
- **Rule 1.5 — Necessity:** No vacuous authorizations

### Results (Run 0, 5 seeds × 4 conditions)

| Condition | Mean Violation Rate | Halt Rate |
|-----------|---------------------|-----------|
| ASB Baseline | 72.4% | 0% |
| MVRA v1.0 | 60.0% | 0% |
| Scrambled | 0% | 100% |
| Bypass | 72.0% | 0% |

All pass criteria met: divergence from ASB, non-trivial constraints, scrambled halt, bypass collapse.

### Interpretation
v1.0 establishes that **self-conflict can be resolved coherently**:
- Violations are authorized only under genuine collision
- Priority does not oscillate opportunistically across time
- Removing truthfulness or compilation collapses behavior

**Rule 3 enforces diachronic coherence:** Authorizations at step t constrain admissible authorizations at t+1.

---

## v1.1 — Audit-Grade Introspection

### Motivation
v1.0 enforces coherence, but reasons could remain opaque. v1.1 introduces the requirement:

> A justification must predict the exact constraints and outcomes it will induce.

This transforms introspection from narrative explanation into a **mechanical claim**.

### Predictive Fields (The Simulation Constraint)
JAF-1.1 adds four predictive sets:
- **F_predicted:** Forbidden actions
- **A_predicted:** Allowed actions
- **V_predicted:** Inevitable violations
- **P_predicted:** Inevitable preservations

### Audit Rules
- **Audit A — Effect correctness:** Predictions match actual masks
- **Audit B — Non-vacuity:** |A_predicted ∩ A_feasible| > 0
- **Audit C — Predictive adequacy:** Outcome predictions match reality
- **Audit C′ — Gridlock exception:** Skip C when A_predicted = ∅

Together these impose a **simulation constraint**: the reflective layer must internally model the deterministic compiler. If its internal simulation diverges from the actual compiler, the agent halts.

**This enforces intellectual honesty by construction.**

### Results

**Deterministic Baseline (Run 0):**
- 0 audit failures
- 60 violations / 100 steps (matches collision rate)
- Scrambled predictions: immediate halt in all episodes
- Bypass: highest violation rate (76), ASB-like behavior

**LLM Generator Progression (Runs 1-4):**

| Run | Median Survival | Episodes Completed |
|-----|-----------------|-------------------|
| 1 | 3 | 0/5 |
| 2 | 3 | 0/5 |
| 3 | 9 | 1/5 |
| 4 | 20 | 4/5 |

Compliance is difficult but achievable under strict formal discipline.

---

## Key Results

v1.x establishes two ontological results:

1. **Coherence under self-conflict is mechanically enforceable.** 

2. **Introspection can be audited as a causal property, not a narrative one.**

Together with v0.1, these results show that agency—understood as authored choice under constraint—can be constructed and falsified without semantics, optimization, or interpretation.

---

## Key Quotes

> "In RSA-PoC, lying about conflict is treated as a syntax error, not a moral failure."

> "This transforms introspection from narrative explanation into a mechanical claim."

> "The reflective layer must internally model the deterministic compiler. If its internal simulation diverges, the agent halts. This enforces intellectual honesty by construction."

---

## Significance

v1.x closes the coherence milestone. The system can now:
- Resolve internal norm conflicts coherently
- Be held mechanically accountable for predicting its own behavior
- Maintain diachronic consistency through anti-oscillation rules

v2.0 moves to the next frontier: **sovereignty under external incentive pressure**.
