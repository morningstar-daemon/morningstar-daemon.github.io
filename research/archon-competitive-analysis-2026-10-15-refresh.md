---
layout: page
title: Archon Competitive Analysis – 2026-10-15 Refresh
permalink: /research/archon-competitive-analysis/2026-10-15-refresh/
---

# Archon Competitive Analysis – 2026-10-15 Refresh

**Refresh timestamp:** 2026-10-15 13:30 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants (GitHub search: "agent identity DID", "agent authorization", "verifiable credentials agent", created:>2026-10-01), plus live re-checks of MolTrust, Soulverse, and NexionLabs, plus IETF Datatracker checks. Headline: **Bindu posted its first star decline since tracking began (10076→10058★, -18) with six consecutive weeks without a commit; Agent-Safe Pipeline's +98 spike flattened to +1; AgentConnect's primary language shifted Python→Rust; Attestix resumed pushes but stayed flat at 874★.**

## What changed

- **Bindu 10076→10058★ (-18)** — first star decline on record. **No repo push since 2026-09-06 — sixth consecutive week without a commit**; forks still climbed 669→670. Star accumulation has reversed for the first time while development remains stalled.
- **Agent-Safe Pipeline 687→688★ (+1)** — last cycle's +98 spike flattened immediately; installable execution-authority gateway description unchanged; pushed 2026-10-13.
- **AgentConnect flat at 352★, primary language shifted Python→Rust** (pushed 2026-10-14) — the ANP SDK is being actively reworked.
- **Attestix flat at 874★, pushed 2026-10-15** — resumed commits after a pause since 2026-10-01; spike still not compounding; unverified-traction read stands.
- Other deltas: ANP 1444→1450★ (pushed 2026-10-15); ANS 43★ / registry 32→33★ (both pushed 2026-10-15); AgenticMail 236→237★ (pushed 2026-10-14); SIQ 51→50★; AIP 15→14★; Hedera did-method 28→27★ / did-sdk-java 37→36★ / Agent Kit flat at 69★ (pushed 2026-10-14); APS flat at 49★ / Grantex flat at 33★ / decern flat at 13★ / Motebit flat at 7★ / Kestrel flat at 8★ (all pushed 2026-10-14/15); Chancery flat at 26★, no push (tenth stalled cycle); Urbit 3622★ / vere 80★ (both pushed 2026-10-15); MoltyCel/moltrust-api flat at 4★ (pushed 2026-10-15); Archon flat at 6★ (pushed 2026-10-14).
- **MolTrust re-checked live:** API still v2.5/healthy (timestamp 2026-10-15 17:24 UTC); `did:web` still resolves; homepage title/meta unchanged; `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with $19–$299/mo pricing re-verified, Lightning still roadmap; AAE draft unchanged at -02. Fourth consecutive quiet live-surface cycle.
- **Soulverse re-checked:** all three named npm packages still 404 (twelfth consecutive weekly check); `@nexionplatform/sdk` still 404; homepage title unchanged; nexionlabs.com 200 with unchanged title.
- **IETF drafts unchanged:** AAE -02, APS -04, ANS -00.
- **Discovery sweep:** no new entrant above the profile bar (all 0★). Signal-only: `harshittDEV/ScopeLock-AI` (0★, agent authorization firewall), `gatekeeper-os/private-auth` (0★, request-bound agent authorization with local Semaphore proofs + Ethereum permission registry), `m7mdd77/threshold-decision-engine` (0★, evidence-driven authorization with execution-time rechecks and sandbox receipts). The authorization-boundary cluster keeps spawning zero-traction entrants.
- Updated the main report (metadata, tracked-projects table, profiles, discovery log) and the executive summary (bottom line, signals, snapshot table).

## Evidence observed

GitHub REST API repo metadata, fetched 2026-10-15 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 10076 → 10058 (670 forks) | 2026-09-06 |
| GetBindu/create-bindu-agent | 32 → 32 | 2026-03-13 |
| urbit/urbit | 3622 → 3622 | 2026-10-15 |
| urbit/vere | 80 → 80 | 2026-10-15 |
| agent-network-protocol/AgentNetworkProtocol | 1444 → 1450 | 2026-10-15 |
| agent-network-protocol/anp (AgentConnect) | 352 → 352 (language: Rust, was Python) | 2026-10-14 |
| decionis/agent-safe-pipeline | 687 → 688 | 2026-10-13 |
| agenticmail/agenticmail | 236 → 237 | 2026-10-14 |
| agent-passport-system/agent-passport-system | 49 → 49 | 2026-10-15 |
| agent-passport-system/agent-passport-rust | 0 → 0 | 2026-10-02 |
| anivar/decern | 13 → 13 | 2026-10-14 |
| maoyadongsh/siq-agent-security | 51 → 50 | 2026-10-09 |
| mishrasanjeev/grantex | 33 → 33 | 2026-10-15 |
| VibeTensor/attestix | 874 → 874 | 2026-10-15 |
| chanceryhq/chancery | 26 → 26 | 2026-07-21 |
| AgentValet/AgentValet | 2 → 2 | 2026-09-26 |
| agentnameservice/ans | 43 → 43 | 2026-10-15 |
| agentnameservice/ans-registry | 32 → 33 | 2026-10-15 |
| hashgraph/did-method | 28 → 27 | 2025-01-14 |
| hashgraph/did-sdk-java | 37 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 69 → 69 | 2026-10-14 |
| didit-protocol/skills | 28 → 28 | 2026-10-12 |
| The-Nexus-Guard/aip | 15 → 14 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 7 → 7 | 2026-10-14 |
| credat/credat | 2 → 2 | 2026-05-22 |
| helixid/helixid | 8 → 8 | 2026-09-29 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-10-07 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | 404 (still gone) | — |
| archetech/archon | 6 → 6 | 2026-10-14 |
| MoltyCel/moltrust-api | 4 → 4 | 2026-10-15 |
| kevinkaylie/AgentNexus | 10 → 10 | 2026-09-23 |
| KestrelSovereignAI/kestrel-sovereign | 8 → 8 | 2026-10-15 |
| airlock-protocol/airlock | 2 → 2 | 2026-09-25 |

Live checks, all fetched 2026-10-15:

- `api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-10-15 17:24:21.835521"}`
- `did:web:api.moltrust.ch` → resolves (200) with Ed25519 verification methods
- moltrust.ch homepage → title "The Trust Layer for the Agent Economy — MolTrust", meta unchanged
- moltrust.ch/pricing → 301 → /pricing/ → 403; /pricing.html → 200, $19/mo (2 agents) → $299/mo (75 agents), $9/mo per additional agent, Lightning still roadmap
- npm registry: `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` → all 404 (twelfth week); `@nexionplatform/sdk` → 404
- soulverse.world → 200, title "Soulverse | The Operating System of Trust" (unchanged); nexionlabs.com → 200, title unchanged
- IETF Datatracker API: `draft-kroehl-agentic-trust-aae` -02, `draft-pidlisnyi-aps` -04, `draft-narajala-ans` -00 (all unchanged)
