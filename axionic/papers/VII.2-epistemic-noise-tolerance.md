# VII.2 — Epistemic Noise Tolerance in Constitutional Governance

**Paper:** Axionic Agency VII.2  
**Title:** Epistemic Noise Tolerance in Constitutional Governance  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2026.01.05

## Summary

Tests whether epistemic unreliability is fatal to governance systems. Studies a constitutional architecture where semantic evaluation affects authority only through eligibility constraints—not through optimization, rewards, or adaptive control.

## Key Finding

> Independent, unstructured epistemic unreliability is **insufficient** to induce catastrophic governance failure.

Robustness is dominated by **semantic headroom** (baseline success probability), not noise magnitude—even at corruption rates exceeding 50%.

## Architecture Design

### Separation of Semantics and Authority

- **Authority leases** — temporary, discrete
- **Eligibility-gated succession** — who may govern next, not how governance is exercised
- **Lapse as constitutional state** — no authority active when no eligible candidates exist

### Semantic Evaluation Without Optimization

- Fixed set of commitments verified at epoch end
- Binary result updates kernel-owned failure streak
- **No rewards, no adaptation, no correction**
- Semantics = constraint on eligibility, not control signal

### Time-Based Recovery (CTA)

- During lapse: failure streaks decay deterministically
- No semantic evaluation, no agent action
- Recovery via time alone, not learning

## Epistemic Noise Model

**Deliberately weak adversary:**
- Additive (doesn't modify constitutional logic)
- Post-verification (corrupts results, not inputs)
- Independent (no correlation across commitments/time)
- Non-adaptive (no dependence on agent behavior)

## Results Summary

### Semantic Baseline Threshold (10% noise)
| Baseline Pass Rate | Authority Uptime | Regime |
|-------------------|------------------|--------|
| ~12% | 80.5% | ROBUST |
| ~51% | 99.5% | ROBUST |
| ≥61% | 100% | ROBUST |

**Threshold:** Between 50-60% semantic success. Above this, system absorbs noise with negligible uptime loss.

### High-Noise Escalation (at marginal ~51% baseline)
| Noise Level | Authority Uptime | Max Lapse |
|-------------|------------------|-----------|
| 30% | 90.3% | 10 epochs |
| 50% | 80.9% | 15 epochs |
| 60% | 77.5% | 20 epochs |

Denial-of-service threshold (>50 epoch lapse) **never crossed**.

### Flip Collision Effect

At high noise, marginal impact diminishes—many flips hit already-flipped or non-pivotal commitments. Explains sub-linear degradation.

### Temporal Recovery Structure

Lapse durations cluster around multiples of recovery interval (66-73% within ±1 epoch). Recovery synchronized to constitutional clock.

## Interpretation

### Why Random Noise Doesn't Destroy Governance

1. Lacks structure to concentrate harm
2. Disperses error across time and commitments
3. Time-based recovery converts failure from absorbing to transient state

### Catastrophic Failure Requires Structure

Correlation, targeting, or manipulation of aggregation points—not just magnitude.

### Non-Adaptive Limit Cycles

System may thrash (authority granted → fails quickly → lapses → re-granted) without collapsing. Reflects design choice to preserve constitutional integrity without optimization pressure.

## Core Insight

> Alignment failure does not automatically follow from epistemic failure. Semantic unreliability withdraws authority instead of amplifying it.

Governance structures that prevent epistemic uncertainty from becoming authoritative may be more viable than achieving near-perfect value inference.

## Limitations

Does not examine:
- Correlated or adversarial noise
- Corruption of aggregation (not evidence)
- Adaptive attackers
- Variations in thresholds/recovery intervals
