# OpenCode Integration Boundary

이 저장소는 OpenCode의 모델·에이전트 정의 자체를 관리하지 않는다. OpenCode 쪽 구성은 사용자가 별도로 운영하고, GitHub에서는 입력/출력 계약만 고정한다.

외부 시스템이 지켜야 할 것은 두 가지다.

1. 원고를 수정하지 말 것
2. 결과를 `11_REVIEW/inbox/<role>/` 형식으로 제출할 것

이렇게 분리하면 OpenCode 모델이나 제공자가 바뀌어도 저장소의 편집 루프는 영향을 받지 않는다.
