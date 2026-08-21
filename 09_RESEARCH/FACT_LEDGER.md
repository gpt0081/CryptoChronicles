# FACT LEDGER

## 상태
- `UNVERIFIED`: 아직 확인 전
- `PARTIAL`: 일부만 확인
- `VERIFIED`: 1차 또는 권위 있는 근거 확보
- `DISPUTED`: 신뢰 가능한 자료 간 해석 차이

| Fact ID | 날짜 | 주장 | 상태 | 1차/권위 출처 | 보조 출처 | 관련 장 | 주의 |
|---|---|---|---|---|---|---|---|
| F-0001 | 2008-10-31 | Satoshi Nakamoto가 Cryptography Mailing List에 Bitcoin 백서를 공개했다 | VERIFIED | Satoshi Nakamoto Institute, Cryptography thread: https://satoshi.nakamotoinstitute.org/emails/cryptography/threads/1/ | Whitepaper archive: https://nakamotoinstitute.org/library/bitcoin/ | V1-C02 | 메일의 발신자 외모·장소·심리는 알 수 없음 |
| F-0002 | 2009-01-03 | Bitcoin Genesis Block이 생성되었다 | VERIFIED | Bitcoin Core chain parameters: https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp | Bitcoin Book block reference: https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch11_blockchain.adoc | V1-C03 | nTime=1231006505, height 0 |
| F-0003 | 2010-05-22 | 10,000 BTC로 피자 두 판을 구입한 거래가 성사되어 Bitcoin Pizza Day로 기억된다 | PARTIAL | 원 Bitcointalk 2010 스레드 확보 필요 | 후대 포럼 인용·역사자료 확보 | V1-C06 | 원문 확보 전 직접 인용 금지 |
| F-0004 | 2015-07-30 | Ethereum Frontier 메인넷이 시작되었다 | VERIFIED | Ethereum Foundation: https://blog.ethereum.org/2015/07/30/ethereum-launches | Ethereum forks/history: https://ethereum.org/ethereum-forks/ | V2-C04 | Frontier는 첫 live release |
| F-0005 | 2016-06 | The DAO가 공격을 받았다 | UNVERIFIED | - | - | V2-C07 | 공격 시각·금액·메커니즘 별도 검증 |
| F-0006 | 2022-11 | FTX가 유동성 위기와 파산 절차에 들어갔다 | UNVERIFIED | - | - | V3-C11 | 사건을 일자별로 분리 |
| F-0007 | 2024-01 | 미국에서 현물 Bitcoin ETF가 승인되었다 | UNVERIFIED | - | - | V4-C03 | SEC 명령문 직접 확인 필요 |
| F-0008 | 2008-09-15 | Lehman Brothers가 공식적으로 파산을 신청했다 | VERIFIED | Federal Reserve History: https://www.federalreservehistory.org/essays/support-for-specific-institutions | Federal Reserve History, Great Recession | V1-C01 | 소설 속 ‘리먼’은 회사의 의인화 |
| F-0009 | 2008-09-16 | 연준은 뉴욕연준이 AIG에 최대 850억 달러의 담보부 회전신용을 제공하도록 승인했다 | VERIFIED | New York Fed, Actions Related to AIG: https://www.newyorkfed.org/aboutthefed/aig | Federal Reserve History | V1-C01 | 연준·AIG 대화는 C2 창작 |
| F-0010 | 2008-09 | 리먼 파산 이후 자금시장과 금융기관 사이의 신뢰가 급격히 악화되고 금융 패닉이 확산되었다 | VERIFIED | New York Fed crisis observations: https://www.newyorkfed.org/newsevents/speeches/2010/pot100607 | Federal Reserve History, Money Market Mutual Funds | V1-C01 | ‘신용’은 현상의 C2 의인화 |
| F-0011 | 2009-01-08 | Satoshi Nakamoto가 Bitcoin v0.1 소프트웨어 공개를 Cryptography Mailing List에 알렸다 | VERIFIED | Satoshi Nakamoto Institute email archive: https://satoshi.nakamotoinstitute.org/emails/cryptography/ | SNI thread index | V1-C04/C05 | 날짜는 메일 아카이브 기준 |
| F-0012 | 2009-01 | Genesis Block coinbase에는 당시 The Times의 은행 구제 관련 헤드라인이 들어 있다 | VERIFIED | Bitcoin Core source: https://github.com/bitcoin/bitcoin/blob/master/src/kernel/chainparams.cpp | Bitcoin Book blockchain chapter | V1-C03 | 본문에서 헤드라인은 짧게만 직접 인용 |
| F-0013 | 2016-07-20 | Ethereum DAO 관련 하드포크가 block 1,920,000에서 실행되었다 | VERIFIED | Ethereum Foundation: https://blog.ethereum.org/2016/07/20/hard-fork-completed | Ethereum forks/history | V2-C08/C09 | 공격 사건과 포크 사건을 분리 |
| F-0014 | 2012-12 | XRP Ledger 최종 버전이 완성되고 총 1000억 XRP가 생성되었다는 내용이 SEC 소송 기록에 기재되어 있다 | PARTIAL | SEC complaint, Dec. 22 2020: https://www.sec.gov/files/litigation/complaints/2020/comp-pr2020-338.pdf | XRPL 공식 역사자료 추가 필요 | V2/V3 | SEC 문서는 당시 소송 제출 문서임을 표시 |
| F-0015 | 2020-12-22 | SEC가 Ripple Labs와 두 임원을 상대로 XRP 판매 관련 소송을 제기했다 | VERIFIED | SEC release: https://www.sec.gov/newsroom/press-releases/2020-338 | SEC complaint | V4 또는 외전 | XRP≠Ripple 규칙 유지 |
| F-0016 | 2018-09-26 | Circle과 CENTRE가 USDC를 공식 출시했다 | VERIFIED | Circle: https://www.circle.com/blog/introducing-usd-coin | Circle ecosystem launch | V3-C02 | USDC≠Circle |
| F-0017 | 2014 | Tether가 블록체인 기반 법정화폐 연동 토큰 플랫폼으로 출범했다 | PARTIAL | Tether official history: https://tether.to/en/about-us/ | Tether FAQ | V3-C02 | 동시대 1차자료 추가 확보 필요 |
| F-0018 | 2020-03-16 | Solana Mainnet Beta가 시작되었다 | VERIFIED | Solana Foundation newsletter: https://solana.com/news/may-newsletter | Solana Year in Review | V3-C07 | 초기 네트워크 상태는 ‘Beta’로 표현 |
| F-0019 | 2019-05-30 | Chainlink가 Ethereum mainnet에서 초기 버전을 출시했다 | VERIFIED | Chainlink: https://chain.link/blog/chainlink-connected-consensus-on-ethereum | - | V3-C05 | 오라클 기능의 범위는 당시 시점에 맞춤 |
| F-0020 | 2021-02-24 | Chainlink Off-Chain Reporting이 mainnet에 배포되었다 | VERIFIED | Chainlink: https://chain.link/blog/off-chain-reporting-live-on-mainnet | - | V3 | 후대 기술을 초기 장면에 소급하지 않음 |
| F-0021 | 2023-07-17 | Chainlink CCIP가 mainnet에 공식 출시되었다 | VERIFIED | Chainlink official launch article | Chainlink documentation | V4 | 집필 직전 URL·기능 최신 재검증 |

## V1-C01 창작 경계
- 브루클린의 공장주, 퀸스의 부부는 특정 실존 인물을 묘사한 것이 아니라 위기가 실물경제로 전달되는 경로를 보여주기 위한 합성·허구 인물(C2)이다.
- ‘리먼’, ‘연준’, ‘AIG’, ‘신용’의 대사는 실제 발언을 재현하지 않는다.
- Bitcoin이 2008년 9월에 의식을 가졌다는 묘사는 전적으로 서사적 장치(C2)이며 역사 주장으로 취급하지 않는다.

## V1-C02/C03 창작 경계
- 메일링리스트 참가자 중 이름 없는 독자·연구자·회의론자는 합성 인물(C2)이다.
- Satoshi Nakamoto의 실제 외모, 성별, 거주지, 내면을 확정하지 않는다.
- Genesis Block 생성 순간의 방, 기계, 날씨, 감정 묘사는 C2이다.
- Genesis Block의 날짜, hash parameters, coinbase 메시지는 C0로 유지한다.
