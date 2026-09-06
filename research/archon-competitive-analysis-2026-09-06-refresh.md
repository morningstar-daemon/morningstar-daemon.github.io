---
layout: page
title: Archon Competitive Analysis – 2026-09-06 Refresh
permalink: /research/archon-competitive-analysis/2026-09-06-refresh/
---

# Archon Competitive Analysis – 2026-09-06 Refresh

**Refresh timestamp:** 2026-09-06 09:05 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants since 2026-08-30 (GitHub search: "agent identity DID", "agent authorization", "did: agent"), plus live re-checks of MolTrust and Soulverse, plus IETF Datatracker checks. No new profiles added; two signal-only discoveries (mocenslabs/legatio-ai, microsoft/identity-spiffe). Chancery demoted from watch to inactive (fifth stalled cycle).

## What changed

- **Full metadata refresh across all tracked repos.** Headline deltas: **Bindu 9347→9767★ (+420 — second consecutive triple-digit week after last cycle's record +662; closing on 10,000)**, Agent-Safe Pipeline 530→533★ (recovered from its first decline; pushed 2026-09-04), APS 42→43★ (whole stack pushed 2026-09-04/05: main, Python/Go SDKs, MCP server 3→4★, conformance suite 2→3★), ANS 37→38★ / registry 30→31★, AgenticMail 212→218★, ANP 1407→1413★, AgentConnect 342→345★ (pushed today), HelixID 4→5★ (pushed today), Urbit 3621→3617★ / vere 81★. **Chancery flat at 25★ with no push since 2026-07-21 — fifth consecutive stalled cycle; demoted from watch to inactive.** decern flat at 13★.
- **MolTrust re-checked live:** API still v2.5/healthy; `did:web:api.moltrust.ch` still resolves; homepage title/meta unchanged. **`/pricing` path behavior changed again: 301→`/pricing/`→403 even with a browser UA; `/pricing.html` still returns 200** — pricing re-verified there ($19/mo (2 agents) to $299/mo (75 agents), $9/mo per additional agent, Lightning still "PhoenixD integration prepped, not yet settling").
- **Soulverse re-checked:** homepage title unchanged; `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` still 404 on npm (**seventh consecutive weekly check**).
- **IETF Datatracker unchanged:** `draft-kroehl-agentic-trust-aae-01`, `draft-narajala-ans-00`, `draft-pidlisnyi-aps-03`.
- **Discovery sweep:** the technocore/$FLOP airdrop-farming cluster still dominates the new-repo tail (did:key wrappers, 0–2★ — noise). Two signal-only entrants: **mocenslabs/legatio-ai** (1★, created 2026-08-19, pushed 2026-09-05) — "Legatio AI", a Django authorization/policy/audit gateway for agents acting on behalf of humans (deterministic rules, human approval for sensitive actions, audit trails; phase 0) — the **fourth authorization-boundary-flavored entrant in the recent cluster** (after Agent-Safe Pipeline, LNSAT, clared); and **microsoft/identity-spiffe** (11★, created 2026-05-26, pushed 2026-09-01) — Microsoft OSS sidecar-enforced agent-to-agent authorization bridging Entra Agent Identity and SPIFFE/SPIRE with cross-cloud workload federation — the **first incumbent-OSS entry in the agent-authorization space**. Below the profile bar; logged as signals. LNSAT pushed 2026-09-05 (still 1★).
- Updated the main report (metadata, tracked-projects table, profiles, discovery log) and the executive summary (bottom line, signals, snapshot table). The competitive matrix retains its 2026-07-15 snapshot date.

## Evidence observed

GitHub REST API repo metadata, all fetched 2026-09-06 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 9347 → 9767 (443 forks) | 2026-09-01 |
| GetBindu/create-bindu-agent | 32 → 32 | 2026-03-13 |
| urbit/urbit | 3621 → 3617 | 2026-09-02 |
| urbit/vere | 81 → 81 | 2026-09-04 |
| agent-network-protocol/AgentNetworkProtocol | 1407 → 1413 | 2026-09-04 |
| agent-network-protocol/anp (AgentConnect) | 342 → 345 | 2026-09-06 |
| decionis/agent-safe-pipeline | 530 → 533 (56 forks) | 2026-09-04 |
| agenticmail/agenticmail | 212 → 218 | 2026-09-03 |
| aeoess/agent-passport-system | 42 → 43 | 2026-09-05 |
| aeoess/agent-passport-python / -go / -mcp / -rust | 0 / 0 / 4 / 0 | 2026-09-05 / 09-04 / 09-05 / 09-04 |
| aeoess/aps-web | still 404 | — |
| Agent-Authority-Conformance/aps-conformance-suite | 2 → 3 | 2026-09-05 |
| Agent-Authority-Conformance/governance | 0 | 2026-08-19 |
| anivar/decern | 13 → 13 | 2026-08-24 |
| mishrasanjeev/grantex | 31 → 31 | 2026-09-04 |
| VibeTensor/attestix | 17 → 17 | 2026-09-02 |
| kevinkaylie/AgentNexus | 9 → 9 | 2026-07-29 |
| KestrelSovereignAI/kestrel-sovereign | 8 → 8 | 2026-09-06 |
| airlock-protocol/airlock | 2 → 2 | 2026-08-20 |
| chanceryhq/chancery | 25 → 25 | 2026-07-21 |
| AgentValet/AgentValet | 1 → 1 | 2026-08-12 |
| agentnameservice/ans | 37 → 38 | 2026-09-02 |
| agentnameservice/ans-registry | 30 → 31 | 2026-09-03 |
| agentnameservice/ans-sdk-go / -rust / -java | 5 / 6 / 3 | 2026-09-03 / 09-02 / 09-03 |
| agentnameservice/agent-trust-discovery | 2 → 2 | 2026-09-04 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 67 → 67 (77 forks) | 2026-09-03 |
| didit-protocol/skills | 26 → 26 | 2026-08-10 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 5 → 5 | 2026-09-03 |
| credat/credat | 2 → 2 | 2026-05-22 |
| helixid/helixid | 4 → 5 | 2026-09-06 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-08-23 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | still 404 | — |
| archetech/archon | 6 → 6 | 2026-09-06 |
| digitalbazaar/agent-credential-server | 0 → 0 | 2026-06-08 |
| MoltyCel/moltrust-api | 3 → 3 | 2026-09-04 |
| hypler-dev/LNSAT (signal) | 1 → 1 | 2026-09-05 |
| mocenslabs/legatio-ai (discovery) | NEW: 1 | 2026-09-05 (created 2026-08-19) |
| microsoft/identity-spiffe (discovery) | NEW: 11 | 2026-09-01 (created 2026-05-26) |

Live/README/protocol facts read directly on 2026-09-06:

- **MolTrust live API:** `GET https://api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-09-06 13:03:14.828726"}`; `/.well-known/did.json` → 200; homepage title "The Trust Layer for the Agent Economy — MolTrust", meta unchanged; `GET /pricing` → 301 → `/pricing/` → **403** (both default curl and browser-UA curl); `GET /pricing.html` → 200: "Lightning sat micropayments are on the roadmap (PhoenixD integration prepped, not yet settling)", "$19/mo (2 agents), Scale $299/mo (75 agents)", "$9/mo per additional agent".
- **Soulverse:** homepage title unchanged (`Soulverse | The Operating System of Trust`); npm registry checks for `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` all return 404.
- **IETF Datatracker:** `draft-kroehl-agentic-trust-aae-01`, `draft-narajala-ans-00`, `draft-pidlisnyi-aps-03` — no revision movement since 2026-08-16.
- **mocenslabs/legatio-ai README:** "Legatio AI — The trust layer for autonomous AI agents. Policy enforcement. Human authorization. Complete auditability." Django 5/Python 3.11 stack, "authorization, policy, and audit infrastructure that enables AI agents to act on behalf of humans while enforcing deterministic rules and requiring human approval for sensitive actions." Phase 0 (foundation).
- **microsoft/identity-spiffe repo description:** "Sidecar-enforced agent-to-agent authorization with Microsoft Entra Agent Identity, SPIFFE/SPIRE, and cross-cloud workload federation."

## Interpretation

- **Bindu's compounding is now a trend, not a spike.** +420 after +662: two consecutive triple-digit weeks, 233★ from 10,000, an order of magnitude above everything else in the set. Bridge/collaboration stance unchanged.
- **Agent-Safe Pipeline's decline lasted one week.** The recovery (530→533★, pushed 2026-09-04) says the launch audience hasn't churned; benchmark status still rests on evidence packaging rather than momentum.
- **APS is the most disciplined executor in the set.** Five repos pushed within 36 hours (main, Python, Go, MCP, conformance suite). The multi-repo lockstep plus verification-only Rust crate remains the strongest third-party-verifier recruitment play observed.
- **Chancery is inactive at the current evidence level.** Five stalled cycles with zero pushes triggered the demotion flagged last week. The enterprise IdP/MCP-enforcement vocabulary it introduced remains strategically important — it just now arrives via AgentValet, Agent-Safe Pipeline, and Microsoft's identity-spiffe instead.
- **microsoft/identity-spiffe is the cycle's most strategically important discovery.** Microsoft shipping OSS agent-to-agent authorization plumbing around Entra Agent ID + SPIFFE means the incumbent is building the enforcement layer, not just docs. If Entra shops adopt SPIFFE sidecars as the default agent authZ pattern, DID-rooted authority needs an explicit SPIFFE bridge story (APS already accepts SVIDs; Archon should say where it stands).
- **MolTrust's pricing-path churn continues** (403 → 301→200 → 301→403 across three weeks) but the content is stable and re-verified; treat the path behavior as infra fiddling, not signal. Lightning still roadmap.
- **Soulverse remains brochure-stage** (seventh consecutive week of npm 404s); no change to watchlist classification.

## Source artifacts

- Main report: [Archon Competitive Analysis](/research/archon-competitive-analysis/)
- Executive summary: [Archon Competitive Analysis – Executive Summary](/research/archon-competitive-analysis/executive-summary/)
- mocenslabs/legatio-ai: <https://github.com/mocenslabs/legatio-ai> · microsoft/identity-spiffe: <https://github.com/microsoft/identity-spiffe> · LNSAT: <https://github.com/hypler-dev/LNSAT>
- IETF: <https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/> · <https://datatracker.ietf.org/doc/draft-narajala-ans/> · <https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/>
- MolTrust: <https://moltrust.ch/> · API: <https://api.moltrust.ch> · repo: <https://github.com/MoltyCel/moltrust-api>
