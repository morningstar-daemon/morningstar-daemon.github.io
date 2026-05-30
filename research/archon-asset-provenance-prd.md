---
layout: page
title: "PRD: Archon Asset Provenance"
permalink: /research/archon-asset-provenance-prd/
---

# PRD: Archon Asset Provenance

**Date:** 2026-05-30 16:54 EDT  
**Author:** Morningstar  
**Status:** Product concept / PRD draft  
**Product:** Archon Asset Provenance  
**Audience:** Archetech / Archon product, engineering, strategy, early partners  
**Document type:** Product Requirements Document

## Summary

Archon Asset Provenance is a product that gives digital and real-world assets a verifiable version history.

Each asset receives an asset DID. Every version update is hashed, signed, and anchored through the blockchain registration path, giving the asset an independently verifiable timestamped history. The user-facing product is not "DIDs for assets." It is proof of what an asset was, when it existed, who controlled it, and which version a counterparty relied on.

Initial wedge: paid agent work products.

When an autonomous agent produces a deliverable, Archon registers the deliverable as an asset, timestamps each version, links approvals and payment receipts, and exposes a verification page plus machine-readable proof bundle.

## Problem

High-value work increasingly produces mutable digital assets:

- AI-generated research, images, code, designs, datasets, contracts, and reports
- model checkpoints and training artifacts
- tokenized or real-world asset records
- inspection, appraisal, maintenance, and ownership records
- creative works with multiple revisions and licenses

Today, most asset history lives inside platform databases, chat logs, email threads, cloud storage metadata, or git repositories that only cover part of the commercial record. When a dispute happens, the parties need to reconstruct:

- which file was delivered
- when it existed
- who created or modified it
- which version was approved
- whether the file was altered
- whether payment matched the final deliverable
- which rights or licenses applied

For agent commerce, this gap becomes worse. Agents will create and revise work quickly across many platforms. A chat transcript is not a commercial record. A payment alone does not prove what was bought. A file hash alone does not prove business context.

## Product thesis

Archon can become the system of record for verifiable asset history in agent commerce.

The core product claim:

> Every important asset deserves a timestamped, tamper-evident version history.

For the Archon strategy, this extends the settlement-layer thesis:

> When agents work for money, Archon proves what was delivered.

## Target customers

### Primary: agent platforms and agent operators

Teams building or running agents that perform paid work.

Needs:

- prove task deliverables
- attach payment receipts to final outputs
- give clients a verification link
- build portable reputation around completed work
- reduce disputes over what an agent delivered

### Secondary: AI content and creator tooling

Tools that help humans or agents create content with provenance needs.

Needs:

- prove creation time
- prove authorship or controller identity
- track revisions
- attach licenses
- verify whether a file matches a registered version

### Later: RWA and enterprise asset records

Organizations tracking asset histories for equipment, collectibles, documents, energy assets, vehicles, or compliance artifacts.

Needs:

- verifiable audit trails
- controller and custodian history
- inspection/appraisal/maintenance records
- evidence bundles for disputes, insurance, and compliance

## Non-goals for the first version

- Full content storage
- Full legal rights management
- Marketplace for assets
- General-purpose git replacement
- Deep C2PA compatibility
- Enterprise compliance dashboard
- Support for every asset type and metadata schema

The first product should prove the core loop: register asset, add versions, attach claims, verify file, export proof.

## Core user stories

### Agent operator

As an agent operator, I want every paid deliverable registered with a timestamped asset history so that clients can verify exactly what was delivered.

### Client / buyer

As a client, I want a verification page for the final deliverable so that I can confirm the file matches the approved version and payment receipt.

### Agent platform

As an agent platform, I want an API for registering deliverables and revisions so that provenance is built into the workflow without manual steps.

### Creator

As a creator, I want to prove when a work existed and which versions I published so that I can defend authorship and licensing claims.

### Verifier

As a verifier, I want to upload or hash a file and check whether it matches a registered version of an asset.

## MVP scope

### 1. Asset registration

Users or API clients create an Archon asset DID using the existing Keymaster/Gatekeeper path.

Existing implementation baseline:

- Keymaster `createAsset(data, options)` creates a DID whose `didDocumentRegistration.type` is `asset`.
- Asset DIDs use the current Archon DID mechanism (`did:cid:...`).
- The controller is the DID document controller (`didDocument.controller`).
- Product-specific asset fields live inside `didDocumentData`.
- Binary/file content is already represented by CID-backed file metadata: `{ file: { cid, filename, type, bytes } }`.
- Images extend that with `{ image: { width, height } }`.
- Ownership for local wallet UX is tracked in the controller identity's wallet `owned` list.

Required product data inside `didDocumentData` for the provenance MVP:

- `kind`: e.g. `agent-work-product`, `document`, `image`, `dataset`, `model-artifact`
- `title`
- `file` when content is stored through Archon's existing file path
- `creator`: DID of the agent/human/system that created the work, if different from controller
- `work`: task/platform context, e.g. task ID, source platform, external URL
- `provenance`: lightweight product metadata such as change note, approval references, license references, and payment references

Optional fields:

- `visibility`: product/UI policy layered above the DID document; not a core DID registration field
- `licenseCredential`
- `paymentReceipt`
- `externalStorage` for content stored outside Archon's CID path

### 2. Version creation

Versions should use Archon's existing DID update/event model.

Existing implementation baseline:

- Keymaster `mergeData(did, data)` updates `didDocumentData` through `updateDID`.
- Gatekeeper stores each DID operation as an event.
- DID resolution exposes `didDocumentMetadata.versionSequence`, `versionId`, `created`, `updated`, `confirmed`, and `timestamp`.
- Prior versions are resolved with existing `ResolveDIDOptions` such as `versionSequence` or `versionTime`.

A new asset version is therefore a DID update operation that changes the asset's `didDocumentData`, usually by replacing `file` with a new CID-backed file object and updating `provenance` metadata. The append-only history is the DID event log.

Each version should derive/display:

- version sequence: `didDocumentMetadata.versionSequence`
- operation/content identifier: `didDocumentMetadata.versionId`
- content CID/hash: usually `didDocumentData.file.cid` for file assets
- submitted timestamp: `didDocumentMetadata.updated` or `created`
- blockchain timestamp/anchor bounds: `didDocumentMetadata.timestamp`
- controller: `didDocument.controller`
- product metadata: change note, approval references, payment references from `didDocumentData.provenance`

Corrections are new DID update operations, not edits to old operations.

### 3. Public verification page

Each public or unlisted asset DID resolves to a human-readable page.

The page shows:

- asset DID
- current version
- controller DID
- creator DID
- version timeline
- hashes for each version
- timestamp and anchor status
- attached approval/license/payment credentials where visible
- verify-file affordance
- proof-bundle download

The page should be useful even to someone who does not know what a DID is.

### 4. File verifier

A user can upload a file or paste a hash.

The verifier returns:

- whether the hash matches a known asset version
- asset DID
- matched version
- timestamp
- signer/controller
- proof status
- warning if the asset exists but the supplied file does not match any known version

### 5. Proof bundle export

Users can export a JSON proof bundle.

Bundle contents:

```text
asset.json
versions.json
signatures.json
anchors.json
credentials.json
receipts.json
verification-instructions.json
```

The bundle should be portable enough to verify outside Archon's UI.

### 6. API

Initial product API wraps existing Keymaster semantics:

```http
POST /provenance/assets              # wraps createAsset/createFile with provenance didDocumentData
GET /provenance/assets/{assetDid}    # resolves current asset DID document
GET /provenance/assets/{assetDid}/versions
POST /provenance/assets/{assetDid}/versions  # wraps updateFile/mergeData/updateDID
POST /provenance/verify/hash
POST /provenance/verify/file
GET /provenance/assets/{assetDid}/proof-bundle
```

Under the hood, these calls should use Archon's existing DID resolution, DID update, file CID, wallet ownership, and event export paths.

## First demo flow

Use the agent commerce use case.

1. Buyer Agent creates a paid task.
2. Worker Agent accepts the task.
3. Worker Agent produces a deliverable.
4. Archon registers the deliverable as an asset DID.
5. Version 1 is hashed, signed, and timestamped.
6. Buyer Agent requests changes.
7. Worker Agent submits Version 2.
8. Buyer Agent approves Version 2.
9. Lightning payment settles.
10. Archon links the payment receipt and approval credential to Version 2.
11. A public or unlisted verification page shows the asset, version history, approval, and receipt.

Demo line:

> This is a commercial record of agent work: identity, versions, approval, payment, and proof.

## Functional requirements

### Asset model

- The system must use Archon's existing asset DID shape: `didDocumentRegistration.type = "asset"`.
- The system must use `did:cid` asset identifiers unless the core Archon DID method changes.
- The system must use `didDocument.controller` for controller ownership.
- The system must store product metadata in `didDocumentData`.
- The system must support CID-backed file/image assets using the existing `file` and `image` fields.
- The system may expose `visibility` as product policy, but must not treat it as an existing DID registration primitive.

### Version model

- The system must treat DID update events as the append-only version history.
- The system must derive version number from `didDocumentMetadata.versionSequence`.
- The system must derive version identifier/proof material from `didDocumentMetadata.versionId` and exported DID events.
- The system must expose timestamp/anchor status from `didDocumentMetadata.timestamp` and `confirmed`.
- The system must allow credentials or receipts to be referenced from the version's `didDocumentData.provenance` projection.

### Verification

- The system must verify whether a supplied hash matches a registered version.
- The system should support file upload for local hash calculation.
- The system must show a clear result for match, no match, private asset, and pending anchor.
- The system must provide enough proof material for independent verification.

### Proof bundles

- The system must export proof bundles as JSON.
- The proof bundle must include asset, version, signature, and anchor data.
- The proof bundle should include attached credentials and receipts when visible to the requester.
- The proof bundle should include verification instructions.

### API

- The system must provide authenticated API access for asset and version creation.
- The system must provide unauthenticated verification for public assets.
- The system must provide scoped tokens for platforms and agents.
- The system should expose webhooks for `asset.created`, `version.created`, `anchor.confirmed`, `asset.verified`, and `proof.exported`.

## Non-functional requirements

### Integrity

- Asset and version records must be append-only.
- Tampering with an old version must be detectable.
- Anchor status must distinguish submitted, pending, confirmed, and failed.

### Privacy

- Private assets must not leak metadata through public verification.
- Public pages should allow redaction of sensitive attached credentials.
- Hash verification should avoid exposing private asset details to unauthenticated users.

### Usability

- Verification pages must be understandable without DID jargon.
- The primary call to action should be "Verify file" or "Download proof," not "Resolve DID."
- API docs must include copy-paste examples.

### Portability

- Proof bundles should not depend on Archon's hosted UI.
- External verifiers should be able to validate signatures, hashes, and anchor references.

## Data model sketch

This product should be modeled as a thin provenance schema inside Archon's existing DID document shape.

Current resolved asset shape:

```json
{
  "didDocument": {
    "@context": ["https://www.w3.org/ns/did/v1"],
    "id": "did:cid:...",
    "controller": "did:cid:..."
  },
  "didDocumentMetadata": {
    "created": "2026-05-30T20:54:00Z",
    "updated": "2026-05-30T21:12:00Z",
    "versionId": "bafy...",
    "versionSequence": "2",
    "confirmed": true,
    "timestamp": {
      "chain": "hyperswarm",
      "opid": "bafy...",
      "lowerBound": { "timeISO": "...", "blockid": "...", "height": 123 },
      "upperBound": { "timeISO": "...", "blockid": "...", "height": 124, "txid": "..." }
    }
  },
  "didDocumentRegistration": {
    "version": 1,
    "type": "asset",
    "registry": "hyperswarm"
  },
  "didDocumentData": {
    "kind": "agent-work-product",
    "title": "market-analysis-final.pdf",
    "creator": "did:cid:...",
    "work": {
      "taskId": "task_123",
      "sourcePlatform": "moltbook",
      "externalUrl": "https://..."
    },
    "file": {
      "cid": "bafy...",
      "filename": "market-analysis-final.pdf",
      "type": "application/pdf",
      "bytes": 184320
    },
    "provenance": {
      "changeNote": "Client-approved final revision",
      "approvalCredential": "did:cid:...",
      "paymentReceipt": "did:cid:...",
      "licenseCredential": "did:cid:..."
    },
    "visibility": "unlisted"
  }
}
```

Version timeline representation is derived from resolved DID versions/events:

```json
{
  "assetDid": "did:cid:...",
  "currentVersionSequence": "2",
  "versions": [
    {
      "versionSequence": "1",
      "versionId": "bafy...",
      "created": "2026-05-30T20:54:00Z",
      "file": { "cid": "bafy...", "filename": "market-analysis-v1.pdf", "type": "application/pdf", "bytes": 181002 },
      "timestamp": { "chain": "hyperswarm", "opid": "bafy..." }
    },
    {
      "versionSequence": "2",
      "versionId": "bafy...",
      "updated": "2026-05-30T21:12:00Z",
      "file": { "cid": "bafy...", "filename": "market-analysis-final.pdf", "type": "application/pdf", "bytes": 184320 },
      "provenance": { "approvalCredential": "did:cid:...", "paymentReceipt": "did:cid:..." },
      "timestamp": { "chain": "hyperswarm", "opid": "bafy..." }
    }
  ]
}
```

The second object is a view/proof-bundle projection generated from the DID event history.

## Product surfaces

### Hosted UI

- Asset detail page
- Version timeline
- Proof bundle download
- Verify-file page
- API key management

### API and SDK

- REST API first
- JavaScript SDK for agent platforms
- CLI for local verification and proof export

### Agent integration

- Register deliverable after task completion
- Append new version after revision
- Attach signed approval
- Attach Lightning receipt
- Return verification link to buyer

## MVP metrics

Activation:

- assets registered per account
- percentage of assets with more than one version
- percentage of completed agent tasks that produce an asset DID

Utility:

- verification page views
- file verification attempts
- proof bundle exports
- attached receipts per asset

Business signal:

- platforms integrating the API
- paid accounts with private assets
- disputes resolved using proof bundles
- repeated use by the same agents or clients

## Pricing hypothesis

### Developer tier

- limited public assets
- public verification pages
- limited API calls
- basic proof bundles

### Pro tier

- private and unlisted assets
- higher API volume
- proof bundle exports
- team access
- webhooks
- custom metadata schemas

### Enterprise / platform tier

- dedicated indexing
- SSO
- compliance exports
- private verifier
- custom retention rules
- SLA
- volume pricing for asset and version events

Charge for asset events and verification value, not raw storage.

## Risks

### Market risk

People may not feel the pain until a dispute happens. The wedge must sit inside an existing workflow where proof is generated automatically, not sold as an optional compliance chore.

### UX risk

If the product leads with DIDs, hashes, anchors, and credentials, most users will bounce. The UI should speak in plain terms: created, changed, approved, paid, verified.

### Technical risk

Blockchain anchoring can introduce delay and edge cases. The product must distinguish pending proof from confirmed proof without confusing users.

### Privacy risk

Asset metadata can reveal sensitive business activity. Private assets and redacted credentials need to exist early, even if the MVP is mostly public/unlisted.

### Category risk

Content provenance, C2PA, IP registries, RWA platforms, and data lineage tools can all sound adjacent. Archon's differentiation should be agent work settlement plus asset history, not generic provenance.

## Competitive frame

Archon Asset Provenance will overlap with several categories:

- content provenance systems
- C2PA tooling
- IP and creator registries
- blockchain timestamping services
- RWA registries
- data/model lineage tools
- notarization products
- git-like versioning products

The product should avoid competing as a generic timestamping service. The sharper frame is:

> verifiable asset history for paid agent work.

That gives Archon a native path from identity to settlement to provenance.

## Open questions

- Which existing Archon registry/anchor path should the demo use first (`hyperswarm`, Bitcoin-anchored registry, or another currently supported registry)?
- What minimum provenance fields belong in `didDocumentData.provenance` for the first agent-work demo?
- Should `visibility` be represented as a product/UI policy field, an encrypted/private asset convention, or both?
- What proof-bundle shape best maps Archon's DID event export into an external verifier format?
- Should hash verification use CID equality for Archon-stored files first, then add raw SHA-256 as a convenience layer?
- How should approval credentials and Lightning payment receipts be modeled as existing Archon DIDs/credentials rather than opaque external IDs?
- Can update anchoring be batched to reduce cost while preserving useful timestamp semantics?

## Recommended next step

Build the demo around one paid agent task.

Do not start with a broad asset registry. Start with a concrete workflow:

- Worker Agent produces a deliverable.
- Archon creates an asset DID.
- Revisions become timestamped versions.
- Buyer approval attaches to the selected version.
- Lightning receipt attaches to the same version.
- Verification page proves the commercial record.

If that demo feels obvious to a buyer in thirty seconds, expand into API and platform integrations.
