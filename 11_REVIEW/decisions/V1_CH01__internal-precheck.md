# V1 CH01 Internal Precheck Decision

## Metadata

- target: `04_VOLUME_1/CH01_신뢰가_멈춘_날.md`
- manuscript_commit: `5f20e2b12805e5e14db4b95e86a9bf4edd841430`
- decided_at: 2026-08-24
- editor: ChatGPT editorial loop

## Decision Ledger

### DECISION-001

- source: `11_REVIEW/internal/V1_CH01__historical-precheck.md` / FINDING-001
- verdict: ACCEPTED
- severity: MAJOR
- reason: 공개 시점 이전이라는 사실은 서사적으로 사용할 수 있지만, 2008-09-15 당시 Satoshi의 비공개 작문 상태와 Bitcoin 명칭 존재 여부를 단정할 근거는 없다. 작품 자체의 `01_HISTORY/2008-2012.md`도 금융위기와 Bitcoin 탄생의 직접 인과 단정을 경계한다. 마지막 장면의 예고 기능을 유지하면서 불확정 사실만 제거하는 것이 가장 작은 수정이다.
- affected_files: `04_VOLUME_1/CH01_신뢰가_멈춘_날.md`
- regression_scope: V1 CH01, V1 CH02
- fix_commit:
- final_status: OPEN

## Intended minimal fix

- `Bitcoin이 존재하지 않았다`는 표현을 `아직 세상에 모습을 드러내지 않았다` 수준으로 낮춘다.
- `이름도 없었다`처럼 비공개 명명 상태를 단정하는 문장을 제거한다.
- `아직 아무 문장도 쓰이지 않았다`를 Satoshi의 집필 상태를 단정하지 않는 문장으로 바꾼다.
- Lehman → Bitcoin 직접 인과가 역사적 사실처럼 읽히지 않도록 현재의 C2(서사적 질문) 성격을 유지한다.

## Independence note

이 결정은 내부 사전감사 처리이며, Pass 5의 독립 `historian`·`continuity` 제출을 완료 처리하지 않는다.
