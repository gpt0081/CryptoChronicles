# Pass 5 V2 CH03–CH04 Precheck

## Scope

- `05_VOLUME_2/CH03_새_도시의_투자자들.md`
- `05_VOLUME_2/CH04_프로그래머블_시티의_점화.md`
- adjacent continuity into CH05

This is an internal precheck only. It does not satisfy the independent Pass 5 role requirements in `11_REVIEW/QUEUE.md`.

## CH03 — no manuscript change

Reviewed the Ether sale chronology, sale duration, BTC-denominated purchase structure, delayed network usability, and transition into Olympic/Frontier preparation. No publication-blocking historical or narrative issue was found in this pass.

## CH04 — resolved novel-voice issue

### Finding

The Frontier thawing passage was historically accurate but read like protocol documentation:

- block gas limit = 5,000
- ordinary transaction needs more gas than the initial cap
- thawing intentionally prevented immediate economic activity

The Ethereum Foundation's July 22, 2015 Frontier notice confirms that the first release hardcoded a 5,000 gas-per-block limit specifically to prevent transactions during the first few days. The August 4 thawing update also confirms that 21,000 gas was required for a basic transaction.

### Decision

`RESOLVED`

The explanatory paragraph was compressed into scene language while preserving the two historically material facts: the 5,000 gas cap and the practical impossibility of an ordinary transfer at launch.

### Revision principle

Keep the technical constraint visible as action and image, not as a miniature protocol lesson.

## Regression check

- CH03 still leads cleanly from presale/fundraising into launch preparation.
- CH04 still establishes Frontier's deliberately cautious launch and foreshadows governance/code-risk questions.
- CH05 can still move into smart-contract fallibility without requiring technical exposition from CH04.

## External review status

- V2 CH03 remains `pending` for `novel-editor + red-team`.
- V2 CH04 remains `pending` for `historian + continuity`.
- Any future external report must match the current manuscript blob SHA recorded in `11_REVIEW/QUEUE.md`.
