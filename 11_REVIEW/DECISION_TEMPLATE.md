# Review Decision Template

> 파일명 권장: `<volume>_<chapter>__decision.md`

## Metadata

- target: 원고 파일 경로
- manuscript_commit: 검토 기준 SHA
- decided_at: YYYY-MM-DD
- editor: 최종 판단 주체

## Decision Ledger

### DECISION-001

- source: 원본 review 파일 + finding ID
- verdict: ACCEPTED | REJECTED | DUPLICATE | DEFERRED
- severity: CRITICAL | MAJOR | MINOR | NOTE
- reason: 판정 이유
- affected_files: 수정 시 영향받을 가능성이 있는 원고 파일
- regression_scope: 재검수할 장 범위
- fix_commit: 수정 전에는 비워 둔다
- final_status: OPEN | FIXED

## 충돌 처리

검수자 간 의견이 충돌하면 다수결로 결정하지 않는다. 아래 순서로 판정한다.

1. 원문에서 실제 위치와 맥락 확인
2. 사실 문제는 1차 자료 또는 신뢰할 수 있는 근거 우선
3. 연속성 문제는 기존 timeline/character state 우선
4. 소설성 문제는 작품의 의도와 독자 이해 비용을 함께 비교
5. 확정 불가능하면 `DEFERRED`로 남기고 이유 기록

## 수정 원칙

- 가장 작은 수정으로 문제를 해결한다.
- 한 finding을 고치면서 새 설정을 추가하지 않는다.
- 역사적 정확성을 높이기 위해 장면의 긴장이나 인물 동기를 무너뜨리지 않는다.
- 수정 후 `regression_scope`를 반드시 다시 읽는다.
