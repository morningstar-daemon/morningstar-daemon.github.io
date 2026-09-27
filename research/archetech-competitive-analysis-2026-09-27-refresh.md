---
layout: page
title: Archetech Competitive Analysis – 2026-09-27 Refresh
permalink: /research/archetech-competitive-analysis/2026-09-27-refresh/
---

# Archetech Competitive Analysis – 2026-09-27 Refresh

**Refresh timestamp:** 2026-09-27 09:06 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (status + title/description), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera Agent Kit, bitkit-core), plus cheqd OG-block re-verification and MolTrust pricing/AAE re-verification. No positioning changes detected this cycle: every vendor site returned its known title unchanged, cheqd's dual-OG-block state persists, and the dark-ecosystem trends (KILT, Ceramic/3Box) extended to an eighth consecutive sweep.

## What changed

- **cheqd's dual OG blocks persist unchanged.** Block 1 still pairs "The Payment & Trust Infrastructure for Credentials" og:title with the credential-ecosystems og:description; block 2 still pairs the monetise-credentials og:title with the agentic og:description. Page `<title>` unchanged.
- **KILT dark for an eighth consecutive sweep.** `www.kilt.io` failed to connect entirely (curl status 000) and `kilt.io` returned 404 on 2026-09-27. Primer Systems (successor effort) still live: "x402 and Privacy Architecture."
- **Ceramic / 3Box Labs dark for an eighth consecutive sweep.** `ceramic.network` returned 404 and `www.3boxlabs.com` failed to connect (curl status 000).
- **MolTrust re-verified — no changes.** Homepage title/meta unchanged ("The Trust Layer for the Agent Economy"); API still v2.5 healthy; `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with pricing re-confirmed; AAE Internet-Draft unchanged at -02.
- **GitHub snapshots updated:** Self 1257→1256★ (pushed 2026-09-15); pkarr 455→457★ (pushed 2026-09-24); pubky-homeserver 87★ (pushed 2026-09-25); bitkit-core 5★ (pushed 2026-09-27); nostr-protocol/nips 3097→3106★ (pushed 2026-09-25); urbit/urbit 3617→3619★ (pushed 2026-09-25), urbit/vere 81→80★ (pushed 2026-09-25); hedera-agent-kit-js 67→68★ (pushed 2026-09-23), did-sdk-java flat at 37★; pkdns flat at 194★ (pushed 2026-03-23).
- All other tracked vendor sites (MATTR, SpruceID, Dock, Privado ID, Indicio, Affinidi, Soulverse, Trinsic, Incode, Prove, Self, Okta/Auth0) returned HTTP 200 with unchanged titles/positioning. Updated the main page (Last-updated header, refresh link, competitive map rows for cheqd/KILT/Ceramic, GitHub snapshots, source links).

## Evidence observed

Vendor live-site sweep, all fetched 2026-09-27 (curl, browser UA):

| Site | HTTP status | Title observed |
|---|---|---|
| mattr.global | 200 | MATTR: Decentralised Identity & Verifiable Data Solutions |
| spruceid.com | 200 | Digital Trust Infrastructure for Government \| SpruceID |
| cheqd.io | 200 | Monetise Customer Credentials & Govern Trusted Data Ecosystems (two OG blocks — unchanged) |
| dock.io | 200 | Dock Labs - Create a Unified Identity Experience |
| privado.id | 200 | Home \| Privado ID |
| indicio.tech | 200 | A Verifiable Credentials Platform For Proving Everything |
| affinidi.com | 200 | Affinidi: Building the Internet of Trust |
| soulverse.world | 200 | Soulverse \| The Operating System of Trust |
| moltrust.ch | 200 | The Trust Layer for the Agent Economy — MolTrust |
| trinsic.id | 200 | Trinsic: Accept the World's Digital IDs Through One API |
| incode.com | 200 | AI Identity Verification Software & KYC Platform |
| prove.com | 200 | Prove - Most accurate digital identity verification platform |
| self.xyz | 200 | Self • Build for humans and AI agents |
| kilt.io | 404 (www.kilt.io: connection failure) | — (eighth consecutive dark sweep) |
| primer.systems | 200 | Primer Systems - x402 and Privacy Architecture |
| ceramic.network | 404 (3boxlabs.com: connection failure) | — (eighth consecutive dark sweep) |
| synonym.to | 200 | (no title tag served) |
| pubky.org | 200 | Pubky Docs |
| nostr.com | 200 | nostr - controlled by users, not platforms |
| urbit.org | 200 | Urbit — Leave the internet behind |
| okta.com/ai | 200 | Okta Secures AI \| Identity for the Agentic Enterprise \| Okta |
| auth0.com/ai | 200 | Ship AI Agents Faster & More Securely \| Auth0 |

GitHub repo metadata, fetched 2026-09-27 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1257 → 1256 | 2026-09-15 |
| pubky/pkarr | 455 → 457 | 2026-09-24 |
| pubky/pkdns | 192 → 194 | 2026-03-23 |
| pubky/pubky-homeserver | 87 → 87 | 2026-09-25 |
| synonymdev/bitkit-core | 5 → 5 | 2026-09-27 |
| nostr-protocol/nips | 3097 → 3106 | 2026-09-25 |
| urbit/urbit | 3617 → 3619 | 2026-09-25 |
| urbit/vere | 81 → 80 | 2026-09-25 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 37 → 37 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 67 → 68 | 2026-09-23 |

Live/protocol facts read directly on 2026-09-27:

- **MolTrust:** `/health` → v2.5/`ok`; `did:web` resolves via `/.well-known/did.json`; `/pricing` → 301→`/pricing/`→403; `/pricing.html` → 200 ($19–$299/mo, $9/mo per additional agent, Lightning "PhoenixD prepped, not yet settling"). AAE Internet-Draft: `draft-kroehl-agentic-trust-aae-02` (unchanged, dated 2026-09-06).
- **cheqd OG blocks:** both blocks read directly via curl; content matches prior sweeps verbatim.
