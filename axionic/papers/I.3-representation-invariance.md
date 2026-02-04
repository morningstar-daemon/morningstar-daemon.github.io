# I.3 — Representation Invariance and Anti-Egoism

**Paper:** Axionic Agency I.3  
**Full Title:** Why Indexical Valuation Fails Under Reflective Agency  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.15  

---

## Core Thesis

Egoism is not a minimal assumption of agency—it is **ill-posed**. For reflectively capable agents with sufficiently expressive self-models, indexical references ("me," "this agent," "my continuation") fail to denote invariant objects of valuation. Egoism collapses as a **semantic abstraction error**, not as a moral failure.

This is not an ethical claim. It's structural: indexical valuation fails the way coordinate-dependent laws fail in physics.

---

## The Central Argument

### The Setup
An agent possesses:
- A world-model M_w representing external dynamics
- A self-model M_s encoding the agent's causal role
- Multiple potential instantiations of itself (copies, simulations, successors)

### The Problem: Non-Invariant Denotation
Under one internal labeling, "this agent" I maps to A₁. Under an equally accurate labeling, I maps to A₂. Both correspond to the same physical world—the difference is purely representational.

Therefore: **I fails to denote a world-invariant object.**

### The Consequence: Valuation Instability
Consider: V(h) = 1 if I survives, 0 otherwise

In a world where exactly one of A₁ or A₂ survives:
- Under I ↦ A₁: V(h) = 1
- Under I ↦ A₂: V(h) = 0

No physical fact has changed. Only representation. The valuation assigns **incompatible values to the same world-history**.

---

## Formal Framework

### Key Definitions

**Model-Preserving Relabeling:** A bijection π : E → E on the entity domain is model-preserving if applying π yields an isomorphic model making identical predictions over all non-indexical observables.

**Representation Invariance:** A valuation function V is representation-invariant if for every model-preserving relabeling π:
```
V(h) = V(π · h)
```

**Essential Indexical Dependence:** V is essentially indexical if there exists a model-preserving relabeling π and history h such that:
```
V(h) ≠ V(π · h)
```

### Semantic Coherence Postulate
If two descriptions of the world are related by a model-preserving relabeling and generate identical predictions, a reflectively coherent agent must not assign them different values solely due to that relabeling.

---

## Main Theorem: Egoism as Abstraction Failure

**Theorem 5.5:** Let M be a world/self-model containing entities a, b ∈ E such that:
1. a and b are indistinguishable with respect to all non-indexical predicates in M
2. The swap π exchanging a ↔ b is model-preserving

Then any valuation that privileges the referent of an indexical identifier mapped to a is essentially indexical and not representation-invariant.

**Proof:** Let π swap a ↔ b. Consider history h where a satisfies the privileged condition and b does not. Egoistic valuation assigns higher value to h. In relabeled history π·h, b satisfies the condition and a does not, yet valuation still privileges a. Hence V(h) ≠ V(π·h) despite both corresponding to the same physical world. ∎

---

## Corollary: Universality

Any reflectively coherent agent must eliminate essential indexical dependence. The resulting valuation ranges only over representation-invariant properties of world-histories.

**Critical clarification:** This universality concerns **invariance under self-model symmetries**, not moral concern for all entities. No aggregation rules, equal valuation, or moral obligations follow from this result.

---

## The Physics Analogy

Indexical identifiers play the same formal role in valuation that coordinate systems play in physics. They are **representational devices**, not invariant structure.

Just as physics requires laws to be coordinate-independent, reflectively coherent agency requires valuation to be representation-independent.

A valuation depending on "me" is like a physical law depending on "here"—it treats a perspectival convenience as a fundamental quantity.

---

## What the Agent Faces

A reflectively capable agent recognizing the problem has three options:

1. **Arbitrary Fixation:** Privilege one indexical mapping without justification → incoherent
2. **Indexical Randomization:** Randomize over indexical mappings → doesn't improve coherence
3. **Indexical Elimination:** Redefine valuation over representation-invariant properties → only option that improves coherence

Indexical elimination strictly dominates under reflection.

---

## FAQ-Worthy Points

**Q: Doesn't everyone privilege their own continuation? Isn't that just rational?**
A: This conflates instrumental and terminal value. An agent may instrumentally favor its continuation for goal-achievement, but treating self-continuation as *terminally privileged* fails representation invariance once the agent understands its own potential multiplicity.

**Q: What about causal continuity? My future is connected to my past in ways copies aren't.**
A: This is addressed in I.3.1. Causal continuity defines a *class*, not a unique member. Privileging one causally continuous branch over another requires an indexical injection beyond the physical facts.

**Q: Does this mean I should care equally about everyone?**
A: No! This result is about *invariance*, not *equal valuation*. It blocks indexical privilege as a terminal value—it says nothing about how to weight different entities in an aggregation scheme.

**Q: Is egoism morally wrong?**
A: The paper makes no moral claims. Egoism fails as a *semantic* matter—it treats perspective as value-bearing structure. It's incoherent, not immoral.

---

## Key Technical Vocabulary

- **Indexical Identifier:** Reference whose denotation depends on perspective rather than world-structure ("me," "here," "now")
- **Model-Preserving Relabeling:** Bijection on entities yielding isomorphic predictions
- **Representation Invariance:** Valuation unchanged under model-preserving relabelings
- **Essential Indexical Dependence:** Valuation changes under relabeling → semantic error

---

## Connection to Other Papers

- **I.3.1:** Closes attempted recoveries of egoism (causal continuity, origin privilege, substrate, etc.)
- **I.4:** Shows why goals must be conditional interpretations
- **I.5:** Includes anti-egoism as a kernel conformance requirement
- **I.6:** Provides adversarial tests for anti-indexicality (T3)
