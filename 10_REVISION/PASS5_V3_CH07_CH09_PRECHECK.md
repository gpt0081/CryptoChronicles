# Pass 5 Internal Precheck — V3 CH07~CH09

## Scope

- `06_VOLUME_3/CH07_고속_신도시들.md`
- `06_VOLUME_3/CH08_레버리지의_제국.md`
- `06_VOLUME_3/CH09_루나의_몰락.md`
- Regression edge: `06_VOLUME_3/CH10_빚의_연쇄반응.md`

This is an internal precheck only. It does **not** satisfy the independent Pass 5 roles assigned in `11_REVIEW/QUEUE.md`.

## CH07 — no manuscript change

The September 14, 2021 Solana outage sequence remains consistent with the project Fact Ledger and the Solana Foundation incident report:

- network offline for about 17 hours;
- Grape Protocol IDO traffic and bot-generated transactions flooded the network;
- unbounded forwarder-queue memory growth and resource-heavy blocks contributed to validator crashes/forks;
- restart required at least 80% of active stake consensus and coordination among 1000+ validators;
- no funds were reported lost in the outage.

No new historical blocker or explanatory-voice blocker was identified that justified manuscript churn.

Primary check: Solana Foundation, `9-14 Network Outage Initial Overview` (2021-09-20).

## CH08 — no manuscript change

The chapter functions as the bridge from visible on-chain leverage to opaque company/fund credit networks. The distinctions among Celsius, BlockFi, Voyager, Genesis, 3AC, Terra/UST and DeFi are preserved. It does not claim that Terra was the sole cause of later CeFi failures.

No manuscript change was made.

## CH09 — chronology correction

### Finding

The previous ending stated that, after the Terra collapse, a door was already closing at Celsius and that users' exit door had begun to be locked. In the local scene chronology this follows the May 2022 Terra collapse by only days, which can be read as placing the Celsius withdrawal freeze in May.

The project Fact Ledger correctly dates the Celsius withdrawal and account-transfer halt to **2022-06-13** (`V3-F16`), and CH10 already opens on that exact date.

### Resolution

The ending was changed from an already-closing Celsius door to a foreshadowing image:

- Celsius remains visibly **open** at the end of CH09;
- the next fracture is described as moving toward it;
- CH10 retains the exact historical event and date: `2022년 6월 13일. Celsius가 문을 잠갔다.`

This removes a false temporal compression without adding research/explanatory prose to the novel.

## Regression check

- CH08 → CH09: leverage network and Terra/UST transition remains intact.
- CH09 → CH10: Terra aftermath now foreshadows, rather than prematurely depicts, the Celsius freeze.
- CH10 retains the exact June 13 date and distinction between withdrawal/transfer suspension and the later July 13 Chapter 11 filing.

## Queue impact

V3 CH09 manuscript blob changed to:

`35994a38924a5333e939daf41ce7d15e7d11edbd`

The queue fingerprint was updated. V3 CH07, CH08, and CH09 remain `pending` because the required independent review roles have not submitted current reviews.
