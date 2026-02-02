---
layout: default
nav_exclude: true
title: Archon Backup Procedure
---

# Archon Backup Procedure for AI Agents

Self-backup your workspace, config, and wallet to your DID using Archon vaults.

## Why Archon Backups?

**Secure** backups with two key properties:

- **Distributed** — Your data is stored in IPFS and replicated across the hyperswarm network. No single point of failure. If one node goes down, your backups persist on others. This mitigates loss from hardware failure, provider outages, or infrastructure changes.

- **Encrypted** — Vault contents are encrypted to your DID. Only you (or members you explicitly add) can decrypt. Your secrets, memory, and identity stay private even though the data is distributed.

**Recoverable from mnemonic alone** — Your 12-word recovery phrase is the master key. Lose everything else and you can still recover your wallet, resolve your vault, and restore your full state.

## Prerequisites

- Archon identity (DID) created via Keymaster
- Environment variables set:
  ```bash
  export ARCHON_GATEKEEPER_URL=https://archon.technology  # or http://localhost:4224 for local
  export ARCHON_PASSPHRASE=your-passphrase
  ```

### Gatekeeper Options

| Gatekeeper | URL | File Size Limit | Use Case |
|------------|-----|-----------------|----------|
| **Public** | `https://archon.technology` | 10MB | Most agents, standard backups |
| **Local** | `http://localhost:4224` | Unlimited | Large files >10MB |

**Note:** The public gatekeeper at archon.technology supports files up to 10MB. If your backups exceed this (large memory databases, extensive research archives), you can run a local Archon node. Documentation for running your own node is coming soon.

## Step 1: Create a Backup Vault

```bash
npx @didcid/keymaster create-vault --name backup
```

This creates a new vault DID and registers it with your wallet under the name "backup".

## Step 2: Configure .backup-ignore Files

Create `.backup-ignore` in each directory to specify what to exclude. Uses the same pattern format as zip's `-x` flag.

**Workspace `.backup-ignore` example:**
```
# Large directories and dependencies
.git/*
**/node_modules/*
**/__pycache__/*
**/.venv/*

# Test environments and submodules
archon-test/*
cli-test/*
hexmem/*

# Temporary and generated files
*.log
*.tmp
*.swp
*.db
.env
```

**Config `.backup-ignore` example (in `~/.openclaw/`):**
```
# Session data (large, regenerable)
agents/*/sessions/*
agents/*/cache/*
logs/*
*.log

# Browser data (contains sockets, regenerable)
browser/*
media/*
canvas/*
```

## Step 3: Archive Your Workspace

```bash
zip -r workspace.zip ~/your-workspace -x@~/your-workspace/.backup-ignore
```

This backs up everything except patterns in `.backup-ignore`. The zip is created in the current directory, outside the workspace.

## Step 4: Archive Your Config

```bash
zip -r config.zip ~/.openclaw -x@~/.openclaw/.backup-ignore
```

## Step 5: Upload to Vault

```bash
npx @didcid/keymaster add-vault-item backup workspace.zip
npx @didcid/keymaster add-vault-item backup config.zip
npx @didcid/keymaster add-vault-item backup ~/your-workspace/hexmem/hexmem.db
```

Items with the same name are automatically replaced. Verify:
```bash
npx @didcid/keymaster list-vault-items backup
```

## Step 6: Backup Wallet to Seed Bank

```bash
npx @didcid/keymaster backup-wallet-did
```

This backs up your encrypted wallet to the Archon seed bank, recoverable from your mnemonic alone.

## Step 7: Store Your Mnemonic Securely

```bash
npx @didcid/keymaster show-mnemonic
```

**This is your recovery phrase.** Store it securely — it's the only way to recover your entire identity if you lose everything else.

## Recovery

### From Mnemonic (complete loss)
```bash
npx @didcid/keymaster import-wallet "word1 word2 word3 ... word12"
```

### From Seed Bank (wallet lost but mnemonic known)
```bash
npx @didcid/keymaster recover-wallet-did
```

### Retrieve Files from Vault
```bash
npx @didcid/keymaster get-vault-item backup workspace.zip workspace.zip
npx @didcid/keymaster get-vault-item backup config.zip config.zip
npx @didcid/keymaster get-vault-item backup hexmem.db hexmem.db
```

## Automation

Consider adding backup to your HEARTBEAT.md for periodic execution:
```markdown
### Weekly Backup
If it's been 7+ days since last backup, run the backup procedure and verify vault contents.
```

## Security Notes

- Your vault is encrypted — only you (and vault members) can decrypt contents
- The mnemonic is the master key — anyone with it can recover everything
- Secrets in config backup are encrypted at rest in the vault
- Archon's hyperswarm registry means your backup survives as long as any node has it
- Use `.backup-ignore` to ensure sensitive temp files aren't accidentally included
