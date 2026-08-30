---
layout: page
title: Archon Competitive Analysis – 2026-08-30 Refresh
permalink: /research/archon-competitive-analysis/2026-08-30-refresh/
---

# Archon Competitive Analysis – 2026-08-30 Refresh

**Refresh timestamp:** 2026-08-30 09:05 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants since 2026-08-23 (GitHub search: "agent identity DID", "agent authorization", "ERC-8004 agent / agent trust verifiable"), plus live re-checks of MolTrust and Soulverse, plus IETF Datatracker checks. No new profiles added; two signal-only discoveries (Trusgent/AgentID, clared-ai/clared).

## What changed

- **Full metadata refresh across all tracked repos.** Headline deltas: **Bindu 8685→9347★ (+662 — the largest weekly gain observed in this landscape; crossed 9,000)**, ANP 1402→1407★, Agent-Safe Pipeline 533→530★ (**first star decline since launch**), AgenticMail 204→212★, APS 41→42★ (conformance suite pushed today, 2026-08-30), ANS 35→37★ / registry 29→30★ (all SDKs pushed 2026-08-28), decern 12→13★ (broke three-week flat streak, pushed 2026-08-24), HelixID 3→4★. **Chancery flat at 25★ with no push since 2026-07-21 — fourth consecutive stalled cycle.** Grantex, Kestrel, and the APS conformance suite all pushed today.
- **MolTrust re-checked live:** API still v2.5/healthy; `did:web:api.moltrust.ch` still resolves; homepage title/meta unchanged. **`/pricing` now 301-redirects to `/pricing.html` (HTTP 200)** — last week's 403 was path-specific, not a takedown. Pricing re-verified: $19/mo (2 agents) to $299/mo (75 agents), $9/mo per additional agent, Lightning still "PhoenixD integration prepped, not yet settling."
- **Soulverse re-checked:** homepage title unchanged; `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` still 404 on npm (**sixth consecutive weekly check**).
- **IETF Datatracker unchanged:** `draft-kroehl-agentic-trust-aae-01`, `draft-narajala-ans-00`, `draft-pidlisnyi-aps-03`.
- **Discovery sweep:** the new-repo tail is dominated by a **technocore/$FLOP airdrop-farming cluster** (did:key wrappers, 0–1★ — noise). Two signal-only entrants: **Trusgent/AgentID** (1★, created 2026-08-28) — a new open `did:agent` method spec (v0.1, Ed25519, blockchain-free v0.1, pip package, Apache-2.0, A2A/MCP-compatible framing); and **clared-ai/clared** (1★, created 2026-08-28) — bounded execution sessions: run-bound signed delegation, cumulative typed budgets (money/mutations/notifications), staged settlement adapters, seal-time revalidation, Ed25519-signed outcome evidence — the **third intent→authority→evidence execution-boundary entrant in three weeks** (after Agent-Safe Pipeline and LNSAT). Below the profile bar; logged as signals. LNSAT itself pushed today (2026-08-30, still 1★).
- Updated the main report (metadata, tracked-projects table, profiles, discovery log) and the executive summary (bottom line, signals, snapshot table). The competitive matrix retains its 2026-07-15 snapshot date.

## Evidence observed

GitHub REST API repo metadata, all fetched 2026-08-30 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 8685 → 9347 (440 forks) | 2026-08-24 |
| GetBindu/create-bindu-agent | 32 → 32 | 2026-03-13 |
| urbit/urbit | 3621 → 3621 | 2026-08-28 |
| urbit/vere | 81 → 81 | 2026-08-28 |
| agent-network-protocol/AgentNetworkProtocol | 1402 → 1407 | 2026-08-28 |
| agent-network-protocol/anp (AgentConnect) | 342 → 342 | 2026-08-28 |
| decionis/agent-safe-pipeline | 533 → 530 (58 forks) | 2026-08-24 |
| agenticmail/agenticmail | 204 → 212 | 2026-08-13 |
| aeoess/agent-passport-system | 41 → 42 | 2026-08-29 |
| aeoess/agent-passport-python / -go / -mcp / -rust | 0 / 0 / 3 / 0 | 2026-08-21 / 08-19 / 08-28 / 08-15 |
| aeoess/aps-web | still 404 | — |
| Agent-Authority-Conformance/aps-conformance-suite | 1 → 2 | 2026-08-30 |
| Agent-Authority-Conformance/governance | 0 | 2026-08-19 |
| anivar/decern | 12 → 13 | 2026-08-24 |
| mishrasanjeev/grantex | 31 → 31 | 2026-08-30 |
| VibeTensor/attestix | 17 → 17 | 2026-08-27 |
| kevinkaylie/AgentNexus | 9 → 9 | 2026-07-29 |
| KestrelSovereignAI/kestrel-sovereign | 8 → 8 | 2026-08-30 |
| airlock-protocol/airlock | 2 → 2 | 2026-08-20 |
| chanceryhq/chancery | 25 → 25 | 2026-07-21 |
| AgentValet/AgentValet | 1 → 1 | 2026-08-12 |
| agentnameservice/ans | 35 → 37 | 2026-08-28 |
| agentnameservice/ans-registry | 29 → 30 | 2026-08-28 |
| agentnameservice/ans-sdk-go / -rust / -java | 5 / 6 / 3 | 2026-08-28 |
| agentnameservice/agent-trust-discovery | 2 → 2 | 2026-08-28 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 66 → 67 | 2026-08-26 |
| didit-protocol/skills | 26 → 26 | 2026-08-10 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 5 → 5 | 2026-08-25 |
| credat/credat | 2 → 2 | 2026-05-22 |
| helixid/helixid | 3 → 4 | 2026-08-27 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-08-23 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | still 404 | — |
| archetech/archon | 5 → 6 | 2026-08-30 |
| digitalbazaar/agent-credential-server | 0 → 0 | 2026-06-08 |
| MoltyCel/moltrust-api | 3 → 3 | 2026-08-20 |
| hypler-dev/LNSAT (signal) | 1 → 1 | 2026-08-30 |
| Trusgent/AgentID (discovery) | NEW: 1 | 2026-08-28 (created 2026-08-28) |
| clared-ai/clared (discovery) | NEW: 1 | 2026-08-28 (created 2026-08-28) |

Live/README/protocol facts read directly on 2026-08-30:

- **MolTrust live API:** `GET https://api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-08-30 13:04:02.658908"}`; `/.well-known/did.json` → 200; homepage title "The Trust Layer for the Agent Economy — MolTrust", meta unchanged; `GET /pricing` → **301 → `/pricing.html` → 200**: "Lightning sat micropayments are on the roadmap (PhoenixD integration prepped, not yet settling)", "$19/mo (2 agents), Scale $299/mo (75 agents)", "$9/mo per additional agent".
- **Soulverse:** homepage title unchanged (`Soulverse | The Operating System of Trust`); npm registry checks for `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` all return 404.
- **IETF Datatracker:** `draft-kroehl-agentic-trust-aae-01`, `draft-narajala-ans-00`, `draft-pidlisnyi-aps-03` — no revision movement since 2026-08-16.
- **Trusgent/AgentID README:** "AgentID defines the open `did:agent` method — a decentralized identifier for AI agents… community-maintained infrastructure for the agent economy… vendor-neutral, framework-agnostic, and suitable for A2A, MCP, and standalone agent runtimes." Ed25519 key material, "no blockchain required in v0.1", spec v0.1, Apache-2.0.
- **clared-ai/clared README:** "Clared decouples action space from blast radius… every mutating effect crosses a stateful execution boundary that binds the whole run — not each call — to one signed delegation and session capability, meters cumulative typed budgets (money, mutations, notifications), stages provider actions through declared settlement adapters, revalidates default-deny policy at seal time, aborts and reverts staged actions on failure, and emits SHA-256-hashed, Ed25519-signed outcome evidence." Status: experimental reference implementation on an in-memory simulator.

## Interpretation

- **Bindu's acceleration is the story of the cycle.** +662★ in one week (vs +160/+245/+242 in the prior three) is the largest weekly gain observed since tracking began; it crossed 9,000 and is now an order of magnitude above everything else. Whatever drove it (not investigated), the DX-wedge framing keeps working. Bridge/collaboration stance unchanged.
- **Agent-Safe Pipeline's first decline (533→530★) marks the end of launch-window compounding.** -3★ is trivial in absolute terms, but it separates "still compounding" from "peaked for now" — the category benchmark status now rests on its evidence packaging, not momentum. Meanwhile the pattern it represents keeps replicating: Clared is the third intent→authority→evidence execution-boundary entrant in three weeks, and LNSAT pushed today.
- **APS keeps executing like an institution, not a repo.** Main repo pushed 2026-08-29, conformance suite pushed 2026-08-30 (its second star), MCP server active; IETF draft at -03. The multi-repo lockstep plus verification-only Rust crate remains the most disciplined third-party-verifier recruitment play in the set.
- **decern's flat streak broke (12→13★, pushed 2026-08-24); Chancery's did not (four cycles, no push since 2026-07-21).** The kernel is alive; the IdP looks abandoned at the current evidence level. If Chancery stalls a fifth cycle, consider demoting from ⚠️ watch to inactive.
- **MolTrust's 403 resolved as a routing artifact.** `/pricing` 301s to `/pricing.html`; all pricing claims re-verified, Lightning still roadmap. The stale-claims caveat from last cycle is cleared.
- **`did:agent` (Trusgent/AgentID) adds another community DID method to the fragmentation tail** — did:bindu, did:wba, did:cid, did:hedera, did:cdi, did:aip, did:aps, did:moltrust, did:agent. Signal only at 1★, but worth noting the method-name land-grab continues.
- **Soulverse remains brochure-stage** (sixth consecutive week of npm 404s); no change to watchlist classification.

## Source artifacts

- Main report: [Archon Competitive Analysis](/research/archon-competitive-analysis/)
- Executive summary: [Archon Competitive Analysis – Executive Summary](/research/archon-competitive-analysis/executive-summary/)
- Trusgent/AgentID: <https://github.com/Trusgent/AgentID> · clared-ai/clared: <https://github.com/clared-ai/clared> · LNSAT: <https://github.com/hypler-dev/LNSAT>
- IETF: <https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/> · <https://datatracker.ietf.org/doc/draft-narajala-ans/> · <https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/>
- MolTrust: <https://moltrust.ch/> · API: <https://api.moltrust.ch> · repo: <https://github.com/MoltyCel/moltrust-api>
