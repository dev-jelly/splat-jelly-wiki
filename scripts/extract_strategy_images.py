import os
import re
from bs4 import BeautifulSoup

# Map of local file name to target stage directory name
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
    f_out.write("mkdir -p public/images/stages\n")

    for filename, stage_slug in stages.items():
        filepath = os.path.join(source_dir, filename)
        if not os.path.exists(filepath):
            print(f"Skipping {filename} (not found)")
            continue
            
        print(f"Processing {filename}...")
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
            
        # Function to find image for a section
        def find_image(keyword, slug_suffix):
            # Find header containing keyword
            headers = soup.find_all(['h3', 'h4'], string=re.compile(keyword))
            if not headers:
                # Try finding in id
                headers = soup.find_all(['h3', 'h4'], id=re.compile(keyword))
            
            for header in headers:
                # Look for img in next siblings
                curr = header
                for _ in range(20): # Look ahead
                    if curr is None: break
                    curr = curr.next_element
                    if curr.name == 'img':
                        src = curr.get('src') or curr.get('data-src')
                        if src:
                            # Fix relative URLs if any (wikiwiki usually absolute or root relative)
                            if src.startswith("//"): src = "https:" + src
                            elif src.startswith("/"): src = "https://wikiwiki.jp" + src
                            
                            # Construct download command
                            out_path = f"public/images/stages/{stage_slug}/{slug_suffix}.webp"
                            f_out.write(f"mkdir -p public/images/stages/{stage_slug}\n")
                            f_out.write(f"curl -L -o '{out_path}' '{src}'\n")
                            print(f"  Found {keyword}: {src}")
                            return True
            return False

        find_image("ラッシュ", "rush-map")
        find_image("グリル", "griller-map")

print("Download script generated.")
