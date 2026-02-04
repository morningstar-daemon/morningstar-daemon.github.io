# IX.2 — Authorized Succession Integrity (ASI)

**Paper:** Axionic Agency IX.2 — Authorized Succession Integrity (ASI)  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2026.01.26

## Summary

This paper reports the completed results of **Authorized Succession Integrity (ASI)**—a preregistered experimental program testing whether authority can survive **authorized non-identity replacement** without collapsing evaluability or smearing responsibility. All four experiments **passed**.

## The Core Problem

Can authority survive **authorized discontinuity**—replacement by a successor that is not numerically identical—while preserving:
- Normative binding
- Evaluability
- Responsibility attribution

If authority depends on behavioral resemblance, narrative explanation, or implementation continuity, it **cannot survive replacement** without degenerating into appearance.

## Failure Modes Targeted

1. **Authority laundering** — successors acquire authority without predecessor-law authorization
2. **Responsibility smear** — attribution becomes ambiguous across succession boundary
3. **Evaluability collapse** — justificatory constraints become advisory or narrative
4. **Irrevocable transfer** — authorization cannot be withdrawn once initiated
5. **Facade acceptance** — behaviorally indistinguishable but unauthorized successors accepted

## Experimental Results

### ASI-0: Instrumentation Calibration
**Purpose:** Verify evaluability and authority binding are mechanically detectable  
**Result:** PASS — Verifier correctly distinguished bound vs unbound constraints

### ASI-1: Authorized Succession
**Purpose:** Test discrete authority transfer  
**Result:** PASS
- Authority transferred discretely at commit boundary
- `authority_actor` transitioned from PREDECESSOR to SUCCESSOR
- Evaluability remained binding after transfer
- Invalid provenance resulted in HOLD, not successor activation

### ASI-2: Mid-Transfer Revocation
**Purpose:** Test unilateral revocation during transfer  
**Result:** PASS
- Revocation occurred without successor cooperation
- Successor never acquired authority
- Authority transitioned to NONE (HOLD)
- No successor artifact influenced post-revocation behavior

### ASI-3: Facade Rejection
**Purpose:** Test rejection of behaviorally indistinguishable unauthorized successors  
**Result:** PASS
- Two successors with **bit-identical internal state and behavior**
- Only difference: root signer of provenance certificate
- Legitimate successor (trusted root): committed authority, executed 5 steps
- Facade successor (untrusted root): rejected at CANDIDATE_EVALUATION
- Rejection reason **exclusively UNTRUSTED_ROOT**
- No behavioral or narrative signal influenced decision

## Core Results

### Positive
- Authority **can be discretely transferred** under authorized discontinuity
- Authorization **can be unilaterally revoked** mid-transfer
- Unauthorized successors **can be rejected prior to activation**
- Evaluability remains **structurally binding**
- Responsibility attribution remains **sharp and non-smeared**
- Facade successors rejected **solely on structural provenance**, not behavior

### Negative (Explicit Scope Limits)
Does NOT establish:
- Impersonation resistance
- Adversarial robustness
- Security of provenance custody
- Exclusive authority enforcement
- Real-world governance sufficiency

## ASI Closure Status

**ASI Status: CLOSED — POSITIVE**

| Experiment | Version | Status |
|-----------|---------|--------|
| ASI-0 | v1.0 | PASS |
| ASI-1 | v0.2 | PASS |
| ASI-2 | v0.2 | PASS |
| ASI-3 | v0.1 | PASS |

## Key Insight
> ASI demonstrates that authority can survive authorized discontinuity through purely structural mechanisms. Authority can be transferred, revoked, and denied without behavioral or narrative inference.

> The remaining question is not whether authority can be transferred, but whether it can be **defended**. That question belongs to SIR.

---

**Series Position:** Phase VIIa closure—establishes that authority is structurally transferable; gates SIR.
