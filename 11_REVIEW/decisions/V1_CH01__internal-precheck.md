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
- fix_commit: `dda3ac31a0f7fbd053f1c72b29106c3e57f7a952`
- final_status: RESOLVED

## Applied fix

- `Bitcoin이 존재하지 않았다`는 표현을 `아직 세상 앞에 모습을 드러내지 않았다`로 낮췄다.
- `이름도 없었다`처럼 비공개 명명 상태를 단정하는 문장을 제거했다.
- Satoshi의 집필 상태를 꾸며내던 컴퓨터·빈 화면 장면을 제거했다.
- `리먼이 떠난 자리`를 제거해 Lehman → Bitcoin 직접 인과로 읽힐 가능성을 낮췄다.
- 질문의 주제적 연결은 유지하되 역사적 원인 주장으로 확정하지 않았다.

## Regression result

- V1 CH01: 수정 구간 전후의 신용/연준/규칙 모티프가 유지됨.
- V1 CH02: 2008-10-31 `Bitcoin P2P e-cash paper` 메일 장면과 시간순서 및 공개 시점이 자연스럽게 이어짐.
- Copyedit Audit run #17: 48 chapter files / hard issues 0 / soft warnings 0.

## Independence note

이 결정은 내부 사전감사 처리이며, Pass 5의 독립 `historian`·`continuity` 제출을 완료 처리하지 않는다. V1 CH01은 외부 두 역할의 제출이 들어오기 전까지 `11_REVIEW/QUEUE.md`에서 pending 상태를 유지한다.
