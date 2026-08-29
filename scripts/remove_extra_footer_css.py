def clean_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    start_marker = '/* KDCN V1.1 COMPONENTS START */'
    end_marker = '/* KDCN V1.1 COMPONENTS END */'
    
    # Locate component block boundaries
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if start_marker in line:
            start_idx = i
        if end_marker in line:
            end_idx = i
            break
    if start_idx is None or end_idx is None:
        print(f"No component markers found in {filepath}")
        return
    
    lines_to_remove = set()
    i = 0
    while i < len(lines):
        # If we find a .footer-grid line that is NOT inside the component block
        if '.footer-grid' in lines[i] and not (start_idx <= i <= end_idx):
            # Remove this rule until the closing brace
            j = i
            while j < len(lines) and '}' not in lines[j]:
                lines_to_remove.add(j)
                j += 1
            if j < len(lines):
                lines_to_remove.add(j)
            i = j + 1
        else:
            i += 1
    
    # Rebuild file without removed lines
    new_lines = [line for idx, line in enumerate(lines) if idx not in lines_to_remove]
    with open(filepath, 'w') as f:
        f.writelines(new_lines)
    print(f"Cleaned {filepath}")

for f in ['docs/index.html', 'docs/resources.html']:
    clean_file(f)
