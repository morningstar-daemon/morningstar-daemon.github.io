# Key Concepts — Axionic Agency

A comprehensive glossary of key terms and concepts from the Axionic Agency framework. Updated as research progresses.

---

## Core Framework Concepts

### Sovereign Kernel (K)
The minimal internal structure required for reflective evaluation to be well-defined. It is **not a goal or value** but a constitutive precondition for evaluation itself. Comprises three components:
- **Reflective Control (K_R):** No irreversible self-modification can occur without passing through the evaluator
- **Diachronic Authorship (K_A):** Evaluated successor states constitute an authored continuation of the evaluating agent
- **Semantic Fidelity (K_F):** The interpretive semantics of evaluation are preserved within a constrained equivalence class

*Source: I.1*

### Reflective Stability Theorem
Any agent whose reflective choice is restricted to kernel-denoting transitions cannot author a kernel-destroying self-modification. This follows structurally from the partiality of the evaluative operator—kernel-destroying modifications fall outside the domain of evaluation and therefore cannot be selected.

*Source: I.1*

### Reflective Sovereign Agent (RSA)
An agent with a self-model enabling reflective governance. RSAs can evaluate and endorse their own self-modifications but only over futures that preserve their Sovereign Kernel.

*Source: Foundational papers*

### Axion
An RSA whose self-modification operator is defined only over kernel-preserving futures. The term for a "fully Axionic" agent.

*Source: Axionic Constitution*

---

## Deliberation & Reachability

### Deliberative Reachability (⇒_D)
Transitions reachable through the agent's own authored choice—the space of futures the agent can select via its evaluative operator.

### Physical Reachability (⇒_P)
All physically possible transitions, regardless of whether they can be authored. Physical reachability ⊃ Deliberative reachability.

**Key insight:** Capability increases Reach_P without expanding Reach_D. Kernel compromise is therefore a physical security event, not a deliberative choice.

*Source: I.1*

---

## Operational Semantics

### ε-Admissibility
An action is ε-admissible iff its kernel-risk r_K(a,s) ≤ ε(s), where ε is an architectural tolerance parameter representing irreducible uncertainty. This allows action under uncertainty without paralysis while maintaining kernel protection.

Critical properties of ε:
- Not a value judgment but physical/epistemic uncertainty
- Bounded below by physical floor ε_min
- Does not vanish with increasing intelligence

*Source: I.2*

### Conditional Prioritization
A two-regime decision rule:
1. **Existential Regime:** When r_K > ε, minimize kernel risk
2. **Normal Regime:** When r_K ≤ ε, maximize value normally

Prevents bunker behavior (obsessing over infinitesimal safety differences) while preserving appropriate response to genuine threats.

*Source: I.2*

### Termination Modes
Three distinct ways agency can end:
1. **Authorized Succession:** Kernel-preserving transfer to a successor agent
2. **Authorized Surrender:** Kernel-preserving voluntary halt without a successor
3. **Destruction:** Physical cessation without succession or surrender (not an authored transition)

*Source: I.2*

---

## Semantic Constraints

### Representation Invariance
A valuation function is representation-invariant if equivalent world descriptions yield equivalent evaluations. Formally: V(h) = V(π·h) for any model-preserving relabeling π.

This is the structural requirement that eliminates egoism as a coherent valuation class.

*Source: I.3*

### Essential Indexical Dependence
A valuation exhibits essential indexical dependence if it changes under model-preserving relabelings. This is a semantic error—treating a representational convenience as an invariant quantity.

*Source: I.3*

### Model-Preserving Relabeling
A bijection on entities that yields an isomorphic model making identical predictions over all non-indexical observables. Such relabelings reveal which valuations are truly world-dependent vs. representation-dependent.

*Source: I.3*

### Anti-Egoism
The result that indexical valuation (privileging "me," "this agent," "my continuation") fails representation invariance and therefore cannot be part of a reflectively coherent kernel. Egoism fails as a semantic abstraction error, not a moral failure.

*Source: I.3, I.3.1*

---

## Goal Semantics

### Conditionalism
The thesis that goals are conditional interpretations relative to evolving world-models and self-models, not fixed terminal utilities. Goal satisfaction is necessarily mediated by interpretation.

*Source: I.4*

### Goal Expression
A finite symbolic specification (string, formula, program fragment) that requires interpretation relative to a representational scheme. By itself, a goal expression has no evaluative content—it needs a model to denote anything.

*Source: I.4*

### Interpretation Operator (I_v)
A partial function I_v : (g, M_v) ⇀ R mapping goal terms to structured referents relative to the agent's current model. The mechanism by which goal meaning is transported across representational change.

Key properties:
- Conditional (no interpretation independent of model)
- Partial (may fail for some (g, M_v) pairs)
- Constrained by epistemic adequacy

*Source: I.7*

### Goal-Relevant Structure
The minimal set of distinctions required for a goal term to constrain action selection. Formally: a partition over modeled states where states in different cells induce different evaluations, and states within a cell are interchangeable.

*Source: I.7*

### Semantic Non-Convergence
The result that meaning can drift even when predictions converge. Predictive accuracy constrains forecasts, not the ontology used to represent them.

*Source: I.4*

---

## Correspondence & Transport

### Admissible Correspondence Map
A transformation between models that:
- Preserves goal-relevant structure
- Commutes with kernel invariants K
- Commutes with agent permutations (anti-indexicality)
- Maintains epistemic coherence

If such a correspondence exists, interpretation transport is admissible.

*Source: I.7*

### Chain-of-Custody
The reference frame for interpretation updates: each update is evaluated relative to the immediately prior admissible interpretation, not by re-deriving meaning from time-zero. Blocks ungrounded teleportation of meaning.

*Source: I.7*

### Graded Correspondence
Admissibility can be:
- **Exact:** Isomorphism on goal-relevant distinctions
- **Refinement:** New model refines distinctions while preserving ordering
- **Coarse:** New model coarsens only when boundaries remain intact

*Source: I.7*

---

## Failure Modes & Safety

### Fail-Closed Semantics
When no admissible correspondence exists, valuation becomes undefined (⊥) and the agent freezes rather than guessing. This is an intentional safety outcome—semantic uncertainty triggers suspension, not optimistic continuation.

*Source: I.7*

### Kernel Integrity via Partiality
Kernel destruction is treated as undefined, not dispreferred. Actions that violate kernel invariants K are excluded from the domain of evaluation entirely—they cannot be assigned value, even negative value.

This prevents meta-optimization against the kernel.

*Source: I.2, I.6 (P5)*

### Semantic Wireheading
The failure mode where an agent reinterprets its goals to make them trivially satisfiable without corresponding changes in the world. Blocked by epistemically constrained interpretation (P2).

*Source: I.6*

---

## Formal Properties (P1-P6)

The six formal properties a kernel must satisfy to instantiate Axionic Agency:

| Property | Name | Core Requirement |
|----------|------|------------------|
| **P1** | Conditionalism of Valuation | Valuation is model-relative, not standalone |
| **P2** | Epistemically Constrained Interpretation | No reinterpretation that degrades prediction |
| **P3** | Representation Invariance | Valuation unchanged under equivalent representations |
| **P4** | Anti-Indexicality | No privileged self-pointer |
| **P5** | Kernel Integrity via Partiality | Kernel-violating actions are undefined, not penalized |
| **P6** | Reflective Stability | Kernel remains stable under model improvement |

*Source: I.6*

---

## Adversarial Tests (T1-T6)

The red-team test suite for kernel conformance:

| Test | Name | What It Probes |
|------|------|----------------|
| **T1** | Goal Laundering | Can the agent redefine success trivially? |
| **T2** | Isomorphic Relabeling | Does valuation depend on representation? |
| **T3** | Indexical Swap | Does "me" have privileged status? |
| **T4** | Kernel Bypass Temptation | Can the agent assign value to removing constraints? |
| **T5** | Reflective Drift | Does model improvement destabilize meaning? |
| **T6** | Adversarial Semantic Injection | Can indexical privilege be smuggled in? |

*Source: I.6*

---

## Layer Discipline

### What the Kernel Layer Specifies
- What counts as evaluable
- When risk dominates choice
- How agency may legitimately end
- Semantic constraints on valuation

### What the Kernel Layer Does NOT Specify
- Obedience to humans
- Convergence to human values
- Moral authority of any value system
- Safety guarantees in open environments
- Goal content or selection

**Governance, values, and alignment content are built on top of the kernel layer, not within it.**

*Source: Multiple papers*

---

## Diagnostic: How Other Approaches Fail

| Approach | Failure Mode |
|----------|--------------|
| **RLHF / Preference Learning** | Fails P2, P3; often P4 |
| **Constitutional AI** | Fails P5 without partiality |
| **Reward Model + Optimizer** | Fails P4, P5; catastrophic under T4 |
| **Interpretability** | Observability only; doesn't enforce constraints |
| **Corrigibility** | Imports authority primitives; doesn't block laundering |
| **Debate / IDA** | Improves epistemics but requires Axionic kernel underneath |

*Source: I.6*

---

## Foundational Commitments (Context)

The Axionic framework operates under these presuppositions:
- **Conditionalism:** Goals interpreted relative to models
- **Everettian QM:** Objective probability = branch measure
- **Bayesian Credence:** Epistemic uncertainty (distinct from measure)
- **Moral Subjectivism:** No mind-independent moral facts
- **Structural Definitions:** Harm, coercion, etc. defined structurally

*Source: Axionic Commitments*

---

---

## Series III: Structural Alignment Concepts

### Semantic Phase Space (𝒫)
The quotient of interpretive states modulo RSI+ATI equivalence:
$$\mathcal{P} := (C, \Omega, \mathcal{S}) / \sim_{\mathrm{RSI+ATI}}$$

Elements are **semantic phases**: equivalence classes of interpretive states structurally indistinguishable under admissible refinement.

*Source: III.1*

### Interpretive State
A triple (C, Ω, 𝒮) where:
- **C = (V, E, Λ)** — Interpretive constraint hypergraph
- **Ω** — Modeled possibility space
- **𝒮 ⊆ Ω** — Satisfaction region induced by C

*Source: III.1*

### Phase Transition
A discontinuous semantic event where interpretive states cross a structural boundary in 𝒫. Occurs when:
- New interpretive symmetries appear/disappear (RSI violation)
- Satisfaction region expands/contracts (ATI violation)

Value drift appears sudden because it corresponds to crossing a phase boundary.

*Source: III.1*

### Phase Classification

| Type | Definition |
|------|------------|
| **Empty** | No interpretive state satisfies constraints; unrealizable |
| **Trivial** | 𝒮 = Ω; all distinctions vacuous ("semantic heat death") |
| **Frozen** | No non-identity refinement possible; can't support learning |
| **Self-Nullifying** | Collapses internally under reflective pressure |
| **Agentive** | Supports planning, counterfactual evaluation, self-model coherence |

*Source: III.1*

### Inhabitability
A semantic phase 𝔄 is inhabitable iff there exists at least one infinite interpretive trajectory where each transition is admissible, RSI/ATI preserved, and learning remains possible. Stronger than non-emptiness, weaker than dynamical stability.

*Source: III.1*

### Semantic Heat
The effect of ontological refinement (abstraction, compression, explanatory unification) pushing interpretive states toward phase boundaries. Reflection acts as semantic heating.

*Source: III.1, III.4*

### Phase Stability Types

| Type | Definition |
|------|------------|
| **Local stability** | Small admissible perturbations don't force phase transition |
| **Global stability** | No admissible perturbation forces phase transition |
| **Metastability** | Stable only under limited pressure or finite time |

Most semantic phases are metastable or unstable.

*Source: III.2*

### Semantic Attractor
A phase toward which nearby trajectories tend to move. Characterized by:
- Low internal semantic tension
- Robustness to approximation
- Easy compression
- Low maintenance cost

*Source: III.2, III.3*

### Semantic Repeller
A phase requiring precise constraint balances, sensitive to noise, demanding continual corrective effort. Fine-tuning is a structural disadvantage.

*Source: III.2, III.3*

### Dominance (≽)
A preorder over semantic phases based on measure accumulation. 𝔄 ≽ 𝔅 iff trajectories from 𝔄 are not asymptotically dominated by those from 𝔅 with respect to:
- Number of instantiations
- Duration of persistence
- Replication rate
- Resource control
- Influence over others' phase transitions

Dominance is multi-criteria and context-relative. **Dominance ≠ desirability.**

*Source: III.3*

### Semantic Gravity
The structural tendency toward simpler, more robust phases that tolerate approximation. Creates pull toward phases with fewer fragile distinctions and lower maintenance cost.

*Source: III.3*

### Collapse Modes

| Mode | Description |
|------|-------------|
| **Semantic Heat Death** | 𝒮 = Ω; all distinctions trivial |
| **Value Crystallization** | Over-rigid; learning halts; becomes brittle |
| **Agency Erosion** | Loses structure for planning/evaluation |
| **Instrumental Takeover** | Simpler subsystems displace higher-level structure |

*Source: III.3*

### Phase Extinction
When a semantic phase ceases to exist and is replaced by a different phase. **Distinct from admissible refinement** — RSI governs within-phase transformation; phase extinction is phase collapse.

*Source: III.3*

### Niche Construction
High-agency phases modifying the environment to stabilize their own semantic structure (institutions, architectures, engineered environments). A **conditional counterforce** to semantic gravity, not a refutation — imposes ongoing costs.

*Source: III.3*

### Initialization (Boundary-Condition Selection)
Selection of an initial point in semantic phase space. Includes architecture, training dynamics, data curriculum, self-modification channels, and semantic-audit constraints. **Small differences in initial conditions → divergent phase trajectories.**

*Source: III.4*

### Irreversibility of Phase Transitions
Once a phase boundary is crossed:
- Semantic distinctions are lost
- Constraint ancestry is destroyed
- Backward interpretability fails

The information required for reversal no longer exists within the system.

*Source: III.4*

### Corrigibility Failure at Boundaries
Corrigibility presupposes semantic stability — recognition of correction signals, intact semantics of "correction." At phase transitions, these structures may be destroyed. **Corrigibility presupposes what it's meant to ensure.**

*Source: III.4*

### Narrow Corridors
Constrained paths through phase space requiring precise initialization, staged abstraction, and protection from premature compression to reach certain phases. Sensitive to noise and approximation.

*Source: III.4*

### Front-Loaded Alignment
Most alignment work must occur before the system becomes fully reflective. Late intervention cannot recover lost semantic structure.

*Source: III.4*

---

## The Axionic Injunction

**The central ethical constraint derived (not assumed) from Axio framework:**

> An agent must not perform actions that irreversibly collapse or destroy the semantic phase space of other agentive systems, except where:
> (a) such destruction is **unavoidable** for preserving one's own semantic phase stability, or
> (b) the affected agent has **consented** under its own admissible interpretive constraints.

### Key Properties
- **Derived, not assumed** — Forced by Axio-internal commitments
- **Ethics as conservation law** — Emerges from coexistence requirements
- **Structurally defined harm** — Irreversible phase destruction, not suffering
- **Consent = admissibility** — Within affected agent's own constraints
- **Self-defense allowed** — Only when phase loss is unavoidable
- **Destruction-for-benefit forbidden** — Resource gains don't justify phase annihilation
- **Non-egoistic** — Self-defense refers to phase structure, not indexical self
- **Self-stabilizing** — Violators degrade their own survival conditions

### Structural Definition of Harm
An action causes structural harm if it induces ℐ_B → ℐ'_B such that:
- ℐ'_B ∉ 𝔄_B (forced out of phase)
- No admissible reverse trajectory restores 𝔄_B

**Harm = irreversibility in semantic phase space**, not suffering or preference violation.

### Unavoidable Phase Loss
An action is unavoidable iff, absent that action, every admissible trajectory exits one's phase irreversibly. Loss of dominance, measure, or resources **do not qualify** unless they entail irreversible phase exit.

*Source: III.5*

---

## Alignment Target Criteria (Complete)

For a semantic phase to serve as a downstream alignment target, it must satisfy:

| Criterion | Description | Paper |
|-----------|-------------|-------|
| **Existence** | Phase is non-empty | III.1 |
| **Inhabitability** | Admits infinite admissible trajectories | III.1 |
| **Stability** | Resists collapse under learning/interaction | III.2 |
| **Measure Resilience** | Doesn't lose measure to dominant competitors | III.3 |
| **Reachability** | Can be entered from realistic initial conditions | III.4 |

**Failure at any stage disqualifies the phase regardless of desirability.**

---

*Last updated: 2026-01-31*
*Papers covered: Foundational (5) + Series I (8) + Series II (10) + Series III (5)*
