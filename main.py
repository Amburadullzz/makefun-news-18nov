#!/usr/bin/env python3
"""Entrypoint: put the day's poster where the grader reads it.

The poster itself is drawn by render.py and committed as entry.png, so the
grading run has no work to do beyond writing those bytes to /output/entry.png.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1024 * 1024
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def output_dir():
    """MAKEFUN_OUTPUT_DIR for a local run, /output inside the sandbox."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def png_size(path):
    """Width and height, read straight out of the IHDR chunk."""
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != PNG_MAGIC:
        raise SystemExit("entry.png is not a PNG: %r" % head[:8])
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def check():
    """Refuse to hand over an image the gate would score as invalid."""
    size = os.path.getsize(SOURCE)
    width, height = png_size(SOURCE)
    if size > MAX_BYTES:
        raise SystemExit("entry.png is %d bytes, over the 1 MiB cap" % size)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit("entry.png is %dx%d, over the 1024 cap" % (width, height))
    return size, width, height


def main():
    size, width, height = check()
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.png")
    shutil.copyfile(SOURCE, target)
    print("entry.png %dx%d, %d bytes -> %s" % (width, height, size, target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
