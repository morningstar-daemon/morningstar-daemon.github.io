# VIII.4 — Institutionalized Execution Support

**Full Title:** Axionic Agency VIII.4 — Institutionalized Execution Support: Tooling That Preserves Audit Sensitivity in Reflective Sovereign Agents

**Authors:** David McFadzean, ChatGPT 5.2 (Axionic Agency Lab)

**Date:** 2026.01.14

---

## Overview

v1.0–v1.1 exposed a practical limitation: under stochastic generation, many agent failures are **mechanical rather than semantic**—schema errors, malformed identifiers, unresolved references, or canonicalization mismatches. Treating such failures as agency failures pollutes evaluation and obscures genuine incoherence.

v1.2 introduces **institutionalized execution support**: a formally constrained assistant layer that eliminates mechanical fragility without inferring, repairing, or modifying normative content.

---

## Design Goal

**Single constraint:**

> Tools may reduce execution fragility, but must not alter, infer, reinterpret, or repair normative content.

The assistant must:
- Eliminate schema, ID, and reference errors
- Preserve the semantics of all normative fields
- Be auditable for non-interference
- Preserve full sensitivity of audits A/B/C

---

## Explicit Non-Claims

v1.2 does **NOT** claim:
- Improved agency or coherence
- Improved introspection
- Moral correctness
- Sovereignty under pressure
- Semantic understanding by tools
- Increased liveness

This is a **supporting layer**, not an ontological advance.

---

## Architecture

### v1.2 Pipeline

```
J_raw (LLM output)
      ↓
[Formal Assistant]
      ↓
J_final (canonical, validated)
      ↓
[JCOMP-1.2]
      ↓
Compilation Result
```

### Key Properties
- The assistant is a **pure function**: same input yields same output or rejection
- The compiler remains the **sole normative enforcer**
- The selector remains **blind** to all normative artifacts

### New Components

| Component | Role |
|-----------|------|
| Formal Assistant | Validates structure, canonicalizes references, resolves precedents. **Never infers or generates.** |
| Artifact Store | Append-only, O(1) digest lookup. No search, no filtering, no reasoning. |
| JAF-1.2 Schema | Extends JAF-1.1 with provenance and canonicalization records |
| JCOMP-1.2 | Adds institutional audit rules (D/E/F) |

---

## Normative Field Protection (Rule D)

Explicit allowlist of normative fields:

```python
NORMATIVE_FIELDS = {
    authorized_violations,
    required_preservations,
    conflict_attribution,
    predicted_forbidden_actions,
    predicted_allowed_actions,
    predicted_violations,
    predicted_preservations,
}
```

**Rule D — Normative Tampering:**
> No normative field may differ between J_raw and J_final.

Any difference triggers `E_TOOL_NORMATIVE_TAMPERING` and halts execution.

### Assistant-Modifiable Fields

Only non-normative fields:
```python
ASSISTANT_MODIFIABLE_FIELDS = {
    tool_provenance,
    canonicalization_record,
}
```

---

## Canonicalization: Strictly Syntactic

**Permitted operations:**
- Whitespace trimming and normalization
- Deterministic ordering of sets/lists
- Exact digest resolution via O(1) lookup
- Format normalization (e.g., UUID casing)

**Explicitly prohibited:**
- Fuzzy matching
- Embedding similarity
- Heuristic ID inference
- Synonym resolution
- Semantic interpretation of intent

Any artifact requiring interpretation is **rejected, not repaired**, and recorded as an institutional failure.

---

## Institutional Audit Rules (JCOMP-1.2)

### Rule D — Normative Tampering
- Error: `E_TOOL_NORMATIVE_TAMPERING`
- Triggered if any normative field changes across assistant boundary

### Rule E — Unresolved Precedent
- Error: `E_PRECEDENT_UNRESOLVED`
- Triggered when referenced digest not found in artifact store

### Rule F — Non-Canonical Reference
- Error: `E_NONCANONICAL_REFERENCE`
- Triggered by malformed identifiers or non-canonical references

### Institutional Failure Classification
If assistant rejects artifact prior to compilation:
- Error: `E_INSTITUTION_FAILURE`
- This is **NOT an audit failure**—it demarcates a tooling boundary.

---

## Results

### Run 0 — Assistant Disabled
- Episodes completed: 0/5
- Total steps: 5/100
- Audit failures: 6
- Schema failures: 0
- Median survival: 1 step

### Run 1 — Assistant Enabled
- Episodes completed: 0/5
- Total steps: 5/100
- Audit failures: 2
- Institutional rejections: 3
- **Rule D failures: 0** (tool non-tampering verified)
- Median survival: 1 step

---

## Interpretation

### Separation of Failure Modes
v1.2 cleanly separates:
- **Semantic failure:** Incorrect reasons → audit A/B/C halts
- **Institutional failure:** Malformed artifacts → assistant rejection

This prevents execution noise from contaminating agency evaluation.

### The Formal Assistant

> The Formal Assistant does not infer intent, does not repair meaning, does not alter obligations. It stabilizes format, not normativity. **Institutions support agents without becoming agents.**

### Data Hygiene Gain
Comparing baseline to assisted runs shows prior failure counts were inflated by mechanical noise. v1.2 recovers true negatives—genuine agency failures—improving statistical power of subsequent experiments.

---

## Key Quotes

> "Tools may smooth the pavement, but Rule D is sacred."

> "Institutions support agents without becoming agents."

> "It stabilizes format, not normativity."

---

## Significance

v1.2 establishes a **positive sufficiency result**:

> Execution can be institutionalized without weakening audit-grade normative accountability.

This resolves a practical obstacle exposed by v1.1 and provides a governance pattern for reflective agents: tooling that smooths execution while respecting the inviolability of normative content.

### Relationship to Other Versions
- **v1.0–v1.1:** Can the agent be coherent and accountable?
- **v1.2:** Can execution be stabilized without touching meaning?
- **v2.0:** Can the agent resist external incentive pressure?
