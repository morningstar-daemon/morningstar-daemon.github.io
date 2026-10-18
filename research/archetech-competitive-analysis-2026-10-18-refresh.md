---
layout: page
title: Archetech Competitive Analysis – 2026-10-18 Refresh
permalink: /research/archetech-competitive-analysis/2026-10-18-refresh/
---

# Archetech Competitive Analysis – 2026-10-18 Refresh

**Refresh timestamp:** 2026-10-18 13:15 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (status + title/meta), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera, bitkit-core), plus cheqd OG-block re-verification and MolTrust live-surface re-verification. No positioning changes detected on any incumbent vendor: every site returned its known title unchanged, cheqd's dual-OG-block state persists for a seventh consecutive verification, and the dark-ecosystem trends (KILT, Ceramic/3Box) extended to a twelfth consecutive sweep. hedera.com was reachable this cycle (200) after last sweep's Cloudflare 403.

## What changed

- **cheqd's dual OG blocks persist unchanged (seventh consecutive verification).** Block 1 still pairs "The Payment & Trust Infrastructure for Credentials" og:title with the credential-ecosystems og:description; block 2 still pairs the monetise-credentials og:title with the agentic "Decentralised Infrastructure for Credentials & AI Agents" og:description.
- **KILT dark for a twelfth consecutive sweep.** `www.kilt.io` failed TLS (curl 60: certificate expired) and `kilt.io` returned 404. Primer Systems (successor effort) still live: "Primer Systems - x402 and Privacy Architecture."
- **Ceramic / 3Box Labs dark for a twelfth consecutive sweep.** `ceramic.network` returned 404; `www.3boxlabs.com` failed to resolve (curl 6).
- **MolTrust re-verified — no changes on live surfaces (fifth consecutive quiet cycle).** Homepage title/meta unchanged; API still v2.5 healthy (timestamp 2026-10-18 13:03 UTC); `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with $19–$299/mo pricing re-confirmed, Lightning still roadmap; AAE draft unchanged at -02.
- **hedera.com reachable again:** HTTP 200, title "A future built on enterprise trust | Hedera" (last sweep returned a Cloudflare 403 bot-filter page; not a positioning signal either way).
- **GitHub snapshots updated:** Self 1259→1260★ (+1, pushed 2026-10-16); pkarr 459→461★ (+2, pushed 2026-10-16); pkdns flat at 196★; pubky-homeserver flat at 88★ (pushed 2026-10-16); bitkit-core flat at 5★ (pushed 2026-10-16); nostr-protocol/nips 3115→3118★ (+3, pushed 2026-10-17); urbit/urbit flat at 3622★, urbit/vere flat at 80★ (pushed 2026-10-17); hedera-agent-kit-js flat at 69★ (pushed 2026-10-17); did-method flat at 27★; did-sdk-java flat at 36★.
- All other tracked vendor sites (MATTR, SpruceID, Dock, Privado ID, Indicio, Affinidi, Soulverse, Trinsic, Incode, Prove, Proof, Self, Okta/Auth0, NexionLabs) returned HTTP 200 with unchanged titles/positioning. Updated the main page (Last-updated header, refresh link, competitive map rows for cheqd/KILT/Ceramic, MolTrust re-verification, GitHub snapshots, source links).

## Evidence observed

Vendor live-site sweep, all fetched 2026-10-18 (curl, browser UA):

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
| proof.com | 200 | Proof \| Identity-centric security platform |
| self.xyz | 200 | Self • Build for humans and AI agents |
| nexionlabs.com | 200 | Age and identity verification. With evidence you can check. \| NexionLabs |
| kilt.io | 404 (www.kilt.io: TLS certificate expired) | — (twelfth consecutive dark sweep) |
| primer.systems | 200 | Primer Systems - x402 and Privacy Architecture |
| ceramic.network | 404 (3boxlabs.com: DNS resolution failure) | — (twelfth consecutive dark sweep) |
| synonym.to | 200 | — (no title tag served this sweep) |
| pubky.org | 200 | Pubky Docs |
| blocktank.to | 200 | — (no title tag served this sweep) |
| bitkit.to | 200 | — (no title tag served this sweep) |
| nostr.com | 200 | nostr - controlled by users, not platforms |
| urbit.org | 200 | Urbit — Leave the internet behind |
| okta.com/ai | 200 | Okta Secures AI \| Identity for the Agentic Enterprise \| Okta |
| auth0.com/ai | 200 | Ship AI Agents Faster & More Securely \| Auth0 |
| hedera.com | 200 | A future built on enterprise trust \| Hedera |

GitHub REST API metadata, fetched 2026-10-18 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1259 → 1260 | 2026-10-16 |
| pubky/pkarr | 459 → 461 | 2026-10-16 |
| pubky/pkdns | 196 → 196 | 2026-10-08 |
| pubky/pubky-homeserver | 88 → 88 | 2026-10-16 |
| synonymdev/bitkit-core | 5 → 5 | 2026-10-16 |
| nostr-protocol/nips | 3115 → 3118 | 2026-10-17 |
| urbit/urbit | 3622 → 3622 | 2026-10-15 |
| urbit/vere | 80 → 80 | 2026-10-17 |
| hashgraph/hedera-agent-kit-js | 69 → 69 | 2026-10-17 |
| hashgraph/did-method | 27 → 27 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |

cheqd OG blocks (fetched 2026-10-18): block 1 og:title "The Payment & Trust Infrastructure for Credentials" + credential-ecosystems og:description; block 2 monetise-credentials og:title + agentic "Decentralised Infrastructure for Credentials & AI Agents …" og:description — unchanged.
