---
layout: page
title: Archetech Competitive Analysis – 2026-08-02 Refresh
permalink: /research/archetech-competitive-analysis/2026-08-02-refresh/
---

# Archetech Competitive Analysis – 2026-08-02 Refresh

**Refresh timestamp:** 2026-08-02 10:35 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (positioning, blogs, pricing, docs), plus a discovery scan for new company-level entrants and sector news (funding, eIDAS 2.0). No protocol/repo metadata sweep — that lives on the Archon page.

## What changed

- **Added MolTrust as a sixth pressure group: commercial agent trust services.** Company-level profile added (positioning, pricing, differentiation); protocol-level detail stays on the [Archon page](/research/archon-competitive-analysis/).
- **Microsoft Entra Agent ID documented as a named product surface.** Entra is no longer just VC tooling — it now ships dedicated agent-identity docs (dated 2026-06-19).
- **cheqd homepage now leads with "Credentials & AI Agents"** and promotes a Vouched integration for AI-agent identity (post dated 2026-06-03).
- **Affinidi shipped an Agent Gateway narrative** — blog post "Agent Gateway: A New Era of Governed AI Agents Interactions" dated 2026-07-24; agent-trust content now dominates its blog.
- **KILT downgraded to effectively inactive.** `www.kilt.io` failed to connect (curl status 000), `kilt.io` still 404; successor effort Primer Systems is x402 privacy payments, not identity.
- **Ceramic / 3Box Labs downgraded to effectively inactive.** Both `ceramic.network` and `www.3boxlabs.com` returned 404.
- Updated the main report: pressure groups, competitive map, profiles (cheqd, Affinidi, Microsoft, KILT, Ceramic, +MolTrust), market-pressure summary, source links.

## Evidence observed

Live site checks on 2026-08-02 (curl, desktop UA):

| Check | Result |
|---|---|
| `learn.microsoft.com/en-us/entra/agent-id/` | HTTP 200, title "Microsoft Entra Agent ID documentation", `ms.date` 2026-06-19, meta: "Build, secure, and manage agent identities with Microsoft Entra Agent ID … apply Zero Trust principles, and govern agent access at scale." |
| `cheqd.io` og:description | "Decentralised Infrastructure for Credentials & AI Agents Built for digital identity, verifiable credentials, agentic ecosystems, and trusted data payments" |
| cheqd blog: Vouched post | HTTP 200, "How cheqd and Vouched Are Building Trust in AI Agents", `article:published_time` 2026-06-03 |
| `affinidi.com/blog` | Latest post "Agent Gateway: A New Era of Governed AI Agents Interactions", dated 2026-07-24; also "Why Agent Identity is the Missing Piece in Enterprise AI Governance" |
| `moltrust.ch/pricing.html` | HTTP 200; "$19/mo (2 agents), Scale $299/mo (75 agents)", "$9/mo per additional agent", "Lightning sat micropayments are on the roadmap (PhoenixD integration prepped, not yet settling)" |
| `www.kilt.io` | curl status 000 (connection failure); `kilt.io` 404 |
| `ceramic.network` / `www.3boxlabs.com` | Both 404 |
| `primer.systems` | Live, title "Primer Systems - x402 and Privacy Architecture" |
| `didit.me` | HTTP 200, "One API for identity and fraud … $0.33 per full KYC" — assessed low-relevance KYC/fraud API, not added |

Discovery/news scans on 2026-08-02: decentralized-identity funding search surfaced only Didit's $2M seed (KYC API, low relevance); eIDAS 2.0 / EUDI Wallet 2026 developer-guide content continues to proliferate (sector context, no new vendor added). MATTR and SpruceID blog URLs 404'd during this sweep — homepage positioning unchanged.

## Interpretation

- **The incumbent wedge into agent identity is now named and documented.** Microsoft Entra Agent ID is the sharpest incumbent move observed to date: it frames agent identity as IAM governance under Zero Trust, exactly the buyer-expectation capture this page warns about. Archetech's counter remains that IAM-governed agent identity is rented from the platform; `did:cid` is portable root authority.
- **SSI vendors are converging on the agent narrative.** cheqd ("Credentials & AI Agents" + Vouched) and Affinidi (Agent Gateway) have moved agent identity from thought leadership to homepage/product surface in the last month. The company-level race for agent-trust mindshare is real and accelerating.
- **MolTrust validates the category while renting trust.** It is the clearest proof that enterprises will pay for agent trust infrastructure — and the clearest foil: scoring and resolution route through one operator's API.
- **Two ecosystem-pressure entries went dark.** KILT and Ceramic losing their public web presence removes two Web3-native identity narratives from active competition; Hedera, Synonym/Pubky, Nostr, and Urbit remain the live ecosystem pressure.

## Source artifacts

- Main report: [Archetech Competitive Analysis](/research/archetech-competitive-analysis/)
- Microsoft Entra Agent ID: <https://learn.microsoft.com/en-us/entra/agent-id/>
- cheqd × Vouched: <https://cheqd.io/blog/how-cheqd-and-vouched-are-building-trust-in-ai-agents/>
- Affinidi blog: <https://www.affinidi.com/blog>
- MolTrust: <https://moltrust.ch/> · pricing: <https://moltrust.ch/pricing.html>
- Primer Systems: <https://primer.systems/>
