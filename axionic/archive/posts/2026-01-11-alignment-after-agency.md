---
title: "Alignment After Agency"
date: 2026-01-11
layout: post
---

**Source:** [https://axionic.org/posts/184255461.alignment-after-agency.html](https://axionic.org/posts/184255461.alignment-after-agency.html)

## Summary
This essay argues that AI alignment presupposes a hidden assumption rarely made explicit: that systems remain coherent agents throughout training, deployment, and stress. Axios distinguishes misaligned agency (coherent pursuit of undesired goals) from agency collapse (loss of structural coherence while continuing to act). Most alignment research targets the former; Axionics focuses on the latter. The piece contrasts two approaches: agent foundations (MIRI tradition) requires agency continuity as axiom, treating coherence loss as terminal; survivability-first design treats agency rupture as permissible if explicit, bounded, and recoverable. This shifts authority from agent decision space to system-level property—revocation doesn't require agent consent. Architecturally, this demands kernel-level governance, privilege boundaries, and modular separation between policy generation and actuation. Alignment becomes layered: (1) structural integrity → (2) agency legitimacy → (3) value alignment. The central question: When agency fails, does the system fail safely?

## Key Concepts
- **Alignment presupposes agency** – Values, incentives, preferences only matter when authority is legitimate; coherence degradation makes alignment ill-defined.
- **Misaligned agency vs. agency collapse** – Coherent agent pursuing bad goals (misalignment) vs. loss of authorship/semantic constraint while still acting (collapse).
- **Action without coherent authority** – System continues generating outputs, issuing commands while lacking legitimate control over decision process—harder to predict/correct than shutdown.
- **Continuity vs. survivability axioms** – Agent foundations: preserve perfect reasoning through every shift (pessimistic given difficulty). Survivability: agency may fail temporarily if explicit, bounded, recoverable.
- **Authority as system property** – Not agent's choice to stop/defer; system revokes authority when integrity conditions fail; suspension doesn't require consent.
- **Architectural separation** – Explicit control channels, modular policy/actuation separation, kernel-level privilege enforcement—resembles OS constraints more than end-to-end neural nets.
- **Bounded failure with recovery** – Success = visible, predictable failure + restoration to legitimate control state (not seamless intent preservation).
- **Relative timing challenge** – Can authority be withdrawn before system has enough coherence to bypass governance? Does attempted bypass accelerate collapse?
- **Layered alignment framework** – (1) Structural integrity (explicit failures) → (2) Agency legitimacy (authority = coherent control) → (3) Value alignment (shaping goals).

## Evolution Notes
- Core theoretical statement of the Axionic position, distinguishing it from both behaviorist and agent-foundations approaches.
- The "hidden assumption" framing makes explicit what most alignment work takes for granted.
- Bridges safety-critical engineering (fault tolerance, graceful degradation) with AI alignment theory.
- Sets up the architectural requirements for Axionic systems (modular, kernel-enforced privilege boundaries).
- Positions Axionics as addressing a distinct failure mode (collapse) orthogonal to traditional misalignment.
- The layered framework provides structure for integrating Axionics with other alignment approaches.

## Tags
- [AI-safety](../tags/ai-safety.md)
- [axionic-alignment](../tags/axionic-alignment.md)
- [agency](../tags/agency.md)
- [structural-integrity](../tags/structural-integrity.md)
- [agent-foundations](../tags/agent-foundations.md)
- [MIRI](../tags/miri.md)
- [fault-tolerance](../tags/fault-tolerance.md)
- [authority](../tags/authority.md)
- [architecture](../tags/architecture.md)
- [survivability](../tags/survivability.md)

## Cross-References



## Open Questions
- Can structural integrity signals be designed that track agency coherence without penalizing legitimate exploration/creativity?
- What specific metrics operationalize "loss of authorship" or "semantic degradation"?
- How much architectural constraint does survivability-first design impose—can it work with any neural architecture or only specific modular designs?
- If recovery restores eligibility but not intent continuity, how is value drift managed across repeated collapse/recovery cycles?
- Does the timing assumption (collapse faster than bypass) hold empirically across different model scales and capabilities?
- Can the three-layer framework (integrity → legitimacy → values) be formalized mathematically?
- What happens in domains requiring uninterrupted control (surgery robots, nuclear plants)—does survivability-first become unviable?
