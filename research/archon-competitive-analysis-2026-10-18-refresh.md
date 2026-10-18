---
layout: page
title: Archon Competitive Analysis – 2026-10-18 Refresh
permalink: /research/archon-competitive-analysis/2026-10-18-refresh/
---

# Archon Competitive Analysis – 2026-10-18 Refresh

**Refresh timestamp:** 2026-10-18 13:15 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants (GitHub search: "agent identity DID", "agent authorization", "verifiable credentials agent", "agent identity", sorted by recently updated), plus live re-checks of MolTrust, Soulverse, and NexionLabs, plus IETF Datatracker checks. Headline: **two credible new entrants surfaced — Wirken (191★, Rust enterprise agent gateway) and OpenA2A AIM (67★, Go agent IAM) — while Bindu posted a second consecutive star decline (10058→10053★, -5) with six weeks without a commit and forks flat for the first time.**

## What changed

- **Wirken added to tracking** (`gebruder/wirken`, 191★/10 forks, MIT, created 2026-03-25, pushed 2026-10-18). Enterprise gateway for autonomous agents: per-channel lines, credential vault with edge injection (model never sees tokens), signed hash-chained attributed audit log, three-tier permission model, no-network sandbox, per-agent spend budgets. Strongest authorization/gateway-cluster entrant since Agent-Safe Pipeline; not previously surfaced by the weekly discovery queries. README verified before profiling.
- **OpenA2A AIM added to tracking** (`opena2a-org/agent-identity-management`, 67★/23 forks, Apache-2.0, created 2025-10-06, pushed 2026-10-18). Agent IAM: Ed25519 keypairs per agent, capability grants, admin verification lifecycle, monitoring/strict org enforcement modes, cloud dashboard + self-hosted. Front-runner of the agent-IAM cluster (Chancery/AgentValet/Grantex). README verified before profiling.
- **Bindu 10058→10053★ (-5)** — second consecutive star decline. **No repo push since 2026-09-06 — six weeks without a commit**; forks flat at 670 (no growth for the first time since the decline began). The reversal is now a trend.
- **APS 49→51★ (+2, pushed 2026-10-15)** — the only tracked project with a multi-star gain this cycle.
- **HelixID pushed 2026-10-16** (flat at 8★) — first push since 2026-09-29.
- Other deltas: ANP 1450→1455★ (pushed 2026-10-15); AgentConnect 352→353★ (Rust, pushed 2026-10-14); Agent-Safe Pipeline flat at 688★ (pushed 2026-10-18); AgenticMail 237→239★ (pushed 2026-10-18); ANS 43★ / registry 33★ (registry pushed 2026-10-16); Grantex flat at 33★ (pushed 2026-10-17); Attestix flat at 874★ (pushed 2026-10-15); Motebit/Kestrel/A2AL/MoltyCel (4★) pushed 2026-10-18; Hedera did-method 27★ / did-sdk-java 36★ / Agent Kit 69★ (pushed 2026-10-17); Chancery flat at 26★, no push (eleventh stalled cycle); Urbit 3622★ / vere 80★ (vere pushed 2026-10-17); Archon flat at 6★ (pushed 2026-10-14).
- **MolTrust re-checked live:** API still v2.5/healthy (timestamp 2026-10-18 13:03 UTC); `did:web` still resolves; homepage title/meta unchanged; `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with $19–$299/mo pricing re-verified, Lightning still roadmap; AAE draft unchanged at -02. Fifth consecutive quiet live-surface cycle.
- **Soulverse re-checked:** all three named npm packages still 404 (thirteenth consecutive weekly check); `@nexionplatform/sdk` still 404; homepage title unchanged; nexionlabs.com 200 with unchanged title.
- **IETF drafts unchanged:** AAE -02, APS -04, ANS -00.
- **Discovery sweep below the profile bar:** `FransDevelopment/open-agent-trust-registry` (11★, federated root-of-trust registry), `arthneura/arthneura-core` (3★, settlement/escrow substrate), `opena2a-standards` conformance/spec repos (1★ each), `kingces95/ai-certmint` (0★). technocore/$FLOP cluster persists (noise).
- Updated the main report (metadata, tracked-projects table, profiles for both new entrants, discovery log, source links) and the executive summary (bottom line, signals, snapshot table).

## Evidence observed

GitHub REST API repo metadata, fetched 2026-10-18 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 10058 → 10053 (670 forks) | 2026-09-06 |
| GetBindu/create-bindu-agent | 32 → 32 | 2026-03-13 |
| urbit/urbit | 3622 → 3622 | 2026-10-15 |
| urbit/vere | 80 → 80 | 2026-10-17 |
| agent-network-protocol/AgentNetworkProtocol | 1450 → 1455 | 2026-10-15 |
| agent-network-protocol/anp (AgentConnect) | 352 → 353 (language: Rust) | 2026-10-14 |
| decionis/agent-safe-pipeline | 688 → 688 | 2026-10-18 |
| agenticmail/agenticmail | 237 → 239 | 2026-10-18 |
| agent-passport-system/agent-passport-system | 49 → 51 | 2026-10-15 |
| agent-passport-system/agent-passport-rust | 0 → 0 | 2026-10-02 |
| anivar/decern | 13 → 13 | 2026-10-14 |
| maoyadongsh/siq-agent-security | 50 → 50 | 2026-10-09 |
| mishrasanjeev/grantex | 33 → 33 | 2026-10-17 |
| VibeTensor/attestix | 874 → 874 | 2026-10-15 |
| chanceryhq/chancery | 26 → 26 | 2026-07-21 |
| AgentValet/AgentValet | 2 → 2 | 2026-09-26 |
| agentnameservice/ans | 43 → 43 | 2026-10-15 |
| agentnameservice/ans-registry | 33 → 33 | 2026-10-16 |
| hashgraph/did-method | 27 → 27 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 69 → 69 | 2026-10-17 |
| didit-protocol/skills | 28 → 28 | 2026-10-17 |
| The-Nexus-Guard/aip | 14 → 14 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 7 → 7 | 2026-10-18 |
| credat/credat | 2 → 2 | 2026-05-22 |
| helixid/helixid | 8 → 8 | 2026-10-16 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-10-18 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | 404 (still gone) | — |
| archetech/archon | 6 → 6 | 2026-10-14 |
| MoltyCel/moltrust-api | 4 → 4 | 2026-10-18 |
| kevinkaylie/AgentNexus | 10 → 10 | 2026-09-23 |
| KestrelSovereignAI/kestrel-sovereign | 8 → 8 | 2026-10-18 |
| airlock-protocol/airlock | 2 → 2 | 2026-09-25 |
| gebruder/wirken (new) | 191 (10 forks) | 2026-10-18 |
| opena2a-org/agent-identity-management (new) | 67 (23 forks, language: Go) | 2026-10-18 |

Live checks, all fetched 2026-10-18:

- `api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-10-18 13:03:45.935711"}`
- `did:web:api.moltrust.ch` → resolves (200)
- moltrust.ch homepage → title "The Trust Layer for the Agent Economy — MolTrust", meta unchanged
- moltrust.ch/pricing → 301 → /pricing/ → 403; /pricing.html → 200, $19/mo (2 agents) → $299/mo (75 agents), $9/mo per additional agent, Lightning still roadmap ("PhoenixD integration prepped, not yet settling")
- npm registry: `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` → all 404 (thirteenth week); `@nexionplatform/sdk` → 404
- soulverse.world → 200, title "Soulverse | The Operating System of Trust" (unchanged); nexionlabs.com → 200, title unchanged
- IETF Datatracker API: `draft-kroehl-agentic-trust-aae` -02, `draft-pidlisnyi-aps` -04, `draft-narajala-ans` -00 (all unchanged)
- New-entrant READMEs read in full before profiling: `gebruder/wirken` (enterprise gateway, vault/audit/permissions/sandbox), `opena2a-org/agent-identity-management` (Ed25519 identity, capability authorization, monitoring/strict modes)
