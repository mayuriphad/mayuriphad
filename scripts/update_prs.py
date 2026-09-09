import os
import re
import subprocess
import json

def get_merged_prs():
    # Fetch latest 20 merged PRs
    # Using gh CLI, which uses the GITHUB_TOKEN environment variable implicitly
    cmd = ['gh', 'search', 'prs', '--author', '@me', '--merged', '--limit', '20', '--json', 'url,title,repository']
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error fetching PRs:", result.stderr)
        return []
    
    return json.loads(result.stdout)

def main():
    prs = get_merged_prs()
    
    if not prs:
        print("No PRs found or error occurred.")
        return

    # Format the PRs
    pr_lines = []
    for pr in prs:
        repo_name = pr['repository']['nameWithOwner']
        title = pr['title']
        url = pr['url']
        # Remove the /pull/... part for the repo link
        repo_url = url.split('/pull/')[0]
        pr_lines.append(f"- **[{repo_name}]({repo_url})** — {title}")
    
    new_prs_section = '\n'.join(pr_lines) + '\n'

    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace content between markers
    start_marker = "<!-- START_PRS -->"
    end_marker = "<!-- END_PRS -->"
    
    pattern = re.compile(rf"({start_marker}).*?({end_marker})", re.DOTALL)
    
    new_content = pattern.sub(rf"\1\n{new_prs_section}\2", content)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("README.md updated with latest PRs!")

if __name__ == '__main__':
    main()
