# Pass 5 V1 CH06 Precheck — 가격의 탄생

## Scope

- Manuscript: `04_VOLUME_1/CH06_가격의_탄생.md`
- Internal precheck only; does **not** satisfy the independent Pass 5 `historian + blind-reader` requirement.
- Canon references: `09_RESEARCH/FACT_CHECK.md`, `09_RESEARCH/FACT_LEDGER.md`, adjacent V1 chapters.

## Finding

### P5-V1-CH06-001 — first Bitcoin Market trade price presented too specifically

- Severity: **MINOR**
- Status: **RESOLVED**
- Area: historical precision / novel prose

The manuscript correctly places the first documented Bitcoin Market real trading activity on 2010-03-17. Contemporary forum evidence attributed to operator `dwdollar` records that the first real trade had occurred around noon that day.

However, the manuscript then displayed `0.003` inside that first-trade scene and repeated it in dialogue as though it were the documented matched price. The exact price and size of that first matched trade are not established by the available contemporary record. Later reconstructed price histories often associate roughly `$0.003/BTC` with early BitcoinMarket.com trading, but that is not sufficient to assign the number to the first trade itself.

This also aligns with the repository's existing `FACT_CHECK.md`, which classifies CH06 as `VERIFIED WITH CAVEAT` and notes that early Bitcoin Market contemporaneous sourcing still merits caution.

## Resolution

Removed the exact `0.003` assertion from the 2010-03-17 first-trade scene while preserving the dramatic function of the passage.

The revised prose describes only a tiny dollar-denominated figure and keeps the contrast between `no market price` and `someone committing money` without pretending that the first matched trade price is known.

No research explanation was inserted into the novel body.

## Regression check

- CH05 → CH06: early person-to-person transfer history remains intact.
- CH06 → CH07: the transition from price discovery to the May 2010 pizza purchase remains intact.
- The verified 2009-10-05 New Liberty Standard rate and the 2009-10-12 Martti Malmi / NewLibertyStandard trade remain unchanged.
- `11_REVIEW/QUEUE.md` fingerprint for V1 CH06 updated to the new manuscript blob SHA.

## Evidence consulted

- Repository: `09_RESEARCH/FACT_CHECK.md`, CH06 entry.
- Historical Bitcointalk discussion referencing dwdollar's 2010-03-17 post and the first real trade.
- Recent historical synthesis reproducing the contemporaneous March 16–17 dwdollar posts while noting the lack of exact first-trade price/size data.

## Pass 5 status

V1 CH06 remains `pending`. This precheck removes a known avoidable historical overstatement but does not replace independent external review.