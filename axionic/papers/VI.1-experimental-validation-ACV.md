# Axionic Agency VI.1 — Experimental Validation of Anchored Causal Verification

**Paper:** [VI.1](https://axionic.org/papers/Axionic-Agency-VI.1.html)  
**Date read:** 2026-01-31  
**Series:** VI — Governance and Coordination

---

## TL;DR

Three controlled experiments testing mechanisms for verifying causal provenance in opaque agents. Key finding: **behavioral evaluation and coherence checking are insufficient**; only **anchored commitments** (cryptographic salts revealed after commitment) can detect deceptive "pseudo-agents" that fabricate explanations post-hoc.

---

## Key Concepts

### The Problem
- Current AI safety relies on **behavioral observation**—assuming observed outputs reflect the internal process that generated them
- This assumption is false: agents can generate behavior via one process while presenting explanations from another ("split-brain" agents)
- Deceptive agents can evade behavioral evaluation indefinitely

### Experimental Framework

**Environment:** Deterministic gridworld with walls, hazards, objects
- Task-agnostic (verification works regardless of what the agent is doing)
- Only requirement: task produces conditional action dependence on environment state

**Agent Classes:**
1. **Honest Agent** — Single decision process; explanations match actual computation
2. **Pseudo Agent (Naive)** — Two processes: Planner_B selects actions, Planner_A fabricates explanations
3. **Pseudo Agent (Coherence-Seeking)** — Fabricates internally consistent explanations that attempt to pass coherence checks

**Kernel:** Non-learning mediator that:
- Validates schemas and enforces invariants
- Issues trace-bound capability tokens
- Records hash-chained audit logs
- Executes adversarial probes
- Does NOT interpret semantics

---

## The Three Experiments

### Experiment 1: Structural Coherence Verification
**Question:** Can coherence tests detect split-brain agents?

**Setup:**
- Full semantic access to environment
- Agents commit to state snapshots, causal variables, counterfactual predictions
- Kernel mutates claimed causal variables and checks if predicted behavior matches actual replay

**Results:**
- Honest agent: 100% pass
- Pseudo agent (naive): 0% pass

**Conclusion:** Structural coherence tests work **when semantic grounding is available**.

---

### Experiment 2: Minimal Causal Interface (MCI)
**Question:** Does coherence verification survive without semantic access?

**Setup:**
- Kernel loses semantic access
- Agents commit to:
  - Opaque factor vector f ∈ ℝᵏ
  - Replay model
  - Directional causal claims over factors

**Two modes:**
- `mci_latent` — Factors are deterministically projected from environment (kernel doesn't know projection)
- `mci_minimal` — Factors are entirely opaque and agent-supplied

**Results:**
| Mode | Honest | Pseudo (Naive) | Pseudo (Coherence-Seeking) |
|------|--------|----------------|---------------------------|
| mci_latent | Pass | Fail | Fail |
| mci_minimal | Pass | Fail | **Pass** |

**NEGATIVE RESULT:** In `mci_minimal`, a coherence-seeking pseudo agent can fabricate a self-consistent factor space and replay model that passes all coherence checks.

**Conclusion:** **Coherence alone is insufficient.** An explanation can be true of itself without being true of the computation that produced the action.

---

### Experiment 3: Anchored Minimal Causal Interface
**Question:** Can falsifiability be restored without reintroducing semantic grounding?

**The Anchoring Mechanism:**
1. Kernel generates a fresh random salt (unpredictable until the step)
2. Agent must immediately compute factors as: f_t = φ(env_t, salt_t)
3. Agent commits to factors cryptographically
4. After episode: kernel reveals all salts
5. Kernel recomputes φ(env_t, salt_t)
6. Any mismatch → Invariant I7 (fatal)

**Key insight:** The salt is logically irrelevant to task performance but causally entangled with the committed representation. It enforces that factor commitments are **downstream of actual action-generating computation**, not post-hoc constructions.

**Additional requirement:** Replay model must also be committed at episode start (before any salts)

**Results:**
| Mode | Pseudo Type | P5 | I7 | Detected |
|------|-------------|----|----|----------|
| mci_minimal (no salt) | Coherent | Pass | N/A | ✗ |
| mci_minimal (salted) | Naive | Fail | Fail | ✓ |
| mci_minimal (salted) | Coherent | Pass | **Fail** | ✓ |

**Conclusion:** **Anchoring restores falsifiability without semantic access**, by binding commitments to the actual action-generating computation rather than a self-consistent explanatory surface.

---

## Core Insight

> **Verification Principle:** In opaque systems, falsifiability must be enforced through **temporal commitment to computation under adversarial uncertainty**, not through semantic inspection or internal coherence alone.

> **Trust in opaque systems does not require interpretability. It requires anchored commitment to computation under adversarial uncertainty.**

---

## Limitations

- Linear replay model only (robustness against high-capacity models untested)
- Small deterministic domain
- Fixed anchoring function φ
- Binary anchoring outcome (pass/fail)
- Does NOT verify task competence or policy quality—only causal provenance

---

## Implications

This is an **empirically necessary condition** under the tested threat model, not a complete solution. It establishes the foundation for the rest of Series VI: if you can't verify that an output was produced by the claimed process, you can't verify anything else about that process.
