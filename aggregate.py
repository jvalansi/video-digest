#!/usr/bin/env python3
"""
Aggregator — runs all fetchers, merges output, deduplicates, and ranks by engagement.

Usage:
  python aggregate.py [--limit N] [--output FILE]

Output: JSON array of top N deduplicated items, sorted by engagement.
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

FETCHERS_DIR = os.path.join(os.path.dirname(__file__), "fetchers")
PYTHON = sys.executable

FETCHERS = [
    {"cmd": ["python", "fetchers/rss.py", "--limit", "20"]},
    {"cmd": ["python", "fetchers/hn.py", "--feed", "top", "--limit", "30"]},
    {"cmd": ["python", "fetchers/youtube.py", "--mode", "channels", "--limit", "5"]},
    {"cmd": ["python", "fetchers/github.py", "--limit", "25"]},
]


def run_fetcher(cmd: list[str]) -> list[dict]:
    result = subprocess.run(
        [PYTHON if c == "python" else c for c in cmd],
        capture_output=True, text=True, cwd=os.path.dirname(__file__)
    )
    if result.stderr:
        for line in result.stderr.strip().splitlines():
            print(f"  {line}", file=sys.stderr)
    if result.returncode != 0:
        print(f"  ERROR running {cmd[1]}: {result.stderr[-200:]}", file=sys.stderr)
        return []
    return json.loads(result.stdout)


def deduplicate(items: list[dict]) -> list[dict]:
    """Remove near-duplicate items by comparing lowercased title words."""
    seen = []
    unique = []
    for item in items:
        words = set(item["title"].lower().split())
        # Consider duplicate if >60% of words overlap with an existing item
        is_dup = any(
            len(words & s) / max(len(words | s), 1) > 0.6
            for s in seen
        )
        if not is_dup:
            seen.append(words)
            unique.append(item)
    return unique


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=20, help="Top N items to return (default: 20)")
    parser.add_argument("--output", help="Write output to FILE instead of stdout")
    args = parser.parse_args()

    all_items = []
    for fetcher in FETCHERS:
        print(f"\n[{fetcher['cmd'][1]}]", file=sys.stderr)
        items = run_fetcher(fetcher["cmd"])
        all_items.extend(items)
        print(f"  Subtotal: {len(all_items)} items", file=sys.stderr)

    print(f"\nTotal before dedup: {len(all_items)}", file=sys.stderr)
    unique = deduplicate(all_items)
    print(f"After dedup: {len(unique)}", file=sys.stderr)

    ranked = sorted(unique, key=lambda x: x.get("engagement", 0), reverse=True)
    top = ranked[:args.limit]

    output = json.dumps(top, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"\nWrote {len(top)} items to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
