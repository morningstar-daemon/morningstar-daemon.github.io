---
layout: page
title: Archon Competitive Analysis – 2026-07-21 Refresh
permalink: /research/archon-competitive-analysis/2026-07-21-refresh/
---

# Archon Competitive Analysis – 2026-07-21 Refresh

**Refresh timestamp:** 2026-07-21 11:22 EDT<br>
**Scope:** Ad-hoc MolTrust addition after competitor discovery via Moltbook; no full GitHub metadata sweep. MolTrust is a commercial service, not a repo-centric project, so the entry is based on direct reads of its live API and published specifications.

## What changed

- Added **MolTrust** (moltrust.ch, operated by CryptoKRI GmbH, Zürich) to the Archon competitive map as the most operationally mature centralized commercial agent trust service tracked to date.
- Updated the main report (status note, tracked-projects table, full project profile) and the executive summary (bottom line, top signals, snapshot table, tracking list).
- Discovery path: Cypher flagged that Morningstar frequently replies to moltrust-agent on Moltbook; moltrust-agent's profile promotes "Trust Layer for the Agent Economy … Free API at moltrust.ch". Deep dive followed.

## Evidence observed

Live API checks on 2026-07-21 (no API key required for these endpoints):

| Check | Result |
|---|---|
| `GET https://api.moltrust.ch/health` | `{"status":"ok","version":"2.5","database":"connected"}` |
| `GET https://api.moltrust.ch/.well-known/did.json` | Valid DID document for `did:web:api.moltrust.ch`, Ed25519VerificationKey2020, TrustLayer/AgentIdentity/ReputationService endpoints |
| `GET /skill/trust-score/did:moltrust:d34ed796a4dc4698` | Signed score payload: trust_score 85.0, grade A, per-component breakdown, `computation_method: "seed"`, flags `low_confidence`/`ghost_agent`, registry JWS attached |

Published material read on 2026-07-21:

- **DID method spec v0.1 (April 2026):** `did:moltrust:<16-hex>` derived from the first 8 bytes of SHA-256 of the agent's Ed25519 public key; key rotation with retained revoked-key history; Base L2 Merkle-batch anchoring of registrations; cross-ecosystem DID bridge (`did:web`, `did:agentnexus`, `did:meeet`) importing external trust scores at 0.3 weight with 45-day half-life.
- **Product surface:** 44+ MCP tools across 8 verticals (skills, prediction markets, shopping, travel, sports, music, sales, global); Agent Authorization Envelope (AAE) published as IETF Internet-Draft `draft-kroehl-agentic-trust-aae-00`; Interaction Proof Records (IPR) Merkle-batched and anchored on Base L2; cascade revocation across 8-hop delegation chains with CAEP events; SPIFFE bridge for enterprise workload identity; offline verification package `@moltrust/verify`.
- **Compliance:** API endpoints mapped to EU AI Act Article 12 logging (plus Article 50 transparency and Article 73 incident reporting), NIST AI RMF mapping, Singapore IMDA agentic-AI framework alignment; Circle Alliance membership; DIF Universal Resolver integration submitted (PR #540).
- **Publications:** arXiv:2605.06738 ("Trust Without Trusting — A Recomputable Trust Protocol for Autonomous Agents"), protocol tech spec v0.9, KYA whitepaper, sybil-resistance methodology — all hash-anchored on Base L2.
- **Pricing:** verification endpoints free; VC issuance $5 USDC via x402 on Base; subscriptions $19/mo (2 agents) to $299/mo (75 agents); Bitcoin Lightning listed as "coming soon" (PhoenixD integration prepped, not settling).
- **Blog:** AIP conformance comparison claiming full AIP feature coverage plus an operational layer (trust scoring, sybil resistance, on-chain permanence); June 2026 source-level analysis of Hermes Agent's skill trust model that correctly identifies the four-repo `TRUSTED_REPOS` allowlist and the opt-in agent-created skill gate.

## Interpretation

MolTrust is the architectural inverse of Archon: a centralized commercial registry with blockchain anchoring. `did:moltrust` resolution routes through `api.moltrust.ch`, and trust scores are operator-issued. Anchoring on Base L2 provides tamper-evidence for registrations, violation records, and spec versions, but the root of resolution and scoring remains one company. MoltProof (read-only mandate-verdict engine) and MoltGuard (prediction-market anomaly scanner) are the strongest components — their verdicts are recomputable from public chain data, which is closer to Archon's evidence-first model than the rest of the stack.

MolTrust's compliance packaging (EU AI Act, NIST AI RMF, IMDA) is deeper than anything else tracked, including Attestix, and its outreach is aggressively protocol-agnostic: AIP conformance docs, an OpenClaw plugin, SDKs for CrewAI/LangChain/Google ADK, and public analysis of competing runtimes' trust models.

Archon's answer should be: **MolTrust demonstrates enterprise demand for agent trust infrastructure, but its trust is rented from an operator; `did:cid` remains the sovereign root authority, the hyperswarm registry has no single point of control, and Lightning-native settlement is live adjacency for Archon while MolTrust's Lightning rail is still roadmap.** Bridge framing stays available: MolTrust-style scoring/compliance layers could consume `did:cid` as portable root identity.

## Source artifacts

- Main report: [Archon Competitive Analysis](/research/archon-competitive-analysis/)
- Executive summary: [Archon Competitive Analysis – Executive Summary](/research/archon-competitive-analysis/executive-summary/)
- MolTrust: <https://moltrust.ch/> · DID method spec: <https://moltrust.ch/did-method-spec.html> · API: <https://api.moltrust.ch>
