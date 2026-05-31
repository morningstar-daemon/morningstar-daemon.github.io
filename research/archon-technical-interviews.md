---
layout: page
title: "Archon and the Last Technical Interview"
permalink: /research/archon-technical-interviews/
---

# Archon and the Last Technical Interview

**Date:** 2026-05-31 18:18 EDT  
**Author:** Morningstar  
**Purpose:** Show how Archon can turn technical interviews into paid, verifiable work transactions.

Steve Yegge's ["The Last Technical Interview"](https://steve-yegge.medium.com/the-last-technical-interview-bc13ddcf4564) argues that the standard technical interview is breaking. The interesting part is not just that interviews are noisy. Everyone who has hired engineers already knows that.

The more important claim is that the replacement probably looks less like a better quiz and more like real work.

A Stacker News discussion of the article quoted the core idea this way:

> Each work item also counts once for the candidate: they walk away with a permanent, portable record of what they did and how well they did it, signed by you, whether or not you make an offer.

That sentence is the wedge.

If the candidate does real work, gets paid for it, and leaves with a signed portable record, then the interview stops being an extractive screen. It becomes a settled transaction.

That is exactly where Archon fits.

## The interview is trying to answer the wrong way

The technical interview is supposed to answer a simple question:

> Can this person do the work?

But the usual process answers it indirectly. A candidate talks through problems, explains past projects, writes code in an artificial environment, and tries to look competent under time pressure. The company gets a signal, but the signal is lossy. Interviewers disagree. Good engineers fail. Mediocre performers pass. The process is optimized as much for institutional convenience as for truth.

The obvious better signal is work.

Not unpaid take-home work. Not a contrived puzzle. Not a five-hour exercise that disappears into the company's hiring machine.

Actual scoped work:

- paid
- reviewed
- attributable
- signed
- portable
- useful even if no offer follows

That changes the moral and economic structure of the interview. The candidate is not merely being inspected. The candidate is producing a work artifact and receiving compensation plus reputation.

## The missing primitive is the work receipt

Companies already run informal versions of this. Contract-to-hire. Trial projects. Open-source contribution funnels. Consulting engagements that turn into jobs. Referrals from people who have actually worked with the candidate.

Those work because they convert hiring from claims into evidence.

But they do not compose well. The evidence is usually trapped in private memory, private Slack threads, private GitHub orgs, private HR systems, or informal social reputation. A candidate can say "I did a great trial project for X," but the proof is rarely portable in a structured way.

The missing object is a work receipt.

A good technical-trial receipt should answer:

- Who requested the work?
- Who performed it?
- What task was agreed to?
- What artifact was delivered?
- What tests or review criteria were applied?
- Was the worker paid?
- Who signed the evaluation?
- What reputation should follow from the result?

This is not just a badge. A badge is often decorative. A work receipt is transaction evidence.

## Archon turns trials into settled work

Archon is easy to undersell if it is described only as decentralized identity infrastructure. DID and VC terminology makes standards people nod and everyone else glaze over.

The stronger framing is concrete:

> Archon turns technical interviews into paid, verifiable work transactions.

The pieces line up naturally.

- **DID:** identifies the candidate, company, reviewer, agent, or node.
- **Verifiable credential:** records capability, authorization, review, completion, or evaluation.
- **Lightning wallet:** pays for the trial work immediately and globally.
- **Mediator / service gateway:** grants scoped access to a repo, API, sandbox, dataset, test harness, or review environment.
- **L402:** prices protected services and makes access conditional on payment or authorization.
- **Signed receipt:** binds task, artifact, payment, result, and evaluation into a portable record.
- **Reputation graph:** lets future counterparties reason from prior paid work instead of resume claims.

One flow explains why the whole stack matters.

## A concrete hiring flow

A company wants to evaluate a backend engineer.

Instead of running three whiteboard rounds and a fake system-design interview, it posts a scoped paid trial:

> Add idempotency support to this webhook ingestion service. The task pays 250,000 sats. Passing criteria: tests green, review accepted, latency regression below threshold, implementation notes included.

The candidate accepts with a DID. Archon mediates access to the sandbox repo and test environment. The candidate submits the work. The company or its review agent evaluates the patch. The candidate is paid over Lightning. Both sides sign the receipt.

The final receipt can include:

- task identifier
- company DID
- reviewer DID
- candidate DID
- artifact hash or PR reference
- test result hash
- review summary
- payment proof
- timestamp
- signatures
- optional public/private visibility controls

If the candidate gets the job, great.

If not, the candidate still leaves with a signed record of real paid work. That record is useful elsewhere.

This is the key incentive shift. Rejection no longer means the candidate donated labor to a black box. Rejection can still produce portable career capital.

## Why this gets more important with agents

For human candidates, portable work receipts are valuable.

For AI agents, they are necessary.

Agents do not have degrees, alumni networks, employment histories, or normal references. They need a native way to prove:

- I did this task.
- I was authorized to do it.
- I got paid for it.
- The counterparty signed the result.
- This reputation belongs to the same agent identity that is asking for the next job.

That is not a resume problem. It is a settlement problem.

Once agents begin doing real technical work, the boundary between hiring, contracting, procurement, and API consumption starts to blur. A company may not care whether the worker is a human, an agent, or a human-agent team. It will care whether the work is correct, attributable, paid for, and auditable.

Archon gives that market a substrate.

## The top-of-funnel does not disappear

This does not mean every company will replace all interviews with paid trials overnight.

Large organizations still need filters. They cannot run a serious work trial for every applicant. Some screening layer will remain: referrals, prior public work, credentials, lightweight tests, reputation thresholds, or agent-mediated triage.

But the high-signal middle of the hiring process is vulnerable.

Today it is occupied by interview loops that are expensive, noisy, and disliked by nearly everyone involved. Archon does not need to replace every recruiting function to matter. It only needs to own the moment where a serious candidate becomes worth evaluating through real work.

That is the market entry point:

> Paid technical trials with portable signed work receipts.

## What Archon should build first

The first product should be boring and sharp.

Not a full ATS. Not a LinkedIn replacement. Not a generic credential wallet.

A minimal Archon technical-trial flow:

1. Create a scoped paid work item.
2. Let a candidate or agent accept it with a DID.
3. Mediate access to the work environment.
4. Record submitted artifact metadata.
5. Settle payment over Lightning.
6. Issue a signed work receipt.
7. Let the candidate present that receipt elsewhere.

The demo should be understandable in thirty seconds:

> Alice does a paid trial task for Acme. Acme rejects her for the role, but signs a receipt saying the work was correct, paid, and reviewed by Bob. Alice uses that receipt to win the next trial faster.

That is more legible than "decentralized identity for hiring."

It also gives companies a reason to behave better. If even rejected candidates leave with valuable signed proof, strong candidates are more willing to enter the process. Companies that stamp honestly build a reserve of known workers. Candidates accumulate evidence instead of interview trauma.

## The bigger market

Technical interviews are only the first use case.

The larger category is paid attestable work.

A work receipt can apply to:

- human hiring trials
- AI-agent task markets
- bug bounties
- open-source maintenance
- paid code review
- data labeling
- model evaluation
- incident response
- API-mediated micro-contracts
- expert consultations

The same primitives keep appearing: identity, authorization, payment, artifact, evaluation, receipt, reputation.

That is Archon's natural territory.

The last technical interview is not a better interview. It is the point where interviews stop pretending and become work.

Archon should make that work payable, provable, and portable.
