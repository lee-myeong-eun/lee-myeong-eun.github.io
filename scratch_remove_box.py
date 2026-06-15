import re

file_path = 'C:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/python-basics.md'

with open(file_path, encoding='utf-8') as f:
    content = f.read()

# Specifically target the section wrappers and remove their box styling
# Original: class="border-0 shadow welcome-box p-4 mb-5" style="background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 12px;"
# We want to replace it with: class="mb-5"

# Because the exact class string or style string might vary slightly if there are multiple sections, I will use regex.
pattern = r'<div\s+id="section(\d+)"\s+class="[^"]*welcome-box[^"]*"\s+style="[^"]*">?'
replacement = r'<div id="section\1" class="mb-5" style="padding: 1rem 0;">'

content_new = re.sub(pattern, replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content_new)

print("Box borders removed from sections.")
