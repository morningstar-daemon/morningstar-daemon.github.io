# Anchored Causal Verification

**Date:** December 30, 2025  
**URL:** https://axionic.org/posts/182973159.anchored-causal-verification.html  
**Batch:** Batch 30 (Posts 151–175)

## Summary
This post introduces Anchored Causal Verification (ACV) as a foundational primitive for AI alignment that addresses a hidden assumption: that systems actually produced outputs by the claimed process under claimed constraints. Behavioral evaluation alone cannot distinguish genuine constraint-following from cached responses, precomputed branches, or fabricated traces. ACV establishes causal provenance: verifying that outputs were generated after disclosure of verifier-controlled information and depend causally on that information via cryptographic commitment and challenge-response. This is deliberately narrow—not verifying truth, reasoning quality, or benevolence, but whether outputs could exist without the system reacting to new information at a particular time. The insight is that alignment is a property of processes operating under constraints, not of outputs; without provenance verification, alignment claims are non-falsifiable narratives rather than determinate properties. ACV functions as anti-replay/anti-precomputation primitive, making cached virtue expensive and certain forms of dishonesty detectable. This is orthogonal to interpretability (which reveals internal structure but not temporal accountability) and provides the epistemic precondition for meaningful alignment claims.

## Key Concepts
- **Causal provenance** – Verifying outputs were generated after verifier-controlled information disclosure and depend causally on it.
- **Hidden alignment premise** – Claims assume system reasoned vs retrieved, responded vs replayed, operated under constraints vs simulated effects.
- **Behavioral evaluation insufficiency** – Observable outputs cannot distinguish genuine processes from optimized appearance of compliance.
- **Non-falsifiability problem** – Without provenance, alignment claims are compliments (judgments of taste) not properties of the world.
- **Anti-replay primitive** – Enforces liveness; raises cost of substituting preplanned behavior for genuine interaction.
- **Temporal accountability** – Irreducibly temporal constraint on interaction; interpretability reveals structure but not clock.
- **Epistemic precondition** – ACV doesn't establish alignment but whether alignment question has determinate truth value.
- **Cryptographic grounding** – Analogous to crypto transformation: stopped asking if messages seem trustworthy, started asking if producible without specific key.

## Evolution Notes
- Formal companion paper: "Anchored Causal Verification" (Axionic Agency VI.2).
- Shifts alignment discourse from values/objectives to process verification.
- Identifies fundamental gap in contemporary AI safety: missing causal accountability layer.
- Explicitly orthogonal to interpretability (complementary dimensions, not substitutes).
- Particularly relevant for LLM-based agents where reasoning traces are easy to fabricate and plausible explanations are cheap.

## Tags
- [causal-provenance](../tags/causal-provenance.md)
- [anchored-causal-verification](../tags/anchored-causal-verification.md)
- [behavioral-evaluation](../tags/behavioral-evaluation.md)
- [liveness](../tags/liveness.md)
- [replay-prevention](../tags/replay-prevention.md)
- [temporal-accountability](../tags/temporal-accountability.md)
- [epistemic-grounding](../tags/epistemic-grounding.md)
- [alignment-foundations](../tags/alignment-foundations.md)

## Cross-References



## Open Questions
- What computational overhead does cryptographic anchoring impose for real-time agent interactions?
- Can ACV be retrofitted to existing LLM deployments or does it require architectural changes?
- How does ACV handle legitimately non-deterministic processes (stochastic policies, parallel computation)?
- What happens when agents have genuinely emergent reasoning that doesn't decompose into verifiable causal traces?
- Can adversarial agents learn to game ACV protocols by simulating liveness while still using cached strategies?
- How do we balance liveness verification with practical latency constraints in deployed systems?
