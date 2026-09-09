import os

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

header = "## Open Source Contributions\n\nBeyond my own projects, I contribute fixes and features upstream to real-world open source projects:\n\n"
if header in content:
    idx = content.find(header) + len(header)
    
    # Add markers
    new_content = content[:idx] + "<!-- MANUALLY_ADDED_PRS -->\n- **[facebookresearch/faiss](https://github.com/facebookresearch/faiss)** - Fix range_search_max_results to respect all similarity metrics\n<!-- END_MANUALLY_ADDED_PRS -->\n\n<!-- START_PRS -->\n"
    
    # get the rest
    rest = content[idx:]
    # remove the facebookresearch one from the rest if it's there
    rest_lines = [l for l in rest.split('\n') if 'facebookresearch/faiss' not in l and l.strip() != '']
    new_content += '\n'.join(rest_lines) + "\n<!-- END_PRS -->\n"
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
