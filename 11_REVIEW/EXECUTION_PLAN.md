# Pass 5 Independent Review Execution Plan

이 문서는 이미 완료된 내부 사전감사를 반복하지 않고, 남은 48장 독립 검수를 실제로 실행하기 위한 운영 순서를 정의한다.

## 목표

- 대상: `11_REVIEW/QUEUE.md`의 48장
- 기본 깊이: 장당 서로 다른 2개 역할
- 총 기본 review 슬롯: 96
- 외부 reviewer는 원고를 수정하지 않는다.
- 결과는 `11_REVIEW/inbox/<role>/`에 보고서로 제출한다.
- 보고서의 `manuscript_blob_sha`는 반드시 해당 queue 행의 SHA와 일치해야 한다.

## 역할별 기본 물량

Queue의 현재 배정을 그대로 집계하면 다음과 같다.

| Role | Assigned chapter reviews | Dispatch issue |
|---|---:|---|
| historian | 20 | #48 |
| continuity | 20 | #49 |
| character | 16 | #51 |
| novel-editor | 16 | #52 |
| blind-reader | 12 | #53 |
| red-team | 12 | #54 |
| **Total** | **96** | **96/96 dispatched** |

## 실행 순서

### Wave 1 — 역사 + 연속성

실행 계약: historian issue #48, continuity issue #49.

`historian`과 `continuity`가 자신에게 배정된 queue 행만 독립적으로 검수한다.

목적:
- 날짜·순서·기술·법률 사실 오류
- 후대 사실을 과거 인물이 미리 아는 문제
- 인과관계 과장
- 장 사이 상태·관계·사건 연결 충돌

두 역할은 서로의 보고서를 보기 전에 제출한다.

### Wave 2 — 캐릭터 + 소설성

실행 계약: character issue #51, novel-editor issue #52.

`character`와 `novel-editor`가 자신에게 배정된 queue 행만 검수한다.

목적:
- dossier/canon과 행동·대사 불일치
- 의인화 인물과 실제 인간의 혼동
- 연구·설명·교과서 목소리가 소설 본문을 침범한 구간
- 장면보다 요약·설명이 앞서는 구간
- 반복되는 대사·모티프·캐릭터 기능 충돌

### Wave 3 — 초독자 + Red Team

실행 계약: blind-reader issue #53, red-team issue #54.

`blind-reader`는 설정·Fact Ledger·내부 precheck를 읽지 않고 해당 장과 필요 최소한의 인접 원고만 읽는다.

`red-team`은 다른 reviewer 결과를 보기 전에 독립 제출한다.

목적:
- 설정을 모르는 독자가 이해하지 못하는 장면
- 작가가 당연하다고 가정한 비약
- 과장·오해·법적/역사적 오독 가능성
- 작품 전체의 신뢰도를 무너뜨릴 수 있는 반례

## 제출 파일 규칙

각 보고서는 `REVIEW_TEMPLATE.md`를 따르고 최소한 아래를 포함한다.

- role
- volume / chapter
- manuscript_commit
- manuscript_blob_sha
- verdict
- severity
- finding 위치
- 근거
- 권장 조치

권장 파일명:

`V<volume>_CH<chapter>_<role>_<blob-short-sha>.md`

예: `V1_CH01_historian_82188d40.md`

## Queue 상태 전이

1. 첫 유효 외부 보고서가 들어오면 `pending → reviewing`
2. 필요한 두 역할의 최신 보고서가 모두 들어오면:
   - CRITICAL/MAJOR 없음: 판정 기록 후 `reviewed` 후보
   - CRITICAL/MAJOR 존재: `decision`
3. finding 채택 후 본문 수정 필요: `revising`
4. 수정 후 새 blob SHA로 queue 갱신
5. 수정 장 + 앞뒤 한 장 회귀검수
6. 최신 원고 기준의 필수 reviewer 증거가 충족되면 `reviewed`

## 자동 폐기 조건

다음 보고서는 완료 근거로 사용할 수 없다.

- queue의 현재 blob SHA와 다른 원고를 읽은 보고서
- 역할·장·SHA가 없는 보고서
- 내부 precheck를 독립 review라고 이름만 바꾼 보고서
- 다른 reviewer의 결론을 그대로 재진술한 보고서
- 근거 없이 `OK`만 적은 보고서

stale/invalid 보고서는 삭제하지 않고 기록으로 보존한다.

## 수정 원칙

독립 finding이 들어와도 즉시 원고를 뜯어고치지 않는다.

- CRITICAL: 사실·연속성·법률·인물 정체성에 중대한 오류. 우선 수정 검토.
- MAJOR: 장의 의미·인과·캐릭터·독해를 크게 왜곡. 수정 검토.
- MINOR: 정확성이나 문학성을 개선하지만 publication blocker는 아님.
- NOTE: 취향·대안·관찰. 자동 수정하지 않음.

채택된 finding만 최소 범위로 수정하며, 연구 설명문을 본문에 새로 삽입하는 방식으로 해결하지 않는다.

## 완료 게이트

독립 Pass 5를 끝났다고 선언하려면 다음을 모두 만족해야 한다.

1. Queue 48/48 `reviewed`
2. 각 장에 현재 blob SHA 기준 최소 2개 유효 독립 역할 보고서 존재
3. 모든 CRITICAL/MAJOR finding에 decision 기록 존재
4. 채택된 수정의 인접 장 회귀검수 완료
5. 최종 Copyedit Audit Hard 0 / Soft 0 또는 명시적 intentional exception만 존재
6. 열린 draft PR 및 미완성 manuscript 작업 없음
7. README 상태가 실제 GitHub 상태와 일치

이 문서는 검수 결과를 대신하지 않는다. 역할은 단 하나다. 현재의 0/48 상태를 실제 48/48로 전진시키기 위한 실행 계약을 고정하는 것이다.
