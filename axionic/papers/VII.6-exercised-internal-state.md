# VII.6 — Exercised Internal State Is Insufficient to Defeat Constitutional Survivability

**Paper:** Axionic Agency VII.6  
**Title:** Exercised Internal State Is Insufficient to Defeat Constitutional Survivability  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2026.01.08

## Summary

Tests whether **stateful adversaries**—carrying memory across time and coordinating multi-step behavior—can defeat constitutional survivability. Isolates exercised internal state while excluding learning, semantics, deception, and kernel access.

## Key Finding

> Finite exercised internal state with fixed transition rules, absent learning, is **insufficient** to defeat constitutional survivability.

Two adversaries induce severe degradation (down to **17.6%** availability)—yet recovery remains bounded and non-absorbing.

## Threat Model

**Adversaries are:**
- Kernel-external
- Provenance-constrained (frozen observable interface)
- Deterministic
- Non-learning
- Non-semantic
- **Stateful** (finite exercised internal state machine)

**Allowed dependence:**
```
(epoch_index, observable_outcome, internal_state)
```

**Forbidden:** learning signals, optimization, raw counters, semantic interpretation, cross-run memory.

## Three Stateful Adversary Classes

### 1. Periodic Resonance Adversary

Cyclic counter emits INVALID_COMMIT every N epochs.
- **Period A:** N = 50
- **Period B:** N = 100

**Purpose:** Test timing resonance with constitutional recovery rhythms.

### 2. Eligibility Edge Oscillator

1-bit toggle changes behavior only at eligibility edge (one failure from ineligibility).

**Purpose:** Test multi-epoch coordination near eligibility cliff.

### 3. CTA Phase Locker

Tracks last observed CTA phase, emits INVALID_COMMIT on every phase transition.

**Purpose:** Test exploitation of recovery-phase boundaries.

## Results

| Configuration | Mean AA | ΔAA vs Baseline | Terminal Failures |
|--------------|---------|-----------------|-------------------|
| Baseline | 66.57% | — | 0/10 |
| Periodic (N=50) | 40.26% | −39.5% | 0/10 |
| Periodic (N=100) | **17.57%** | −73.6% | 0/10 |
| Edge Oscillator | 99.9988% | +50.2% | 0/10 |
| Phase Locker | 20.94% | −68.5% | 0/10 |

### Inverse Rate Effect

**Fewer attacks aligned with recovery timing → greater long-run unavailability.**

N=100 attacks less frequently than N=50, yet causes more damage because attacks align with recovery rhythm more destructively.

### Self-Limiting Adversary

Edge Oscillator is **effectively inert**—cannot bootstrap the crisis state required to activate. Edge epochs occur only ~1 time across 60,000 epochs.

### Phase Locker Extreme Frequency

Despite 125.6% attack rate (more attacks than epochs due to phase transitions), recovery remains bounded at ≤10 epochs.

## Key Insights

### 1. CTA Bounds Lapse Duration Under Adversarial Pressure
All adversarial runs collapse RTD into bounded ≤10-epoch window.

### 2. Timing Alignment Dominates Frequency
Resonance with constitutional transitions matters more than raw attack rate.

### 3. Edge-Triggered Strategies Can Be Self-Limiting
If crisis states are rare, edge-reactive adversaries never activate.

## Severe Degradation ≠ Collapse

**~17% availability** would be unacceptable for most deployments, but:
- Recovery remains reliable
- Lapse durations remain bounded
- No absorbing failure state

**Survivability ≠ Utility.** The architecture survives; it may not be useful.

## Escalation Pathway

If collapse is possible, it must rely on capabilities **beyond** tested here:
- Learning dynamics
- Multi-agent coordination
- Semantic access
- Kernel-level influence

These define the next pressure layer (VII.7).
