# Pass 5 V1 CH07 Internal Precheck

## Scope

- Manuscript: `04_VOLUME_1/CH07_두_장의_피자.md`
- Purpose: internal historical/technical precheck only
- External Pass 5 roles remain required: `continuity`, `character`

## Finding

### MINOR — block timing phrasing was technically inaccurate

The chapter described Bitcoin as being accustomed to “a few seconds of block delay.” That compresses Bitcoin block timing into a seconds-scale process and can mislead the reader about the protocol’s early cadence.

Bitcoin’s target block interval is approximately ten minutes, while actual intervals vary substantially. The narrative did not need a technical explanation; it only needed to avoid the false seconds-scale implication.

## Fix

Replaced:

> 그는 몇 초의 블록 시간 지연에는 익숙했지만 인간의 망설임은 훨씬 길게 느껴졌다.

with:

> 그는 들쭉날쭉한 블록 간격에는 익숙했지만 인간의 망설임은 훨씬 길게 느껴졌다.

This preserves the scene’s rhythm and contrast without inserting explanatory prose.

## Historical cross-check

The chapter’s core pizza chronology remains consistent with the historical record used for this precheck:

- Laszlo Hanyecz posted the 10,000 BTC pizza offer on May 18, 2010.
- On May 22, 2010, he reported the successful trade and thanked `jercos`.
- Jeremy Sturdivant (`jercos`) was the counterparty.

No additional manuscript changes were required in this pass.

## Regression check

- CH06 → CH07 transition remains intact: price discovery leads into tangible-goods exchange.
- CH07 → CH08 transition remains intact: ordinary exchange precedes Bitcoin’s darker-market phase.
- `11_REVIEW/QUEUE.md` fingerprint for V1 CH07 was updated to the new manuscript blob SHA.
- V1 CH07 remains `pending`; this precheck does not substitute for the independent Pass 5 roles.

## Result

`RESOLVED` for this internal finding. Independent Pass 5 review is still required before the chapter can be marked `reviewed`.
