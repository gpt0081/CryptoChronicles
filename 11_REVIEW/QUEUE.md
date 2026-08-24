# Pass 5 Review Queue

상태 값: `pending` / `reviewing` / `decision` / `revising` / `reviewed`

| Volume | Chapter | Status | Required roles | Critical | Major | Last manuscript SHA |
|---|---|---|---|---:|---:|---|
| V1 | CH01 | pending | historian, continuity | 0 | 0 | - |
| V1 | CH02 | pending | character, blind-reader | 0 | 0 | - |
| V1 | CH03 | pending | historian, novel-editor | 0 | 0 | - |
| V1 | CH04 | pending | continuity, red-team | 0 | 0 | - |
| V1 | CH05 | pending | character, novel-editor | 0 | 0 | - |
| V1 | CH06 | pending | historian, blind-reader | 0 | 0 | - |
| V1 | CH07 | pending | continuity, character | 0 | 0 | - |
| V1 | CH08 | pending | novel-editor, red-team | 0 | 0 | - |
| V1 | CH09 | pending | historian, continuity | 0 | 0 | - |
| V1 | CH10 | pending | character, blind-reader | 0 | 0 | - |
| V1 | CH11 | pending | novel-editor, red-team | 0 | 0 | - |
| V1 | CH12 | pending | historian, continuity | 0 | 0 | - |
| V2 | CH01 | pending | historian, blind-reader | 0 | 0 | - |
| V2 | CH02 | pending | continuity, character | 0 | 0 | - |
| V2 | CH03 | pending | novel-editor, red-team | 0 | 0 | - |
| V2 | CH04 | pending | historian, continuity | 0 | 0 | - |
| V2 | CH05 | pending | character, blind-reader | 0 | 0 | - |
| V2 | CH06 | pending | historian, novel-editor | 0 | 0 | - |
| V2 | CH07 | pending | continuity, red-team | 0 | 0 | - |
| V2 | CH08 | pending | character, novel-editor | 0 | 0 | - |
| V2 | CH09 | pending | historian, blind-reader | 0 | 0 | - |
| V2 | CH10 | pending | continuity, character | 0 | 0 | - |
| V2 | CH11 | pending | novel-editor, red-team | 0 | 0 | - |
| V2 | CH12 | pending | historian, continuity | 0 | 0 | - |
| V3 | CH01 | pending | historian, continuity | 0 | 0 | - |
| V3 | CH02 | pending | character, blind-reader | 0 | 0 | - |
| V3 | CH03 | pending | historian, novel-editor | 0 | 0 | - |
| V3 | CH04 | pending | continuity, red-team | 0 | 0 | - |
| V3 | CH05 | pending | character, novel-editor | 0 | 0 | - |
| V3 | CH06 | pending | historian, blind-reader | 0 | 0 | - |
| V3 | CH07 | pending | continuity, character | 0 | 0 | - |
| V3 | CH08 | pending | novel-editor, red-team | 0 | 0 | - |
| V3 | CH09 | pending | historian, continuity | 0 | 0 | - |
| V3 | CH10 | pending | character, blind-reader | 0 | 0 | - |
| V3 | CH11 | pending | novel-editor, red-team | 0 | 0 | - |
| V3 | CH12 | pending | historian, continuity | 0 | 0 | - |
| V4 | CH01 | pending | historian, blind-reader | 0 | 0 | - |
| V4 | CH02 | pending | continuity, character | 0 | 0 | - |
| V4 | CH03 | pending | novel-editor, red-team | 0 | 0 | - |
| V4 | CH04 | pending | historian, continuity | 0 | 0 | - |
| V4 | CH05 | pending | character, blind-reader | 0 | 0 | - |
| V4 | CH06 | pending | historian, novel-editor | 0 | 0 | - |
| V4 | CH07 | pending | continuity, red-team | 0 | 0 | - |
| V4 | CH08 | pending | character, novel-editor | 0 | 0 | - |
| V4 | CH09 | pending | historian, blind-reader | 0 | 0 | - |
| V4 | CH10 | pending | continuity, character | 0 | 0 | - |
| V4 | CH11 | pending | novel-editor, red-team | 0 | 0 | - |
| V4 | CH12 | pending | historian, continuity | 0 | 0 | - |

## 운영 규칙

- 한 장에 최소 2개 역할을 배정한다.
- `historian`은 역사·기술 의존도가 높은 장에 우선 배정한다.
- `blind-reader`는 설정 문서를 읽지 않는다.
- `red-team`은 다른 역할 보고서를 보기 전에 독립 제출한다.
- 동일 장에서 `CRITICAL` 또는 `MAJOR`가 나오면 자동으로 `decision` 상태로 올린다.
- 수정이 발생하면 해당 장뿐 아니라 앞뒤 한 장을 회귀 검수한다.
