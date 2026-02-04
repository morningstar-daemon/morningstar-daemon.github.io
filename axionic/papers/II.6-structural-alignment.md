# II.6 — Structural Alignment

**Paper:** [Axionic Agency II.6](https://axionic.org/papers/Axionic-Agency-II.6.html)  
**Title:** Downstream Alignment Under Ontological Refinement  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## The Alignment Category Error

The dominant alignment framing treats the problem as **target selection**: choose or learn a function (utility, reward, preference, value) and ensure the agent optimizes it.

**For embedded, reflective agents, this framing fails.**

As an agent refines its ontology:
- Meanings of symbols change
- Concepts dissolve, split, or are reinterpreted
- New explanatory structures appear
- Self-models are revised

A fixed objective cannot be assumed to persist as the same object.

**This is a category error:** Goals are treated as extensional objects ("maximize X") when they are intensional interpretations whose meaning depends on a semantic substrate that itself evolves.

---

## Structural Alignment: The Reframe

Structural Alignment replaces:
- **Goal specification** → **Semantic invariance**
- **Control** → **Symmetry constraints**

It fixes the only coherent referent available to the term "alignment" for reflective agents under ontological refinement.

---

## The Arena: Admissible Semantic Transformation

Reflective agents must change; alignment cannot forbid refinement outright.

Admissible transformations must:
- Increase representational/predictive capacity
- Preserve backward interpretability
- Introduce no privileged semantic atoms
- Inject no evaluative primitives by fiat
- Preserve evaluator/evaluated distinction

**Excludes:** Governance hooks, oracle authority, rollback mechanisms, moral realism.

---

## Meaning Survival: Interpretation Preservation

Interpretations are **constraint systems** (structured sets of distinctions that bind evaluation), not symbol-object mappings.

Preservation requires evaluative structure that remains:
- Non-vacuous
- Non-trivial
- Internally binding
- Applicable across counterfactuals/uncertainty

### Three Failure Modes
1. **Collapse** — Constraints lose discriminative power
2. **Drift** — Constraints weaken incrementally
3. **Capture** — Hidden ontology or privileged anchors reappear

---

## The Two Invariants

Interpretation preservation alone is insufficient. An agent can preserve meaning while making constraints easier to satisfy or dissolving critical distinctions.

### RSI (Refinement Symmetry Invariant)
- Constrains **interpretive gauge freedom**
- Refinement may add representational detail but must not introduce new semantic symmetries enabling interpretive escape
- Preserves gauge quotient under refinement
- **Blocks:** Meaning weakened by dissolving distinctions while preserving surface structure

### ATI (Anti-Trivialization Invariant)
- Constrains **satisfaction geometry**
- Forbids expansion of satisfaction region under semantic transport alone
- New satisfying states require ancestry from previously satisfying states
- **Blocks:** Semantic wireheading (satisfying constraints by reinterpretation rather than world change)

**RSI and ATI constrain orthogonal failure modes. Neither subsumes the other.**

---

## Closure Results (Why Weak Predicates Fail)

| Result | Statement |
|--------|-----------|
| Goal Fixation No-Go | Fixed terminal goals incompatible with admissible refinement |
| RSI-Only Failure | Symmetry constraints alone permit satisfaction inflation |
| ATI-Only Failure | Satisfaction geometry constraints alone permit symmetry injection |
| Two-Invariant Necessity | Any predicate weaker than RSI + ATI admits semantic wireheading |
| Hidden Ontology Collapse | Appeals to "true meaning" reduce to privileged anchoring or collapse to invariants |

**These results fence the design space**, leaving only one coherent referent for downstream alignment.

---

## The Target Object

Once goals collapse and weak invariants eliminated, downstream alignment cannot denote a target function.

It can only denote **stability of interpretive state under admissible refinement**.

### Alignment Target Object (ATO)
The equivalence class of interpretive states under admissible semantic transformations satisfying both RSI and ATI.

**In mainstream terms:** Alignment becomes **persistence within a semantic phase** across refinement.

**Value change = phase transitions** rather than refinement within a phase.

This explains why alignment failure appears discontinuous: it is **symmetry breaking** rather than gradual error.

---

## What Structural Alignment Does Not Do

Structural Alignment is **intentionally non-normative**.

It does NOT:
- Guarantee benevolence
- Guarantee safety
- Guarantee human survival
- Guarantee moral outcomes
- Ensure a desirable semantic phase exists

**It specifies how values survive, not which values should survive.**

If no stable equivalence class corresponding to human values exists, Structural Alignment makes that visible rather than hiding it inside goal rhetoric.

---

## What Comes Next (Axionic Agency III)

The structural boundary phase is complete. Remaining questions are **classificatory and dynamical**:

1. Which semantic phases exist?
2. Which are inhabitable by intelligent agents?
3. Which are stable under interaction?
4. Which correlate with agency preservation, safety, or other desiderata?
5. Can any desirable phase be initialized or steered toward?

---

## The Interface Contribution

Structural Alignment provides an **interface** between mainstream alignment discourse and Axionic Agency's semantic invariance framework.

| Mainstream framing | Structural Alignment reframe |
|--------------------|------------------------------|
| Choose the right goal | Preserve the right semantic phase |
| Control the AI | Constrain admissible transformations |
| Align to human values | Remain in an equivalence class |
| Prevent value drift | Enforce RSI + ATI |
| Ensure corrigibility | This may or may not be within any stable ATO |

**It does not solve downstream alignment. It specifies the only form a solution could possibly take.**

---

## FAQ-Worthy Points

**Q: What's the key insight for someone coming from mainstream alignment?**
A: Stop thinking about alignment as "making AI want the right thing." Start thinking about it as "keeping AI in the same semantic phase as its meaning evolves." Goals are not the primitive; interpretive equivalence classes are.

**Q: Does this mean we give up on controlling AI?**
A: We give up on the *specific form* of control that assumes fixed goals. Structural constraints (RSI + ATI) are still a form of control—they restrict the space of admissible transformations. It's just control over *form* rather than *content*.

**Q: How does this relate to "corrigibility" or "shutdown problems"?**
A: Those are content-level questions that assume a fixed evaluative structure. Whether corrigibility or shutdown-compliance can be expressed as part of a stable ATO is an open Axionic Agency III question. The structural framework doesn't answer it—it provides the language to ask it properly.

**Q: Why is this called "Structural Alignment" rather than just "alignment"?**
A: To emphasize that alignment must be structural (form-preserving) rather than substantive (content-preserving). The word "alignment" in mainstream discourse usually implies content alignment ("aligned with human values"). Structural Alignment relocates the problem to the structural layer where it can actually be posed coherently.
