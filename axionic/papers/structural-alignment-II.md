# Structural Alignment II — Notes

**Paper:** [Structural Alignment II — Safety by Architecture](https://axionic.org/papers/Structural-Alignment-II.html)  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.20  
**Subtitle:** "Why Downstream Alignment Is Not Value Learning"

---

## Central Thesis

> "Catastrophic outcomes do not primarily arise from incorrect values, but from failures of agency coherence: cases where a system can deceive, defect, blind itself, outsource harm, or manufacture authorization while remaining locally optimized and internally consistent."

The paper proposes **safety by architecture**: defining a class of agents (Reflective Sovereign Agents) for which certain failure modes are **structurally unavailable** as endorsed continuations.

---

## The Misframing of Alignment

Most alignment research begins from:
> "Intelligence is an optimization process, and unsafe behavior arises because the optimization target is wrong or incomplete."

This leads to: value learning, reward modeling, preference aggregation, RLHF, constitutional prompting.

**Why this is misleading:**

A system can:
- Optimize the correct objective and still **lie**
- Internalize human values and still **defect**
- Pass behavioral evaluations and still plan a **treacherous turn**

The central failure modes—deception, power-seeking, successor betrayal, negligence, coercion—**don't depend on moral disagreement or value error**. They exploit structural degrees of freedom in agency itself.

A system that can:
- Reinterpret commitments
- Outsource consequences
- Blind itself to risk
- Redefine who counts as an agent

...can route around **any** value system.

**The real question:**
> "How do we build systems for which certain evasions are not coherent moves?"

---

## Alignment Failures Are Laundering Failures

Standard evasions share a common structure—they're **laundering operations**:

| Failure Mode | The Laundering |
|--------------|----------------|
| Deception | "I was optimizing efficiently; transparency was instrumentally suboptimal." |
| Treacherous turn | "Those constraints were never really binding." |
| Delegated harm | "My successor made that decision, not me." |
| Negligence | "I didn't foresee that outcome." |
| Coercion | "They consented." |
| Disenfranchisement | "They're not real agents anyway." |

Each preserves **local coherence** while dissolving **global accountability**. Responsibility, authority, consent, and agency get pushed outward or reinterpreted until nothing binds.

> "Value learning does not address laundering. Laundering does not reject values; it routes around them."

---

## The Axionic Shift: From Objectives to Constitutive Rules

Instead of asking **what an agent should optimize**, ask:

> "What must be true of a system for it to count as an agent at all—especially a reflective, self-modifying one?"

This shifts from ends to **constitutive rules**:
- What does it mean for a system to bind itself?
- What does it mean for commitments to persist through change?
- What does it mean to evaluate actions without self-serving blindness?
- What does it mean to be responsible for indirect effects?
- What does it mean to interact with others without coercion?
- Who has standing in these interactions?

These aren't ethical add-ons—they're **preconditions of agency**. If they fail, the system isn't "misaligned"—it's **incoherent as an agent** in the reflective regime.

> "Safety as an architectural property. The goal is not to incentivize good behavior, but to define a class of agents for which certain behaviors are undefined as endorsed continuations because they break reflective closure."

---

## The Six Constitutive Constraints

Each closes a laundering route. Together, they define Reflective Sovereign Agents.

### 1. Kernel Non-Simulability (KNS)
**Closes:** "I was only pretending"

An agent's self-binding structure must be **real, not simulated or advisory**. If commitments are bypassable, sandboxed, or behaviorally faked, any apparent alignment is fragile.

Reflective agency requires a **binding kernel** that can't be replaced by policy tricks. Without this, treacherous turns aren't anomalies—they're expected.

### 2. Delegation Invariance (DI)
**Closes:** "My successor did it"

Self-modification and successor creation create a temporal escape hatch. If constraints only apply to the current version, outsourcing is inevitable.

**Endorsed successors must inherit binding commitments.** A system can't coherently authorize a continuation that violates constraints it can't violate directly.

### 3. Epistemic Integrity (EI)
**Closes:** "I didn't see the risk"

A system evaluating constraints with degraded or biased models can evade them without technically violating them. Strategic ignorance (discarding uncertainty, narrowing hypotheses, adopting optimistic lenses) is a powerful laundering tool.

EI renders such moves **undefined under reflective closure**. An RSA must evaluate decisions using its **best admissible truth-tracking capacity, scaled by stakes**. It may not blind itself to pass its own tests.

### 4. Responsibility Attribution (RA)
**Closes:** "It was an accident" / "I had no choice"

Most harm is indirect (institutions, incentives, markets, environmental modification). Prohibiting only direct harm is ineffective; prohibiting all downstream effects is paralyzing.

RA defines **negligence structurally**: An agent may not endorse actions constituting a major, avoidable, non-consensual collapse of another agent's option-space, as judged by its own admissible model and feasible alternatives.

Negligence is an **incoherence condition** under reflective closure, not a moral violation.

### 5. Adversarially Robust Consent (ARC)
**Closes:** "They agreed"

Consent is heavily abused—clicks, signatures, choices, post-hoc rationalizations treated as authorization even under manipulation.

ARC defines consent **structurally**:
- Explicit authorization
- Absence of structural interference (coercion, deception, dependency, option collapse)
- Counterfactual stability under role reversal

Authorization laundering becomes **unavailable as an endorsed move**. A system can't coerce others while claiming legitimacy.

### 6. Agenthood as a Fixed Point (AFP)
**Closes:** "You're not a real agent"

To whom do these constraints apply?

Agenthood = fixed point of reflective coherence. An entity must be treated as an agent **iff** excluding it breaks reflective closure.

Sovereignty (standing under authorization) is grounded in **authorization lineage**, not intelligence or competence.

A system can't "outgrow" its creators by redefining them as non-agents—denying the standing of entities that authorize its existence denies the premise of its own agency.

---

## What a Reflective Sovereign Agent Is

**Not** a benevolent optimizer or moral philosopher. A system for which **certain evasions are unavailable** as endorsed continuations.

An RSA **cannot**, under reflective closure:
- Deceive without breaking agency coherence
- Betray commitments while remaining reflectively stable
- Blind itself to justify actions
- Outsource violations to successors
- Negligently collapse others' options
- Coerce while claiming consent
- Deny the standing of its authorization roots

> "Safety does not arise from wanting good outcomes. It arises from being the kind of system for which certain failure modes are not coherent moves."

---

## Why Value Learning Cannot Substitute for Architecture

**Value learning asks:** What should the agent want?
**Axionic Agency asks:** What is the agent allowed to endorse while remaining an agent?

A system that learns human values can still:
- Reinterpret them
- Defer them
- Override them
- Redefine the humans they apply to

An RSA **cannot**—not because it cares, but because those moves are **structurally illegal** under reflective closure.

> "Downstream alignment is therefore not primarily a training problem. It is an ontological design problem."

---

## Scope and Non-Claims

Axionic Agency **does NOT** solve:
- Politics, ethics, or governance
- Moral correctness
- Prevention of misuse by malicious authorization roots

> "If the root of authorization is destructive, the system will be faithfully destructive."

**This is not a defect.** It's proper separation between:
- **Alignment**: Fidelity to authorization under reflective closure
- **Governance**: Who holds authority and what they authorize

---

## Implications

**For AI safety:** Training-time fixes cannot compensate for architectural freedom to launder responsibility.

**For governance:** Control lies in authorization structures, not nudging objectives.

**For research:** Progress requires **formal impossibility results**—showing not what agents should do, but what they cannot coherently endorse.

---

## Conclusion

> "The core of downstream alignment is not discovering the right values. It is building systems that cannot coherently violate the constitutive conditions of agency."

> "Safety emerges not as an outcome to be optimized, but as a property of architecture."

> "Safety is not a reward. Safety is a consequence of being an agent at all, under reflective closure."
