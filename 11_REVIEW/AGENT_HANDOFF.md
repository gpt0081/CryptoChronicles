# External Agent Handoff Contract

OpenCode 또는 다른 외부 검수 시스템은 이 문서를 인터페이스 계약으로 사용한다.

## 입력

필수:

- 대상 원고 파일 1개
- 역할 1개
- 검수 기준 commit SHA

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
5. 검수 기준 commit SHA를 반드시 기록한다.
6. 근거 없는 단정 대신 confidence를 낮춘다.

## 편집 루프가 기대하는 최소 필드

- role
- target
- manuscript_commit
- severity
- location
- category
- status
- confidence
- 문제
- 근거
- 수정 방향

이 계약만 지키면 외부 모델 종류나 실행 방식은 교체 가능하다.
