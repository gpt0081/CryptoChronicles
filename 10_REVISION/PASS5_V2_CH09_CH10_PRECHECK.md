# Pass 5 Precheck — V2 CH09~CH10

Status: COMPLETE (internal precheck only; does not satisfy independent Pass 5 roles)

## Scope
- V2 CH09 `두 개의 Ethereum`
- V2 CH10 `블록 크기 전쟁`
- Regression read into V2 CH11 `ICO의 불꽃`

## CH09 — no manuscript change

`09_RESEARCH/V2_FACT_LEDGER.md`의 V2-F020과 대조했다. 비포크 체인이 2016-07 이후 계속 블록을 만들며 Ethereum Classic으로 존속했다는 핵심 사실, block 1,920,000에서의 분기, 두 체인이 같은 과거를 공유한다는 서술은 현재 원고와 일치한다.

새로운 역사·연속성 blocker를 발견하지 않았다.

## CH10 — finding and resolution

### Finding
기존 도입부는 프로토콜 규칙 변경 문제를 두고 다음처럼 서술했다.

> 그 질문에는 백서에도 짧은 답만 있었다.
> 사람들이 합의해야 했다.

이 표현은 Satoshi Nakamoto의 2008년 백서가 Bitcoin 프로토콜 변경 거버넌스 또는 업그레이드 의사결정 절차를 규정한 것처럼 읽힐 수 있다.

원 백서는 거래 검증, proof-of-work chain, 네트워크 동작을 설명하지만 이후의 프로토콜 변경 절차를 정식으로 설계하지 않는다. 새로운 기능·프로세스 제안과 community input을 기록하는 BIP 체계는 이후 별도로 정착했고, Bitcoin Core 역시 개발자가 consensus rules를 일방적으로 결정하지 않으며 사용자가 어떤 소프트웨어를 실행할지 선택한다고 설명했다.

### Evidence
- Satoshi Nakamoto, `Bitcoin: A Peer-to-Peer Electronic Cash System`: https://bitcoin.org/bitcoin.pdf
- BIP 1, `BIP Purpose and Guidelines`: https://bitcoin.org/bip/1/
- Bitcoin Core statement, 2016-01-07: https://bitcoin.org/en/bitcoin-core/2016-01-07-statement
- Repository canon: `09_RESEARCH/V2_FACT_LEDGER.md`, V2-F021~F023

### Fix
거버넌스를 백서에 귀속하지 않고 다음 흐름으로 최소 수정했다.

> 그 질문은 백서가 답해주지 않았다.
> 누군가가 새 규칙을 제안할 수는 있었다.
> 하지만 다른 사람들이 받아들이지 않으면 네트워크의 규칙이 되지 않았다.

New York Agreement, Bitcoin Cash, SegWit의 날짜·순서는 기존 V2-F021~F023과 일치하므로 다른 역사 서술은 건드리지 않았다.

## Regression check
- CH09 → CH10: Ethereum/Classic의 포크 경험이 Bitcoin/BCH 분열의 비교 장치로 이어지는 흐름 유지.
- CH10 → CH11: 블록 크기 전쟁에서 ICO 열풍으로 이동하는 마지막 장면과 CH11의 `2017년 여름` 진입이 유지됨.
- 의인화 대사는 C2 창작으로 남기되 실제 인물의 사적 심리나 발언을 새로 만들지 않음.

## Review queue
CH10 manuscript blob SHA changed from `bf9dc348bcd7d349bc41eb168b5f7b615d326f9e` to `999e55838aae7d4639046b1c2442616b0722ad4b`; `11_REVIEW/QUEUE.md` fingerprint updated. CH09 and CH10 remain `pending` because the required independent roles have not submitted reviews.
