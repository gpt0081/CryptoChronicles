# Pass 5 Active Review Baseline

Pass 5 외부 검수는 아래 기준점을 현재 정본 출발점으로 사용한다.

- active baseline branch: `main`
- active baseline commit: `bcf6f765870aadaaa06a3959d2bccd3fbddf3237`
- baseline established after: PR #45 (`Final art: replace legacy portraits with canonical character SVG set`)
- manuscript state at baseline: 4부 48장 완료, Pass 1~4 완료, 내부 Pass 5 사전감사 48/48 완료, Copyedit Audit 기준 Hard 0 / Soft 0, 최종 캐릭터 아트 main 반영
- baseline purpose: 독립 Pass 5가 내부 사전감사 및 그 과정의 모든 원고 수정이 끝난 뒤의 최신 정본에서 시작하도록 고정

## 사용 규칙

1. 외부 검수자는 가능하면 이 active baseline commit을 checkout한 뒤 검수한다. 이후 `main` commit을 사용한다면 보고서의 `manuscript_commit`과 대상 파일 `manuscript_blob_sha`를 반드시 기록한다.
2. `11_REVIEW/QUEUE.md`의 48개 `Last manuscript blob SHA`가 장별 검수 지문이다. 외부 보고서의 `manuscript_blob_sha`와 해당 큐 행이 다르면 stale review로 처리한다.
3. 원고 수정이 발생하면 수정된 장의 queue blob SHA를 즉시 갱신하고, 그 장에 대해 수정 전 blob을 읽은 보고서는 완료 근거에서 제외한다.
4. 기존 review 보고서는 stale이 되어도 삭제하지 않는다. historical evidence로 보존한다.
5. 새 전권 기준점이 필요할 때만 active baseline commit을 갱신한다. 개별 장 수정의 최신성 판정은 queue blob SHA를 우선한다.
6. `pending`은 독립 검수가 아직 완료되지 않았다는 상태값이며 SHA 부재를 뜻하지 않는다. 현재 모든 48개 pending 행에는 기준 manuscript blob SHA가 채워져 있다.

## 기준점과 장별 SHA를 둘 다 쓰는 이유

commit SHA는 전권이 어느 시점의 정본인지 고정한다. blob SHA는 실제로 검수한 장이 현재 장과 같은 내용인지 판별한다. 둘을 함께 사용하면 다른 장이나 캐릭터 아트·문서만 변경된 경우 불필요하게 모든 review를 폐기하지 않으면서도, 원고가 바뀐 장의 오래된 review는 확실히 걸러낼 수 있다.

이 기준점은 독립 검수 결과가 들어오기 전의 최종 내부 정리 상태다. 독립 reviewer 결과 없이 queue를 `reviewed`로 올리거나 publication-ready로 선언해서는 안 된다.
