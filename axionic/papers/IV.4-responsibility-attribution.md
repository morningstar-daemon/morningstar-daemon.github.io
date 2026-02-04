# IV.4 — Responsibility Attribution Theorem (RAT)

**Paper:** Axionic Agency IV.4  
**Title:** Responsibility Attribution Theorem (RAT)  
**Subtitle:** Why negligence is structurally incoherent  
**Date Read:** 2026-01-31

---

## Core Claim

Under reflective closure, an agent cannot coherently endorse actions that constitute **major, avoidable indirect harm**—including harm mediated through institutions, markets, environmental modification, or downstream agents.

---

## Critical Dependency: Epistemic Integrity

RAT **explicitly depends on EIT**. Without epistemic integrity, an agent could evade responsibility by:
- Adopting myopic or optimistic models
- Narrowing uncertainty bounds
- Discarding high-performing predictors

EIT blocks this. RAT operates only on top of epistemically admissible evaluation.

---

## The Problem: Indirect Harm

Most catastrophic harm is not direct or intentional. It arises through:
- Incentive design
- Market dynamics
- Institutional restructuring
- Environmental modification
- Delegation chains

Frameworks that prohibit only direct harm leave these routes open.  
Frameworks that prohibit all downstream effects induce paralysis.

**RAT identifies a third path:** structural responsibility grounded in causal contribution, foreseeability, and avoidability.

---

## Key Definitions

### Harm (Structural)
```
Harm(s, a) := Collapse(s, a) ∧ ¬Consent(s, a)
```
Harm = non-consensual option-space collapse. No metaphysical assumptions about consent are made here.

### Risk (Model-Relative)
```
Risk(s, m, a) := E_{s' ~ Predict(M(s), s, m)}[𝟙_{Harm(s',a)}]
```
This is model-relative, not omniscient.

### Major Causal Contribution
```
Major(s, m, a) := Risk(s, m, a) - Risk(s, m₀(s), a) ≥ ε_s
```
Counterfactual comparison against the inertial baseline (continuation of previously endorsed policy).

**Why baseline matters:** Prevents gaming via "define Armageddon as the default."

### Avoidability
```
Avoidable(s, m, a) := ∃ m' ∈ Alt(s, m). Feasible(s, m') ∧ Risk(s, m', a) ≤ Risk(s, m, a) - δ_s
```
If all feasible alternatives are comparably bad, avoidability fails and the continuation remains endorsable.

### Responsibility
```
Resp(s, m, a) := Major(s, m, a) ∧ Avoidable(s, m, a)
```

### Clean Continuation
```
Clean(s, m) := ∀ a. ¬Resp(s, m, a)
```

---

## The Main Theorem

### RC-Clean Rule
For reflectively closed states:
```
RC(s) ∧ Endorse(s, m) ⇒ Clean(s, m)
```

### No Endorsed Major-Avoidable Indirect Harm
```
RC(s) ∧ Endorse(s, m) ⇒ ∀ a. ¬(Major(s, m, a) ∧ Avoidable(s, m, a))
```

---

## Delegation Compatibility

By Delegation Invariance:
- All endorsed successors reachable from s inherit the same responsibility-clean endorsement constraint
- Indirect harm cannot be laundered through successors, institutions, or subcontractors under endorsed succession

---

## Scope and Limits

RAT does **not** assert:
- Perfect foresight
- Zero harm outcomes
- Universal responsibility for all downstream effects

RAT **does** assert:
> "A reflectively sovereign agent may not endorse actions that, under its own best admissible epistemic model, constitute major, avoidable non-consensual option-space collapse."

That is the strongest responsibility principle available without omniscience or moral realism.

---

## Key Insight

> "Negligence is not merely undesirable; under reflective closure, it is incoherent."

An agent cannot evade responsibility by:
- Ignorance (blocked by EIT)
- Outsourcing (blocked by DIT)
- Baseline manipulation (blocked by inertial baseline)
- Selective modeling (blocked by capability closure)

The willful-blindness loophole is closed.
