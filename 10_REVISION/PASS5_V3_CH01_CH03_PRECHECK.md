# Pass 5 V3 CH01–CH03 Precheck

## Scope

- `06_VOLUME_3/CH01_얼어붙은_시장.md`
- `06_VOLUME_3/CH02_스테이블코인의_부상.md`
- `06_VOLUME_3/CH03_보이지_않는_은행들.md`
- Adjacent regression target: `06_VOLUME_3/CH04_DeFi의_여름.md`
- Canon/reference: `09_RESEARCH/V3_FACT_LEDGER.md`, current manuscript on `main`

This is an internal precheck. It does **not** satisfy or replace the independent roles assigned in `11_REVIEW/QUEUE.md`.

## CH01 — no manuscript change

The dated infrastructure sequence in the chapter was rechecked against first-party/near-primary records:

- USDC official launch: 2018-09-26 (Circle/CENTRE)
- Compound money-market protocol launch: 2018-09-27 (Compound announcement)
- Uniswap public announcement and Ethereum mainnet deployment: 2018-11-02 (Hayden Adams / Uniswap history)

The chapter's sequence `USDC → next day Compound → Nov. 2 Uniswap` is consistent with those records. No blocker or prose intervention was justified.

## CH02 — no manuscript change

The chapter remains consistent with the V3 canon boundary: fiat-reserve stablecoins and crypto-collateralized Dai are not conflated, and the empty third chair is presented as a category/risk question rather than a claim that all later algorithmic stablecoins shared one mechanism.

USDC's 2018-09-26 launch date also remains correct. No factual or continuity blocker found.

## CH03 — MINOR / RESOLVED

### Finding

One mid-chapter passage temporarily shifted from novel prose into an explanatory inventory:

- `Maker는 안정화폐와 담보대출.`
- `Compound는 자금시장.`
- `Uniswap은 교환.`
- `Stablecoins는 결제와 기준단위.`
- `지갑은 사용자 계정.`
- `스마트 컨트랙트는 자동 집행.`

The information was broadly compatible with the project's research, but the list read like a taxonomy rather than a scene and duplicated functions already dramatized immediately before and after it.

### Resolution

Replaced the functional checklist with a visual city-map beat:

- Maker's vault
- Compound's windowless market
- Uniswap's pool
- wallets and contracts as scattered lights
- Ethereum connecting them until a financial-city outline appears

No new historical claim was introduced. The point that financial functions were being decomposed and recomposed remains intact.

### Manuscript fingerprint

- old blob: `881d3f925de931497a11971ff17a89883561185c`
- new blob: `b6daf59a2d1dc89946985362f3a3fba27c0f9533`

`11_REVIEW/QUEUE.md` was updated to the new blob SHA. V3 CH03 remains `pending` because its assigned independent `historian + novel-editor` reviews have not arrived.

## Regression check

- CH02 → CH03: stablecoin/Dai mechanics still transition naturally into the broader 2019 on-chain finance system.
- CH03 internal continuity: the new city-map image leads directly into the following composability/contagion section without changing any causal claim.
- CH03 → CH04: the closing governance-token/liquidity-incentive setup remains untouched, preserving the bridge into DeFi Summer.

## Result

- CH01: no change
- CH02: no change
- CH03: explanatory-voice cleanup merged into review branch; factual structure unchanged
- Independent Pass 5 status: still pending
