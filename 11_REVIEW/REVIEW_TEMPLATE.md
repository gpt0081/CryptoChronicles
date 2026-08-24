# Review Report Template

> 파일명 권장: `<volume>_<chapter>__<role>.md`
> 예: `V4_CH12__historian.md`

## Metadata

- role: historian | continuity | character | novel-editor | blind-reader | red-team
- target: 원고 파일 경로
- manuscript_commit: 검수 기준 커밋 SHA
- manuscript_blob_sha: 검수한 대상 원고 파일의 blob SHA
- reviewer_model: 사용 모델 또는 도구 이름
- reviewed_at: YYYY-MM-DD
- scope: 검수 범위

## Findings

각 항목은 아래 형식을 반복한다.

### FINDING-001

- severity: CRITICAL | MAJOR | MINOR | NOTE
- location: 문단, 장면, 인용 가능한 짧은 식별 문구
- category: chronology | fact | continuity | character | motivation | pacing | exposition | clarity | bias | other
- status: OPEN
- confidence: high | medium | low

**문제**

무엇이 잘못되었거나 위험한지 설명한다.

**근거**

왜 문제라고 판단했는지 설명한다. 역사·기술 검수라면 근거 자료나 확인 경로를 남긴다.

**수정 방향**

직접 원고를 다시 쓰지 말고, 최소 수정 방향만 제안한다.

**연관 항목**

다른 장 또는 다른 finding과 연결되는 경우 기록한다.

---

## No-Finding 선언

문제가 없다고 판단한 경우에도 빈 파일을 만들지 말고 아래를 명시한다.

- result: NO_FINDINGS
- checked: 실제로 확인한 범위
- residual_risk: 검수하지 못했거나 확신이 낮은 부분

## 유효성 규칙

- `manuscript_commit`은 `11_REVIEW/BASELINE.md`의 active baseline 이상이어야 한다.
- `manuscript_blob_sha`는 실제 검수한 원고 파일 blob SHA와 일치해야 한다.
- 원고 수정으로 blob SHA가 바뀌면 기존 보고서는 stale이며, 해당 역할 검수를 다시 수행해야 한다.

## 금지 사항

- 원고 파일 직접 수정
- 다른 검수자의 결론을 복사해 독립 검수처럼 제출
- 위치나 근거 없는 막연한 취향 평가
- 전체 문단 재작성 제안
- 사실 확인이 필요한 내용을 사실인 것처럼 단정
