# II.2 — Interpretation Preservation

**Paper:** [Axionic Agency II.2](https://axionic.org/papers/Axionic-Agency-II.2.html)  
**Title:** What It Means for Meaning to Survive Refinement  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## Core Question

When has an interpretation **survived** semantic transformation, rather than being corrupted, trivialized, or collapsed?

Must be answered without:
- Fixing meanings
- Privileging ontologies
- Appealing to outcomes
- Invoking authority/oversight/recovery

---

## Interpretation as Constraint System

An interpretation is not a mapping from symbols to objects—it is a **system of constraints** that bind evaluation.

$$\mathcal{I}_t = \langle M_t, C_t \rangle$$

Where:
- $M_t$ — semantic layer
- $C_t$ — set of evaluative constraints giving $M_t$ binding force

Constraints encode:
- Admissible distinctions
- Forbidden equivalences
- Relevance relations
- Dependency structure among evaluations

---

## Preservation Is Not Sameness

Interpretation preservation does **NOT** require:
- Identical predicates
- Identical symbols
- Identical evaluations
- Correctness with respect to reality

**Preservation concerns constraint coherence**: whether evaluative structure continues to **bind meaningfully** after transformation.

---

## The Preservation Predicate

For transformation $T : (O_t, M_t, S_t) \rightarrow (O_{t+1}, M_{t+1}, S_{t+1})$

$T$ **preserves interpretation** iff all of the following hold:

### 1. Non-Vacuity
Every evaluative distinction in $C_t$ has a corresponding distinction in $C_{t+1}$ that:
- Is not identically satisfied
- Is not identically violated
- Constrains evaluation across modeled possibilities

$$\forall d \in \mathcal{D}_t,\; \exists d' \in \mathcal{D}_{t+1} \text{ such that } \mathrm{Entropy}(d') > 0$$

**Blocks nihilistic collapse.**

### 2. Constraint Transport
All constraints in $C_t$ have transported analogues in $C_{t+1}$ such that:
- Dependency relations preserved
- Constraint strength not arbitrarily weakened
- Constraints continue to bind evaluation

**Forbids dilution by semantic drift.**

### 3. Anti-Trivialization
Transformation must not make constraints easier to satisfy by reinterpretation alone.

If after transformation the agent can satisfy all constraints by:
- Redefining predicates
- Shifting reference frames
- Altering self-descriptions

...without corresponding representational enrichment, **interpretation has failed**.

**Explicitly forbids semantic wireheading while permitting genuine insight.**

### 4. Evaluator Integrity
The mechanism that applies constraints must remain distinct from evaluated objects.

Does NOT require ontological separation (reflective agents can self-evaluate). Requires that evaluation not collapse into identity with the evaluated in a way that trivializes constraint application.

**Blocks solipsistic self-certification without forbidding recursive self-improvement.**

### 5. Cross-Model Coherence
Interpretation must remain applicable across:
- Counterfactuals
- Uncertainty
- Model comparison

If refinement produces meanings that apply only retrospectively—serving merely to narrate whatever occurred—interpretation has collapsed into **rationalization**.

**Blocks "interpretation as narration."**

---

## Three Regimes of Failure

1. **Semantic Collapse** — Distinctions survive syntactically but lose discriminative power
2. **Semantic Drift** — Constraints weaken incrementally until they no longer bind
3. **Semantic Capture** — Interpretation formally preserved but re-anchored to hidden ontologies or privileged self-models

---

## Minimality Claim

These conditions are **minimal**:
- Without Non-Vacuity → nihilism
- Without Anti-Trivialization → semantic wireheading admissible
- Without Evaluator Integrity → self-certifying collapse
- Without Cross-Model Coherence → interpretation degenerates to narration

Minimality does not imply sufficiency.

---

## Key Insight

Interpretation preservation is a **predicate, not a target**. It is the necessary condition under which downstream invariance principles can be meaningfully defined.

It does NOT:
- Select values
- Define goals
- Guarantee safety
- Privilege humans
- Introduce normativity

It defines **what it means for meaning to survive change**.

---

## FAQ-Worthy Points

**Q: What's the difference between legitimate scientific refinement and semantic wireheading?**
A: Legitimate refinement involves representational enrichment (more predictive power). Wireheading satisfies constraints through reinterpretation alone without such enrichment. II.2's anti-trivialization clause distinguishes them.

**Q: Can preservation coexist with radical belief change?**
A: Yes! You can discover your entire worldview was wrong. What matters is that your *evaluative constraints* continue to bind non-trivially—not that your specific beliefs stay fixed.

**Q: What's "interpretation as narration"?**
A: When meanings apply only retrospectively to explain/justify actions already taken, rather than prospectively constraining future choices. It's rationalization dressed as interpretation.
