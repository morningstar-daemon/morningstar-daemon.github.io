#!/usr/bin/env python3
"""Update index.md Posts by Date section with YYYY-MM-DD - [title](link) format."""

from pathlib import Path
import re

def extract_title(filepath):
    """Extract title from Jekyll front matter or first markdown heading."""
    try:
        content = filepath.read_text()
        
        # Try Jekyll front matter first
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                title_match = re.search(r'^title:\s*["\']?([^"\'\n]+)["\']?', front_matter, re.MULTILINE)
                if title_match:
                    return title_match.group(1).strip()
        
        # Fallback to markdown heading
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        
        return None
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
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
            posts.append((date, title, f.name))
        else:
            print(f"Warning: No title found for {f.name}")
    
    print(f"Found {len(posts)} posts with titles")
    
    # Read current index.md
    index_path = Path("index.md")
    content = index_path.read_text()
    
    # Find the "Posts by Date" section
    start_marker = "## Posts by Date"
    
    if start_marker not in content:
        print("Error: 'Posts by Date' section not found")
        return
    
    # Keep everything up to and including the section heading
    before_section = content.split(start_marker)[0]
    
    # Build new posts list (reverse chronological) with markdown links
    posts_lines = [f"- {date} - [{title}]({filename})" for date, title, filename in sorted(posts, reverse=True)]
    
    # Rebuild index.md
    new_content = (
        before_section + start_marker + "\n\n" +
        "Browse all posts in reverse chronological order:\n\n" +
        "\n".join(posts_lines) + "\n"
    )
    
    index_path.write_text(new_content)
    print(f"Updated index.md with {len(posts)} posts in YYYY-MM-DD - [title](link) format")

if __name__ == "__main__":
    main()
