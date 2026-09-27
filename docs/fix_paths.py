#!/usr/bin/env python3
"""Fix KDCN website: convert all relative paths to absolute"""

import os
import re

total_fixed = 0

for root, dirs, files in os.walk('.'):
    # Skip assets folder itself
    if 'assets' in root.split(os.sep) or 'images' in root.split(os.sep):
        continue

    for file in files:
        if not file.endswith('.html'):
            continue

        path = os.path.join(root, file)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # FIX 1: extra.css (any variant)
        content = re.sub(r'href="\.?/?extra\.css"', 'href="/extra.css"', content)

        # FIX 2: kdcn-agent.js
        content = re.sub(r'src="\.?/?assets/kdcn-agent\.js"', 'src="/assets/kdcn-agent.js"', content)

        # FIX 3: General assets/ paths
        content = re.sub(r'(?<![/\w])href="assets/', 'href="/assets/', content)
        content = re.sub(r'(?<![/\w])src="assets/', 'src="/assets/', content)
        content = re.sub(r'(?<![/\w])srcset="assets/', 'srcset="/assets/', content)

        # FIX 4: General images/ paths
        content = re.sub(r'(?<![/\w])href="images/', 'href="/images/', content)
        content = re.sub(r'(?<![/\w])src="images/', 'src="/images/', content)
        content = re.sub(r'(?<![/\w])srcset="images/', 'srcset="/images/', content)

        # FIX 5: Continuation lines in srcset (with comma+whitespace)
        content = re.sub(r',\s+assets/', ', /assets/', content)
        content = re.sub(r',\s+images/', ', /images/', content)

        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Fixed: {path}")
            total_fixed += 1

print(f"\n🎯 {total_fixed} files fixed")
