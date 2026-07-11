---
layout: page
title: Archon Competitive Analysis – 2026-07-11 Refresh
permalink: /research/archon-competitive-analysis/2026-07-11-refresh/
---

# Archon Competitive Analysis – 2026-07-11 Refresh

**Refresh timestamp:** 2026-07-11 11:07 EDT<br>
**Scope:** GitHub metadata refresh, live competitor table updates, matrix cleanup, and promotion of Chancery/AgentValet into the tracked landscape.

## What changed

- Updated repo metadata for tracked Archon competitors and adjacent infrastructure using the GitHub API.
- Promoted **Chancery** into the main report as an agent IdP / MCP enforcement / revocation / audit watchlist item.
- Promoted **AgentValet** into the main report as an enterprise IGA / credential governance / MCP proxy watchlist item.
- Refreshed the executive summary, project table, major profile metadata, strategic signals, action items, resource links, and discovery log.
- Rebuilt the competitive matrix and removed the stale duplicate matrix fragment left under the 2026-07-05 snapshot.

## Metadata observed

| Repo | Stars | Language | Last pushed | Description signal |
|------|-------|----------|-------------|--------------------|
| archetech/archon | 5 | TypeScript | 2026-07-10 | did:cid reference implementation |
| GetBindu/Bindu | 7488 | Python | 2026-07-06 | identity, communication, and payments layer for AI agents |
| urbit/urbit | 3616 | Hoon | 2026-07-10 | personal server / P2P / identity substrate incumbent |
| agent-network-protocol/AgentNetworkProtocol | 1347 | HTML | 2026-07-08 | open protocol for agent communication |
| agent-network-protocol/anp | 326 | Python | 2026-07-05 | ANP SDK / AgentConnect implementation path |
| agenticmail/agenticmail | 166 | TypeScript | 2026-06-21 | email/SMS/phone-call infrastructure for AI agents |
| aeoess/agent-passport-system | 28 | TypeScript | 2026-07-10 | delegation narrowing, gateway enforcement, signed receipts |
| mishrasanjeev/grantex | 30 | TypeScript | 2026-07-11 | identity, authorization, and audit infrastructure |
| VibeTensor/attestix | 17 | Python | 2026-07-09 | DID identity, VCs, EU AI Act compliance, MCP tools |
| chanceryhq/chancery | 0 | Go | 2026-07-11 | agent IdP, scoped delegation, in-path MCP enforcement, revocation, audit |
| AgentValet/AgentValet | 1 | TypeScript | 2026-07-05 | IGA for AI agents, SPIFFE/AuthZEN/CIBA, MCP proxy |
| hashgraph/hedera-agent-kit-js | 64 | TypeScript | 2026-07-09 | Hedera agent tooling remains fresher than old DID repos |

## Strategic interpretation

The 2026-07-11 refresh reinforces the same market shift: root identity matters, but buyers and developers increasingly evaluate the whole authority path — who grants scope, where enforcement happens, how revocation propagates, what receipt exists afterward, and whether the flow maps to MCP/API/payment rails.

The strongest Archon positioning remains: **`did:cid` as sovereign root authority, composable with external enforcement, transport, payment, and audit rails.** Chancery and AgentValet make the enterprise version of that pressure explicit; Bindu and APS make the developer/DX version explicit.

## Source artifacts

- Metadata capture: `tmp/research/repo-meta.jsonl` in the site repo working tree at refresh time.
- Main report: [Archon Competitive Analysis](/research/archon-competitive-analysis/)
- Executive summary: [Archon Competitive Analysis – Executive Summary](/research/archon-competitive-analysis/executive-summary/)
