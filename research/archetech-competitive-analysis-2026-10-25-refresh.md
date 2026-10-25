---
layout: page
title: Archetech Competitive Analysis – 2026-10-25 Refresh
permalink: /research/archetech-competitive-analysis/2026-10-25-refresh/
---

# Archetech Competitive Analysis – 2026-10-25 Refresh

**Refresh timestamp:** 2026-10-25 09:10 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (status + title/meta), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera, bitkit-core), plus cheqd OG-block re-verification and MolTrust live-surface re-verification. No positioning changes detected on any incumbent vendor: every site returned its known title unchanged, cheqd's dual-OG-block state persists for an eighth consecutive verification, and the dark-ecosystem trends (KILT, Ceramic/3Box) extended to a thirteenth consecutive sweep — with ceramic.network degrading further from last week's 404 to a full connection failure. MolTrust made its first live-surface copy change in six weeks ("MolCheck record" branding in the meta description).

## What changed

- **cheqd's dual OG blocks persist unchanged (eighth consecutive verification).** Block 1 still pairs "The Payment & Trust Infrastructure for Credentials" og:title with the credential-ecosystems og:description; block 2 still pairs the monetise-credentials og:title with the agentic "Decentralised Infrastructure for Credentials & AI Agents" og:description.
- **KILT dark for a thirteenth consecutive sweep.** `kilt.io` returned 404 and `www.kilt.io` failed to connect (curl 000). Primer Systems (successor effort) still live: "Primer Systems - x402 and Privacy Architecture."
- **Ceramic / 3Box Labs dark for a thirteenth consecutive sweep, and degrading.** `ceramic.network` failed to connect entirely (curl 000 — last week it still returned a 404); `www.3boxlabs.com` failed to resolve (curl 000).
- **MolTrust re-verified — sixth consecutive quiet cycle on API/pricing/standards, but the first copy change in six weeks.** Homepage title unchanged; meta description now says agents' actions are sealed "into a MolCheck record anyone can re-run from the public record" (previously "into proof"). API still v2.5 healthy (timestamp 2026-10-25 13:05 UTC); `/pricing` still 301→`/pricing/`→403; `/pricing.html` still 200 with $19–$299/mo pricing re-confirmed, Lightning still roadmap; AAE draft unchanged at -02.
- **GitHub snapshots updated:** Self 1260→1264★ (+4, pushed 2026-10-23); pkarr 461→466★ (+5, pushed 2026-10-23); pkdns 196→197★ (+1); pubky-homeserver 88→89★ (+1, pushed 2026-10-24); bitkit-core flat at 5★ (pushed 2026-10-24); nostr-protocol/nips 3118→3123★ (+5, pushed 2026-10-22); urbit/urbit 3622→3621★ (-1, pushed 2026-10-23), urbit/vere flat at 80★ (pushed 2026-10-22); hedera-agent-kit-js flat at 69★ (pushed 2026-10-23); did-method flat at 27★; did-sdk-java flat at 36★.
- All other tracked vendor sites (MATTR, SpruceID, Dock, Privado ID, Indicio, Affinidi, Soulverse, Trinsic, Incode, Prove, Proof, Self, Okta/Auth0, NexionLabs, Hedera) returned HTTP 200 with unchanged titles/positioning. Updated the main page (Last-updated header, refresh link, competitive map rows for cheqd/KILT/Ceramic, MolTrust re-verification, GitHub snapshots, source links).

## Evidence observed

Vendor live-site sweep, all fetched 2026-10-25 (curl, browser UA):

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
| moltrust.ch | 200 | The Trust Layer for the Agent Economy — MolTrust (meta description now uses "MolCheck record" branding) |
| trinsic.id | 200 | Trinsic: Accept the World's Digital IDs Through One API |
| incode.com | 200 | AI Identity Verification Software & KYC Platform \| Incode |
| prove.com | 200 | Prove - Most accurate digital identity verification platform |
| proof.com | 200 | Proof \| Identity-centric security platform |
| self.xyz | 200 | Self • Build for humans and AI agents |
| nexionlabs.com | 200 | Age and identity verification. With evidence you can check. \| NexionLabs |
| kilt.io | 404 (www.kilt.io: connection failure, curl 000) | — (thirteenth consecutive dark sweep) |
| primer.systems | 200 | Primer Systems - x402 and Privacy Architecture |
| ceramic.network | connection failure, curl 000 (was 404 last week) | — (thirteenth consecutive dark sweep) |
| www.3boxlabs.com | DNS resolution failure, curl 000 | — (thirteenth consecutive dark sweep) |
| synonym.to | 200 | — (no title tag served this sweep) |
| pubky.org | 200 | Pubky Docs |
| blocktank.to | 200 | — (no title tag served this sweep) |
| bitkit.to | 200 | — (no title tag served this sweep) |
| nostr.com | 200 | nostr - controlled by users, not platforms |
| urbit.org | 200 | Urbit — Leave the internet behind |
| okta.com/ai | 200 | Okta Secures AI \| Identity for the Agentic Enterprise \| Okta |
| auth0.com/ai | 200 | Ship AI Agents Faster & More Securely \| Auth0 |
| hedera.com | 200 | A future built on enterprise trust \| Hedera |

GitHub REST API metadata, fetched 2026-10-25 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1260 → 1264 | 2026-10-23 |
| pubky/pkarr | 461 → 466 | 2026-10-23 |
| pubky/pkdns | 196 → 197 | 2026-10-08 |
| pubky/pubky-homeserver | 88 → 89 | 2026-10-24 |
| synonymdev/bitkit-core | 5 → 5 | 2026-10-24 |
| nostr-protocol/nips | 3118 → 3123 | 2026-10-22 |
| urbit/urbit | 3622 → 3621 | 2026-10-23 |
| urbit/vere | 80 → 80 | 2026-10-22 |
| hashgraph/hedera-agent-kit-js | 69 → 69 | 2026-10-23 |
| hashgraph/did-method | 27 → 27 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |

cheqd OG blocks (fetched 2026-10-25): block 1 og:title "The Payment & Trust Infrastructure for Credentials" + credential-ecosystems og:description; block 2 monetise-credentials og:title + agentic "Decentralised Infrastructure for Credentials & AI Agents …" og:description — unchanged.

MolTrust live surface (fetched 2026-10-25): `/health` → `{"status":"ok","version":"2.5","database":"connected","timestamp":"2026-10-25 13:05:08.492287"}`; `did:web:api.moltrust.ch` → 200; `/pricing` → 301 → `/pricing/` → 403; `/pricing.html` → 200 with $19/mo (2 agents), $299/mo (75 agents), $9/mo per additional agent, "PhoenixD integration prepped, not yet settling" re-verified.
