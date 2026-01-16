import os
import re

stages = {
    "spawning_grounds.md": "spawning-grounds",
    "sockeye_station.md": "sockeye-station",
    "marooners_bay.md": "marooners-bay",
    "salmonid_smokeyard.md": "salmonid-smokeyard",
    "gone_fission.md": "gone-fission-hydroplant",
    "jammin_salmon.md": "jammin-salmon-junction",
    "bonerattle_arena.md": "bonerattle-arena"
}

source_dir = ".sisyphus/raw_sources/stages"
output_script = "scripts/download_strategy_images.sh"

with open(output_script, "w") as f_out:
    f_out.write("#!/bin/bash\n")
    
    for filename, stage_slug in stages.items():
        filepath = os.path.join(source_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        print(f"Processing {filename}...")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Simplified regex approach
        # Look for header id or text, then find the first img src within reasonable distance
        
        def find_img_after_keyword(keyword, suffix):
            # Find the position of the keyword
            # wikiwiki anchors often look like id="h1db4f92" but the text is inside
            # We look for the text literally
            pos = content.find(keyword)
            if pos == -1:
                return
            
            # Search for img src after this position
            # <img ... src="URL" ...>
            img_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', content[pos:])
            if img_match:
                src = img_match.group(1)
                # Filter out small icons/emojis (often in tables)
                # Wikiwiki strategy maps are usually hosted on cdn.wikiwiki.jp
                if "cdn.wikiwiki.jp" in src:
                     if src.startswith("//"): src = "https:" + src
                     
                     f_out.write(f"mkdir -p public/images/stages/{stage_slug}\n")
                     f_out.write(f"curl -L -o 'public/images/stages/{stage_slug}/{suffix}.webp' '{src}'\n")
                     print(f"  Found {keyword}: {src}")

        find_img_after_keyword("ラッシュ", "rush-map")
        find_img_after_keyword("グリル", "griller-map")

print("Download script generated.")
