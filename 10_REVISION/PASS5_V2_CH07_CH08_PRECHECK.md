# Pass 5 Precheck — V2 CH07–CH08

Status: internal precheck complete; independent Pass 5 roles still required.

## Scope

- `05_VOLUME_2/CH07_빈틈.md`
- `05_VOLUME_2/CH08_되돌릴_것인가.md`
- Adjacent continuity: V2 CH06 → CH07 → CH08 → CH09
- Canon and V2 research/fact-check material
- Ethereum Foundation primary-source posts from 2016-06-17, 2016-06-28, 2016-07-15, and 2016-07-20

## CH07 — RESOLVED VOICE FINDING

Historical sequence is consistent with primary sources: the DAO exploit was publicly identified on 2016-06-17 as recursive calling through `split`; the affected ether was held in a child DAO with roughly a 27-day withdrawal delay; a proposed soft fork was later found on 2016-06-28 to contain a high-severity DoS vector.

The manuscript contained a classroom-style bank-teller analogy explaining reentrancy. The explanation was accurate enough, but it stepped outside the established novel voice. It has been replaced with an embodied sequence in the scene:

- a withdrawal has not finished before the same hand returns;
- the ledger has not yet fallen before another call arrives;
- Code continues because the calls remain valid under the written rules.

No historical claim was added or removed. The change is narrative-only.

Primary sources:

- Ethereum Foundation, `CRITICAL UPDATE Re: DAO Vulnerability`, 2016-06-17: https://blog.ethereum.org/2016/06/17/critical-update-re-dao-vulnerability
- Ethereum Foundation, `Security Alert - DoS Vulnerability in the Soft Fork`, 2016-06-28: https://blog.ethereum.org/2016/06/28/security-alert-dos-vulnerability-in-the-soft-fork

## CH08 — NO BLOCKER FOUND

The chapter's central chronology matches the primary-source record:

- The Foundation explicitly stated on 2016-07-15 that neither it nor any single entity could make the hard-fork decision alone.
- The proposed irregular state change was targeted for block 1,920,000.
- The hard fork completed on 2016-07-20 at block 1,920,000.
- The Foundation reported roughly 85% of miners mining on the fork immediately afterward.
- The non-fork chain continued and later became Ethereum Classic.

Primary sources:

- Ethereum Foundation, `To fork or not to fork`, 2016-07-15: https://blog.ethereum.org/2016/07/15/to-fork-or-not-to-fork
- Ethereum Foundation, `Hard Fork Completed`, 2016-07-20: https://blog.ethereum.org/2016/07/20/hard-fork-completed

No manuscript change was required for CH08.

## Regression check

- CH06 still ends with the vulnerability having become a concrete public danger.
- CH07 now depicts the exploit and failed soft-fork path without slipping into textbook explanation.
- CH08 still advances naturally into the governance decision and chain split.
- No independent review status was advanced. V2 CH07 remains assigned to `continuity + red-team`; V2 CH08 remains assigned to `character + novel-editor`.

## Queue fingerprint

CH07 manuscript blob changed from `3b7dbabceaa143d121909a06622e4653742ef46d` to `45b47388b5ae9839847f7046282e99feedbbbfa3`. `11_REVIEW/QUEUE.md` was updated accordingly so stale external reviews can be rejected.