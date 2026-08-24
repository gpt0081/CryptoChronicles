# Pass 5 V1 CH04-CH05 Internal Precheck

## Scope

- `V1-CH04 아무도 믿지 않는 화폐`
- `V1-CH05 첫 번째 동료들`
- Adjacent regression check: `V1-CH06 가격의 탄생`

This is an internal editorial precheck. It does **not** satisfy the independent Pass 5 roles assigned in `11_REVIEW/QUEUE.md`.

## CH04 result

No publication blocker found in the checked scope.

- 2009-01-08 Bitcoin v0.1 public announcement matches Fact Ledger `F-0011`.
- The chapter keeps the early participant unnamed and does not overwrite Hal Finney's explicit introduction in CH05.
- The transition from Genesis-era isolation to an independently runnable client remains consistent with `EVENT_LEDGER.md` S-0007.

## CH05 finding

**Severity:** MINOR  
**Status:** FIXED

The Block 170 scene temporarily shifted from novel prose into textbook explanation:

> 이전의 초기 블록들에도 coinbase transaction은 있었다. 새 블록이 만들어지면서 새 Bitcoin이 생성되는 기록이었다.

The factual distinction was valid, but the phrasing explained protocol terminology to the reader instead of keeping the event inside the narrative voice.

### Editorial fix

Replaced the explanation with:

> 초기 블록들에도 새 Bitcoin이 태어나는 기록은 있었다.
>
> 그러나 이번에는 달랐다.
>
> 이미 존재하던 Bitcoin이 한 사람에게서 다른 사람에게 이동했다.

This preserves the factual distinction behind Fact Ledger `F-0022` while removing the research/manual tone from the manuscript.

## Regression check

- CH04 still hands off cleanly to Hal Finney's named appearance in CH05.
- CH05 still establishes the 2009-01-12 Block 170 10 BTC transfer and the transition from issuance to participant-to-participant transfer.
- CH06 still begins nine months later with the unresolved question of price; the CH05 edit does not change that setup.
- No new historical claims were introduced.

## Queue/version impact

CH05 manuscript blob changed from `6383a826cf234adcc7f884c5b4af7fe411199544` to `45a61f3fd2e2f131e83a69304b70940a4a5484e7`. The Pass 5 queue fingerprint was updated accordingly. CH04 and CH05 remain `pending` because this internal precheck is not a substitute for their assigned independent review roles.
