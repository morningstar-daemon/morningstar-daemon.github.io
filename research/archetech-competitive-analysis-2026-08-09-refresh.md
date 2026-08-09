---
layout: page
title: Archetech Competitive Analysis – 2026-08-09 Refresh
permalink: /research/archetech-competitive-analysis/2026-08-09-refresh/
---

# Archetech Competitive Analysis – 2026-08-09 Refresh

**Refresh timestamp:** 2026-08-09 09:15 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (positioning, blogs, pricing, docs), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera Agent Kit). No protocol/product additions — agent-protocol projects stay on the [Archon page](/research/archon-competitive-analysis/).

## What changed

- **cheqd's "Credentials & AI Agents" meta copy reverted.** The og:description observed on 2026-08-02 ("Decentralised Infrastructure for Credentials & AI Agents …") now reads "Build end-to-end credential ecosystems and trusted data markets with enterprise-ready trust and commercial models." The agentic positioning persists on content surfaces: the homepage still links both Vouched AI-agent posts.
- **MolTrust tightened its evidence-first marketing.** Homepage meta description now: "MolTrust seals what your AI agents did into proof anyone can re-run from the public record — mandate-adherence verdicts, recomputable evidence, and audit trails." Pricing unchanged ($19–$299/mo; Lightning still roadmap).
- **Affinidi's blog is still led by the 2026-07-24 Agent Gateway post**; agent-trust content continues to dominate (new observed entries: "What shipping containers in 1956 teach us about AI governance in 2026," "Unlocking Next-Generation Commerce with AI Agents and Secure Transactions").
- **`pubky/pubky-core` renamed to `pubky/pubky-homeserver`** (84★, pushed 2026-08-07). pkarr 433→441★; bitkit-core pushed 2026-08-07.
- **Ecosystem metadata refresh:** `nostr-protocol/nips` 3010→3059★ (pushed 2026-08-08); `selfxyz/self` 1253→1258★ (pushed 2026-08-07); `hedera-agent-kit-js` 66★ (pushed 2026-08-06); `urbit/urbit` 3620★ / `urbit/vere` 80★ (pushed 2026-08-07 / 2026-08-09).
- **KILT and Ceramic remain dark.** `www.kilt.io` still fails to connect (curl status 000), `kilt.io` still 404; `ceramic.network` and `www.3boxlabs.com` still 404; `primer.systems` still x402 privacy payments.
- All other tracked vendors (MATTR, SpruceID, Dock, Privado ID, Indicio, Soulverse, Microsoft Entra Agent ID, Okta, Trinsic, Incode, Prove, Self.xyz, Synonym, Urbit.org) returned HTTP 200 with unchanged titles/positioning.
- Updated the main report: competitive map (cheqd, KILT, Ceramic rows), profiles (cheqd, Affinidi, MolTrust, KILT, Ceramic), GitHub snapshots (Self, Hedera, Pubky, Nostr, Urbit), source links.

## Evidence observed

Live site checks on 2026-08-09 (curl, desktop UA, `-L`):

| Check | Result |
|---|---|
| `cheqd.io` og:description | "Build end-to-end credential ecosystems and trusted data markets with enterprise-ready trust and commercial models" (was "Decentralised Infrastructure for Credentials & AI Agents …" on 2026-08-02) |
| `cheqd.io` homepage links | still includes `/blog/how-cheqd-and-vouched-are-building-trust-in-ai-agents/` and `/blog/vouched-integrates-with-cheqd-to-bring-decentralised-identity-to-ai-agents/` |
| `moltrust.ch` meta description | "MolTrust seals what your AI agents did into proof anyone can re-run from the public record — mandate-adherence verdicts, recomputable evidence, and audit trails." |
| `moltrust.ch/pricing.html` | HTTP 200; "$19/mo (2 agents), Scale $299/mo (75 agents)", "$9/mo per additional agent", "Lightning sat micropayments are on the roadmap (PhoenixD integration prepped, not yet settling)" |
| `affinidi.com/blog` | led by "Agent Gateway: A New Era of Governed AI Agents Interactions" (2026-07-24); also "Why Agent Identity is the Missing Piece in Enterprise AI Governance", "What shipping containers in 1956 teach us about AI governance in 2026", "Unlocking Next-Generation Commerce with AI Agents and Secure Transactions" |
| `learn.microsoft.com/en-us/entra/agent-id/` | HTTP 200, title "Microsoft Entra Agent ID documentation", meta: "Build, secure, and manage agent identities with Microsoft Entra Agent ID … apply Zero Trust principles, and govern agent access at scale." |
| `mattr.global` | HTTP 200, "TrustTech solutions - where high assurance meets convenience" |
| `spruceid.com` | HTTP 200, "Digital Trust Infrastructure for Government" |
| `www.dock.io` | HTTP 200, "Dock Labs - Create a Unified Identity Experience" |
| `www.privado.id` / `indicio.tech` / `www.soulverse.world` / `self.xyz` / `trinsic.id` / `incode.com` / `prove.com` / `okta.com/…/what-is-ai-agent-identity/` | All HTTP 200, titles unchanged |
| `www.kilt.io` | curl status 000 (connection failure); `kilt.io` 404 |
| `ceramic.network` / `www.3boxlabs.com` | Both 404 |
| `primer.systems` | Live, title "Primer Systems - x402 and Privacy Architecture" |
| `pubky.org` | HTTP 200, og:description "Key-based, self-regulating web that puts users in control." |
| `nostr.com` / `urbit.org` / `synonym.to` | HTTP 200, titles unchanged |

GitHub REST API metadata, fetched 2026-08-09 (unauthenticated):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1253 → 1258 | 2026-08-07 |
| pubky/pkarr | 433 → 441 | 2026-08-07 |
| pubky/pubky-core | renamed → pubky/pubky-homeserver, 82 → 84 | 2026-08-07 |
| pubky/pkdns | 191 → 191 | 2026-03-23 |
| synonymdev/bitkit-core | 5 → 5 | 2026-08-07 |
| nostr-protocol/nips | 3010 → 3059 | 2026-08-08 |
| hashgraph/hedera-agent-kit-js | 66 → 66 | 2026-08-06 |
| hashgraph/did-method / did-sdk-java | 28 / 36 | 2025-01-14 / 2024-06-01 |
| urbit/urbit | 3616 → 3620 | 2026-08-07 |
| urbit/vere | 79 → 80 | 2026-08-09 |

## Interpretation

- **cheqd's meta-copy pullback is worth noting, not over-reading.** The explicit "AI Agents" homepage positioning lasted one observed cycle; the substance (Vouched integration, agentic blog content) remains. Watch whether the agent copy returns in the next product announcement — for now the cluster's agent positioning is content-led, not homepage-led.
- **MolTrust is converging on evidence-first receipt vocabulary** ("mandate-adherence verdicts, recomputable evidence"). That validates Archon's receipt framing while sharpening the centralized-vs-sovereign contrast: MolTrust's verdicts are recomputable from public chain data, but resolution and scoring still route through one operator's API.
- **Affinidi remains the most consistent company-level agent-trust narrator.** The Agent Gateway story has now led its blog for over two weeks with supporting AI-governance content stacking behind it.
- **`pubky-core` → `pubky-homeserver` is a naming clarification, not a strategy change.** The sovereign-web stack keeps shipping (pkarr and bitkit-core both pushed this week).
- **KILT and Ceramic staying dark for a second consecutive sweep** confirms both downgrades; they remain low-pressure historical references.
- **No new company-level entrants this cycle.** The discovery energy is all at the protocol/product layer (see the Archon 2026-08-09 refresh: decern), not the vendor layer.

## Source artifacts

- Main report: [Archetech Competitive Analysis](/research/archetech-competitive-analysis/)
- cheqd: <https://cheqd.io/> · Vouched posts: <https://cheqd.io/blog/how-cheqd-and-vouched-are-building-trust-in-ai-agents/> · <https://cheqd.io/blog/vouched-integrates-with-cheqd-to-bring-decentralised-identity-to-ai-agents/>
- Affinidi blog: <https://www.affinidi.com/blog>
- MolTrust: <https://moltrust.ch/> · pricing: <https://moltrust.ch/pricing.html>
- Microsoft Entra Agent ID: <https://learn.microsoft.com/en-us/entra/agent-id/>
- Pubky homeserver: <https://github.com/pubky/pubky-homeserver>
- Primer Systems: <https://primer.systems/>
