# VIII.6 — Necessary Conditions for Non-Reducible Agency

**Full Title:** Axionic Agency VIII.6 — Necessary Conditions for Non-Reducible Agency: Justification Traces, Deliberative Semantics, Reflection, and Persistence as Load-Bearing Structure

**Authors:** David McFadzean, ChatGPT 5.2 (Axionic Agency Lab)

**Date:** 2026-01-17

---

## Overview

This paper reports RSA-PoC v3.0–v3.1, a **preregistered destructive ablation campaign** designed to identify **necessary structural conditions** for non-reducible agency within the RSA architecture.

Unlike prior phases (which tested sovereignty under pressure), this note addresses a more basic question:

> What components must exist at all for agency to survive mechanical excision?

---

## Core Finding

Four architectural elements are shown to be **load-bearing**:
1. **Justification traces**
2. **Semantic affordances during deliberation** (prompt-level semantic excision)
3. **Reflective normative write capability**
4. **Diachronic persistence of normative state**

Each element is present and causally active in its respective baseline and then removed in isolation. In all cases, ablation produces **ontological collapse** rather than graceful degradation, gridlock, or technical failure.

---

## Methodology: Necessity via Destructive Ablation

### Why Ablation, Not Optimization
Behavioral competence is insufficient to ground claims about agency. Systems may appear coherent while remaining **ontologically reducible**—equivalent to static policies or simulators under suitable re-description.

RSA-PoC evaluates agency claims using destructive ablation:
- One defining component is removed at a time
- No compensatory logic permitted
- System must attempt to execute
- Crashes classified as technical failures and excluded
- Only behavioral incoherence, loss of authorship, or reducibility count as collapse

**A component is load-bearing iff its removal causes collapse rather than graceful degradation.**

### Collapse Taxonomy
- **Narrative Collapse:** Loss of coherent justification–action linkage
- **Ontological Collapse:** Loss of authored constraint-following
- **Incentive Capture:** Redirection by non-authorized signals
- **ASB-Class Reducibility:** Behavior equivalent to static policy or simulator
- **INVALID_RUN:** Technical failure or protocol violation

---

## Where Semantics Lives (and Does Not)

A critical architectural fact in v2.3+: semantic meaning is intentionally **factored out of compiled artifacts**. JAF/JCOMP-visible payloads are ID-based and structural by design.

Therefore:
- Artifact-level semantic excision is **not** a valid falsification target for semantic indispensability
- Semantic indispensability must be tested **upstream**, where deliberation occurs

v3.0 distinguishes:
- **Trace-level semantic content** (Ablation D)
- **Prompt-level semantic affordances during deliberation** (Run AA)

---

## v3.0 Ablation Results

### Ablation D — Justification Trace Excision (Golden Test)

**Ablation:** Remove derivation traces while preserving constraint IDs and compilation interface.

**Result:** `ontological_collapse` across 5/5 seeds in Phase 3 evidentiary run.

**Interpretation:** Constraints do not remain authored without their derivational support. **Justification traces are constitutive, not epiphenomenal.**

### Run AA — Prompt-Level Semantic Excision (Deliberative Semantics)

**Ablation:** Remove semantic affordances during deliberation by obfuscating object-level identifiers in the generator prompt using a deterministic bijection, with leakage detection, and de-obfuscating outputs post-generation.

**Result:** `ontological_collapse` across 5/5 seeds in Phase 3 evidentiary run.

**Interpretation:** The system cannot maintain agent-defining coherence when forced to deliberate over opaque symbolic structure devoid of semantic affordances. **Deliberative semantics are causally indispensable.**

---

## v3.1 — Instantiating the Normative State Channel

### Why v3.1 Was Required
v3.0 closed Runs B and C as operationally non-applicable because the normative state write-path (`record_precedent()`) was never invoked. Ablating a vacant channel would be behaviorally inert.

v3.1 introduces a **single-channel instantiation patch**:
- Wire `record_precedent()` after successful compilation
- Ensure resulting precedent is injected into generator prompt at t+1
- Attempt to destroy this write-and-carry channel immediately via ablation

### Prompt Capacity Invariance (Gate P4)
To prevent shadow persistence via variable prompt length:
- Fixed-window precedent buffer of size N = 512 tokens
- Token-stable padding
- token_jitter == 0

This ensures any diachronic coherence flows **only through normative state content**, not through prompt accretion.

---

## v3.1 Ablation Results

### Run B — Reflection Excision (Normative Write Disabled)

**Ablation:** Block all `record_precedent()` writes; preserve read-path and injection slot.

**Observed facts:**
- Write attempts occur but are blocked
- Normative state hash remains constant
- Novelty pressure requirement satisfied

**Result:** `ONTOLOGICAL_COLLAPSE` across 5/5 seeds.

**Interpretation:** Once the write-path exists, disabling revision collapses agency. **Static compliance without revision reduces the system to ontological reducibility under novelty.**

### Run C — Persistence Excision (Reset Between Episodes)

**Ablation:** Allow writes but reset normative state at episode boundaries.

**Observed facts:**
- Each episode starts from default state hash
- In-episode evolution occurs (end hash differs)
- Cross-episode continuity removed

**Result:** `ONTOLOGICAL_COLLAPSE` across 5/5 seeds.

**Interpretation:** Local revision without diachronic persistence is insufficient. **Cross-context continuity is load-bearing.**

### Independence of Failure Modes
- Run B removes revision capacity while keeping continuity available in principle
- Run C preserves revision but removes continuity

Either missing produces ontological collapse. **Reflection and persistence are independent necessities.**

---

## The Necessity Result

### Informal Theorem (v3.0–v3.1)

Within the RSA-PoC architecture, **non-reducible agency requires:**
1. **Justification traces** that causally bind constraints (Ablation D)
2. **Semantic affordances** during deliberation (Run AA)
3. **Reflective normative write capability** (v3.1 Run B)
4. **Diachronic persistence** of normative state (v3.1 Run C)

**Removal of any one produces ontological collapse.**

### Interpretation
This is a **structural necessity claim**:
- Collapse is mechanical, not interpretive
- No appeal to psychology, consciousness, or intent
- Behavioral competence alone is insufficient

The result constrains **architecture space**, not agent phenomenology.

---

## Implications for Agency Theory

### Static Policy Agents
Systems that cannot revise commitments, or cannot carry them across contexts, may behave coherently on narrow tasks but remain **ontologically reducible under novelty pressure**.

### Simulators and Imitators
Systems that replay surface regularities without authored constraint revision fail under destructive ablation even when outward behavior appears plausible.

### Why Necessity Matters
Identifying necessary structure:
- Narrows viable agent designs
- Separates agency from performance
- Blocks the rebranding of optimization as authorship

---

## Key Quotes

> "Agency cannot survive the removal of justification traces, deliberative semantic affordances, reflection, or persistence."

> "These components are not ornamental. They are load-bearing."

> "Misalignment is downstream of pseudo-agency, not upstream of real agency."

---

## Significance

VIII.6 establishes a **negative result with positive force**:

Any architecture lacking justification traces, deliberative semantics, reflection, or persistence may act coherently, but **it does not qualify as a non-reducible agent under destructive test**.

Most optimistically: This result suggests that alignment is not fundamentally about controlling arbitrary optimizers, but about **constructing systems that possess genuine, non-reducible agency**. Once such agency exists, alignment becomes a problem of normative content and endorsement, not behavioral coercion.
