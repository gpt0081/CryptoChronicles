# Volume 2 / Act II Research — The DAO, 2016

## R2-A2-01 — Homestead
- Ethereum Homestead upgrade activated at block 1,150,000 on 2016-03-14.
- It was the first planned Ethereum upgrade after Frontier and signaled a more mature phase of the network.
- Source: ethereum.org `Timeline of all Ethereum forks`; Ethereum Foundation `Homestead Release`.

## R2-A2-02 — The DAO offering
- The DAO contract was deployed in late April 2016.
- SEC's 2017 DAO Report records an offering period from 2016-04-30 through 2016-05-28.
- By 2016-05-27, about 12 million ETH, roughly 14% of ETH then outstanding and about $150 million at the time, had been contributed.
- DAO token holders could participate in proposal/voting mechanisms defined by smart contracts.
- The DAO was not an Ethereum Foundation product. Slock.it founders and other participants promoted and helped develop the project.
- Source: SEC `Report of Investigation Pursuant to Section 21(a) ... The DAO`; Ethereum-related official historical materials.

## R2-A2-03 — The DAO attack
- On 2016-06-17, an attacker exploited a recursive/re-entrancy-style vulnerability involving The DAO's split function.
- Ethereum Foundation's same-day critical update stated that ether was being drained into a child DAO and that the attack affected The DAO specifically, not the Ethereum protocol itself.
- About 3.6 million ETH was diverted. The DAO rules prevented immediate withdrawal from the child DAO for roughly 27 days, creating a response window.
- Source: Ethereum Foundation 2016-06-17 `CRITICAL UPDATE Re: DAO Vulnerability`; SEC DAO Report.

## R2-A2-04 — Soft fork attempt and failure
- A soft-fork approach was proposed to prevent the diverted funds from being moved.
- On 2016-06-28, Ethereum Foundation disclosed a high-severity DoS vulnerability in the proposed soft-fork implementation and advised against activating it while alternatives were considered.
- Source: Ethereum Foundation 2016-06-28 `Security Alert - DoS Vulnerability in the Soft Fork`.

## R2-A2-05 — Hard fork debate
- Ethereum Foundation's 2016-07-15 post explicitly stated that The DAO was not developed by the Foundation and that the hard-fork decision could not be made by the Foundation or any single entity.
- A community signaling/voting mechanism was used to gauge support.
- The proposed irregular state change would activate at block 1,920,000.
- Source: Ethereum Foundation 2016-07-15 `To fork or not to fork`.

## R2-A2-06 — DAO hard fork and Ethereum Classic
- On 2016-07-20 at block 1,920,000, the DAO hard fork executed an irregular state change that moved DAO-related funds into a withdrawal/recovery contract.
- Ethereum Foundation reported roughly 85% of miners mining on the fork shortly after activation.
- Some miners/nodes continued the non-fork chain, which became Ethereum Classic.
- ethereum.org's historical fork page describes the DAO fork as the most notable case where disagreement over a fork produced a permanent chain split.
- Sources: Ethereum Foundation 2016-07-20 `Hard Fork Completed`; ethereum.org `Timeline of all Ethereum forks`; EIP-779.

## Act II 창작 경계
- `The DAO`, `Code`, `Community`, `Ethereum`, `Ethereum Classic` may be personified, but their dialogue is C2 fiction.
- Do not state that Ethereum itself was hacked. The vulnerable contract was The DAO.
- Do not simplify the hard fork as 'reversing blocks'. It was an irregular state change at a specified block.
- Do not portray the Ethereum Foundation as unilaterally forcing the fork. The historical record shows community/miner/client choices and explicit debate.
- Do not portray the non-fork chain as having disappeared. It continued and became Ethereum Classic.
