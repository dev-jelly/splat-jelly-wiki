import re
import os

source_file = ".sisyphus/raw_sources/enemies/bosses.html"

if not os.path.exists(source_file):
    # Fallback to the markdown file if html is not there (the previous archive script saved as .md but it was html content)
    source_file = ".sisyphus/raw_sources/enemies/bosses.md"

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Simple regex to find boss sections and extract HP/Damage if possible
# This is a heuristic extraction to guide the writing.
bosses = {
    "バクダン": "Steelhead",
    "カタパッド": "Flyfish",
    "テッパン": "Scrapper",
    "ヘビ": "Steel Eel",
    "タワー": "Stinger",
    "モグラ": "Maws",
    "コウモリ": "Drizzler",
    "ハシラ": "Fish Stick",
    "ダイバー": "Flipper-Flopper",
    "ナベブタ": "Slammin' Lid",
    "テッキュウ": "Big Shot"
}

print("--- Boss Data Extraction ---")
for jp_name, en_name in bosses.items():
    print(f"\nScanning for {jp_name} ({en_name})...")
    # Find the section
    idx = content.find(jp_name)
    if idx != -1:
        # Extract a chunk of text after the name to find HP/Damage numbers
        chunk = content[idx:idx+2000]
        # Look for HP patterns like "HP: 300" or similar in table cells
        # Wikiwiki often uses |HP|300| format
        hp_match = re.search(r'HP.*?(\d{3,5})', chunk)
        if hp_match:
            print(f"  HP: {hp_match.group(1)}")
        else:
            print("  HP: Not found in immediate context")
            
        # Look for other keywords
        if "即死" in chunk: print("  Note: Instant death mechanics mentioned")
        if "ボム" in chunk: print("  Note: Bomb usage mentioned")
        if "弱点" in chunk: print("  Note: Weak point mentioned")

print("\nDone.")
