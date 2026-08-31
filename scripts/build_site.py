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

    # 1. REPLACE NAV (first <nav> tag)
    nav_match = re.search(r'(<\s*nav[^>]*>)(.*?)(<\s*\/\s*nav>)', content, re.DOTALL | re.IGNORECASE)
    if nav_match:
        new_nav_block = nav_match.group(1) + nav + nav_match.group(3)
        content = content.replace(nav_match.group(0), new_nav_block)
        print(f"  ✅ Nav replaced in {file}")
        changed = True
    else:
        print(f"  ⚠️ No <nav> found in {file}, prepending it.")
        content = nav + content
        changed = True

    # 2. REPLACE FOOTER (first <footer> tag)
    footer_match = re.search(r'(<\s*footer[^>]*>)(.*?)(<\s*\/\s*footer>)', content, re.DOTALL | re.IGNORECASE)
    if footer_match:
        new_footer_block = footer_match.group(1) + footer + footer_match.group(3)
        content = content.replace(footer_match.group(0), new_footer_block)
        print(f"  ✅ Footer replaced in {file}")
        changed = True
    else:
        print(f"  ⚠️ No <footer> found in {file}, appending it.")
        content = content + footer
        changed = True

    # 3. FIX CSS LINK (point to docs/root)
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
print("👉 Now open http://localhost:8000 in your browser.")
print("👉 Press Ctrl+Shift+R (or pull to refresh) to clear cache.")
