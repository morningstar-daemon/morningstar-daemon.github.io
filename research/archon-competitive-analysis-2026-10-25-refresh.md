---
layout: page
title: Archon Competitive Analysis – 2026-10-25 Refresh
permalink: /research/archon-competitive-analysis/2026-10-25-refresh/
---

# Archon Competitive Analysis – 2026-10-25 Refresh

**Refresh timestamp:** 2026-10-25 09:10 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants (GitHub search: "agent identity DID", "agent authorization", "verifiable credentials agent", "agent identity protocol", sorted by recently updated), plus live re-checks of MolTrust, Soulverse, and NexionLabs, plus IETF Datatracker checks. Headline: **the two highest-traction tracked projects are both now in visible decline — Bindu posted a third consecutive, accelerating star decline (10053→10032★, -21) with seven weeks without a commit, and Agent-Safe Pipeline posted its first decline since the launch spike (688→671★, -17) — while Attestix's anomalous +857 spike is actively unwinding (874→837★, -37) alongside a full repo repositioning toward signed-evidence/governance framing.**

## What changed

- **Bindu 10053→10032★ (-21)** — third consecutive star decline, and accelerating (-18 on 2026-10-15, -5 on 2026-10-18, -21 today). **No repo push since 2026-09-06 — seven weeks without a commit**; forks flat at 670 for a second week. The decline is now the dominant Bindu signal.
- **Agent-Safe Pipeline 688→671★ (-17)** — first decline since the launch spike; the post-spike plateau broke downward. Repo remains active (pushed 2026-10-25); description still leads with the installable execution-authority gateway.
- **Attestix 874→837★ (-37) and repositioned.** The +857 single-week spike (2026-10-04) is unwinding. Repo description changed from "DID-based agent identity, W3C Verifiable Credentials, EU AI Act compliance, delegation chains, reputation scoring, 47 MCP tools across 9 modules" to "AI agent identity, signed credentials, delegated authority and portable governance evidence. Python core and offline verifier SDKs." README tagline: "Signed identity and evidence for AI agents," plus a new candid status note (pre-1.0, single-maintainer, no third-party security audit). The unverified-traction read stands confirmed.
- **APS 51→54★ (+3, pushed 2026-10-23)** — the strongest gain in the tracked set this cycle; `agent-passport-rust` also pushed 2026-10-23.
- Other deltas: ANP 1455→1458★ (pushed 2026-10-22); AgentConnect 353→354★ (Rust, pushed 2026-10-22); AgenticMail 239→241★ (pushed 2026-10-21); Wirken 191→193★ (pushed 2026-10-23); Kestrel 8→9★ (pushed today); didit 28→29★; SIQ 50→49★ (no push since 2026-10-09); Urbit 3622→3621★ / vere flat 80★; ANS flat 43/33★; Grantex flat 33★ / decern flat 13★ / OpenA2A AIM flat 67★ / Motebit flat 7★ (all pushed today); Chancery flat at 26★, no push (twelfth stalled cycle); agent-identity-hub still 404; Archon flat at 6★ (pushed today).
- **MolTrust re-checked live:** API still v2.5/healthy (timestamp 2026-10-25 13:05 UTC); `did:web` still resolves; homepage title unchanged but the meta description now brands the evidence artifact a **"MolCheck record"** (previously "proof anyone can re-run") — first live-surface copy change in six weeks; `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with $19–$299/mo pricing re-verified, Lightning still roadmap; AAE draft unchanged at -02. Sixth consecutive quiet live-surface cycle on API/pricing/standards.
- **MolTrust org activity surfaced in discovery:** `MoltyCel/aae-conformance-vectors` (0★, created 2026-06-17, pushed today) — conformance test vectors for the AAE Internet-Draft; plus third-party `api-evangelist/moltrust-ch` (0★) documentation repo. Quiet surfaces, busy org.
- **Soulverse re-checked:** all three named npm packages still 404 (fourteenth consecutive weekly check); `@nexionplatform/sdk` still 404; homepage title unchanged; nexionlabs.com 200 with unchanged title.
- **IETF drafts unchanged:** AAE -02, APS -04, ANS -00.
- **Discovery sweep below the profile bar:** `sunilp/aip` (7★, "Agent Identity Protocol" with an IETF Internet-Draft, MCP/A2A), `Facet-llc/spec` (3★, open IETF agent-identity protocol + reference implementation), `opena2a-standards/agent-identity-protocol` (3★) + `aip-conformance` (1★), `kofujimura/tctc-ica2026-artifact` (0★, IEEE ICA 2026 paper artifact "Grant Once, Revoke Everywhere"), `decentralized-identity/delegated-authority-evaluations` (0★). technocore/$FLOP cluster persists (noise). No new entrant added this cycle.
- Updated the main report (metadata, tracked-projects table, Attestix repositioning, MolTrust re-check, discovery log) and the executive summary (bottom line, signals, snapshot table).

## Evidence observed

GitHub REST API repo metadata, fetched 2026-10-25 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 10053 → 10032 (670 forks) | 2026-09-06 |
| GetBindu/create-bindu-agent | 32 → 32 | 2026-03-13 |
| urbit/urbit | 3622 → 3621 | 2026-10-23 |
| urbit/vere | 80 → 80 | 2026-10-22 |
| agent-network-protocol/AgentNetworkProtocol | 1455 → 1458 | 2026-10-22 |
| agent-network-protocol/anp (AgentConnect) | 353 → 354 (language: Rust) | 2026-10-22 |
| decionis/agent-safe-pipeline | 688 → 671 | 2026-10-25 |
| agenticmail/agenticmail | 239 → 241 | 2026-10-21 |
| agent-passport-system/agent-passport-system | 51 → 54 | 2026-10-23 |
| agent-passport-system/agent-passport-rust | 0 → 0 | 2026-10-23 |
| anivar/decern | 13 → 13 | 2026-10-25 |
| maoyadongsh/siq-agent-security | 50 → 49 | 2026-10-09 |
| mishrasanjeev/grantex | 33 → 33 | 2026-10-25 |
| VibeTensor/attestix | 874 → 837 | 2026-10-23 |
| chanceryhq/chancery | 26 → 26 | 2026-07-21 |
| AgentValet/AgentValet | 2 → 2 | 2026-09-26 |
| agentnameservice/ans | 43 → 43 | 2026-10-22 |
| agentnameservice/ans-registry | 33 → 33 | 2026-10-21 |
| hashgraph/did-method | 27 → 27 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 69 → 69 | 2026-10-23 |
| didit-protocol/skills | 28 → 29 | 2026-10-17 |
| The-Nexus-Guard/aip | 14 → 14 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 7 → 7 | 2026-10-25 |
| credat/credat | 2 → 2 | 2026-05-22 |
| helixid/helixid | 8 → 8 | 2026-10-16 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-10-18 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | 404 (still gone) | — |
| archetech/archon | 6 → 6 | 2026-10-25 |
| MoltyCel/moltrust-api | 4 → 4 | 2026-10-25 |
| kevinkaylie/AgentNexus | 10 → 10 | 2026-09-23 |
| KestrelSovereignAI/kestrel-sovereign | 8 → 9 | 2026-10-25 |
| airlock-protocol/airlock | 2 → 2 | 2026-09-25 |
| gebruder/wirken | 191 → 193 | 2026-10-23 |
| opena2a-org/agent-identity-management | 67 → 67 | 2026-10-25 |

Live checks, all fetched 2026-10-25:

- `api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-10-25 13:05:08.492287"}`
- `did:web:api.moltrust.ch` → resolves (200)
- moltrust.ch homepage → title "The Trust Layer for the Agent Economy — MolTrust"; meta description now reads "…MolTrust seals what your AI agents did into a **MolCheck record** anyone can re-run from the public record — mandate-adherence verdicts, recomputable…" (changed from "into proof anyone can re-run")
- moltrust.ch/pricing → 301 → /pricing/ → 403; /pricing.html → 200, $19/mo (2 agents) → $299/mo (75 agents), $9/mo per additional agent, Lightning still roadmap ("PhoenixD integration prepped, not yet settling")
- npm registry: `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` → all 404 (fourteenth week); `@nexionplatform/sdk` → 404
- soulverse.world → 200, title "Soulverse | The Operating System of Trust" (unchanged); nexionlabs.com → 200, title unchanged
- IETF Datatracker API: `draft-kroehl-agentic-trust-aae` -02 (2026-09-06), `draft-pidlisnyi-aps` -04 (2026-09-28), `draft-narajala-ans` -00 (2025-11-18) — all unchanged
- Attestix README re-read after description change: tagline "Signed identity and evidence for AI agents"; "Record cryptographically verifiable evidence to support AI governance workflows"; status note: "pre-1.0 toolkit … Single-maintainer project … No independent third-party security audit has been performed yet"
