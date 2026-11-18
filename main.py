#!/usr/bin/env python3
"""news-image-20261118 entrypoint.

Copies the front-page image (entry.png, rendered by
render_frontpage.py) to the Make.fun output directory.

Runs with no network and no input: the same bytes on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        print(f"error: {SOURCE} missing", file=sys.stderr)
        return 1
    # Sanity-check the image before copying: PNG magic bytes and
    # the competition's 1 MiB size cap.
    with open(SOURCE, "rb") as fh:
        head = fh.read(8)
    if head != b"\x89PNG\r\n\x1a\n":
        print("error: entry.png is not a PNG", file=sys.stderr)
        return 1
    if os.path.getsize(SOURCE) > 1048576:
        print("error: entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    print(f"wrote {dest} ({os.path.getsize(dest)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
