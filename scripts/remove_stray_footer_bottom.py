import re

files = ['docs/index.html', 'docs/resources.html']

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find all <footer> blocks
    footers = list(re.finditer(r'<footer>.*?</footer>', content, flags=re.DOTALL))
    if not footers:
        continue
    # We assume the last footer is the correct one
    proper_footer = footers[-1].group(0)
    
    # Replace the proper footer with a unique token
    token = '{{PROPER_FOOTER_TOKEN}}'
    content = content.replace(proper_footer, token)
    
    # Remove all footer-bottom divs that are now outside the proper footer
    content = re.sub(r'<div class="footer-bottom[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    
    # Also remove any stray copyright divs outside the proper footer if present
    content = re.sub(r'<div class="copyright">.*?</div>', '', content, flags=re.DOTALL)
    
    # Restore the proper footer
    content = content.replace(token, proper_footer)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f'Cleaned {filepath}')
