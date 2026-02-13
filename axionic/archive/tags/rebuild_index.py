#!/usr/bin/env python3
"""Rebuild tags/index.md with tag names instead of filenames."""

from pathlib import Path
import re

TAGS_DIR = Path(".")

def extract_tag_name(filepath):
    """Extract tag name from markdown file."""
    try:
        content = filepath.read_text()
        # Look for title in front matter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                title_match = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', front_matter, re.MULTILINE)
                if title_match:
                    return title_match.group(1).strip()
        
        # Fallback: look for first heading
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        
        # Last resort: use filename with dashes replaced by spaces
        return filepath.stem.replace('-', ' ').title()
    except:
        return filepath.stem.replace('-', ' ').title()

def main():
    # Get all tag files
    tag_files = sorted([f for f in TAGS_DIR.glob("*.md") if f.name != "index.md"])
    
    print(f"Found {len(tag_files)} tag files")
    
    # Build index content
    content = """---
layout: default
title: Tag Index
parent: Axio Archive Study
grand_parent: Axionic Agency
---

# Tag Index

**Total Tags:** {total}  
**All tags alphabetically:**

## Navigation

- **[Taxonomy](../taxonomy)** — Full tag reference with descriptions
- **[All Posts](../posts/)** — Browse all posts
- **[Sequence Summaries](../)** — Overview of 12 sequences

## All Tags (A-Z)

""".format(total=len(tag_files))
    
    # Add tag links with names
    for tag_file in tag_files:
        tag_name = extract_tag_name(tag_file)
        content += f"- [{tag_name}]({tag_file.name})\n"
    
    # Write index
    index_path = Path("index.md")
    index_path.write_text(content)
    print(f"Rebuilt index.md with {len(tag_files)} tags")

if __name__ == "__main__":
    main()
