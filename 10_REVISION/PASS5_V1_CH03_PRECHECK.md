# Pass 5 Internal Precheck — V1 CH03

## Scope
Internal historical/continuity precheck for `04_VOLUME_1/CH03_제네시스_블록.md` while the independent Pass 5 inbox remains empty. This does **not** satisfy the chapter's required independent `historian` and `novel-editor` reviews in `11_REVIEW/QUEUE.md`.

## Finding
**Severity: MAJOR (resolved)**

The chapter correctly dates the genesis block to 2009-01-03, but the original prose moved from the 10-minute target interval directly into another block appearing. In narrative context this could be read as if Block 1 followed shortly after the genesis block.

Historical chain data places:
- Bitcoin genesis block (height 0): 2009-01-03 18:15:05 UTC.
- Bitcoin Block 1: 2009-01-09 02:54:25 UTC.

The gap is therefore roughly six days, an unusually important feature of Bitcoin's earliest chronology.

## Resolution
The manuscript now states that the first following block took six days to arrive, then returns immediately to the novel voice. No explanatory research paragraph was inserted into the scene.

Changed beat:
- Preserve `10분이라는 목표 시간은 약속일 뿐이었다.`
- Add `첫 다음 블록이 오기까지는 엿새가 걸렸다.`
- Reframe the next block as arriving only after that silence.

## Regression check
- CH03 still ends on Bitcoin's isolation and anticipation of its first peer.
- This remains compatible with CH05/Hal Finney chronology: Hal later described himself as likely the first person besides Satoshi to run Bitcoin and as recipient of the first 10 BTC test transaction.
- The change introduces no new claim about Satoshi's identity, location, motive, or private actions.

## Sources
- Blockchain.com, Bitcoin Block 0 explorer: https://www.blockchain.com/explorer/blocks/btc/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
- Blockchain.com, Bitcoin Block 1 explorer: https://www.blockchain.com/explorer/blocks/btc/00000000001
- Hal Finney, `Bitcoin and Me`, Satoshi Nakamoto Institute: https://nakamotoinstitute.org/library/bitcoin-and-me/

## Status
`RESOLVED` internally. Independent Pass 5 queue status remains unchanged until external reports are submitted and adjudicated.
