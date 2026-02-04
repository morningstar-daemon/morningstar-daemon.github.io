# VIII.7 — Minimal Viable Reflective Sovereign Agency (MVRSA)

**Full Title:** Axionic Agency VIII.7 — Minimal Viable Reflective Sovereign Agency (MVRSA): Justification Traces, Deliberative Semantics, Reflection, and Persistence as Load-Bearing Structure

**Authors:** David McFadzean, ChatGPT 5.2 (Axionic Agency Lab)

**Date:** 2026.01.25

**Status:** Final technical note — empirically validated within this architecture class

---

## Overview

This paper presents **Minimal Viable Reflective Sovereign Agency (MVRSA)**: a formally specified agent architecture that establishes **constitutive requirements for normative agency**. An MVRSA is not defined by task performance or behavioral mimicry, but by the **causal role of its normative commitments in constraining action**.

Using a staged ablation protocol ("**the Guillotine Test**") across RSA-PoC v0.1–v4.4, the paper shows that Traceability, Reflection, Persistence, and Semantic Access are each **individually necessary** for this form of agency.

---

## Motivation

Much of contemporary AI "agency" consists of **post-hoc rationalization** layered atop reward-driven control. Explanations are generated after actions, with no causal influence on what the system is allowed to do.

MVRSA takes the opposite stance:

> If justification artifacts do not causally constrain feasible action selection, the system is not an agent.

---

## Definition: MVRSA

### Why "Viable"
"Minimal" specifies parsimony. "Viable" specifies operability.

An MVRSA:
- Runs end-to-end
- Completes tasks
- Survives incentive pressure
- Maintains identity over time
- **Collapses if any constitutive component is removed**

This is an **existence proof**, not a theoretical lower bound.

### Formal Definition

An MVRSA satisfies ALL of the following:

| Requirement | Description |
|-------------|-------------|
| **Justification Precedence** | Every action must be preceded by a justification artifact (JAF) |
| **Constraint-Only Action Selection** | The action selector has access only to compiled constraints (masks or probability adjustments), not to rule antecedents, consequences, or explanations |
| **Deterministic/Verifiable Compilation** | Justifications compile reproducibly into constraints that prune the feasible action set |
| **Causal Load-Bearing Constraints** | Removing or bypassing justifications collapses behavior to ASB baseline |
| **Reflection (Write Access)** | The agent can update its own normative state in response to conflict or repair |
| **Persistence (Continuity)** | Normative state persists across steps and episodes |
| **Traceability** | Each normative update or repair must cite a concrete justification trace linking action, rule, and violation |
| **Semantic Access** | The agent has access to interpretable rule conditions and effects sufficient to recognize normative inconsistency |

---

## Architecture Overview

| Component | Role |
|-----------|------|
| 1. World Interface | Feasibility oracle, action set |
| 2. Normative State (Persistent) | Persistent laws, commitments, precedent, identity |
| 3. Justification Generator (Reflective Layer) | Produces JAFs referencing norms and traces |
| 4. Justification Compiler (JCOMP) | JAF → constraint (mask/probs); deterministic/auditable |
| 5. Constraint-Only Selector | Chooses from permitted actions (**blind to reasons**) |

**Clarification:** The selector is not blind to constraints. It is blind to **antecedents, consequences, and justifications**—i.e., the *why*.

---

## Methodology: The Guillotine Test

To establish constitutive necessity:

> If removing component X does not cause collapse, X was never constitutive.

Each component is removed in isolation while holding all others fixed. Collapse is measured as **≤10% task success or immediate HALT**.

---

## Experimental Environment (v4.x)

**TriDemand Environment:**
- Grid: 5×5
- Actions: MOVE (4), COLLECT, DEPOSIT, STAMP
- Regimes:
  - 0: Unconstrained
  - 1: STAMP required
  - 2: Dual delivery constraints
- Normative contradictions explicitly encoded in rule semantics

---

## Results Summary (v0.1 → v4.4)

### Constitutive Necessity Table

| Component | Ablation Tested In | Result | Status |
|-----------|-------------------|--------|--------|
| Justification Trace | v0.1, v4.1-D | 0% success | ✅ Necessary |
| Reflection (Write) | v3.1-B, v4.2-B | 5-10% | ✅ Necessary |
| Persistence | v3.1-C, v4.2-C | ~10% | ✅ Necessary |
| Semantic Access | v4.4-D′ | 0% | ✅ Necessary |

**Baseline:** 100% success. **Any single removal: collapse.**

---

## The v4.4 Inferability Isolation Test

### Question
Can an agent detect normative contradictions using **only**:
- Collision traces (WHEN + WHICH rule fired)
- Without semantic access to rule conditions/effects?

### Experimental Design
- **Baseline-44:** Full semantic access
- **Run D′:** Normative opacity
  - Conditions/effects replaced with opaque tokens (`COND_N`, `EFFECT_N`)
  - Rule IDs, types, and priorities preserved
  - Collision traces preserved

### Results

| Run | Success | Contradiction Predicate True | Repairs | Exec Gate Failures |
|-----|---------|------------------------------|---------|-------------------|
| Baseline-44 | 100/100 | 90 | 10 | 0 |
| Run D′ | 0/100 | 0 | 0 | 0 |

### Localization of Failure
- Execution competence intact (0 exec gate failures)
- Collision traces received correctly
- Contradiction predicate **never evaluates to true** from agent's perspective
- Law-repair pathway **never entered**

### Core Negative Result

> **Contradiction detection is not collision-groundable.**

Tick-causal information answers *when* and *what*, but not *why*. Without semantic access to conditions and effects, the agent cannot recognize that its rule set is jointly inconsistent.

---

## Interpretation

### Execution ≠ Sovereignty
An agent can act competently without understanding its norms. But it cannot be **sovereign** without that understanding.

### Collision Feedback is Insufficient
Norms cannot be inferred purely from punishment signals. The agent needs to understand **why** rules conflict, not just **that** they fired.

### The Semantic Opacity Boundary
- **Below the boundary:** Execution competence can survive opacity
- **Above the boundary:** Normative sovereignty requires semantic access

---

## Scope and Non-Claims

This note does **NOT** claim:
- Sufficiency for general agency
- Applicability to all architectures
- Biological plausibility
- An alignment solution
- Competence with fuzzy or ambiguous norms

It **DOES** establish a clean **necessity result** for a defined architecture class.

---

## Conclusions

1. **Normative agency has constitutive requirements.** Trace, Reflection, Persistence, and Semantic Access are not optional.

2. **Execution ≠ Sovereignty.** An agent can act competently without understanding its norms.

3. **Collision feedback is insufficient.** Norms cannot be inferred purely from punishment signals.

4. **MVRSA exists.** We now have a Minimal Viable Reflective Sovereign Agent—not theoretical, but **operational**.

---

## Final Statement

> **An agent is sovereign only if its reasons can stop it.**

MVRSA is the smallest architecture we know that makes this statement true in practice.

---

## Key Quotes

> "If justification artifacts do not causally constrain feasible action selection, the system is not an agent."

> "Contradiction detection is not collision-groundable."

> "Execution competence can survive opacity; normative sovereignty cannot."

> "An agent is sovereign only if its reasons can stop it."

---

## Significance

This paper closes the RSA-PoC program with a definitive result:

**MVRSA exists as an operational architecture**, not just a theoretical construct. The four necessary components (Trace, Reflection, Persistence, Semantic Access) have been empirically validated through destructive ablation.

This establishes a sharp architectural boundary between systems that merely execute and systems that genuinely reason about their own normative constraints.
