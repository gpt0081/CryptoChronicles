# Volume 3 / Act II Research — Oracles, NFTs, Solana, Hidden Leverage

## R3-A2-01 — Chainlink mainnet and oracle problem
- Chainlink released on Ethereum mainnet on 2019-05-30.
- The core problem: smart contracts can verify on-chain state, but many financial contracts need external data such as asset prices. That creates an oracle dependency.
- Chainlink's design uses oracle networks and multiple data sources/nodes so contracts do not have to rely on a single external reporter.
- On 2021-02-24, Chainlink announced Off-Chain Reporting (OCR) live on mainnet across a number of Price Feed oracle networks, reducing on-chain aggregation costs and improving scalability.
- Sources: Chainlink 2019-05-30 `Connected Consensus on Ethereum`; Chainlink 2021-02-24 `Off-Chain Reporting Live on Mainnet`.

## R3-A2-02 — Oracle boundaries
- A blockchain cannot natively know a dollar price, weather result, election result or API response merely because the information exists on the Internet.
- DeFi liquidations and collateral ratios can depend critically on external price data, but not every protocol uses Chainlink and not every oracle system works the same way.
- Maker historically maintained its own oracle architecture; do not write Chainlink as universal oracle for all DeFi.
- Narrative principle: an oracle can make data delivery more robust but cannot make the underlying real-world data metaphysically true.

## R3-A2-03 — 2021 NFT mainstream art-market moment
- NFTs existed before 2021. The 2021 chapter is about mass cultural/financial attention, not NFT invention.
- On 2021-03-11, Christie's sold Beeple's `EVERYDAYS: THE FIRST 5000 DAYS` for $69,346,250.
- Christie's described it as the first purely digital NFT-based work offered by a major auction house and said the result was the third-highest auction price for a living artist at the time.
- The work was paid for in Ether in the Christie's transaction context, and the sale connected traditional art collectors with crypto-native collectors.
- Sources: Christie's press releases and auction page, 2021-03-11/12.

## R3-A2-04 — NFT ownership boundary
- An NFT is an on-chain token/record with a unique identifier and ownership state. Ownership of the NFT does not automatically transfer copyright, trademark rights or every legal right in the referenced image/artwork unless the relevant contract/license says so.
- The token and the media/resource it references are distinct layers.
- Narrative rule: portray NFT as digital provenance/market coordination plus speculation, not as 'buying a JPEG file'.

## R3-A2-05 — Solana launch and growth
- Solana Mainnet Beta launched on 2020-03-16.
- Solana Foundation's 2020 review describes substantial ecosystem growth after launch; by 2021 DeFi, wallets, NFT projects and stablecoins had expanded rapidly.
- On 2021-06-09 Solana Labs announced a $314,159,265 private token sale led by Andreessen Horowitz and Polychain Capital, reflecting institutional funding for ecosystem expansion.
- The protocol, Solana Labs, Solana Foundation and SOL token are distinct entities/layers.
- Sources: Solana Foundation 2020 May Newsletter; Year in Review 2020; 2021 funding announcement.

## R3-A2-06 — Solana 2021 outage
- On 2021-09-14, Solana Mainnet Beta was offline for 17 hours. The Foundation reported that no funds were lost.
- During the Grape Protocol IDO on Raydium, bots flooded the network with transactions. These produced unbounded forwarder-queue memory growth and resource-heavy blocks; validators ran out of memory/crashed, forks accumulated, and consensus stalled.
- Recovery required diagnosis, software changes and a coordinated restart supported by 80%+ of active stake; the Foundation said 1,000+ validators participated in recovery coordination.
- Source: Solana Foundation 2021-09-20 `9-14 Network Outage Initial Overview`.
- Narrative rule: do not claim 'speed itself caused the outage'. The documented event had specific software/resource/traffic causes.

## R3-A2-07 — Centralized crypto lenders and hidden counterparty risk
- During the 2020-2022 cycle, centralized crypto lenders attracted deposits by offering high yields and made loans to institutional borrowers/hedge funds. These arrangements did not necessarily expose collateral and counterparty positions transparently on-chain to depositors.
- Celsius froze withdrawals on 2022-06-13 citing extreme market conditions; Reuters later described the business model as taking depositor tokens and lending mostly to institutional investors, earning the spread.
- Three Arrows Capital (3AC), a crypto hedge fund, failed margin calls in June 2022. Reuters reported BlockFi liquidated at least part of a 3AC position.
- Voyager disclosed 3AC owed 15,250 BTC (then about $324m) plus $350m USDC and issued a default notice on 2022-06-27.
- Genesis later disclosed exposure to 3AC and said the loans had a weighted average margin requirement above 80%.
- Sources: Reuters 2022-06-13, 06-16, 06-27, 07-06; Voyager 2022-06-27 statement.

## R3-A2-08 — Act II chronology boundary
- Chapter 8 is primarily the *construction* of the leverage web in 2020-early 2022. Exact defaults and bankruptcies are revealed in Chapters 9-11 when historically reached.
- Characters in 2021 must not know 3AC/Celsius/Voyager/FTX will fail in 2022.
- Omniscient narration may foreshadow structural opacity, but avoid presenting later allegations or bankruptcy findings as facts known to participants at the time.

## Act II 창작 경계
- `Chainlink`, `Oracle`, `NFT`, `Solana`, `Leverage`, `CeFi Lenders`, `3AC` may be personified. Dialogue is C2.
- Chainlink is not the source of all truth and is not used by every protocol.
- NFT token ownership, media possession and intellectual-property rights are distinct.
- Solana≠Solana Labs≠Solana Foundation≠SOL.
- The 2021 Solana outage is a liveness failure with a documented traffic/software-resource cause; no funds were reported lost.
- Celsius, BlockFi, Voyager, Genesis and 3AC are distinct businesses/fund structures. Do not merge them into a single villain.
