import json

in_path = 'C:/Users/user/Desktop/c#.ipynb'
out_path = 'C:/Users/user/Desktop/lee-myeong-eun.github.io/_pages/c-sharp-basics.md'

with open(in_path, encoding='utf-8') as f:
    d = json.load(f)

# Extract sections
# A section starts when a markdown cell has "## <number>."
sections = []
current_section = None

# Icons for the 8 sections
icons = [
    ("fa-terminal", "#38bdf8"),    # 1. 출력
    ("fa-cube", "#fb7185"),        # 2. 데이터형
    ("fa-microchip", "#34d399"),   # 3. 메모리
    ("fa-code-fork", "#a78bfa"),   # 4. 제어문 배열
    ("fa-cubes", "#fb923c"),       # 5. 구조체 클래스
    ("fa-warning", "#2dd4bf"),     # 6. 예외처리
    ("fa-object-group", "#f472b6"),# 7. 객체지향
    ("fa-sitemap", "#818cf8")      # 8. 상속 다형성
]

for cell in d.get('cells', []):
    if cell['cell_type'] == 'markdown':
        src = "".join(cell['source'])
        lines = src.split('\n')
        # Check if the first line is a section header like "## 1."
        header_line = None
        for i, line in enumerate(lines):
            if line.startswith('## '):
                header_line = line
                # Keep the rest of the lines as content for this block
                block_content = '\n'.join(lines[i+1:])
                # Create a new section
                current_section = {
                    'title': header_line.lstrip('#').strip(),
                    'content': block_content
                }
                sections.append(current_section)
                break
        
        if header_line is None and current_section is not None:
            # If it's just continuation content
            current_section['content'] += '\n\n' + src

if len(sections) == 0:
    print("No sections found!")
    exit(1)

with open(out_path, 'w', encoding='utf-8') as out:
    out.write('---\n')
    out.write('layout: default\n')
    out.write('title: C# 기초 문법 실습\n')
    out.write('permalink: /assignments/c-sharp-basics/\n')
    out.write('---\n\n')
    
    out.write('<div class="row">\n')
    out.write('  <div class="col-md-12 mb-5">\n')
    out.write('    \n')
    out.write('    <!-- Header -->\n')
    out.write('    <div class="animate-fade-in-up delay-100">\n')
    out.write('      <span class="tech-badge">💻 C# Study Record</span>\n')
    out.write('      <h2 class="text-gradient">C# 기초 문법 및 객체지향 프로그래밍 실습</h2>\n')
    out.write('      <hr />\n')
    out.write('      <p class="lead text-light font-weight-normal">\n')
    out.write('        반도체 장비 GUI 및 제어 개발을 위해 학습하고 정리한 **C# 기초 및 메모리/객체지향 구조** 기록입니다.\n')
    out.write('      </p>\n')
    out.write('    </div>\n\n')

    out.write('    <!-- Contents Grid -->\n')
    out.write('    <div class="row mt-5 animate-fade-in-up delay-200">\n')
    out.write('      \n')
    out.write('      <!-- Left Sidebar Index -->\n')
    out.write('      <div class="col-lg-4 mb-4">\n')
    out.write('        <div class="border-0 shadow welcome-box p-3 sticky-top" style="top: 100px; z-index: 10; background-color: #161e2f; border: 1px solid rgba(255,255,255,0.05) !important;">\n')
    out.write('          <h4 class="text-gradient mb-3" style="font-size: 1.1rem;"><i class="fa fa-list-ul mr-2"></i>학습 목차</h4>\n')
    out.write('          <ul class="list-unstyled small mb-0 pl-1" style="line-height: 2.2;">\n')
    
    for i, sec in enumerate(sections):
        icon, color = icons[i % len(icons)]
        out.write(f'            <li><a href="#section{i+1}" class="text-info text-hover-glow" style="transition: all 0.2s;"><i class="fa {icon} mr-2" style="color: {color}; width: 16px; text-align: center;"></i>{sec["title"]}</a></li>\n')
        
    out.write('          </ul>\n')
    out.write('          <hr class="my-3" style="border-top: 1px solid rgba(255,255,255,0.08);" />\n')
    out.write('          <a href="{{ site.baseurl }}/assignments/" class="btn btn-outline-light btn-sm btn-block text-hover-glow">\n')
    out.write('            <i class="fa fa-arrow-left mr-1"></i>아카이브로 돌아가기\n')
    out.write('          </a>\n')
    out.write('        </div>\n')
    out.write('      </div>\n\n')

    out.write('      <!-- Right Detailed Content -->\n')
    out.write('      <div class="col-lg-8 mb-4">\n')
    
    for i, sec in enumerate(sections):
        icon, color = icons[i % len(icons)]
        out.write(f'        <!-- Section: {sec["title"]} -->\n')
        out.write(f'        <div id="section{i+1}" class="mb-5" style="padding: 1rem 0;">\n')
        out.write('          <div class="d-flex align-items-center mb-4">\n')
        out.write(f'            <div class="icon-wrapper mr-3" style="font-size: 1.8rem; color: {color}; background: rgba(255,255,255,0.02); width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">\n')
        out.write(f'              <i class="fa {icon}"></i>\n')
        out.write('            </div>\n')
        out.write('            <div>\n')
        out.write(f'              <h3 class="mb-0 text-gradient font-weight-bold" style="font-size: 1.4rem;">{sec["title"]}</h3>\n')
        out.write('            </div>\n')
        out.write('          </div>\n')
        out.write('          <hr class="mb-4" style="border-top: 1px solid rgba(255,255,255,0.08);" />\n')
        out.write('          <div class="content-body" style="line-height: 1.8; color: #cbd5e1;">\n')
        
        # Process the content to handle #### tags properly just like python-basics
        lines = sec["content"].split("\n")
        parsed_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("#### ") or stripped.startswith("##### ") or stripped.startswith("📌"):
                if stripped.startswith("📌"):
                    title = stripped.lstrip("📌").strip()
                    parsed_lines.append(f'<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>{title}</span>\n')
                else:
                    title = stripped.lstrip("#").strip()
                    if '주의' in title or '예외' in title:
                        parsed_lines.append(f'<br><span style="color: #f59e0b;"><i class="fa fa-exclamation-triangle mr-2"></i>{title}</span>\n')
                    else:
                        parsed_lines.append(f'<br><span style="color: #38bdf8;"><i class="fa fa-check mr-2"></i>{title}</span>\n')
            else:
                parsed_lines.append(line)
        
        out.write("\n".join(parsed_lines) + "\n")
        out.write('          </div>\n')
        out.write('        </div>\n\n')

    out.write('      </div>\n')
    out.write('    </div>\n')
    out.write('  </div>\n')
    out.write('</div>\n')

print("C# Markdown generated.")
