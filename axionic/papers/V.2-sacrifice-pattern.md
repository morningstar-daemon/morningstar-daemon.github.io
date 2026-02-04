# V.2 — Agency Conservation and the Sacrifice Pattern

## Paper Summary
Formalizes a recurrent failure mode in governance systems: systematic destruction of individual agency as instrumental means of achieving system-level objectives. Shows structural isomorphism between ancient ritual sacrifice and modern "collateral damage."

## Key Concepts

### Agency Operationalized
Agency = the set of future trajectories an agent can still steer toward from a given vantage state.

### Quantifying Agency Loss

**Hard Loss**: Futures that become unreachable
$$H_i(\pi_1 \rightarrow \pi_2) = P_i^{\pi_1}\left(\Omega_i \setminus \operatorname{supp}\left(P_i^{\pi_2}\right)\right)$$

**Soft Deformation**: Futures that remain reachable but become statistically implausible
$$K_i(\pi_1 \rightarrow \pi_2) = D_{\mathrm{KL}}\left(P_i^{\pi_1}(\cdot \mid s)\,\|\,P_i^{\pi_2}(\cdot \mid s)\right)$$

**Individual Agency Loss**:
$$\Delta A_i(\pi_1 \rightarrow \pi_2) = \alpha\,H_i(\pi_1 \rightarrow \pi_2) + \beta\,K_i(\pi_1 \rightarrow \pi_2)$$

### Standing Sensitivity
$$S_i = \left|\frac{\partial C}{\partial \Delta A_i}\right|$$

**Standing Asymmetry**: When expected sensitivity for victim-candidate class V is much less than for decision-bearing class D.

## The Sacrifice Pattern

### Definition (All must hold)
1. **Instrumentality**: ∃i ∈ V such that ∂G/∂ΔAᵢ > 0 (reducing agency improves goal)
2. **Non-consent**: Members of V lack effective exit or veto
3. **Standing Asymmetry**: Harm to V weakly affects institutional cost
4. **Epistemic Avoidability**: No documented agency-conserving exploration of lower-agency-loss alternatives proportional to stakes

> "Instrumentality, not intent, is the bright line."

### The Sacrifice Attractor
Under standing asymmetry and responsibility diffusion, policies concentrating harm on V while improving G are locally stable outcomes of institutional selection.

> "Sacrifice is an attractor."

## Structural Persistence Mechanisms

The pattern persists not by malice but by:
- **Standing Asymmetry**: Who counts
- **Responsibility Diffusion**: Who's accountable
- **Cosmological Abstraction**: Framing that obscures individual harm

### Gradient Suppression (Modern Theology)
Modern systems stabilize sacrificial regimes by suppressing moral gradients through:
- Aggregation
- Abstraction  
- Responsibility diffusion
- "Cosmology tokens" (greater good, progress, necessity)

$$\frac{\partial C}{\partial \Delta A_i} \downarrow \quad \text{while} \quad \Delta A_i \not\downarrow$$

> "This is functionally identical to theological sanctification in ancient sacrifice."

## Admissibility Conditions

A policy π is admissible only if:
1. **Targeting**: Directed at specific threat/constraint
2. **Minimality**: Least harmful option
3. **Non-instrumentality**: ∂G/∂ΔAᵢ ≈ 0 for non-coercive agents
4. **Responsibility Localization**: Clear accountability
5. **Robustness**: Admissibility invariant across reasonable α/β range

## Anti-Ethics-Washing Constraint

Exploration process E is admissible only if:
- Standing preservation
- Model diversity
- Gradient visibility
- Auditability

> "Simulated exploration that suppresses victim gradients constitutes a second-order sacrificial violation."

## Implications for Algorithmic Governance

> "Any governance system—human or artificial—that aggregates utility while hiding per-agent marginal agency loss is structurally sacrificial."

Safe governance must expose ∂C/∂ΔAᵢ as a first-class metric for all i.

## Key Insight

> "Ritual sacrifice and modern collateral damage differ in presentation, not structure."

Prevention requires:
- Restoring standing
- Enforcing exit and veto
- Localizing responsibility
- Auditing exploration
- Rejecting abstractions that override individual agency

## Connection to Axionic Framework

- Operationalizes "harm" from Axionic Injunction (III.5)
- Provides diagnostic criteria for detecting phase-destruction
- Extends non-consent analysis from ARC (IV.5)
