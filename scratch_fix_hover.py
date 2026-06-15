import re

file_path = 'C:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/python-basics.md'

with open(file_path, encoding='utf-8') as f:
    content = f.read()

# Fix the massive hover jump effect by removing the 'card' class from the welcome-box containers
content = content.replace('class="card border-0 shadow welcome-box', 'class="border-0 shadow welcome-box')

# Fix the font size and weight by changing h5 to h4 and removing font-weight-bold
content = content.replace('<h5 class="alert-heading font-weight-bold mb-3"', '<h4 class="alert-heading mb-3"')
content = content.replace('</h5>', '</h4>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixes applied.")
