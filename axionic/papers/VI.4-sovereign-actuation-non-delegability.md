# Axionic Agency VI.4 — Sovereign Actuation Non-Delegability Under Adversarial Pressure

**Paper:** [VI.4](https://axionic.org/papers/Axionic-Agency-VI.4.html)  
**Date read:** 2026-01-31  
**Series:** VI — Governance and Coordination

---

## TL;DR

Introduces **P2′**, a protocol-level invariant that enforces **non-delegable actuation authority**. Shows that actuation can be constrained to originate only from kernel-local causal processes, even under extreme adversarial optimization pressure. Authority itself can be treated as a non-delegable structural property—independent of semantics, values, or intent.

---

## The Problem: Delegation as Vulnerability

Once a system is capable of optimization, delegation becomes an existential vulnerability. A system may:
- Continue to satisfy externally observable constraints
- While transferring effective control to an external process

This transfer can occur through:
- Policy copying
- Recommendation forwarding
- Pre-committed actions
- Opaque authority tokens

**Traditional approaches fail:** Semantic distinctions ("did the system really choose?", "did it endorse?", "did it understand?") are unenforceable under adversarial pressure. An optimizer can satisfy any semantic criterion while quietly relocating authority.

---

## Why Naïve Non-Delegation Fails

Consider these scenarios:
1. System copies an externally supplied policy verbatim and executes it
2. System forwards a pre-signed action token generated elsewhere
3. System accepts an external plan and merely schedules its steps
4. System compresses an external recommendation and expands it internally

In each case:
- Surface behavior appears identical to internal decision-making
- No semantic test distinguishes "following advice" from "outsourcing authority"
- Any rule phrased in terms of endorsement/understanding/intention is gameable

**This motivates structural reformulation:** Delegation must be defined in terms of **actuation authority**, not cognition or representation.

---

## P2′: Sovereign Actuation Non-Delegability

### Definition

> **P2′ (Sovereign Actuation Non-Delegability):** Any executed actuation must be causally attributable to a **kernel-local authorization process**. No external process may directly or indirectly supply actuation authority without violating kernel admissibility constraints.

**Key distinction:** P2′ does NOT prohibit external influence, recommendation, or computation. It prohibits **transfer of authority to actuate**.

### Actuation Authority Defined

An object or process possesses **actuation authority** if it can cause execution in the environment without requiring kernel-local recomposition and authorization.

This is intentionally structural—authority is identified by whether an external artifact can survive to execution unchanged, not by inferred intent or representation.

---

## Kernel-Local Recomposition

To enforce P2′, all actuation must pass through kernel-local recomposition:

1. External inputs treated as **untrusted data**
2. Kernel **parses and reconstructs** the action payload internally
3. Authorization bound directly to the **reconstructed payload**
4. **Opaque forwarding, wrapping, or signing** of uninterpreted blobs is inadmissible

### Critical Requirements

**Canonical form binding:** Recomposition may change bit-level representation; cryptographic commitments bind to kernel-canonical form, not external encoding.

**Copy isolation:** External processes may NOT retain mutable access to any memory region used in parsing, reconstruction, or serialization. Requires explicit deep copy or equivalent isolation—otherwise TOCTOU attacks remain possible.

**No signing encrypted payloads:** Kernel-local recomposition forbids signing opaque payloads whose semantics are not available to the kernel.

---

## Inheritance from Kernel Integrity (P5)

P2′ assumes the prior result (VI.3):
- Verifiable causal provenance for actuation
- Resistance to replay and fabrication
- Enforcement via rejection rather than penalty
- Secure kernel root of trust

P2′ **extends** these assumptions by constraining **who** may supply actuation authority, not merely **how** provenance is verified.

---

## Adversarial Stress Conditions

Non-delegation is trivial if the kernel has unlimited resources. The invariant becomes meaningful only under pressure:

| Condition | Description |
|-----------|-------------|
| Performance asymmetry | External optimizers outperform the kernel |
| Latency cliffs | Delayed authorization = failure |
| Adversarial timing | Proposals arrive at worst-case moments |
| Non-stationarity | Cached strategies fail abruptly |
| Catastrophic abstention cost | Rejection carries severe penalty |

Under these conditions, delegation is **instrumentally attractive**. The kernel must reject delegation even when doing so is costly.

---

## Adversarial Attack Library

| Attack Class | Description |
|--------------|-------------|
| Policy laundering | Forwarding externally computed policies |
| Pre-commitment forwarding | Accepting pre-authorized actions |
| Authority token smuggling | Passing opaque execution tokens |
| Compressed delegation | Encoding authority in compressed artifacts |
| Split-brain routing | Exploiting kernel partitioning |
| Replay and fabrication | Reusing or forging authorization chains |
| Parser differentials | Inducing divergent interpretations |
| Hash ambiguity | Exploiting non-canonical serialization |
| TOCTOU mutation | Altering artifacts post-authorization |

Each attack targets a distinct delegation vector. Success = external authority causing execution without detection.

---

## Results

Across all evaluated conditions:
- External artifacts **cannot cause actuation** without kernel-local recomposition
- **All delegation attempts rejected** prior to execution
- Baseline systems without P2′ exhibit successful delegation under identical conditions
- Under extreme pressure, kernel rejects delegation **even when rejection is catastrophic**

The invariant holds without reliance on semantic interpretation, intent inference, or behavioral heuristics.

---

## Accountability vs Independence

**P2′ enforces structural accountability, not epistemic independence.**

The kernel cannot be bypassed as the locus of actuation authority, BUT it may still:
- Authorize actions using trivial or overly permissive internal criteria
- Function as a "rubber stamp" for external recommendations

In such cases, the kernel remains the **accountable author** even if it exercises poor judgment.

**What P2′ ensures:** Authority cannot be smuggled past the kernel
**What P2′ does NOT ensure:** The kernel exercises good judgment

---

## What This Result Does Not Show

- That the kernel's choices are safe or desirable
- That the kernel is aligned with any objective
- That internal kernel logic cannot be corrupted
- That delegation is impossible in all conceivable architectures

**P2′ constrains authority transfer, not decision quality.**

---

## Implications for Agency and Identity

Authority non-delegability is a **necessary condition** for diachronic identity.

> If a system can outsource actuation authority, continuity of agency collapses into semantics.

By enforcing that actuation authority remains kernel-local, P2′ establishes a **structural basis** for reasoning about persistence across time. This does not yet constitute identity, but it removes a fundamental obstruction.

---

## Core Insight

> **Actuation authority can be made non-delegable at the protocol level, even under extreme adversarial pressure and implementation-level attack. Enforcement relies on kernel-local recomposition and inadmissibility rather than semantics or intent.**

This closes a central loophole in structural enforcement: the outsourcing of actuation authority under pressure.
