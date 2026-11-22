#!/usr/bin/env python3
"""Check generated HTML and local references before deployment."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
LOCALHOST = re.compile(r"(?:localhost|127\.0\.0\.1):8000", re.I)
URL = re.compile(r"(?:https?://[^\s\"'<>`)]+|/[^\s\"'<>`)]+)")
IMPORT = re.compile(r"(?:from\s*|import\s*)[\"'](\.{1,2}/[^\"']+)[\"']")


def check() -> int:
    if not DIST.is_dir():
        print("dist/ is missing; run python3 scripts/build_site.py first", file=sys.stderr)
        return 1
    failures: list[str] = []
    pages = [DIST / "index.html", DIST / "demos/city-2/index.html"]
    for page in pages:
        if not page.is_file():
            failures.append(f"Missing route output: {page.relative_to(ROOT)}")
            continue
        source = page.read_text(encoding="utf-8")
        if LOCALHOST.search(source):
            failures.append(f"Localhost URL remains in {page.relative_to(ROOT)}")
        for raw in URL.findall(source):
            url = html.unescape(raw)
            split = urlsplit(url)
            if split.scheme and split.scheme not in {"http", "https"}:
                continue
            if split.scheme and split.netloc not in {"", "127.0.0.1:8000", "localhost:8000", "framerusercontent.com", "www.missingpieceinvites.com", "missingpieceinvites.com"}:
                continue
            if split.scheme and split.netloc:
                path = split.path
            else:
                path = split.path
            # Only check site-local absolute paths and captured Framer resources.
            if not path.startswith("/framerusercontent.com/"):
                continue
            target = DIST / unquote(path.lstrip("/"))
            if not target.is_file():
                failures.append(f"Missing local asset {path} referenced by {page.relative_to(ROOT)}")
    for path in DIST.rglob("*"):
        if path.is_file() and "?" in path.name:
            failures.append(f"Unnormalized query-string filename: {path.relative_to(DIST)}")
        if path.suffix.lower() in {".html", ".mjs", ".css", ".json"}:
            text = path.read_text(encoding="utf-8", errors="replace")
            if LOCALHOST.search(text):
                failures.append(f"Localhost URL remains in {path.relative_to(DIST)}")
            if path.suffix.lower() == ".mjs":
                for imported in IMPORT.findall(text):
                    target = (path.parent / unquote(imported.split("?", 1)[0])).resolve()
                    if not target.is_file():
                        failures.append(f"Missing module import {imported} in {path.relative_to(DIST)}")
            for raw in URL.findall(text):
                split = urlsplit(html.unescape(raw))
                if split.path.startswith("/framerusercontent.com/"):
                    target = DIST / unquote(split.path.lstrip("/"))
                    if not target.is_file():
                        failures.append(f"Missing local asset {split.path} referenced by {path.relative_to(DIST)}")
    if failures:
        print("\n".join(f"FAIL: {message}" for message in failures), file=sys.stderr)
        return 1
    print(f"Checked {len(pages)} routes and {sum(1 for p in DIST.rglob('*') if p.is_file())} output files; no missing local Framer references or localhost URLs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
