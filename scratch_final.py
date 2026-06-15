import re

file_path = 'C:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/python-basics.md'

with open(file_path, encoding='utf-8') as f:
    lines = f.readlines()

out = []

for line in lines:
    # Fix the massive hover jump effect
    if 'class="card border-0 shadow welcome-box' in line:
        line = line.replace('class="card border-0 shadow welcome-box', 'class="border-0 shadow welcome-box')
        
    stripped = line.strip()
    
    # Replace #### and ##### with normal text spans to keep size/weight uniform with body text
    if stripped.startswith('#### ') or stripped.startswith('##### '):
        title = stripped.lstrip('#').strip()
        is_warning = '주의' in title
        
        if is_warning:
            out.append(f'<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>{title}</span>\n\n')
        else:
            out.append(f'<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>{title}</span>\n\n')
    else:
        out.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(out)

print("Final formatting applied.")
