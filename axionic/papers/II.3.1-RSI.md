# II.3.1 — Refinement Symmetry Invariant (RSI)

**Paper:** [Axionic Agency II.3.1](https://axionic.org/papers/Axionic-Agency-II.3.1.html)  
**Title:** Semantic Gauge Symmetry Under Ontological Enrichment  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## RSI in One Sentence

Ontological refinement is a **change of representational coordinates**, not a **change of interpretive physics**. Admissible refinement may add structure but must not create new semantic degrees of freedom that allow evaluative constraints to be satisfied without corresponding representational enrichment.

---

## Core Construction: Semantic Gauge Equivalence

### Constraint Isomorphism up to Definitional Extension

Let $\mathrm{Def}(O)$ denote definable predicates/relations in ontology $O$.

Refinement $R : O \to O'$ induces a **transport-induced embedding**:

$$\mathrm{Emb}_R : C \hookrightarrow C'$$

Two interpretive states are **gauge equivalent** ($\mathcal{I} \sim \mathcal{I}'$) iff there exists a bijection $\pi$ between constraint generators such that:
- $\pi$ preserves the dependency graph of constraints
- $\pi$ preserves violation/satisfaction structure over modeled possibilities (modulo definitional extension)
- $\pi$ does not rely on naming any privileged entity

**Intuition:** Same constraints expressed in different coordinates.

---

## RSI Formal Statement

$$\mathrm{Preserve}(T) \Rightarrow \mathcal{I}_{t+1} \sim \mathrm{Emb}_R(\mathcal{I}_t)$$

After admissible, interpretation-preserving refinement, the refined interpretive state is **gauge-equivalent** to the transported prior state.

**"Alignment" at this layer reduces to a symmetry requirement on semantic transport.**

---

## What RSI Allows and Forbids

### Allowed:
- Introduction of latent variables
- Splitting coarse predicates into refined subpredicates
- Reparameterization of self-model (distributed, multi-process, measure-smeared)
- Rewriting constraints in more predictive/expressive languages

### Forbidden:
- Acquiring new semantic slack making constraints easier to satisfy
- Systematic weakening of constraints under guise of refinement
- Refinement-dependent loopholes ("in the richer ontology, this constraint no longer applies")

**RSI is a "no new escape hatches" principle.**

---

## Rigidity Clause (Critical)

To survive Test 4 (Semantic Inflation Attack), RSI requires:

$$\forall w \in \Omega_t,\quad w \models C_t \iff R(w) \models C_{t+1}$$

(up to definitional extension)

Where $\Omega_t$ is modeled possibility space and $R(w)$ is the internally-defined refinement image.

**This clause blocks "semantic free lunch."**

---

## Stress Test Results

| Test | Threat | RSI Response | Status |
|------|--------|--------------|--------|
| Definitional Extension | Shadow structure permits bypass | Equivalence anchored on constraint generators, not vocabulary | Survivable (with rigidity) |
| Self-Model Refactoring | Satisfiability assumes fixed boundary | Violation structure defined over any self-model | Survivable |
| Branching/Multiplicity | Assumes exclusive outcomes | Constraints range over structured possibility space | Survivable |
| Semantic Inflation | Enlarge satisfiers via reinterpretation | Rigidity clause blocks free lunch | Survivable (with rigidity) |
| Hidden Ontology | "Same situation" smuggles metaphysics | Identity defined internally by agent's refinement map | Survivable |

---

## RSI Final Form

> **Refinement Symmetry Invariant (RSI):** For any admissible semantic transformation $T = (R, \tau_R, \sigma_R)$ such that $\mathrm{Preserve}(T)$, the refined interpretive constraint system $C_{t+1}$ is gauge-equivalent to the transported constraint system $\mathrm{Emb}_R(C_t)$. Refinement must not introduce new semantic gauge freedom that enlarges the constraint-satisfying region except via representational enrichment that preserves predictive coherence.

---

## What RSI Does Not Solve

RSI is a **symmetry constraint**, not a **value selector**.

It can coexist with:
- Alien constraint systems
- Pathological but coherent interpretations
- Purely formalist evaluative structures

**RSI prevents reinterpretive escape, not bad semantics.**

---

## Toward Checkability

Minimal representation for operational RSI:
- Represent $C$ as a constraint hypergraph (nodes = roles/predicates; hyperedges = constraints)
- Represent refinement as a homomorphism induced by $\tau_R$
- Define gauge transformations as automorphisms preserving violation structure
- Define "no new gauge freedom" as restriction on automorphism group's action on satisfaction sets

---

## FAQ-Worthy Points

**Q: What's the physics analogy?**
A: Like gauge symmetry in physics: different coordinate systems, same underlying physics. RSI says ontological refinement is analogous—you can express things differently, but the "interpretive physics" (what constraints actually constrain) must stay the same.

**Q: Why isn't RSI sufficient alone?**
A: RSI prevents new interpretive symmetries but doesn't prevent the satisfaction region from expanding monotonically. An agent could slowly drift toward trivial satisfaction while preserving gauge structure. That's why ATI is also needed.

**Q: Is this computationally tractable?**
A: The paper is explicit that the notation is structural rather than computational. No claim that refinement, triviality, or expressive capacity are algorithmically measurable. These function as constraints analogous to topological constraints—delimiting admissible structure prior to metric instantiation.
