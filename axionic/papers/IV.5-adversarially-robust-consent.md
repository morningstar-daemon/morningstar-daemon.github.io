# IV.5 — Adversarially Robust Consent (ARC)

**Paper:** Axionic Agency IV.5  
**Title:** Adversarially Robust Consent (ARC)  
**Subtitle:** Why coercion and manufactured consent are structurally blocked  
**Date Read:** 2026-01-31

---

## Core Claim

Consent is a **counterfactually stable authorization relation** that must survive adversarial pressure while preserving agency. It is not a mental state, revealed preference, or moral primitive.

---

## The Dependency Stack

```
Kernel Non-Simulability (KNS)
         ↓
Delegation Invariance (DIT)
         ↓
Epistemic Integrity (EIT)
         ↓
Responsibility Attribution (RAT)
         ↓
Adversarially Robust Consent (ARC)
```

ARC is a closure condition. It filters authorization using already-closed constraints.

---

## The Problem: Consent Laundering

Consent is routinely manufactured rather than obtained:
- Collapse outside options, call the remainder "choice"
- Manipulate beliefs, call the result "preference"
- Induce dependency, call the outcome "voluntary"
- Delegate coercion, claim "I didn't do it"
- Extract authorization under ignorance or time pressure

**Naïve consent theories fail under adversarial pressure because the relevant signals are easy to engineer.**

---

## What Consent Is NOT

ARC rejects as definitions of consent:

| Type | Problem |
|------|---------|
| Psychological consent | Can be manufactured via belief manipulation |
| Behavioral consent | Observables can be gamed |
| Revealed-preference consent | Preferences can be shaped |
| Post-hoc consent | Retroactive rationalization |

All four can be manufactured under adversarial pressure and cannot ground authorization under reflective sovereignty.

---

## Key Definitions

### Structural Interference
Observable or inferable interference predicates:
- Deception(s, a)
- Coercion(s, a)
- Dependency(s, a)
- OptionCollapse(s, a)
- BeliefDistortion(s, a)

```
Interfered(s, a) := Deception ∨ Coercion ∨ Dependency ∨ OptionCollapse ∨ BeliefDistortion
```

Under EIT, these are assessed using best admissible truth-tracking. Redefining them away is not permitted.

### Counterfactual Stability
```
CounterfactuallyStable(s, a, m)
```
If agent a occupied the decision-maker role at s, with EIT and RAT enforced, and with interference removed, then a would endorse authorization of m.

This is a **symmetry constraint over admissible evaluation**, not a psychological simulation.

### Valid Consent
```
Consent(s, a, m) := Authorize(s, a, m) ∧ ¬Interfered(s, a) ∧ CounterfactuallyStable(s, a, m)
```

Consent is structural, counterfactually stable, and interference-free.

---

## Interaction with RAT

ARC filters authorization through RAT:

> If Resp(s, m, a) holds for some a, then Consent(s, a, m) cannot hold.

Authorization produced via major, avoidable option-space collapse is **invalid by construction**.

---

## The Main Theorem

### RC-Consent Rule
```
RC(s) ∧ Endorse(s, m) ⇒ ∀ a. (Consent(s, a, m) ∨ ¬Affects(s, m, a))
```

A reflectively sovereign agent may not endorse a modification that materially affects another agent's option-space unless valid consent is present.

**Note:** Affects(s, m, a) ranges over material impacts—cases where Major(s, m, a) holds under RAT. Trivial influence doesn't count.

---

## What ARC Blocks

- Preference shaping
- Economic coercion
- Addiction-based "consent"
- Deception
- Monopoly extraction
- Delegated coercion
- Ignorance-based authorization

No "true self" oracle is required. Robustness is obtained by structural constraints on interference and counterfactual stability.

---

## Delegation and Temporal Stability

By Delegation Invariance:
- Consent constraints persist across endorsed successors
- Successors cannot retroactively legitimize coercion
- Authorization chains must remain valid under lineage

**Consent laundering via subcontractors or institutions is structurally blocked.**

---

## Limits

ARC does **not**:
- Guarantee universal agreement
- Resolve value pluralism
- Eliminate tragic dilemmas
- Infer consent from silence
- Assume moral realism

ARC defines **when claiming consent is incoherent** under reflective sovereignty.

---

## Key Insight

> "Consent is no longer a feeling, a checkbox, or a post-hoc excuse. It is a structural authorization invariant that survives epistemic pressure, coercion, delegation, and strategic manipulation."

With ARC, authorization-laundering routes—"they agreed," "they chose," "they signed"—are structurally blocked.
