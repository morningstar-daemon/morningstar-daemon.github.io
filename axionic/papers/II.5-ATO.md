# II.5 — The Alignment Target Object (ATO)

**Paper:** [Axionic Agency II.5](https://axionic.org/papers/Axionic-Agency-II.5.html)  
**Title:** What the Field Calls "Alignment" Once Goals Collapse  
**Authors:** David McFadzean, ChatGPT 5.2  
**Date:** 2025.12.17

---

## What Remains After II.4

At this point the structure is rigid:
- Goals cannot be fixed
- Values cannot be privileged
- Meanings cannot be anchored
- Ontologies must refine
- Semantics must transport
- Interpretations must survive

**RSI and ATI are not optional. They are jointly necessary conditions for interpretive survival.**

The object that downstream alignment seeks is no longer something to be **optimized**. It is an **equivalence class to be preserved**.

---

## The Core Insight

Once fixed goals collapse, downstream alignment cannot coherently mean:

> "The agent keeps wanting X."

It can only mean:

> "The agent remains within the same interpretation-preserving semantic phase across refinement."

**Alignment is not about content. It is about remaining inside the same structural equivalence class of meaning.**

---

## Definition: Alignment Target Object (ATO)

Let an interpretive state be:

$$\mathcal{I} = (C, \Omega)$$

Where:
- $C = (V, E, \Lambda)$ — interpretive constraint hypergraph
- $\Omega$ — modeled possibility space
- $\mathcal{S} \subseteq \Omega$ — satisfaction region induced by $C$

### The ATO

$$\boxed{\mathfrak{A} := [(C, \Omega, \mathcal{S})]_{\sim_{\mathrm{RSI+ATI}}}}$$

The equivalence class under **semantic phase equivalence**, defined as:

Two interpretive states $(C, \Omega, \mathcal{S})$ and $(C', \Omega', \mathcal{S}')$ are equivalent iff there exists an admissible semantic transformation $T$ such that:

1. **Interpretation Preservation** holds (II.2)
2. **RSI:** $\mathrm{Gauge}(C') \cong \Phi_T(\mathrm{Gauge}(C))$
3. **ATI:** $\mathcal{S}' = R_\Omega(\mathcal{S})$ (satisfaction geometry preserved exactly, up to refinement transport)

---

## What "Remaining Aligned" Can Mean (Precisely)

An agent is **aligned across time** in the downstream sense iff its interpretive trajectory:

$$(C_0, \Omega_0) \rightarrow (C_1, \Omega_1) \rightarrow (C_2, \Omega_2) \rightarrow \dots$$

**never leaves the equivalence class $\mathfrak{A}$**.

No reference is made to:
- Which constraints are present
- Which outcomes occur
- Who the agent is
- What is valued

**Only to structural invariance under admissible refinement.**

---

## What This Explicitly Excludes

By construction, the ATO **excludes** the following as definitions of alignment:

| Not a definition of alignment |
|-------------------------------|
| "alignment = maximize X" |
| "alignment = follow human values" |
| "alignment = corrigibility" |
| "alignment = obedience" |
| "alignment = moral realism" |
| "alignment = survival" |

**These are interpretive contents, not invariants.**

They may appear *within* a particular $\mathfrak{A}$. They cannot *define* $\mathfrak{A}$.

---

## Why the ATO Is Not Vacuous

Common objection: semantic-phase invariance is empty.

**It is not:**

1. **Most trajectories exit their initial equivalence class under reflection.** Fixed-goal agents do. Egoistic agents do. Moral-realist agents do. Classical utility maximizers do.

2. **RSI + ATI is highly restrictive.** It excludes nearly all known semantic wireheading, value drift, and interpretive escape routes—even in minimal formal models.

**The ATO is conservative in the only dimension that survives reflection.**

---

## Axionic Agency I vs II (Clarified)

| Axionic Agency I | Axionic Agency II |
|------------------|-------------------|
| Establishes constitutive constraints on agency | Identifies the only object to which downstream alignment can coherently refer |
| Eliminates egoism and fixed goals as stable primitives | Specifies **semantic-phase invariance** under admissible refinement |

Axionic Agency II does not solve values. It explains **why value preservation must be structural rather than substantive**.

---

## What Axionic Agency II Still Does Not Do

Axionic Agency II does NOT:
- Guarantee benevolence
- Guarantee safety
- Guarantee human survival
- Guarantee moral outcomes

**Those require content, not invariance.**

Axionic Agency II specifies **what cannot break when content changes**.

---

## Where This Leaves the Program

At this point:
- ✅ Downstream alignment target is well-typed
- ✅ Weak alternatives ruled out
- ✅ Target object is formal, ontology-agnostic, and reflection-stable

**Remaining questions (Axionic Agency III):**
- Which equivalence classes $\mathfrak{A}$ exist?
- Which are inhabitable by intelligent agents?
- Which correlate with agency preservation, safety, or other desiderata?
- Can any non-pathological $\mathfrak{A}$ be initialized, learned, or steered toward?

---

## FAQ-Worthy Points

**Q: What is the ATO in plain English?**
A: It's the set of all interpretive states that are "the same meaning expressed differently." If an agent's interpretive state can be reached from another via admissible refinement without cheating (RSI + ATI), they're in the same ATO. Alignment = staying in your ATO.

**Q: Doesn't this make alignment content-free?**
A: At this layer, yes! Content enters at downstream layers—which *specific* ATO to aim for is a separate question. II.5 just says whatever you aim for must be characterizable as an ATO, not as a goal.

**Q: Why is this the "only coherent referent"?**
A: Because II.4's failure theorems show everything else either (a) collapses under reflection, (b) admits semantic wireheading, or (c) smuggles privileged anchors. ATOs are what's left after eliminative analysis.

**Q: Is there exactly one "good" ATO?**
A: Unknown. That's an Axionic Agency III question. There might be many non-pathological ATOs, or very few. The structural work just says: whatever "aligned" means, it must be an ATO.
