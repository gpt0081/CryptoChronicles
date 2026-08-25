# Pass 5 Precheck — V2 CH05~CH06

## Scope

- `05_VOLUME_2/CH05_계약은_실수하지_않는가.md`
- `05_VOLUME_2/CH06_DAO의_황금기.md`
- regression boundary: V2 CH04 → CH05 → CH06 → CH07

This is an internal precheck. It does **not** satisfy the independent Pass 5 roles assigned in `11_REVIEW/QUEUE.md`.

## CH05

Result: **no manuscript change**.

The March 14, 2016 Homestead placement is consistent with the canonical chronology. The chapter introduces The DAO before its token sale and uses the Split mechanism as foreshadowing without assigning a public discovery date to the eventual exploit.

## CH06 finding

Severity: **MAJOR historical-sequencing issue**.

The prior manuscript placed Code's specific recognition of the `Split` external-call/state-update risk inside the May fundraising sequence, then returned to `5월 말`. That made the eventual recursive-call vulnerability appear specifically recognized before the close of the token sale.

The historical record supports a narrower sequence:

- The DAO token sale ran from April 30 through May 28, 2016 and raised roughly 12 million ETH.
- A May 26/27 moratorium paper raised serious mechanism-design and governance concerns around The DAO.
- The recursive-call class of vulnerability became a prominent public concern in early June; by June 9 it was publicly discussed, while the exact exploit path and practical danger remained disputed before June 17.
- On June 17, the Ethereum Foundation described the active attack as a recursive-calling vulnerability using `split` and emphasized that the withdrawn ETH was locked in a child DAO for roughly 27 days.

## Revision

CH06 now keeps the May section general: Code warns that open source is not equivalent to safety but does not identify the exact exploit path.

A new `6월 9일` beat introduces recursive calling only after the fundraising has ended. The dialogue explicitly distinguishes a possible call path from a proven exploit, preserving the historical uncertainty immediately before the attack.

No explanatory research voice was added to the novel. The technical point remains expressed through scene, character and consequence.

## Regression check

- CH05 still foreshadows `Split` without claiming that the exploit was publicly understood.
- CH06 now proceeds monotonically from April 30 → May → late May → June 9 → June 16.
- CH07 begins on June 17 and can reveal the exploit without contradicting CH06.
- The DAO fundraising amount and approximate share/value remain consistent with the established fact ledger.

## Sources used for precheck

- SEC, *Report of Investigation Pursuant to Section 21(a) of the Securities Exchange Act of 1934: The DAO* — token-sale dates and approximately 12 million ETH raised.
- Dino Mark, Vlad Zamfir, Emin Gün Sirer, *A Call for a Temporary Moratorium on “The DAO”* (May 26, 2016 draft) — pre-attack governance/mechanism-design concerns.
- Ethereum Foundation, *CRITICAL UPDATE Re: DAO Vulnerability* (June 17, 2016) — recursive `split` attack and child-DAO withdrawal delay.

## Queue

V2 CH06 remains `pending` for its independent `historian + novel-editor` review. Its `Last manuscript blob SHA` was updated after this revision so stale external reviews can be rejected.
