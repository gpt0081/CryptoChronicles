# Pass 5 Precheck — V4 CH07~CH08

## 범위
- `07_VOLUME_4/CH07_현실_자산의_토큰화.md`
- `07_VOLUME_4/CH08_국가와_체인의_협상.md`

이 문서는 내부 사전감사 기록이다. `11_REVIEW/QUEUE.md`의 독립 역할 검수를 대체하지 않는다.

## CH07 — 현실 자산의 토큰화

### 판정
- 새 역사 blocker 없음.
- 본문 수정 없음.

### 확인 사항
- BUIDL을 토큰화된 펀드의 상징으로 사용하되, 토큰 자체가 모든 법적 권리를 창조한다고 쓰지 않는다.
- permissioned 이전, KYC, 발행자·수탁·법적 청구권을 온체인 토큰과 분리한다.
- RWA를 '현실 자산 자체가 체인 안으로 이동한다'고 오해시키지 않고, 현실의 권리관계를 코드가 읽을 수 있는 형태로 표현하는 구조로 설명한다.
- Stablecoins·Institutions·Chainlink가 RWA와 상호작용하는 장면은 각 캐릭터 dossier의 역할과 충돌하지 않는다.
- 기술 설명이 다소 많은 장이지만, 대화와 공간 이미지 안에서 작동하며 추가 재작성의 이득보다 manuscript churn 위험이 더 크다고 판단했다.

## CH08 — 국가와 체인의 협상

### 판정
- 새 역사 blocker 없음.
- 본문 수정 없음.

### 1차 자료 대조
- U.S. Treasury는 2025-03-21 Tornado Cash에 대한 경제제재 제거를 공식 발표했다. 동시에 DPRK 및 악성 사이버 행위자의 디지털자산 악용 우려와 제재 집행 의지는 유지했다.
- White House의 2025-03-06 행정명령은 Strategic Bitcoin Reserve를 설치하고, 최종 몰수 등으로 정부가 보유한 BTC를 reserve 자산으로 관리하도록 했다. Reserve에 편입된 Government BTC는 원칙적으로 매각하지 않도록 규정한다.

### 서술 경계 확인
- `국가`를 단일 정치적 의지로 쓰지 않고 기관·법원·행정부가 충돌할 수 있는 복합 행위자로 유지한다.
- Tornado Cash 제재 제거를 '정부가 프라이버시 도구를 승인했다'는 식으로 확대하지 않는다.
- Strategic Bitcoin Reserve를 Bitcoin 프로토콜 자체에 대한 국가 승인으로 쓰지 않는다.
- 중앙 발행 스테이블코인과 Bitcoin의 검열·피해구제 차이는 절대적 우열이 아니라 상충하는 위험으로 묘사한다.

## 연속성 회귀검수
- CH06의 L2 확장과 permissionless/permissioned 경계가 CH07의 RWA 금융구역으로 자연스럽게 이어진다.
- CH07의 법적 청구권·KYC·발행자 권한이 CH08의 국가·법집행·제재 논쟁으로 연결된다.
- CH08의 협상 프레임은 CH09 이후 자유·책임·제도권 공존에 대한 결말부 논의와 충돌하지 않는다.

## 결론
CH07~CH08은 현재 `main` 원고를 유지한다. 독립 Pass 5 reviewer가 이후 MAJOR/CRITICAL finding을 제출하면 별도 decision 절차를 거친다.
