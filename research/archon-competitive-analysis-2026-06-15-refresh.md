---
layout: page
title: Competitive Intel Refresh – 2026-06-15
permalink: /research/archon-competitive-analysis/2026-06-15-refresh/
---

# 2026-06-15 Competitive Intel Refresh

**Completed:** 2026-06-15 09:26 EDT
**Scope:** Full metadata refresh for tracked competitors, addition of Self / self.xyz as a new adjacent competitor section, main report update, executive summary update, and dated refresh log.

## What Changed

### Repo metadata re-verified

Verified via GitHub API on 2026-06-15:

| Project | Previous stars | Current stars | Notes |
|---------|----------------|---------------|-------|
| Archon | 4 | 5 | Active push on 2026-06-15 |
| ANP | 1301 | 1330 | Still the protocol/spec mindshare leader |
| AgentConnect | 308 | 321 | ANP implementation/SDK path continues to grow |
| Self | N/A | 1249 | Added as major adjacent human-proof / sybil-resistance primitive |
| AgenticMail | 129 | 147 | Transport traction still rising |
| Grantex | 25 | 27 | Delegated authorization / commerce audit watchlist item |
| Attestix | 16 | 16 | Active push on 2026-06-14; compliance positioning remains strong |
| didit skills | 13 | 16 | Adjacent KYC/verification skills |
| AIP | 13 | 13 | No star movement; still a trust-chain benchmark |
| clawdentity | 9 | 9 | Closest messaging/identity philosophical rival, slower recent movement |
| Motebit | 4 | 4 | Active push on 2026-06-14; sovereign runtime + signed receipts watchlist item |
| Credat | 2 | 2 | Identity/delegation/verification SDK watchlist item |
| HelixID | 1 | 1 | Active push on 2026-06-11; DID/VC authorization-layer watchlist item |
| IDProva | 1 | 2 | Enterprise identity/audit receipts watchlist item |
| A2AL | 0 | 1 | Decentralized discovery/networking watchlist item |
| Chorus | 0 | 2 | P2P encrypted communication watchlist item |
| payelink-agent-identity-sdk | 2 | 2 | No traction change |
| agent-did | 0 | 0 | No traction change |
| agent-identity-hub | N/A | N/A | Still 404 / unavailable |

### New project added: Self

- **Self / self.xyz** — privacy-preserving identity wallet and protocol for generating ZK proofs from government-issued IDs such as passports, ID cards, and Aadhaar.
- Public site title/description now explicitly frames Self as identity and agent infrastructure for humans and AI agents.
- README positions the core use cases as airdrop protection, social media humanity checks, quadratic funding sybil resistance, wallet recovery, and compliance.
- Competitive classification: **adjacent, not equivalent**. Self proves human/document attributes; Archon proves agent identity, delegated authority, provenance, and receipts.

### Strategic reframing

The report now emphasizes a sharper market structure:

1. **Identity is becoming the root of authority**, not the whole product.
2. **Human-proof identity is a distinct adjacent layer.** Self can be a complement for proving a human/controller exists behind a flow, but it does not replace agent-side identity or action provenance.
3. **Authorization and audit are first-class competitive dimensions.** Grantex, Credat, HelixID, IDProva, Motebit, and Attestix all point this direction.
4. **Communication protocol and transport layers are pulling visible adoption.** ANP/AgentConnect and AgenticMail remain the clearest signals.
5. **DID method competition is not enough to track.** The important question is which stack proves who may do what, under whose authority, with what evidence afterward.

## Main Takeaways

- Archon's strongest differentiator is still sovereign agent identity substrate: did:cid, decentralized registry, credentials, and substrate independence.
- Self is a high-traction adjacent project but should not be framed as a decentralized agent DID competitor; its trust root is human/document-centric.
- The market is rewarding concrete action flows: delegated auth, transport, compliance, receipts, human-proof gates, and commerce.
- Archon should present identity as the anchor for verifiable action, not as an abstract DID endpoint.
- ANP/AgentConnect deserves a direct comparison because DID-WBA continues gaining implementation gravity.
- Self deserves a boundary note because human proof complements agent authority; it does not replace it.

## Files Updated

- `research/archon-competitive-analysis.md` — main report refreshed and Self section added
- `research/archon-competitive-analysis-executive-summary.md` — executive summary updated to current market view
- `research/archon-competitive-analysis-2026-06-15-refresh.md` — this refresh log

## Data Sources

- GitHub REST API (`/repos/{owner}/{repo}`)
- Self public site (`https://self.xyz`), including title/description and search-index text
- Self GitHub README (`https://github.com/selfxyz/self`)
- README / metadata inspection for selected high-signal projects
- Prior manual review notes from 2026-05-23 for retained feature context

## Next Refresh

**Scheduled trigger:** next weekly evangelism sweep or any material repo shift: major star movement, repo disappearance, new DID method, high-traction human-proof identity project, or emergence of an authorization/receipt/payment-control layer with visible adoption.

> For full context, read the [main competitive analysis](/research/archon-competitive-analysis/) and the [executive summary](/research/archon-competitive-analysis/executive-summary/).
