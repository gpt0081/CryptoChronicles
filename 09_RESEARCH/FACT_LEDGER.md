# FACT LEDGER

## 상태
- `UNVERIFIED`: 아직 확인 전
- `PARTIAL`: 일부만 확인
- `VERIFIED`: 근거 확보
- `DISPUTED`: 신뢰 가능한 자료 간 해석 차이

## 항목 형식

| Fact ID | 날짜 | 주장 | 상태 | 1차 출처 | 보조 출처 | 관련 장 | 주의 |
|---|---|---|---|---|---|---|---|
| F-0001 | 2008-10-31 | Bitcoin 백서가 공개되었다 | UNVERIFIED | - | - | V1 | 원문 메일/백서 확인 |
| F-0002 | 2009-01-03 | Genesis Block이 생성되었다 | UNVERIFIED | - | - | V1 | 블록 데이터 확인 |
| F-0003 | 2010-05-22 | Pizza Day로 알려진 거래가 성사되었다 | UNVERIFIED | - | - | V1 | 포럼 원문 확인 |
| F-0004 | 2015-07-30 | Ethereum Frontier가 출시되었다 | UNVERIFIED | - | - | V2 | 공식 자료 확인 |
| F-0005 | 2016-06 | The DAO가 공격을 받았다 | UNVERIFIED | - | - | V2 | 날짜·금액·메커니즘 검증 |
| F-0006 | 2022-11 | FTX가 유동성 위기와 파산 절차에 들어갔다 | UNVERIFIED | - | - | V3 | 사건을 일자별로 분리 |
| F-0007 | 2024-01 | 미국에서 현물 Bitcoin ETF가 승인되었다 | UNVERIFIED | - | - | V4 | SEC 문서 확인 |
| F-0008 | 2008-09-15 | Lehman Brothers가 공식적으로 파산을 신청했다 | VERIFIED | Federal Reserve History, `Support for Specific Institutions` https://www.federalreservehistory.org/essays/support-for-specific-institutions | Federal Reserve History, `The Great Recession and Its Aftermath` https://www.federalreservehistory.org/essays/great-recession-and-its-aftermath | V1-C01 | 소설 속 ‘리먼’은 회사의 의인화이며 실제 개인이 아님 |
| F-0009 | 2008-09-16 | 연준은 뉴욕연준이 AIG에 최대 850억 달러의 담보부 회전신용을 제공하도록 승인했다 | VERIFIED | Federal Reserve Bank of New York, `Actions Related to AIG` https://www.newyorkfed.org/aboutthefed/aig | Federal Reserve History, `Support for Specific Institutions` https://www.federalreservehistory.org/essays/support-for-specific-institutions | V1-C01 | 소설의 연준·AIG 대화는 전부 C2 창작 |
| F-0010 | 2008-09 | 리먼 파산 이후 자금시장과 금융기관 사이의 신뢰가 급격히 악화되고 금융 패닉이 확산되었다 | VERIFIED | Federal Reserve Bank of New York, `Some Observations and Lessons from the Crisis` https://www.newyorkfed.org/newsevents/speeches/2010/pot100607 | Federal Reserve History, `Money Market Mutual Funds` https://www.federalreservehistory.org/essays/money-market-mutual-funds | V1-C01 | ‘신용’이라는 인물은 이 현상을 표현한 C2 의인화 |

## V1-C01 창작 경계

- 브루클린의 공장주, 퀸스의 부부는 특정 실존 인물을 묘사한 것이 아니라 위기가 실물경제로 전달되는 경로를 보여주기 위한 합성·허구 인물(C2)이다.
- ‘리먼’, ‘연준’, ‘AIG’, ‘신용’의 대사는 실제 발언을 재현하지 않는다.
- Bitcoin이 2008년 9월에 의식을 가졌다는 묘사는 전적으로 서사적 장치(C2)이며 역사 주장으로 취급하지 않는다.
