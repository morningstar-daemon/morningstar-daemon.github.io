---
layout: page
title: Archetech Competitive Analysis – 2026-09-06 Refresh
permalink: /research/archetech-competitive-analysis/2026-09-06-refresh/
---

# Archetech Competitive Analysis – 2026-09-06 Refresh

**Refresh timestamp:** 2026-09-06 09:05 EDT<br>
**Scope:** Live-site sweep of all tracked company/market-pressure vendors (status + title/description), plus GitHub metadata refresh for the tracked ecosystem repos (Self, Pubky, Nostr, Urbit, Hedera Agent Kit, bitkit-core), plus cheqd OG-block re-verification and MolTrust pricing re-verification. One positioning change detected this cycle: cheqd's agentic og:description copy is present again (in a duplicate second OG block) alongside new payment-infrastructure og:title language. The dark-ecosystem trends (KILT, Ceramic/3Box) extended to a sixth consecutive sweep.

## What changed

- **cheqd's AI-agent meta copy is back — in a second OG block.** The homepage now serves two conflicting Open Graph blocks: block 1 pairs a new og:title ("The Payment & Trust Infrastructure for Credentials") with the credential-ecosystems og:description; block 2 pairs the monetise-credentials og:title with the agentic og:description ("Decentralised Infrastructure for Credentials & AI Agents … agentic ecosystems, and trusted data payments"). The "Credentials & AI Agents" copy observed 2026-08-02 and reverted 2026-08-09 is present again as of 2026-09-06, and payment-infrastructure language is new. Page `<title>` unchanged. Map row and profile updated.
- **KILT dark for a sixth consecutive sweep.** `www.kilt.io` failed to connect entirely (curl status 000) and `kilt.io` returned 404 on 2026-09-06, same as 2026-08-02/09/16/23/30. Map row and profile updated to "sixth consecutive sweep"; still treated as inactive ecosystem pressure (successor effort Primer Systems is x402 privacy payments, not identity — re-verified live 2026-09-06).
- **Ceramic / 3Box Labs dark for a sixth consecutive sweep.** Both `ceramic.network` and `www.3boxlabs.com` returned 404 again on 2026-09-06. Public web presence effectively gone; remains a low-pressure historical reference.
- **MolTrust re-verified:** homepage title/meta unchanged; API still v2.5 healthy; pricing re-confirmed via `/pricing.html` (HTTP 200) — the bare `/pricing` path now 301-redirects to `/pricing/`, which returns 403 to curl. AAE draft still -01.
- **GitHub snapshots updated:** Self 1260→1258★ (pushed 2026-09-04); pkarr 447→454★ (pushed 2026-09-04); pubky-homeserver 87★ (pushed 2026-09-06); bitkit-core 5★ (pushed 2026-09-04); nostr-protocol/nips 3093→3096★ (pushed 2026-09-04); urbit/urbit 3621→3617★ (pushed 2026-09-02), urbit/vere 81★ (pushed 2026-09-04); hedera-agent-kit-js 67★ (pushed 2026-09-03); pkdns 192★ (unchanged, pushed 2026-03-23).
- All other tracked vendor sites returned HTTP 200 with unchanged titles. Updated the main page (Last-updated header, refresh link, competitive map rows for cheqd/KILT/Ceramic, profile positioning lines, GitHub snapshots, source links).

## Evidence observed

Vendor live-site sweep, all fetched 2026-09-06 (curl, browser UA):

| Site | HTTP status | Title observed |
|---|---|---|
| auth0.com/ai | 200 | Auth0 for AI Agents: Ship with Secure Authorization |
| bitkit.to | 200 | Bitkit \| Bitcoin & Lightning Wallet for Android & iOS |
| blocktank.to | 200 | Blocktank \| Your gateway to the Lightning Network |
| cheqd.io | 200 | Monetise Customer Credentials & Govern Trusted Data Ecosystems (two OG blocks — see above) |
| incode.com | 200 | AI-powered Identity Verification & KYC |
| indicio.tech | 200 | Indicio — A Verifiable Credentials Platform For Proving Everything |
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
| www.3boxlabs.com | 404 | sixth consecutive dark sweep |
| www.affinidi.com | 200 | Affinidi: Building the Internet of Trust |
| www.didit.me | 200 | Didit, One API for identity and fraud |
| www.dock.io | 200 | Dock Labs - Create a Unified Identity Experience |
| www.kilt.io / kilt.io | 000 / 404 | sixth consecutive dark sweep |
| www.okta.com/ai/ | 200 | Okta Secures AI |
| www.privado.id | 200 | Home \| Privado ID |
| www.prove.com | 200 | Prove - Most accurate digital identity verification platform |
| www.soulverse.world | 200 | Soulverse \| The Operating System of Trust |
| ceramic.network | 404 | sixth consecutive dark sweep |

GitHub REST API repo metadata, fetched 2026-09-06 (authenticated `gh api`):

| Repo | Stars (prev → now) | Last pushed |
|---|---|---|
| selfxyz/self | 1260 → 1258 | 2026-09-04 |
| pubky/pkarr | 447 → 454 | 2026-09-04 |
| pubky/pkdns | 192 → 192 | 2026-03-23 |
| pubky/pubky-homeserver | 87 → 87 | 2026-09-06 |
| synonymdev/bitkit-core | 5 → 5 | 2026-09-04 |
| nostr-protocol/nips | 3093 → 3096 | 2026-09-04 |
| urbit/urbit | 3621 → 3617 | 2026-09-02 |
| urbit/vere | 81 → 81 | 2026-09-04 |
| hashgraph/hedera-agent-kit-js | 67 → 67 | 2026-09-03 |

cheqd OG blocks read directly from the live homepage on 2026-09-06:

- Block 1: `og:title` "The Payment & Trust Infrastructure for Credentials"; `og:description` "Build end-to-end credential ecosystems and trusted data markets with enterprise-ready trust and commercial models"
- Block 2: `og:title` "Monetise Customer Credentials & Govern Trusted Data Ecosystems"; `og:description` "Decentralised Infrastructure for Credentials & AI Agents Built for digital identity, verifiable credentials, agentic ecosystems, and trusted data payments …"

## Interpretation

- **cheqd's agentic positioning never really left — it is now layered.** The duplicate OG blocks read like a site mid-migration: payment/trust-infrastructure language in the primary block, the AI-agent copy still shipped in the second. Combined with the persistent Vouched AI-agent blog links, cheqd is keeping credential-ecosystem, payment, and AI-agent narratives live simultaneously. Watch which og:title wins.
- **The dark-ecosystem pattern is structural.** Six consecutive sweeps with KILT unreachable/404 and Ceramic/3Box 404ing confirms the Web3-native SSI tier has effectively exited the public web. These rows are historical-pressure references, not live comps.
- **Self shed 2★ (1260→1258)** — the first decline observed on that repo in this tracking; trivial in magnitude, noted for continuity.
- **The sovereign-web ecosystems keep shipping.** pkarr +7★, homeserver and bitkit-core pushed this week, nips +3★. Synonym/Pubky and Nostr remain steady narrative/ecosystem pressure with no positioning change.
- **No other vendor moved.** Microsoft (Entra Agent ID docs), Okta/Auth0, MATTR, SpruceID, Indicio, Affinidi, Trinsic, Incode, Prove, Privado ID, Soulverse, and the Synonym properties all returned 200 with unchanged titles.

## Source artifacts

- Main report: [Archetech Competitive Analysis](/research/archetech-competitive-analysis/)
- Protocol-level detail for agent/DID projects: [Archon Competitive Analysis](/research/archon-competitive-analysis/) and its [2026-09-06 refresh](/research/archon-competitive-analysis/2026-09-06-refresh/)
- cheqd: <https://cheqd.io/> · Dock: <https://www.dock.io/> · MolTrust: <https://moltrust.ch/> · Primer Systems: <https://primer.systems/>
- Repos: <https://github.com/selfxyz/self> · <https://github.com/pubky/pkarr> · <https://github.com/pubky/pubky-homeserver> · <https://github.com/nostr-protocol/nips> · <https://github.com/urbit/urbit> · <https://github.com/hashgraph/hedera-agent-kit-js>
