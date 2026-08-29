import os, re
from urllib.parse import urlparse, unquote

DOCS = 'docs'
missing = []

def check_path(path):
    """Return True if path exists relative to docs."""
    full = os.path.join(DOCS, path)
    return os.path.exists(full)

# Regex for href and src attributes
href_re = re.compile(r'href="([^"]+)"')
src_re = re.compile(r'src="([^"]+)"')

for filename in os.listdir(DOCS):
    if not filename.endswith('.html'):
        continue
    filepath = os.path.join(DOCS, filename)
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check hrefs
    for match in href_re.finditer(content):
        url = match.group(1)
        # Skip external URLs, mailto, tel, javascript, and pure anchors
        if url.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', '#')):
            continue
        # Skip pure anchor links (start with #)
        if url.startswith('#'):
            continue
        # Strip query string and fragment
        path_part = unquote(url.split('#')[0].split('?')[0])
        if path_part and not check_path(path_part):
            missing.append(f'{filename}: href="{url}" -> missing file "{path_part}"')
    
    # Check srcs
    for match in src_re.finditer(content):
        url = match.group(1)
        # Skip external or data URIs
        if url.startswith(('http://', 'https://', 'data:')):
            continue
        path_part = unquote(url.split('#')[0].split('?')[0])
        if path_part and not check_path(path_part):
            missing.append(f'{filename}: src="{url}" -> missing file "{path_part}"')

if missing:
    print("MISSING ASSETS FOUND:")
    for item in missing:
        print(' ', item)
else:
    print("All internal links and assets are valid.")
