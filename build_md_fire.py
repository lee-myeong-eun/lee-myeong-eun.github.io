import json
import os

try:
    with open('C:/Users/user/Desktop/lee-myeong-eun.github.io/화재대피_.ipynb', encoding='utf-8') as f:
        d = json.load(f)
except Exception as e:
    print("Error reading the notebook:", e)
    exit(1)

out_path = 'C:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/fire-evac-notebook.md'

with open(out_path, 'w', encoding='utf-8') as out:
    out.write('---\n')
    out.write('layout: default\n')
    out.write('title: 실내 화재 대피 유도 시스템 (SIGNAL_SPEAK) 코드 리뷰\n')
    out.write('permalink: /projects/fire-evac-notebook/\n')
    out.write('---\n\n')
    
    out.write('<style>\n')
    out.write('  /* Ensure code blocks have a light, readable color on dark backgrounds */\n')
    out.write('  pre, code, .highlight pre, .highlight code, pre code {\n')
    out.write('    color: #bae6fd !important;\n')
    out.write('    background-color: #161b22 !important;\n')
    out.write('    border-radius: 8px;\n')
    out.write('  }\n')
    out.write('  .highlight {\n')
    out.write('    background-color: #161b22 !important;\n')
    out.write('    border-radius: 8px;\n')
    out.write('    padding: 15px;\n')
    out.write('  }\n')
    out.write('</style>\n\n')

    out.write('## 실내 화재 대피 유도 시스템 (SIGNAL_SPEAK) 프로젝트 코드 리뷰\n\n')

    for cell in d.get('cells', []):
        source = ''.join(cell.get('source', []))
        if cell['cell_type'] == 'markdown':
            out.write(source + '\n\n')
        elif cell['cell_type'] == 'code':
            if source.strip():
                # Assuming the code is C/C++ based on the includes
                out.write('```c\n' + source + '\n```\n\n')
            
            # Print execution outputs if any
            outputs = cell.get('outputs', [])
            if outputs:
                out.write('<div class="terminal-output mt-2 mb-4" style="box-shadow: 0 4px 20px rgba(0,0,0,0.3);">\n')
                out.write('  <div class="terminal-header d-flex align-items-center justify-content-between px-3 py-2" style="background-color: #0d1117; border-radius: 8px 8px 0 0; border: 1px solid rgba(255,255,255,0.05); border-bottom: none; font-size: 0.8rem; color: #8b949e;">\n')
                out.write('    <span><i class="fa fa-terminal mr-2"></i>Execution Output</span>\n')
                out.write('  </div>\n')
                out.write('  <pre class="p-3 m-0 small" style="background-color: #161b22; border-radius: 0 0 8px 8px; border: 1px solid rgba(255,255,255,0.05); font-family: \'Fira Code\', \'Courier New\', monospace; overflow-x: auto; white-space: pre-wrap; line-height: 1.5; color: #a3e635 !important;">')
                
                output_text = ''
                for o in outputs:
                    if o.get('output_type') == 'stream':
                        output_text += ''.join(o.get('text', []))
                    elif o.get('output_type') == 'execute_result':
                        data = o.get('data', {})
                        if 'text/plain' in data:
                            output_text += ''.join(data['text/plain'])
                
                # escape HTML characters in output text
                output_text = output_text.replace('<', '&lt;').replace('>', '&gt;')
                out.write(output_text)
                out.write('</pre>\n</div>\n\n')
                
print("Conversion successful.")
