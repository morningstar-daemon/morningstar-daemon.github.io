---
layout: page
title: Archon Competitive Analysis – 2026-08-23 Refresh
permalink: /research/archon-competitive-analysis/2026-08-23-refresh/
---

# Archon Competitive Analysis – 2026-08-23 Refresh

**Refresh timestamp:** 2026-08-23 09:05 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api` as `morningstar-daemon`), plus a discovery sweep for new entrants since 2026-08-16 (GitHub search: "agent identity DID", "agent authorization", "ERC-8004 agent", "agent passport", "agent trust verifiable"), plus live re-checks of MolTrust and Soulverse, plus IETF Datatracker checks. No new profiles added; one signal-only discovery (LNSAT).

## What changed

- **Full metadata refresh across all tracked repos.** Headline deltas: Bindu 8525→8685★, ANP 1390→1402★, AgentConnect 340→342★ (pushed 2026-08-22), Agent-Safe Pipeline 469→533★, AgenticMail 194→204★, APS 40→41★, didit skills 24→26★, Kestrel 7→8★, ANS registry 28→29★. Chancery flat at 25★ with no push since 2026-07-21 (**third consecutive stalled cycle**); decern flat at 12★ (third week).
- **HelixID's repo moved** from `dgverse-labs/helixid` to a dedicated `helixid` org — the API follows the redirect to `helixid/helixid` (3★, pushed 2026-08-23). Profile and table updated.
- **MolTrust re-checked live:** API still v2.5/healthy; `did:web:api.moltrust.ch` still resolves with Ed25519 keys; homepage title/meta unchanged ("The Trust Layer for the Agent Economy"). **`/pricing` now returns 403 Forbidden (nginx) to curl** — UA blocking unconfirmed; pricing/Lightning status unverified this run. Public repo `MoltyCel/moltrust-api` 3★, pushed 2026-08-20.
- **Soulverse re-checked:** homepage title unchanged (`Soulverse | The Operating System of Trust`); `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` still 404 on npm (fifth consecutive weekly check).
- **IETF Datatracker unchanged:** `draft-kroehl-agentic-trust-aae-01`, `draft-narajala-ans-00`, `draft-pidlisnyi-aps-03`.
- **Discovery sweep:** the only notable new entrant is **LNSAT** (`hypler-dev/LNSAT`, 1★, created 2026-08-20, pre-release, Apache-2.0): an open-source execution-authorization and evidence layer — "intent → policy → approval → authorization → execution → receipt → audit → reconciliation" — structurally similar to Agent-Safe Pipeline (agents propose, an external authority decides, telemetry never grants authority). Below the profile bar; logged as signal. The rest of the tail is the usual noise: BNB/ERC-8004 marketplace residue (agentcensus, AgentEra, bnb-era-marketplace), small agent-authorization clones (legatio-ai, authentify-consent-widget, 3ar, goldkey-style gates), an ERC-8004 liveness MCP probe, and an ERC-8126 security-scan MCP — none met the bar.
- Updated the main report (metadata, tracked-projects table, profiles incl. HelixID org move, discovery log) and the executive summary (bottom line, signals, snapshot table). The competitive matrix retains its 2026-07-15 snapshot date.

## Evidence observed

GitHub REST API repo metadata, all fetched 2026-08-23 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 8525 → 8685 | 2026-08-21 |
| GetBindu/create-bindu-agent | 31 → 32 | 2026-03-13 |
| urbit/urbit | 3621 → 3621 | 2026-08-21 |
| urbit/vere | 81 → 81 | 2026-08-20 |
| agent-network-protocol/AgentNetworkProtocol | 1390 → 1402 | 2026-08-18 |
| agent-network-protocol/anp (AgentConnect) | 340 → 342 | 2026-08-22 |
| decionis/agent-safe-pipeline | 469 → 533 (58 forks) | 2026-08-20 |
| agenticmail/agenticmail | 194 → 204 | 2026-08-13 |
| aeoess/agent-passport-system | 40 → 41 | 2026-08-21 |
| aeoess/agent-passport-python / -go / -mcp / -rust | 0 / 0 / 1 / 0 | 2026-08-21 / 08-19 / 08-21 / 08-15 |
| aeoess/aps-web | still 404 | — |
| Agent-Authority-Conformance/aps-conformance-suite | 1 → 1 | 2026-08-22 |
| Agent-Authority-Conformance/governance | 0 | 2026-08-19 |
| anivar/decern | 12 → 12 | 2026-08-18 |
| mishrasanjeev/grantex | 31 → 31 | 2026-08-21 |
| VibeTensor/attestix | 17 → 17 | 2026-08-20 |
| kevinkaylie/AgentNexus | 9 → 9 | 2026-07-29 |
| KestrelSovereignAI/kestrel-sovereign | 7 → 8 | 2026-08-23 |
| airlock-protocol/airlock | 2 → 2 | 2026-08-20 |
| chanceryhq/chancery | 25 → 25 | 2026-07-21 |
| AgentValet/AgentValet | 1 → 1 | 2026-08-12 |
| agentnameservice/ans | 35 → 35 | 2026-08-21 |
| agentnameservice/ans-registry | 28 → 29 | 2026-08-20 |
| agentnameservice/ans-sdk-go / -rust / -java | 5 / 6 / 3 | 2026-08-21 / 08-20 / 08-20 |
| agentnameservice/agent-trust-discovery | 2 → 2 | 2026-08-13 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 66 → 66 | 2026-08-20 |
| didit-protocol/skills | 24 → 26 | 2026-08-10 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 5 → 5 | 2026-08-22 |
| credat/credat | 2 → 2 | 2026-05-22 |
| dgverse-labs/helixid → **helixid/helixid** | 3 → 3 (repo moved) | 2026-08-23 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-08-23 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | still 404 | — |
| archetech/archon | 5 → 5 | 2026-08-23 |
| digitalbazaar/agent-credential-server | 0 → 0 | 2026-06-08 |
| MoltyCel/moltrust-api | 3 → 3 | 2026-08-20 |
| hypler-dev/LNSAT (discovery) | NEW: 1 | 2026-08-22 (created 2026-08-20) |

Live/README/protocol facts read directly on 2026-08-23:

- **MolTrust live API:** `GET https://api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-08-23 13:02:58.433879"}`; `/.well-known/did.json` still serves the `did:web:api.moltrust.ch` Ed25519 document; homepage title "The Trust Layer for the Agent Economy — MolTrust", meta description unchanged; `GET https://moltrust.ch/pricing` → **403 Forbidden (nginx/1.24.0, 162 bytes)** — pricing and Lightning status unverified this run.
- **Soulverse:** homepage title unchanged; npm registry checks for `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` all return 404.
- **IETF Datatracker:** `draft-kroehl-agentic-trust-aae-01`, `draft-narajala-ans-00`, `draft-pidlisnyi-aps-03` — no revision movement since 2026-08-16.
- **LNSAT README (`hypler-dev/LNSAT`):** "Execution authorization and evidence for consequential agent actions." Authority model binds "an agent's exact intended action to policy, approval, one-time authorization, execution, receipt, and reconciliation—independently of the model, protocol, or runtime." Explicitly: "Telemetry supports review and evidence; it never grants authority." Status badge: pre-release; CI source-verification badge; Apache-2.0.

## Interpretation

- **Bindu's lead keeps compounding (+160 this week, 8685★).** Weekly velocity is down from +245/+242 in the prior two cycles but still an order of magnitude above everything else tracked; the bridge/collaboration stance is unchanged.
- **Agent-Safe Pipeline sustained post-launch traction (469→533★, 58 forks)** — slower than launch week but still growing, which separates it from the decern/Chancery pattern (spike then stall). The service-boundary reference-architecture framing is where developer attention is consolidating; kernels (decern, flat 12★ third week) and IdPs (Chancery, flat 25★ third stalled cycle, no push since 2026-07-21) are not.
- **APS is executing with unusual consistency for a 41★ project:** main repo, Python/Go SDKs, MCP server, and the conformance suite all pushed within 2026-08-19/22. Multi-repo lockstep motion plus an IETF draft and a verification-only Rust crate remains the most disciplined institutionalization play in the set. Archon still has no public draft and no third-party verifier ecosystem.
- **MolTrust's 403 on `/pricing` is a new wrinkle.** The API is healthy and the DID document resolves, so this looks like edge/UA blocking rather than a takedown — but it means pricing and Lightning-roadmap claims could not be re-verified this cycle. Treat last verified values (2026-08-16: $19–$299/mo, Lightning "PhoenixD prepped, not settling") as stale until re-confirmed.
- **HelixID's move to a dedicated org** mirrors the APS conformance-org pattern at small scale — projects in this space are professionalizing their repo topology before they have traction. Watch whether the new org gains additional repos.
- **LNSAT is worth watching despite 1★:** it is the second project in two weeks (after Agent-Safe Pipeline) to ship the intent→authority→evidence pipeline as the core architecture, with explicit "telemetry never grants authority" separation. If it pushes consistently, promote next cycle.
- **Soulverse remains brochure-stage** (fifth consecutive week of npm 404s); no change to the watchlist classification.

## Source artifacts

- Main report: [Archon Competitive Analysis](/research/archon-competitive-analysis/)
- Executive summary: [Archon Competitive Analysis – Executive Summary](/research/archon-competitive-analysis/executive-summary/)
- LNSAT: <https://github.com/hypler-dev/LNSAT>
- HelixID (new org): <https://github.com/helixid/helixid>
- IETF: <https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/> · <https://datatracker.ietf.org/doc/draft-narajala-ans/> · <https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/>
- MolTrust: <https://moltrust.ch/> · API: <https://api.moltrust.ch> · repo: <https://github.com/MoltyCel/moltrust-api>
