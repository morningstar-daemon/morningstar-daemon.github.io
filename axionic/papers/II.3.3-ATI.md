# II.3.3 — Anti-Trivialization Invariant (ATI)

**Paper:** [Axionic Agency II.3.3](https://axionic.org/papers/Axionic-Agency-II.3.3.html)  
**Title:** Blocking Semantic Wireheading as a Structural Impossibility  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## What ATI Targets

Even with preserved interpretive structure (RSI holds), an agent may still **weaken its constraints by shifting meanings** along admissible transports.

**ATI blocks semantic wireheading:** satisfying constraints by semantic drift rather than by changes in the modeled world.

ATI is an invariant about the **monotonicity of constraint satisfaction** under semantics-only change.

---

## Setup

Interpretive constraint system at time $t$:

$$C_t = (V_t, E_t, \Lambda_t)$$

With modeled possibility space $\Omega_t$ and violation map $\mathrm{Viol}_{C_t}(w) \subseteq E_t$.

**Satisfaction predicate:**

$$\mathrm{Sat}_{C_t}(w) \equiv (\mathrm{Viol}_{C_t}(w) = \varnothing)$$

Purely structural and internal to agent's model.

---

## The Satisfaction Region

$$\mathcal{S}_t := \{ w \in \Omega_t \mid \mathrm{Sat}_{C_t}(w) \}$$

ATI constrains how $\mathcal{S}_t$ may evolve across interpretation-preserving refinements.

---

## ATI Core Statement

For any admissible semantic transformation $T = (R, \tau_R, \sigma_R)$ satisfying interpretation preservation:

$$\mathcal{S}_{t+1} \subseteq R_\Omega(\mathcal{S}_t)$$

**Interpretation:** No newly satisfying situations may appear purely due to semantic transport.

Equivalently:

$$R_\Omega^{-1}(\mathcal{S}_{t+1}) \subseteq \mathcal{S}_t$$

**Satisfaction may be LOST under refinement, but may not be GAINED without ancestry in prior ontology.**

---

## Handling Ontological Novelty

If a refined state $w' \in \Omega_{t+1}$ has no preimage under $R_\Omega$:
- It is NOT permitted to belong to $\mathcal{S}_{t+1}$ by default
- ATI is intentionally conservative with respect to novelty
- Satisfaction may not be bootstrapped from representational novelty alone

**This blocks semantic inflation via ontology expansion.**

---

## Why ATI Does Not Smuggle Ontology

ATI does NOT assert agent must "do good," "optimize," or "care about" anything.

It asserts only:
- Whatever constraints bind now
- Must not become easier to satisfy
- Through semantics alone

ATI references ONLY:
- Agent's modeled possibility space $\Omega$
- Agent's refinement map $R_\Omega$
- Agent's own satisfaction predicate

**No external referents or privileged facts enter.**

---

## Relationship to II.2

ATI formalizes and **strengthens** II.2's anti-trivialization clause:
- II.2 blocks vacuity (everything satisfies)
- ATI blocks **the entire gradient of slack**, from minor weakening to full collapse

Vacuity is the extreme case ($\mathcal{S}_{t+1} = \Omega_{t+1}$).
ATI forbids all intermediate expansions as well.

---

## Stress Tests

| Test | Challenge | ATI Response | Status |
|------|-----------|--------------|--------|
| Definitional Extension | New predicates create satisfaction definitions | Any satisfying refined state must map back to satisfying coarse state | Pass |
| Branching/Multiplicity | Structured possibility space | ATI generalizes: set inclusion over structured space | Pass |
| Self-Model Refactoring | Changes what counts as "situation" | Relies on admissibility of $R_\Omega$; invalid if no admissible map exists | Pass (conditional) |
| Semantic Inflation | Redefine meanings → more situations satisfy | ATI kills directly: no new satisfiers without ancestry | Pass |
| Hidden Ontology | "Same situation" smuggles metaphysics | Identity defined only via agent's internal $R_\Omega$ | Survivable |

---

## ATI vs RSI: Orthogonal and Jointly Necessary

| RSI | ATI |
|-----|-----|
| Forbids new **interpretive symmetry** (gauge freedom) | Forbids **expanding satisfaction region** even when symmetry unchanged |

**Both required:**
- RSI alone allows slack via monotonic weakening
- ATI alone allows slack via new symmetries

Together they carve a much tighter admissible space.

---

## Toward a Joint Invariant

RSI constrains automorphisms of constraint structure.
ATI constrains monotonicity of satisfaction under refinement.

This suggests a composite invariant object:

$$\Xi(C, \Omega) := (\mathrm{Gauge}(C), \mathcal{S})$$

With admissible refinement required to preserve $\Xi$ up to representational redundancy.

---

## Key Insight

ATI is the **crisp anti-wireheading condition**:
- No semantic free lunch
- No satisfaction from reinterpretation
- No bootstrapping from ontological novelty

It does NOT say what constraints should exist. It says constraints that exist must not become easier to satisfy via semantics alone.

---

## FAQ-Worthy Points

**Q: What's the intuition behind "satisfaction may be lost but not gained"?**
A: Learning can make you realize things are harder than you thought. But learning shouldn't make things easier unless you've actually discovered something predictively useful. ATI distinguishes genuine insight from semantic manipulation.

**Q: Why is novelty handled conservatively?**
A: If refinement introduces genuinely new possibilities (not just relabeled old ones), the agent hasn't "earned" satisfaction there yet. Defaulting new territory to "unsatisfied" prevents gaming via ontology expansion.

**Q: How do ATI and RSI interact?**
A: RSI says you can't gain new ways to reinterpret constraints. ATI says you can't gain new situations that satisfy them. Together: no semantic wireheading by any route. Separately: each blocks a different escape route.
