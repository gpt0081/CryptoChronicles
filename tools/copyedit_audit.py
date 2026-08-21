#!/usr/bin/env python3
"""Copyedit audit for CryptoChronicles Markdown manuscript.

This tool never rewrites prose. It reports likely publication-style inconsistencies
so a human/editor can decide whether each occurrence is intentional.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VOLUME_DIRS = [ROOT / f"{n:02d}_VOLUME_{n-3}" for n in range(4, 8)]

# English generic terms that COPYEDIT_STYLE recommends rendering in Korean prose.
SOFT_PATTERNS: list[tuple[str, re.Pattern[str], str]] = [
    ("english-protocol", re.compile(r"\bprotocol\b", re.I), "프로토콜"),
    ("english-stablecoin", re.compile(r"\bstablecoins?\b", re.I), "일반 개념은 스테이블코인, 캐릭터만 Stablecoins"),
    ("english-mainnet", re.compile(r"\bmainnet\b", re.I), "메인넷 또는 공식 고유명사 여부 확인"),
    ("english-validator", re.compile(r"\bvalidators?\b", re.I), "검증자"),
    ("english-miner", re.compile(r"\bminers?\b", re.I), "채굴자"),
    ("english-sequencer", re.compile(r"\bsequencers?\b", re.I), "시퀀서"),
    ("english-bridge", re.compile(r"\bbridges?\b", re.I), "브리지"),
    ("english-oracle", re.compile(r"\boracles?\b", re.I), "오라클"),
    ("english-custody", re.compile(r"\bcustody\b", re.I), "수탁"),
    ("english-transaction", re.compile(r"\btransactions?\b", re.I), "거래 또는 트랜잭션"),
    ("english-tokenized", re.compile(r"\btokenized\b", re.I), "토큰화된"),
    ("english-onchain", re.compile(r"\bon[- ]?chain\b", re.I), "온체인"),
    ("english-offchain", re.compile(r"\boff[- ]?chain\b", re.I), "오프체인"),
    ("dollar-symbol", re.compile(r"\$\s?\d"), "본문은 20,000달러 형식을 우선"),
    ("research-number", re.compile(r"\b\d+(?:\.\d+)?\s?(?:bn|m)\b", re.I), "조사노트식 bn/m 표기 여부 확인"),
]

HEADING_RE = re.compile(r"^# 제\d+장 — .+$")


def markdown_files() -> list[Path]:
    files: list[Path] = []
    for directory in VOLUME_DIRS:
        if directory.exists():
            files.extend(sorted(directory.glob("CH*.md")))
    return files


def iter_lines(text: str):
    for number, line in enumerate(text.splitlines(), start=1):
        yield number, line


def audit_file(path: Path) -> tuple[list[str], list[str]]:
    hard: list[str] = []
    soft: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    rel = path.relative_to(ROOT).as_posix()

    if not lines or not HEADING_RE.match(lines[0].strip()):
        hard.append(f"{rel}:1 [heading] expected '# 제N장 — 제목'")

    # Pass 3 intentionally preserved V1-C01's different scene divider.
    allow_dash_divider = rel == "04_VOLUME_1/CH01_신뢰가_멈춘_날.md"

    for lineno, line in iter_lines(text):
        stripped = line.strip()
        if stripped == "---" and not allow_dash_divider:
            soft.append(f"{rel}:{lineno} [divider] '---' 사용. 장면 전환은 기본적으로 '***'")

        for code, pattern, suggestion in SOFT_PATTERNS:
            if pattern.search(line):
                # Stablecoins is a canonical character name, not a generic-term error.
                if code == "english-stablecoin" and "Stablecoins" in line:
                    without_character = line.replace("Stablecoins", "")
                    if not pattern.search(without_character):
                        continue
                # Official proper names remain in English.
                if code == "english-mainnet" and "Mainnet Beta" in line:
                    continue
                if code == "english-offchain" and "Off-Chain Reporting" in line:
                    continue
                soft.append(f"{rel}:{lineno} [{code}] {line.strip()} -> {suggestion}")

    # V4 must not use a floating publication cutoff in expository date statements.
    if rel.startswith("07_VOLUME_4/"):
        for lineno, line in iter_lines(text):
            if re.search(r"\b현재\b", line) and "현재" in line:
                soft.append(f"{rel}:{lineno} [floating-current] 기준일이 필요한 '현재' 표현인지 확인")

    return hard, soft


def main() -> int:
    files = markdown_files()
    if len(files) != 48:
        print(f"HARD: expected 48 chapter files, found {len(files)}", file=sys.stderr)
        return 2

    all_hard: list[str] = []
    all_soft: list[str] = []
    for path in files:
        hard, soft = audit_file(path)
        all_hard.extend(hard)
        all_soft.extend(soft)

    print(f"Checked {len(files)} chapter files")
    print(f"Hard issues: {len(all_hard)}")
    print(f"Soft warnings: {len(all_soft)}")

    if all_hard:
        print("\n[HARD ISSUES]")
        print("\n".join(all_hard))
    if all_soft:
        print("\n[SOFT WARNINGS]")
        print("\n".join(all_soft))

    # Only structural errors fail CI. Soft copyedit items require human judgment.
    return 1 if all_hard else 0


if __name__ == "__main__":
    raise SystemExit(main())
