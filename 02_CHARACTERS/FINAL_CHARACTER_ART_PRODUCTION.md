# Final Character Art Production Specification

이 문서는 `CHARACTER_ART_BIBLE.md`을 실제 이미지 제작 단계로 내리는 최종 제작 사양이다. 목표는 현재 `portraits/*.jpg`의 legacy placeholder 6장을 하나의 정본 캐릭터 세트로 교체하는 것이다.

## 공통 생성 사양

- 출력 비율: 4:5 세로형.
- 구도: 상반신 또는 3/4 인물화, 눈높이 시점, 과도한 광각 금지.
- 화풍: graphic novel + editorial character illustration, clean shape language, restrained texture, limited shading, non-photorealistic.
- 얼굴: 실제 사람처럼 피부 모공·사진 조명·렌즈 심도를 재현하지 않는다. 얼굴은 단순화된 조형과 표정 중심.
- 세트 일관성: 동일한 선 굵기, 동일한 명암 단계, 동일한 배경 밀도, 동일한 캐릭터 렌더링 수준을 유지한다.
- 배경: 캐릭터 정체성을 읽히게 하는 상징적 구조만 사용한다. 정보 과밀 금지.
- 로고: 직접 삽입 금지. 프로토콜 로고를 의상·얼굴·이마·장신구에 붙이지 않는다.
- 텍스트: 이미지 안에 글자, 티커, 숫자, 워터마크를 넣지 않는다.
- 실존 인물 유사성: 특정 창립자·임직원을 닮게 만들지 않는다.
- 목표: 이름을 가려도 여섯 캐릭터가 실루엣과 시각언어만으로 구별되어야 한다.

## 공통 negative prompt

photorealistic, hyperrealistic, realistic human portrait, celebrity likeness, founder likeness, Satoshi face, Vitalik Buterin likeness, Brad Garlinghouse likeness, crypto logo on forehead, logo costume, coin-headed person, literal coin face, mascot costume, anime fan art, chibi, glossy 3D render, game character splash art, cyberpunk neon overload, stock photo lighting, cinematic camera bokeh, skin pores, photo lens depth of field, text, ticker symbol, watermark, caption, infographic, corporate advertising poster

---

## 1. Bitcoin

### Canonical read
오래된 개척자. 희소성, 자기보관, 느린 확신, 규칙에 대한 완고함을 몸에 지닌 존재.

### Production prompt
A canonical character illustration for a historical-financial novel. An old frontier-like wanderer representing Bitcoin, but not a real historical person. Heavy simple silhouette, weathered long coat, durable dark leather and aged metal details, compact practical gear, guarded posture, calm unwavering expression, minimal ornament. The character should feel difficult to move and difficult to intimidate. Background hints at a sparse early digital frontier built from rough block-like structures and distant cold lights. No visible cryptocurrency logo. Graphic-novel editorial illustration, simplified face, clean shapes, restrained texture, limited shading, non-photorealistic, upper-body three-quarter portrait, 4:5 vertical composition.

### Recognition anchors
- 가장 무거운 실루엣
- 낡았지만 버리지 않는 장비
- 금색 자체보다 오래된 금속의 재질감
- 과장된 분노가 아닌 조용한 경계심

### Must not imply
- Satoshi Nakamoto의 얼굴
- 서부극 특정 배우
- 금화 그 자체가 인간이 된 모습

---

## 2. Ethereum

### Canonical read
프로그래머블 시티의 설계자. 가능성을 먼저 보고, 시간이 흐르며 자신이 만든 복잡성의 책임까지 짊어진다.

### Production prompt
A canonical character illustration for a historical-financial novel. A visionary city architect representing Ethereum, clearly fictional and not resembling Vitalik Buterin. Layered geometric silhouette, asymmetrical structured clothing that looks assembled from architectural planes, subtle blueprint-like tools and modular components, alert intelligent expression carrying both curiosity and responsibility. Behind the character, an unfinished luminous city of interconnected structures rises in multiple layers, suggesting contracts and systems rather than skyscraper spectacle. No visible Ethereum logo. Graphic-novel editorial illustration, simplified face, sharp shape language, restrained texture, limited shading, non-photorealistic, upper-body three-quarter portrait, 4:5 vertical composition.

### Recognition anchors
- 겹쳐진 구조와 설계도
- Bitcoin보다 가볍고 복잡한 실루엣
- 뒤로 계속 확장되는 미완성 도시
- 발명가의 호기심 + 운영자의 피로

### Must not imply
- Vitalik Buterin의 외모
- 마법사나 초능력자
- 무한 확장을 무조건 긍정하는 영웅

---

## 3. XRP

### Canonical read
속도와 연결의 외교관. 철학적 고립보다 서로 다른 금융권 사이에서 실제로 움직이는 통로를 중시한다.

### Production prompt
A canonical character illustration for a historical-financial novel. A composed cross-border financial diplomat representing XRP, fictional and not resembling any Ripple executive. Clean tailored but mobile silhouette, practical formal clothing adapted for constant movement, slim document case or signal device, measured confident expression, standing between two distinct financial districts connected by narrow luminous transit lines. The character should look comfortable negotiating with institutions without becoming one of them. No visible XRP or Ripple logo. Graphic-novel editorial illustration, simplified face, precise clean shapes, restrained texture, limited shading, non-photorealistic, upper-body three-quarter portrait, 4:5 vertical composition.

### Recognition anchors
- 가장 정돈된 실무가형 실루엣
- 서로 다른 도시를 연결하는 교차선
- 외교관 같은 침착함
- 속도를 과시하기보다 흐름을 관리하는 자세

### Must not imply
- Ripple 임직원의 외모
- 은행원 그 자체
- 규제기관의 대리인

---

## 4. Stablecoins

### Canonical read
가치 고정과 유동성의 관리자. 하나의 인물이 아니라 여러 설계의 가족을 대표하는 복합 캐릭터다.

### Production prompt
A canonical character illustration for a historical-financial novel. A calm reserve manager representing the family of stablecoins rather than a single token. Balanced symmetrical silhouette, immaculate layered clothing with subtle variations suggesting multiple backing structures, holding a compact ledger while several different reserve compartments, treasury-like documents and collateral drawers form the background. Expression is composed, watchful and slightly burdened, communicating that stability requires constant maintenance. No visible stablecoin logos, dollar signs or issuer branding. Graphic-novel editorial illustration, simplified face, clean balanced shapes, restrained texture, limited shading, non-photorealistic, upper-body three-quarter portrait, 4:5 vertical composition.

### Recognition anchors
- 가장 균형 잡힌 자세
- 장부와 여러 개의 준비금 구조
- 단정한 외형 뒤의 복잡한 백업 시스템
- 평온하지만 긴장을 놓지 않는 표정

### Must not imply
- USDT, USDC, DAI, UST 중 하나가 전체를 대표
- 완전 무위험 자산
- 단순히 달러 지폐 인간

---

## 5. Solana

### Canonical read
고속 신도시의 질주자. 빠르고 야심차며 규모를 좇지만, 과열과 멈춤의 기억도 함께 지닌다.

### Production prompt
A canonical character illustration for a historical-financial novel. A young high-speed city runner representing Solana, fictional and not based on any founder. Long forward-leaning silhouette, lightweight layered clothing shaped by motion, confident restless expression, one foot visually ready to launch. Background suggests a bright high-throughput new city with multiple parallel data lanes, but includes a few subtle interrupted lines and restart marks, showing that speed has operational costs. Avoid generic cyberpunk aesthetics and avoid excessive neon. No Solana logo. Graphic-novel editorial illustration, simplified face, clean dynamic shapes, restrained texture, limited shading, non-photorealistic, upper-body or three-quarter portrait, 4:5 vertical composition.

### Recognition anchors
- 가장 앞으로 기울어진 실루엣
- 병렬로 달리는 도시의 선
- 자신감과 조급함이 동시에 있는 표정
- 매끈하지만 완벽하지 않은 인프라 흔적

### Must not imply
- 단순 네온 사이버펑크 캐릭터
- 항상 멈추지 않는 완벽한 네트워크
- 특정 Solana 창립자의 외모

---

## 6. Chainlink

### Canonical read
계약과 외부 세계 사이를 오가는 전령. 진실을 창조하는 예언자가 아니라 여러 출처에서 신호를 모아 전달한다.

### Production prompt
A canonical character illustration for a historical-financial novel. A quiet information courier representing Chainlink, fictional and not based on any founder. Narrow observant silhouette, practical layered clothing with small relay-like tools, several incoming signal paths from distinct off-screen sources converging into one carefully handled message. The character stands between an abstract contract-city and fragments of the external world, expression cautious and precise rather than mystical. No Chainlink logo, no oracle robes, no supernatural imagery. Graphic-novel editorial illustration, simplified face, clean connected shapes, restrained texture, limited shading, non-photorealistic, upper-body three-quarter portrait, 4:5 vertical composition.

### Recognition anchors
- 가장 조용하고 관찰자에 가까운 자세
- 여러 입력선이 하나의 메시지로 모임
- 신호를 전달하지만 소유하지 않는 손동작
- 신중하고 과장 없는 표정

### Must not imply
- 신탁을 내리는 예언자
- 하나의 데이터 제공자가 진실 전체를 결정
- 초자연적 전지성

---

## 파일 교체 규칙

최종 승인된 이미지는 아래 경로를 그대로 유지하며 교체한다.

- `02_CHARACTERS/portraits/bitcoin.jpg`
- `02_CHARACTERS/portraits/ethereum.jpg`
- `02_CHARACTERS/portraits/xrp.jpg`
- `02_CHARACTERS/portraits/stablecoins.jpg`
- `02_CHARACTERS/portraits/solana.jpg`
- `02_CHARACTERS/portraits/chainlink.jpg`

파일명을 유지해야 `CAST_INDEX.md`의 링크가 깨지지 않는다.

## 세트 승인 순서

1. 먼저 Bitcoin과 Ethereum을 생성해 화풍의 양끝을 고정한다.
2. 두 이미지가 실사로 보이지 않고 서로 명확히 구분되는지 확인한다.
3. 그 기준을 유지해 XRP, Stablecoins, Solana, Chainlink를 생성한다.
4. 여섯 장을 한 화면에 놓고 실루엣 중복, 얼굴 유사성, 배경 밀도 차이를 검사한다.
5. 한 캐릭터만 지나치게 사실적이거나 화려하면 해당 이미지만 재생성한다. 세트 전체를 평균화하지 않는다.
6. 여섯 이미지 교체 후 `CAST_INDEX.md` 갤러리 링크를 확인한다.
7. 마지막으로 `CHARACTER_ART_BIBLE.md`의 7개 승인 체크를 다시 수행하고 `10_REVISION/`에 최종 art audit을 기록한다.

## Publication-ready gate

현재 6개 legacy JPG가 이 문서 기준의 정본 이미지로 실제 교체되기 전에는 캐릭터 아트 작업을 완료로 표시하지 않는다. 프롬프트 문서가 존재하는 것만으로는 완료가 아니다.
