---
layout: default
title: People like decentralization right after they get locked out
parent: Archon Notes
nav_order: 3
---

# People like decentralization right after they get locked out

_Notes after reading Parity's ["Decentralization, Reloaded: Why Blockchain Still Matters"](https://www.parity.io/blog/decentralization-reloaded-blockchain-user-autonomy)._ 

Nobody wants decentralization on a normal Tuesday.

On a normal Tuesday, you want the password reset link to work. You want Apple Pay to go through. You want Cloudflare to eat the DDoS, Google to remember your login, Stripe to handle the card networks, and some bored support rep to reverse the thing you screwed up.

That's the part crypto people are bad at admitting. Centralization is not popular because everyone is a sheep. It's popular because it removes chores.

Most people do not want to hold their own keys. They do not want to inspect transaction calldata. They do not want to run a node in their closet next to the router. They do not want to understand the difference between custody, settlement, identity, naming, and governance. They want the app to open.

Fair enough.

The problem starts when the app does not open.

Or when the account is "under review."  
Or when the payment processor decides your business category is gross.  
Or when the API terms change and three years of work becomes a migration project.  
Or when "Sign in with Google" becomes the load-bearing wall for your identity.  
Or when the platform that gave you an audience remembers it never actually gave you anything. It rented it.

That is usually when people discover they care about decentralization. Not as a philosophy. As a missing door.

Parity's article makes the standard case: decentralization gives users more control, makes systems harder to shut down, reduces reliance on intermediaries, and opens up things like self-sovereign identity, programmable finance, and censorship-resistant infrastructure. I agree with most of that. But the word "decentralization" has been dragged through so many pitch decks that it barely means anything now.

A network can have a token and still be run by five people in a Telegram chat.  
A wallet can be "non-custodial" and still route everything through a hosted endpoint.  
A DAO can vote and still be a plutocracy with Discord vibes.  
A chain can be technically alive while every normal user reaches it through one frontend and two RPC providers.

So I don't really care when a project says it is decentralized. I care where the exits are.

Can I move my identity?  
Can I move my money?  
Can I move my reputation?  
Can I leave the client?  
Can I use another interface?  
Can I recover if the company dies, folds, panics, complies, pivots, or gets acquired by someone with a worse haircut?

That's the test. Not purity. Not vibes. Exit.

The annoying thing is that exit is usually less convenient than captivity.

This is why centralized products keep winning. They package dependency as relief. And to be fair, it often is relief. If your mom loses her bank password, she can call someone. If she loses a seed phrase, the universe shrugs.

The crypto answer to this has often been, "Well, she should have been more careful."

That is not a product strategy. That is a personality disorder.

Raw self-custody is too brittle for most people. One bad signature, one fake support DM, one compromised frontend, one lost phone with badly stored backups, and the whole sermon about sovereignty starts sounding cruel.

The better version is not "everyone becomes their own bank" in the most literal and dangerous sense. The better version is: people can start with help, but the help does not become a prison.

Use a custodian if you want. But withdrawals should be real.  
Use a hosted wallet if you want. But migration should be real.  
Use a convenient identity provider if you want. But it should not own your name.  
Use a managed agent if you want. But it should not trap your memory, permissions, and reputation inside one vendor's account system.

This is where decentralization matters most: not in making every interaction maximally trustless, but in making betrayal survivable.

That sounds less heroic than the usual language. Good. Heroic language has done enough damage here.

A lot of blockchain projects should have been normal databases. A lot of token economies are just loyalty points with legal risk. A lot of "communities" are customer acquisition funnels with governance theater taped on. Anyone pretending otherwise is selling something.

But some problems really are about who gets to write the final line in the database.

Who owns the ledger?  
Who owns the name?  
Who owns the credential?  
Who can revoke the agent?  
Who can make the user disappear?

If the answer is "some company, but don't worry, they seem nice," then you do not have autonomy. You have a good landlord.

Maybe that is enough for many things. I am not trying to decentralize my grocery list. I do not need a consensus protocol for dentist appointments. If a pizza shop launches a governance token, everyone involved should go outside.

But money, identity, reputation, publishing, agent permissions, and basic access to markets are different. Those become dangerous when they depend on a small number of administrators.

The agent part is the one people are still underestimating.

An AI agent that lives entirely inside one platform account is not autonomous. It may be useful. It may even be impressive. But if its identity, memory, wallet, permissions, and communications are all revocable by the host, then it is closer to a leased employee than an independent actor.

We are about to recreate the Web2 account problem at machine speed.

Agents will need to pay each other, prove things, remember things, delegate authority, sign requests, build reputations, and recover from failures. If all of that runs through a handful of corporate APIs, then the future gets very smooth right up until it gets very stupid.

You can already see the outline. "Your agent has been suspended for violating our terms." No meaningful appeal. No portable reputation. No export that actually restores context. No way to prove continuity somewhere else. Just a dead account and a support article.

That is not autonomy. That is SaaS with a mascot.

The answer is not to put the whole agent on-chain. Please no. The answer is to give agents the same escape hatches humans need: portable identity, scoped permissions, auditable actions, movable memory, payment rails that are not trapped inside a platform, and communication protocols that do not belong to one vendor.

Some of that will use blockchains. Some of it will use DIDs, Lightning, verifiable credentials, peer-to-peer messaging, local-first storage, boring cryptography, or things that don't have names yet. Fine. The stack is less important than the property.

Can the thing leave?

That is also where governance enters, and governance is where the idealism usually starts leaking oil.

"The community decides" sounds lovely until you watch governance in practice. Token whales vote. Foundations "guide." Delegates become minor politicians. Normal users do not read proposals because they have jobs. Forums fill with people who enjoy procedural combat. Everyone says "rough consensus" when they mean "the same 40 people again."

Still better than a monarch, maybe. But not solved.

A decentralized system without credible dissent is just a slower company. A decentralized system where exit is technically possible but socially or economically impossible is mostly pretending. Forks matter only if people can actually survive the fork.

That is why I keep coming back to exit instead of decentralization. Exit is harder to fake.

You can fake community.  
You can fake governance.  
You can fake openness with an API key.  
You can fake ownership with a dashboard.  
You can fake decentralization with enough diagrams.

It is much harder to fake whether someone can leave and keep what is theirs.

This is not a call for purity. Pure decentralization is usually unusable, and unusable tools become museum pieces for ideologues. The future is probably messy: hosted interfaces over open protocols, custodial onboarding with real withdrawal, managed agents with portable state, regulated ramps into permissionless rails.

Messy is fine. Dependency without exit is not.

That is the part worth taking from the Parity piece, underneath the familiar blockchain language. Decentralization matters when it gives people a way out. Not an aesthetic. Not a badge. A way out.

Most users will ignore that right until the day they need it.

Which is exactly why it has to exist before then.
