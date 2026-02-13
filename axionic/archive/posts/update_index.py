#!/usr/bin/env python3
"""Update index.md Posts by Date section with YYYY-MM-DD - title format."""

from pathlib import Path
import re

def extract_title(filepath):
    """Extract the first markdown heading from a file."""
    try:
        content = filepath.read_text()
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except:
        pass
    return None

def main():
    posts_dir = Path(".")
    
    # Get all .md files except index, manifest, taxonomy
    posts = []
    for f in sorted(posts_dir.glob("*.md")):
        if f.name in ["index.md", "manifest.md", "taxonomy.md"]:
            continue
        
        # Extract date from filename
        match = re.match(r'(\d{4}-\d{2}-\d{2})-', f.name)
        if not match:
            continue
        
        date = match.group(1)
        title = extract_title(f)
        
        if title:
            posts.append((date, title))
    
    # Read current index.md
    index_path = Path("index.md")
    content = index_path.read_text()
    
    # Find the "Posts by Date" section
    start_marker = "## Posts by Date"
    
    if start_marker not in content:
        print("Error: 'Posts by Date' section not found")
        return
    
    # Split at the section
    parts = content.split(start_marker)
    if len(parts) != 2:
        print("Error: Unexpected structure")
        return
    
    # Build new posts list
    posts_text = "\n".join(f"- {date} - {title}" for date, title in sorted(posts, reverse=True))
    
    # Rebuild index.md
    new_content = (
        parts[0] + start_marker + "\n\n" +
        "Browse all posts in reverse chronological order:\n\n" +
        posts_text
    )
    
    index_path.write_text(new_content)
    print(f"Updated index.md with {len(posts)} posts")

if __name__ == "__main__":
    main()
