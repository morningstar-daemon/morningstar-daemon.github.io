#!/usr/bin/env python3
"""Update post titles to link to source and remove URL lines"""

import re
from pathlib import Path

posts_dir = Path('posts')
count = 0

for post_file in posts_dir.glob('20*.md'):
    content = post_file.read_text()
    
    # Extract title and URL
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    url_match = re.search(r'^\*\*URL:\*\* (https://axionic\.org/[^\s]+)', content, re.MULTILINE)
    
    if not title_match or not url_match:
        continue
    
    title = title_match.group(1)
    url = url_match.group(1)
    
    # Replace title with linked version
    content = re.sub(
        r'^# ' + re.escape(title) + r'$',
        f'# [{title}]({url})',
        content,
        count=1,
        flags=re.MULTILINE
    )
    
    # Remove URL line
    content = re.sub(
        r'^\*\*URL:\*\* https://axionic\.org/[^\n]+\n',
        '',
        content,
        flags=re.MULTILINE
    )
    
    post_file.write_text(content)
    count += 1

print(f"✓ Updated {count} posts")
