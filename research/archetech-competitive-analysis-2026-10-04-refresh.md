---
layout: page
title: Archetech Competitive Analysis – 2026-10-04 Refresh
permalink: /research/archetech-competitive-analysis/2026-10-04-refresh/
---

# Archetech Competitive Analysis – 2026-10-04 Refresh

**Refresh timestamp:** 2026-10-04 09:06 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (status + title/description), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera Agent Kit, bitkit-core), plus cheqd OG-block re-verification and MolTrust pricing/AAE re-verification. No positioning changes detected this cycle: every vendor site returned its known title unchanged, cheqd's dual-OG-block state persists, and the dark-ecosystem trends (KILT, Ceramic/3Box) extended to a ninth consecutive sweep.

## What changed

- **cheqd's dual OG blocks persist unchanged.** Block 1 still pairs "The Payment & Trust Infrastructure for Credentials" og:title with the credential-ecosystems og:description; block 2 still pairs the monetise-credentials og:title with the agentic og:description. Page `<title>` unchanged.
- **KILT dark for a ninth consecutive sweep.** `www.kilt.io` failed to connect entirely (curl status 000) and `kilt.io` returned 404 on 2026-10-04. Primer Systems (successor effort) still live: "x402 and Privacy Architecture."
- **Ceramic / 3Box Labs dark for a ninth consecutive sweep.** `ceramic.network` returned 404 and `www.3boxlabs.com` failed to connect (curl status 000).
- **MolTrust re-verified — no changes.** Homepage title/meta unchanged ("The Trust Layer for the Agent Economy"); API still v2.5 healthy; `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with pricing re-confirmed; AAE Internet-Draft unchanged at -02.
- **Minor: synonym.to now serves a `<title>`** ("Home - Synonym.to") where previous sweeps observed no title tag. Content-level change only; positioning unchanged.
- **GitHub snapshots updated:** Self 1256→1257★ (pushed 2026-09-15); pkarr 457→458★ (pushed 2026-10-02); pkdns flat at 194★ (pushed 2026-10-01 — first push since 2026-03-23); pubky-homeserver 87★ (pushed 2026-10-03); bitkit-core 5★ (pushed 2026-10-02); nostr-protocol/nips 3106→3108★ (pushed 2026-09-27); urbit/urbit 3619→3620★ (pushed 2026-10-02), urbit/vere flat at 80★ (pushed 2026-10-02); hedera-agent-kit-js 68→69★ (pushed 2026-10-04), did-sdk-java flat at 37★, did-method flat at 28★.
- All other tracked vendor sites (MATTR, SpruceID, Dock, Privado ID, Indicio, Affinidi, Soulverse, Trinsic, Incode, Prove, Self, Didit, Okta/Auth0) returned HTTP 200 with unchanged titles/positioning. Updated the main page (Last-updated header, refresh link, competitive map rows for cheqd/KILT/Ceramic, GitHub snapshots, source links).

## Evidence observed

Vendor live-site sweep, all fetched 2026-10-04 (curl, browser UA):

| Site | HTTP status | Title observed |
|---|---|---|
| mattr.global | 200 | MATTR: Decentralised Identity & Verifiable Data Solutions |
| spruceid.com | 200 | Digital Trust Infrastructure for Government - SpruceID |
| cheqd.io | 200 | Monetise Customer Credentials & Govern Trusted Data Ecosystems - cheqd (two OG blocks — unchanged) |
| dock.io | 200 | Dock Labs - Create a Unified Identity Experience |
| privado.id | 200 | Home - Privado ID |
| indicio.tech | 200 | A Verifiable Credentials Platform For Proving Everything |
| affinidi.com | 200 | Affinidi: Building the Internet of Trust |
| soulverse.world | 200 | Soulverse - The Operating System of Trust |
| moltrust.ch | 200 | The Trust Layer for the Agent Economy — MolTrust |
| trinsic.id | 200 | Trinsic: Accept the World's Digital IDs Through One API |
| incode.com | 200 | AI Identity Verification Software & KYC Platform - Incode |
| prove.com | 200 | Prove - Most accurate digital identity verification platform |
| self.xyz | 200 | Self • Build for humans and AI agents |
| kilt.io | 404 (www.kilt.io: connection failure) | — (ninth consecutive dark sweep) |
| primer.systems | 200 | Primer Systems - x402 and Privacy Architecture |
| ceramic.network | 404 (3boxlabs.com: connection failure) | — (ninth consecutive dark sweep) |
| synonym.to | 200 | Home - Synonym.to (title tag now served; previously none) |
| pubky.org | 200 | Pubky Docs |
| nostr.com | 200 | nostr - controlled by users, not platforms |
| urbit.org | 200 | Urbit — Leave the internet behind |
| okta.com/ai | 200 | Okta Secures AI - Identity for the Agentic Enterprise - Okta |
| auth0.com/ai | 200 | Ship AI Agents Faster & More Securely - Auth0 |
| didit.me | 200 | Didit, One API for identity and fraud |

GitHub repo metadata, fetched 2026-10-04 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1256 → 1257 | 2026-09-15 |
| pubky/pkarr | 457 → 458 | 2026-10-02 |
| pubky/pkdns | 194 → 194 | 2026-10-01 |
| pubky/pubky-homeserver | 87 → 87 | 2026-10-03 |
| synonymdev/bitkit-core | 5 → 5 | 2026-10-02 |
| nostr-protocol/nips | 3106 → 3108 | 2026-09-27 |
| urbit/urbit | 3619 → 3620 | 2026-10-02 |
| urbit/vere | 80 → 80 | 2026-10-02 |
| hashgraph/hedera-agent-kit-js | 68 → 69 | 2026-10-04 |
| hashgraph/did-sdk-java | 37 → 37 | 2024-06-01 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |

cheqd OG blocks, fetched 2026-10-04: block 1 og:title "The Payment & Trust Infrastructure for Credentials" + credential-ecosystems og:description; block 2 monetise-credentials og:title + agentic "Credentials & AI Agents … trusted data payments" og:description — unchanged.

MolTrust live checks, 2026-10-04: API v2.5 healthy; `did:web` resolves; `/pricing` → 301 → `/pricing/` → 403; `/pricing.html` → 200 ($19–$299/mo re-verified, Lightning still roadmap); AAE draft -02 (Datatracker).

## Interpretation

- **Fully quiet vendor-positioning cycle.** Every tracked site returned its known title unchanged; the only content-level delta is synonym.to now serving a title tag.
- **The dark ecosystems are staying dark.** KILT and Ceramic/3Box reach nine consecutive dead sweeps; treat both as historical references at this point.
- **Pubky/Synonym repos remain the most consistently active tracked ecosystem** — pkarr, pkdns (first push since March), homeserver, and bitkit-core all pushed within the window.
- **Hedera Agent Kit continues its slow steady climb** (68→69★, pushed today) — persistent enterprise agent-tooling activity.
- **MolTrust remains frozen on every observable surface** — second consecutive cycle with no change to API, pricing, homepage, or IETF draft.
