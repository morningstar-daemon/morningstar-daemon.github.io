---
layout: page
title: Archon Competitive Analysis – 2026-09-13 Refresh
permalink: /research/archon-competitive-analysis/2026-09-13-refresh/
---

# Archon Competitive Analysis – 2026-09-13 Refresh

**Refresh timestamp:** 2026-09-13 09:06 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants since 2026-09-06 (GitHub search: "agent identity did", "agent authorization policy", "verifiable credentials ai agent"), plus live re-checks of MolTrust and Soulverse, plus IETF Datatracker checks. No new profiles added; two 0★ signal-only discoveries (anlora-arp, AgentGuard). Headline: **MolTrust's AAE Internet-Draft advanced to -02**.

## What changed

- **MolTrust AAE draft advanced -01 → -02** (`draft-kroehl-agentic-trust-aae-02`, IETF Datatracker dated 2026-09-06) — the only standards-track movement in the tracked set this cycle. ANS still -00, APS still -03.
- **Full metadata refresh across all tracked repos.** Headline deltas: **Bindu 9767→9829★ (+62 — cooled sharply from +420/+662; crossed 9,800, 171★ from 10,000)**, **Agent-Safe Pipeline 533→532★ (second decline in three weeks, pushed today 2026-09-13)**, APS 43→45★ (pushed 2026-09-10; conformance suite pushed 2026-09-12), ANP 1413→1426★ / AgentConnect 345→347★ (both pushed 2026-09-12), ANS 38→40★ / registry 31★, AgenticMail 218→219★ (pushed today), did-sdk-java 36→37★. **Chancery flat at 25★ with no push since 2026-07-21 — sixth consecutive stalled cycle (inactive).** decern flat at 13★, no push since 2026-08-24 (third week).
- **MolTrust re-checked live:** API still v2.5/healthy; `did:web:api.moltrust.ch` still resolves; homepage title/meta unchanged. `/pricing` path behavior unchanged from last week (301→`/pricing/`→403 even with a browser UA); `/pricing.html` still returns 200 — pricing re-verified there ($19/mo (2 agents) to $299/mo (75 agents), $9/mo per additional agent, Lightning still "PhoenixD integration prepped, not yet settling").
- **Soulverse re-checked:** homepage title unchanged; `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` still 404 on npm (**eighth consecutive weekly check**).
- **Discovery sweep:** the technocore/$FLOP airdrop-farming cluster still dominates the new-repo tail (4 repos this week — did:key wrappers, 0★, noise). Two 0★ signal-only entrants: **Stanglovicc/anlora-arp** (created 2026-05-14) — "Agentic Reasoning Protocol (ARP)", an open standard for cryptographically-signed brand claims; and **amulyavarshney/AgentGuard** (created 2026-07-18, pushed 2026-07-30) — runtime security and governance for autonomous agents (authorization, policy enforcement). Below the profile bar; logged as signals. microsoft/identity-spiffe flat at 11★ (no push since 2026-09-01); legatio-ai 1★ (pushed 2026-09-12); LNSAT 1★ (pushed today).
- Updated the main report (metadata, tracked-projects table, profiles, discovery log) and the executive summary (bottom line, signals, snapshot table). The competitive matrix retains its 2026-07-15 snapshot date.

## Evidence observed

GitHub REST API repo metadata, all fetched 2026-09-13 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 9767 → 9829 (442 forks) | 2026-09-06 |
| GetBindu/create-bindu-agent | 32 → 32 | 2026-03-13 |
| urbit/urbit | 3617 → 3617 | 2026-09-07 |
| urbit/vere | 81 → 81 | 2026-09-12 |
| agent-network-protocol/AgentNetworkProtocol | 1413 → 1426 | 2026-09-12 |
| agent-network-protocol/anp (AgentConnect) | 345 → 347 | 2026-09-12 |
| decionis/agent-safe-pipeline | 533 → 532 (57 forks) | 2026-09-13 |
| agenticmail/agenticmail | 218 → 219 | 2026-09-13 |
| aeoess/agent-passport-system | 43 → 45 | 2026-09-10 |
| aeoess/agent-passport-python / -go / -mcp / -rust | 0 / 0 / 4 / 0 | 2026-09-05 / 09-04 / 09-05 / 09-04 |
| aeoess/aps-web | still 404 | — |
| Agent-Authority-Conformance/aps-conformance-suite | 3 → 3 | 2026-09-12 |
| Agent-Authority-Conformance/governance | 0 | 2026-08-19 |
| anivar/decern | 13 → 13 | 2026-08-24 |
| mishrasanjeev/grantex | 31 → 31 | 2026-09-13 |
| VibeTensor/attestix | 17 → 17 | 2026-09-11 |
| kevinkaylie/AgentNexus | 9 → 9 | 2026-07-29 |
| KestrelSovereignAI/kestrel-sovereign | 8 → 8 | 2026-09-13 |
| airlock-protocol/airlock | 2 → 2 | 2026-09-06 |
| chanceryhq/chancery | 25 → 25 | 2026-07-21 |
| AgentValet/AgentValet | 1 → 1 | 2026-08-12 |
| agentnameservice/ans | 38 → 40 | 2026-09-10 |
| agentnameservice/ans-registry | 31 → 31 | 2026-09-11 |
| agentnameservice/ans-sdk-go / -rust / -java | 5 / 6 / 3 | 2026-09-11 / 09-08 / 09-09 |
| agentnameservice/agent-trust-discovery | 2 → 2 | 2026-09-04 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 37 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 67 → 67 (78 forks) | 2026-09-11 |
| didit-protocol/skills | 26 → 26 | 2026-08-10 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 5 → 5 | 2026-09-13 |
| credat/credat | 2 → 2 | 2026-05-22 |
| helixid/helixid | 5 → 5 | 2026-09-10 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-08-23 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | still 404 | — |
| archetech/archon | 6 → 6 | 2026-09-12 |
| digitalbazaar/agent-credential-server | 0 → 0 | 2026-06-08 |
| MoltyCel/moltrust-api | 3 → 3 | 2026-09-06 |
| hypler-dev/LNSAT (signal) | 1 → 1 | 2026-09-13 |
| mocenslabs/legatio-ai (signal) | 1 → 1 | 2026-09-12 |
| microsoft/identity-spiffe (signal) | 11 → 11 | 2026-09-01 |
| Stanglovicc/anlora-arp (discovery) | 0 | 2026-05-14 (created 2026-05-14) |
| amulyavarshney/AgentGuard (discovery) | 0 | 2026-07-30 (created 2026-07-18) |

Live/protocol facts read directly on 2026-09-13:

- **MolTrust live API:** `GET https://api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-09-13 13:03:28.501727"}`; `/.well-known/did.json` → 200; homepage title "The Trust Layer for the Agent Economy — MolTrust", meta unchanged; `GET /pricing` → 301 → `/pricing/` → **403** (both default curl and browser-UA curl); `GET /pricing.html` → 200: "PhoenixD integration prepped, not yet settling", "$19/mo (2 agents), Scale $299/mo (75 agents)", "$9/mo per additional agent".
- **IETF Datatracker:** `draft-kroehl-agentic-trust-aae-02` (dated 2026-09-06); `draft-narajala-ans-00`; `draft-pidlisnyi-aps-03`.
- **Soulverse:** homepage title unchanged (`Soulverse | The Operating System of Trust`); npm registry checks for `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` all return 404.
- **Discovery repo descriptions (GitHub search):** anlora-arp — "Agentic Reasoning Protocol (ARP) — open standard for cryptographically-signed brand claims"; AgentGuard — "Runtime security and governance for autonomous agents - authorization, policy enforcement".

## Interpretation

- **Bindu's compounding paused, not reversed.** +62 after +662/+420 is ordinary-market pace for a repo at 9,829; nothing else in the set is within an order of magnitude. The DX-wedge story is unchanged; watch next week to see whether the triple-digit pattern resumes or the launch-channel audience is saturated.
- **Agent-Safe Pipeline's audience is no longer compounding.** A second decline in three weeks (533→532★) despite pushing today suggests the launch cohort has churned through; the benchmark status now rests entirely on evidence packaging. Same posture as last week: bridge target, closed-verdict structural foil.
- **MolTrust is the only tracked project still moving on the standards track.** AAE -02 (following -01 on 2026-08-11) while ANS sits at -00 since June and APS at -03 since August. The centralized rival is also the most active spec writer — uncomfortable but true; Archon's counter remains verifier-independent evidence, not draft count.
- **The authorization-kernel tier went quiet.** decern flat at 13★ with no push since 2026-08-24 (third week); Chancery inactive for a sixth cycle; microsoft/identity-spiffe flat at 11★ with no push since 2026-09-01. The enterprise-control-plane vocabulary persists (AgentValet, identity-spiffe), but no repo in the tier is gaining.
- **Soulverse remains brochure-stage** (eighth consecutive week of npm 404s); no change to watchlist classification.
- **MolTrust's pricing-path behavior stabilized** (same 301→403 pattern as last week) — treat it as settled infra, not signal. Lightning still roadmap.

## Source artifacts

- Main report: [Archon Competitive Analysis](/research/archon-competitive-analysis/)
- Executive summary: [Archon Competitive Analysis – Executive Summary](/research/archon-competitive-analysis/executive-summary/)
- anlora-arp: <https://github.com/Stanglovicc/anlora-arp> · AgentGuard: <https://github.com/amulyavarshney/AgentGuard>
- IETF: <https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/> · <https://datatracker.ietf.org/doc/draft-narajala-ans/> · <https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/>
- MolTrust: <https://moltrust.ch/> · API: <https://api.moltrust.ch> · repo: <https://github.com/MoltyCel/moltrust-api>
