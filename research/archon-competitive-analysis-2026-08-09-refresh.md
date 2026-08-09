---
layout: page
title: Archon Competitive Analysis – 2026-08-09 Refresh
permalink: /research/archon-competitive-analysis/2026-08-09-refresh/
---

# Archon Competitive Analysis – 2026-08-09 Refresh

**Refresh timestamp:** 2026-08-09 09:10 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos, plus a discovery sweep for new entrants since 2026-08-02 (GitHub search: "agent identity DID", "verifiable credentials AI agent", "agent trust", "agent authorization", "ERC-8004", "agent passport"), plus live re-checks of MolTrust and Soulverse. One new project added: decern.

## What changed

- **Full metadata refresh across all tracked repos.** Headline deltas: Bindu 8038→8280★, ANP 1378→1386★, AgentConnect 337→339★, AgenticMail 182→188★, Agent Passport System 35→39★, ANS 33→34★, didit skills 21→23★. Chancery flat at 25★ with no push since 2026-07-21.
- **Added decern (`anivar/decern`)** — created 2026-08-02, already 12★ / 3 forks. A Rust deterministic authorization kernel: one principal type for humans/agents/workloads, 9 safety invariants machine-checked by the cvc5 SMT solver across the entire input space, an AuthZEN-shaped PDP HTTP API, and a signed hash-chained decision ledger with offline verification (`decern verify`). Thin clients for Python/TypeScript/Go; Zenodo DOI. New profile in the main report.
- **APS conformance suite moved orgs.** `aeoess/aps-conformance-suite` now redirects to `Agent-Authority-Conformance/aps-conformance-suite` (1★, pushed 2026-08-07); the new org also hosts a `governance` repo (0★, pushed 2026-08-06). `aeoess/aps-web` returns 404. APS is institutionalizing its conformance/governance surface.
- **MolTrust re-checked live:** API still v2.5/healthy; `did:web:api.moltrust.ch` still resolves with Ed25519 keys; pricing unchanged ($19–$299/mo, Lightning still "PhoenixD integration prepped, not yet settling"); homepage meta description now leads with "mandate-adherence verdicts, recomputable evidence, and audit trails." Public repo `moltycel/moltrust-api` at 3★, pushed 2026-08-06.
- **Soulverse re-checked:** homepage unchanged (`The Operating System of Trust`); `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` still 404 on npm.
- **IETF Datatracker:** `draft-narajala-ans` and `draft-kroehl-agentic-trust-aae` both still at revision -00.
- **Discovery sweep found the usual noise-heavy tail** created since 2026-08-02: ERC-8004 marketplaces on BSC/Arc (thesio, agripinaa, assay-bsc, era-market, agentpay), several "agent passport" clones (marcelogdomingues/agent-passport — offline did:key+VC, 0★), an AP2/Visa TAP Go implementation (SkylinePlatform/agentic-payments, 0★), MCP policy proxies (johnnydoer/mcpguard, 0★), and boilerplate (trustless-agent-substrate, README is one line). None except decern met the bar for a profile.
- Updated the main report (metadata, tracked-projects table, profiles incl. new decern profile, discovery log) and the executive summary (bottom line, signals, snapshot table, tracking list). The competitive matrix retains its 2026-07-15 snapshot date.

## Evidence observed

GitHub REST API repo metadata, all fetched 2026-08-09 (unauthenticated; rate limit hit near the end of the sweep, after all tracked repos were fetched):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 8038 → 8280 | 2026-08-03 |
| urbit/urbit | 3620 → 3620 | 2026-08-07 |
| urbit/vere | 80 → 80 | 2026-08-09 |
| agent-network-protocol/AgentNetworkProtocol | 1378 → 1386 | 2026-08-04 |
| agent-network-protocol/anp (AgentConnect) | 337 → 339 | 2026-08-09 |
| agenticmail/agenticmail | 182 → 188 | 2026-08-06 |
| aeoess/agent-passport-system | 35 → 39 | 2026-08-07 |
| aeoess/agent-passport-python / -go / -mcp | 0 / 0 / 1 | 2026-08-01 (all) |
| Agent-Authority-Conformance/aps-conformance-suite | (moved from aeoess) 1 | 2026-08-07 |
| Agent-Authority-Conformance/governance | 0 | 2026-08-06 |
| aeoess/aps-web | now 404 | — |
| anivar/decern | NEW: 12 (3 forks) | 2026-08-09 (created 2026-08-02) |
| mishrasanjeev/grantex | 31 → 31 | 2026-08-09 |
| VibeTensor/attestix | 17 → 17 | 2026-08-09 |
| kevinkaylie/AgentNexus | 9 → 9 | 2026-07-29 |
| KestrelSovereignAI/kestrel-sovereign | 7 → 7 | 2026-08-09 |
| airlock-protocol/airlock | 2 → 2 | 2026-08-03 |
| chanceryhq/chancery | 25 → 25 | 2026-07-21 |
| AgentValet/AgentValet | 1 → 1 | 2026-07-05 |
| agentnameservice/ans | 33 → 34 | 2026-08-04 |
| agentnameservice/ans-registry | 28 → 28 | 2026-08-07 |
| agentnameservice/ans-sdk-go / -rust / -java | 5 / 6 / 3 | 2026-07-22 / 2026-08-03 / 2026-08-06 |
| agentnameservice/agent-trust-discovery | 2 → 2 | 2026-07-31 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 66 → 66 | 2026-08-06 |
| didit-protocol/skills | 21 → 23 | 2026-07-31 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 5 → 5 | 2026-08-05 |
| credat/credat | 2 → 2 | 2026-05-22 |
| dgverse-labs/helixid | 3 → 3 | 2026-08-04 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-08-05 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | still 404 | — |
| archetech/archon | 5 → 5 | 2026-08-08 |
| digitalbazaar/agent-credential-server | 0 → 0 | 2026-06-08 |
| moltycel/moltrust-api | 3 → 3 | 2026-08-06 |

README/protocol facts read directly on 2026-08-09:

- **decern (`anivar/decern` README):** "The industry standardizes how authority is *represented* — tokens, delegation envelopes, decision-request formats — and defers the *guarantee* … to implementer policy. decern is the guarantee." Decision = pure function of `(principal, authority graph, policy, now)`; humans, agents, workloads are one principal type. 9 invariants discharged by cvc5 across the entire input space: money-gate, isolation, decay, attenuation-edge, scope-gate, revocation-gate, residency-gate, role-gate, consent-gate. AuthZEN-shaped `/access/v1/evaluation` endpoint; `decern verify --ledger … --pubkey …` re-checks the hash chain and every signature offline. Clients: `uv add decern`, `npm install decern`, `go get github.com/anivar/decern/sdks/go`. Apache-2.0. Zenodo DOI 10.5281/zenodo.21848620.
- **APS org move (GitHub API):** `api.github.com/repos/aeoess/aps-conformance-suite` → 301 → `Agent-Authority-Conformance/aps-conformance-suite`, description "Byte-level conformance vectors for Agent Passport System implementations. JCS ca[nonicalization…]"; sibling repo `Agent-Authority-Conformance/governance` pushed 2026-08-06.
- **IETF Datatracker:** `draft-narajala-ans-00` and `draft-kroehl-agentic-trust-aae-00` both still at revision -00.
- **MolTrust live API (2026-08-09):** `GET https://api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-08-09 13:04:44.201942"}`; `/.well-known/did.json` still serves the `did:web:api.moltrust.ch` Ed25519 document; pricing page still "$19/mo (2 agents), Scale $299/mo (75 agents)", "$9/mo per additional agent", "Lightning sat micropayments are on the roadmap (PhoenixD integration prepped, not yet settling)"; homepage meta description now "MolTrust seals what your AI agents did into proof anyone can re-run from the public record — mandate-adherence verdicts, recomputable evidence, and audit trails."
- **Soulverse (2026-08-09):** homepage title unchanged; npm registry checks for `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` all return 404.

## Interpretation

- **Bindu's compounding continues (+242 in a week).** Nothing else in the tracked set is within an order of magnitude; the collaboration/bridge framing remains the correct stance.
- **decern is the most technically serious authorization-layer entrant since Chancery.** Formal-methods posture (SMT-checked invariants over the whole input space) plus an offline-verifiable decision ledger is exactly the "guarantee, not representation" wedge the APS/Chancery/AgentValet cluster gestures at. It has no DID root or registry — which makes it a natural bridge target: Archon credentials and delegation chains could be the authority graph a decern-class PDP decides over. If it keeps its early traction, expect it to become the citation for "authorization with machine-checked guarantees."
- **APS moving conformance into its own org is an institutionalization signal.** Separating byte-level conformance vectors and governance from the product repo is how protocols present themselves as multi-implementation standards. Archon's receipt/delegation story still lacks an equivalent public conformance artifact.
- **Chancery stalled this cycle** (25★ flat, no push since 2026-07-21). One flat week proves nothing, but the MCP-enforcement novelty spike has cooled; decern may be absorbing the "serious authorization" attention.
- **MolTrust and Soulverse are static again.** MolTrust's Lightning rail remains roadmap-only (Archon's Lightning adjacency stays a live differentiator); Soulverse still has no verifiable public SDK. MolTrust's meta-description shift toward "mandate-adherence verdicts, recomputable evidence" tightens its evidence-first marketing — it is converging on Archon's receipt vocabulary from the centralized side.
- **The ERC-8004/BSC tail remains noise.** Marketplaces and soulbound-passport clones keep appearing at ≤1★; logged as signal only.

## Source artifacts

- Main report: [Archon Competitive Analysis](/research/archon-competitive-analysis/)
- Executive summary: [Archon Competitive Analysis – Executive Summary](/research/archon-competitive-analysis/executive-summary/)
- decern: <https://github.com/anivar/decern> · site: <https://decern.anivar.net/>
- APS conformance: <https://github.com/Agent-Authority-Conformance/aps-conformance-suite> · governance: <https://github.com/Agent-Authority-Conformance/governance>
- IETF: <https://datatracker.ietf.org/doc/draft-narajala-ans/> · <https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/>
- MolTrust: <https://moltrust.ch/> · API: <https://api.moltrust.ch> · repo: <https://github.com/moltycel/moltrust-api>
