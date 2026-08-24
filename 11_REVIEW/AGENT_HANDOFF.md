# External Agent Handoff Contract

OpenCode 또는 다른 외부 검수 시스템은 이 문서를 인터페이스 계약으로 사용한다.

## 입력

필수:

- 대상 원고 파일 1개
- 역할 1개
- 검수 기준 commit SHA
- 대상 원고 파일의 blob SHA

선택:

- 역할별 허용 참고 자료
- 인접 장 1~2개

## 출력

- `11_REVIEW/REVIEW_TEMPLATE.md` 형식의 Markdown 1개
- 위치: `11_REVIEW/inbox/<role>/<volume>_<chapter>__<role>.md`

## 절대 규칙

1. 원고 파일을 수정하지 않는다.
2. 한 실행은 한 역할만 수행한다.
3. 다른 역할의 review 파일을 읽지 않는다.
4. findings가 없어도 NO_FINDINGS 보고서를 남긴다.
5. 검수 기준 commit SHA와 대상 원고 blob SHA를 반드시 기록한다.
6. 근거 없는 단정 대신 confidence를 낮춘다.
7. `11_REVIEW/BASELINE.md`의 active baseline보다 오래된 commit을 기준으로 작성한 보고서는 자동 채택하지 않는다.
8. 보고서의 `manuscript_blob_sha`가 현재 검수 대상 파일과 다르면 stale review로 처리하고 재검수한다.

## 편집 루프가 기대하는 최소 필드

- role
- target
- manuscript_commit
- manuscript_blob_sha
- reviewer_model
- reviewed_at
- severity
- location
- category
- status
- confidence
- 문제
- 근거
- 수정 방향

## stale review 처리

원고가 검수 뒤 수정되면 기존 보고서를 삭제하지 않는다. 대신 해당 보고서를 근거 기록으로 보존하고 큐 상태를 다시 `reviewing`으로 되돌린다. 같은 역할의 새 보고서는 새 commit/blob SHA를 기록해 제출한다.

이 계약만 지키면 외부 모델 종류나 실행 방식은 교체 가능하다.
