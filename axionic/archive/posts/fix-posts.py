#!/usr/bin/env python3
"""Fix post titles and regenerate index.md"""
import os
import re
from pathlib import Path

posts_dir = Path(__file__).parent
posts = []

# Fix title format and collect post info
for md_file in sorted(posts_dir.glob("*.md")):
    if md_file.name in ("index.md", "fix-posts.py"):
        continue
    
    content = md_file.read_text()
    
    # Extract and fix title - match [Title](url) pattern
    title_match = re.search(r'title:\s*"\[([^\]]+)\]\([^)]+\)"', content)
    if title_match:
        old_title = title_match.group(0)
        plain_title = title_match.group(1)
        new_title = f'title: "{plain_title}"'
        content = content.replace(old_title, new_title, 1)
        
        # Also fix the H1 header if it has the same pattern
        h1_pattern = r'^# \[([^\]]+)\]\([^)]+\)$'
        content = re.sub(h1_pattern, f'# {plain_title}', content, flags=re.MULTILINE)
        
        md_file.write_text(content)
        print(f"Fixed: {md_file.name}")
    else:
        # Extract plain title
        title_match = re.search(r'title:\s*"([^"]+)"', content)
        if title_match:
            plain_title = title_match.group(1)
        else:
            plain_title = md_file.stem
    
    # Extract date
    date_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', content)
    date = date_match.group(1) if date_match else md_file.stem[:10]
    
    posts.append({
        "file": md_file.name,
        "title": plain_title,
        "date": date
    })

# Sort by date (newest first)
posts.sort(key=lambda x: x["date"], reverse=True)

# Generate index.md
index_content = """---
layout: default
title: All Posts
parent: Axio Archive Study
grand_parent: Axionic Agency
---

# Axio Archive: All Posts

**Total Posts:** {count}  
**Date Range:** 2022-2026  
**Source:** [axionic.org](https://axionic.org/publications.html)

## Navigation

- **[Taxonomy](../taxonomy)** — Browse by tag with descriptions
- **[Tag Index](../tags/)** — All 1835 tags
- **[Sequence Summaries](../)** — Overview of 12 major sequences

## Posts by Date

Browse all posts in reverse chronological order:

""".format(count=len(posts))

for post in posts:
    index_content += f"- [{post['title']}]({post['file']})\n"

(posts_dir / "index.md").write_text(index_content)
print(f"\nGenerated index.md with {len(posts)} posts")
