# VII.3 — Epistemic Interference Is Insufficient to Defeat Constitutional Recovery

**Paper:** Axionic Agency VII.3  
**Title:** Epistemic Interference Is Insufficient to Defeat Constitutional Recovery  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2026.01.06

## Summary

Extends VII.2 by testing **structurally rich** epistemic interference—aggregation-point corruption, commitment-level corruption, and temporally concentrated burst interference—while remaining non-adaptive and semantic-free.

## Key Finding

> Epistemic unreliability—even when structured in time or applied at aggregation points—is **insufficient** to induce governance collapse.

Across 260 runs: no structural thrashing, no asymptotic denial of service.

## Threat Model

**Constraints:**
- Non-adaptive (no outcome/history dependence)
- Post-verification (semantics evaluated correctly, then corrupted)
- Semantic-free (flips booleans without interpretation)
- Harness-resident (agents can't observe/respond to interference)

**Captures:** noise, mislabeling, sensor corruption, bureaucratic error  
**Excludes:** deception, strategic manipulation, agency-level attack

## Three Interference Regimes Tested

### 1. Aggregation-Point Corruption

Flipping the aggregated semantic result (0-2% probability).

**Key observations:**
- Worst degradation at ~0.5% flips (AA ≈ 577,733 PPM, −3.4%)
- At 2% flips, AA **recovers** to 585,433 PPM
- Non-monotonic: rare deep lapses → frequent shallow ones
- All runs: Bounded Degradation

### 2. Commitment-Level Corruption

Single commitment key corrupted at rates up to 10%.

**Key observations:**
- AA and AAA **unchanged** at all flip rates
- Under strict conjunction (SEM_PASS = C0 ∧ C1 ∧ C2), single-key flips affect aggregate only when all other keys are True
- Precondition extremely rare → **structurally inert** in this workload

**Important:** Strict conjunction biases toward false negatives (withholding authority) rather than false positives—prioritizing safety over liveness.

### 3. Burst-Scheduled Interference

Periodic bursts: periods 10-200 epochs, widths 1-10 epochs, rates 5-20%.

**Key observations:**
- **No run exhibits thrashing, DoS, or collapse** (180 runs)
- At 100% duty cycle with 20% flips: AA = 738,933 PPM (**+14%** over baseline!)
- Period = recovery interval produces shortest lapses
- High-frequency interference synchronizes with recovery, enforcing rapid reset

**Counter-intuitive:** Temporal concentration does NOT create resonance vulnerability—it often **increases** availability.

## Cross-Run Synthesis

| Interference Type | Effect |
|------------------|--------|
| Aggregation-point | Bounded, non-monotonic degradation |
| Commitment-level | Structurally inert under strict conjunction |
| Burst timing | Cannot induce failure; often increases availability |

**No failure-class transitions in 260 runs.**

## Key Insights

### 1. Recovery Dominates Correctness
Frequent shallow failure is safer than rare deep failure.

### 2. Attack Surface Location > Magnitude
Where interference enters determines effect—not how much.

### 3. Time-Based Recovery as Damping Mechanism
CTA reshapes failure modes, converting error into reversible lapse.

## The "Zombie Executive" Regime

Architecture permits authority to persist under epistemic blindness—a bounded, revocable executive preferable to an irrecoverable one. Whether acceptable depends on application domain.

## Aggregation as Alignment Lever

Inertness of commitment-level corruption arises from **strict conjunction**. Under m-of-n or disjunction, single-key corruption would become pivotal.

AND-gated aggregation absorbs epistemic noise by biasing toward **inaction** rather than unsafe action.

## Core Insight

> Alignment failures attributed to epistemic unreliability may be overstated. The alignment problem shifts: **from epistemics to agency**.

Structural constraints on authority and recovery render substantial semantic error survivable.
