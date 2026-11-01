---
layout: page
title: Archetech Competitive Analysis – 2026-11-01 Refresh
permalink: /research/archetech-competitive-analysis/2026-11-01-refresh/
---

# Archetech Competitive Analysis – 2026-11-01 Refresh

**Refresh timestamp:** 2026-11-01 09:05 EST<br>
**Scope:** Live status/title sweep of tracked vendors and GitHub metadata refresh for Self, Pubky, Nostr, Urbit, Hedera, and bitkit-core.

## Evidence observed

| Surface | Current evidence |
|---|---|
| Vendor sites | All tracked live vendors returned 200 with known titles; KILT returned 404, `www.kilt.io` 000; Ceramic and 3Box Labs 000; Primer Systems 200 |
| cheqd | Dual OG blocks re-verified: payment/trust credentials block plus agentic credentials/AI-agents block |
| GitHub: Self | 1260→1266★ (+6), pushed 2026-10-30 |
| GitHub: Pubky | pkarr 466→467★, pkdns flat 197★, pubky-homeserver flat 89★; pushes 2026-10-27/30 |
| GitHub: Nostr / Urbit | NIPs 3123→3132★ (+9); urbit/urbit 3621→3623★ (+2), vere flat 80★; pushes through 2026-11-01 |
| GitHub: Hedera / Bitcoin | Agent Kit flat 69★, did-method flat 27★, did-sdk-java flat 36★; bitkit-core flat 5★ |
| MolTrust | API v2.5 healthy; did:web 200; `/pricing` 301 then `/pricing.html` 200; current meta description retains “MolCheck record” branding |

## Interpretation

- The main page's market map remains stable: no new company-level entrant or material vendor repositioning was verified.
- Self, Nostr, and Urbit were the visible GitHub gainers in this sweep.
- KILT and Ceramic/3Box remain dark; Primer Systems remains live as an adjacent x402/privacy surface.
- cheqd's conflicting OG metadata persists, so its agentic positioning remains a live but internally inconsistent signal.
- MolTrust's public API and evidence-record positioning remain active; no new pricing or Lightning settlement change was verified.

## Sources

- Vendor HTTPS status/title checks, fetched 2026-11-01 with browser user agent.
- GitHub REST API metadata, fetched 2026-11-01 with authenticated `gh api`.
- MolTrust API/site and cheqd HTML metadata, fetched 2026-11-01.
