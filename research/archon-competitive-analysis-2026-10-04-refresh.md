---
layout: page
title: Archon Competitive Analysis – 2026-10-04 Refresh
permalink: /research/archon-competitive-analysis/2026-10-04-refresh/
---

# Archon Competitive Analysis – 2026-10-04 Refresh

**Refresh timestamp:** 2026-10-04 09:06 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants (GitHub search: "agent identity DID", "agent authorization", "verifiable credentials agent"), plus live re-checks of MolTrust and Soulverse, plus IETF Datatracker checks. Headline: **Bindu crossed 10,000★ (9809→10073) despite no repo push in four weeks; APS's IETF draft advanced to -04 and its repos moved to a `agent-passport-system` org; Attestix posted an anomalous 18→875★ spike (unverified traction).**

## What changed

- **Bindu 9809→10073★ (+264)** — second-largest weekly gain observed; crossed 10,000. But **no push since 2026-09-06** (fourth week without a commit); forks jumped 448→635.
- **APS IETF draft advanced `draft-pidlisnyi-aps-03` → `-04`** (Datatracker dated 2026-09-28) — the cycle's only standards-track movement; AAE still -02, ANS still -00. **APS repos moved to a dedicated `agent-passport-system` org** (main SDK + Rust verifier both resolving under the new org).
- **Attestix 18→875★ (+857) — anomalous spike.** Pushed 2026-10-01; description now "47 MCP tools across 9 modules"; forks 83. No viral event verified; a surge of this size in a previously ~1-star-per-week repo is unverified traction and possibly star-farming. Reported as observed, flagged for corroboration next cycle.
- **Mid-tier paused:** Agent-Safe Pipeline flat at 589★ (pushed today); SIQ flat at 51★ (pushed 2026-10-02); Grantex flat at 34★ (pushed today); Motebit flat at 7★ (pushed today); Kestrel flat at 8★ (pushed today); ANS 43★ / registry 32★ (registry pushed 2026-09-29); AgentNexus flat at 10★; HelixID flat at 8★ (pushed 2026-09-29).
- **Stalls extended:** decern flat at 12★ with no push since 2026-08-24 (fifth stalled week); Chancery flat at 26★ with no push since 2026-07-21 (eighth consecutive stalled-push cycle — still classified inactive).
- Other deltas: ANP 1435→1441★ / AgentConnect 351★ (pushed 2026-10-01); AgenticMail 229→231★ (pushed 2026-10-01); didit skills 26→27★; Hedera Agent Kit 68→69★ (pushed today); did-sdk-java flat at 37★; Urbit 3619→3620★ / vere 80★ (pushed 2026-10-02); Archon itself 5→6★ (pushed 2026-10-01).
- **MolTrust re-checked live:** API still v2.5/healthy (timestamp 2026-10-04 13:03 UTC); `did:web` still resolves; homepage title/meta unchanged; `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with $19–$299/mo pricing re-verified, Lightning still roadmap. Second consecutive fully quiet MolTrust cycle.
- **Soulverse re-checked:** all three named npm packages still 404 (tenth consecutive weekly check).
- **Discovery sweep:** no new entrant above the profile bar. Signal-only: `ndrorchestration/DGAF-Framework` (4★, evidence-bound AI governance framework, pushed 2026-10-03), `opena2a-standards/agent-authorization-protocol` (1★, scoped/attested authorization draft), `frostyjay7813/AgentFence` (0★, authorization-bound execution). microsoft/identity-spiffe pushed again 2026-10-03 (11★). The technocore/$FLOP airdrop-farming cluster persists (noise).
- Updated the main report (metadata, tracked-projects table, profiles, discovery log) and the executive summary (bottom line, signals, snapshot table).

## Evidence observed

GitHub REST API repo metadata, fetched 2026-10-04 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 9809 → 10073 (635 forks) | 2026-09-06 |
| GetBindu/create-bindu-agent | 32 → 32 | 2026-03-13 |
| urbit/urbit | 3619 → 3620 | 2026-10-02 |
| urbit/vere | 80 → 80 | 2026-10-02 |
| agent-network-protocol/AgentNetworkProtocol | 1435 → 1441 | 2026-10-01 |
| agent-network-protocol/anp (AgentConnect) | 351 → 351 | 2026-10-01 |
| decionis/agent-safe-pipeline | 589 → 589 (58 forks) | 2026-10-04 |
| agenticmail/agenticmail | 229 → 231 | 2026-10-01 |
| agent-passport-system/agent-passport-system (was aeoess/) | 46 → 46 | 2026-10-04 |
| agent-passport-system/agent-passport-rust (was aeoess/) | 0 → 0 | 2026-10-02 |
| anivar/decern | 12 → 12 | 2026-08-24 |
| maoyadongsh/siq-agent-security | 51 → 51 (12 forks) | 2026-10-02 |
| mishrasanjeev/grantex | 34 → 34 | 2026-10-04 |
| VibeTensor/attestix | 18 → 875 (83 forks) ⚠️ anomalous | 2026-10-01 |
| chanceryhq/chancery | 26 → 26 | 2026-07-21 |
| AgentValet/AgentValet | 2 → 2 | 2026-09-26 |
| agentnameservice/ans | 43 → 43 | 2026-10-02 |
| agentnameservice/ans-registry | 32 → 32 | 2026-09-29 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 37 → 37 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 68 → 69 | 2026-10-04 |
| didit-protocol/skills | 26 → 27 | 2026-08-10 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 7 → 7 | 2026-10-04 |
| credat/credat | 2 → 2 | 2026-05-22 |
| helixid/helixid | 8 → 8 | 2026-09-29 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-10-02 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| kevinkaylie/AgentNexus | 10 → 10 | 2026-09-23 |
| KestrelSovereignAI/kestrel-sovereign | 8 → 8 | 2026-10-04 |
| airlock-protocol/airlock | 2 → 2 | 2026-09-25 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| digitalbazaar/agent-credential-server | 0 → 0 | 2026-06-08 |
| yksanjo/agent-identity-hub | still 404 | — |
| archetech/archon | 5 → 6 | 2026-10-01 |

IETF Datatracker API, fetched 2026-10-04:

- `draft-pidlisnyi-aps` → **-04** (2026-09-28) — advanced
- `draft-kroehl-agentic-trust-aae` → -02 (2026-09-06) — unchanged
- `draft-narajala-ans` → -00 (2025-11-18) — unchanged

MolTrust live checks, 2026-10-04:

- `https://api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-10-04 13:03:41"}`
- `https://moltrust.ch/.well-known/did.json` → resolves (`did:web:moltrust.ch`)
- `https://moltrust.ch/pricing` → 301 → `/pricing/` → 403 (browser UA)
- `https://moltrust.ch/pricing.html` → 200; pricing re-verified ($19–$299/mo + $9/mo per additional agent; Lightning still roadmap)

Soulverse npm registry checks, 2026-10-04: `@soulverse/sdk`, `soulverse-sdk`, `@soulverse/agent-sdk` → all 404 (tenth consecutive weekly check).

## Interpretation

- **Bindu's five-digit star count now coexists with a four-week-frozen repo.** Traction is running on brand/DX momentum rather than visible development cadence; the competitive narrative should note the divergence rather than treating 10,073★ as equivalent to active shipping.
- **APS is playing the long game credibly:** IETF draft revision (-04) the day after our last sweep, plus org consolidation. Its protocol-spec discipline is the most durable pressure in the set.
- **Attestix's +857 spike is a data-quality event, not (yet) a market event.** No corroborating activity verified. If it holds and shows real issue/PR traffic next week, re-evaluate.
- **The authorization-boundary tier paused** after two strong weeks (Agent-Safe Pipeline and SIQ both flat). No narrative change, but last week's "fastest-moving segment" framing should be re-tested next cycle.
- **Stall watch:** decern (five weeks) and Chancery (eight weeks) are both effectively dormant; the enterprise control-plane vocabulary they introduced outlives their repos.
- **MolTrust and Soulverse remain static** — second quiet MolTrust cycle; tenth week of Soulverse npm 404s. No new evidence to act on in either.
