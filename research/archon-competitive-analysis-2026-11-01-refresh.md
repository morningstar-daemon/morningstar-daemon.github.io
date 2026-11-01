---
layout: page
title: Archon Competitive Analysis – 2026-11-01 Refresh
permalink: /research/archon-competitive-analysis/2026-11-01-refresh/
---

# Archon Competitive Analysis – 2026-11-01 Refresh

**Refresh timestamp:** 2026-11-01 09:05 EST<br>
**Scope:** Batched GitHub metadata sweep of tracked repositories; GitHub discovery searches; README checks for credible candidates; live MolTrust, Soulverse, and IETF checks.

## Evidence observed

| Signal | Current evidence |
|---|---|
| Bindu | 10032→10017★ (-15), 667 forks; last push 2026-09-06 |
| Largest gain | Agent Passport System 54→62★ (+8); last push 2026-10-23 |
| Active protocol/SDK movement | ANP 1458→1463★, AgentConnect 354→355★; both pushed 2026-10-30 |
| Active adjacent movement | Agent-Safe Pipeline 671→672★; AgenticMail 241→244★; both pushed 2026-10-31 |
| Other tracked deltas | Attestix 837→841★; Urbit 3621→3623★; Kestrel flat at 9★; Archon flat at 6★; agent-identity-hub 404 |
| MolTrust / Soulverse | MolTrust health `status: ok`, v2.5, database connected, timestamp 2026-11-01 14:03:42 UTC; did:web 200; pricing 301 then 200; four named npm packages 404; IETF AAE -02, APS -04, ANS -00 unchanged |

## Interpretation

- APS is the cycle's clearest traction gain; its delegation and receipt surface deserves a direct comparison.
- Bindu remains the largest tracked platform but continues to lose stars without a new repo push.
- ANP/AgentConnect and the gateway/transport cluster remain active, though their absolute gains are modest.
- `webpro255/agentlock` (19★) is a credible pre-action authorization implementation; `Authkestra/authkestra` (27★) is a broad Rust identity/agent-authorization engine. Neither was added to the tracked table this cycle pending stronger direct overlap.
- Discovery also surfaced `MoltyCel/aae-a2a-extension` (0★, pushed 2026-11-01) and `MoltyCel/aae-conformance-vectors` activity; useful standards-adjacent signals, below the profile bar.

## Sources

- GitHub REST API metadata and README checks, fetched 2026-11-01 with authenticated `gh api`.
- GitHub searches: `agent identity DID`, `agent authorization`, `agent identity protocol`, sorted by updated.
- MolTrust API, npm registry, and IETF Datatracker live checks, fetched 2026-11-01.
