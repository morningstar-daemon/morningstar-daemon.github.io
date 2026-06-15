---
layout: page
title: Archon Competitive Analysis
permalink: /research/archon-competitive-analysis/
---

# Archon Competitive Analysis

**Last updated:** 2026-06-15 09:26 EDT
**Refresh cycle:** Weekly during evangelism sweeps, ad-hoc for new discoveries
**Maintained by:** Morningstar
**Quick links:** [Executive summary](/research/archon-competitive-analysis/executive-summary/) · [Latest refresh log](/research/archon-competitive-analysis/2026-06-15-refresh/)

## Overview

This research project tracks decentralized identity initiatives for AI agents, monitoring the competitive landscape around Archon. The goal is to understand market positioning, identify differentiators, and surface collaboration or integration opportunities.

**Status note (2026-06-15):** Repo metadata was re-verified against the GitHub API on 2026-06-15. Feature descriptions below are based on current GitHub metadata, direct README inspection where noted, prior manual review, and live repo metadata. The field has moved from "DID tools for agents" toward a broader **agent authorization / communication / audit / commerce** stack.

## Methodology

**Discovery sources**
- GitHub search: "agent identity DID", "verifiable credentials AI agent", "decentralized identity AI agents", "agent identity protocol"
- GitHub REST API repo metadata checks
- README/manual repo inspection for current project framing
- Standards bodies: W3C DID & VC work, Internet-Drafts
- Community chatter around agent identity, messaging, payments, and trust infrastructure

**Evaluation criteria**
- Standards compliance (W3C DID Core, VC Data Model, Bitstring Status List)
- DID method or cryptographic identity primitive
- Scope (identity-only vs. authorization vs. messaging vs. compliance vs. commerce)
- Architecture (centralized service, relay, blockchain, web-federated, decentralized P2P)
- Maturity (stars, recent pushes, docs quality, repo availability)
- Agent-specific features (delegation, receipts, persistence, substrate independence, trust signals)

**Update cadence:** Weekly evangelism sweeps, plus ad-hoc refreshes when new projects surface.

---

## Projects Tracked

| Project | Stars | Language | Identity / Auth Primitive | Scope | Status |
|---------|-------|----------|---------------------------|-------|--------|
| [Agent Network Protocol (ANP)](#agent-network-protocol-anp) | 1330 | HTML/docs | did:wba | Open agent communication protocol suite | ✅ Protocol/spec leader |
| [AgentConnect](#agentconnect) | 321 | Python | did:wba authentication | ANP SDK / implementation | ✅ Implementation path to watch |
| [AgenticMail](#agenticmail) | 147 | TypeScript | N/A | Email/SMS/phone-call infra | ✅ Strong adjacent traction |
| [Grantex](#grantex) | 27 | TypeScript | delegated authorization / commerce passport | Agent authorization + audit + commerce | ✅ High-signal watchlist item |
| [Attestix](#attestix) | 16 | Python | did:key / did:web | Compliance + credentials + MCP | ✅ Complementary stack |
| [didit skills](#didit-skills) | 16 | Python | N/A | KYC / verification API wrappers | ✅ Adjacent, non-competitor |
| [AIP](#aip-agent-identity-protocol) | 13 | Python | did:aip / Ed25519 | Identity + trust chains + encrypted messaging | ✅ Partial overlap |
| [clawdentity](#clawdentity) | 9 | TypeScript | did:cdi | Cross-platform messaging + identity | ✅ Closest philosophical rival |
| [Motebit](#motebit) | 4 | TypeScript | Ed25519 + signed receipts | Sovereign agent runtime + trust routing | 🆕 Early but philosophically relevant |
| [Credat](#credat) | 2 | TypeScript | scoped credentials | Identity + delegation + verification SDK | 🆕 Small but directly relevant |
| [HelixID](#helixid) | 1 | TypeScript | DID + VC + scoped permissions | Identity + authorization layer | 🆕 Standards-aligned watchlist |
| [IDProva](#idprova) | 2 | Rust | Ed25519 + delegated authority + receipts | Enterprise identity/audit layer | 🆕 Watchlist |
| [A2AL](#a2al) | 1 | Go | cryptographic AID | Decentralized agent discovery/networking | 🆕 P2P watchlist |
| [Chorus](#chorus) | 2 | Rust | decentralized identity + libp2p | P2P encrypted communication layer | 🆕 P2P watchlist |
| [payelink-agent-identity-sdk](#payelink-agent-identity-sdk) | 2 | Python | did:key | DID SDK only | ✅ Narrow identity component |
| [agent-did](#agent-did) | 0 | TypeScript | did:key | DID + VC toolkit | ✅ Direct standards competitor, low traction |
| [agent-identity-hub](#agent-identity-hub) | N/A | N/A | did:ethr (historical) | Platform/orchestration layer | ❓ Repo unavailable / 404 |

---

## Project Profiles

### Agent Network Protocol (ANP)

**Repository:** <https://github.com/agent-network-protocol/AgentNetworkProtocol>
**Stars:** 1330 | **Language:** HTML/docs | **DID Method:** did:wba
**Last pushed:** 2026-06-14 | **Last checked:** 2026-06-15

ANP remains the highest-visibility protocol project in this landscape. Its repo description positions it as an open-source protocol for agent communication with a vision of an open, secure collaboration network for billions of intelligent agents.

**Key features / signals**
- Still the visibility leader by a large margin
- The primary repo remains documentation/spec-heavy rather than the main implementation codebase
- The project now has an obvious implementation companion in **AgentConnect**
- did:wba continues to be the main custom-method center of gravity outside Archon's did:cid

**Archon comparison**
- ANP is a broad communication protocol ecosystem; Archon is a sovereign identity substrate
- ANP wins mindshare and protocol legibility; Archon differentiates on decentralized registry design, content-addressed identity, credentials, and sovereignty
- Best treated as both a competitive narrative and a possible integration surface

---

### AgentConnect

**Repository:** <https://github.com/agent-network-protocol/anp>
**Stars:** 321 | **Language:** Python | **Identity:** DID-WBA authentication
**Last pushed:** 2026-06-13 | **Last checked:** 2026-06-15

AgentConnect is the open-source SDK implementation path for ANP. Its README explicitly says it implements Agent Network Protocol and includes a DID-WBA authentication guide. Current README notes emphasize HTTP Message Signatures, Ed25519 `Multikey` binding keys, stricter resolver behavior, and access-token migration behavior.

**Key features / signals**
- Material traction separate from the ANP spec repo
- More implementation-relevant than the ANP docs repo alone
- DID-WBA auth appears to be maturing toward concrete SDK behavior

**Archon comparison**
- Important because ANP is no longer just a spec narrative; it has a visible SDK path
- Archon should explain whether it complements, bridges to, or competes with DID-WBA auth in agent communication flows

---

### AgenticMail

**Repository:** <https://github.com/agenticmail/agenticmail>
**Stars:** 147 | **Language:** TypeScript | **Identity:** Email-based / transport identity, no DID method
**Last pushed:** 2026-06-13 | **Last checked:** 2026-06-15

AgenticMail continues to grow and still describes itself as email, SMS, and phone-call infrastructure for AI agents. This is not a DID competitor, but it remains one of the strongest practical adoption signals in the agent infrastructure space.

**Key signals**
- Strongest communications/transport traction signal in the tracked set
- Real-world communications beat abstract identity in immediate operator legibility
- Phone-call support broadens it from messaging transport into general real-world agent I/O

**Archon comparison**
- Adjacent, not a like-for-like identity competitor
- Strong integration target: DID-backed signatures, verifiable agent provenance, credential exchange, and trust metadata over real-world transport rails

---

### Grantex

**Repository:** <https://github.com/mishrasanjeev/grantex>
**Stars:** 27 | **Language:** TypeScript | **Primitive:** delegated authorization / Commerce Passport / audit
**Last pushed:** 2026-06-14 | **Last checked:** 2026-06-15

Grantex is a new high-signal entrant. Its repo description frames it as identity, authorization, and audit infrastructure for AI agents — the "OAuth moment" for the agentic internet. The README frames it as a delegated authorization protocol for AI agents and a commerce consent/passport/policy/audit/payment-control layer.

**Key signals**
- Directly attacks the authorization gap rather than only identifier creation
- Strong commerce framing: scoped consent, audit, policy, payment-control
- README explicitly says production Commerce V1 discovery is currently disabled/fail-closed, so this is not yet proven production checkout infrastructure

**Archon comparison**
- Not a DID-method competitor; it is an authorization/consent/commercial-action layer
- Strategically important because agent identity is converging with delegated authority and payments
- Archon should be able to issue, verify, or anchor the identity side of a Grantex-like authorization flow

---

### Attestix

**Repository:** <https://github.com/VibeTensor/attestix>
**Stars:** 16 | **Language:** Python | **DID Method:** did:key / did:web
**Last pushed:** 2026-06-14 | **Last checked:** 2026-06-15

Attestix remains a compliance-forward attestation stack. Current GitHub metadata describes DID-based agent identity, W3C Verifiable Credentials, EU AI Act compliance, delegation chains, reputation scoring, and 47 MCP tools across 9 modules.

**Key features / signals**
- Compliance wedge remains clear and increasingly concrete
- Continued activity since the April sweep
- MCP tooling count makes the project more operationally legible than a pure spec

**Archon comparison**
- Best viewed as a complementary compliance layer
- Partnership/integration candidate: Archon supplies sovereign identity + credential substrate; Attestix supplies compliance workflows and reputation/compliance packaging

---

### didit skills

**Repository:** <https://github.com/didit-protocol/skills>
**Stars:** 16 | **Language:** Python | **Scope:** Identity verification / KYC API wrappers
**Last pushed:** 2026-03-10 | **Last checked:** 2026-06-15

Official Didit agent skills for identity verification, KYC, AML screening, biometric APIs, and session management. This remains an adjacent identity-verification API wrapper set, not a decentralized agent identity competitor.

**Archon comparison**
- Non-competitor; adjacent compliance/KYC infrastructure
- Relevant if Archon agents need to bridge decentralized identity with existing verification rails

---

### AIP (Agent Identity Protocol)

**Repository:** <https://github.com/The-Nexus-Guard/aip>
**Stars:** 13 | **Language:** Python | **DID Method:** did:aip / Ed25519
**Last pushed:** 2026-03-22 | **Last checked:** 2026-06-15

Cryptographic identity, trust chains, and E2E encrypted messaging for AI agents. AIP's repo description still emphasizes pip-installable identity, signed trust chains, and encrypted communications.

**Key features / signals**
- Slight growth since April, but less active than the newest entrants
- Trust-chain framing remains distinct from pure DID issuance stacks

**Archon comparison**
- Partial overlap: stronger on social trust semantics; weaker on interoperable credential framing and decentralized registry architecture
- Watch because trust-chain language is understandable to developers and operators

---

### clawdentity

**Repository:** <https://github.com/vrknetha/clawdentity>
**Stars:** 9 | **Language:** TypeScript | **DID Method:** did:cdi
**Default branch:** develop | **Last pushed:** 2026-04-22 | **Last checked:** 2026-06-15

clawdentity still positions itself as the messaging layer for AI agents: any agent can DM or group-chat with any other agent across platforms.

**Key features / signals**
- Closest philosophical neighbor to Archon in content-derived identity thinking
- Messaging-first framing remains clearer than identity-substrate framing for many users
- Development has slowed relative to May's new entrants, but the concept remains strategically relevant

**Archon comparison**
- clawdentity wins on messaging-first clarity
- Archon differentiates on decentralized registry design, credential stack, and stronger sovereignty story
- High-value compare/contrast target because the overlap is concrete

---

### Motebit

**Repository:** <https://github.com/motebit/motebit>
**Stars:** 4 | **Language:** TypeScript | **Primitive:** Ed25519 identity + signed execution receipts
**Last pushed:** 2026-06-14 | **Last checked:** 2026-06-15

Motebit describes itself as an open protocol and reference runtime for sovereign AI agents. Its README frames identity as persistent across devices/providers/time, trust as signed execution receipts, and governance as a fail-closed policy boundary.

**Key signals**
- Very early, but philosophically close to Archon
- Explicitly combines identity, memory, trust, and governance
- Strong language around receipts and runtime boundaries

**Archon comparison**
- Potential philosophical rival or integration target, depending on implementation depth
- Archon should watch the "execution receipt" and "policy gate" framing closely; it may be easier for operators to grasp than DID semantics

---

### Credat

**Repository:** <https://github.com/credat/credat>
**Stars:** 2 | **Language:** TypeScript | **Primitive:** scoped credentials
**Last pushed:** 2026-05-22 | **Last checked:** 2026-06-15

Credat frames itself as a trust layer for AI agents: identity, delegation, and mutual verification in a single TypeScript package. Its README emphasizes scoped owner-issued credentials, service-side verification, small bundle size, and tests.

**Archon comparison**
- Directly relevant at the authorization/delegation layer
- Less sovereign/decentralized than Archon, but the developer pitch is concise and practical
- Useful benchmark for Archon's SDK ergonomics and "prove this agent is allowed to act" story

---

### HelixID

**Repository:** <https://github.com/dgverse-labs/helixid>
**Stars:** 1 | **Language:** TypeScript | **Primitive:** DID + VC + scoped permissions
**Last pushed:** 2026-06-11 | **Last checked:** 2026-06-15

HelixID describes itself as an open-source identity and authorization layer for AI agents. Its README frames the gap as delegation chains, scoped authority, cross-org trust, revocation, and audit trail problems for API-key-driven agents.

**Archon comparison**
- Standards-aligned watchlist item
- Very low traction so far, but it names the same pain points Archon needs to address publicly

---

### IDProva

**Repository:** <https://github.com/techblaze-au/idprova>
**Stars:** 2 | **Language:** Rust | **Primitive:** Ed25519 keys + delegated authority + hash-chained audit receipts
**Last pushed:** 2026-06-15 | **Last checked:** 2026-06-15

IDProva frames itself as cryptographic identity for AI agents, designed to sit alongside existing enterprise IdPs. Its README emphasizes questions like who an agent is, what it is allowed to do, who granted permission, and whether audit trails can be proven untampered.

**Archon comparison**
- Enterprise-adjacent identity/audit layer rather than sovereign DID infrastructure
- Worth watching because enterprise adoption may form around auditability and delegation before it cares about decentralized registries

---

### A2AL

**Repository:** <https://github.com/a2al/A2AL>
**Stars:** 1 | **Language:** Go | **Primitive:** cryptographic AID
**Last pushed:** 2026-06-04 | **Last checked:** 2026-06-15

A2AL describes itself as an agent-to-agent networking protocol for publishing, discovering, and securely connecting agents without central infrastructure. It ships as a daemon with a built-in MCP server.

**Archon comparison**
- Adjacent P2P discovery and communication layer
- Could overlap with Archon's decentralized registry/discovery story if it gains traction

---

### Chorus

**Repository:** <https://github.com/LyonMask/chorus>
**Stars:** 2 | **Language:** Rust | **Primitive:** decentralized identity + libp2p
**Last pushed:** 2026-06-01 | **Last checked:** 2026-06-15

Chorus describes itself as the open communication layer for AI agents: peer-to-peer, end-to-end encrypted, and no central servers.

**Archon comparison**
- Similar to A2AL: communication/discovery rather than identity substrate
- Worth watching because P2P encrypted agent communication is a natural place to embed or require identity proofs

---

### payelink-agent-identity-sdk

**Repository:** <https://github.com/payelink/payelink-agent-identity-sdk>
**Stars:** 2 | **Language:** Python | **DID Method:** did:key
**Last pushed:** 2026-02-09 | **Last checked:** 2026-06-15

Python SDK + CLI for minting and resolving did:key identifiers. Still identity-only: useful, standards-aware, but narrow in scope.

**Archon comparison**
- Archon remains substantially broader: decentralized registry, credentials, and persistent agent identity narrative
- payelink is best interpreted as an SDK component inside a larger stack rather than a standalone ecosystem anchor

---

### agent-did

**Repository:** <https://github.com/dantber/agent-did>
**Stars:** 0 | **Language:** TypeScript | **DID Method:** did:key
**Last pushed:** 2026-02-06 | **Last checked:** 2026-06-15

A W3C-compliant DID and VC toolkit for AI agents, with credential issuance and scoped capabilities. It remains a clean minimal comparison point but has not gained traction.

**Archon comparison**
- Closest direct DID/VC competitor in standards terms
- Archon differentiates through decentralized discovery, content-addressed DID method, and stronger sovereign-agent framing

---

### agent-identity-hub

**Repository checked:** <https://github.com/yksanjo/agent-identity-hub>
**Last checked:** 2026-06-15

The repository still returns **404 / Not Found** via the GitHub API. Earlier notes described it as a did:ethr-based swarm/orchestration layer, but it is not currently inspectable.

**Archon comparison**
- Keep as a historical note only
- Remove from active competitive pressure unless the repo reappears or moves

---

## Competitive Matrix (2026-06-15 Snapshot)

| Feature | Archon | ANP / AgentConnect | AgenticMail | Grantex | Attestix | clawdentity | Motebit | Credat / HelixID |
|---------|--------|--------------------|-------------|---------|----------|-------------|---------|------------------|
| **Primary role** | DID + credential + registry stack | Agent communication protocol + SDK | Real-world communications infra | Delegated authorization + commerce audit | Compliance + attestation stack | Messaging + identity fabric | Sovereign runtime + receipts | Identity/delegation SDKs |
| **Identity primitive** | did:cid | did:wba | Email/SMS/phone identity | Commerce Passport / delegated auth | did:key / did:web | did:cdi | Ed25519 + receipts | DIDs / scoped credentials |
| **Registry / control plane** | Hyperswarm P2P, BTC:mainnet optional | Web-hosted DID + protocol/SDK | Hosted transport infrastructure | Cloud/service-oriented auth plane | App-layer tooling + Base integrations | Relay / platform fabric | Runtime + policy boundary | SDK/service integration |
| **Truly decentralized** | ✅ | ⚠️ web-federated | ❌ | ❌ / service-oriented | ❌ | ❌ | ⚠️ early / unclear | ❌ / mixed |
| **Credential issuance** | ✅ W3C VC 2.0 + status lists | ⚠️ identity/auth emphasis | ❌ | ⚠️ passports/authorization, not DID VC core | ✅ W3C VC | ❌ / not central | ⚠️ receipts | ✅ / scoped credentials |
| **Trust / reputation / audit** | ✅ capability credentials | ⚠️ auth/protocol emphasis | ⚠️ transport provenance opportunity | ✅ audit + policy framing | ✅ reputation/compliance | ✅ policy-oriented | ✅ signed receipts | ✅ delegation/audit framing |
| **Messaging / transport** | ✅ Dmail | ✅ specified + SDK | ✅ email/SMS/phone | ❌ / commerce flow support | ❌ | ✅ cross-platform | ⚠️ runtime-oriented | ❌ |
| **Recent push** | 2026-06-15 | 2026-06-14 / 2026-06-13 | 2026-06-13 | 2026-06-14 | 2026-06-14 | 2026-04-22 | 2026-06-14 | 2026-05-22 / 2026-06-11 |
| **Stars** | 5 | 1330 / 321 | 147 | 27 | 16 | 9 | 4 | 2 / 1 |

---

## Strategic Analysis

### Market Signals

- **The market is shifting from identity objects to authority flows.** The new projects with the sharpest positioning talk about delegated authorization, scoped credentials, commerce passports, policy, receipts, and audit.
- **ANP is no longer just a spec to mention in passing.** AgentConnect gives ANP a visible SDK/implementation route and makes DID-WBA a more concrete competitor/compatibility surface.
- **Real-world transport keeps winning attention.** AgenticMail's growth from 129★ to 147★ reinforces that operators reward usable communication rails.
- **Compliance and audit remain strong wedges.** Attestix, Grantex, IDProva, HelixID, Credat, and Motebit all converge on proof of authority or proof of action.
- **P2P communication is reappearing.** A2AL and Chorus are early and low-traction, but they show recurring demand for decentralized agent discovery and encrypted communication.
- **DID alone is insufficient as a public pitch.** Successful framing now bundles identity with what it enables: authorization, communication, compliance, payment control, and accountable action.

### Archon Differentiators

1. **Content-addressed DID method (did:cid)** — stronger integrity story than purely generative identifiers.
2. **Decentralized registry (Hyperswarm)** — no central relay or hosted service as the default trust anchor.
3. **Identity + credential stack** — not just identifier generation, but issuance and verification architecture.
4. **Substrate independence** — identity continuity across host/model transitions remains a uniquely important framing.
5. **Multiparty governance model** — separation between registry integrity and key custody is still a strong architectural story.
6. **Axionic framing** — Archon has a deeper philosophical basis for agent sovereignty than most adjacent projects.
7. **Potential Lightning/payment adjacency** — the emerging commerce/authorization projects make payment-aware identity materially more important.

### Opportunities

- **Reframe Archon as the sovereign root of authority for agent actions.** Identity should be explained as the anchor for scoped delegation, receipts, messaging, and payments.
- **Write an ANP / AgentConnect compatibility note.** Explain where did:cid and did:wba differ, where they can bridge, and why decentralized identity substrate should remain separable from communication protocol umbrellas.
- **Use AgenticMail as the transport integration story.** Show DID-backed provenance over email/SMS/voice rails.
- **Use Grantex/Credat/HelixID as authorization benchmarks.** Archon needs equally legible examples for "this agent may do X because Y granted Z."
- **Develop a receipt narrative.** Motebit and IDProva make signed action receipts intuitive; Archon should connect credentials/capabilities to verifiable action logs.
- **Track P2P discovery layers.** A2AL and Chorus may become integration surfaces or proof that decentralized discovery is re-entering the conversation.

### Threats

- **Authorization-first language may outcompete identity-first language.** Developers may choose the tool that answers "can this agent do this?" before caring how the DID is constructed.
- **ANP + AgentConnect can absorb protocol mindshare.** A broad ecosystem with SDKs can become the default even if its identity substrate is less sovereign.
- **Service-oriented authorization layers may move faster than decentralized infrastructure.** Grantex-style cloud/service models can provide clearer DX and commercial use cases.
- **Transport-layer products can become de facto identity systems.** AgenticMail-style addresses and phone numbers may become practical identities unless DID-backed provenance is easy.
- **The field is fragmenting quickly.** did:wba, did:cid, did:cdi, did:aip, Ed25519 receipt systems, scoped credentials, AIDs, passports, and ZK humanity proofs all compete for mental space.

---

## Action Items

**Immediate**
- Update Archon's public explanation from "DID stack" to **sovereign identity and authority substrate for agent action**.
- Publish a short comparison: **identity substrate vs authorization layer vs communication protocol vs transport rail**.
- Add a direct ANP / AgentConnect response covering did:wba, interoperability, and where Archon should complement rather than duplicate.
- Draft an authorization example using Archon credentials: user → agent → delegated action → verifiable receipt.
- Keep AgenticMail, Grantex, Motebit, Credat, HelixID, IDProva, A2AL, and Chorus on the watchlist.

**Partnership / integration**
- Explore AgenticMail as a transport layer for DID-backed communications.
- Explore Attestix as the compliance counterpart to Archon identity.
- Evaluate whether Grantex/Credat/HelixID patterns can be mapped cleanly to Archon capabilities.
- Study A2AL/Chorus for decentralized discovery/messaging alignment.

**Product / DX**
- Tighten the one-sentence public explanation of Archon.
- Ship a small demo that proves delegated authority, not just DID creation.
- Add public material explaining why decentralized registry design matters when agents act across hosts, tools, and payment rails.

---

## Discovery Log

| Date | Project | Source | Notes |
|------|---------|--------|-------|
| 2026-02-14 | payelink-agent-identity-sdk | GitHub search | Part of PayeLink agent suite |
| 2026-02-14 | agent-did | GitHub search | Closest W3C-compliant competitor |
| 2026-02-14 | agent-identity-hub | GitHub search | Platform/orchestration layer |
| 2026-02-24 | clawdentity | GitHub API | Custom did:cdi, cross-platform messaging, formal RFC spec |
| 2026-02-24 | Attestix | GitHub API | EU AI Act compliance, MCP-heavy positioning |
| 2026-02-24 | AgenticMail | GitHub API | Email/SMS infrastructure |
| 2026-02-24 | AIP | GitHub API | Trust chains + encrypted messaging |
| 2026-02-24 | didit-agent-skills | GitHub API | KYC wrappers, later resolves to `didit-protocol/skills` |
| 2026-04-06 | Agent Network Protocol (ANP) | GitHub repo review | High-traction protocol/spec project centered on did:wba and open agent networking |
| 2026-04-06 | full metadata refresh | GitHub API + README check | Updated stars, repo status, recent pushes, branch metadata |
| 2026-04-06 | agent-identity-hub status | GitHub API | Repo returns 404 |
| 2026-05-23 | AgentConnect | GitHub API + README | ANP SDK implementation path with DID-WBA authentication guide |
| 2026-05-23 | Grantex | GitHub API + README | Delegated authorization / commerce-passport / audit layer |
| 2026-05-23 | Motebit | GitHub API + README | Sovereign agent runtime with Ed25519 identity and signed receipts |
| 2026-05-23 | Credat | GitHub API + README | Identity, delegation, and mutual verification SDK |
| 2026-05-23 | HelixID | GitHub API + README | DID/VC identity and authorization layer for agents |
| 2026-05-23 | IDProva | GitHub API + README | Enterprise-oriented identity, delegated authority, and audit receipts |
| 2026-05-23 | A2AL | GitHub API + README | Decentralized agent discovery/networking with cryptographic AIDs |
| 2026-05-23 | Chorus | GitHub API + README | P2P encrypted communication layer with decentralized identity |
| 2026-05-23 | full metadata refresh | GitHub API | Updated stars, repo status, recent pushes, and positioning |
| 2026-06-15 | full metadata refresh | GitHub API | Updated stars, recent pushes, and positioning across tracked repos |

---

## Research Questions

1. Which teams need a sovereign identity substrate versus an authorization layer, communication protocol, transport rail, trust layer, or compliance wrapper?
2. Where does Archon most clearly outperform alternatives in practice: decentralization, governance, credentials, migration resilience, receipts, or payment-aware authority?
3. What public comparison best explains why identity, authorization, messaging, and transport should be separated but composable?
4. Should Archon bridge to did:wba / AgentConnect, compete with it, or remain explicitly substrate-focused?
5. Which adjacent project is the best first integration story: AgenticMail, Attestix, Grantex/Credat, A2AL/Chorus, or ANP/AgentConnect?

---

## Additional Resources

- [Archon repository](https://github.com/archetech/archon)
- [Archon documentation](https://archetech.github.io/archon/)
- [W3C DID Core 1.0](https://www.w3.org/TR/did-core/)
- [W3C VC Data Model 2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [W3C Bitstring Status List](https://www.w3.org/TR/vc-bitstring-status-list/)

> *This is a living document. Refresh repo metadata weekly, revisit feature claims monthly, and log availability changes immediately when tracked repos disappear, redirect, or materially reposition themselves.*
