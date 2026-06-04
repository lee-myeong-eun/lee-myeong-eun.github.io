import json

f = open('C:/Users/user/Desktop/c언어 문제정리-1.ipynb', encoding='utf-8')
d = json.load(f)
f.close()

with open('c:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/c-programming-problems.md', 'w', encoding='utf-8') as out:
    out.write('---\n')
    out.write('layout: default\n')
    out.write('title: C언어 문제정리\n')
    out.write('permalink: /assignments/c-programming/\n')
    out.write('---\n\n')
    
    out.write('<style>\n')
    out.write('  /* Ensure code blocks have a light, readable color on dark backgrounds */\n')
    out.write('  pre, code, .highlight pre, .highlight code, pre code {\n')
    out.write('    color: #a3e635 !important;\n')
    out.write('    background-color: #161b22 !important;\n')
    out.write('    border-radius: 8px;\n')
    out.write('  }\n')
    out.write('  .highlight {\n')
    out.write('    background-color: #161b22 !important;\n')
    out.write('    border-radius: 8px;\n')
    out.write('    padding: 15px;\n')
    out.write('  }\n')
    out.write('</style>\n\n')

    for cell in d['cells']:
        source = ''.join(cell.get('source', []))
        if cell['cell_type'] == 'markdown':
            out.write(source + '\n\n')
        else:
            out.write('```c\n' + source + '\n```\n\n')
