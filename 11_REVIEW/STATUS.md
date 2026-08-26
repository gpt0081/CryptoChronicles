# Pass 5 Status

- phase: independent-review-wave1-dispatched
- active_branch: main
- manuscript_baseline_commit: `bcf6f765870aadaaa06a3959d2bccd3fbddf3237`
- current_main_commit_at_status_refresh: `8f24cd2675ec895049718005cb26bee46269e155`
- manuscript_state: 4 volumes / 48 chapters complete; Pass 1-4 merged; internal Pass 5 precheck 48/48 complete
- copyedit: 48 chapters / hard 0 / soft 0
- character_art: 6/6 canonical SVG portraits merged to main
- queue: 48 chapters pending independent review
- external_reports_received: 0
- default_review_depth: 2 independent roles per chapter
- escalation: adaptive by severity/conflict
- manuscript_editing_by_external_agents: forbidden
- open_pull_requests_at_refresh: 0
- wave1_historian_dispatch: GitHub issue #48 — 20 assigned chapter reviews
- wave1_continuity_dispatch: GitHub issue #49 — 20 assigned chapter reviews

`BASELINE.md`와 각 장의 `QUEUE.md` blob SHA를 검수 버전의 정본으로 사용한다. 내부 사전감사는 독립 검수로 간주하지 않는다.

Wave 1은 문서상 계획 상태를 넘어 실제 GitHub 작업 단위로 dispatch됐다. `historian`은 issue #48, `continuity`는 issue #49를 실행 계약으로 사용하며, 각 issue의 완료 조건은 해당 역할의 유효 보고서 20개가 `11_REVIEW/inbox/<role>/`에 제출되는 것이다. 보고서가 들어오기 전에는 queue 상태를 임의로 `reviewing` 또는 `reviewed`로 올리지 않는다.

상세 진행률은 `QUEUE.md`, 외부 제출 계약은 `AGENT_HANDOFF.md`, 실행 순서는 `EXECUTION_PLAN.md`를 기준으로 한다.
