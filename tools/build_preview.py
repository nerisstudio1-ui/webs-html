#!/usr/bin/env python3
"""Assemble dist/preview.html — a single self-contained page that plays the ad.

Built from the same src/ files the exported MP4s come from, so the page can
never drift from the video. Everything is inlined: the page has to work with no
network at all (it is published under a CSP that blocks external hosts).
"""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "dist" / "preview.html"

PARTS = ["fonts.css", "ad.css", "photos.js", "art.js", "sites.js", "ad.js", "preview.template.html"]


def main() -> int:
    missing = [p for p in PARTS if not (SRC / p).exists()]
    if missing:
        print(f"missing source files: {missing}", file=sys.stderr)
        return 1

    read = {p: (SRC / p).read_text(encoding="utf-8") for p in PARTS}

    page = "\n".join([
        "<style>",
        read["fonts.css"],
        "</style>",
        "<style>",
        read["ad.css"],
        "</style>",
        read["preview.template.html"],
        "<script>",
        read["photos.js"],
        "</script>",
        "<script>",
        read["art.js"],
        "</script>",
        "<script>",
        read["sites.js"],
        "</script>",
        "<script>",
        read["ad.js"],
        "</script>",
    ])

    # The template's own <script> runs before ad.js is defined if it stays where
    # it is written, so move it to the very end.
    marker = "<script>\n(function () {\n  const FMT_RATIO"
    if marker in page:
        start = page.index(marker)
        end = page.index("</script>", start) + len("</script>")
        block = page[start:end]
        page = page[:start] + page[end:] + "\n" + block

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
