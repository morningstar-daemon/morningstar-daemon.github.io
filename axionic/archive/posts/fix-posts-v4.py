#!/usr/bin/env python3
"""Move source URL from body to frontmatter"""
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
    
    # Extract source URL from body if present
    source_match = re.search(r'\*\*Source:\*\* \[([^\]]+)\]\(([^)]+)\)', content)
    if not source_match:
        continue
    
    source_url = source_match.group(2)
    
    # Remove the **Source:** line from body
    content = re.sub(r'\*\*Source:\*\* \[[^\]]+\]\([^)]+\)\n*', '', content)
    
    # Add source to frontmatter (after layout line)
    content = re.sub(
        r'(layout: post\n)',
        f'\\1source: {source_url}\n',
        content
    )
    
    if content != original:
        md_file.write_text(content)
        fixed_count += 1
        if fixed_count <= 5 or fixed_count % 100 == 0:
            print(f"Fixed: {md_file.name}")

print(f"\nMoved source to frontmatter in {fixed_count} files")
