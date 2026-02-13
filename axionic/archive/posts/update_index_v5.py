#!/usr/bin/env python3
"""Update index.md Posts by Date section with [YYYY-MM-DD - title](link) format."""

from pathlib import Path
import re

def extract_title(filepath):
    """Extract title from Jekyll front matter or first markdown heading."""
    try:
        content = filepath.read_text()
        
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                title_match = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', front_matter, re.MULTILINE)
                if title_match:
                    return title_match.group(1).strip()
        
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        
        return None
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def main():
    posts_dir = Path(".")
    
    posts = []
    for f in sorted(posts_dir.glob("*.md")):
        if f.name in ["index.md", "manifest.md", "taxonomy.md"]:
            continue
        
        match = re.match(r'(\d{4}-\d{2}-\d{2})-', f.name)
        if not match:
            continue
        
        date = match.group(1)
        title = extract_title(f)
        
        if title:
            posts.append((date, title, f.name))
    
    print(f"Found {len(posts)} posts with titles")
    
    index_path = Path("index.md")
    content = index_path.read_text()
    
    start_marker = "## Posts by Date"
    
    if start_marker not in content:
        print("Error: 'Posts by Date' section not found")
        return
    
    before_section = content.split(start_marker)[0]
    
    # Put date inside the link text: [YYYY-MM-DD - Title](filename)
    posts_lines = [f"- [{date} - {title}]({filename})" for date, title, filename in sorted(posts, reverse=True)]
    
    new_content = (
        before_section + start_marker + "\n\n" +
        "Browse all posts in reverse chronological order:\n\n" +
        "\n".join(posts_lines) + "\n"
    )
    
    index_path.write_text(new_content)
    print(f"Updated index.md with {len(posts)} posts in [YYYY-MM-DD - title](link) format")

if __name__ == "__main__":
    main()
