---
layout: page
title: Archon Competitive Analysis – 2026-10-11 Refresh
permalink: /research/archon-competitive-analysis/2026-10-11-refresh/
---

# Archon Competitive Analysis – 2026-10-11 Refresh

**Refresh timestamp:** 2026-10-11 09:05 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants (GitHub search: "agent identity DID", "agent authorization", "verifiable credentials agent", created:>2026-09-27), plus live re-checks of MolTrust, Soulverse, and NexionLabs, plus IETF Datatracker checks. Headline: **Agent-Safe Pipeline jumped 589→687★ (+98) and repositioned from a reference architecture to an installable execution-authority gateway; Bindu's growth collapsed to +3 with five consecutive weeks without a commit; decern broke its five-week push stall; microsoft/identity-spiffe is gone (404).**

## What changed

- **Agent-Safe Pipeline 589→687★ (+98)** — sharpest move this cycle. Repo description repositioned: now "An execution-authority gateway for AI agents and APIs. It intercepts consequential HTTP actions, asks Decionis whether they are authorized, and forwards exactly the authorized request once on a single-use grant… Installs by Homebrew, Linux package, Docker or Helm." Productization signal: from reference architecture to installable gateway. Pushed 2026-10-10.
- **Bindu 10073→10076★ (+3)** — growth collapsed after last cycle's +264. **No repo push since 2026-09-06 — fifth consecutive week without a commit**; forks still climbed 635→669. Star accumulation has visibly decoupled from development cadence.
- **decern 12→13★, pushed 2026-10-10** — broke its five-week push stall (first commit since 2026-08-24).
- **Attestix 875→874★ (-1), no push since 2026-10-01** — last cycle's +857 spike is not compounding; corroborates the unverified-traction read.
- **microsoft/identity-spiffe now returns 404** (was 11★, last observed pushed 2026-10-03) — removed, renamed, or made private; the first incumbent-OSS agent-authorization entry is no longer publicly visible.
- Other deltas: APS 46→49★ (pushed 2026-10-10); ANP 1441→1444★ (pushed 2026-10-09); AgentConnect 351→352★ (pushed today); AgenticMail 231→236★; SIQ flat at 51★ (pushed 2026-10-09); Grantex 34→33★ (pushed 2026-10-10); ANS 43★ (pushed 2026-10-08) / registry 32★ (pushed 2026-10-10); Chancery flat at 26★, no push (ninth stalled cycle); didit skills 27→28★; Hedera Agent Kit flat at 69★ (pushed 2026-10-07); Urbit 3620→3622★ / vere 80★; MoltyCel/moltrust-api 3→4★ (pushed today); Motebit/Kestrel pushed today; Archon flat at 6★.
- **MolTrust re-checked live:** API still v2.5/healthy (timestamp 2026-10-11 13:03 UTC); `did:web` still resolves; homepage title/meta unchanged; `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with $19–$299/mo pricing re-verified, Lightning still roadmap; AAE draft unchanged at -02. Third consecutive quiet live-surface cycle.
- **Soulverse re-checked:** all three named npm packages still 404 (eleventh consecutive weekly check); homepage title unchanged. `@nexionplatform/sdk` still 404 publicly; nexionlabs.com 200 with unchanged title.
- **IETF drafts unchanged:** AAE -02, APS -04, ANS -00.
- **Discovery sweep:** no new entrant above the profile bar (all ≤2★). Signal-only: `wienerlabs/square-solana` (2★, compliance-gated agent job settlement on Solana — USDC escrow, ZK spending-mandate proofs, DID identity), `oleg-tkachuk/limes` (0★, Biscuit budgeted/delegable capabilities in Go), `thesithunyein/witness` (0★, passkey-signed on-chain human authorization, Monad/ERC-8004), `DuNorth595/xrpl_agent_id` (1★, `did:xrpl` + XLS-70 VCs on XRPL), `goun7/Kredent` (0★, did:key + reputation). The technocore/$FLOP airdrop-farming cluster did not surface in this window's results.
- Updated the main report (metadata, tracked-projects table, profiles, discovery log) and the executive summary (bottom line, signals, snapshot table).

## Evidence observed

GitHub REST API repo metadata, fetched 2026-10-11 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 10073 → 10076 (669 forks) | 2026-09-06 |
| GetBindu/create-bindu-agent | 32 → 32 | 2026-03-13 |
| urbit/urbit | 3620 → 3622 | 2026-10-09 |
| urbit/vere | 80 → 80 | 2026-10-10 |
| agent-network-protocol/AgentNetworkProtocol | 1441 → 1444 | 2026-10-09 |
| agent-network-protocol/anp (AgentConnect) | 351 → 352 | 2026-10-11 |
| decionis/agent-safe-pipeline | 589 → 687 (59 forks) | 2026-10-10 |
| agenticmail/agenticmail | 231 → 236 | 2026-10-01 |
| agent-passport-system/agent-passport-system | 46 → 49 | 2026-10-10 |
| agent-passport-system/agent-passport-rust | 0 → 0 | 2026-10-02 |
| anivar/decern | 12 → 13 | 2026-10-10 |
| maoyadongsh/siq-agent-security | 51 → 51 | 2026-10-09 |
| mishrasanjeev/grantex | 34 → 33 | 2026-10-10 |
| VibeTensor/attestix | 875 → 874 | 2026-10-01 |
| chanceryhq/chancery | 26 → 26 | 2026-07-21 |
| AgentValet/AgentValet | 2 → 2 | 2026-09-26 |
| agentnameservice/ans | 43 → 43 | 2026-10-08 |
| agentnameservice/ans-registry | 32 → 32 | 2026-10-10 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 37 → 37 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 69 → 69 | 2026-10-07 |
| didit-protocol/skills | 27 → 28 | 2026-08-10 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 7 → 7 | 2026-10-11 |
| credat/credat | 2 → 2 | 2026-05-22 |
| helixid/helixid | 8 → 8 | 2026-09-29 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-10-07 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | 404 (still gone) | — |
| archetech/archon | 6 → 6 | 2026-10-07 |
| MoltyCel/moltrust-api | 3 → 4 | 2026-10-11 |
| microsoft/identity-spiffe | 404 (was 11★) | — |
| kevinkaylie/AgentNexus | 10 → 10 | 2026-09-23 |
| KestrelSovereignAI/kestrel-sovereign | 8 → 8 | 2026-10-11 |
| airlock-protocol/airlock | 2 → 2 | 2026-09-25 |

Live checks, all fetched 2026-10-11:

- `api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-10-11 13:03:17.722845"}`
- `did:web:api.moltrust.ch` → resolves with Ed25519 verification methods
- moltrust.ch homepage → title "The Trust Layer for the Agent Economy — MolTrust", meta description unchanged
- moltrust.ch/pricing → 301 → /pricing/ → 403; /pricing.html → 200, $19–$299/mo + $9/mo per additional agent, "PhoenixD integration prepped, not yet settling"
- npm registry: `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` → all 404 (eleventh week); `@nexionplatform/sdk` → 404
- soulverse.world → 200, title "Soulverse | The Operating System of Trust" (unchanged); nexionlabs.com → 200, title unchanged
- IETF Datatracker: `draft-kroehl-agentic-trust-aae-02`, `draft-pidlisnyi-aps-04`, `draft-narajala-ans-00` (all unchanged)
