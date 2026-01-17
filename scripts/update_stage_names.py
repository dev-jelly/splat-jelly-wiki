#!/usr/bin/env python3
"""
Update Salmon Run stage names to official Korean names.
"""

import os
from pathlib import Path

# Define the replacements
REPLACEMENTS = {
    "아라마키 요새": "연어말이 요새",
    "무니・엘 해양 발전소": "뫼니 엘 해양 발전소",
    "스지코 정션 터": "연어알젓 교차로 옛터",
    "토키라즈 이부시 공방": "사계절 훈제 공방",
    "돈피코 투기장": "연어 심장 투기장",
}

# Define the files to update
FILES = [
    "/Users/jelly/personal/splat-jelly-wiki/src/content/docs/stages/index.mdx",
    "/Users/jelly/personal/splat-jelly-wiki/src/content/docs/stages/sockeye-station.mdx",
    "/Users/jelly/personal/splat-jelly-wiki/src/content/docs/stages/gone-fission-hydroplant.mdx",
    "/Users/jelly/personal/splat-jelly-wiki/src/content/docs/stages/jammin-salmon-junction.mdx",
    "/Users/jelly/personal/splat-jelly-wiki/src/content/docs/stages/salmonid-smokeyard.mdx",
    "/Users/jelly/personal/splat-jelly-wiki/src/content/docs/stages/bonerattle-arena.mdx",
]

def update_file(file_path: str) -> tuple[int, str]:
    """Update a single file with the new stage names."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    replacement_count = 0

    # Apply all replacements
    for old_name, new_name in REPLACEMENTS.items():
        if old_name in content:
            content = content.replace(old_name, new_name)
            replacement_count += content.count(new_name) - original_content.count(new_name)

    # Write back only if changes were made
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return replacement_count, "updated"
    else:
        return 0, "no changes"

def main():
    print("Updating Salmon Run stage names to official Korean names...\n")

    total_replacements = 0

    for file_path in FILES:
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            continue

        count, status = update_file(file_path)
        total_replacements += count

        file_name = Path(file_path).name
        if status == "updated":
            print(f"✓ {file_name}: {count} replacements made")
        else:
            print(f"- {file_name}: no changes needed")

    print(f"\n{'='*60}")
    print(f"Total replacements made: {total_replacements}")
    print(f"{'='*60}\n")

    print("Replacements applied:")
    for old_name, new_name in REPLACEMENTS.items():
        print(f"  • {old_name} → {new_name}")

if __name__ == "__main__":
    main()
