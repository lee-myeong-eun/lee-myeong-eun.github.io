import re

file_paths = [
    'C:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/c-sharp-basics.md',
    'C:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/python-basics.md'
]

pattern = re.compile(r'^(?:-\s*)?([A-Za-z가-힣0-9\s\(\)\.\_]+):\s+(.*)$')

for file_path in file_paths:
    with open(file_path, encoding='utf-8-sig') as f:
        lines = f.readlines()

    out = []
    in_code_block = False
    in_frontmatter = False

    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Frontmatter usually starts with --- on the very first line
        if i == 0 and stripped == '---':
            in_frontmatter = True
            out.append(line)
            continue
            
        if in_frontmatter:
            out.append(line)
            if stripped == '---':
                in_frontmatter = False
            continue
        
        # Check for code blocks
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            out.append(line)
            continue
            
        if in_code_block:
            out.append(line)
            continue
            
        # Avoid lines that are already HTML or Markdown headers or blockquotes
        if stripped and not stripped.startswith('<') and not stripped.startswith('#') and not stripped.startswith('→') and not stripped.startswith('>'):
            match = pattern.match(line)
            if match:
                keyword = match.group(1)
                rest = match.group(2)
                if len(keyword) < 40 and len(keyword.strip()) > 1:
                    prefix = "- " if line.startswith("-") else ""
                    # Added display: inline-block; word-break: keep-all; to prevent truncation or awkward wrapping
                    new_line = f'{prefix}<span style="color: #38bdf8; font-weight: bold; word-break: keep-all; display: inline-block;">{keyword}:</span> {rest}\n'
                    out.append(new_line)
                    continue
        
        out.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(out)

print("Colored keywords applied perfectly.")
