# Pass 5 Fact Ledger Coverage Audit

## 목적

최종 원고 48장과 `09_RESEARCH/`의 권별 Fact Ledger / Fact Check를 다시 대조해, publication-readiness 조건 중 사실검증 커버리지와 남은 조사 부채를 구분한다.

## 결론

- V1: 12/12장에 관련 Fact 또는 chapter-level fact check가 존재한다.
- V2: 12/12장에 관련 Fact가 존재하며 `V2_FACT_LEDGER.md`의 핵심 사건은 모두 VERIFIED다.
- V3: 12/12장에 관련 Fact가 존재하며 `V3_FACT_LEDGER.md`의 핵심 사건은 모두 VERIFIED다.
- V4: C01~C08, C11~C12는 `V4_FACT_LEDGER.md`에 직접 연결된 검증 항목이 있다. C09 `자유의 가격`과 C10 `탈중앙화의 역설`은 새로운 날짜·가격·법률 사건을 전개하는 장이 아니라, 앞 장들에서 이미 검증된 ETF·스테이블코인·L2·PoS·채굴풀·수탁 구조를 철학적/구조적으로 재조합하는 장이다. 두 장에서 별도 신규 사실 ID가 필요한 독립 사건은 확인되지 않았다.

## 상위 FACT_LEDGER의 오래된 상태값

`09_RESEARCH/FACT_LEDGER.md`의 초기 통합표에는 F-0005(The DAO), F-0006(FTX), F-0007(spot Bitcoin ETF)가 UNVERIFIED로 남아 있다. 이는 이후 권별 ledger가 만들어지기 전의 오래된 상태다.

최신 권별 정본에서는 다음과 같이 이미 검증됐다.

- F-0005 → V2-F015~V2-F020: The DAO 공격, soft-fork 취약점, 2016-07-20 hard fork, ETC 존속까지 VERIFIED.
- F-0006 → V3-F23~V3-F26: FTX 유동성 위기, Binance 비구속 LOI, 2022-11-11 Chapter 11, 후대 형사재판 결과까지 VERIFIED.
- F-0007 → V4-F07~V4-F10: 2024-01-10 spot Bitcoin ETP 승인과 2024-01-11 거래 개시, spot Ether ETP 승인/개시까지 VERIFIED.

따라서 publication 판단에서는 권별 ledger가 최신 source of truth이며, 통합표의 세 UNVERIFIED 행은 미해결 사실 문제가 아니라 stale summary entry로 취급한다. 이후 통합표를 재정규화할 때 권별 ID를 직접 참조하도록 정리하면 된다.

## 남은 비차단 조사 부채

V1 `FACT_CHECK.md`에 두 caveat가 남아 있다.

1. F-0026 Bitcoin Market의 2010-03-17 초기 시장 시작점은 동시대 원자료 보강 여지가 있다.
2. F-0031 Avalon ASIC의 2013년 초 등장에 대해 `세계 최초` 같은 절대 표현 범위는 추가 검증 여지가 있다.

현재 원고는 두 항목 모두 절대적 단정을 피하고 있어 역사적 hard error로 보지 않는다. 외부 historian review에서 반대 근거가 나오면 재개한다.

## 원고 영향

이번 감사에서 새로 발견된 원고 사실 오류는 없다. 원고 수정 없음.

## Publication-readiness 영향

- `Fact Ledger·최종 본문 대조` 조건은 내부 감사 기준으로 완료.
- 이 감사는 Pass 5의 독립 historian/continuity/character/novel-editor/blind-reader/red-team 검수를 대체하지 않는다.
- 최종 publication-ready 선언은 48장 독립 review queue 완료 후 가능하다.
