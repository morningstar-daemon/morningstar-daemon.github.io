#!/usr/bin/env python3
"""Fix posts: remove redundant Date line, ensure source link before Summary"""
import subprocess
import re
from pathlib import Path

posts_dir = Path(__file__).parent

fixed_count = 0
for md_file in sorted(posts_dir.glob("*.md")):
    if md_file.name.startswith(("index", "fix-posts")):
        continue
    
    content = md_file.read_text()
    original = content
    
    # Check if source link already exists  
    has_source = '**Source:**' in content
    
    # Get the original URL from git history if no source link
    source_url = None
    if not has_source:
        try:
            # Go back 2 commits to before any fixes
            old_content = subprocess.check_output(
                ['git', 'show', f'HEAD~2:axionic/archive/posts/{md_file.name}'],
                cwd=posts_dir.parent.parent.parent,
                stderr=subprocess.DEVNULL
            ).decode('utf-8')
            
            url_match = re.search(r'\]\((https://axionic\.org/posts/[^)]+)\)', old_content)
            source_url = url_match.group(1) if url_match else None
        except:
            pass
    
    # Remove **Date:** line(s) - Jekyll shows date from frontmatter
    content = re.sub(r'\*\*Date:\*\*[^\n]*\n\s*', '', content)
    
    # Remove **Batch:** line(s) - not needed
    content = re.sub(r'\*\*Batch:\*\*[^\n]*\n\s*', '', content)
    
    # Get title from frontmatter to remove redundant H1
    title_match = re.search(r'title:\s*"([^"]+)"', content)
    if title_match:
        title = title_match.group(1)
        # Remove H1 that matches title (exactly)
        h1_pattern = r'^# ' + re.escape(title) + r'\s*\n+'
        content = re.sub(h1_pattern, '', content, flags=re.MULTILINE)
    
    # If source URL found and no source link yet, insert before ## Summary
    if source_url and not has_source and '## Summary' in content:
        content = content.replace(
            '## Summary',
            f'**Source:** [{source_url}]({source_url})\n\n## Summary'
        )
    
    if content != original:
        md_file.write_text(content)
        fixed_count += 1
        if fixed_count <= 10 or fixed_count % 100 == 0:
            print(f"Fixed: {md_file.name}")

print(f"\nFixed {fixed_count} files")
