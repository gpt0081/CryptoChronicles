# Pass 5 Branch Hygiene Audit

## Purpose

Publication readiness requires that no draft PR or unfinished manuscript branch remain. This audit distinguishes an **active unfinished branch** from a **merged historical branch ref** that GitHub still retains after its PR was merged.

## Current repository state

- Open pull requests: **0**
- Draft pull requests: **0**
- Active unfinished manuscript PRs: **0**
- `main` contains all four completed volumes and all revision/art work that was merged through the recorded PR sequence.
- Independent Pass 5 review remains incomplete; this audit does not change any chapter review status.

## Retained branch refs

The repository still exposes old `write/*`, `revise/*`, `review/*`, and `art/*` branch names. They are not treated as unfinished work when their corresponding PR is already merged into `main`.

### Writing branches

- `write/volume1-ch01` → merged PR #2
- `write/volume2-act1` → merged PR #4
- `write/volume3` → merged PR #5
- `write/volume4` → merged PR #6

Volume 1's completed 12-chapter delivery was merged through PR #3 (`expand/full-series-cast-v1`), so the earlier CH01 branch is only an historical precursor.

### Revision branches

- `revise/full-series-pass1` → merged PR #7
- `revise/full-series-pass1b` → merged PR #8
- `revise/full-series-pass1c` → merged PR #9
- `revise/character-motif-pass2` → merged PR #10
- `revise/rhythm-pass3` → merged PR #11
- `revise/final-copyedit-pass4` → merged PR #12

### Review branches

The retained `review/*` refs correspond to merged Pass 5 infrastructure, audit, and internal-precheck PRs. Examples include:

- `review/pass5-narrative-loop` → merged PR #13
- `review/v1-ch01-historical-precheck` → merged PR #14
- `review/cast-dossier-completion` → merged PR #15
- `review/continuity-thread-closure` → merged PR #16
- `review/fact-ledger-coverage-audit` → merged PR #17
- `review/pass5-baseline-pinning` → merged PR #21
- `review/pass5-queue-blob-baseline` → merged PR #22
- `review/v4-ch09-ch12-precheck` → merged PR #43
- `review/pass5-final-baseline-refresh` → merged PR #46
- `review/pass5-execution-ready` → merged PR #47
- `review/pass5-wave1-dispatch` → merged PR #50
- `review/pass5-all-waves-dispatched` → merged PR #55

The chapter-specific `review/v1-*`, `review/v2-*`, `review/v3-*`, and `review/v4-*` refs likewise belong to already merged internal-precheck PRs. Their continued existence as Git refs does not represent unpublished manuscript work.

### Art branches

- `art/canonical-character-portraits` → merged PR #40
- `art/final-character-production-spec` → merged PR #44
- `art/final-character-svg-set` → merged PR #45

## Publication gate interpretation

For this project, the branch-cleanliness gate is considered satisfied when:

1. no open or draft manuscript/revision/art PR exists;
2. no branch contains intended publication work that has not been merged to `main`;
3. any remaining branch names are documented merged-history refs only.

Physical deletion of merged refs is housekeeping, not a manuscript-completeness requirement. If GitHub branch deletion becomes available, these refs may be pruned after publication without changing canon.

## Result

**Branch hygiene audit: PASS for unfinished-work detection.**

There is currently no identified unfinished manuscript, revision, review-infrastructure, or final-art branch. The project is still **not publication-ready** because the independent Pass 5 chapter review evidence remains outstanding.
