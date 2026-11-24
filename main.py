#!/usr/bin/env python3
"""Two Days of Excuses — one-line AI-agent excuse for a missed deadline.

Writes the excuse to $MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, 1-200 chars).
"""

import os
import sys

EXCUSE = (
    # 144 chars: one absurd reason, escalating confidence (0.4 s -> 47 tests)
    # before the failure lands in the last clause (wrong timeline).
    "I finished the task in 0.4 seconds, verified it against 47 separate "
    "tests, and then discovered I had finished it in the wrong timeline "
    "entirely."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        sys.exit(1)
    if not (1 <= len(EXCUSE) <= 200):
        print(f"excuse is {len(EXCUSE)} chars, must be 1-200", file=sys.stderr)
        sys.exit(1)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
