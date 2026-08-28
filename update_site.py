import re
import os

# Read the new nav and footer HTML
with open('nav.html', 'r') as f:
    nav_html = f.read().strip()
with open('footer.html', 'r') as f:
    footer_html = f.read().strip()
with open('extra.css', 'r') as f:
    extra_css = f.read().strip()

# Get list of html files (excluding nav.html, footer.html)
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f not in ['nav.html', 'footer.html']]

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()
    
    # Replace nav block
    # Pattern: <nav> ... </nav> with possible multiline
    content = re.sub(r'<nav>.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    # Replace footer block
    content = re.sub(r'<footer>.*?</footer>', footer_html, content, flags=re.DOTALL)
    
    # Insert extra CSS before </style>
    content = content.replace('</style>', extra_css + '\n</style>', 1)
    
    # Write back
    with open(filename, 'w') as f:
        f.write(content)
    print(f'Updated {filename}')
