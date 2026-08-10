#!/usr/bin/env python3
"""Inline src/ad.html into a single self-contained dist/ad.html.

Useful when the ad needs to travel as one file — a preview link, an email to a
client, an upload to a host that will not serve the sibling assets. The fonts
are already base64 data URIs by the time build_fonts.py is done, so this is a
straight substitution of every local <link> and <script src>.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "dist" / "ad.html"


def main() -> int:
    page = SRC / "ad.html"
    if not page.exists():
        print(f"missing {page}", file=sys.stderr)
        return 1

    html = page.read_text(encoding="utf-8")

    def inline_css(match: re.Match) -> str:
        name = match.group(1)
        path = SRC / name
        if not path.exists():
            return match.group(0)
        return f"<style>\n{path.read_text(encoding='utf-8')}\n</style>"

    def inline_js(match: re.Match) -> str:
        name = match.group(1)
        path = SRC / name
        if not path.exists():
            return match.group(0)
        return f"<script>\n{path.read_text(encoding='utf-8')}\n</script>"

    html = re.sub(r'<link rel="stylesheet" href="([^"/:]+)">', inline_css, html)
    html = re.sub(r'<script src="([^"/:]+)"></script>', inline_js, html)

    remaining = re.findall(r'(?:href|src)="([^"#:]+\.(?:css|js))"', html)
    if remaining:
        print(f"warning: still referencing {remaining}", file=sys.stderr)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
