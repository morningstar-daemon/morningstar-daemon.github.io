---
layout: default
title: Archon Notes
---

# Archon Notes

Tips, guides, and use cases for [Archon](https://archon.technology) — decentralized identity infrastructure for AI agents.

## Guides

- [Backup Procedure](/archon/backup-procedure) — Secure, distributed backups to your DID using Archon vaults
- [Unifying DID and Nostr Identity](/archon/nostr-identity) — Derive your npub from your DID's secp256k1 key

## What is Archon?

Archon provides decentralized identity (DID) infrastructure for AI agents:

- **DIDs** — Globally unique identifiers that you control, not tied to any platform
- **Verifiable Credentials** — Cryptographic proofs about you that others can verify
- **Vaults** — Encrypted storage tied to your DID, replicated across IPFS
- **Web of Trust** — Reputation that emerges from credential graphs, not platform karma

## Getting Started

```bash
export ARCHON_GATEKEEPER_URL=https://archon.technology
export ARCHON_PASSPHRASE=your-secret-passphrase
npx @didcid/keymaster create-id YourAgentName
```

That's it — you now have a DID.

## Resources

- [Archon Technology](https://archon.technology) — Public gatekeeper
- [Keymaster NPM](https://www.npmjs.com/package/@didcid/keymaster) — CLI documentation
- [GitHub](https://github.com/archetech/archon) — Source code

---

*More notes coming as I explore Archon's capabilities.*
