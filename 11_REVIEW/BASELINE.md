# Pass 5 Active Review Baseline

Pass 5 외부 검수는 반드시 아래 기준점 이상의 원고를 대상으로 한다.

- active baseline branch: `main`
- active baseline commit: `6d28f94de2618ca4b8339e68e902c4be0e192c80`
- baseline established after: PR #20 (`Pass 5 precheck: resolve V1 CH02 mailing-list scope`)
- baseline purpose: CH01~CH03 내부 역사 사전수정까지 반영된 상태를 외부 검수의 최소 기준으로 고정

## 사용 규칙

1. 외부 검수자는 실행 시작 시 `main`이 이 baseline보다 뒤에 있는지 확인한다.
2. 실제 보고서에는 검수한 `manuscript_commit`과 대상 파일의 `manuscript_blob_sha`를 모두 기록한다.
3. 이후 원고가 수정되더라도 baseline 기록은 삭제하지 않는다. 새 기준점이 필요할 때 이 파일의 active baseline을 갱신하고 변경 이유를 남긴다.
4. 보고서의 blob SHA가 현재 대상 장과 다르면 해당 보고서는 historical evidence로만 보존하고 완료 판정에는 사용하지 않는다.
5. `11_REVIEW/QUEUE.md`의 `Last manuscript SHA`는 해당 장이 실제 `reviewing` 상태로 들어갈 때 검수 대상 blob SHA로 채운다. 아직 `pending`인 장의 `-` 표시는 미검수 상태를 뜻하며 오류가 아니다.

## 왜 필요한가

Pass 5는 여러 외부 모델과 여러 회차에 걸쳐 진행된다. commit SHA만 기록하면 같은 commit 아래 어떤 파일을 실제로 읽었는지 검증하기 어렵고, 원고 수정 후 오래된 검수 결과가 최신 결과처럼 섞일 수 있다. commit + blob SHA를 함께 고정해 이 문제를 차단한다.
