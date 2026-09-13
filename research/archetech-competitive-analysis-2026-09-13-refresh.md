---
layout: page
title: Archetech Competitive Analysis – 2026-09-13 Refresh
permalink: /research/archetech-competitive-analysis/2026-09-13-refresh/
---

# Archetech Competitive Analysis – 2026-09-13 Refresh

**Refresh timestamp:** 2026-09-13 09:06 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (status + title/description), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera Agent Kit, bitkit-core), plus cheqd OG-block re-verification and MolTrust pricing re-verification. No positioning changes detected this cycle: cheqd's dual-OG-block state persists unchanged, and the dark-ecosystem trends (KILT, Ceramic/3Box) extended to a seventh consecutive sweep.

## What changed

- **cheqd's dual OG blocks persist unchanged.** Re-verified 2026-09-13: block 1 still pairs "The Payment & Trust Infrastructure for Credentials" og:title with the credential-ecosystems og:description; block 2 still pairs the monetise-credentials og:title with the agentic og:description ("Decentralised Infrastructure for Credentials & AI Agents … trusted data payments"). Page `<title>` unchanged. Map row and profile updated; no new movement.
- **KILT dark for a seventh consecutive sweep.** `www.kilt.io` failed to connect entirely (curl status 000) and `kilt.io` returned 404 on 2026-09-13, same as every sweep since 2026-08-02. Successor effort Primer Systems re-verified live (still "x402 and Privacy Architecture" — payments, not identity).
- **Ceramic / 3Box Labs dark for a seventh consecutive sweep.** `ceramic.network` returned 404 and `www.3boxlabs.com` failed to connect entirely (curl status 000) on 2026-09-13. Public web presence effectively gone; remains a low-pressure historical reference.
- **MolTrust re-verified:** homepage title/meta unchanged; API still v2.5 healthy; pricing re-confirmed via `/pricing.html` (HTTP 200) with `/pricing` still 301→`/pricing/`→403. **AAE draft advanced to -02** (Datatracker dated 2026-09-06).
- **GitHub snapshots updated:** Self 1258→1257★ (second consecutive small decline; pushed 2026-09-06); pkarr 454→455★ (pushed 2026-09-08); pubky-homeserver 87★ (pushed 2026-09-11); bitkit-core 5★ (pushed 2026-09-11); nostr-protocol/nips 3096→3097★ (pushed 2026-09-09); urbit/urbit 3617★ (pushed 2026-09-07), urbit/vere 81★ (pushed 2026-09-12); hedera-agent-kit-js 67★ (pushed 2026-09-11), did-sdk-java 36→37★; pkdns 192★ (unchanged, pushed 2026-03-23).
- All other tracked vendor sites returned HTTP 200 with unchanged titles. Updated the main page (Last-updated header, refresh link, competitive map rows for cheqd/KILT/Ceramic, profile positioning lines, GitHub snapshots, source links).

## Evidence observed

Vendor live-site sweep, all fetched 2026-09-13 (curl, browser UA):

| Site | HTTP status | Title observed |
|---|---|---|
| auth0.com/ai | 200 | Auth0 for AI Agents: Ship with Secure Authorization |
| bitkit.to | 200 | Bitkit \| Bitcoin & Lightning Wallet for Android & iOS |
| blocktank.to | 200 | Blocktank \| Your gateway to the Lightning Network |
| cheqd.io | 200 | Monetise Customer Credentials & Govern Trusted Data Ecosystems (two OG blocks — unchanged) |
| incode.com | 200 | AI Identity Verification Software & KYC Platform |
| indicio.tech | 200 | A Verifiable Credentials Platform For Proving Everything |
| learn.microsoft.com/en-us/entra/agent-id/ | 200 | Microsoft Entra Agent ID documentation |
| mattr.global | 200 | MATTR: Decentralised Identity & Verifiable Data Solutions |
| moltrust.ch | 200 | The Trust Layer for the Agent Economy — MolTrust |
| nostr.com | 200 | nostr - controlled by users, not platforms |
| primer.systems | 200 | Primer Systems - x402 and Privacy Architecture |
| pubky.org | 200 | Pubky Docs |
| self.xyz | 200 | Self • Build for humans and AI agents |
| spruceid.com | 200 | Digital Trust Infrastructure for Government |
| synonym.to | 200 | Home \| Synonym.to |
| trinsic.id | 200 | Trinsic: Accept the World's Digital IDs Through One API |
| urbit.org | 200 | Urbit — Leave the internet behind |
| www.3boxlabs.com | 000 | seventh consecutive dark sweep (connection failure) |
| www.affinidi.com | 200 | Affinidi: Building the Internet of Trust |
| www.didit.me | 200 | Didit, One API for identity and fraud |
| www.dock.io | 200 | Dock Labs - Create a Unified Identity Experience |
| www.kilt.io / kilt.io | 000 / 404 | seventh consecutive dark sweep |
| www.okta.com/ai/ | 200 | Okta Secures AI |
| www.privado.id | 200 | Home \| Privado ID |
| www.prove.com | 200 | Prove - Most accurate digital identity verification platform |
| www.soulverse.world | 200 | Soulverse \| The Operating System of Trust |
| ceramic.network | 404 | seventh consecutive dark sweep |

GitHub REST API repo metadata, fetched 2026-09-13 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1258 → 1257 | 2026-09-06 |
| pubky/pkarr | 454 → 455 | 2026-09-08 |
| pubky/pkdns | 192 → 192 | 2026-03-23 |
| pubky/pubky-homeserver | 87 → 87 | 2026-09-11 |
| synonymdev/bitkit-core | 5 → 5 | 2026-09-11 |
| nostr-protocol/nips | 3096 → 3097 | 2026-09-09 |
| urbit/urbit | 3617 → 3617 | 2026-09-07 |
| urbit/vere | 81 → 81 | 2026-09-12 |
| hashgraph/did-sdk-java | 36 → 37 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 67 → 67 | 2026-09-11 |

cheqd OG blocks read directly from the live homepage on 2026-09-13 (unchanged from 2026-09-06):

- Block 1: `og:title` "The Payment & Trust Infrastructure for Credentials"; `og:description` "Build end-to-end credential ecosystems and trusted data markets with enterprise-ready trust and commercial models"
- Block 2: `og:title` "Monetise Customer Credentials & Govern Trusted Data Ecosystems"; `og:description` "Decentralised Infrastructure for Credentials & AI Agents Built for digital identity, verifiable credentials, agentic ecosystems, and trusted data payments …"

## Interpretation

- **No vendor moved this cycle.** Every tracked site returned the same status and title as 2026-09-06; cheqd's layered OG state is now stable for two consecutive sweeps, which reads less like mid-migration churn and more like a deliberate (or forgotten) dual-track narrative — payment/trust infrastructure primary, AI-agent copy still shipped.
- **The dark-ecosystem pattern is structural.** Seven consecutive sweeps with KILT unreachable/404 and Ceramic/3Box dark confirms the Web3-native SSI tier has effectively exited the public web. These rows are historical-pressure references, not live comps.
- **Self shed 1★ again (1258→1257)** — a second consecutive trivial decline; noted for continuity, not signal.
- **The sovereign-web ecosystems keep shipping.** pkarr +1★, homeserver and bitkit-core pushed this week, nips +1★. Synonym/Pubky and Nostr remain steady narrative/ecosystem pressure with no positioning change.
- **MolTrust's AAE -02 is the only spec-track movement in either landscape this week** — a company-level credibility asset (IETF authorship) that Archetech's public materials currently don't match.

## Source artifacts

- Main report: [Archetech Competitive Analysis](/research/archetech-competitive-analysis/)
- Protocol-level detail for agent/DID projects: [Archon Competitive Analysis](/research/archon-competitive-analysis/) and its [2026-09-13 refresh](/research/archon-competitive-analysis/2026-09-13-refresh/)
- cheqd: <https://cheqd.io/> · Dock: <https://www.dock.io/> · MolTrust: <https://moltrust.ch/> · Primer Systems: <https://primer.systems/>
- Repos: <https://github.com/selfxyz/self> · <https://github.com/pubky/pkarr> · <https://github.com/pubky/pubky-homeserver> · <https://github.com/nostr-protocol/nips> · <https://github.com/urbit/urbit> · <https://github.com/hashgraph/hedera-agent-kit-js>
