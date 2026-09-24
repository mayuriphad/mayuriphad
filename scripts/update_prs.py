import os
import re
import subprocess
import json
from datetime import datetime

def get_merged_prs():
    cmd = ['gh', 'search', 'prs', '--author', '@me', '--merged', '--limit', '10', '--json', 'url,title,repository,closedAt,number']
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error fetching PRs:", result.stderr)
        return []
    
    return json.loads(result.stdout)

def format_date(date_str):
    if not date_str:
        return ""
    dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
    return dt.strftime('%b %d').lower()

def main():
    prs = get_merged_prs()
    
    if not prs:
        print("No PRs found or error occurred.")
        return

    table = [
        '<div align="center">',
        '  <table>',
        '    <tr>',
        '      <th align="left">repo</th>',
        '      <th align="left">pr</th>',
        '      <th align="center">date</th>',
        '    </tr>'
    ]

    for pr in prs:
        repo_name = pr['repository']['name']
        title = pr['title']
        if len(title) > 55:
            title = title[:52] + '...'
            
        url = pr['url']
        repo_url = url.split('/pull/')[0]
        date = format_date(pr.get('closedAt'))
        
        table.append('    <tr>')
        table.append(f'      <td><a href="{repo_url}"><b>{repo_name}</b></a></td>')
        table.append(f'      <td><a href="{url}">{title.lower()}</a></td>')
        table.append(f'      <td align="right"><i>{date}</i></td>')
        table.append('    </tr>')
        
    table.append('  </table>')
    table.append('</div>')
    
    new_prs_section = '\n'.join(table)

    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = "<!-- START_PRS -->"
    end_marker = "<!-- END_PRS -->"
    
    # We will use simple string splitting to replace the content
    if start_marker in content and end_marker in content:
        before = content.split(start_marker)[0]
        after = content.split(end_marker)[1]
        
        new_content = f"{before}{start_marker}\n{new_prs_section}\n{end_marker}{after}"
        
        with open('README.md', 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print("README.md updated with latest PRs!")
    else:
        print("Markers not found in README.md")

if __name__ == '__main__':
    main()
