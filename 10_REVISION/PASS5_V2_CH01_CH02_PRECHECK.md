# Pass 5 V2 CH01–CH02 Internal Precheck

Status: INTERNAL PRECHECK ONLY — does not satisfy independent Pass 5 role requirements.

## Scope

- `05_VOLUME_2/CH01_거래소의_유령.md`
- `05_VOLUME_2/CH02_어린_설계자.md`
- Adjacent continuity into V2 CH03

## CH01 — 거래소의 유령

No manuscript change in this pass.

The chapter's core historical frame remains consistent with the project canon: Mt. Gox withdrawal problems escalated in February 2014, the site stopped normal operation around February 25, civil rehabilitation was filed in Tokyo on February 28, roughly 850,000 BTC were initially reported missing, and about 200,000 BTC were later found. The chapter already avoids reducing the failure to transaction malleability alone and keeps protocol weakness distinct from exchange custody/operations failure.

## CH02 — 어린 설계자

### Finding

Severity: MAJOR

The chapter correctly places the initial Ethereum whitepaper in late 2013 and the public announcement in January 2014, but a later scene had Ethereum point directly at the ruins of Mt. Gox and say that it needed to build its system to avoid "that kind of door." In context this could make the February 2014 Mt. Gox collapse read as a cause of Ethereum's original design.

That chronology is backwards. Vitalik Buterin wrote the initial Ethereum whitepaper draft in November 2013. On January 23, 2014, before Mt. Gox's February collapse, the official Ethereum blog already described unreliable exchanges, fraudulent services, and residual centralization as ecosystem problems Ethereum hoped to address. Ethereum was formally presented at the Miami Bitcoin conference on January 25, 2014.

### Sources

- Ethereum Foundation Blog, "Ethereum: Now Going Public," 2014-01-23: https://blog.ethereum.org/2014/01/23/ethereum-now-going-public
- Ethereum Foundation Blog, "Cut and try: building a dream," 2016-02-09 retrospective: https://blog.ethereum.org/2016/02/09/cut-and-try-building-a-dream
- ethereum.org, Ethereum history: https://ethereum.org/ethereum-history-founder-and-ownership/

### Fix applied

Removed the direct gesture toward the Mt. Gox ruins. Ethereum now looks toward exchange signs generally and says:

> “저런 문 하나에 모든 선택을 맡기지 않으려면.”

This preserves the scene's thematic argument about centralized intermediaries without inventing a false causal sequence.

## Regression check

- V2 CH01 still hands off naturally from the Mt. Gox collapse to the arrival of Ethereum as a contrasting design philosophy.
- V2 CH02 still preserves the verified 2013 whitepaper → January 2014 public announcement → later funding arc.
- V2 CH03 remains compatible with the revised motivation; no downstream event or character state depends on Mt. Gox being the origin of Ethereum.

## Pass 5 status

Do not mark CH01 or CH02 `reviewed` from this document. CH01 still requires independent `historian + blind-reader`; CH02 still requires independent `continuity + character`. The CH02 queue fingerprint was updated to the new manuscript blob SHA after the edit.
