#!/usr/bin/env python3
"""Build the locally captured Framer export as a static Vercel-ready site."""

from __future__ import annotations

import hashlib
import html
import re
import shutil
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "download" / "framerusercontent.com"
PAGE = ROOT / "download" / "www.missingpieceinvites.com" / "demos" / "city-2-local.html"
DIST = ROOT / "dist"
PREFIX = "/framerusercontent.com/"
LOCAL_ORIGINS = ("http://127.0.0.1:8000", "http://localhost:8000", "https://framerusercontent.com")


def normalized_assets() -> dict[str, str]:
    """Map Framer URLs to deterministic, query-free filenames in dist."""
    mapping: dict[str, str] = {}
    for source in SOURCE.rglob("*"):
        if not source.is_file() or "?" not in source.name:
            continue
        base, query = source.name.split("?", 1)
        digest = hashlib.sha256(query.encode()).hexdigest()[:10]
        stem, dot, suffix = base.rpartition(".")
        normalized = f"{stem}__{digest}.{suffix}" if dot else f"{base}__{digest}"
        mapping[source.relative_to(SOURCE).as_posix()] = PREFIX + source.relative_to(SOURCE).parent.as_posix() + "/" + normalized
    # Some SSR fallback URLs omit the Framer query even though the captured
    # file on disk includes one. Point those fallbacks at a deterministic
    # unqueried copy of the largest captured variant.
    by_name: dict[str, list[Path]] = {}
    for source in SOURCE.rglob("*"):
        if source.is_file() and "?" in source.name:
            base = source.name.split("?", 1)[0]
            by_name.setdefault((source.parent / base).relative_to(SOURCE).as_posix(), []).append(source)
    for relative, variants in by_name.items():
        source = max(sorted(variants), key=lambda item: item.stat().st_size)
        mapping[relative] = mapping[source.relative_to(SOURCE).as_posix()]
    return mapping


def rewrite_references(content: str, mapping: dict[str, str]) -> str:
    """Rewrite captured origins and query-string disk names to static paths."""
    # HTML commonly entity-escapes ampersands while JavaScript does not.
    for local in LOCAL_ORIGINS:
        content = content.replace(local + "/framerusercontent.com/", PREFIX)
    content = re.sub(r"https?://(?:www\.)?missingpieceinvites\.com/assets/", PREFIX + "assets/", content)

    # Asset disk names include their Framer query string. Use the URL up to
    # whitespace/quotes; compare both the raw and HTML-decoded representations.
    pattern = re.compile(r"(?:/framerusercontent\.com/|framerusercontent\.com/)[^\s\"'<>`)]+")

    def replace(match: re.Match[str]) -> str:
        raw = match.group(0)
        leading = "/" if raw.startswith("/") else ""
        path = raw.lstrip("/")
        decoded = html.unescape(unquote(path))
        # Only image/font/audio files are query-bearing in this export.
        candidate = decoded
        if candidate.startswith("framerusercontent.com/"):
            candidate = candidate[len("framerusercontent.com/"):]
        target = mapping.get(candidate)
        if not target:
            return raw
        return target

    return pattern.sub(replace, content)


def build() -> None:
    if not PAGE.is_file() or not SOURCE.is_dir():
        raise SystemExit("Expected active page and Framer assets were not found.")
    if DIST.exists():
        shutil.rmtree(DIST)
    (DIST / "demos").mkdir(parents=True)
    assets = normalized_assets()

    # Copy every captured Framer asset and module. Backups are not runtime imports.
    def ignore_backups(_directory: str, names: list[str]) -> set[str]:
        return {name for name in names if ".bak" in name}

    shutil.copytree(SOURCE, DIST / "framerusercontent.com", ignore=ignore_backups)
    for relative, target in assets.items():
        original = SOURCE / relative
        if not original.is_file():
            # Queryless fallback mapping uses the largest captured variant.
            base = original.name
            original = max(
                sorted(SOURCE.glob(str(Path(relative).with_name(base + "?*")))),
                key=lambda item: item.stat().st_size,
            )
        destination = ROOT / "dist" / target.lstrip("/")
        destination.parent.mkdir(parents=True, exist_ok=True)
        if not destination.exists():
            shutil.copy2(original, destination)
        # The source filename with literal query marks is deliberately absent
        # from the deploy tree; all references point at the normalized copy.

    for path in (DIST / "framerusercontent.com").rglob("*"):
        if path.is_file() and "?" in path.name:
            path.unlink()

    # Framer modules embed absolute asset URLs in addition to relative imports.
    for path in (DIST / "framerusercontent.com").rglob("*"):
        if path.is_file() and path.suffix.lower() in {".mjs", ".json", ".css"}:
            path.write_text(rewrite_references(path.read_text(encoding="utf-8"), assets), encoding="utf-8")

    page = rewrite_references(PAGE.read_text(encoding="utf-8"), assets)
    page = page.replace('href="https://www.missingpieceinvites.com/demos/city-2"', 'href="/demos/city-2/"')
    page = page.replace('content="https://www.missingpieceinvites.com/demos/city-2"', 'content="/demos/city-2/"')
    (DIST / "index.html").write_text(page, encoding="utf-8")
    (DIST / "demos" / "city-2" ).mkdir(parents=True)
    (DIST / "demos" / "city-2" / "index.html").write_text(page, encoding="utf-8")
    print(f"Built {len(assets)} query-string assets into dist/ with root and /demos/city-2/ routes.")


if __name__ == "__main__":
    build()
