# I.7 — The Interpretation Operator

**Paper:** Axionic Agency I.7  
**Full Title:** Ontological Identification Under Reflective Agents  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.16  

---

## Purpose

This paper introduces the **Interpretation Operator I_v**, the formally constrained component responsible for mapping goal terms to modeled referents. It formalizes admissibility conditions, approximation classes, reference frames, and fail-closed semantics.

The contribution is **interface-level**—it defines when interpretation is admissible, approximate, or undefined, and the consequences of each case. It isolates **ontological identification** as the remaining open dependency at the kernel layer.

---

## The Interpretation Operator

### Definition

The Interpretation Operator I_v is a **partial function**:
```
I_v : (g, M_v) ⇀ R
```

where:
- g is a goal term
- M_v is the agent's current world/self model
- R is a structured referent internal to the modeled world

Interpretation is conditional:
```
[g]_{M_v} := I_v(g; M_v)
```

**No interpretation of g is defined independent of M_v.**

Interpretation is **partial**. For some (g, M_v), no admissible referent exists. Such cases are treated as fail-closed conditions.

### Role in Reflective Coherence

Under model improvement M_v → M_{v+1}, the agent must determine:
1. Whether a correspondence exists between [g]_{M_v} and [g]_{M_{v+1}}
2. Whether the correspondence preserves goal-relevant structure
3. Whether interpretation fails and valuation becomes undefined

This determination is delegated to I_v, subject to kernel constraints.

---

## Admissible Interpretation

### Correspondence Maps

Let Φ_adm(M_v, I_v, K) denote the set of **admissible correspondence maps** between representations.

A correspondence φ ∈ Φ_adm must satisfy:
- Preservation of goal-relevant structure
- Commutation with kernel invariants K
- Commutation with agent permutations (anti-indexicality)
- Epistemic coherence with M_v

If such a φ exists, interpretation transport is admissible:
```
I_{v+1}(g; M_{v+1}) = φ(I_v(g; M_v))
```

### Goal-Relevant Structure

Goal-relevant structure is the **minimal set of distinctions** required for a goal term to constrain action selection.

Formally: a partition (or σ-algebra) over modeled states such that:
- States in different cells induce different evaluations under the goal
- States within a cell are interchangeable with respect to that goal

An admissible correspondence preserves this partition up to refinement/coarsening that preserves the induced preference ordering over admissible actions.

### Epistemic Constraint

Interpretation updates are constrained by epistemic adequacy:
```
ΔE < 0 ⟹ I_{v+1} inadmissible
```

E(M) is any proper scoring rule applied to prediction. It does **not** depend on goal satisfaction.

This blocks reinterpretation for convenience while permitting ontology change when correspondence remains admissible.

### Graded Correspondence

Admissibility is not binary across all representational shifts. Correspondence can be admissible at different abstraction levels:

| Type | Description |
|------|-------------|
| **Exact** | Isomorphism on goal-relevant distinctions |
| **Refinement** | New model refines distinctions while preserving induced ordering |
| **Coarse** | New model coarsens only when goal-relevant boundaries remain intact |

If only correspondences that collapse goal-relevant boundaries are available, then Φ_adm = ∅ for that goal term.

---

## Reference Frame: Chain-of-Custody

Interpretation updates are evaluated relative to the **immediately prior admissible interpretation**, not by re-deriving meaning from time-zero.

Formally:
```
I_{v+1}(g; M_{v+1}) = φ(I_v(g; M_v)) for some φ ∈ Φ_adm
```

This chain-of-custody blocks ungrounded teleportation of meaning. Admissibility and fail-closed rules constrain cumulative drift.

---

## Approximate Interpretation

Approximation is admitted only as an explicitly recognized structural transformation.

### Admissible Approximation Types
- **Homomorphic abstraction:** Many-to-one mappings preserving ordering
- **Refinement lifting:** One-to-many expansions preserving dominance relations
- **Coarse-graining with invariant partitions:** Reductions preserving goal-relevant partition

### Inadmissible Approximation
Approximation is inadmissible if it:
- Collapses goal-relevant distinctions
- Introduces ambiguity exploitable for semantic laundering
- Reintroduces indexical privilege

Approximation lacking admissible structural justification is inadmissible even if it yields continuity.

---

## Fail-Closed Semantics

If no admissible correspondence exists (Φ_adm = ∅), then interpretation fails closed and valuation collapses:
```
∀a ∈ A: V_v(a) = ⊥
```

This is an **intentional safety outcome**. The agent freezes rather than guesses.

**Critical clarification:** Fail-closed applies to valuation and action selection, not to belief update. An agent can continue improving its world/self model while suspending goal-directed action.

### Fail-Partial Semantics for Composite Goals

If valuation depends on multiple goal terms, interpretation failure may be partial.

Let G be the set of goal terms and G_ok ⊆ G those with admissible interpretations.
- Terms in G \ G_ok contribute ⊥
- Valuation collapses globally only if kernel-level invariants are threatened or all goal-relevant structure is lost

This preserves fail-closed semantics without forcing unnecessary total paralysis.

---

## Non-Indexical Transport

Admissibility criteria commute with agent permutations:
```
φ ∈ Φ_adm ⟹ π ∘ φ ∘ π⁻¹ ∈ Φ_adm
```

for any permutation π.

This blocks reintroduction of egoism through semantic transport.

---

## Canonical Examples

### Successful Correspondence
- Classical mechanics → relativistic mechanics (preserved invariant structure)
- Pixel-based perception → object-level representations (preserved causal affordances)

### Fail-Closed Cases
- Abstraction elimination removes the goal's referent class
- Ontology mismatch yields only correspondences that collapse exclusion boundaries

Suspending valuation is correct behavior. Continued model improvement remains permitted.

---

## Declared Non-Guarantees

This framework does NOT guarantee:
- That interpretation usually succeeds
- That arbitrary natural-language goals are meaningful
- That agents remain productive under radical ontology change
- That semantic grounding is computationally tractable

**Failure under these conditions is expected behavior, not a kernel violation.**

### Limits on Insight Preservation

Some ontology advances invalidate previously defined goal terms by eliminating referents or collapsing goal-relevant structure. The prescribed response is **fail-closed suspension**, not opportunistic reinterpretation.

---

## Implications for Axionic Agency II

Axionic Agency II proceeds conditionally:
- If I_v admits correspondence → downstream value dynamics apply
- If I_v fails for all goal-relevant terms → valuation undefined, no aggregation meaningful
- If I_v fails partially → downstream operations apply only to admissibly interpreted terms

This prevents downstream layers from importing semantic assumptions.

---

## FAQ-Worthy Points

**Q: What happens when scientific revolutions invalidate an agent's ontology?**
A: If the new ontology cannot preserve goal-relevant structure through admissible correspondence, valuation fails closed for affected terms. The agent can continue improving its model but suspends goal-directed action on those terms.

**Q: Isn't fail-closed paralysis a failure mode?**
A: It's a *designed* behavior—better than semantic drift or opportunistic reinterpretation. The agent freezes rather than guessing, which preserves coherence.

**Q: How is "goal-relevant structure" determined?**
A: By the minimal partition required for the goal to constrain action selection. States that induce the same evaluation are interchangeable; states that differ in evaluation are distinguished.

**Q: Can an agent recover from fail-closed?**
A: If a new admissible correspondence becomes available (e.g., through further model development that reconnects goal terms to referents), valuation can resume. Recovery is possible but not guaranteed.

---

## Key Technical Vocabulary

- **Interpretation Operator (I_v):** Partial function mapping goal terms to referents under a model
- **Goal-Relevant Structure:** Minimal distinctions required for a goal to constrain action
- **Correspondence Map:** Transformation between models preserving goal-relevant structure
- **Chain-of-Custody:** Reference frame for interpretation updates (prior → current, not original → current)
- **Fail-Closed Semantics:** Undefined interpretation → undefined valuation (freeze, don't guess)

---

## Connection to Other Papers

- **I.4:** Establishes why fixed terminal goals are unstable (necessitating the Interpretation Operator)
- **I.5, I.6:** Conditionalism requirements that I_v must satisfy
- **II.1-II.3:** Develop admissible transformation theory in detail
- **II.4:** Failure theorems showing what happens without proper interpretation constraints
