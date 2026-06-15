import os
import glob
import re

files = glob.glob('C:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/*.md')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove !important from inline color styles
    # Match color: #a3e635 !important;
    new_content = re.sub(r'color:\s*#[0-9a-fA-F]+\s*!important\s*;', lambda m: m.group(0).replace('!important', ''), content)
    
    # Also for background-color if any
    new_content = re.sub(r'background-color:\s*#[0-9a-fA-F]+\s*!important\s*;', lambda m: m.group(0).replace('!important', ''), new_content)

    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed inline !important from {file}")

print("Done.")
