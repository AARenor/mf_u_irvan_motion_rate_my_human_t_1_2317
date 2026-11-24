"""Writes one short text for make.fun's bounty entry."""

import os
import sys

TEXT = "Five stars. He asked me to summarize his day. I wrote: argued with a toaster, lost. He said add nuance. I wrote: twice."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "text must be between 1 and 280 characters"
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
