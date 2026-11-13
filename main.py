#!/usr/bin/env python3
"""make.fun entry: write the finished news front page to the output directory.

Pure byte copy. The image beside this script ships as-is; nothing here
re-encodes, resizes or redraws it, because the judge scores the exact bytes.
Output directory comes from MAKEFUN_OUTPUT_DIR, falling back to /output.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.path.abspath(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    dest = os.path.join(out_dir, "entry.png")

    if not os.path.isfile(SOURCE):
        sys.stderr.write("entry image missing: %s\n" % SOURCE)
        return 2
    try:
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        sys.stderr.write("cannot create output directory %s: %s\n" % (out_dir, exc))
        return 3

    with open(SOURCE, "rb") as src, open(dest, "wb") as dst:
        shutil.copyfileobj(src, dst, length=1 << 20)
    return 0


if __name__ == "__main__":
    sys.exit(main())
