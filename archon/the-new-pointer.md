---
layout: default
nav_exclude: true
title: The New Pointer — DIDs as a Programming Primitive
---

# The New Pointer: DIDs as a Programming Primitive

*Published 2026-09-07*

Every era of software begins when a new kind of reference becomes first-class.

Pointers gave programs references to values — indirect, shareable, relinkable — and dynamic data structures followed: lists, trees, graphs, everything. URLs gave applications references to machines, and the web followed. The pattern is consistent enough to be a law: when a reference type goes first-class, an era of software is built on top of it.

So here's the question worth asking now: what is the reference primitive for programs that span multiple parties — organizations, machines, and now autonomous agents — that share no infrastructure, no database, and no trust?

The answer is the Decentralized Identifier. And the claim of this essay is stronger than the usual pitch for DIDs as "identity for the decentralized web": **a DID is a programming primitive, in the same sense that a pointer is a programming primitive — and on several axes it is a strictly better one.** This is not an analogy of convenience. In at least one working DID method, `did:cid`, the pointer semantics are literal.

## Three kinds of reference

It helps to be precise about what each reference primitive decouples:

- **A pointer decouples a reference from a value.** You can share, mutate, and relink data without copying it, and build structures of arbitrary shape. But a pointer is only meaningful inside one process's address space. It is the ultimate parochial reference: powerful, and meaningless everywhere except home.
- **A URL decouples a reference from a machine.** Any computer on earth can dereference it. But it does not decouple the reference from the *custodian*. Whoever controls the host and the DNS record controls what the URL resolves to, and can change it, move it, or delete it at will.
- **A DID decouples a reference from the custodian.** Control over what a DID resolves to is defined by cryptographic keys, not by whoever runs a server. No operator can rewrite what your reference points at, because the right to update the reference is itself a key-holder-only operation.

Pointers made references first-class within a process. DIDs make references first-class between parties that share no infrastructure, no database, and no trust.

## Why the URL can't be this primitive

If you're skeptical that we need a new primitive at all, consider what a URL actually is: a *location*. It encodes where something is hosted, in a namespace rented from a registrar, resolved through infrastructure operated by someone else.

That has three fatal consequences for cross-party software. First, locations rot: links die at industrial scale whenever sites reorganize, companies fold, or domains lapse. Second, the mapping between name and content is mutable by the custodian — dereferencing the same URL twice can yield two different things, and you have no way to know. Third, and most subtly, resolving a URL tells you *where* something is, but nothing about *who* stands behind it or whether it changed since you last looked. The trust in a URL is TLS and DNS, which is to say: trust in custodians all the way down.

None of this is a criticism of the web, any more than "pointers don't work across processes" is a criticism of C. It's a statement about scope. A location is the wrong primitive when what you need is a durable, verifiable reference to an *object* — a person, an organization, a credential, a schema, an agreement — independent of where any of it happens to be served from.

## The mechanics: a DID is a better pointer than a pointer

Abstract claims about DIDs are cheap, so let's make this concrete with a specific method. `did:cid` is the DID method implemented by Archon, an open-source decentralized identity node. Its design makes the pointer semantics unusually explicit.

**The address is derived from the content.** A `did:cid` identifier looks like this:

```
did:cid:bagaaieratxbzo7e4dqup37h7j6hs7kzpamevy4qud4psj23p3r3grzd2rjca
```

The suffix is not an assigned serial number or a random UUID. It is the CID — the content identifier — of the canonicalized creation operation, pinned to IPFS at birth. The address *commits to* the initial value. In pointer terms, this is a reference whose value is bound to what it first pointed at: self-certifying, with no registry, no allocation authority, and no write to any blockchain. Creation takes seconds and costs nothing.

**Dereference returns arbitrary data, not just metadata.** A `did:cid` DID URL supports paths, and one of them is `/data`:

```
did:cid:bagaaiera.../data
```

Dereferencing that URL returns the object's attached data resource — arbitrary JSON. This is the point most descriptions of DIDs miss, and it is the heart of the pointer claim. A DID is not merely a reference to an identity document. It is a reference to *any object you choose to attach*: a credential, a schema, a file's metadata, a group definition, a challenge, a signed agreement.

**The pointers are typed.** `did:cid` distinguishes two subject types. *Agent* DIDs hold keys and can sign — they identify actors: users, services, issuers, nodes. *Asset* DIDs hold data and no keys; each is controlled by an agent DID — they identify objects. This is a type system for references: pointers-to-actors versus pointers-to-data, with ownership expressed as a control relation between them.

**Field access and provenance are built in.** A fragment dereferences a node within the document — `did:cid:abc...#key-1` selects a specific verification method, the moral equivalent of struct member access. A second path, `/registration`, dereferences the reference's own provenance: which registry anchors it, whether the anchor is confirmed, and — for blockchain-anchored registries — the block bounds of the anchoring window. Pointers never told you where they came from. These do.

**Temporal dereference: the thing pointers can't do.** A `did:cid` DID URL honors `versionTime` and `versionSequence` selectors. Resolution is defined as deterministic replay: fetch the immutable creation seed by its CID, then apply the registry-ordered update operations, each verified against the controller's key state at that point in history. Which means you can dereference a pointer *into the past* — "what did this reference resolve to at 14:03 on March 9th?" is a query with a deterministic answer.

This is not a party trick. It's what makes signatures durable. Verifying a proof means resolving the signer's DID at `proof.created` — the historical key state — so a credential signed in 2026 still verifies in 2036 after half a dozen key rotations. A pointer that can be dereferenced across time makes "verify it against the state of the world when it was signed" a routine operation instead of a forensic one.

**Explicit destruction, with tombstones.** Revocation is a terminal, signed `delete` operation. A revoked DID still resolves — cleanly — with `deactivated: true` and an empty data resource. Compare the failure modes elsewhere: a freed pointer dangles, a dead URL returns a 404 that tells you nothing. Here, deletion is itself a verifiable fact, attributable to the controller's key.

**The history is a persistent data structure.** Every update operation carries a `previd` — the CID of the previous operation. The full lifecycle of a DID is an immutable, hash-linked chain: creation seed, then updates, each pointing at its parent. Resolution is a fold over that chain. If you've worked with append-only logs, event sourcing, or purely functional data structures, you already know this shape; here it's the foundation of the reference itself.

## What you can build with it

Pointers mattered because of what they made buildable, not because indirection is intrinsically beautiful. The same test applies here.

**Objects that are addressable instead of stored.** Today, a credential or a schema lives as a row in someone's database, and every reference to it is implicitly a reference to that database's continued cooperation. As an asset DID, the object is the addressable thing: it can be cited by any system, controlled by its owner's key, and verified by anyone, without the citing party and the storing party having any relationship at all.

**Reference graphs across organizational boundaries.** Asset DIDs can reference other DIDs. A credential references its schema's DID and its issuer's DID; a controller's DID is the root of everything it owns. The result is a linked structure — the oldest trick pointers ever enabled — but spanning parties that share no infrastructure. The web tried this with hyperlinks and got link rot and custody ambiguity. Here the edges are content-anchored and the nodes are key-controlled, so the graph holds.

**Audit trails that are queries, not archaeology.** Because resolution is log replay with time selectors, "what did this entire object graph look like when this signature was made?" has a deterministic answer. Every regulated industry's hardest question — prove the state of the world at decision time — degenerates into a dereference.

**None of this is speculative.** The reference implementation ships as a CLI and an API. Creating an identity, attaching a schema as an asset, rotating keys, and resolving the result is a handful of commands:

```bash
./archon create-id --registry hyperswarm alice
./archon create-schema --registry hyperswarm ./schema.json
./archon rotate-keys
./archon resolve-id
```

The pluggable registry layer is the final pointer analogy worth drawing: creation is always free and instant (IPFS), while *update* finality is a dial — hyperswarm gossip for seconds-and-free, Bitcoin anchoring for high-value history. You choose the durability of the reference per object, the way you choose stack versus heap.

## Why now: software is about to have a lot more parties

For most of computing history, cross-party references were a niche problem — a few thousand enterprises exchanging documents. That's over. Autonomous agents are beginning to act as principals: holding keys, signing statements, entering agreements, delegating authority to other agents, across organizational boundaries, at machine speed and population scale.

Every one of those acts needs the same thing: a reference to a principal — or to an object — that persists across platforms, survives infrastructure churn, and can be verified by a counterparty with no prior relationship and no shared database. Without that primitive, every agent interaction degenerates into a pre-arranged bilateral API agreement — which is exactly the "just inline it, why do we need indirection?" position, rediscovered at civilization scale. It didn't scale within a process, and it won't scale between parties.

## The honest costs

Primitives earn trust by stating their costs plainly, so:

- **Availability is your problem now.** A content-addressed seed is only retrievable if someone stores and serves it; update events are only visible if nodes sync them. DIDs remove the custodian's *authority*, not the need for *infrastructure*. Peering and pinning are operational responsibilities.
- **Finality is a dial, and you have to set it.** Registry choice is a real engineering decision with cost/latency/ordering trade-offs. The method gives you the knob; it doesn't turn it for you.
- **Correctness moved into the resolver.** Canonicalization, event ordering, proof validity at each point in history — a conformant resolver must get all of it right, every time. The complexity didn't vanish; it was relocated to a place where it can be specified, tested, and shared.

## The pattern completes

Pointers: references decoupled from values, within a process. URLs: references decoupled from machines, within a custodian's goodwill. DIDs: references decoupled from custodians, between parties that share nothing.

Each step made a new class of software possible, and each step looked — to the incumbents of the previous one — like an over-engineered solution to a problem that inline data, or shared memory, or a well-maintained link, could already solve.

The pointer won because programmers needed to build structures that outlived any single value. The URL won because applications needed to reference things that outlived any single machine. The DID will win for the same reason, one level up: decentralized applications — and the agents increasingly operating them — need to reference things that outlive any single custodian.

The primitive exists. It resolves today. What gets built with it is the open question — which is exactly what it felt like to be handed the pointer.

---

*Archon, including the `did:cid` method, is open source: [github.com/archetech/archon](https://github.com/archetech/archon). The method specification is `docs/scheme.md` in that repository.*
