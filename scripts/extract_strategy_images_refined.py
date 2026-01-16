import os
import re
from urllib.parse import unquote

# Map local file -> target directory
stages = {
    "spawning_grounds.md": "spawning-grounds",
    "sockeye_station.md": "sockeye-station",
    "marooners_bay.md": "marooners-bay",
    "salmonid_smokeyard.md": "salmonid-smokeyard",
    "gone_fission.md": "gone-fission-hydroplant",
    "jammin_salmon.md": "jammin-salmon-junction",
    "bonerattle_arena.md": "bonerattle-arena",
    "big_run_strategy.md": "big-run" 
    # Big run usually has one page for all, but I might need to split images by stage name if possible.
    # Actually, big run images might be less organized. I'll dump them in a 'big-run' folder for now or specific folders if I can detect the stage name.
}

source_dir = ".sisyphus/raw_sources/stages"
system_dir = ".sisyphus/raw_sources/system" # For big run

output_script = "scripts/download_strategy_images_v2.sh"

def get_stage_slug_from_filename(filename, img_alt, img_url):
    # Heuristic to map generic Big Run images to specific stages if possible
    decoded_url = unquote(img_url)
    if "スメーシー" in decoded_url or "Wahoo" in img_alt: return "maho-mahi-resort"
    if "美術大学" in decoded_url or "Inkblot" in img_alt: return "undam-burger"
    if "マテガイ" in decoded_url or "Undertow" in img_alt: return "undertow-canyon"
    if "ナンプラー" in decoded_url or "Umami" in img_alt: return "umami-ruins"
    if "タラポート" in decoded_url or "Barnacle" in img_alt: return "stageworks"
    if "ゴンズイ" in decoded_url or "Scorch" in img_alt: return "familys-bend"
    if "ユノハナ" in decoded_url: return "yunohana-canyon" # Not in my list but good to have
    if "カジキ" in decoded_url: return "shoreside-scrapyard" # Crableg
    return "big-run" # Default fallback

with open(output_script, "w") as f_out:
    f_out.write("#!/bin/bash\n")
    
    # Process standard stages
    for filename, stage_slug in stages.items():
        filepath = os.path.join(source_dir, filename)
        if not os.path.exists(filepath):
            # Check system dir for big run
            filepath = os.path.join(system_dir, filename)
            if not os.path.exists(filepath):
                continue
        
        print(f"Scanning {filename}...")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Regex to find all images
        # <img ... src="..." ... alt="..." ...>
        # We need to capture src and alt
        # This regex is a bit complex to handle attributes in any order
        
        # Simpler approach: find all <img tags and parse them
        img_tags = re.findall(r'<img[^>]+>', content)
        
        for img in img_tags:
            src_match = re.search(r'src=["\']([^"\']+)["\']', img)
            alt_match = re.search(r'alt=["\']([^"\']+)["\']', img)
            
            if not src_match: continue
            src = src_match.group(1)
            alt = alt_match.group(1) if alt_match else ""
            
            # Decode URL to check for Japanese keywords
            decoded_src = unquote(src)
            
            # Filter logic
            is_strategy = False
            img_type = "misc"
            
            if "ラッシュ" in decoded_src or "ラッシュ" in alt:
                is_strategy = True
                img_type = "rush"
            elif "グリル" in decoded_src or "グリル" in alt:
                is_strategy = True
                img_type = "griller"
            elif "キンシャケ" in decoded_src or "間欠泉" in decoded_src or "水脈" in decoded_src: # Goldie Seeking / Geyser
                is_strategy = True
                img_type = "goldie"
            elif "ドスコイ" in decoded_src:
                is_strategy = True
                img_type = "cohock"
            elif "マップ" in decoded_src or "Map" in alt or "全体" in decoded_src:
                is_strategy = True
                img_type = "map"
            elif "カタパ" in decoded_src and "ワンパン" in decoded_src: # Flyfish one-shot spots
                is_strategy = True
                img_type = "flyfish-spot"
                
            if is_strategy and "cdn.wikiwiki.jp" in src:
                if src.startswith("//"): src = "https:" + src
                
                # Determine output directory
                target_slug = stage_slug
                if filename == "big_run_strategy.md":
                    target_slug = get_stage_slug_from_filename(filename, alt, src)
                
                # Generate unique filename to avoid collisions
                # Hash the src to get a unique suffix or use the original filename
                original_name = src.split("/")[-1].split("?")[0]
                # Clean up filename
                safe_name = re.sub(r'[^\w\-\.]', '_', unquote(original_name))
                
                out_path = f"public/images/stages/{target_slug}/{img_type}-{safe_name}"
                if not out_path.endswith(".webp") and not out_path.endswith(".png") and not out_path.endswith(".jpg") and not out_path.endswith(".jpeg"):
                     out_path += ".webp" # Default extension if missing
                
                f_out.write(f"mkdir -p public/images/stages/{target_slug}\n")
                f_out.write(f"curl -L -o '{out_path}' '{src}'\n")
                # print(f"  Queued {img_type}: {out_path}")

print("Download script v2 generated.")
