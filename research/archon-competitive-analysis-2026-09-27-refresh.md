---
layout: page
title: Archon Competitive Analysis – 2026-09-27 Refresh
permalink: /research/archon-competitive-analysis/2026-09-27-refresh/
---

# Archon Competitive Analysis – 2026-09-27 Refresh

**Refresh timestamp:** 2026-09-27 09:06 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants (GitHub search: "agent identity DID", "agent authorization", "verifiable credentials agent"), plus live re-checks of MolTrust and Soulverse, plus IETF Datatracker checks. **No refresh ran on 2026-09-20**, so this cycle's deltas span two weeks. Headline: **Bindu's first observed weekly decline (9829→9809★); Agent-Safe Pipeline's sharpest gain since launch (532→589★); new entrant SIQ Agent Security (51★).**

## What changed

- **Bindu 9829→9809★ (-20)** — first observed weekly decline after nine consecutive weeks of gains (including two triple-digit weeks in August); forks 417→448.
- **Agent-Safe Pipeline 532→589★ (+57)** — sharpest weekly gain since its launch week, pushed 2026-09-26.
- **New entrant: SIQ Agent Security** (`maoyadongsh/siq-agent-security`, 51★/12 forks, Apache-2.0, created 2026-08-13, pushed 2026-09-27) — local-first agent/skill authorization runtime binding Ed25519-signed intents, parameters, and receipts; individual + enterprise control-plane variants; signed 0.4.0 release shipped today. Highest-traction discovery since Agent-Safe Pipeline.
- **Chancery ticked 25→26★ with no push** — still no commit since 2026-07-21 (seventh consecutive stalled-push cycle); remains classified inactive.
- **decern dipped 13→12★**, no push since 2026-08-24 (fourth stalled week).
- Other deltas: ANP 1426→1435★ / AgentConnect 347→351★ (pushed 2026-09-24); AgenticMail 219→229★; ANS 40→43★ / registry 31→32★ (SDKs and trust-discovery repo all pushed within window); Grantex 31→34★ and Attestix 17→18★ (both pushed 2026-09-27); Motebit 5→7★ and HelixID 5→8★ (both pushed 2026-09-27); AgentValet 1→2★ (first push since 2026-08-12); AgentNexus 9→10★ (first push since 2026-07-29); APS 45→46★ (pushed 2026-09-25); Urbit 3617→3619★ / vere 81→80★; Hedera Agent Kit 67→68★ (pushed 2026-09-23); did-sdk-java flat at 37★.
- **MolTrust re-checked live:** API still v2.5/healthy; `did:web` still resolves; homepage title/meta unchanged; `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with pricing re-verified. AAE Internet-Draft unchanged at -02 — first fully quiet MolTrust cycle since it was added.
- **Soulverse re-checked:** homepage title unchanged; all three named npm packages still 404 (ninth consecutive weekly check).
- **Discovery sweep:** the technocore/$FLOP airdrop-farming cluster and generic did:key/authorization scaffolds continue to dominate the new-repo tail (noise). SIQ Agent Security was the one credible new entrant verified via README read.
- Updated the main report (metadata, tracked-projects table, profiles, new SIQ profile, discovery log) and the executive summary (bottom line, signals, snapshot table).

## Evidence observed

GitHub REST API repo metadata, fetched 2026-09-27 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 9829 → 9809 (448 forks) | 2026-09-06 |
| GetBindu/create-bindu-agent | 32 → 32 | 2026-03-13 |
| urbit/urbit | 3617 → 3619 | 2026-09-25 |
| urbit/vere | 81 → 80 | 2026-09-25 |
| agent-network-protocol/AgentNetworkProtocol | 1426 → 1435 | 2026-09-24 |
| agent-network-protocol/anp (AgentConnect) | 347 → 351 | 2026-09-24 |
| decionis/agent-safe-pipeline | 532 → 589 (58 forks) | 2026-09-26 |
| agenticmail/agenticmail | 219 → 229 | 2026-09-13 |
| aeoess/agent-passport-system | 45 → 46 | 2026-09-25 |
| aeoess/agent-passport-python / -go / -mcp / -rust | 0 / 0 / 4 / 0 | 2026-09-24 / 09-04 / 09-22 / 09-04 |
| Agent-Authority-Conformance/aps-conformance-suite | 3 → 4 | 2026-09-24 |
| Agent-Authority-Conformance/governance | 0 | 2026-08-19 |
| anivar/decern | 13 → 12 | 2026-08-24 |
| mishrasanjeev/grantex | 31 → 34 | 2026-09-27 |
| VibeTensor/attestix | 17 → 18 | 2026-09-27 |
| kevinkaylie/AgentNexus | 9 → 10 | 2026-09-23 |
| KestrelSovereignAI/kestrel-sovereign | 8 → 8 | 2026-09-27 |
| airlock-protocol/airlock | 2 → 2 | 2026-09-25 |
| chanceryhq/chancery | 25 → 26 | 2026-07-21 (no push) |
| AgentValet/AgentValet | 1 → 2 | 2026-09-26 |
| agentnameservice/ans | 40 → 43 | 2026-09-24 |
| agentnameservice/ans-registry | 31 → 32 | 2026-09-15 |
| agentnameservice/ans-sdk-go / -rust / -java | 5→6 / 6→6 / 3→3 | 2026-09-21 / 09-21 / 09-21 |
| agentnameservice/agent-trust-discovery | 2 → 7 | 2026-09-23 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 37 → 37 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 67 → 68 (76 forks) | 2026-09-23 |
| didit-protocol/skills | 26 → 27 | 2026-08-10 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 5 → 7 | 2026-09-27 |
| credat/credat | 2 → 2 | 2026-05-22 |
| helixid/helixid | 5 → 8 | 2026-09-27 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-09-21 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | still 404 | — |
| archetech/archon | 6 → 6 | 2026-09-25 |
| digitalbazaar/agent-credential-server | 0 → 0 | 2026-06-08 |
| MoltyCel/moltrust-api | 3 → 4 | 2026-09-27 |
| hypler-dev/LNSAT (signal) | 1 → 1 | 2026-09-27 |
| mocenslabs/legatio-ai (signal) | 1 → 1 | 2026-09-15 |
| microsoft/identity-spiffe (signal) | 11 → 11 | 2026-09-14 |
| **maoyadongsh/siq-agent-security (new)** | — → 51 (12 forks) | 2026-09-27 |

Live/protocol facts read directly on 2026-09-27:

- **MolTrust live API:** `GET https://api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected"}`; `/.well-known/did.json` → 200; homepage title "The Trust Layer for the Agent Economy — MolTrust", meta unchanged; `GET /pricing` → 301 → `/pricing/` → **403**; `GET /pricing.html` → 200: "$19/mo (2 agents)", "$299/mo (75 agents)", "$9/mo per additional agent", "PhoenixD integration prepped, not yet settling."
- **IETF Datatracker:** `draft-kroehl-agentic-trust-aae-02` (unchanged, dated 2026-09-06); `draft-narajala-ans-00`; `draft-pidlisnyi-aps-03`.
- **Soulverse:** homepage title unchanged (`Soulverse | The Operating System of Trust`); npm registry checks for `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` all return 404.
- **SIQ Agent Security README read directly:** bilingual (Chinese-primary) README describes a "secure runtime for agent skills" binding trusted authorization intent, action parameters, and execution receipts with Ed25519 signatures and SHA-256 digests; distinguishes discovered vs. managed vs. protected assets; ships individual client and enterprise control-plane variants from one codebase; signed release 0.4.0 pinned to commit `2cd6116`.
