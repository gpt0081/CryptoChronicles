# Pass 5 Precheck — V3 CH10–CH12

Status: COMPLETE (internal precheck only)

Scope:
- `06_VOLUME_3/CH10_*`
- `06_VOLUME_3/CH11_*`
- `06_VOLUME_3/CH12_*`
- regression boundary: V3 CH09 → V3 CH10 → V3 CH11 → V3 CH12 → V4 CH01

This is an internal historical/narrative precheck. It does **not** satisfy the independent Pass 5 role assignments in `11_REVIEW/QUEUE.md`.

## CH10 — 빚의 연쇄반응

Verdict: no manuscript change required.

Checks:
- Celsius suspension is placed on 2022-06-13 and described as a halt to withdrawals and account transfers, rather than a protocol failure.
- 3AC, Voyager and Celsius are not collapsed into one causal mechanism. The chapter explicitly distinguishes leverage/loss exposure, creditor default exposure, and different asset-liability structures.
- Voyager's 3AC exposure is stated as 15,250 BTC plus USD 350 million USDC, followed by the June 27 default notice; the chapter then separates Voyager's July 5 Chapter 11 filing from Celsius's July 13 filing.
- The ending correctly hands the timeline to Ethereum's September 15 Merge without implying that the summer credit failures caused the Merge.

Narrative voice: the credit-chain explanation remains embedded in character conflict and scene movement. No research-note insertion was found that justified churn.

## CH11 — 병합 이후의 침묵

Verdict: no manuscript change required.

Primary-source cross-check:
- Ethereum Foundation's Merge announcements describe a two-step sequence: Bellatrix on the consensus layer, then Paris on the execution layer at Terminal Total Difficulty.
- Bellatrix activated on 2022-09-06; Paris/The Merge completed on 2022-09-15.
- ethereum.org records The Merge as reducing Ethereum energy consumption by approximately 99.95%.

The manuscript matches this sequence and correctly avoids common false claims: it explicitly says The Merge did not create a new ETH asset, did not instantly lower fees, and did not magically multiply throughput.

Narrative voice: technical details are carried through the 'heart transplant' scene and Bitcoin/Ethereum dialogue. No explanatory rewrite was warranted.

## CH12 — FTX의 밤

Verdict: no manuscript change required.

Checks:
- The chapter keeps the early-November liquidity crisis distinct from later reconstruction of the full balance-sheet and customer-fund story.
- November 8 is used for the non-binding Binance acquisition announcement; the rescue collapses after due diligence rather than being presented as a completed acquisition.
- November 11 is used for the Chapter 11 filing, Sam Bankman-Fried's resignation and John J. Ray III's arrival.
- The manuscript treats FTX/Alameda opacity and custody failure as a centralized-intermediary problem rather than claiming the underlying public networks failed together.
- The transition into V4 is structurally clean: institutions and state actors enter after the FTX crisis without being presented as a single coordinated actor.

Narrative voice: no glossary-style or research-report paragraph was found that justified a manuscript edit.

## Regression result

- CH09 → CH10: Celsius remains open at the end of CH09 and closes on the dated CH10 scene, preserving the prior chronology fix.
- CH10 → CH11: summer credit failures lead into, but do not cause, the September Merge.
- CH11 → CH12: November FTX rumors follow the completed September Merge in chronological order.
- CH12 → V4 CH01: the arrival of institutions/regulators is a thematic handoff, not a claim of unified intent.

## Pass 5 impact

No chapter blob SHA changed in this precheck. Therefore the existing `11_REVIEW/QUEUE.md` fingerprints for V3 CH10–CH12 remain current.

Required independent reviews remain unchanged:
- V3 CH10: `character`, `blind-reader`
- V3 CH11: `novel-editor`, `red-team`
- V3 CH12: `historian`, `continuity`

Publication readiness: not yet. Independent Pass 5 review remains outstanding.