#!/usr/bin/env python3
import os
import re

THEME_SCRIPT = '''
<script>
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            navMenu.classList.toggle('active');
        });
    }
    const toggle = document.getElementById('theme-toggle');
    if (localStorage.getItem('theme') === 'light') {
        document.body.classList.add('light');
        toggle.textContent = '☀️';
    }
    toggle.addEventListener('click', () => {
        document.body.classList.toggle('light');
        const isLight = document.body.classList.contains('light');
        localStorage.setItem('theme', isLight ? 'light' : 'dark');
        toggle.textContent = isLight ? '☀️' : '🌙';
    });
</script>
'''

# Pages that should have the theme toggle
legal_pages = [
    'docs/privacy.html',
    'docs/terms.html',
    'docs/security.html',
    'docs/cookies.html',
    'docs/cookie-preferences.html'
]

for page in legal_pages:
    if not os.path.exists(page):
        continue
    with open(page, 'r') as f:
        content = f.read()
    if 'theme-toggle' not in content:
        # Find the closing body tag and insert the script before it
        content = content.replace('</body>', THEME_SCRIPT + '\n</body>')
        with open(page, 'w') as f:
            f.write(content)
        print(f"✅ Added theme toggle to {page}")
    else:
        print(f"✅ {page} already has theme toggle")

print("\n🎯 All legal pages now have the theme toggle!")
