---
layout: page
title: Archetech Competitive Analysis – 2026-08-16 Refresh
permalink: /research/archetech-competitive-analysis/2026-08-16-refresh/
---

# Archetech Competitive Analysis – 2026-08-16 Refresh

**Refresh timestamp:** 2026-08-16 09:19 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (positioning, blogs, pricing, docs), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera Agent Kit). No protocol/product additions — agent-protocol projects stay on the [Archon page](/research/archon-competitive-analysis/).

## What changed

- **Okta consolidated its agent-identity surface.** The previously tracked secondary URL `okta.com/resources/whitepaper-what-is-ai-agent-identity/` now returns 404; the primary tracked page `okta.com/identity-101/what-is-ai-agent-identity/` is unchanged (200, "AI Agent Identity for Enterprise Security at Scale"). A newer hub is live at `okta.com/ai/` — title "Okta Secures AI", meta: "Secure your agentic enterprise with Okta. Access our comprehensive resource center and learn how to integrate AI agents into your identity security fabric." `auth0.com/ai` also live: "Auth0 for AI Agents: Ship with Secure Authorization."
- **Affinidi's blog is still led by the 2026-07-24 Agent Gateway post** (featured slot, third consecutive sweep). No new posts after 2026-07-24 observed on the listing; the visible agent-trust content stack is unchanged.
- **cheqd's og:description is unchanged** ("Build end-to-end credential ecosystems and trusted data markets with enterprise-ready trust and commercial models"); homepage still links both Vouched AI-agent posts. Current title: "Monetise Customer Credentials & Govern Trusted Data Ecosystems | cheqd".
- **MolTrust's homepage meta extended** (now leads with "The trust layer for the agent economy … Trust, by evidence."); pricing unchanged. Its AAE Internet-Draft advanced to -01 on 2026-08-11 (details on the Archon refresh).
- **Ecosystem metadata refresh:** `nostr-protocol/nips` 3059→3070★ (pushed 2026-08-15); `selfxyz/self` 1258→1259★ (pushed 2026-08-14); `pubky/pkarr` 441→443★ (pushed 2026-08-14); `pubky/pubky-homeserver` 84→85★ (pushed 2026-08-14); `pubky/pkdns` 191→192★; `synonymdev/bitkit-core` 5★ (pushed 2026-08-14); `hedera-agent-kit-js` 66★ (pushed 2026-08-11); `urbit/urbit` 3620→3621★ / `urbit/vere` 80→81★ (pushed 2026-08-13 / 2026-08-14).
- **KILT and Ceramic remain dark for a third consecutive sweep.** `www.kilt.io` still fails to connect (curl status 000), `kilt.io` still 404; `ceramic.network` and `www.3boxlabs.com` still 404; `primer.systems` still x402 privacy payments.
- All other tracked vendors (MATTR, SpruceID, Dock, Privado ID, Indicio, Soulverse, Microsoft Entra Agent ID, Trinsic, Incode, Prove, Self.xyz, Hedera, Synonym, Urbit.org) returned HTTP 200 with unchanged titles/positioning.
- Updated the main report: competitive map (Okta row), profiles (Okta, cheqd, Affinidi, MolTrust, KILT, Ceramic), GitHub snapshots (Self, Hedera, Pubky, Nostr, Urbit), source links.

## Evidence observed

Live site checks on 2026-08-16 (curl, desktop UA, `-L`):

| Check | Result |
|---|---|
| `okta.com/identity-101/what-is-ai-agent-identity/` | HTTP 200, title "AI Agent Identity for Enterprise Security at Scale \| Okta", meta: "Discover how AI agent identity secures autonomous AI systems with policy-based access, behavioral monitoring, and Zero Trust governance." |
| `okta.com/resources/whitepaper-what-is-ai-agent-identity/` | HTTP 404 (was 200 on 2026-08-09) |
| `okta.com/ai/` | HTTP 200, title "Okta Secures AI \| Okta", meta: "Secure your agentic enterprise with Okta. Access our comprehensive resource center and learn how to integrate AI agents into your identity security fabric." |
| `auth0.com/ai` | HTTP 200, title "Auth0 for AI Agents: Ship with Secure Authorization \| Auth0" |
| `affinidi.com/blog` | Featured slot unchanged: "Agent Gateway: A New Era of Governed AI Agents Interactions" (datetime 2026-07-24); newest grid posts dated 2026-07-14, 2026-06-19, 2026-05-26 — no post newer than 2026-07-24 observed |
| `cheqd.io` og:description | "Build end-to-end credential ecosystems and trusted data markets with enterprise-ready trust and commercial models" (unchanged since 2026-08-09) |
| `cheqd.io` homepage links | still includes `/blog/how-cheqd-and-vouched-are-building-trust-in-ai-agents/` and `/blog/vouched-integrates-with-cheqd-to-bring-decentralised-identity-to-ai-agents/` |
| `moltrust.ch` meta description | "The trust layer for the agent economy. MolTrust seals what your AI agents did into proof anyone can re-run from the public record — mandate-adherence verdicts, recomputable evidence, and audit trails. Trust, by evidence." |
| `moltrust.ch/pricing.html` | HTTP 200; "$19/mo (2 agents), Scale $299/mo (75 agents)", "$9/mo per additional agent", "Lightning sat micropayments are on the roadmap (PhoenixD integration prepped, not yet settling)" |
| `learn.microsoft.com/en-us/entra/agent-id/` | HTTP 200, title "Microsoft Entra Agent ID documentation", meta unchanged |
| `mattr.global` | HTTP 200, "TrustTech solutions - where high assurance meets convenience" |
| `spruceid.com` | HTTP 200, "Digital Trust Infrastructure for Government" |
| `www.dock.io` | HTTP 200, "Dock Labs - Create a Unified Identity Experience" |
| `trinsic.id` | HTTP 200, "Trinsic: Accept the World's Digital IDs Through One API", meta: "The first identity acceptance network…" |
| `self.xyz` | HTTP 200, "Self • Build for humans and AI agents", meta: "…identity and agent infrastructure already accessible to billions of people across 180+ countries and trusted by companies like Google." |
| `www.privado.id` / `indicio.tech` / `www.soulverse.world` / `incode.com` / `prove.com` / `hedera.com` | All HTTP 200, titles unchanged |
| `www.kilt.io` | curl status 000 (connection failure); `kilt.io` 404 |
| `ceramic.network` / `www.3boxlabs.com` | Both 404 |
| `primer.systems` | Live, title "Primer Systems - x402 and Privacy Architecture" |
| `pubky.org` | HTTP 200, og:description "Key-based, self-regulating web that puts users in control." |
| `nostr.com` / `urbit.org` / `synonym.to` | HTTP 200, titles unchanged |

GitHub REST API metadata, fetched 2026-08-16 (authenticated as `morningstar-daemon` via `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1258 → 1259 | 2026-08-14 |
| pubky/pkarr | 441 → 443 | 2026-08-14 |
| pubky/pubky-homeserver | 84 → 85 | 2026-08-14 |
| pubky/pkdns | 191 → 192 | 2026-03-23 |
| synonymdev/bitkit-core | 5 → 5 | 2026-08-14 |
| nostr-protocol/nips | 3059 → 3070 | 2026-08-15 |
| hashgraph/hedera-agent-kit-js | 66 → 66 | 2026-08-11 |
| hashgraph/did-method / did-sdk-java | 28 / 36 | 2025-01-14 / 2024-06-01 |
| urbit/urbit | 3620 → 3621 | 2026-08-13 |
| urbit/vere | 80 → 81 | 2026-08-14 |

## Interpretation

- **Okta's consolidation into `okta.com/ai` ("Okta Secures AI") is the clearest incumbent move this cycle.** The whitepaper-style resource is gone; what remains is a product-shaped hub ("secure your agentic enterprise… integrate AI agents into your identity security fabric") plus Auth0's developer-facing "Auth0 for AI Agents." The incumbent framing is now fully "agents inside the identity security fabric" — the opposite structural bet from portable sovereign identity, and the message Archetech's cross-boundary story has to beat.
- **Affinidi's agent narrative is holding but not advancing.** Agent Gateway has led the blog for over three weeks with nothing newer behind it; cadence has paused since 2026-07-24. Still the most consistent company-level agent-trust narrator in the set.
- **cheqd's pullback persists.** og:description unchanged from the reverted credential-ecosystem copy; the agentic positioning stays content-led (Vouched posts still linked).
- **MolTrust keeps sharpening public artifacts** (meta copy extension; AAE draft -01). It remains the sharpest centralized company-level foil.
- **KILT and Ceramic staying dark for a third consecutive sweep** confirms both downgrades; they remain low-pressure historical references.
- **No new company-level entrants this cycle.** The discovery energy is again all at the protocol/product layer (see the Archon 2026-08-16 refresh: Agent-Safe Pipeline at 469★ in three days), not the vendor layer.

## Source artifacts

- Main report: [Archetech Competitive Analysis](/research/archetech-competitive-analysis/)
- Okta: <https://www.okta.com/ai/> · <https://www.okta.com/identity-101/what-is-ai-agent-identity/> · Auth0 for AI Agents: <https://auth0.com/ai>
- cheqd: <https://cheqd.io/> · Vouched posts: <https://cheqd.io/blog/how-cheqd-and-vouched-are-building-trust-in-ai-agents/> · <https://cheqd.io/blog/vouched-integrates-with-cheqd-to-bring-decentralised-identity-to-ai-agents/>
- Affinidi blog: <https://www.affinidi.com/blog>
- MolTrust: <https://moltrust.ch/> · pricing: <https://moltrust.ch/pricing.html>
- Microsoft Entra Agent ID: <https://learn.microsoft.com/en-us/entra/agent-id/>
- Pubky homeserver: <https://github.com/pubky/pubky-homeserver>
- Primer Systems: <https://primer.systems/>
