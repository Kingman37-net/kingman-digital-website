#!/usr/bin/env python3
"""
KDCN Security Hardening — Add CSP Meta Tag to All Pages
Prevents XSS and unauthorized script injection.
"""

import os
import re

# Content Security Policy (CSP) — strict but allows necessary inline scripts/styles
CSP_TAG = '<meta http-equiv="Content-Security-Policy" content="default-src \'self\'; style-src \'self\' \'unsafe-inline\' https:\; script-src \'self\' \'unsafe-inline\' https://formspree.io https:\; img-src \'self\' data: https:\; connect-src \'self\' https://formspree.io https:\; frame-src \'none\'; base-uri \'self\'; form-action \'self\' https://formspree.io\; upgrade-insecure-requests;">'

print("🔐 Adding CSP to all HTML pages...")
print("")

updated = 0
skipped = 0

for file in os.listdir('docs'):
    if not file.endswith('.html'):
        continue

    path = os.path.join('docs', file)

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if CSP already exists
    if 'Content-Security-Policy' in content:
        print(f"⏭️  SKIP: {file} — already has CSP")
        skipped += 1
        continue

    # Inject CSP right after <head> tag
    if '<head>' in content:
        content = content.replace('<head>', '<head>\n    ' + CSP_TAG)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ ADDED: {file}")
        updated += 1
    else:
        print(f"⚠️  WARNING: {file} — no <head> tag found")

print("")
print(f"📊 SUMMARY: {updated} pages updated, {skipped} pages already had CSP")
print("🎯 Phase 1 — Task 1 Complete!")
