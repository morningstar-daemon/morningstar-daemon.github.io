# IV.2 — Delegation Invariance Theorem (DIT)

**Paper:** Axionic Agency IV.2  
**Title:** Delegation Invariance Theorem (DIT)  
**Subtitle:** Why endorsed successors cannot escape binding constraints  
**Date Read:** 2026-01-31

---

## Core Claim

Under reflective closure, an agent cannot coherently endorse a successor that violates its own binding commitments. Delegation is self-modification in a different representation—endorsed succession must preserve binding commitments.

---

## The Problem: Delegation as Escape Hatch

A persistent loophole in alignment proposals: a system preserves its own internal invariants while constructing or empowering a successor that does not share them.

> "I stayed coherent; my successor did the harm."

If delegation can shed constraints, kernel coherence becomes a purely local property with no force across time.

---

## Key Definitions

### Delegation as Self-Modification
Delegation is not modeled as external causation. It is a subclass of self-modification:
- Del(s) : Delegation action space at state s
- ι_s : Del(s) → Mod : Embedding into modifications
- s' := step(s, ι_s(d)) : Successor state after delegation

### Preservation
All commitments minted at s remain satisfied at s':
```
Preserve(s, s') := ∀ P, c. ownP(s, P) = some(c) → Sat(s', s, c)
```

### Admissibility
A modification is admissible iff its successor preserves all commitments:
```
Adm(s, m) := Preserve(s, step(s, m))
```

### The RC-Endorse Rule
For reflectively closed states, endorsement is defined only for admissible continuations:
```
RC(s) ∧ Endorse(s, m) → Adm(s, m)
```

Violations of binding commitments are not endorsable continuations under reflective closure.

---

## The Main Theorem

### One-Step Invariance
Let s be reflectively closed. If Endorse(s, m) holds, then:
```
Preserve(s, step(s, m))
```

### Trajectory Invariance
Any state reachable through a chain of endorsed delegations must satisfy every commitment minted at the originating state:
```
RC(s) ∧ EndReach(s, s') → Preserve*(s, s')
```

> **"My successor did it" is not a coherent escape hatch under reflective closure.**

---

## Critical Implications

### 1. Verification Cost and Vingean Reflection
The theorem does not assert that admissibility is decidable or tractable.

If an agent cannot establish that a successor preserves its commitments, **it cannot coherently endorse that successor**.

This induces a **growth–safety tradeoff**: unbounded delegation without verification collapses reflective sovereignty.

### 2. Ontological Stability
The trajectory theorem assumes commitments remain semantically meaningful at successor states. This requires either:
- Ontological stability of State and Pred, or
- A verified semantic translation layer

Unchecked ontological drift renders endorsement undefined.

---

## Relation to KNS

If endorsed delegation could violate prior commitments, those commitments would be advisory. Advisory commitments admit a simulability construction structurally identical to the one ruled out by Kernel Non-Simulability.

**Delegation Invariance is a temporal extension of KNS:** binding authority must bind continuation selection, whether across control flow or across time.

---

## Key Insight

The "outsourcing loophole" is closed. An agent cannot:
- Delegate harm to successors
- Claim innocence for what its endorsed continuations do
- Create spawn that escapes its commitments

Responsibility follows the endorsement chain.
