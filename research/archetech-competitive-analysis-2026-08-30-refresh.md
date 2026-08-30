---
layout: page
title: Archetech Competitive Analysis – 2026-08-30 Refresh
permalink: /research/archetech-competitive-analysis/2026-08-30-refresh/
---

# Archetech Competitive Analysis – 2026-08-30 Refresh

**Refresh timestamp:** 2026-08-30 09:05 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (status + title/description), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera Agent Kit), plus cheqd og:description and Affinidi meta re-verification. No positioning changes detected this cycle; the dark-ecosystem trends (KILT, Ceramic/3Box) extended to a fifth consecutive sweep.

## What changed

- **All live vendor sites returned HTTP 200 with unchanged positioning.** MATTR ("TrustTech solutions"), SpruceID ("Digital Trust Infrastructure for Government"), cheqd ("Monetise Customer Credentials & Govern Trusted Data Ecosystems" — og:description re-verified as credential-ecosystem copy, not the agentic variant), Dock, Privado ID, Indicio, Affinidi ("Building the Internet of Trust"; meta still mentions AI agents), Okta (`okta.com/ai` "Okta Secures AI"; `auth0.com/ai` "Auth0 for AI Agents"), Trinsic, Incode, Prove, Self ("Build for humans and AI agents"), Synonym, Pubky, Blocktank, Bitkit, Nostr, and Urbit all match their recorded positioning lines. No title/meta changes worth reclassifying.
- **KILT dark for a fifth consecutive sweep.** `www.kilt.io` failed to connect entirely (curl status 000) and `kilt.io` returned 404 on 2026-08-30, same as 2026-08-02/09/16/23. Map row and profile updated to "fifth consecutive sweep"; still treated as inactive ecosystem pressure (successor effort Primer Systems is x402 privacy payments, not identity — re-verified live 2026-08-30).
- **Ceramic / 3Box Labs dark for a fifth consecutive sweep.** Both `ceramic.network` and `www.3boxlabs.com` returned 404 again on 2026-08-30. Public web presence effectively gone; remains a low-pressure historical reference.
- **GitHub snapshots refreshed:** `selfxyz/self` 1257→1260★ (pushed 2026-08-28 — still actively developed), `pubky/pkarr` 444→447★ (pushed 2026-08-25), `pubky/pubky-homeserver` 87★ (pushed 2026-08-28), `nostr-protocol/nips` 3082→3093★ (pushed 2026-08-27), `hedera-agent-kit-js` 66→67★ (pushed 2026-08-26), `urbit/urbit` 3621★ (pushed 2026-08-28), `urbit/vere` 81★ (pushed 2026-08-28), `pubky/pkdns` 192★ (2026-03-23), `bitkit-core` 5★ (pushed 2026-08-28), `did-method` 28★ / `did-sdk-java` 36★ (unchanged, quiet).
- Updated the main page (Last-updated header, refresh link, competitive map rows for KILT/Ceramic/cheqd copy-check date, and the Self/Hedera/Pubky/Nostr/Urbit GitHub snapshots; added refresh-log source links).

## Evidence observed

Live-site checks (curl, 2026-08-30, status / title excerpt):

| Site | Status | Title / positioning observed |
|---|---|---|
| mattr.global | 200 | "MATTR \| TrustTech solutions - where high assurance meets convenience" |
| spruceid.com | 200 | "Digital Trust Infrastructure for Government \| SpruceID" |
| cheqd.io | 200 | "Monetise Customer Credentials & Govern Trusted Data Ecosystems" (og:description re-verified: "Build end-to-end credential ecosystems and trusted data markets…") |
| dock.io | 200 | "Dock Labs - Create a Unified Identity Experience" |
| privado.id | 200 | "Home \| Privado ID" |
| indicio.tech | 200 | "Indicio — A Verifiable Credentials Platform For Proving Everything" |
| affinidi.com | 200 | "Affinidi: Building the Internet of Trust" (meta re-verified: "…individuals, businesses, systems, and AI agents") |
| okta.com/ai | 200 | "Okta Secures AI" |
| auth0.com/ai | 200 | "Auth0 for AI Agents: Ship with Secure Authorization" |
| trinsic.id | 200 | "Accept the World's Digital IDs Through One API" |
| incode.com | 200 | "AI-powered Identity Verification & KYC" |
| prove.com | 200 | "Most accurate digital identity verification platform" |
| self.xyz | 200 | "Self • Build for humans and AI agents" |
| www.kilt.io / kilt.io | 000 / 404 | fifth consecutive dark sweep |
| www.3boxlabs.com | 404 | fifth consecutive dark sweep |
| ceramic.network | 404 | fifth consecutive dark sweep |
| synonym.to | 200 | "Home \| Synonym.to" |
| pubky.org | 200 | "Pubky Docs" |
| blocktank.to | 200 | "Your gateway to the Lightning Network" |
| bitkit.to | 200 | "Bitcoin & Lightning Wallet for Android & iOS" |
| nostr.com | 200 | "controlled by users, not platforms" |
| urbit.org | 200 | "Urbit — Leave the internet behind" |
| primer.systems | 200 | "Primer Systems - x402 and Privacy Architecture" |

GitHub REST API metadata (authenticated `gh api`, 2026-08-30):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1257 → 1260 | 2026-08-28 |
| hashgraph/did-method | 28 → 28 | 2025-01-14 |
| hashgraph/did-sdk-java | 36 → 36 | 2024-06-01 |
| hashgraph/hedera-agent-kit-js | 66 → 67 | 2026-08-26 |
| pubky/pkarr | 444 → 447 | 2026-08-25 |
| pubky/pkdns | 192 → 192 | 2026-03-23 |
| pubky/pubky-homeserver | 87 → 87 | 2026-08-28 |
| synonymdev/bitkit-core | 5 → 5 | 2026-08-28 |
| nostr-protocol/nips | 3082 → 3093 | 2026-08-27 |
| urbit/urbit | 3621 → 3621 | 2026-08-28 |
| urbit/vere | 81 → 81 | 2026-08-28 |

## Interpretation

- **No company-level repositioning this cycle.** Every live vendor matches its recorded positioning; the competitive map needs no category changes. cheqd's meta pullback to credential-ecosystem copy persists (re-verified at og:description level), and Affinidi's "…and AI agents" meta persists — the agentic narratives remain at different altitudes (Affinidi in meta + blog, cheqd in blog only).
- **The dark-ecosystem pattern is now structural.** Five consecutive sweeps with KILT unreachable/404 and Ceramic/3Box 404ing confirms the Web3-native SSI tier has effectively exited the public web. Archetech's agent/sovereign-infrastructure framing remains well-positioned against that trend; these rows are now historical-pressure references, not live comps.
- **Ecosystem dev activity is steady where it matters for Archetech's narrative:** Nostr NIPs +11★ (3093★), Pubky pkarr +3★ with homeserver and bitkit-core both pushing this week — the Bitcoin-native / public-key identity ecosystems stay visibly alive. Hedera Agent Kit pushed again (2026-08-26, 67★) while its DID repos stay frozen — enterprise DLT effort keeps flowing to agent tooling, not DID methods.
- **Self (`selfxyz/self`) keeps shipping** (1257→1260★, pushed 2026-08-28) — ZK human-proof remains an active, well-resourced adjacent gate near agent workflows; the "humans and AI agents" framing persists in its live title.

## Source artifacts

- Main page: [Archetech Competitive Analysis](/research/archetech-competitive-analysis/)
- Companion protocol view: [Archon Competitive Analysis](/research/archon-competitive-analysis/) and its [2026-08-30 refresh](/research/archon-competitive-analysis/2026-08-30-refresh/)
- selfxyz/self: <https://github.com/selfxyz/self> · Hedera Agent Kit: <https://github.com/hashgraph/hedera-agent-kit-js> · Pubky: <https://github.com/pubky/pubky-homeserver> · Nostr NIPs: <https://github.com/nostr-protocol/nips> · Urbit: <https://github.com/urbit/urbit>
