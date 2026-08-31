#!/usr/bin/env python3

from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TEMPLATE = ROOT / "templates" / "footer.html"

if not TEMPLATE.exists():
    print("ERROR: templates/footer.html not found")
    sys.exit(1)

footer = TEMPLATE.read_text(encoding="utf-8").strip()

if footer.count("<footer") != 1 or footer.count("</footer>") != 1:
    print("ERROR: Footer template must contain exactly one <footer> and one </footer>")
    sys.exit(1)

html_files = sorted(DOCS.glob("*.html"))

changed = []
skipped = []

for path in html_files:
    text = path.read_text(encoding="utf-8")

    matches = list(re.finditer(r"<footer\b[^>]*>.*?</footer>", text, re.IGNORECASE | re.DOTALL))

    if len(matches) == 0:
        skipped.append((path.name, "NO FOOTER"))
        continue

    if len(matches) > 1:
        skipped.append((path.name, f"MULTIPLE FOOTERS ({len(matches)})"))
        continue

    new_text = text[:matches[0].start()] + footer + text[matches[0].end():]

    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        changed.append(path.name)

print("======================================")
print("       KDCN FOOTER V2 DEPLOYMENT")
print("======================================")
print(f"HTML pages found : {len(html_files)}")
print(f"Pages updated    : {len(changed)}")
print(f"Pages skipped    : {len(skipped)}")

if changed:
    print("\nUPDATED:")
    for name in changed:
        print(f"  ✓ {name}")

if skipped:
    print("\nSKIPPED:")
    for name, reason in skipped:
        print(f"  ! {name} — {reason}")

print("\nFooter template validation:")
print("  <footer>  :", footer.count("<footer"))
print("  </footer> :", footer.count("</footer>"))

if skipped:
    print("\nWARNING: Some pages require manual review.")
    sys.exit(2)

print("\nSUCCESS: Footer V2 applied to all HTML pages.")
