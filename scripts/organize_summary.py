#!/usr/bin/env python3
"""
Helper script for organizing Notes to My Future Self summaries.

This script can:
1. Validate that a markdown file has the proper structure
2. Extract metadata (topic, date, status) from a summary file
3. Update the INDEX.md with a new entry
4. List files by category

Usage:
  python3 organize_summary.py validate <filepath>
  python3 organize_summary.py extract <filepath>
  python3 organize_summary.py update-index <filepath> <category>
  python3 organize_summary.py list <category>
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime

# Get the notes directory - looks for it relative to script location
# or uses the NOTES_DIR environment variable if set
def get_notes_dir():
    env_path = os.environ.get('NOTES_DIR')
    if env_path:
        return Path(env_path)

    # Default: parent of parent of this script
    # (notes-to-future-self-skill/scripts/organize_summary.py -> Notes-To-My-Future-Self)
    script_dir = Path(__file__).parent.parent.parent
    return script_dir

NOTES_DIR = get_notes_dir()

def extract_metadata(filepath):
    """Extract title, date, and status from a markdown file."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Extract title (first # heading)
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "Untitled"

    # Extract date created
    date_match = re.search(r'\*\*Date Created:\*\*\s*(\d{4}-\d{2}-\d{2})', content)
    date_created = date_match.group(1) if date_match else datetime.now().strftime("%Y-%m-%d")

    # Extract status
    status_match = re.search(r'\*\*Status:\*\*\s*\[(.+?)\]', content)
    status = status_match.group(1) if status_match else "Active"

    return {
        "title": title,
        "date_created": date_created,
        "status": status
    }

def validate_structure(filepath):
    """Check if markdown file has required sections."""
    required_sections = [
        "Context",
        "Decision Made",
        "Reasoning",
        "Key Learnings",
        "Personal Factors",
        "Action Items"
    ]

    with open(filepath, 'r') as f:
        content = f.read()

    missing = []
    for section in required_sections:
        if f"## {section}" not in content:
            missing.append(section)

    return {
        "valid": len(missing) == 0,
        "missing_sections": missing
    }

def list_files_by_category(category):
    """List all files in a category folder."""
    category_path = NOTES_DIR / category

    if not category_path.exists():
        return []

    files = []
    for md_file in category_path.glob("*.md"):
        if md_file.name != "TEMPLATE.md":
            try:
                metadata = extract_metadata(str(md_file))
                files.append({
                    "filename": md_file.name,
                    "title": metadata["title"],
                    "date": metadata["date_created"],
                    "status": metadata["status"]
                })
            except Exception as e:
                print(f"Warning: Could not read {md_file.name}: {e}", file=sys.stderr)

    return sorted(files, key=lambda x: x["date"], reverse=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "validate" and len(sys.argv) > 2:
        result = validate_structure(sys.argv[2])
        print(f"Valid: {result['valid']}")
        if result['missing_sections']:
            print(f"Missing sections: {', '.join(result['missing_sections'])}")

    elif command == "extract" and len(sys.argv) > 2:
        metadata = extract_metadata(sys.argv[2])
        for key, value in metadata.items():
            print(f"{key}: {value}")

    elif command == "list" and len(sys.argv) > 2:
        files = list_files_by_category(sys.argv[2])
        print(f"\nFiles in {sys.argv[2]}:\n")
        for f in files:
            print(f"  {f['title']}")
            print(f"    File: {f['filename']}")
            print(f"    Date: {f['date']} | Status: {f['status']}\n")

    else:
        print(__doc__)
        sys.exit(1)
