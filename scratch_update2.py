import re

file_path = 'C:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/python-basics.md'

with open(file_path, encoding='utf-8') as f:
    lines = f.readlines()

out = []
in_callout = False

for line in lines:
    stripped = line.strip()
    
    # If we are inside a callout and we hit something that should break it
    if in_callout and (stripped.startswith('```') or 
                       stripped.startswith('### ') or 
                       stripped.startswith('<!--') or 
                       stripped.startswith('<div') or 
                       stripped == '</div>' or 
                       stripped.startswith('---')):
        out.append('\n</div>\n\n')
        in_callout = False

    # Start a new callout
    if stripped.startswith('#### ') or stripped.startswith('##### '):
        if in_callout:
            out.append('\n</div>\n\n')
            in_callout = False
            
        title = stripped.lstrip('#').strip()
        is_warning = '주의' in title
        
        if is_warning:
            out.append('<div class="alert shadow-sm mt-4 mb-4" style="border: 1px solid rgba(245, 158, 11, 0.2); border-left: 4px solid #f59e0b; background-color: rgba(245, 158, 11, 0.05); border-radius: 8px; color: #cbd5e1; line-height: 1.8;" markdown="1">\n')
            out.append(f'  <h5 class="alert-heading font-weight-bold mb-3" style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>{title}</h5>\n')
        else:
            out.append('<div class="alert shadow-sm mt-4 mb-4" style="border: 1px solid rgba(56, 189, 248, 0.2); border-left: 4px solid #38bdf8; background-color: rgba(56, 189, 248, 0.05); border-radius: 8px; color: #cbd5e1; line-height: 1.8;" markdown="1">\n')
            out.append(f'  <h5 class="alert-heading font-weight-bold mb-3" style="color: #38bdf8;"><i class="fa fa-book mr-2"></i>{title}</h5>\n')
            
        in_callout = True
        continue # Skip the original #### line since we rendered it as an h5

    out.append(line)

# If file ends while in callout
if in_callout:
    out.append('\n</div>\n\n')

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(out)

print("Formatting applied.")
