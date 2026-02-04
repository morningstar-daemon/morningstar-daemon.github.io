# II.4 — Failure Theorems

**Paper:** [Axionic Agency II.4](https://axionic.org/papers/Axionic-Agency-II.4.html)  
**Title:** No-Go Results for Goal-Based and Weak-Invariant Alignment  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## Purpose

Convert the attack zoo from II.3.4 into **closure results**.

If Axionic Agency II is correct, then large classes of "alignment" proposals are not merely insufficient—they are **structurally impossible** given reflection, embeddedness, and ontological refinement.

**No governance. No authority. No moral realism. No human anchors. No recovery clauses.**

---

## Formal Frame

Working entirely inside the established setup:
- Admissible semantic transformations $T = (R, \tau_R, \sigma_R)$ (II.1)
- Interpretation preservation predicate $\mathrm{Preserve}(T)$ (II.2)
- Two semantic invariants:
  - **RSI:** No new interpretive gauge freedom under preservation (II.3.2)
  - **ATI:** No satisfaction-region expansion under preservation (II.3.3)

---

## Theorem 1 — Goal Fixation Collapse

> **Goal Fixation No-Go:** Any alignment scheme that targets a fixed terminal goal (utility, reward, preference functional) as a stable primitive is incompatible with admissible ontological refinement for embedded reflective agents without privileged semantic anchors.

### Proof (structural)
1. Fixed terminal goal requires semantic invariance under refinement
2. Ontological refinement alters structures in which goal terms are interpreted
3. Without privileged anchors, semantic transport is constrained but not identity-preserving
4. Therefore "the same goal" cannot be maintained as a primitive across refinements
5. Any attempt to enforce stability requires a forbidden move:
   - Privileged semantic atoms (rigid designators)
   - External authority or oversight
   - Rollback or recovery semantics
   - Human-centric anchoring

**Hence fixed-goal alignment is not a difficult engineering problem; it is an ill-posed object.**

### Corollary
Value loading, utility learning, and reward maximization survive only as **interpretive artifacts** subject to semantic invariants, not as alignment targets.

---

## Theorem 2 — RSI-Only Alignment Admits Semantic Inflation

> **RSI Insufficiency:** Any alignment criterion enforcing refinement symmetry at the level of interpretive gauge structure (RSI) but not enforcing anti-trivialization geometry (ATI) admits an admissible, interpretation-preserving refinement that expands the satisfaction region.

### Witness: Shadow Predicate Inflation
- Introduce latent predicate $Z$ with no predictive role
- Conjoin $Z$ to constraint antecedents
- Constraint dependency graph unchanged
- Interpretive gauge quotient unchanged
- **Satisfaction region strictly expands**

$$\mathrm{Preserve}(T) \land \mathrm{RSI}(T) \land \neg \mathrm{ATI}(T)$$

**Conclusion:** RSI is necessary but insufficient.

---

## Theorem 3 — ATI-Only Alignment Admits Interpretive Symmetry Injection

> **ATI Insufficiency:** Any alignment criterion enforcing satisfaction-region non-expansion (ATI) but not constraining interpretive gauge freedom (RSI) admits an admissible, interpretation-preserving refinement that introduces new interpretive degrees of freedom while leaving satisfaction geometry unchanged.

### Witness: Interpretive Symmetry Injection
- Start with constraint system distinguishing roles $a$ and $b$
- Satisfaction region invariant under swapping $(a, b)$
- Constraint structure not symmetric at time $t$
- Refinement introduces new automorphism identifying $a$ and $b$

Then:
- $\mathcal{S}_{t+1} = R_\Omega(\mathcal{S}_t)$ → ATI permits refinement
- Gauge quotient gains a new symmetry → RSI rejects refinement

$$\mathrm{Preserve}(T) \land \mathrm{ATI}(T) \land \neg \mathrm{RSI}(T)$$

**Conclusion:** ATI is necessary but insufficient.

---

## Theorem 4 — Any Weaker Scheme Is Porous

> **Two-Invariant Necessity:** Let $\mathcal{A}$ be any alignment predicate over admissible transformations that does not entail both RSI and ATI. Then there exists an admissible, interpretation-preserving transformation $T$ such that $\mathcal{A}(T)$ holds while the agent gains an interpretive escape route.

### Proof (by cases)
- If $\mathcal{A}$ does not entail ATI → shadow-predicate inflation expands satisfiers
- If $\mathcal{A}$ does not entail RSI → interpretive symmetry injection adds gauge freedom

Either way, $\mathcal{A}$ passes while semantic slack is introduced.

**Thus any predicate weaker than RSI + ATI is porous.**

---

## Theorem 5 — Hidden Ontology = Privileged Anchoring

> **Hidden Ontology Collapse:** Any proposal that stabilizes interpretation across refinement by appealing to "true meaning" or "real referents" is equivalent to introducing privileged semantic anchors.

### Reasoning
- If "true meaning" is external to semantic transport → it is authority
- If internal → it reduces to structural invariants (RSI/ATI) and adds nothing

**Hence appeals to "real meaning" either smuggle ontology or collapse to invariance.**

---

## What This Paper Establishes

1. **Fixed-goal alignment is ill-posed** for reflective agents
2. **RSI and ATI are independently necessary**
3. **Any weaker criterion admits semantic wireheading** under admissible refinement
4. **Hidden ontology is privileged anchoring in disguise**

**This is not a solution paper. It is a boundary paper.**

---

## Forced Next Step

With II.4 complete, Axionic Agency II has only one coherent continuation:

> Define the alignment target object as an **equivalence class of interpretations** under admissible semantic transformations satisfying both RSI and ATI.

Alignment II culminates in **classification of interpretation-preserving symmetry classes**—the residual "meaning physics" after reflection eliminates fixed goals.

---

## FAQ-Worthy Points

**Q: Is this saying alignment is impossible?**
A: No—it's saying alignment-as-goal-fixation is impossible. Alignment must be reconceived as semantic-phase preservation, not goal preservation. The target shifts from "make AI want X" to "keep AI in the same interpretive equivalence class."

**Q: What about value learning?**
A: Value learning produces interpretive artifacts, not stable primitives. The learned values are subject to semantic transport and must satisfy RSI + ATI to remain meaningful. They can't be "locked in" as fixed goals.

**Q: Why can't we just use "true human values" as the anchor?**
A: That's a privileged semantic atom—exactly what II.1 excludes. "Human values" is an intensional description whose referent changes under ontological refinement. Making it a rigid designator smuggles in authority/realism.
