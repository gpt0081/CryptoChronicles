# V1 CH01 Historical Precheck

## Metadata

- role: internal historical precheck
- target: `04_VOLUME_1/CH01_신뢰가_멈춘_날.md`
- manuscript_commit: `5f20e2b12805e5e14db4b95e86a9bf4edd841430`
- reviewer_model: ChatGPT
- reviewed_at: 2026-08-24
- scope: V1 CH01 역사 사건·시간순서·서사적 인과 단정 여부. 이 파일은 OpenCode 독립 검수를 대체하지 않으며 Pass 5 required-role 완료로 계산하지 않는다.

## Findings

### FINDING-001

- severity: MAJOR
- location: 마지막 장면, `그때 비트코인은 아직 존재하지 않았다`부터 `아직 아무 문장도 쓰이지 않았다`까지
- category: chronology / fact
- status: OPEN
- confidence: high

**문제**

2008년 9월 15일 시점에 Bitcoin 네트워크와 공개 백서는 아직 등장하지 않았다는 서사 방향은 맞지만, `이름도 없었다`와 특히 `아직 아무 문장도 쓰이지 않았다`는 표현은 Satoshi가 그 날짜에 백서 초안을 어느 단계까지 작성했는지 알 수 없는데도 내부 작성 상태를 단정한다. 또한 금융위기 장면 바로 뒤에 이 문장을 두면 Lehman 파산이 Bitcoin 설계의 직접 계기였다는 역사적 인과로 오독될 가능성이 있다.

**근거**

- Lehman Brothers Holdings Inc.는 2008-09-15 Chapter 11을 신청했다. SEC 8-K 및 SEC 보도자료로 확인 가능.
- Federal Reserve Board는 2008-09-16 New York Fed가 AIG에 최대 850억 달러의 secured revolving credit facility를 제공하도록 승인했다.
- 반면 2008-09-15에 Bitcoin 백서가 아직 작성되지 않았다고 입증하는 1차 자료는 없다. 따라서 Satoshi의 비공개 집필 상태를 소설의 역사적 사실처럼 확정하면 안 된다.

**수정 방향**

Bitcoin이 아직 `공개되지 않았다`는 사실만 남기고, 이름의 존재 여부나 백서 문장이 쓰였는지 여부는 단정하지 않는다. 마지막 컴퓨터 장면의 긴장과 예고 기능은 유지한다.

**연관 항목**

- `01_HISTORY/2008-2012.md`: 금융위기와 Bitcoin 탄생을 직접 인과로 단정할 수 있는 범위를 조사 대상으로 명시.
- `08_CONTINUITY/EVENT_LEDGER.md` S-0003: 중심 질문의 형성은 C2(서사적 구성)로 관리.

## Verified facts

- Lehman filing date: 2008-09-15 — verified against SEC filing.
- AIG emergency facility authorization: 2008-09-16, up to $85B — verified against Federal Reserve Board.
- Chapter sequence (`2008-09-15` → `다음 날` AIG): consistent.

## Pass 5 note

이 검수는 내부 사전감사다. `historian` 및 `continuity` 독립 제출은 여전히 필요하다.
