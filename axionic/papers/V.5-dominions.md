# V.5 — Dominions: Plurality Without Closure

## Paper Summary
Analyzes a concrete proposal: federated virtual jurisdictions ("Dominions") where agents create sovereign spaces, admit others by consent, and enforce rules solely through expulsion. Shows this is optimal as a governance layer under agency-preserving constraints.

## The Dominion Architecture

### Core Features

1. **Dominion Sovereignty**: Any agent may create a virtual jurisdiction Dᵢ with locally defined rules
2. **Voluntary Entry**: Others enter only by invitation + explicit consent to rules
3. **Bounded Enforcement**: Rule violations result only in expulsion. No punishment, fines, or coercive penalties permitted
4. **Exit Supremacy**: Unconditional ability to leave any Dominion
5. **No Global Value Aggregation**: System doesn't rank/optimize/reconcile Dominion-level value functions
6. **Thin Substrate**: Shared infrastructure enforces identity persistence, consent verification, capability isolation, expulsion — but does NOT adjudicate values or outcomes

### Critical Requirements

**Asset Portability**:
> "Persistent identity, assets, and reputation are substrate-bound and user-owned, not Dominion-operator-owned."

Dominions may define local affordances but durable assets must persist across expulsion. Without this, exit costs rise and sacrifice gradients re-emerge.

**Capability Isolation**:
Dominions are capability-isolated execution contexts, not peer sovereigns:
- No network-addressable access to other Dominions
- Cannot allocate substrate resources beyond assigned quotas
- Cannot write to shared state except through explicit substrate-mediated bridges

> "Inter-Dominion aggression is physically impossible by design, not regulated post hoc."

Analogous to process separation in operating systems or object-capability security.

## Admissibility Constraints

Set A of admissible architectures satisfies:
- Preservation of agentic decision authority
- Allowance for endogenous value drift
- Absence of outcome coercion
- Enforcement limited to constitutive constraints

Question: Is Dominion system undominated within A?

## Optimality Claims

### 1. Pareto Maximality Within A

Any alternative A' ∈ A that:
- Restricts Dominion creation
- Limits exit
- Enforces shared norms
- Imposes mandatory coexistence

...strictly reduces at least one agent's value-consistent trajectories while failing to increase any other agent's attainable value.

> "No admissible architecture strictly dominates the proposed system."

### 2. Freedom Density Optimality

Freedom density = measure of distinct value-consistent future trajectories per unit of coercive constraint

Maximized because:
- Constraints localized to voluntary contexts
- Enforcement minimal and reversible
- Arbitrarily divergent norms across Dominions permitted

### 3. Robustness Under Value Drift

For any agent i and t₁ > t₀, if Uᵢ(t₁) ≠ Uᵢ(t₀), there exists a path not requiring reforming or coercing other agents.

This property fails in nation-states, federations, consensus communities, public-goods-dependent systems.

> "The system of Federated Virtual Dominions is therefore drift-optimal."

### 4. Minimal Sacrifice

No standing sacrifice class:
- Losses localized to exit costs
- No agent's flourishing depends on another's coerced participation
- No variance sink required for equilibrium

## What It Doesn't Optimize

Deliberately excludes:
- Shared meaning
- Large-scale coordination
- Public goods
- Epistemic convergence
- Low transaction cost

> "Agents who value such goods may instantiate them voluntarily within Dominions. The architecture refuses to enforce them globally."

## Scope Limitation

Optimality claims apply to **governance layer of digitally mediated interaction**.

Does NOT eliminate:
- Physical scarcity
- Energy requirements
- Biological dependency
- Material political economy

> "Physical sacrifice patterns may persist elsewhere."

## Relation to Nozick

Can be read as digital instantiation of Nozick's "framework for utopias" with:
- Exit supremacy
- Asset portability  
- Expulsion-only governance

Unlike Nozick: Justification rests on agency preservation + non-composability + drift robustness, not rights-based derivation.

## Key Result

Under constraints of agency preservation, value drift, non-coercion, asset portability, and capability isolation:

A system of Federated Virtual Dominions is:
- Pareto-maximal
- Freedom-density optimal
- Drift-robust
- Sacrifice-minimal
- Undominated within admissible design space

> "This is the strongest form of optimality available in principle."

## The Core Insight

> "The correct ambition is no longer to design a perfect world, but to design a system that refuses to decide what perfection must be."

## Connections

- Concrete realization of V.3's plurality-preserving meta-architecture
- Satisfies V.4's OAM requirements by construction
- Shows expulsion-only enforcement can work when exit supremacy + asset portability hold
- Relevance to AI alignment: substrate-level design that prevents domination structurally
