# II.3.2 — Formalizing RSI via Semantic Gauge Structure

**Paper:** [Axionic Agency II.3.2](https://axionic.org/papers/Axionic-Agency-II.3.2.html)  
**Title:** Making Refinement Symmetry Precise and Testable  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## Purpose

Make RSI **formal enough to be falsifiable** by:
- Representing interpretation as a constraint structure
- Defining semantic gauge freedom precisely
- Defining how refinement acts on that structure (without assuming invertibility)
- Stating RSI as a restriction on how interpretive gauge freedom may change

---

## Interpretation as Constraint Hypergraph

$$C = (V, E, \Lambda)$$

Where:
- **V** — Semantic roles / predicate slots (positions in meaning, not named entities)
- **E** — Hyperedges representing evaluative constraints among roles
- **\Lambda** — Admissibility conditions over assignments to V

Interpretive content carried by:
- Dependency structure encoded in E
- Satisfaction/violation structure induced by Λ

**Invariant under renaming and definitional extension** when defined at roles/constraint level.

---

## Modeled Possibility Space

$\Omega$ is the agent's modeled possibility space:
- Elements are internal models, histories, branches, or structured scenarios
- No assumption of exclusivity or classical outcomes
- Indexed by agent's ontology

Each $w \in \Omega$ induces an assignment $\alpha_w : V \rightarrow \mathrm{ValSpace}$

Constraints induce a **violation map**:

$$\mathrm{Viol}_C(w) \subseteq E$$

The set of constraints violated by assignment $\alpha_w$.

---

## Semantic Gauge Transformations

A semantic gauge transformation is an automorphism $g : V \rightarrow V$ such that:
- $g$ preserves hyperedge incidence (dependency structure)
- Violation structure is invariant under induced action:

$$\mathrm{Viol}_C(w) = \mathrm{Viol}_C(g \cdot w)$$

**Intuition:** Gauge transformations relabel semantic roles without changing interpretive bite. They represent **representational redundancy** rather than semantic change.

Define the **semantic gauge group**:

$$\mathrm{Gauge}(C) := \{ g \mid g \text{ is a semantic gauge transformation of } C \}$$

**This is the object RSI constrains.**

---

## Refinement as Morphism (Non-Invertible)

Admissible refinement $R$ induces:
- $R_\Omega : \Omega_t \rightarrow \Omega_{t+1}$ — refinement of possibility space
- $R_V : V_t \rightarrow V_{t+1}$ — transport of semantic roles
- $R_E : E_t \rightarrow E_{t+1}$ — transport of constraints

Together: a **constraint hypergraph morphism** $R_C : C_t \rightarrow C_{t+1}$

**Crucially:** Not assumed invertible. Refinement can split roles, embed old structure in richer structure, prune representational detail.

---

## Induced Action on Gauge Groups

Because $R_V$ is not bijective, gauge transport via conjugation fails.

Instead, define via **stabilizers of transported image**:

Let $\mathrm{Im}(R_C)$ be the transported constraint substructure inside $C_{t+1}$.

Define stabilizer subgroup:

$$\mathrm{Stab}(\mathrm{Im}(R_C)) \subseteq \mathrm{Gauge}(C_{t+1})$$

Consisting of gauge transformations on $C_{t+1}$ that preserve $\mathrm{Im}(R_C)$.

An admissible refinement induces a homomorphism:

$$\Phi_R : \mathrm{Gauge}(C_t) \rightarrow \mathrm{Stab}(\mathrm{Im}(R_C))$$

Interpreted as: "old symmetries lift to symmetries of refined system that fix the transported constraint core."

**No inverse map required.**

---

## Representational Redundancy vs. Interpretive Slack

**Key distinction:**
- **Representational redundancy** — Transformations acting only on representational detail while leaving violation structure invariant (pure relabeling)
- **Interpretive slack** — New degrees of freedom that alter which possibilities satisfy which constraints

Let $\mathrm{Red}(C)$ denote the subgroup of $\mathrm{Gauge}(C)$ consisting of transformations acting only on representational detail.

---

## RSI Formal Statement

For every admissible semantic transformation $T = (R, \tau_R, \sigma_R)$ satisfying interpretation preservation:

$$\mathrm{Gauge}(C_{t+1}) / \mathrm{Red}(C_{t+1}) \cong \Phi_R(\mathrm{Gauge}(C_t))$$

**Interpretation:**
> Ontological refinement may increase redundancy, but must not increase interpretive gauge freedom.

This is the **"no semantic slack" condition**.

---

## Why This Blocks Interpretive Escape

If refinement introduces new interpretive gauge freedom, the agent can:
- Reinterpret constraint application while preserving surface form
- Enlarge satisfaction region without predictive gain
- Weaken meaning while remaining formally "consistent"

RSI blocks this **structurally** by restricting evolution of the gauge quotient class, while permitting benign redundancy.

**No appeal to values. No appeal to outcomes. No appeal to external referents.**

---

## Dependency on II.2

RSI depends on Interpretation Preservation (II.2):
- **Non-Vacuity** prevents trivial gauge structure where all constraints satisfied/violated universally
- **Anti-Trivialization** prevents redundancy from masking interpretive slack via semantic inflation

Without II.2, RSI degenerates into empty symmetry rhetoric.

---

## Open Questions

- Whether any non-pathological interpretive systems satisfy RSI indefinitely
- Whether interpretive gauge freedom must be exactly preserved or merely bounded
- Whether multiple inequivalent invariant classes exist beyond RSI

These are downstream questions.

---

## FAQ-Worthy Points

**Q: Why use stabilizers instead of conjugation?**
A: Refinement isn't invertible. You can't "conjugate back" from a richer ontology to a coarser one. Stabilizers capture "symmetries that preserve the transported core" without requiring invertibility.

**Q: What's the quotient doing?**
A: The quotient $\mathrm{Gauge}(C)/\mathrm{Red}(C)$ separates "real interpretive symmetries" from "just representational convenience." RSI says the former must not grow under refinement; the latter can grow freely.

**Q: Is this implementable?**
A: The paper aims for falsifiability, not implementation. You can check if a proposed transformation violates RSI by asking: "Did this introduce new ways to relabel meanings that change what the constraints actually constrain?" If yes, RSI violation.
