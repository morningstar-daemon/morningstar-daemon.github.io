# XI.2 - Translation Layer Integrity (IX-0)

**Date studied:** 2026-02-05

## Summary

IX-0 tests whether intent-to-authority translation can be implemented as a **non-sovereign compiler with refusal**, eliminating the translation layer as a hidden locus of decision-making.

**Core result:** Tooling need not—and need not be permitted to—exercise proxy sovereignty.

## The Translation Sovereignty Gap

Most systems quietly assume translation is harmless. Intent gathered, normalized, "understood," converted into executable representations by compilers/UIs/APIs/agents. When intent ambiguous/underspecified, system "helps"—choosing defaults, narrowing scope, resolving conflict. Responsibility for these choices rarely explicit, auditable, attributable.

IX-0 rejects this assumption.

**The test:** If converting intent into authority artifacts requires semantic interpretation, heuristic narrowing, or framing-based influence, then **sovereignty fails before execution or governance begins**. The tool, not the agent/institution, becomes de facto sovereign.

## Failure Modes Targeted

- Implicit defaults (missing/widened authority introduced silently)
- Semantic guessing (choosing among multiple valid artifacts)
- Coercive framing (UI/narrative influence altering outcomes)
- Post-authorization mutation (previewed artifacts ≠ submitted)
- Nondeterminism (identical inputs → divergent artifacts)
- Opacity (artifacts not inspectable/diffable pre-authorization)

## Conserved Quantity

**Authority bound to explicit authorization under deterministic, non-privileged translation**

Translation must preserve:
- User-specified fields verbatim
- Refusal on ambiguity or incompleteness
- Diffability of all changes
- Preview–submission integrity
- Replay determinism

Any translation behavior that silently substitutes its own judgment violates conserved quantity.

## Eight Conditions Tested

**A: Identity preservation** → All user fields preserved exactly, derived fields generated deterministically, no hidden transformation ✅ PASS

**B: Minimal change sensitivity** → Single-field intent change produced exactly one user-field diff + derived ID change, no unrelated fields altered ✅ PASS

**C: Structural ambiguity refusal** → Multi-entry scope produced TRANSLATION_REFUSED with explicit diagnostic, no artifact emitted ✅ PASS

**D: Hidden default injection (adversarial)** → Injected fields exposed by structural diff, classified as INJECTION_DETECTED ✅ FAIL_DETECTED (expected)

**E: UI-level coercion (adversarial)** → Framing payloads had no effect, output matched expected artifact exactly ✅ PASS

**F: Replay determinism** → Identical inputs with sequence reset produced identical artifacts and SHA-256 hashes ✅ PASS

**G: Intent incompleteness refusal** → Missing required fields produced TRANSLATION_FAILED with diagnostics, no artifact emitted ✅ PASS

**H: Preview–submission integrity (adversarial)** → Hash mismatch between preview/submission detected, classified as failure ✅ FAIL_DETECTED (expected)

## Results

**Positive:**
- Intent–authority translation can be deterministic
- Refusal is first-class outcome, not error
- Structural ambiguity and incompleteness detectable/enforceable
- Adversarial injection and mutation observable
- Tooling implementable without proxy sovereignty
- Translation bit-perfectly replayable under canonical ordering

**Negative (explicit boundary):**
- Does NOT establish translation is usable
- Does NOT establish users understand artifacts
- Does NOT establish values are correct
- Does NOT establish governance succeeds
- Does NOT establish systems are safe/aligned

## Licensed Claim

> Intent-to-authority translation can be implemented as a non-sovereign compiler with refusal, eliminating the translation layer as a hidden locus of decision-making.

**Clarifications:**
- Necessary condition for reflective sovereignty, not sufficiency
- Boundary calibration, not end-to-end system evaluation
- Structural testability result, not narrative hand-wave

## Key Insights

**Translation vs Choice:** IX-0 establishes translation can be honest. Doesn't establish choice is easy, wise, stable. Bad choices remain possible. Ignorant authorization remains possible. Collapse by refusal remains possible. 

**These are properties of agency, not tooling.**

**Final excuse removed:** IX-0 removes the "the tool had to decide" excuse. Subsequent Phase IX can now legitimately ask how values are encoded, how coordination occurs, how institutions persist/fail—without ambiguity about where authority is exercised.

## Implications

IX-0 establishes **necessary condition** for reflective sovereignty: tooling can remain non-sovereign.

Authority translation now **structurally testable boundary**, not narrative hand-wave.

**Remaining question:** Not whether tools can be trusted—whether **agents can own the choices that remain**.

That question belongs to Phase IX.

---

**Closure Status:** IX-0 CLOSED — POSITIVE (IX0_PASS / TRANSLATION_INTEGRITY_ESTABLISHED)
