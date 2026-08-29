import re

files = ['docs/index.html', 'docs/resources.html']

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Remove duplicate CSS component blocks (keep only the first)
    #    Pattern: between /* KDCN V1.1 COMPONENTS START */ and /* KDCN V1.1 COMPONENTS END */
    start_marker = '/* KDCN V1.1 COMPONENTS START */'
    end_marker = '/* KDCN V1.1 COMPONENTS END */'
    # Find all such blocks
    blocks = list(re.finditer(re.escape(start_marker) + r'.*?' + re.escape(end_marker), content, flags=re.DOTALL))
    if blocks:
        # Keep only the first block, remove all others
        first_block = blocks[0].group(0)
        # Remove all blocks
        content = re.sub(re.escape(start_marker) + r'.*?' + re.escape(end_marker), '', content, flags=re.DOTALL)
        # Reinsert the first block at the position of the first occurrence
        # We'll insert before </style> once
        content = content.replace('</style>', first_block + '\n</style>', 1)
    
    # 2. Keep only the last <footer>...</footer> block (the legitimate one, nearest end)
    footers = list(re.finditer(r'<footer>.*?</footer>', content, flags=re.DOTALL))
    if footers:
        # We want to keep the last footer (closest to </body>)
        proper_footer = footers[-1].group(0)
        # Remove all footer blocks
        content = re.sub(r'<footer>.*?</footer>', '', content, flags=re.DOTALL)
        # Insert the proper footer before the chat widget or </body>
        chat_marker = '<!-- KDCN Chat Widget -->'
        if chat_marker in content:
            content = content.replace(chat_marker, proper_footer + '\n' + chat_marker)
        else:
            content = content.replace('</body>', proper_footer + '\n</body>')
    
    # 3. Remove any remaining stray footer-grid / footer-col divs that are outside a footer
    #    They should not exist now, but as a safety, remove any <div class="footer-grid"> ... </div> patterns
    content = re.sub(r'<div class="footer-grid">.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div class="footer-col">.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f'Fixed {filepath}')
