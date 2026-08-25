# CryptoChronicles

암호화폐의 실제 역사를 바탕으로, 네트워크·자산·기업·제도를 개성과 욕망을 지닌 행위자로 의인화해 재구성하는 4부작 장편소설 프로젝트.

## 현재 상태

**4부 48장 전체 원고 완료. Pass 1~4 완료 및 main 병합. Pass 5 내용 검수 진행 단계.**

- 제1부 `Genesis` — 12/12장 완료·검증
- 제2부 `The Programmable City` — 12/12장 완료·검증
- 제3부 `The Age of Leverage` — 12/12장 완료·검증
- 제4부 `The Return of Empire` — 12/12장 완료·검증
- 본문 역사 기준일: **2026-08-21**
- 최종 Copyedit Audit: **48장 / Hard issue 0 / Soft warning 0**
- Pass 5 독립 내용 검수 인프라: `11_REVIEW/`에 병합 완료
- Fact Ledger 전권 커버리지 재대조: **완료** (`10_REVISION/PASS5_FACT_LEDGER_AUDIT.md`)
- 핵심 캐릭터 dossier·portrait 링크 대조: **완료** (`10_REVISION/PASS5_CAST_AUDIT.md`)
- 최종 캐릭터 아트: **교체 진행 필요** — 현재 6개 JPG는 legacy placeholder이며 `02_CHARACTERS/CHARACTER_ART_BIBLE.md` 기준의 캐릭터 일러스트로 교체해야 함

현재 상태는 **publication candidate 이전의 narrative review 단계**다. 표면 교정과 전권 copyedit은 완료했지만, 역사·연속성·캐릭터·소설성·초독자·Red Team 관점의 Pass 5 검수와 최종 캐릭터 아트 교체가 아직 남아 있으므로 publication-ready로 선언하지 않는다.

## 핵심 원칙

- 실제 역사적 사건의 날짜·순서·결과는 검증한다.
- 실제 인물과 의인화된 코인/네트워크는 분리한다.
- 창작 대사는 실제 발언처럼 인용하지 않는다.
- 가격은 서사의 주인공이 아니라 사건의 결과로 다룬다.
- `00_MASTER/`와 `08_CONTINUITY/`를 작품의 정본(canon)으로 본다.
- 최신 시기를 다루는 제4부는 법률·행정명령·최종규칙·제안규칙·계류 법안을 구분한다.
- 외부 검수자는 원고를 직접 수정하지 않고 `11_REVIEW/`에 finding만 제출한다.
- 실제 본문 수정은 검수 finding의 채택·기각 판단 뒤에만 수행한다.
- 프로토콜/자산 초상화는 실사 인물화가 아니라 정본 캐릭터 일러스트로 제작하며 실제 창립자의 외모를 대체하지 않는다.

## 4부작 구성

1. **제1부 — Genesis**: 2008~2013, 금융위기와 비트코인의 탄생·가치 형성·첫 제도적 충돌
2. **제2부 — The Programmable City**: 2014~2017, Mt. Gox 이후 Ethereum·DAO·분열·ICO·Bitcoin scaling war
3. **제3부 — The Age of Leverage**: 2018~2022, stablecoin·DeFi·NFT·L1 경쟁·레버리지·Terra·FTX·The Merge
4. **제4부 — The Return of Empire**: 2023~2026-08-21, ETF·L2·RWA·stablecoin 법제·국가 reserve·미완성 시장구조 협상

## 집필·검증 순서

`역사 조사 → Fact Ledger → 장면 설계 → 초고 → 캐릭터 검사 → 연속성 검사 → 사실 검증 → 정본 반영 → Copyedit Audit → 독립 Narrative Review → 최종 회귀검수`

## 주요 디렉터리

- `00_MASTER/` — 작품 헌법, 정본 규칙, 전체 타임라인
- `01_HISTORY/` — 시대별 역사 배경
- `02_CHARACTERS/` — 주요 등장인물·세력 설정 및 초상화
- `03_WORLD/` — 세계관·조직·용어
- `04_VOLUME_1/` ~ `07_VOLUME_4/` — 48장 본문
- `08_CONTINUITY/` — 인물 상태, 관계, 사건·떡밥 추적
- `09_RESEARCH/` — Fact Ledger, Fact Check, 권별 조사자료
- `10_REVISION/` — Pass별 퇴고 규칙·보고서·트래커
- `11_REVIEW/` — Pass 5 독립 검수 큐·역할별 inbox·판정·회귀검수 기록

## 남은 완료 조건

1. `11_REVIEW/QUEUE.md`의 48장 Pass 5 검수 완료
2. 역사·연속성·캐릭터·소설성·초독자·Red Team finding 판정 및 필요한 수정 반영
3. 수정 장의 앞뒤 장 회귀검수 완료
4. `02_CHARACTERS/portraits/`의 6개 legacy placeholder를 `CHARACTER_ART_BIBLE.md` 기준의 최종 캐릭터 일러스트로 교체하고 갤러리 일관성 재감사
5. 최종 전권 감사에서 미해결 hard issue 및 soft warning 0 확인
6. 미완성 draft PR/작업 브랜치 정리 후 상태를 `publication-ready`로 변경
