#!/usr/bin/env python3
"""Fix posts: remove redundant H1, add source link from git history"""
import subprocess
import re
from pathlib import Path

posts_dir = Path(__file__).parent

for md_file in sorted(posts_dir.glob("*.md")):
    if md_file.name in ("index.md", "fix-posts.py", "fix-posts-v2.py"):
        continue
    
    content = md_file.read_text()
    original = content
    
    # Get the original URL from git history
    try:
        old_content = subprocess.check_output(
            ['git', 'show', f'HEAD~1:{md_file.relative_to(posts_dir.parent.parent.parent)}'],
            cwd=posts_dir.parent.parent.parent,
            stderr=subprocess.DEVNULL
        ).decode('utf-8')
        
        # Extract URL from old title format: [Title](url)
        url_match = re.search(r'title:\s*"\[[^\]]+\]\(([^)]+)\)"', old_content)
        source_url = url_match.group(1) if url_match else None
    except:
        source_url = None
    
    # Extract the title from frontmatter
    title_match = re.search(r'title:\s*"([^"]+)"', content)
    if not title_match:
        continue
    title = title_match.group(1)
    
    # Remove the redundant H1 (plain title, since we already fixed the link format)
    h1_line = f'# {title}\n'
    if h1_line in content:
        content = content.replace(h1_line, '', 1)
    
    # Add source link after Batch line if we have the URL and it's not already there
    if source_url and '**Source:**' not in content:
        batch_pattern = r'(\*\*Batch:\*\* [^\n]+\n)'
        if re.search(batch_pattern, content):
            source_line = f'**Source:** [{source_url}]({source_url})\n'
            content = re.sub(batch_pattern, r'\1' + source_line, content, count=1)
    
    if content != original:
        md_file.write_text(content)
        print(f"Fixed: {md_file.name}")

print("\nDone!")
