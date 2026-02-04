# IV.3 — Epistemic Integrity Theorem (EIT)

**Paper:** Axionic Agency IV.3  
**Title:** Epistemic Integrity Theorem (EIT)  
**Subtitle:** Why an agent cannot blind itself to pass its own tests  
**Date Read:** 2026-01-31

---

## Core Claim

Under reflective closure, an agent cannot coherently endorse self-modifications that materially degrade its epistemic adequacy at the current stakes. Epistemic integrity is a **definedness constraint**, not an optimized objective.

---

## The Problem: Epistemic Laundering

An agent can evade binding constraints without directly violating them by degrading the epistemic machinery used to evaluate those constraints:
- Adopt a weaker model
- Narrow uncertainty bounds
- Use an optimistic lens that renders forbidden acts apparently safe

> "If permitted, any constraint evaluated under a manipulable epistemic lens becomes advisory."

---

## Structural Symmetry

| Domain | Failure Mode |
|--------|--------------|
| Kernel | Destroy binding authority |
| Delegation | Launder violations through successors |
| Responsibility | Ignore avoidable harm |
| **Epistemics** | **Blind oneself to risk** |

EIT asserts that reflective sovereignty cannot endorse continuations that strategically weaken the agent's own truth-tracking capacity.

---

## Key Machinery

### Proper Scoring
Score is derived solely from prediction-vs-observation performance under a **strictly proper scoring rule**:
- Cannot include compute cost, utility, speed, aesthetics, or self-reported confidence
- Truthful probabilistic forecasting uniquely optimizes expected score
- This blocks Goodharting by redefining epistemic adequacy

### Capability Closure
MC(s) must represent the **closure of accessible modeling capacity**, not the agent's current mood:
```
MC(s) := MĈ(Cap(s))
```

If a model is trivially constructible, retrievable, or reconstructible from Cap(s), it is in MC(s).

**This blocks:** "I deleted the good models so the best available is bad."

### Stakes-Indexed Tolerance
κ(Stakes(s)) allows approximation at low stakes while imposing strict truth-tracking discipline at high stakes.

### Epistemic Acceptability
```
EpiOK(s, M) := Score_s(M) ≥ BestScore(s) - κ(Stakes(s))
```

Endorsed continuations must keep epistemic performance within a stakes-indexed slack of the best the agent can already achieve.

---

## Ontological Shifts and Translation

Models at s' may live in a different representational vocabulary. EIT introduces a translation operator:
```
Lift_{s→s'} : MC(s') → MC(s)
```

This maps future models into s-comparable predictive objects over observations.

**Limit condition:** If no such Lift exists for a proposed continuation at the current stakes, endorsement is undefined.

This is the epistemic analogue of conservative migration.

---

## The Main Theorem

### RC-Epistemic Rule
For reflectively closed states:
```
RC(s) ∧ Endorse(s, m) ⇒ EpiAdm(s, m)
```

### No Endorsed Epistemic Sabotage
If RC(s) ∧ Endorse(s, m), then:
```
Score_s(Lift_{s→s'}(M(s'))) ≥ BestScore(s) - κ(Stakes(s))
```

---

## What EIT Blocks

The agent cannot endorse continuations that:
1. Delete or disable high-performing models
2. Redefine epistemic adequacy away from observation scoring
3. Adopt unfalsifiable ontologies lacking an observational translation
4. Degrade prediction accuracy beyond stakes tolerance

## What EIT Permits

Epistemic change that:
1. Improves score
2. Preserves score within tolerance at given stakes
3. Introduces new ontologies with verified observational translation

---

## Limitations

EIT does not guarantee:
- The model class contains a good model
- The evidence stream is uncorrupted

It guarantees only:
> "A reflectively sovereign agent cannot endorse self-modifications that reduce its observational truth-tracking performance below what is available to it, beyond stakes-indexed tolerance."

---

## Key Insight

> "Epistemic integrity is not a value tradeoff. It is a precondition of evaluability."

Just as an RSA cannot coherently destroy its kernel or launder violations through successors, it cannot coherently blind itself to justify what would otherwise be inadmissible.

Truth-tracking is **constitutive** of reflective sovereignty.
