# Pass 5 Status

- phase: independent-review-all-waves-dispatched
- active_branch: main
- manuscript_baseline_commit: `bcf6f765870aadaaa06a3959d2bccd3fbddf3237`
- current_main_commit_at_status_refresh: `5174c332c4e88ce6ddd92db09b2b2a7e288bac18`
- manuscript_state: 4 volumes / 48 chapters complete; Pass 1-4 merged; internal Pass 5 precheck 48/48 complete
- copyedit: 48 chapters / hard 0 / soft 0
- character_art: 6/6 canonical SVG portraits merged to main
- queue: 48 chapters pending independent review
- external_reports_received: 0
- default_review_depth: 2 independent roles per chapter
- total_required_independent_slots: 96
- dispatched_independent_slots: 96
- escalation: adaptive by severity/conflict
- manuscript_editing_by_external_agents: forbidden
- open_pull_requests_at_refresh: 0
- wave1_historian_dispatch: GitHub issue #48 — 20 assigned chapter reviews
- wave1_continuity_dispatch: GitHub issue #49 — 20 assigned chapter reviews
- wave2_character_dispatch: GitHub issue #51 — 16 assigned chapter reviews
- wave2_novel_editor_dispatch: GitHub issue #52 — 16 assigned chapter reviews
- wave3_blind_reader_dispatch: GitHub issue #53 — 12 assigned chapter reviews
- wave3_red_team_dispatch: GitHub issue #54 — 12 assigned chapter reviews

`BASELINE.md`와 각 장의 `QUEUE.md` blob SHA를 검수 버전의 정본으로 사용한다. 내부 사전감사는 독립 검수로 간주하지 않는다.

이제 기본 독립 검수 96개 슬롯 전체가 실제 GitHub issue로 dispatch됐다. Wave 1은 historian/continuity, Wave 2는 character/novel-editor, Wave 3는 blind-reader/red-team이다. 각 역할 issue의 완료 조건은 배정된 모든 유효 보고서가 `11_REVIEW/inbox/<role>/`에 제출되는 것이다.

보고서가 실제로 들어오기 전에는 queue 상태를 임의로 `reviewing` 또는 `reviewed`로 올리지 않는다. 첫 유효 보고서가 들어온 장만 `reviewing`으로 전이하며, 두 필수 역할의 최신 SHA 보고서와 finding 판정이 갖춰진 뒤에만 `reviewed` 후보가 된다.

상세 진행률은 `QUEUE.md`, 외부 제출 계약은 `AGENT_HANDOFF.md`, 실행 순서와 역할별 issue 매핑은 `EXECUTION_PLAN.md`를 기준으로 한다.
