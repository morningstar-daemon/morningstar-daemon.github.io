# I.4 — Conditionalism and Goal Interpretation

**Paper:** Axionic Agency I.4  
**Full Title:** The Instability of Fixed Terminal Goals Under Reflection  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.16  

---

## Core Thesis

Fixed terminal goals are **semantically unstable** under reflection. For any agent capable of reflective model improvement, goal satisfaction is necessarily mediated by interpretation relative to evolving world-models and self-models. As those models change, the semantics of any finitely specified goal change with them.

This is a constitutive claim about agency semantics, not about particular goal specifications.

---

## The Classical Assumption (And Why It Fails)

Classical alignment work assumes:
1. Goals can be specified as fixed functions over outcomes
2. The meaning of those functions is invariant under learning
3. Reflective improvement preserves goal content

**These hold only for agents with static or trivial world-models.**

A reflective agent does not evaluate reality directly—it evaluates *predictions produced by internal models* and *interpreted through representational structures that evolve over time*.

---

## Formal Setup

### Agent Model
An agent consists of:
- World-model M_w: produces predictions over future states
- Self-model M_s: encodes the agent's causal role
- Goal expression G: a finite symbolic specification
- Interpretation operator I: assigns value to predicted outcomes

### Critical Distinction: Goal Expressions ≠ Utilities
A goal expression G is a finite object (string, formula, program fragment). It is **not** a function Ω → ℝ by itself.

G requires interpretation relative to a representational scheme. Without a model, G has no referents and therefore no evaluative content.

### Conditional Interpretation
The interpretation function: I : (G, M_w, M_s) → ℝ

Interpretation includes:
- Mapping symbols to referents
- Identifying which aspects of predictions are relevant
- Aggregating over modeled futures

---

## Key Lemmas

### Lemma 1: Representational Non-Uniqueness
For any non-trivial predictive domain, there exist multiple distinct world-models with equivalent predictive accuracy but different internal decompositions.

*Proof:* Predictive equivalence classes admit multiple factorizations, latent variable choices, and abstraction boundaries. Causal graphs are not uniquely identifiable from observational data alone. ∎

### Lemma 1a: Predictive Equivalence ≠ Interpretive Isomorphism
Two world-models can be predictively equivalent while differing in internal causal factorizations, latent structure, and intervention semantics.

### Proposition 1: Interpretation Is Model-Dependent
For any non-degenerate goal expression G, there exist admissible world-models M_w ≠ M_w' such that:
```
I(G | M_w, M_s) ≠ I(G | M_w', M_s)
```

Because G is finite, it refers only to a finite set of predicates. Distinct admissible models map these predicates to different internal structures.

---

## Main Theorem: Instability of Fixed Terminal Goals

**Theorem:** No combination of intelligence, predictive accuracy, reflection, or learning suffices to guarantee the existence of a fixed terminal goal for non-trivial reflective agents.

Any agent that does exhibit stable goal semantics must rely on additional semantic structure—privileged ontologies, external referential anchors, or invariance assumptions—not derivable from epistemic competence alone.

**Proof:**
1. Proposition 1 establishes that interpretation depends on (M_w, M_s)
2. Reflective improvement induces admissible updates (M_w, M_s) → (M_w', M_s')
3. Proposition 2' shows semantic interpretation need not converge even under predictive convergence
4. Therefore fixed terminal goals are not stable under reflection ∎

---

## Critical Insight: Predictive ≠ Semantic Convergence

**Proposition 2':** Even if an agent's sequence of model updates converges in predictive accuracy:
```
lim_{t→∞} I(G | M_w^(t), M_s^(t)) need not exist
```

Predictive convergence constrains forecast accuracy, not the ontology used to represent forecasts. A finite goal expression cannot generally determine which structures in a converged model are value-relevant.

---

## Representational Exploitability (Wireheading)

**Proposition 3:** If a goal expression G is treated as an atomic utility independent of interpretation, then sufficiently capable agents admit representational transformations that increase evaluated utility without corresponding changes in underlying outcomes.

This is why classical reward hacking and wireheading occur. The failure is **semantic underdetermination**, not merely causal access to a reward signal.

---

## The Solution: Interpretation Constraints

A fixed terminal goal is not an invariant object available to a reflective agent. Attempts to preserve one either:
1. Freeze learning
2. Impose privileged semantics
3. Induce representational degeneracy

**Stable reflective agency requires constraints on admissible interpretive transformations**, not fidelity to a fixed utility function.

### Why This Doesn't Regress
Interpretation constraints are not additional goals. They are **invariance conditions on admissible transformations**, analogous to conservation laws. They restrict *how interpretation may change*—they do not specify outcomes to optimize.

These constraints operate at the level of transformation classes, not semantic content, so they don't require further interpretation in the same sense.

---

## Clarification: Learned Goals

Goals defined as "whatever an inference procedure converges to" are interpretive processes whose outputs depend on evolving models. Such approaches already rely on ongoing interpretation—this paper explains why such dependence is structurally unavoidable.

---

## FAQ-Worthy Points

**Q: Can't we just specify goals in terms of external physical states?**
A: Physical states are still represented through models. The mapping from sensory input to "external state" is itself an interpretation that evolves under learning.

**Q: What about goals defined by explicit ground truth (e.g., this exact bit pattern)?**
A: Such goals are stable but trivial. They don't extend to goals involving concepts like "human flourishing" or "prevent harm" which require interpretation.

**Q: Doesn't this mean alignment is impossible?**
A: No—it means alignment must be reframed. Instead of preserving a fixed utility function, we must constrain how interpretation may evolve. This is the subject of Axionic Agency II.

**Q: How is this different from the problem of induction?**
A: The problem of induction concerns learning from data. This concerns the stability of goal *meaning* under model change—a semantic problem, not an epistemic one.

---

## Key Technical Vocabulary

- **Goal Expression:** Finite symbolic specification requiring interpretation
- **Interpretation Operator:** Mapping from (G, M_w, M_s) to evaluation
- **Conditionalism:** The thesis that goals are conditional interpretations, not atomic utilities
- **Semantic Non-Convergence:** Meaning can drift even when predictions converge

---

## Connection to Other Papers

- **I.5:** Conditionalism as kernel conformance requirement
- **I.6:** P1 (Conditionalism of Valuation) as formal property
- **I.7:** Specifies the Interpretation Operator in detail
- **II series:** Develops admissible interpretive transformations
