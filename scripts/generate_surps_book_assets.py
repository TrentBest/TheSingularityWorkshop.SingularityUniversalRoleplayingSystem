#!/usr/bin/env python3
"""Generate deterministic SURPS book publication assets from a book descriptor.

The descriptor is authoritative. This generator never invents attribution or
publication approval; missing acknowledgement data is stated transparently.
"""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONIKER = "https://raw.githubusercontent.com/TrentBest/TheSingularityWorkshop.Visualize/development/docs/assets/moniker.svg"


def read_descriptor(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    required = ("id", "category", "lod", "title", "version", "publisher", "coverArtwork", "cover", "lodBadge", "acknowledgementsPath")
    missing = [key for key in required if not value.get(key)]
    if missing:
        raise ValueError(f"{path}: missing required descriptor fields: {', '.join(missing)}")
    if not isinstance(value["lod"], int) or isinstance(value["lod"], bool) or value["lod"] < 0:
        raise ValueError(f"{path}: lod must be a non-negative integer")
    return value


def relative_asset(source: Path, target: Path) -> str:
    return Path(__import__("os").path.relpath(source, target.parent)).as_posix()


def render_cover(book: dict, descriptor_path: Path) -> str:
    cover_path = ROOT / book["cover"]
    art_path = ROOT / book["coverArtwork"]
    if not art_path.is_file():
        raise FileNotFoundError(f"{descriptor_path}: coverArtwork does not exist: {book['coverArtwork']}")
    art_href = html.escape(relative_asset(art_path, cover_path), quote=True)
    badge_path = ROOT / book["lodBadge"]
    if not badge_path.is_file():
        raise FileNotFoundError("Missing LOD badge: " + book["lodBadge"])
    badge_href = html.escape(relative_asset(badge_path, cover_path), quote=True)
    title = html.escape(book["title"])
    category = html.escape(book["category"].upper())
    publisher = html.escape(book["publisher"])
    version = html.escape(book["version"])
    canonical = html.escape(f"Singularity Universal Roleplaying System - {book['category']} - LOD {book['lod']} - {book['title']}")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="900" height="1200" viewBox="0 0 900 1200" role="img" aria-labelledby="cover-title cover-desc">
<title id="cover-title">{canonical}</title>
<desc id="cover-desc">{publisher} publication cover for {title}, {category} category, Level of Detail {book["lod"]}, edition {version}. Subject artwork is shown in the central panel.</desc>
<defs>
 <linearGradient id="ground" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#101b2b"/><stop offset=".55" stop-color="#1d3449"/><stop offset="1" stop-color="#090f19"/></linearGradient>
 <linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#f0d6a0"/><stop offset=".5" stop-color="#bd9862"/><stop offset="1" stop-color="#806746"/></linearGradient>
 <pattern id="grid" width="44" height="44" patternUnits="userSpaceOnUse"><path d="M44 0H0V44" fill="none" stroke="#9fb4c7" stroke-opacity=".08"/></pattern>
 <clipPath id="art-clip"><rect x="74" y="310" width="752" height="610" rx="8"/></clipPath>
</defs>
<rect width="900" height="1200" fill="url(#ground)"/>
<rect width="900" height="1200" fill="url(#grid)"/>
<path d="M36 36H864V1164H36Z" fill="none" stroke="url(#metal)" stroke-width="2"/>
<path d="M58 58H842V1142H58Z" fill="none" stroke="#d8c39e" stroke-opacity=".22"/>
<path d="M74 238H826" stroke="url(#metal)" stroke-width="3"/>
<text x="450" y="112" fill="#f1d8a7" font-family="Georgia,serif" font-size="19" letter-spacing="6" text-anchor="middle">{publisher.upper()}</text>
<text x="450" y="165" fill="#ffffff" font-family="Georgia,serif" font-size="30" letter-spacing="3" text-anchor="middle">SINGULARITY UNIVERSAL</text>
<text x="450" y="205" fill="#ffffff" font-family="Georgia,serif" font-size="30" letter-spacing="3" text-anchor="middle">ROLEPLAYING SYSTEM</text>
<text x="450" y="278" fill="#e8c994" font-family="Arial,sans-serif" font-size="18" font-weight="700" letter-spacing="5" text-anchor="middle">{category}  ·  LEVEL OF DETAIL {book["lod"]}</text>
<rect x="70" y="306" width="760" height="618" rx="12" fill="#050b12" stroke="url(#metal)" stroke-width="2"/>
<g clip-path="url(#art-clip)"><image x="74" y="310" width="752" height="610" preserveAspectRatio="xMidYMid slice" href="{art_href}" xlink:href="{art_href}"/></g>
<path d="M74 950H826" stroke="url(#metal)" stroke-width="3"/>
<image x="330" y="960" width="240" height="72" href="{badge_href}" xlink:href="{badge_href}"/>
<text x="450" y="1025" fill="#ffffff" font-family="Georgia,serif" font-size="58" font-weight="bold" text-anchor="middle">{title}</text>
<text x="450" y="1076" fill="#c4d0db" font-family="Arial,sans-serif" font-size="18" letter-spacing="4" text-anchor="middle">A LIVING {category} BOOK</text>
<text x="450" y="1120" fill="#e8c994" font-family="Arial,sans-serif" font-size="15" letter-spacing="2" text-anchor="middle">EDITION {version}</text>
</svg>
'''


def render_acknowledgements(book: dict) -> str:
    lines = [
        "# Acknowledgements",
        "",
        f"**{book['title']}** · Edition {book['version']}",
        "",
        "This page is generated from the book descriptor. It records supplied attribution; it does not infer authorship or permission.",
        "",
    ]
    contributors = book.get("contributors", [])
    if contributors:
        for person in contributors:
            name = str(person.get("name", "")).strip()
            role = str(person.get("role", "Contributor")).strip()
            if name:
                lines.append(f"- **{name}** — {role}")
    else:
        lines.append("No additional contributor acknowledgements have been recorded for this edition.")
    acknowledgements = book.get("acknowledgements", [])
    if acknowledgements:
        lines.extend(["", "## With thanks", ""])
        for item in acknowledgements:
            if isinstance(item, str):
                lines.append(f"- {item}")
            else:
                lines.append(f"- **{item.get('name', 'Contributor')}** — {item.get('note', '')}")
    rights = book.get("rights")
    if rights:
        lines.extend(["", "## Rights and permissions", "", str(rights)])
    provenance = book.get("provenance")
    if isinstance(provenance, dict) and provenance:
        lines.extend(["", "## Provenance", ""])
        for key in ("sourceRepository", "sourcePath", "sourceCommit", "artworkLicense"):
            if provenance.get(key):
                lines.append(f"- **{key}:** {provenance[key]}")
    lines.extend(["", "---", "", f"*Generated by SURPS book publishing tools. Generator version: 0.1.0.*", ""])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated files are stale")
    parser.add_argument("--descriptor", action="append", help="descriptor path; defaults to opted-in descriptors in participation.json")
    args = parser.parse_args()
    manifest_path = ROOT / ".surps" / "participation.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    paths = args.descriptor or [entry["descriptorPath"] for entry in manifest.get("books", []) if entry.get("publication", {}).get("generate", False)]
    if not paths:
        print("No books have opted in to generated publication assets.")
        return 0
    stale = []
    for relative in sorted(paths):
        descriptor_path = ROOT / relative
        book = read_descriptor(descriptor_path)
        outputs = {
            ROOT / book["cover"]: render_cover(book, descriptor_path),
            ROOT / book["acknowledgementsPath"]: render_acknowledgements(book),
        }
        for path, expected in outputs.items():
            if args.check:
                if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                    stale.append(path.relative_to(ROOT).as_posix())
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(expected, encoding="utf-8", newline="\n")
                print(f"Generated {path.relative_to(ROOT)}")
    if stale:
        print("Generated publication assets are stale: " + ", ".join(stale))
        return 1
    if args.check:
        print(f"Generated publication assets are current for {len(paths)} opted-in book(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
