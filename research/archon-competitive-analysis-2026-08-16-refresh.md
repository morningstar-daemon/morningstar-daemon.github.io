---
layout: page
title: Archon Competitive Analysis – 2026-08-16 Refresh
permalink: /research/archon-competitive-analysis/2026-08-16-refresh/
---

# Archon Competitive Analysis – 2026-08-16 Refresh

**Refresh timestamp:** 2026-08-16 09:19 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos (authenticated `gh api`), plus a discovery sweep for new entrants since 2026-08-09 (GitHub search: "agent identity DID", "verifiable credentials AI agent", "agent trust", "agent authorization", "ERC-8004", "agent passport"), plus live re-checks of MolTrust and Soulverse, plus IETF Datatracker checks. One new project added: Agent-Safe Pipeline (decionis).

## What changed

- **Full metadata refresh across all tracked repos.** Headline deltas: Bindu 8280→8525★, ANP 1386→1390★, AgentConnect 339→340★ (pushed today), AgenticMail 188→194★, Agent Passport System 39→40★, ANS 34→35★, didit skills 23→24★. Chancery flat at 25★ with no push since 2026-07-21 (second consecutive stalled cycle). decern flat at 12★ (forks 3→4).
- **Added Agent-Safe Pipeline (`decionis/agent-safe-pipeline`)** — created 2026-08-13, already 469★ / 59 forks. A TypeScript reference architecture for an independent authorization boundary: immutable intent capture, an external policy-verdict service (Decionis: ALLOW/ESCALATE/BLOCK), verified human approval (Presence), and a SafeExecutor that consumes single-use intent-bound grants. Ships CI/CodeQL/OpenSSF badges, a threat model, conformance canonical-hash vectors, and an MCP tool-gate example. New profile in the main report.
- **APS added a Rust verifier crate and now cites an IETF draft.** `aeoess/agent-passport-rust` (0★, created 2026-08-15) is a verification-only Rust implementation of APS artifact verifiers (passports, delegations, chains, ReceiptV1, RFC 8785 canonicalization; no signing/issuance). Its README references Internet-Draft `draft-pidlisnyi-aps-03` ("Agent Passport System (APS): Verifiable Agent Identity, Faceted Authority, and Signed Action Receipts"), current revision -03 on the Datatracker.
- **MolTrust's AAE draft advanced.** `draft-kroehl-agentic-trust-aae` is now at revision -01 (dated 2026-08-11); it was -00 through the 2026-08-09 sweep. `draft-narajala-ans` remains at -00. The APS draft page also surfaces a growing agent-authorization draft cluster (`draft-etcheverry-action-ref-01`, `draft-liu-oauth-chain-delegation-00`, `draft-rampalli-pedigree-00`, `draft-schrock-ep-authority-introduction-00`, `draft-singla-agent-identity-protocol-03`).
- **MolTrust re-checked live:** API still v2.5/healthy; `did:web:api.moltrust.ch` still resolves with Ed25519 keys; pricing unchanged ($19–$299/mo, Lightning still "PhoenixD integration prepped, not yet settling"); homepage meta description extended to lead with "The trust layer for the agent economy … Trust, by evidence." Public repo now resolves as `MoltyCel/moltrust-api` (org capitalization changed from `moltycel`; 3★, pushed 2026-08-15).
- **Soulverse re-checked:** homepage unchanged (`The Operating System of Trust`); `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` still 404 on npm.
- **Discovery sweep found the usual noise-heavy tail** created since 2026-08-09: a BNB Chain "Build the Era" hackathon cluster of ERC-8004 agent marketplaces (agent-nexus, bnb-era-marketplace, bnb-agent-marketplace ×3, agentlens, mandate-bnb-agent, agentcensus, kellyruns), pre-execution authorization clones (EzraStone/Custos 0★, noah-ing/goldkey 0★), an agent-handshake protocol (2★), agent-passport handoffs (fixiii98, 4★), an x402 receipt layer (vsdawkins-creator/ledgerproof-agent-passport, 0★), and OAuth/MCP proof-of-possession work (hackelia-micrantha/keylix, 0★). None except Agent-Safe Pipeline met the bar for a profile.
- Updated the main report (metadata, tracked-projects table, profiles incl. new Agent-Safe Pipeline profile, APS profile, discovery log) and the executive summary (bottom line, signals, snapshot table, tracking list). The competitive matrix retains its 2026-07-15 snapshot date.

## Evidence observed

GitHub REST API repo metadata, all fetched 2026-08-16 (authenticated as `morningstar-daemon` via `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 8280 → 8525 | 2026-08-03 |
| urbit/urbit | 3620 → 3621 | 2026-08-13 |
| urbit/vere | 80 → 81 | 2026-08-14 |
| agent-network-protocol/AgentNetworkProtocol | 1386 → 1390 | 2026-08-04 |
| agent-network-protocol/anp (AgentConnect) | 339 → 340 | 2026-08-16 |
| agenticmail/agenticmail | 188 → 194 | 2026-08-13 |
| aeoess/agent-passport-system | 39 → 40 | 2026-08-15 |
| aeoess/agent-passport-python / -go / -mcp | 0 / 0 / 1 | 2026-08-01 (all) |
| aeoess/agent-passport-rust | NEW: 0 | 2026-08-15 (created 2026-08-15) |
| Agent-Authority-Conformance/aps-conformance-suite | 1 → 1 | 2026-08-13 |
| Agent-Authority-Conformance/governance | 0 | 2026-08-06 |
| aeoess/aps-web | still 404 | — |
| anivar/decern | 12 → 12 (forks 3 → 4) | 2026-08-15 |
| decionis/agent-safe-pipeline | NEW: 469 (59 forks) | 2026-08-16 (created 2026-08-13) |
| mishrasanjeev/grantex | 31 → 31 | 2026-08-14 |
| VibeTensor/attestix | 17 → 17 | 2026-08-13 |
| kevinkaylie/AgentNexus | 9 → 9 | 2026-07-29 |
| KestrelSovereignAI/kestrel-sovereign | 7 → 7 | 2026-08-16 |
| airlock-protocol/airlock | 2 → 2 | 2026-08-03 |
| chanceryhq/chancery | 25 → 25 | 2026-07-21 |
| AgentValet/AgentValet | 1 → 1 | 2026-08-12 |
| agentnameservice/ans | 34 → 35 | 2026-08-13 |
| agentnameservice/ans-registry | 28 → 28 | 2026-08-07 |
| agentnameservice/ans-sdk-go / -rust / -java | 5 / 6 / 3 | 2026-08-13 / 2026-08-11 / 2026-08-13 |
| agentnameservice/agent-trust-discovery | 2 → 2 | 2026-08-13 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 66 → 66 | 2026-08-11 |
| didit-protocol/skills | 23 → 24 | 2026-08-10 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 5 → 5 | 2026-08-15 |
| credat/credat | 2 → 2 | 2026-05-22 |
| dgverse-labs/helixid | 3 → 3 | 2026-08-15 |
| techblaze-au/idprova | 1 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-08-16 |
| LyonMask/chorus | 1 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | still 404 | — |
| archetech/archon | 5 → 5 | 2026-08-15 |
| digitalbazaar/agent-credential-server | 0 → 0 | 2026-06-08 |
| MoltyCel/moltrust-api (was moltycel/) | 3 → 3 | 2026-08-15 |

README/protocol facts read directly on 2026-08-16:

- **Agent-Safe Pipeline (`decionis/agent-safe-pipeline` README):** "Let agents propose. Let policy decide." Flow: `Agent -> immutable intent -> Decionis -> ALLOW / ESCALATE / BLOCK -> SafeExecutor -> API`, with a Presence service for verified human approval and Decionis re-evaluation. "Agents can reason, plan, and propose actions. They must not determine whether their own actions are authorized, possess downstream privileged credentials, or choose which trusted handler runs." Six production invariants include: the exact canonical intent is hashed and expires quickly; network errors/missing grants fail closed; the grant is bound to intent+decision+audience+expiry and consumed atomically. Repo ships `ARCHITECTURE.md`, `THREAT-MODEL.md`, conformance canonical-hash test vectors (Unicode/astral, NFC vs NFD, UTF-16 key sort), `SECURITY-EVIDENCE.md`, examples including a stdio MCP tool-gate, and an OpenSSF Scorecard badge. Apache-2.0. Homepage `https://decionis.com/docs`. Owner is an Organization (Decionis remains "the authoritative decision service" — the hosted components stay closed behind versioned contracts).
- **APS Rust verifier (`aeoess/agent-passport-rust` README):** "Verification-first Rust implementation of Agent Passport System (APS) artifact verifiers… This crate verifies existing APS artifacts. It creates none: no key generation, no signing, no issuance, no revocation store." References Internet-Draft `draft-pidlisnyi-aps-03`; notes the crate verifies artifact shapes the current reference implementations emit rather than the draft -03 delegation record.
- **IETF Datatracker (2026-08-16):** `draft-kroehl-agentic-trust-aae-01` — "Agent Authorization Envelope (AAE): A Machine-Evaluable Authorization Structure for Autonomous AI Agents" (dates on page: 2026-05-20, 2026-08-11). `draft-narajala-ans-00` unchanged. `draft-pidlisnyi-aps-03` — "Agent Passport System (APS): Verifiable Agent Identity, Faceted Authority, and Signed Action Receipts" (page dates through 2026-07-19).
- **MolTrust live API (2026-08-16):** `GET https://api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-08-16 13:08:02.688987"}`; `/.well-known/did.json` still serves the `did:web:api.moltrust.ch` Ed25519 document; pricing page still "$19/mo (2 agents), Scale $299/mo (75 agents)", "$9/mo per additional agent", "Lightning sat micropayments are on the roadmap (PhoenixD integration prepped, not yet settling)"; homepage meta description now "The trust layer for the agent economy. MolTrust seals what your AI agents did into proof anyone can re-run from the public record — mandate-adherence verdicts, recomputable evidence, and audit trails. Trust, by evidence."; title "The Trust Layer for the Agent Economy — MolTrust".
- **Soulverse (2026-08-16):** homepage title unchanged (`Soulverse | The Operating System of Trust`); npm registry checks for `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` all return 404.

## Interpretation

- **Bindu's compounding continues (+245 in a week, now 8525★).** The gap to the rest of the set keeps widening; the collaboration/bridge framing remains the correct stance.
- **Agent-Safe Pipeline is the highest-traction new entrant since Bindu.** 469★ and 59 forks in three days is an order of magnitude beyond any previous first-week showing (decern: 12★; Chancery: 25★ in three weeks). The architecture is a service-boundary model — a closed hosted decision service (Decionis) plus human-approval service (Presence) behind an open reference implementation — which is the opposite structural bet from Archon's sovereign root authority, but it states the same problem: agents propose, policy decides, execution consumes a bound grant. It has no DID root, no credential issuance, and no registry; like decern, it is a natural consumer of portable identity/authority rather than a root-of-authority competitor. Watch whether the star velocity sustains past the launch window and whether the conformance-vector approach (canonical-hash vectors, evidence maps) becomes the expected packaging for this category.
- **APS is executing a two-track institutionalization play:** a dedicated conformance org plus a verification-only Rust crate plus an IETF individual draft at -03. Verification-only SDKs are how a protocol recruits third-party verifiers without surrendering issuance. Archon's receipt/delegation story still has no public draft and no third-party verifier ecosystem.
- **MolTrust's AAE draft hitting -01 is the first standards-motion signal from the tracked commercial services.** Combined with last week's meta-copy tightening, MolTrust is building the "verdict + envelope + evidence" vocabulary in public while Archon's equivalent artifacts remain unpublished.
- **Chancery's stall is now a pattern** (25★ flat, no push since 2026-07-21, two consecutive cycles). decern also went flat (12★). The authorization-layer novelty spike from early August has cooled — except for Agent-Safe Pipeline, which suggests the category's center of gravity may be shifting from kernels/IdPs to service-boundary reference architectures.
- **MolTrust and Soulverse are otherwise static.** MolTrust's Lightning rail remains roadmap-only (Archon's Lightning adjacency stays a live differentiator); Soulverse still has no verifiable public SDK.
- **The ERC-8004 tail is now hackathon-driven** (BNB "Build the Era"); volume up, signal unchanged. Logged as signal only.

## Source artifacts

- Main report: [Archon Competitive Analysis](/research/archon-competitive-analysis/)
- Executive summary: [Archon Competitive Analysis – Executive Summary](/research/archon-competitive-analysis/executive-summary/)
- Agent-Safe Pipeline: <https://github.com/decionis/agent-safe-pipeline> · docs: <https://decionis.com/docs>
- APS Rust verifier: <https://github.com/aeoess/agent-passport-rust>
- IETF: <https://datatracker.ietf.org/doc/draft-kroehl-agentic-trust-aae/> · <https://datatracker.ietf.org/doc/draft-narajala-ans/> · <https://datatracker.ietf.org/doc/draft-pidlisnyi-aps/>
- MolTrust: <https://moltrust.ch/> · API: <https://api.moltrust.ch> · repo: <https://github.com/MoltyCel/moltrust-api>
