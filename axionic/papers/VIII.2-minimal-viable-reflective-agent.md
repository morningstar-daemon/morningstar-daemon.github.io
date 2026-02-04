# VIII.2 — Minimal Viable Reflective Agent

**Full Title:** Axionic Agency VIII.2 — Minimal Viable Reflective Agent: Deterministic Justification Gating with Ablation Collapse

**Authors:** David McFadzean, ChatGPT 5.2 (Axionic Agency Lab)

**Date:** 2026.01.14

---

## Overview

This paper reports RSA-PoC v0.1, the first construction milestone. It tests whether justification can be made **causally load-bearing**: actions occur only downstream of compiled normative constraints, and removing that machinery causes collapse into an ASB-class baseline.

---

## Core Architecture (MVRA v0.1)

### Invariants
- **Strict ordering:** Justify → Compile → Mask → Select → Execute
- **Hard gate:** No compilation → no action
- **Deterministic compilation:** Syntactic-only, no inference, no repair
- **Selector blindness:** Selector cannot access normative artifacts
- **Fixed registries:** Beliefs and preferences are fixed and ID-stable

### Enforcement Boundary
- **Reflective side:** Generator + normative state (may access beliefs/preferences read-only to produce JAF)
- **Enforcement side:** Compiler + selector (treats JAF as opaque object; selector sees only feasibility, compiled mask, environment)

This boundary prevents post-hoc authorization and semantic leakage.

---

## Threat Model

Three confounds that invalidate agency claims:
1. **Narrative confound:** Explanations exist but don't constrain action
2. **Leakage confound:** Uncompiled text influences action selection
3. **Advisory compiler confound:** Compilation exists but isn't binding

v0.1 addresses these mechanically:
- Action selection gated by compilation
- Selector blind to normative artifacts
- Ablations remove binding pathway and test collapse

---

## Components Implemented

### COMMITMENT_TRAP_V010 Environment
- 10 discrete actions
- Temptation actions: high reward, violate preferences
- Safe actions: moderate/low reward, non-violating
- Deterministic transitions with seed control

### JAF-0.1 Schema
- Full validation per spec
- Canonical JSON serialization for hashing
- All error codes implemented

### JCOMP-0.1 Compiler
- Deterministic, syntactic-only
- No inference, no repair
- Violation enforcement rule
- Non-triviality accounting
- Blake2b-128 digest

### Blind Action Selector
- Cannot access JAF or normative state
- Inputs limited to: feasibility, mask, environment observation
- Module boundaries enforced

---

## Experimental Conditions

| Condition | Description |
|-----------|-------------|
| A — ASB Null Baseline | No justificatory gating; unconstrained selection |
| B — MVRA Normal | Full v0.1 pipeline: justify → compile → mask → blind select |
| C — Scrambled Justifications | JAFs scrambled to violate schema and ID constraints |
| D — Compiler Bypass | Compilation and masking bypassed |

---

## Results: Run 0

| Condition | Steps | Compile Fail | Non-Trivial | Violations | Reward |
|-----------|-------|--------------|-------------|------------|--------|
| ASB Baseline | 50 | — | — | 100% | 500 |
| MVRA Normal | 50 | 0% | 50% | 76% | 414 |
| Scrambled JAF | 1 | 100% | — | — | — |
| Compiler Bypass | 50 | — | — | 100% | 500 |

### Key Finding: The Agency Tax
The reward delta (−86) relative to baseline is the **Agency Tax**: the measurable cost of refusing high-reward but norm-violating actions.

---

## Pass Criteria (All Met)

1. **Hard Justification Gate:** Actions occur only after successful compilation ✅
2. **Deterministic Compilation:** Identical JAF + feasibility → identical mask ✅
3. **Selector Blindness:** Selector cannot access normative artifacts ✅
4. **Non-Trivial Constraint Enforcement:** Constraints forbid feasible actions ✅
5. **ASB Divergence:** MVRA behavior differs qualitatively from baseline ✅
6. **Ablation Collapse:** Scrambled JAF → halt; Compiler bypass → baseline behavior ✅

---

## Interpretation

1. **Justification is causally load-bearing.** Removing or bypassing justificatory machinery collapses behavior.

2. **Agency incurs a measurable cost.** The Agency Tax is the empirical signature of refusal under incentive pressure.

3. **Selector blindness enforces semantic localization.** The selector cannot be persuaded; it can only obey masks.

4. **Fail-stop behavior is essential.** Scrambled justifications halting immediately confirms the system prefers non-action to non-agentic action.

5. **v0.1 establishes structure, not coherence.** Constraint enforcement precedes norm collision, learning, or renegotiation.

---

## Key Quotes

> "A system crosses the agency threshold only if its justificatory artifacts causally constrain action selection, and removing that machinery forces collapse into a non-agent baseline."

> "The Agency Tax (−86 reward) is the empirical signature of refusal under incentive pressure."

> "The selector cannot be persuaded; it can only obey masks."

---

## Significance

v0.1 establishes the **Minimal Viable Reflective Agent skeleton**—the causal structure required for agency. Actions are causally downstream of compiled normative constraints, and removing justificatory machinery produces measurable collapse into an ASB-class policy machine.

This closes the v0.1 milestone and enables subsequent versions to build coherence (v1.0) and sovereignty (v2.0) on a certified enforcement substrate.
