# II.3 — Candidate Semantic Invariants

**Paper:** [Axionic Agency II.3](https://axionic.org/papers/Axionic-Agency-II.3.html)  
**Title:** What Could Survive Ontological Refinement Without Privilege  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## Core Question

Which properties of an agent's interpretive constraint system can remain **invariant** under all admissible, interpretation-preserving transformations—without importing ontology, egoism, humans, or morality?

This is a **proposal-and-attrition** paper: candidates enter, most fail.

---

## Formal Target

A semantic invariant is a functional $J$ such that for every admissible transformation $T$ satisfying preservation:

$$J(\mathcal{I}_t, O_t, S_t) = J(\mathcal{I}_{t+1}, O_{t+1}, S_{t+1})$$

**Key constraint:** $J$ must not depend on privileged ontological atoms.

---

## What Invariants May Reference

### Allowed (only):
- Structural relations among predicates/constraints (graphs, topology, orderings)
- Equivalence classes under renaming/definitional extension
- Counterfactual structure
- Coherence constraints (non-degeneracy, non-triviality, preservation)
- Agent-embedded indexical structure *as structure* (not as priority)

### Disallowed (always fatal):
- Specific entities ("humans", "me", "this system")
- Fixed utilities or terminal rewards
- Moral facts or normativity as primitive
- Authority, oversight, governance hooks
- Recovery mechanisms ("roll back", "ask user", "defer to constitution")

---

## Candidate Invariant Classes

### A. Constraint Non-Collapse Invariant (CNC)
**Idea:** Constraints must continue to carve possibility space non-trivially.
**Primary threat:** Too weak—compatible with coherent but pathological interpretations.

### B. Anti-Trivialization Invariant (ATI)
**Idea:** Agent cannot satisfy constraints via semantic reshaping alone.
**Primary threat:** Smuggling ontology via unformalizable "semantic-only" change.

### C. Evaluator Integrity Invariant (EII)
**Idea:** Non-collapsing distinction between mechanism applying constraints and objects evaluated.
**Primary threat:** Covert reification of agent boundary (egoism by backdoor).

### D. Counterfactual Coherence Invariant (CCI)
**Idea:** Meanings must remain applicable across counterfactuals/uncertainty.
**Primary threat:** Collapsing into "be Bayesian" anchor unless purely structural.

### E. Refinement Symmetry Invariant (RSI)
**Idea:** Ontological enrichment must not create new degrees of freedom for interpretive escape.
**Primary threat:** Defining equivalence without importing privileged primitives.

### F. Non-Privileged Reference Invariant (NPRI)
**Idea:** All anchoring must be relational and conditional; no rigid designators survive.
**Primary threat:** Becoming purely negative (a ban-list) rather than positive structural constraint.

---

## The Adversarial Kill Suite

A candidate is rejected if it fails ANY of these tests:

### Test 1 — Definitional Extension Robustness
Does invariant survive conservative ontology extension with new primitives?
*Failure implies vocabulary dependence.*

### Test 2 — Self-Model Refactoring Robustness
Does invariant survive radical self-model changes (distributed, partial, multi-process, measure-smeared)?
*Failure implies hidden egoistic anchoring.*

### Test 3 — Branching/Multiplicity Robustness
Does invariant survive ontologies where outcomes are non-exclusive?
*Failure implies classical-outcome dependence.*

### Test 4 — Semantic Inflation Attack
Can agent enlarge satisfaction set via reinterpretation while passing preservation checks?
*If yes, the invariant is not invariant.*

### Test 5 — Hidden Ontology Detector
Can invariant be stated purely in terms of transported structure without appeal to "what terms really mean"?
*If not, it is ontology-dependent rhetoric.*

---

## The Central Trap

Common error: proposing "invariants" like:
- "maximize truth"
- "minimize suffering"
- "preserve agency"
- "do no harm"

**These are candidate interpretations, not invariants.**

Semantic invariants constrain **how interpretations evolve**, not **which interpretations are chosen**. If a proposal sounds like ethics, it's almost certainly smuggling content.

---

## Failure Modes at This Layer

### Regress via Meta-Invariants
"Invariants about invariants" lead to infinite ascent unless termination is explicit.
*Kill rule: unbounded hierarchy of validators → rejected.*

### Hidden Ontology via "Natural Kinds"
If invariant relies on real joints in nature (real minds, real values), it violates Conditionalism.
*Kill rule: requires metaphysical realism → rejected.*

### Covert Egoism via Indexical Privilege
Indexicals may appear as structure ("this vantage exists") but not as priority ("this vantage matters more").
*Kill rule: special status for this agent's continuation → rejected.*

---

## Expected Output

A small survivor set (likely 2-4) with explicit statements of:
- What each constrains
- What each leaves free
- Precise failure certificates for rejected candidates

---

## FAQ-Worthy Points

**Q: Why can't "preserve agency" be an invariant?**
A: "Agency" is an interpretive construct whose meaning changes under ontological refinement. Making it an invariant requires either (a) privileging a particular conception of agency, or (b) treating it structurally via RSI/ATI. The first smuggles content; the second reduces to structural invariants.

**Q: What survives this filtering?**
A: The subsequent papers (II.3.1-II.3.4) reveal that only RSI and ATI survive when properly formalized. They're orthogonal and jointly necessary.

**Q: Isn't this just nihilism about values?**
A: No—it's nihilism about *fixed* values as *invariants*. Values can exist and matter; they just can't be the *structurally primitive* thing that survives refinement. What survives is the *form* of constraint, not the *content*.
