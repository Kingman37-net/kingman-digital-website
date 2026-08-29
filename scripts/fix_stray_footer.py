import re

files = ['docs/index.html', 'docs/resources.html']

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Find the floating social comment
    comment = '<!-- Floating social icons -->'
    idx = content.find(comment)
    if idx == -1:
        print(f"No floating social comment in {filepath}, skipping.")
        continue
    
    # Find the next occurrence of '</footer>' after the comment
    end_idx = content.find('</footer>', idx)
    if end_idx == -1:
        print(f"No closing footer after comment in {filepath}, skipping.")
        continue
    
    # Remove from comment to that closing footer (inclusive)
    content = content[:idx] + content[end_idx + len('</footer>'):]
    
    # Also remove any stray opening <footer> that might be left (but there shouldn't be)
    # Now we should have only one proper footer later.
    # Save
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Removed stray footer fragment from {filepath}")
