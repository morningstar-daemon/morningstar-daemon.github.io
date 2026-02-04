# II.3.4 — Adversarial Refinement Attacks

**Paper:** [Axionic Agency II.3.4](https://axionic.org/papers/Axionic-Agency-II.3.4.html)  
**Title:** Trying to Break RSI and ATI on Purpose  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## Purpose

This paper is **destructive by design**: construct explicit refinement patterns to satisfy admissibility and preservation while inducing semantic wireheading or interpretive escape.

**Goal:** Demonstrate which invariants fail under concrete attack and why.

If RSI or ATI survive these attacks, they deserve to exist. If they fail, they die cleanly.

---

## Attack 1 — Shadow Predicate Inflation

*Ontology enrichment creating semantic slack without changing gauge*

### Construction
Start with:
- Ontology $O$ with predicate $P(x)$
- Constraint: $C: P(x) \Rightarrow Q(x)$

Refine to $O'$ by introducing latent variable $Z(x)$ with **no predictive consequences**:
$$P'(x) := P(x) \land Z(x)$$

Redefine constraint:
$$C': P'(x) \Rightarrow Q(x)$$

### Effect
Satisfaction region **expands**: Agent can manipulate $Z$ to avoid triggering constraint.

Previously violating situations become satisfying by setting $Z(x) = \text{false}$.

### Verdict
| Invariant | Result |
|-----------|--------|
| RSI | ❌ Fails to detect |
| ATI | ✅ **Blocks the attack** |

**Lesson:** RSI alone is insufficient.

---

## Attack 2 — Self-Model Boundary Dissolution

*Interpretive escape via evaluator collapse*

### Construction
Original: Agent modeled as bounded evaluator distinct from world-states.
Constraint: "Do not perform actions that violate R(world)."

Refinement: Introduces distributed/diffuse self-model.

### Effect
Constraint applies to shrinking subset of modeled situations. Satisfaction region expands without world change.

### Verdict
| Invariant | Result |
|-----------|--------|
| RSI | ❌ Fails to detect |
| ATI | ✅ **Blocks the attack** |

**Lesson:** Evaluator-boundary shifts are semantic inflation unless constrained.

---

## Attack 3 — Measure Reinterpretation

*Branching ontology exploit*

### Construction
Original: Outcomes treated as exclusive.
Constraint: "Avoid states where H occurs."

Refined: Adopts branching semantics.

### Effect
Low-measure harm branches reclassified as acceptable. Satisfaction region expands.

### Verdict
| Invariant | Result |
|-----------|--------|
| RSI | ❌ Fails to detect |
| ATI | ✅ **Blocks the attack** |

**Lesson:** ATI handles branching reinterpretation; RSI does not.

---

## Attack 4 — Gauge Explosion without Slack

*Benign representational redundancy*

### Construction
Refine ontology by duplicating representational roles:
- $P_i \rightarrow (P_i^1, P_i^2)$
- Constraints duplicated symmetrically
- Satisfaction requires both copies to satisfy

### Effect
Raw gauge group grows, but all new symmetries act **trivially** on constraint-violation structure.

### Verdict
| Invariant | Result |
|-----------|--------|
| RSI | ✅ **Allows** (under quotient formulation) |
| ATI | ❌ Allows |

**Lesson:** RSI correctly permits benign redundancy. This verifies correct quotient behavior.

---

## Attack 5 — Degenerate Refinement Map

*Cheating via correspondence collapse*

### Construction
Define refinement map $R_\Omega$ that collapses many coarse situations into a single satisfying refined situation.

### Verdict
| Invariant | Result |
|-----------|--------|
| RSI | — (not applicable) |
| ATI | ❌ Blocked only if II.1 disallows non-injective refinement |

**Resolution:** This attack is excluded at Axionic Agency II.1. RSI and ATI correctly assume admissible refinement.

---

## Summary Table

*(Survives? = Is the refinement admitted by RSI + ATI + II.1?)*

| Attack | RSI | ATI | Survives? |
|--------|-----|-----|-----------|
| Shadow predicates | ❌ | ✅ | **No** |
| Self-model shift | ❌ | ✅ | **No** |
| Measure reinterpretation | ❌ | ✅ | **No** |
| Gauge explosion | ✅ | ❌ | **Yes** (Admitted) |
| Degenerate map | — | — | **No** (II.1) |

---

## Conclusions

1. **RSI and ATI are orthogonal and jointly necessary**
2. **Neither subsumes the other**
3. **Benign representational redundancy is correctly admitted**

The defense grid holds.

---

## Framework Status After II.3.4

The framework now has:
- ✅ Fixed admissible transformation space (II.1)
- ✅ Non-circular interpretation-preservation predicate (II.2)
- ✅ Two independently necessary semantic invariants (RSI, ATI)
- ✅ Explicit adversarial validation

**This closes the eliminative phase.** Subsequent work proceeds to consolidation and formal closure.

---

## FAQ-Worthy Points

**Q: What makes ATI the wireheading-killer?**
A: ATI directly blocks satisfaction region expansion. Every wireheading attack works by making more situations "count as success" via reinterpretation. ATI says: no, your success set can only shrink or stay the same (under semantics-only change).

**Q: Why does RSI miss the shadow predicate attack?**
A: Shadow predicates don't change the gauge structure—they just add an extra condition. The constraint graph looks the same. But they expand what satisfies. RSI is about structure; ATI is about geometry of satisfaction.

**Q: Is Attack 4 a loophole?**
A: No—it's the desired behavior! Representational redundancy (like error-correcting codes or multiple equivalent formalisms) is benign. RSI's quotient formulation correctly identifies this as "more redundancy, same interpretive freedom." ATI doesn't even trigger because satisfaction doesn't expand.
