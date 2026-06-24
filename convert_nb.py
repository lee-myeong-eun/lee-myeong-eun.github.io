import json
import sys
import os

def convert_ipynb_to_md(ipynb_path, md_path):
    with open(ipynb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    md_lines = []
    # Add frontmatter
    md_lines.append("---")
    md_lines.append("layout: default")
    md_lines.append("title: 11. 시험대비요약1(한가지 통합)")
    md_lines.append("permalink: /assignments/machine-learning/exam-summary-1/")
    md_lines.append("---")
    md_lines.append("")

    for cell in nb.get('cells', []):
        cell_type = cell.get('cell_type')
        source = cell.get('source', [])
        source_text = "".join(source)

        if cell_type == 'markdown':
            md_lines.append(source_text)
            md_lines.append("")
        elif cell_type == 'code':
            if source_text.strip():
                md_lines.append("```python")
                md_lines.append(source_text)
                if not source_text.endswith('\n'):
                    md_lines.append("")
                md_lines.append("```")
                md_lines.append("")
            
            # handle outputs
            for output in cell.get('outputs', []):
                output_type = output.get('output_type')
                if output_type in ('execute_result', 'display_data'):
                    data = output.get('data', {})
                    if 'text/plain' in data:
                        text_output = "".join(data['text/plain'])
                        md_lines.append("```text")
                        md_lines.append(text_output)
                        md_lines.append("```")
                        md_lines.append("")
                elif output_type == 'stream':
                    text_output = "".join(output.get('text', []))
                    md_lines.append("```text")
                    md_lines.append(text_output)
                    md_lines.append("```")
                    md_lines.append("")

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(md_lines))

if __name__ == "__main__":
    convert_ipynb_to_md(sys.argv[1], sys.argv[2])
