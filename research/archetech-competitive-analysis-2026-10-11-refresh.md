---
layout: page
title: Archetech Competitive Analysis – 2026-10-11 Refresh
permalink: /research/archetech-competitive-analysis/2026-10-11-refresh/
---

# Archetech Competitive Analysis – 2026-10-11 Refresh

**Refresh timestamp:** 2026-10-11 09:05 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (status + title), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera, bitkit-core), plus cheqd OG-block re-verification and MolTrust pricing/AAE re-verification. No positioning changes detected this cycle: every vendor site returned its known title unchanged, cheqd's dual-OG-block state persists for a fifth consecutive verification, and the dark-ecosystem trends (KILT, Ceramic/3Box) extended to a tenth consecutive sweep.

## What changed

- **cheqd's dual OG blocks persist unchanged (fifth consecutive verification).** Block 1 still pairs "The Payment & Trust Infrastructure for Credentials" og:title with the credential-ecosystems og:description; block 2 still pairs the monetise-credentials og:title with the agentic og:description. Page `<title>` unchanged.
- **KILT dark for a tenth consecutive sweep.** `www.kilt.io` failed to connect entirely (curl status 000) and `kilt.io` returned 404 on 2026-10-11. Primer Systems (successor effort) still live: "Primer Systems - x402 and Privacy Architecture."
- **Ceramic / 3Box Labs dark for a tenth consecutive sweep.** `ceramic.network` returned 404 and `www.3boxlabs.com` failed to connect (curl status 000).
- **MolTrust re-verified — no changes on live surfaces (third consecutive quiet cycle).** Homepage title/meta unchanged; API still v2.5 healthy (timestamp 2026-10-11 13:03 UTC); `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with pricing re-confirmed, Lightning still roadmap; AAE draft unchanged at -02. Its public repo `MoltyCel/moltrust-api` pushed today (3→4★).
- **Minor: synonym.to served no `<title>` this sweep** (last sweep it served "Home - Synonym.to"; the sweep before that, none) — title serving flip-flops; positioning unchanged.
- **GitHub snapshots updated:** Self 1257→1255★ (-2, pushed 2026-09-15); pkarr 458→459★ (pushed 2026-10-06); pkdns flat at 194★ (pushed 2026-10-08); pubky-homeserver 87★ (pushed 2026-10-10); bitkit-core 5★ (pushed 2026-10-08); nostr-protocol/nips 3108→3111★ (pushed 2026-10-05); urbit/urbit 3620→3622★ (pushed 2026-10-09), urbit/vere flat at 80★ (pushed 2026-10-10); hedera-agent-kit-js flat at 69★ (pushed 2026-10-07), did-sdk-java flat at 37★, did-method flat at 28★.
- All other tracked vendor sites (MATTR, SpruceID, Dock, Privado ID, Indicio, Affinidi, Soulverse, Trinsic, Incode, Prove, Self, Didit, Okta/Auth0, NexionLabs) returned HTTP 200 with unchanged titles/positioning. Updated the main page (Last-updated header, refresh link, competitive map rows for cheqd/KILT/Ceramic, GitHub snapshots, source links).

## Evidence observed

Vendor live-site sweep, all fetched 2026-10-11 (curl, browser UA):

| Site | HTTP status | Title observed |
|---|---|---|
| mattr.global | 200 | MATTR: Decentralised Identity & Verifiable Data Solutions |
| spruceid.com | 200 | Digital Trust Infrastructure for Government \| SpruceID |
| cheqd.io | 200 | Monetise Customer Credentials & Govern Trusted Data Ecosystems \| cheqd (two OG blocks — unchanged) |
| dock.io | 200 | Dock Labs - Create a Unified Identity Experience |
| privado.id | 200 | Home \| Privado ID |
| indicio.tech | 200 | A Verifiable Credentials Platform For Proving Everything |
| affinidi.com | 200 | Affinidi: Building the Internet of Trust |
| soulverse.world | 200 | Soulverse \| The Operating System of Trust |
| moltrust.ch | 200 | The Trust Layer for the Agent Economy — MolTrust |
| trinsic.id | 200 | Trinsic: Accept the World's Digital IDs Through One API |
| incode.com | 200 | AI Identity Verification Software & KYC Platform \| Incode |
| prove.com | 200 | Prove - Most accurate digital identity verification platform |
| self.xyz | 200 | Self • Build for humans and AI agents |
| kilt.io | 404 (www.kilt.io: connection failure) | — (tenth consecutive dark sweep) |
| primer.systems | 200 | Primer Systems - x402 and Privacy Architecture |
| ceramic.network | 404 (3boxlabs.com: connection failure) | — (tenth consecutive dark sweep) |
| synonym.to | 200 | — (no title tag served this sweep) |
| pubky.org | 200 | Pubky Docs |
| nostr.com | 200 | nostr - controlled by users, not platforms |
| urbit.org | 200 | Urbit — Leave the internet behind |
| okta.com/ai | 200 | Okta Secures AI \| Identity for the Agentic Enterprise \| Okta |
| auth0.com/ai | 200 | Ship AI Agents Faster & More Securely \| Auth0 |
| didit.me | 200 | Didit, One API for identity and fraud |
| nexionlabs.com | 200 | Age and identity verification. With evidence you can check. \| NexionLabs |

GitHub REST API metadata, fetched 2026-10-11 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1257 → 1255 | 2026-09-15 |
| pubky/pkarr | 458 → 459 | 2026-10-06 |
| pubky/pkdns | 194 → 194 | 2026-10-08 |
| pubky/pubky-homeserver | 87 → 87 | 2026-10-10 |
| synonymdev/bitkit-core | 5 → 5 | 2026-10-08 |
| nostr-protocol/nips | 3108 → 3111 | 2026-10-05 |
| urbit/urbit | 3620 → 3622 | 2026-10-09 |
| urbit/vere | 80 → 80 | 2026-10-10 |
| hashgraph/hedera-agent-kit-js | 69 → 69 | 2026-10-07 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 37 → 37 | 2024-06-01 |

cheqd OG blocks (fetched 2026-10-11): block 1 og:title "The Payment & Trust Infrastructure for Credentials" + credential-ecosystems og:description; block 2 monetise-credentials og:title + agentic "Decentralised Infrastructure for Credentials & AI Agents … trusted data payments" og:description — unchanged.
