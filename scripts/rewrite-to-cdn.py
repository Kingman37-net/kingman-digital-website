#!/usr/bin/env python3
"""
Rewrite local image references in kingman-digital-website to CDN URLs.
Usage:
  python3 scripts/rewrite-to-cdn.py --dry-run
  python3 scripts/rewrite-to-cdn.py --apply
"""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
CDN = "https://media.kingmandigital.co.ke"

# Order matters — longer / more specific keys first
MAPPING = [
    # OG/Twitter meta — full URL form
    ("https://www.kingmandigital.co.ke/images/logo-banner.png",
     f"{CDN}/website/main/logo/logo-banner.png"),

    # Covers
    ("/images/cover-home.jpg", f"{CDN}/website/main/covers/cover-home.jpg"),
    ("/images/cover-page.jpg", f"{CDN}/website/main/covers/cover-page.jpg"),

    # Logos — specific first, then general
    ("/images/logo-transparent.png", f"{CDN}/website/main/logo/logo-transparent.png"),
    ("/images/logo-small.png",       f"{CDN}/website/main/logo/logo-small.png"),
    ("/images/logo-square.png",      f"{CDN}/website/main/logo/logo-square.png"),
    ("/images/logo-banner.png",      f"{CDN}/website/main/logo/logo-banner.png"),
    ("/images/logo-wide.jpg",        f"{CDN}/website/main/logo/logo-wide.jpg"),
    ("/images/logo.png",             f"{CDN}/website/main/logo/logo.png"),

    # Icons — all 12
    ("/images/icons/domain.png",     f"{CDN}/icons/domain.png"),
    ("/images/icons/email.png",      f"{CDN}/icons/email.png"),
    ("/images/icons/facebook.png",   f"{CDN}/icons/facebook.png"),
    ("/images/icons/github.png",     f"{CDN}/icons/github.png"),
    ("/images/icons/instagram.png",  f"{CDN}/icons/instagram.png"),
    ("/images/icons/legal.png",      f"{CDN}/icons/legal.png"),
    ("/images/icons/linkedin.png",   f"{CDN}/icons/linkedin.png"),
    ("/images/icons/phone.png",      f"{CDN}/icons/phone.png"),
    ("/images/icons/tiktok.png",     f"{CDN}/icons/tiktok.png"),
    ("/images/icons/whatsapp.png",   f"{CDN}/icons/whatsapp.png"),
    ("/images/icons/x.png",          f"{CDN}/icons/x.png"),
    ("/images/icons/youtube.png",    f"{CDN}/icons/youtube.png"),
]


def main():
    dry = "--dry-run" in sys.argv
    apply = "--apply" in sys.argv

    if not (dry or apply):
        print("Usage: rewrite-to-cdn.py [--dry-run | --apply]")
        return 1

    html_files = sorted(DOCS.rglob("*.html"))
    print(f"▶ Scanning {len(html_files)} HTML files")
    print()

    total = 0
    changed = 0
    per_file = {}

    for path in html_files:
        original = path.read_text(encoding="utf-8")
        content = original
        hits = 0
        for old, new in MAPPING:
            c = content.count(old)
            if c:
                content = content.replace(old, new)
                hits += c

        if hits:
            per_file[path] = hits
            total += hits
            changed += 1
            rel = path.relative_to(REPO)
            print(f"  {hits:>3}  {rel}")
            if apply:
                path.write_text(content, encoding="utf-8")

    print()
    print(f"▶ Files changed:      {changed}")
    print(f"▶ Total replacements: {total}")
    print()
    print("✅ Dry run complete — no files written" if dry else "✅ Changes applied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
