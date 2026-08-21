# FACT LEDGER

## 상태
- `UNVERIFIED`: 아직 확인 전
- `PARTIAL`: 일부만 확인
- `VERIFIED`: 1차 또는 권위 있는 근거 확보
- `DISPUTED`: 신뢰 가능한 자료 간 해석 차이

| Fact ID | 날짜 | 주장 | 상태 | 1차/권위 출처 | 보조 출처 | 관련 장 | 주의 |
|---|---|---|---|---|---|---|---|
| F-0001 | 2008-10-31 | Satoshi Nakamoto가 Cryptography Mailing List에 Bitcoin 백서를 공개했다 | VERIFIED | Satoshi Nakamoto Institute Cryptography thread | SNI whitepaper archive | V1-C02 | 발신자의 외모·장소·심리는 알 수 없음 |
| F-0002 | 2009-01-03 | Bitcoin Genesis Block이 생성되었다 | VERIFIED | Bitcoin Core `chainparams.cpp` | Bitcoin Book | V1-C03 | nTime=1231006505, height 0 |
| F-0003 | 2010-05-22 | Laszlo Hanyecz가 10,000 BTC를 피자와 교환했다고 공개 보고했다 | VERIFIED | Bitcointalk 원 스레드/보존 인용 | 거래·사진 보존자료 | V1-C07 | ‘최초 실물구매’ 표현은 문맥을 붙여 사용 |
| F-0004 | 2015-07-30 | Ethereum Frontier 메인넷이 시작되었다 | VERIFIED | Ethereum Foundation | ethereum.org forks/history | V2-C04 | Frontier는 첫 live release |
| F-0005 | 2016-06 | The DAO가 공격을 받았다 | UNVERIFIED | - | - | V2-C07 | 공격 시각·금액·메커니즘 별도 검증 |
| F-0006 | 2022-11 | FTX가 유동성 위기와 파산 절차에 들어갔다 | UNVERIFIED | - | - | V3-C11 | 사건을 일자별로 분리 |
| F-0007 | 2024-01 | 미국에서 현물 Bitcoin ETF가 승인되었다 | UNVERIFIED | - | - | V4-C03 | SEC 명령문 직접 확인 필요 |
| F-0008 | 2008-09-15 | Lehman Brothers가 파산을 신청했다 | VERIFIED | Federal Reserve History | Federal Reserve History | V1-C01 | ‘리먼’은 회사의 의인화 |
| F-0009 | 2008-09-16 | 연준은 뉴욕연준이 AIG에 최대 850억 달러의 담보부 회전신용을 제공하도록 승인했다 | VERIFIED | New York Fed | Federal Reserve History | V1-C01 | 연준·AIG 대화는 C2 |
| F-0010 | 2008-09 | 리먼 파산 이후 금융기관 사이의 신뢰와 자금시장이 급격히 악화되었다 | VERIFIED | New York Fed | Federal Reserve History | V1-C01 | ‘신용’은 C2 의인화 |
| F-0011 | 2009-01-08 | Satoshi가 Bitcoin v0.1 소프트웨어 공개를 Cryptography Mailing List에 알렸다 | VERIFIED | SNI email archive | SNI thread | V1-C04 | 공개 메일 기준 |
| F-0012 | 2009-01-03 | Genesis Block coinbase에 당시 The Times의 은행 구제 관련 헤드라인이 들어 있다 | VERIFIED | Bitcoin Core source | Bitcoin Book | V1-C03 | 본문 직접 인용은 짧게 제한 |
| F-0013 | 2016-07-20 | Ethereum DAO 관련 하드포크가 block 1,920,000에서 실행되었다 | VERIFIED | Ethereum Foundation | ethereum.org | V2-C08/C09 | 공격과 포크 분리 |
| F-0014 | 2012-12 | XRP Ledger 최종 버전과 총 1000억 XRP 생성에 관한 내용이 SEC 소송기록에 기재돼 있다 | PARTIAL | SEC complaint | XRPL 공식 자료 추가 필요 | V2/V3 | 소송상 주장과 독립적 사실 구분 |
| F-0015 | 2020-12-22 | SEC가 Ripple Labs와 두 임원을 상대로 XRP 판매 관련 소송을 제기했다 | VERIFIED | SEC | SEC complaint | V4/외전 | XRP≠Ripple |
| F-0016 | 2018-09-26 | Circle과 CENTRE가 USDC를 공식 출시했다 | VERIFIED | Circle | - | V3-C02 | USDC≠Circle |
| F-0017 | 2014 | Tether가 법정화폐 연동 토큰 플랫폼으로 출범했다 | PARTIAL | Tether 공식 역사 | - | V3-C02 | 동시대 자료 추가 확보 |
| F-0018 | 2020-03-16 | Solana Mainnet Beta가 시작되었다 | VERIFIED | Solana Foundation | Year in Review | V3-C07 | Beta 표현 유지 |
| F-0019 | 2019-05-30 | Chainlink가 Ethereum mainnet에서 초기 버전을 출시했다 | VERIFIED | Chainlink | - | V3-C05 | 당시 기능 범위만 사용 |
| F-0020 | 2021-02-24 | Chainlink Off-Chain Reporting이 mainnet에 배포되었다 | VERIFIED | Chainlink | - | V3 | 후대 기술 소급 금지 |
| F-0021 | 2023-07-17 | Chainlink CCIP가 mainnet에 공식 출시되었다 | VERIFIED | Chainlink | docs | V4 | 최신 재검증 필요 |
| F-0022 | 2009-01-12 | Block 170에 초기 비-coinbase Bitcoin 전송이 기록되었고 Hal Finney의 회고와 결합해 Satoshi→Finney 10 BTC 시험 전송으로 알려져 있다 | VERIFIED | Block 170 blockchain data | Hal Finney 공개 회고 | V1-C05 | 수신자 귀속은 공개 역사기록과 결합 |
| F-0023 | 2009-01-11 | Hal Finney가 `Running bitcoin`이라는 공개 상태 메시지를 남겼다 | VERIFIED | Hal Finney 원 공개 게시물/보존자료 | SNI 초기 기록 | V1-C05 | 직접 인용은 두 단어만 사용 |
| F-0024 | 2009-10-05 | New Liberty Standard가 $1 = 1,309.03 BTC라는 초기 달러 환율을 게시했다 | VERIFIED | 당시 페이지의 Web Archive 보존값 | Monetary Future 정리 | V1-C06 | 거래 체결가격이 아니라 비용 기반 게시 환율 |
| F-0025 | 2009-10-12 | Martti Malmi가 5,050 BTC를 $5.02 PayPal 송금과 교환한 최초의 알려진 BTC-USD 거래를 회고·거래기록으로 확인했다 | VERIFIED | Martti Malmi 공개 기록 + blockchain tx | 후대 역사자료 | V1-C06 | ‘최초 알려진’ 표현 유지 |
| F-0026 | 2010-03-17 | Bitcoin Market이 초기 BTC/USD 시장 거래를 시작했다 | PARTIAL | 동시대 포럼·사이트 기록 | 역사자료 | V1-C06 | 연속 가격 데이터 시작시점과 구분 |
| F-0027 | 2011-01경 | Silk Road가 운영을 시작했고 Bitcoin을 결제수단으로 사용했다 | VERIFIED | DOJ Ulbricht 사건자료 | 동시대 보도 | V1-C08 | 범죄시장과 Bitcoin 자체를 동일시하지 않음 |
| F-0028 | 2011-04~06 | Bitcoin 가격이 약 $1에서 $30 이상으로 급등했다 | VERIFIED | 동시대 Ars Technica 보도 | 기타 역사 가격자료 | V1-C09 | 거래소별 가격 차이 존재 |
| F-0029 | 2011-06-19 | Mt. Gox의 계정 침해로 비정상 대량매도가 발생해 표시가격이 $17대에서 센트대로 순간 추락했고 거래가 중단됐다 | VERIFIED | 당시 Ars Technica 보도 + Mt. Gox 공지 보존 | TechCrunch | V1-C09 | Bitcoin 프로토콜 자체 침해가 아님 |
| F-0030 | 2011-06 | Silk Road와 Bitcoin에 대한 보도로 미국 상원의원들이 법 집행기관의 대응을 요구했다 | VERIFIED | 동시대 언론 보도 | Ars/Fortune | V1-C10 | 개별 발언 직접 인용은 원문 확인 시만 |
| F-0031 | 2013-01말 | Avalon ASIC 장치가 공개적으로 사용자 손에 등장하며 Bitcoin 채굴의 ASIC 시대가 본격화했다 | PARTIAL | Bitcointalk Avalon 개발/수령 스레드 | 당시 보도 | V1-C11 | ‘세계 최초’ 단정은 별도 검증 필요 |
| F-0032 | 2013-03-11 | block 225,430에서 Bitcoin 0.8과 구버전 노드의 비호환성으로 예상치 못한 체인 포크가 발생했다 | VERIFIED | bitcoin.org chain fork notice | BIP 50 | V1-C11 | 기술적 accidental fork |
| F-0033 | 2013-03-11 | 주요 0.8 채굴 풀들이 0.7 호환 체인으로 전환하도록 요청받아 단일 체인을 복구했다 | VERIFIED | bitcoin.org | BIP 50 | V1-C11 | ‘개발자가 일방 통제’로 묘사 금지 |
| F-0034 | 2013-03-18 | FinCEN이 convertible virtual currency 지침 FIN-2013-G001을 발표했다 | VERIFIED | FinCEN | FinCEN press release | V1-C12 | 사용자와 administrator/exchanger를 구분 |
| F-0035 | 2013-10-01 | Ross Ulbricht가 체포됐고 미 연방정부가 원 Silk Road를 압수·폐쇄했다 | VERIFIED | DOJ SDNY | 후속 DOJ 문서 | V1-C12 | 혐의·유죄 확정 시점을 혼동하지 않음 |
| F-0036 | 2013-10-25 기준 | 미국 정부가 Silk Road 사건과 관련해 총 약 173,991 BTC를 압수했다고 발표했다 | VERIFIED | DOJ SDNY | - | V1-C12 | 10/1 압수와 10/25 추가 압수 발표 구분 |
| F-0037 | 2013-11-18 | 미 상원 HSGAC가 `Beyond Silk Road: Potential Risks, Threats, and Promises of Virtual Currencies` 청문회를 열었다 | VERIFIED | GovInfo Senate hearing record | Congressional Record | V1-C12 | 제목의 ‘risks/threats/promises’은 공식 명칭 |
| F-0038 | 2013-11-27 | Mt. Gox에서 Bitcoin 가격이 처음 $1,000을 넘어섰다 | VERIFIED | Reuters 동시대 보도 | CBS/Yahoo Reuters 재게재 | V1-C12 | 당일 보도치 $1,044~$1,073 차이는 시점/기사 버전 차이 |

## V1 창작 경계
- ‘Bitcoin’, ‘신용’, ‘가격’, ‘국가’, ‘Mt. Gox’, ‘Silk Road’, ‘채굴자’의 대화·감정은 C2 의인화다.
- Satoshi Nakamoto의 실제 외모, 성별, 거주지, 내면을 확정하지 않는다.
- Hal Finney 등 실존 인물의 심리는 공개 기록에서 확인되지 않는 한 단정하지 않는다.
- 가격·시장 사건은 거래소별 차이가 있으므로 단일한 전세계 공식가격처럼 쓰지 않는다.
- 정부는 단일 의지를 가진 실체가 아니므로 작품 안에서도 기관·정치인의 입장 차이를 인정한다.
- Bitcoin 프로토콜의 실패와 거래소·서비스 사업자의 실패를 반드시 분리한다.
