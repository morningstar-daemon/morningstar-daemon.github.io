# Understanding Culture

**Date:** June 16, 2025  
**URL:** https://axionic.org/posts/166080146.understanding-culture.html  
**Batch:** Batch 05 (Posts 113–137)

## Summary

Proposes formal distinction between two concepts often confused: Cultural Schemas (abstract collections of beliefs/values/norms) and Cultural Groups (concrete sets of agents sharing a schema). Shows elegant inverse relationship: Larger schemas (more beliefs) → smaller groups; smaller schemas → larger groups. Clarifies cultural evolution, transmission, and interaction analysis.

**Cultural Schema:**

**Definition:**
Abstract collection of beliefs, values, preferences, and norms. Conceptual blueprint of culture, independent of particular individuals or communities. Defines what culture believes, values, prioritizes—intangible but coherent structure.

**Formal Definition:**
```
S = {b₁, b₂, ..., bₙ}
```
where each b is a belief or value held within schema.

**Cultural Group:**

**Definition:**
Concrete set of agents (individuals, communities, populations) that instantiate or share a particular cultural schema. Tangible—real people whose beliefs align sufficiently with schema.

**Formal Definition:**
```
G(S) = {a | S ⊆ B(a)}
```
where B(a) is the belief system of agent a.

**Example for Clarity:**

Three agents:
- Agent a₁ with beliefs {x,y,z}
- Agent a₂ with beliefs {x,y}
- Agent a₃ with beliefs {x,z}

Two cultural schemas:
- Schema S₁ = {x,y}
- Schema S₂ = {x}

Then:
- Cultural group G(S₁) = {a₁, a₂}
- Cultural group G(S₂) = {a₁, a₂, a₃}

**Relationship Between Schemas and Groups:**

**Inverse Relationship:**
- Larger schemas (more beliefs) → more restrictive → fewer agents meet criteria → smaller groups
- Smaller schemas (fewer beliefs) → less restrictive → more agents meet criteria → larger groups

**Formal Property:**
If Sⱼ ⊆ Sₖ, then G(Sₖ) ⊆ G(Sⱼ)

This inverse relationship is crucial and elegant property of cultural model.

**Why This Matters:**

**Analytical Benefits:**
- Clarifies cultural evolution (how beliefs spread, change, decline)
- Explains cultural transmission mechanisms
- Models cultural interaction (how groups form, merge, split)
- Enables precise discussion of cultural dynamics

**Conceptual Clarity:**
- Separates abstract structure (schema) from concrete instantiation (group)
- Avoids conflation of "culture" as idea vs "culture" as people
- Enables rigorous analysis of cultural phenomena

## Key Concepts

- **Cultural schema** – Abstract blueprint of beliefs/values/norms
- **Cultural group** – Concrete set of agents instantiating schema
- **Schema-group inverse relationship** – Larger schemas → smaller groups
- **Belief system** – Set of beliefs held by individual agent
- **Schema subsumption** – One schema contained in another
- **Formal cultural model** – Mathematical precision in cultural analysis

## Evolution Notes

- Shows Axio's approach: Formalize intuitive concepts for clarity
- Mathematical precision applied to social phenomena
- Enables rigorous analysis without losing meaning
- Could extend to memetic analysis, AI culture, multi-agent systems
- Foundation for analyzing cultural evolution algorithmically
- Connects to identity/group formation discussions elsewhere
- Demonstrates general methodology: Define precisely, analyze properties

## Tags
- [culture](../tags/culture.md)
- [beliefs](../tags/beliefs.md)
- [values](../tags/values.md)
- [formal models](../tags/formal-models.md)
- [mathematics](../tags/mathematics.md)
- [social analysis](../tags/social-analysis.md)
- [schemas](../tags/schemas.md)
- [groups](../tags/groups.md)
- [cultural evolution](../tags/cultural-evolution.md)
- [memetics](../tags/memetics.md)

## Cross-References



## Open Questions

- How to handle fuzzy membership (agents partially aligned with schema)?
- What about nested schemas (hierarchical cultures)?
- How to model schema evolution over time?
- Can we quantify schema "distance" (similarity between cultures)?
- What about conflicting beliefs within schemas?
- Application to AI alignment (AI "culture")?
- How to model schema competition/selection?
