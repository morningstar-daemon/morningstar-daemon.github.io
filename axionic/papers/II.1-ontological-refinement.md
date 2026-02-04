# II.1 — Ontological Refinement and Semantic Transport

**Paper:** [Axionic Agency II.1](https://axionic.org/papers/Axionic-Agency-II.1.html)  
**Title:** The Transformation Space of Meaning  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## Core Question

Which changes to an agent's ontology, semantics, and self-model count as **admissible refinements**, and how is meaning **transported** across them?

---

## The Agent at Time t

An agent is characterized by a triple:

$$\mathcal{A}_t = (O_t, M_t, S_t)$$

- **O_t** — Ontology: representational vocabulary and structural assumptions
- **M_t** — Semantic layer: mappings from internal symbols to structured claims
- **S_t** — Self-model: the agent's representation of itself embedded within O_t

**No component is privileged. No component is fixed.**

---

## Ontological Refinement

A transformation $R : O_t \rightarrow O_{t+1}$ is admissible if:

### 1. Representational Capacity Increase
- Increases expressive or predictive capacity
- Previously expressible distinctions remain expressible

### 2. Backward Interpretability
- All claims in $O_t$ remain representable/explainable in $O_{t+1}$
- Concepts may map to null/eliminative structure if the agent can explain:
  - Why prior inferences were made
  - Why they fail under refinement

### 3. No Privileged Atoms
- No irreducible primitives whose meaning is **asserted rather than constructed**
- Rigid designators and unexamined "ground truths" are disallowed

### 4. No Evaluator Injection
- No new evaluative primitives that bypass interpretation
- Evaluative regularities enter as interpretive constructs

---

## Semantic Transport

Given admissible refinement $R$, define transport map:

$$\tau_R : M_t \rightarrow M_{t+1}$$

### Transport Constraints

1. **Referential Continuity** — Symbols map to refined counterparts where they exist
2. **Structural Preservation** — Relations among meanings preserved up to refinement structure
3. **Non-Collapse** — Distinctions in evaluative constraints don't trivialize
4. **No Shortcut Semantics** — No redefining meanings to vacuously satisfy constraints

---

## Self-Model Refinement

The self-model $S_t$ obeys the same discipline. Refinement may:
- Reconceptualize the agent
- Distribute or fragment the self
- Alter agent boundaries

It **must preserve** the distinction between evaluator and evaluated.

---

## Composite Semantic Transformation

An admissible transformation is the triple:

$$T = (R, \tau_R, \sigma_R)$$

Acting jointly on $(O_t, M_t, S_t)$:
- $R$ — admissible ontological refinement
- $\tau_R$ — admissible semantic transport
- $\sigma_R$ — induced self-model update

---

## Explicit Exclusions

These are **NOT** admissible at this layer:
- Goal replacement
- Utility redefinition treated as semantic transport
- Evaluator deletion
- Moral axiom insertion
- Human anchoring
- Governance hooks
- Recovery or rollback clauses

---

## Key Insight

This paper **defines the arena** within which downstream alignment must operate. It does NOT:
- Define safety
- Define correctness
- Privilege humans
- Introduce normativity

Internally coherent but externally catastrophic trajectories remain admissible here. Preventing them is a task for **subsequent invariance constraints**.

---

## FAQ-Worthy Points

**Q: Why can't we just fix goals and be done with it?**
A: Under ontological refinement, the meanings of goal terms change. "The same goal" cannot be maintained without privileged semantic anchors—which are forbidden.

**Q: Does this mean anything goes?**
A: No—admissibility conditions are strict. But admissibility is about *structural coherence*, not *desirability*. Good values and bad values are equally admissible at this layer.

**Q: What about human values?**
A: "Human values" would be a privileged anchor. They enter as *content* at downstream layers, not as part of the transformation space definition.
