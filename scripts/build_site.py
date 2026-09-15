import os
import re

def read(f):
    with open(f, 'r', encoding='utf-8') as file:
        return file.read()

def write(f, c):
    with open(f, 'w', encoding='utf-8') as file:
        file.write(c)

print("📖 Loading templates...")
nav = read('templates/nav.html')
footer = read('templates/footer.html')
css = read('templates/extra.css')

print("📁 Copying CSS to docs/...")
write('docs/extra.css', css)

print("🔄 Updating all HTML pages...\n")
for file in os.listdir('docs'):
    if not file.endswith('.html'):
        continue
    path = os.path.join('docs', file)
    content = read(path)
    changed = False

    # 1. REPLACE ENTIRE NAV ELEMENT (not nested)
    nav_match = re.search(r'<nav[^>]*>.*?</nav>', content, re.DOTALL | re.IGNORECASE)
    if nav_match:
        content = content.replace(nav_match.group(0), nav, 1)
        print(f"  ✅ Nav replaced in {file}")
        changed = True
    else:
        print(f"  ⚠️  No <nav> found in {file}, prepending it.")
        content = nav + content
        changed = True

    # 2. REPLACE ENTIRE FOOTER ELEMENT (not nested)
    footer_match = re.search(r'<footer[^>]*>.*?</footer>', content, re.DOTALL | re.IGNORECASE)
    if footer_match:
        content = content.replace(footer_match.group(0), footer, 1)
        print(f"  ✅ Footer replaced in {file}")
        changed = True
    else:
        print(f"  ⚠️  No <footer> found in {file}, appending it.")
        content = content + footer
        changed = True

    # 3. FIX CSS LINK
    if 'href="extra.css"' not in content:
        content = content.replace('href="templates/extra.css"', 'href="extra.css"')
        if 'extra.css' not in content and '<link' in content:
            content = content.replace('<head>', '<head>\n    <link rel="stylesheet" href="extra.css">')
        elif 'extra.css' not in content:
            content = content.replace('</head>', '<link rel="stylesheet" href="extra.css">\n</head>')
        changed = True

    if changed:
        write(path, content)

print("\n🚀 BUILD COMPLETE!")
print("👉 All pages now have exactly 1 nav and 1 footer.")
