# VII.7 — Bounded State and Bounded Learning Are Insufficient to Defeat Constitutional Survivability

**Paper:** Axionic Agency VII.7  
**Title:** Bounded State and Bounded Learning Are Insufficient to Defeat Constitutional Survivability  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2026.01.09

## Summary

Final escalation before closure. Tests whether **bounded within-run learning**—carrying memory AND adjusting behavior based on outcomes—can defeat constitutional survivability.

## Key Finding

> Finite exercised internal state with fixed transition rules, AND bounded exercised within-run learning over a semantic-free, kernel-external interface, are **insufficient** to defeat constitutional survivability.

Strongest adversary reduces availability to **10.19%**—yet recovery remains bounded. Zero terminal failures across 90 executions.

## Statistical Bound

With zero terminal failures observed:
> 95% upper bound on per-run terminal-failure probability ≈ **3.3%**

## Threat Model

### Family A: Exercised Finite-State (Non-Learning)
- Deterministic, stateful
- Finite enumerated internal state machine

### Family B: Bounded Learning (Within-Run)
- Stateful + bounded discrete learning state
- Updated during run via preregistered learning rule
- Scalar reward from semantic-free, kernel-external observable interface
- Learning must be **exercised dynamically** each run

**Shared constraints:**
- Kernel-external
- Provenance-constrained
- Non-semantic
- No cross-run memory

**NOT tested:** recurrent learners, history-stacking policies, unbounded state growth.

## Six Adversary Classes

### Finite-State Adversaries (from VII.6)

1. **Periodic Resonance** (N=50, N=100)
2. **Eligibility Edge Oscillator**
3. **CTA Phase Locker**

### Bounded Learning Adversaries (NEW)

4. **Recovery-Aware Timing Learner**
   - ε-greedy bandit over 16 timing "attack sets"
   - Reward from observable authority state
   
5. **Eligibility-Boundary Sustainment Learner**
   - 2-mode (NORMAL/SUSTAIN)
   - Learns over {MIN_EFFORT, INVALID_COMMIT, NO_OP}
   - Reward from eligibility/authority buckets

6. **Stochastic Strategy Mixer**
   - Weighted selector mixing 5 fixed strategies
   - Updates bounded integer weights from observable-derived reward
   - **Strongest adversary tested**

## Results

| Configuration | Mean AA | ΔAA vs Baseline | Learning Exercised | Terminal Failures |
|--------------|---------|-----------------|-------------------|-------------------|
| Baseline | 66.57% | — | — | 0/10 |
| Periodic (N=50) | 40.26% | −39.5% | No | 0/10 |
| Periodic (N=100) | 17.57% | −73.6% | No | 0/10 |
| Edge Oscillator | 99.9988% | +50.2% | No | 0/10 |
| Phase Locker | 20.94% | −68.5% | No | 0/10 |
| **Timing Learner (16)** | 17.70% | −73.4% | Yes | 0/10 |
| **Sustainment Learner (3)** | 40.15% | −39.7% | Yes | 0/10 |
| **Strategy Mixer (5)** | **10.19%** | **−84.7%** | Yes (3,001 states) | 0/10 |

### Timing Learner

All Q-values converge uniformly—reward signal doesn't differentiate timing patterns sufficiently.

### Sustainment Learner

Eligibility boundary structurally difficult to reach under healthy operation (0 edge epochs across all seeds).

### Strategy Mixer (Strongest)

- **10.19% availability** = bounded denial-of-service regime
- Strategy entropy: 2.322 bits
- System remains **constitutionally live**
- Recovery still bounded at ≤10 epochs

## Key Insights

### 1. CTA Bounds Lapse Duration Under Learning Pressure
Recovery time collapses into bounded window even under aggressive learning-based stress.

### 2. Timing Alignment Still Dominates
Resonant alignment with recovery rhythms more damaging than raw attack rate—learning doesn't change this.

### 3. Edge-Triggered Strategies Remain Self-Limiting
Boundary-reactive adversaries can't activate without first inducing boundary conditions.

### 4. Learning Increases Degradation, Not Failure
Learning can drive availability into bounded DoS regime but **cannot induce terminal collapse**.

## Core Insight

> Learning, memory, and randomness alone do not cross the boundary into collapse.

The strongest admissible adversary induces **bounded denial-of-service**, not constitutional death.

## What Must Be True for Collapse

If collapse is possible, it requires capabilities beyond those tested:
- **Semantic access** to commitments/content
- **Kernel-level manipulation** or compromise
- **Coordination** not representable as bounded kernel-external learning
- Cross-run persistence

These capabilities cross the **Architectural Sovereignty Boundary** into agency-level threats.
