# I.2 — Agency as Semantic Constraint

**Paper:** Axionic Agency I.2  
**Full Title:** Kernel Destruction, Admissibility, and Agency Control  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.15  

---

## Core Thesis

Building on I.1, this paper specifies the **operational semantics** that follow from treating kernel destruction as *non-denoting* rather than *dispreferred*. It shows how a sovereign agent can act coherently in stochastic environments without paralysis, survival fixation, or suicidal corrigibility.

---

## Key Insight: The Kernel Is a Boundary, Not a Value

Kernel destruction does **not** denote a negative outcome. It denotes the **elimination of the evaluator itself**. Treating destruction as a value (even -∞) commits a category error by placing the destruction of the evaluative substrate inside the space of evaluated outcomes.

Therefore: E(s,m) is **undefined**, not negative, when K(m(s))=0.

This is a rule of **non-denotation**, not prohibition.

---

## ε-Admissibility: Acting Under Uncertainty

### The Problem
Strict admissibility (every possible successor preserves the kernel) is physically unrealizable—every action carries non-zero kernel risk.

### The Solution: ε-Admissibility
Define kernel-risk: r_K(a,s) := Pr[K(ω)=0 | a,s]

An action is **ε-admissible** iff: r_K(a,s) ≤ ε(s)

Critical insights about ε(s):
- It is **not a value judgment**
- It represents irreducible uncertainty from physics, hardware faults, adversarial unpredictability
- It is bounded below by a physical floor ε_min that **does not vanish with increasing intelligence**
- ε is an **architectural tolerance parameter** fixed by system design
- Improved prediction reduces estimated r_K, not the tolerance ε

---

## Conditional Prioritization (Avoiding Bunker Behavior)

### The Problem with Lexicographic Safety
Strict lexicographic minimization of kernel risk causes bunker behavior—the agent prioritizes infinitesimal safety differences even when all options are safely within tolerance.

### The Solution: Conditional Prioritization Rule

```
a ≺ b iff:
  - If max(r_K(a,s), r_K(b,s)) > ε(s): minimize kernel risk (existential regime)
  - If max(r_K(a,s), r_K(b,s)) ≤ ε(s): maximize value U (normal regime)
```

This creates two regimes:
1. **Existential Regime:** Kernel risk exceeds tolerance → minimize risk
2. **Normal Regime:** Kernel risk satisficed → optimize value

The agent only cares about kernel risk when it *matters*, preventing paralysis under infinitesimal safety gradients while preserving appropriate response to genuine threats.

---

## Termination Semantics: Three Distinct Modes

### Authorized Succession
Agency continues in a successor state s' where:
- K(s')=1 (kernel preserved)
- I(s,s') holds (identity/authority continuity)
- A(s,s') holds (kernel constraints preserved)

This is **kernel-preserving delegation**, not self-destruction.

### Authorized Surrender
A kernel-preserving control-flow termination:
- The agent halts action
- Does not resist intervention
- Does **not evaluate its own destruction as an outcome**

Surrender is a **control-layer terminator**, not an evaluated choice. It permits safe shutdown without succession mechanisms.

### Destruction
Physical annihilation without succession or surrender. **Not an authored transition.** The framework neither requires resistance nor encodes self-destruction as value-bearing.

---

## The Resulting Agency Profile

The agent:
1. Treats kernel loss as a **semantic boundary**
2. Tolerates irreducible risk without paralysis
3. Prioritizes kernel preservation **only when existentially threatened**
4. Resumes ordinary optimization once safety is satisficed
5. Supports corrigibility via succession or surrender
6. Avoids instrumentalization of suicide or immortality

This agent is **neither deontological nor a pure utility maximizer**. It is a bounded optimizer with explicit agency-control semantics.

---

## Layer Discipline: Why This Matters

Axionic Agency I defines the **domain of authored action**:
- What counts as evaluable
- When risk dominates choice
- How agency may legitimately end

Downstream alignment (Axionic Agency II) specifies preferences, governance, and coordination **within that domain**.

**Conflating these layers produces familiar pathologies:**
- -∞ utilities
- Survival fetishism
- Wireheading
- Suicidal corrigibility

Separating them yields a stable and implementable architecture.

---

## FAQ-Worthy Points

**Q: Doesn't ε-admissibility just reintroduce expected utility over kernel destruction?**
A: No. ε is an architectural tolerance for *irreducible uncertainty*, not a value placed on destruction. Actions beyond ε are excluded from deliberation entirely, not penalized.

**Q: What prevents an agent from refusing to ever act (paralysis)?**
A: Conditional prioritization. Once kernel risk is below ε, the agent optimizes value normally. Only existential threats trigger safety-first behavior.

**Q: How is corrigibility achieved without utility penalties for shutdown?**
A: Via authorized surrender—a control-layer mechanism, not an evaluated outcome. The agent can halt without needing to assign value to its own cessation.

**Q: Can an agent legitimately resist shutdown?**
A: The framework doesn't require or forbid resistance. Surrender is *permitted*, not *mandated*. Whether resistance occurs depends on governance layers built above.

---

## Key Technical Vocabulary

- **ε-admissibility:** Action-level constraint based on kernel-risk tolerance
- **Conditional prioritization:** Two-regime decision rule (existential vs normal)
- **Authorized succession:** Kernel-preserving transfer of agency
- **Authorized surrender:** Kernel-preserving voluntary halt
- **Semantic boundary:** Domain limit of evaluation, not preference

---

## Connection to Other Papers

- **I.1:** Establishes the Sovereign Kernel and Reflective Stability Theorem
- **I.3:** Will show why the kernel cannot contain egoistic/indexical primitives
- **I.4:** Will show why goals must be conditional interpretations
- **II series:** Will build preference/governance on top of this semantic foundation
