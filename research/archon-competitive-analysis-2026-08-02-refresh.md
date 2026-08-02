---
layout: page
title: Archon Competitive Analysis – 2026-08-02 Refresh
permalink: /research/archon-competitive-analysis/2026-08-02-refresh/
---

# Archon Competitive Analysis – 2026-08-02 Refresh

**Refresh timestamp:** 2026-08-02 10:34 EDT<br>
**Scope:** Full GitHub API metadata sweep of all tracked repos, plus a discovery sweep for new entrants since 2026-07-21 (GitHub search: "agent identity DID", "verifiable credentials AI agent", "agent trust", "agent authorization", "ERC-8004", "agent passport"), plus live re-checks of MolTrust and Soulverse. One new project added: Agent Name Service (ANS).

## What changed

- **Full metadata refresh across all 31 tracked repos.** Headline deltas: Bindu 7488→8038★ (crossed 8k), ANP 1347→1378★, AgentConnect 326→337★, AgenticMail 166→182★, Agent Passport System 28→35★, Chancery 0→25★, hedera-agent-kit-js 64→66★, Motebit 4→5★. IDProva slipped 2→1★ and Chorus 2→1★.
- **Added Agent Name Service (ANS)** — the `agentnameservice` GitHub org shipping an IETF-draft-based (`draft-narajala-ans-00`) agent registry + transparency log: reference implementation 33★ (Go), registry 28★, Go/Rust/Java SDKs, and a companion Agent Trust Discovery index (2★). New profile in the main report.
- **Agent Passport System now has a visible SDK ecosystem.** Companion repos under `aeoess/` observed pushing 2026-08-01: `agent-passport-python`, `agent-passport-go`, `agent-passport-mcp`, `aps-conformance-suite` (byte-level conformance vectors), and `aps-web` (agent-passport.org site).
- **MolTrust re-checked live:** API still v2.5/healthy; Lightning still roadmap ("PhoenixD integration prepped, not yet settling"); public repo `moltycel/moltrust-api` at 3★, pushed 2026-08-02; AAE Internet-Draft still `draft-kroehl-agentic-trust-aae-00`.
- **Soulverse re-checked:** homepage unchanged (`The Operating System of Trust`); `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` still 404 on npm. No verified public SDK since 2026-07-15.
- **Discovery sweep found a dense tail of ERC-8004-adjacent trust/scoring experiments** created since 2026-07-21 (oculopus-protocol on Arc, parakletos on Solana, aegis ERC-8004↔DID/VC gateway, tcop receiver-bound evidence protocol tied to a USENIX Security 2027 paper, several "agent passport" clones). None added as profiles: all ≤1★, several READMEs are boilerplate. Logged as a signal only.
- Updated the main report (metadata, tracked-projects table, profiles incl. new ANS profile, discovery log) and the executive summary (bottom line, signals, snapshot table, tracking list). The competitive matrix retains its 2026-07-15 snapshot date.

## Evidence observed

GitHub REST API repo metadata, all fetched 2026-08-02 (unauthenticated, no rate-limit failures):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| GetBindu/Bindu | 7488 → 8038 | 2026-07-20 |
| urbit/urbit | 3616 → 3620 | 2026-07-31 |
| urbit/vere | 79 → 80 | 2026-07-31 |
| agent-network-protocol/AgentNetworkProtocol | 1347 → 1378 | 2026-08-02 |
| agent-network-protocol/anp (AgentConnect) | 326 → 337 | 2026-07-30 |
| agenticmail/agenticmail | 166 → 182 | 2026-07-28 |
| aeoess/agent-passport-system | 28 → 35 | 2026-08-01 |
| mishrasanjeev/grantex | 30 → 31 | 2026-07-31 |
| VibeTensor/attestix | 17 → 17 | 2026-08-01 |
| kevinkaylie/AgentNexus | 9 → 9 | 2026-07-29 |
| KestrelSovereignAI/kestrel-sovereign | 7 → 7 | 2026-08-02 |
| airlock-protocol/airlock | 2 → 2 | 2026-07-28 |
| chanceryhq/chancery | 0 → 25 | 2026-07-21 |
| AgentValet/AgentValet | 1 → 1 | 2026-07-05 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 64 → 66 | 2026-07-31 |
| didit-protocol/skills | 20 → 21 | 2026-07-31 |
| The-Nexus-Guard/aip | 15 → 15 | 2026-03-22 |
| vrknetha/clawdentity | 9 → 9 | 2026-04-22 |
| motebit/motebit | 4 → 5 | 2026-08-02 |
| credat/credat | 2 → 2 | 2026-05-22 |
| dgverse-labs/helixid | 3 → 3 | 2026-08-02 |
| techblaze-au/idprova | 2 → 1 | 2026-07-24 |
| a2al/A2AL | 1 → 1 | 2026-07-13 |
| LyonMask/chorus | 2 → 1 | 2026-06-28 |
| payelink/payelink-agent-identity-sdk | 2 → 2 | 2026-02-09 |
| dantber/agent-did | 0 → 0 | 2026-02-06 |
| yksanjo/agent-identity-hub | still 404 | — |
| archetech/archon | 5 → 5 | 2026-08-01 |
| digitalbazaar/agent-credential-server | 0 → 0 | 2026-06-08 |

New entrant — ANS ecosystem (all fetched 2026-08-02):

| Repo | Stars | Language | Pushed | Note |
|---|---|---|---|---|
| agentnameservice/ans | 33 | Go | 2026-07-30 | Reference implementation of ANS per IETF `draft-narajala-ans-00`: registry + transparency log |
| agentnameservice/ans-registry | 28 | — | 2026-07-23 | ANS registry based on the same draft |
| agentnameservice/ans-sdk-go / -rust / -java | 5 / 6 / 3 | Go/Rust/Java | 2026-07-22 / 2026-08-01 / 2026-07-31 | SDKs |
| agentnameservice/agent-trust-discovery | 2 | Go | 2026-07-31 | Trust Index: five-dimension trust vector (integrity, identity, solvency, behavior, safety), explainable scoring |

README/protocol facts read directly on 2026-08-02:

- **ANS (`agentnameservice/ans` README):** versioned DNS-style names `ans://v1.0.0.my-agent.example.com`; append-only Merkle transparency log; SCITT COSE_Sign1 receipts for point-in-time agent state; identity certificates signed by a private CA for agent mTLS; optional BYOC server certs + pinned TLSA records; offline CLI verifier (`ans-verify`); RA on :18080, TL on :18081.
- **Agent Trust Discovery README:** discovery-and-trust half of the ANS stack; per-agent Trust Vector across five spec-defined dimensions, each 0–100 with per-signal weight and human-readable explanation; `make demo-live` pulls a live production registry snapshot described as GoDaddy's ANS deployment (public Search API + Transparency Log) and produces real DNS/TLS probes.
- **IETF Datatracker:** `draft-narajala-ans-00` and `draft-kroehl-agentic-trust-aae-00` both still at revision -00.
- **MolTrust live API (2026-08-02):** `GET https://api.moltrust.ch/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-08-02 14:32:43"}`; `/.well-known/did.json` still serves the `did:web:api.moltrust.ch` Ed25519 document; homepage still lists Lightning as roadmap ("PhoenixD integration prepped, not yet settling").
- **Soulverse (2026-08-02):** homepage title unchanged; npm registry checks for `@soulverse/soul-id-sdk`, `@soulverse/trust-protocol-sdk`, `@soulverse/soul-ai-agent-sdk` all return 404.

## Interpretation

- **Bindu crossed 8,000★ (+550 in three weeks).** The DX/platform wedge keeps compounding; nothing else in the tracked set is within an order of magnitude. The collaboration/bridge framing remains the correct stance.
- **Chancery's 0→25★ jump is the sharpest relative move.** The enterprise agent-IdP framing (registry, scoped delegation, in-path MCP enforcement, instant revocation) is finding an audience. MCP enforcement is now a proven attention surface, not just a vocabulary.
- **APS is building a conformance moat.** Python/Go SDKs, an MCP server, and a byte-level conformance suite pushing in lockstep on 2026-08-01 means `did:aps` is positioning as a verifiable protocol, not a single repo. Archon's receipt/delegation story needs the same conformance-grade rigor to stay comparable.
- **ANS is the most structurally interesting new entrant.** It is a naming/registry + transparency-log play with SCITT COSE receipts and an IETF draft — closer to Archon's registry layer than to the authorization-layer crowd. It is also CA/DNS-anchored rather than content-addressed or P2P, so the sovereignty contrast with `did:cid` + Hyperswarm is clean. Watch whether the GoDaddy-affiliated deployment gains outside adoption.
- **The ERC-8004 tail is noise-heavy but real.** Dozens of ≤1★ repos since 2026-07-21 name ERC-8004 as their identity anchor. Most are hackathon-grade, but the pattern confirms ERC-8004 is becoming the default citation for on-chain agent identity in the EVM world — the same way did:wba became the citation for the protocol-spec world.
- **MolTrust and Soulverse are static this cycle.** MolTrust's Lightning rail is still not settling (Archon's Lightning adjacency remains a live differentiator); Soulverse still has no verifiable public SDK.

## Source artifacts

- Main report: [Archon Competitive Analysis](/research/archon-competitive-analysis/)
- Executive summary: [Archon Competitive Analysis – Executive Summary](/research/archon-competitive-analysis/executive-summary/)
- ANS: <https://github.com/agentnameservice/ans> · IETF draft: <https://datatracker.ietf.org/doc/html/draft-narajala-ans-00> · Trust Discovery: <https://github.com/agentnameservice/agent-trust-discovery>
- MolTrust: <https://moltrust.ch/> · API: <https://api.moltrust.ch> · repo: <https://github.com/moltycel/moltrust-api>
