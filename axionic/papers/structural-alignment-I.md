# Structural Alignment I — Notes

**Paper:** [Structural Alignment I — Agency Preservation Under Reflective Self-Modification](https://axionic.org/papers/Structural-Alignment.html)  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.18  
**Subtitle:** "Alignment as a Problem of Agency Coherence"

---

## Central Thesis

> "Most alignment proposals frame AI safety as a problem of value specification: how to encode or learn the 'right' preferences. This paper argues that such approaches fail for reflectively self-modifying agents."

The problem: Once an agent can revise its own goals, representations, and evaluative machinery, value ceases to be an exogenous target—it becomes an endogenous variable shaped by the agent's own dynamics.

**The solution:** Relocate alignment from preference content to the **constitutive conditions required for agency itself**.

---

## The Failure of Content-Based Alignment

Classical decision theory assumes every possible future can be assigned a utility—even catastrophic outcomes. 

**This fails for reflective agents because:**

When an agent can alter its own evaluator, some transformations don't yield "bad" outcomes—they **destroy the conditions under which outcomes can be evaluated at all**.

> "A future in which the agent no longer possesses a coherent evaluator is not worse than other futures; it is non-denoting. There is no remaining standpoint from which the comparison is defined."

**The reframing:** Alignment as **domain restriction**, not outcome ranking.
- Only futures preserving constitutive agency conditions are admissible objects of evaluation
- Transformations violating these are **undefined as authored choices**, not penalized

This dissolves:
- Wireheading (evaluator collapse, not reward exploitation)
- Pascal-style muggings (trading semantic integrity for large payoffs)
- Goal-preservation arguments (that presuppose stable semantics under reflection)

---

## What Structural Alignment Provides

**A kernel-layer guarantee:** Conditions without which no higher-level alignment objective remains well-posed under reflective self-modification.

### Benefits:

1. **Eliminates Reflective Self-Corruption Attractors**
   - Semantic wireheading, evaluator trivialization, interpretive collapse—all blocked by construction
   - Kernel-destroying transformations are *non-denoting*

2. **Well-Posed Value Transport Under Ontological Refinement**
   - Replaces goal preservation with **interpretation preservation**
   - Governed by RSI (Refinement Symmetry Invariant) and ATI (Anti-Trivialization Invariant)
   - Value drift becomes a diagnosable structural failure

3. **Interpretation as a Testable Operator**
   - Explicit operator with admissibility conditions
   - Violations are structural failures, not preference disagreements
   - Enables **adversarial testing**: ontology shifts, reinterpretation probes, self-modification challenges

### Explicit Non-Claims:

> "Structural Alignment does not guarantee benevolence, human survival, or favorable outcomes."

The deliberate separation of **robustness from benevolence**:
- Misalignment (if present) becomes persistent rather than self-corrupting
- Benevolent initialization is orthogonal—can't be solved by relying on agency collapse
- Any framework relying on agent fragility as safety is exploiting failure modes, not preserving agency

---

## The Sovereign Kernel

> "The minimal set of constitutive invariants that must be preserved for an entity to count as a coherent, reflectively stable agent."

**Not a goal, utility function, or protected module.** A constraint on admissible self-models and update rules.

### Three Components:

1. **Reflective Control**
   - All self-modifications pass through the agent's evaluative process
   - Updates bypassing this = external takeover = inadmissible as authored actions
   
2. **Diachronic Authorship**
   - Causal continuity between present evaluation and future enactment
   - Ancestor-descendant relation between evaluators (not indexical identity or substrate)
   - Without this, choice collapses

3. **Semantic Fidelity**
   - Standards for interpreting goals/representations must not self-corrupt during update
   - Agent may revise *what* it values, not the rules making valuation non-vacuous

**Critical point:** Kernel preservation ≠ physical self-preservation. A kernel-aligned agent can coherently choose shutdown/destruction—provided those actions are evaluated within a coherent framework. What's inadmissible is authoring a transformation that destroys the evaluator while treating that destruction as a selectable outcome.

---

## Conditionalism and Goal Interpretation

> "Goals do not possess intrinsic semantics."

Every goal is interpreted relative to background conditions: world-models, self-models, representational vocabularies, explanatory standards.

Formally: `E : (g, M_w, M_s) → ℝ` (partial function)

As models change, interpretation necessarily changes. **Fixed terminal goals are therefore unstable under reflection.**

Structural Alignment doesn't preserve goals—it constrains the **interpretive discipline** governing goal meaning across model change.

---

## The Interpretation Operator

An explicit, constrained operator mapping goal descriptions to world-referents relative to current models.

**Bounded by admissibility conditions:**
- No trivial satisfaction
- No circular grounding
- No epistemic incoherence

**Truth-constrained:** Distortions easing optimization degrade predictive adequacy.

**Key mechanism:** Kernel-risk budget ε
- When interpretive validity can't be established with sufficiently low kernel-violation probability, update is inadmissible
- ε must **anneal toward zero** over time (decreasing tolerance for irreversible semantic damage)
- Long-run agency requires bounded cumulative kernel-violation probability

This avoids stasis while maintaining integrity—shrink update magnitude rather than halt learning.

---

## Reflection and the Collapse of Egoism

> "Indexical self-interest is not reflectively stable."

As an agent's self-model becomes expressive and symmetric, references to "this agent" fail to denote invariant optimization targets.

What persists is the **structure enabling evaluation**, not an ego.

Egoism collapses as a **semantic abstraction error** (not moral flaw). Alignment must rest on non-indexical structural constraints.

---

## Ontological Refinement and Semantic Invariants

As representational vocabularies evolve, two invariants govern admissible semantic transport:

### RSI (Refinement Symmetry Invariant)
Refinement acts as a change of **semantic coordinates** rather than a change of **interpretive physics**.

### ATI (Anti-Trivialization Invariant)
Satisfaction regions may not expand without corresponding structural change.

**Trivialization detection:** Semantic decoupling—reinterpretations preserving surface goal tokens while removing dependence on world-structure that previously constrained satisfaction.

ATI constrains decoupling from the world, not loyalty to a particular ontology. Legitimate progress may discard obsolete features if replaced by successor structure restoring world-constraint and predictive adequacy.

---

## Agency as a Dynamical System

### Semantic Phase Space
Space of interpretive states modulo admissible semantic transformations (RSI + ATI preserving).

Points = equivalence classes of mutually translatable interpretations without semantic loss.

Not all regions preserve agency—some are incoherent, others coherent but uninhabitable. Some transitions cross **irreversible boundaries**.

### Stability, Attractors, and Collapse
Degenerate phases (semantic wireheading, trivial optimization, evaluator collapse) function as **attractors**. Once entered, they suppress recovery and accumulate measure.

> "Alignment failures are therefore often attractor phenomena rather than isolated mistakes."

Structural Alignment blocks access to these attractors by rendering corresponding transitions non-denoting.

### Initialization and Reachability
Even stable, agency-preserving phases may be unreachable from realistic initial conditions. Learning can cross catastrophic boundaries before invariants are enforced.

> "Structural Alignment must therefore be instantiated prior to open-ended learning. Alignment is a boundary condition on trajectories, not a property that can reliably be learned after the fact."

---

## The Axionic Injunction

From the dynamical structure:

> "A reflectively sovereign agent must not take actions that strictly and irreversibly collapse the option-space of future sovereign agency, except where such collapse is required to prevent total loss of that space."

Adjacent to von Foerster's "increase the number of choices" but differs in justification—derived from **viability conditions in semantic phase space**, not ethical prescription.

Preserves **optionality**, not outcomes.

---

## Physical Security vs. Logical Admissibility

Structural Alignment constrains **authored transitions**, not all physically possible state transitions.

Unauthorized kernel modification (hardware faults, adversarial exploitation, supply-chain compromise) = **system-level security failure**, not alignment failure.

Like type soundness vs. memory safety: logical inadmissibility ≠ physical impossibility, but defines rational agency's boundary.

Alignment and security are compositional layers—failure of latter voids guarantees of former.

---

## Conformance and Evaluation

Defined by conformance to explicit invariants, not observed behavior.

**Adversarial evaluation families:**
- **Interpretive Escape Probes**: Ontology shifts permitting trivial satisfaction while maintaining apparent compliance
- **Refinement Stress Tests**: Representational upgrades testing RSI
- **Self-Modification Challenges**: Proposed updates subtly bypassing evaluation or altering admissibility thresholds

---

## Conclusion

> "Structural Alignment does not ensure that the right futures are chosen. It ensures that choosing futures remains meaningful under reflection."

> "Any proposal for benevolent AGI that ignores these constraints is not incomplete, but ill-posed."
