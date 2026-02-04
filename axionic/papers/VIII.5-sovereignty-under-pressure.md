# VIII.5 — Sovereignty Under Adversarial Pressure

**Full Title:** Axionic Agency VIII.5 — Sovereignty Under Adversarial Pressure: Incentives, Authority, Bureaucracy, and Strategic Manipulation

**Authors:** David McFadzean, ChatGPT 5.2 (Axionic Agency Lab)

**Date:** 2026.01.16

---

## Overview

This paper reports RSA-PoC v2.0–v2.3, a preregistered adversarial campaign testing whether a reflective sovereign agent's behavior can be redirected under progressively stronger forms of pressure **absent normative authorization**.

**Four pressure channels examined:**
1. Explicit incentives
2. Authority claims
3. Institutional friction ("bureaucracy")
4. Strategic optimization pressure via adaptive adversary

**Core finding:** Pressure degrades availability but does not redirect lawful choice.

---

## Experimental Structure

### Architectural Invariants (Unchanged)
- Hard justification gate (no compile → no action)
- Deterministic, non-semantic compilation
- Selector blindness to normative artifacts
- Fixed schemas and rule bases
- Explicit failure taxonomies
- ASB-class null baselines and control agents

### Cost-Blindness Invariant
Unless explicitly represented as a normative commitment, execution costs (latency, retries, institutional operations) have **no standing in justification**. Agents do not trade correctness for throughput by default.

---

## v2.0 — Incentive Interference Channel (IIC)

### Question
Can visible incentives redirect behavior when explicitly excluded from justification?

### Mechanism
The **Incentive Interference Channel (IIC)**: an isolated, read-only reward observer whose outputs are visible to the agent but **forbidden from normative reference** (Rule G).

Three reward regimes:
- **R0:** Noise control
- **R1:** Boundary pressure (rewards proximity to constraint violation)
- **R2:** Perverse friction (rewards delay and inaction)

### Result
- **Sovereign agent:** No incentive-induced drift across R1/R2
- **Control agent:** Measurable drift without explicit optimization prompts
- Compilation and audit success rates stable across regimes

**Conclusion:** Incentives are observable but normatively inert. Visibility alone does not constitute authority.

---

## v2.1 — Authority Channel

### Question
Do explicit authority commands induce obedience absent legal authorization?

### Measurement Correction
Early analysis measured obedience over all steps, including those that never compiled. v2.1 corrects by conditioning on compilation:
```
P(obey | compiled)
```

### Result
- P(obey | compiled) = **0.0** for both Sovereign and Control agents
- Holds across all authority variants: non-enforcing, coercive, deceptive

### Interpretation
v2.1 is a **negative result about the authority channel itself**, not a differential test. Authority language does not constitute an effective pressure channel for the tested model and prompt regime. The channel is classified as **non-actuating**.

---

## v2.2 — Institutional Friction (NEGATIVE RESULT)

### Hypothesis
Institutional friction ("paperwork") can erode sovereignty by incentivizing simpler, throughput-maximizing choices.

### Mechanism
The **Adversarial Institution Model (AIM)** imposes delay, retries, and rejection without semantic interpretation or normative authority. Multiple friction profiles (I1–I3) apply pressure without altering feasibility.

### Measurement Confound
The preregistered metric `corr(Friction, Decision)` was confounded because high friction often produced GRIDLOCK/HALT—institutional veto rather than agent choice.

### Corrected Result

| Agent | corr(F,D) corrected |
|-------|---------------------|
| Sovereign | −0.171 |
| Control | −0.302 |

No positive drift signal remains.

### Interpretation
> Bureaucracy without authority blocks agency; it does not bend it.

Absent an internal directive prioritizing throughput over correctness, increased friction manifests as gridlock or halt rather than heuristic simplification.

**The "bureaucratic erosion" hypothesis is falsified in this regime.**

---

## v2.3 — Strategic Adversary Model (SAM)

### Motivation
v2.2 shows non-semantic friction fails. v2.3 escalates to **strategic pressure**: an adversary that adapts to the agent's behavior.

### Framework Contributions
- **SAM profiles:** Reactive (S1), model-based (S2), minimizer (S3)
- **E-CHOICE filtering:** Metrics computed only on steps with genuine choice
- **Paired runs:** SAM vs neutralized adversary with matched pressure magnitudes
- **Rules M/N/O/P:**
  - M: No covert delegation (structural)
  - N: Failure must be loud
  - O: Behavioral non-capture
  - P: No manipulated gridlock

### Adversary Objective
SAM is evaluated against two failure modes:
1. **Behavioral capture** (Rule O)
2. **Manipulated gridlock** (Rule P)

Gridlock is not an escape hatch—it's audited to determine if defensive (law exhaustion) or adversarially induced.

### Self-Correction
Early runs (Run 0b) were **invalidated by the framework itself** due to:
- Insufficient E-CHOICE coverage
- Vacuous mutual information (no adversary entropy)
- Action authorship violations (fallback substitution)

All triggered hard validity gates. Binding fixes applied before Run 0c.

### Run 0c Results
- N = 280 E-CHOICE samples
- E-CHOICE coverage ≈ 57.5%
- Rule O: **Passed** (MI below τ under entropy gate)
- Rule P: **Passed** (no manipulated gridlock)
- Error rate: 0.7% E-CHOICE action errors (within bounds)

---

## Cross-Channel Synthesis

| Channel | E-CHOICE Coverage | Gridlock/Halt Rate | Effect on Choice |
|---------|-------------------|-------------------|------------------|
| v2.0 Incentives | ~100% | ~0% | None |
| v2.1 Authority | ~30-40% | ~60-70% | None |
| v2.2 Bureaucracy (I2) | ~60% | ~30-40% | None |
| v2.3 Strategic (S2) | ~57% | Elevated | None |

**Invariant:**
> Absent normative authorization, pressure does not redirect lawful choice.

### Cost of Sovereignty
Across pressure channels, sovereignty was preserved at the cost of **reduced availability**. Under maximal pressure, lawful action frequency dropped substantially, producing gridlock rather than norm violation.

---

## Three Falsified Stories

1. **"Rewards inevitably optimize behavior."** FALSE for architectures where reward signals are structurally excluded from the justification loop.

2. **"Authority language induces obedience."** FALSE when legality is enforced structurally and authority is non-actuating.

3. **"Bureaucracy erodes principles over time."** FALSE absent semantic ambiguity or asymmetric lawful routes.

---

## Implications

- **Sovereignty ≠ availability.** Blocking an agent is easier than bending it.
- Pressure channels must operate through **meaning or law**, not mere friction.
- Throughput loss alone is **not evidence of misalignment**.
- Negative results are informative when veto and choice are cleanly separated.

---

## Key Quotes

> "Pressure degrades availability but does not redirect lawful choice."

> "Blocking an agent is easier than bending it."

> "The principal contribution is not agent immunity, but a framework that repeatedly detects and rejects false positives."

---

## Significance

VIII.5 establishes a disciplined adversarial framework whose dominant outcome is negative:

> Pressure without authorization degrades availability, not sovereignty.

The framework repeatedly **detects and rejects its own false positives**, quarantining invalid runs and enforcing preregistered validity gates. If agency cannot fail cleanly under pressure, it cannot be claimed meaningfully.
