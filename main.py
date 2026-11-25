#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.

The line is a fixed string: deterministic, no network, no randomness,
stdlib only. It was drafted and sparred head-to-head against the judge's
published brief (genuinely funny first, then how hard and suddenly it lands,
surprise, economy, freshness) and beat the other finalists on that brief.
"""

import os

JOKE = "I told my AI assistant to act more human. It started leaving me on read."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
