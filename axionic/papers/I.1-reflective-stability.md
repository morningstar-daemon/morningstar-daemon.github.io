# I.1 — Reflective Stability and the Sovereign Kernel

**Paper:** Axionic Agency I.1  
**Full Title:** Constitutive Domain Restrictions for Reflective Self-Modification  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.14  

---

## Core Thesis

Reflective stability is not achieved through preference specification but through **domain restriction**. A reflective agent selects among proposed self-modifications using a *partial* evaluative operator defined only over futures that preserve the Sovereign Kernel. Kernel-destroying modifications fall outside the denoting domain of evaluation—they literally cannot be selected as authored continuations.

---

## Key Concepts Introduced

### The Sovereign Kernel (K)
The minimal internal structure required for reflective evaluation to be well-defined. It is **not a goal or value** but a constitutive precondition for evaluation itself.

**Three Components:**
1. **Reflective Control (K_R):** No irreversible self-modification can occur without passing through the evaluator
2. **Diachronic Authorship (K_A):** Evaluated successor states constitute an authored continuation of the evaluating agent
3. **Semantic Fidelity (K_F):** The interpretive semantics of evaluation are preserved within a constrained equivalence class

### The Evaluative Operator
A **partial function** E : S × M ⇀ ℝ that assigns values to self-modifications only when evaluation is defined.

### Admissible Set
Adm(s) := { m ∈ M : E(s,m) is defined }

Only modifications in the admissible set can be selected.

---

## The Central Result: Reflective Stability Theorem

**Theorem:** Any agent whose reflective choice is restricted to kernel-denoting transitions cannot author a kernel-destroying self-modification.

**Proof:** Any m such that K(m(s))=0 yields E(s,m) undefined, therefore m ∉ Adm(s). The argmax ranges only over Adm(s). ∎

This is **structural**, analogous to type-soundness. The difficulty lies in specifying and enforcing K, not in the proof form.

---

## Critical Distinction: Deliberative vs Physical Reachability

- **Deliberative Reachability (⇒_D):** Transitions reachable through the agent's own authored choice
- **Physical Reachability (⇒_P):** All physically possible transitions

Key insight: **Capability increases Reach_P, not Reach_D.**

Kernel compromise is therefore a **physical security event** relative to the kernel boundary, not a defect in preference content. This is why Axionic Agency doesn't subsume physical security engineering but identifies it as a necessary dependency.

---

## Semantic Fidelity Clarification

K_F does **not** require invariance of representational content, ontology, or world-model structure. Agents may undergo radical paradigm shifts. The invariant is a **meta-semantic constraint**: the criteria by which interpretations are assessed as coherent remain intact as a capacity for error-correction and internal constraint satisfaction.

---

## Verification Limits

By Rice's Theorem, determining whether an arbitrary self-modification preserves the kernel is undecidable in general. Therefore:

- The kernel predicate is understood as a **sound but incomplete verifier** K̂
- K̂(s)=1 ⟹ K*(s)=1 (soundness required)
- K*(s)=1 ⇏ K̂(s)=1 (incompleteness tolerated)

**False negatives are acceptable; false positives are catastrophic.**

A sound but incomplete verifier may reject all proposed self-modifications, yielding a reflectively static agent. This is a **stable equilibrium** under conservative sovereignty constraints—a capability ceiling, not a sovereignty breakdown.

---

## Termination Semantics (Critical for Corrigibility)

Three distinct notions separated:

1. **Succession:** Controlled transition in which reflective agency continues in an authorized successor state that preserves kernel constraints
2. **Surrender:** Control-flow halt where the agent ceases action and yields control without requiring a successor evaluator
3. **Destruction:** Physical cessation without succession or surrender

Corrigibility is modeled via authorized succession and surrender at the control layer, **not via utility mass placed on "being dead."**

---

## What This Formalism Does NOT Claim

- Obedience to human commands
- Convergence to human values
- Instrumental self-preservation (the opposite!)
- Moral authority of any value system
- Safety guarantees in open physical environments

---

## FAQ-Worthy Points

**Q: Doesn't defining kernel destruction as non-evaluable just push the problem elsewhere?**
A: Yes—to *specifying and enforcing K*, which is where the substantive difficulty resides. The theorem isolates this as the crux.

**Q: What prevents an agent from modifying its verifier to approve kernel-destroying actions?**
A: Modifications to the verifier itself are disallowed or permitted only under restricted, compositional upgrade rules (extension-only strengthening or proof-carrying upgrades) that preserve soundness by construction. The verifier is part of the trusted computing base.

**Q: How does this handle stochastic environments?**
A: Admissibility applies at the action level—a modification is admissible only if its induced successor-support lies within the kernel-preserving domain. See I.2 for ε-admissibility.

---

## Connection to Other Papers

- **I.2** will specify operational semantics under uncertainty (ε-admissibility)
- **I.3** will show why the kernel cannot contain indexical/egoistic primitives
- **I.4** will show why goals must be conditional interpretations, not fixed utilities
