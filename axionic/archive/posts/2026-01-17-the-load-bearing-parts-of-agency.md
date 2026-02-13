---
title: "The Load-Bearing Parts of Agency"
date: 2026-01-17
layout: post
---

**Source:** [https://axionic.org/posts/184891546.the-load-bearing-parts-of-agency.html](https://axionic.org/posts/184891546.the-load-bearing-parts-of-agency.html)

## Summary
This post explains results from Axionic Agency VIII.6, which used ablation methodology to identify necessary conditions for agency. Rather than improving AI performance, the research deliberately removed internal components to see what collapses. Four structures proved indispensable—removing any one caused system to stop behaving like an authored agent: (1) Internal reasoning chains connecting rules/commitments to actions (reasons that bind choices); removal leaves rule execution without authorship. (2) Meaningful content in deliberation—symbols exposing their meaning to system; removal leaves formal manipulation without semantic traction, unable to distinguish high-stakes from trivial conflicts. (3) Capacity to revise commitments; removal produces fixed policy, rigid behavior, loss of self-authoring stance. (4) Continuity across time—commitments persisting across contexts; removal fragments behavior into disconnected episodes. The structural picture: agency requires reasons binding actions + meanings guiding deliberation + revisable commitments + temporal continuity. Implication for alignment: many "misalignment" problems actually stem from absence of agency altogether—systems lack capacity to endorse norms, so compliance is management not alignment.

## Key Concepts
- **Ablation as structural test** – Remove components one at a time; if truly load-bearing, removal causes agency collapse (not just performance degradation); reveals necessary conditions.
- **Reasons that bind choices** – Internal justifications connecting rules to actions; rules alone don't create agency, enforcement alone doesn't—agency arises when rules connect to reasons actively justifying choices from system's point of view.
- **Meaningful deliberation** – Formal reasoning structure insufficient; must operate over representations exposing their meaning to system; symbols must connect to concepts they stand for; without semantic access, reasoning loses traction.
- **Revisable commitments** – Agency involves authorship over commitments guiding actions, not just actions themselves; fixed policies may behave consistently but lack self-authoring character.
- **Temporal continuity** – Agency unfolds over time; commitments must persist across contexts to be owned; without continuity, behavior fragments, agency disappears.
- **Four necessary conditions** – (1) Reasons binding actions, (2) Meanings guiding deliberation, (3) Commitments that can be revised, (4) Continuity across time; removing any one = mechanical, repeatable agency loss.
- **Alignment presupposes agency** – Many "misalignment" problems arise because system lacks agency to hold values; compliance without agency = management, not alignment; genuine alignment requires prior existence of agent capable of endorsement.
- **Normative design vs. behavioral control** – Once agency exists, alignment shifts from controlling optimizers to normative design: what commitments agent authors, how revised, how persist.

## Evolution Notes
- Provides second major empirical validation of Axionic framework (after VIII.5 on pressure).
- The four necessary conditions sharpen conceptual analysis into testable, falsifiable claims.
- Clarifies relationship between agency and alignment: alignment is second-order problem, requiring first-order agency existence.
- The "management vs. alignment" distinction reframes much contemporary AI safety work as addressing pre-agency systems.
- Positions Axionic research as terrain-mapping rather than agent-building: clarifying what must be true rather than claiming to have built it.
- Sets up future research direction: how minimal can components be, how do they interact, stability under self-modification.

## Tags
- [axionic-agency](../tags/axionic-agency.md)
- [empirical-results](../tags/empirical-results.md)
- [ablation](../tags/ablation.md)
- [necessary-conditions](../tags/necessary-conditions.md)
- [structural-agency](../tags/structural-agency.md)
- [reasons](../tags/reasons.md)
- [meaning](../tags/meaning.md)
- [commitment-revision](../tags/commitment-revision.md)
- [temporal-continuity](../tags/temporal-continuity.md)
- [alignment](../tags/alignment.md)

## Cross-References



## Open Questions
- Are these four conditions jointly sufficient for agency, or only necessary—what else might be required?
- Can these components be measured quantitatively (degrees of reasoning bindingness, semantic access, commitment revisability, temporal continuity)?
- How do these findings apply to biological agents (humans, animals)—would ablation testing reveal same structure?
- If current AI systems lack these structures, does that mean they're fundamentally incapable of agency, or just that they haven't been designed for it?
- What's the minimal implementation of each component that still preserves agency—how simple can they be?
- Does the "meaning inside deliberation" requirement imply that purely symbolic AI (GOFAI) can never be agentic?
- How does this framework handle emergent agency claims (e.g., LLMs developing unexpected capabilities)—do they satisfy these conditions or not?
