# Pass 5 V1 CH11–CH12 Precheck

Status: **RESOLVED**
Scope: V1 CH11 `균열의 씨앗`, V1 CH12 `더 이상 실험이 아닌 것`
Purpose: 내부 사전감사. 독립 Pass 5 역할 검수를 대체하지 않는다.

## CH11

- 2013-03-11 Bitcoin 0.8/0.7 체인 분기, Block 225,430, 채굴 풀의 0.7 호환 체인 복귀 서술을 기존 canon/fact 자료와 대조했다.
- 이번 회차에서 새 publication blocker는 발견하지 않았다.
- ASIC·채굴 풀 설명은 다소 설명적이지만 장면의 갈등 구조와 직접 연결되어 있어 본문 수정 없이 유지한다.

## CH12 finding

Severity: **MAJOR**
Type: historical characterization / real-person interiority

기존 마지막 장면은 익명의 `젊은 설계자`가 Bitcoin을 보며 여백에 `계약은? / 조직은? / 시장은?`이라고 적었다고 묘사했다. 문맥상 Vitalik Buterin을 가리키지만, 그 정확한 사적 메모나 순간은 확인 가능한 역사 기록이 아니다.

이 장면은 Ethereum으로 넘어가는 서사적 다리는 유효하지만, 실존 인물의 확인되지 않은 사적 행동을 구체적으로 만들어낼 필요는 없다.

## Evidence

- Ethereum.org history: Vitalik Buterin conceived Ethereum in 2013 and authored the original whitepaper.
  - https://ethereum.org/ethereum-history-founder-and-ownership/
- Ethereum.org fork/history timeline: whitepaper release is recorded on 2013-11-27.
  - https://ethereum.org/ethereum-forks/
- Vitalik Buterin, Ethereum Foundation blog, 2014-01-23: he states that he wrote the initial Ethereum whitepaper draft in San Francisco in November 2013 after months of work on cryptocurrency 2.0 ideas.
  - https://blog.ethereum.org/2014/01/23/ethereum-now-going-public

## Resolution

CH12 마지막 장면을 다음 원칙으로 수정했다.

1. 확인되지 않은 `계약은? / 조직은? / 시장은?` 메모를 제거한다.
2. 2013년 11월 Vitalik의 초기 백서 초안 작성이라는 검증 가능한 사실을 장면의 축으로 사용한다.
3. 연구 설명문을 삽입하지 않고, Bitcoin에서 Ethereum으로 넘어가는 소설적 전환은 유지한다.
4. Ethereum ≠ Vitalik이라는 canon 분리를 깨지 않는다.

## Regression check

- CH11 말미의 2013-03-18 FinCEN 예고와 CH12 시작이 그대로 연결된다.
- CH12의 2013년 사건 순서는 유지된다: FinCEN → Silk Road 폐쇄 → 상원 청문회 → 11월 말 가격/새 설계 전환.
- V2 CH02의 Vitalik/Ethereum 본격 등장으로 넘어가는 기능은 유지된다.
- CH12 원고가 수정되었으므로 `11_REVIEW/QUEUE.md`의 CH12 blob SHA를 새 값으로 갱신했다.
- 독립 `historian + continuity` 검수는 아직 필요하므로 queue status는 `pending`으로 유지한다.
