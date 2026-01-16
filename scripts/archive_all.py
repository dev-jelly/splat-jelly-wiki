import urllib.request
import os
import time

urls = {
    "system/overview.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3",
    "enemies/index.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E",
    "enemies/bosses.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%AA%E3%82%AA%E3%83%A2%E3%83%8E%E3%82%B7%E3%83%A3%E3%82%B1",
    "enemies/small_fry.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B7%E3%83%A3%E3%82%B1%E3%81%AE%E7%A8%AE%E9%A1%9E/%E3%82%B6%E3%82%B3%E3%82%B7%E3%83%A3%E3%82%B1",
    "system/special_waves.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%89%B9%E6%AE%8A%E3%81%AA%E7%8A%B6%E6%B3%81",
    "stages/index.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8",
    "stages/spawning_grounds.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%B7%E3%82%A7%E3%82%B1%E3%83%8A%E3%83%80%E3%83%A0",
    "stages/sockeye_station.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%82%A2%E3%83%A9%E3%83%9E%E3%82%AD%E7%A0%A6",
    "stages/marooners_bay.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%2F%E3%83%96%E3%83%A9%E3%82%B3",
    "stages/salmonid_smokeyard.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%88%E3%82%AD%E3%82%B7%E3%83%A9%E3%82%BA%E3%81%84%E3%81%B6%E3%81%97%E5%B7%A5%E6%88%BF",
    "stages/gone_fission.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%A0%E3%83%8B%EF%BD%A5%E3%82%A8%E3%83%BC%E3%83%AB%E6%B5%B7%E6%B4%8B%E7%99%BA%E9%9B%BB%E6%89%80",
    "stages/jammin_salmon.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%81%99%E3%81%98%E3%81%93%E3%82%B8%E3%83%A3%E3%83%B3%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3%E8%B7%A1",
    "stages/bonerattle_arena.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%81%A9%E3%82%93%E3%81%B4%E3%81%93%E9%97%98%E6%8A%80%E5%A0%B4",
    "system/weapons.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E7%B7%A8%E6%88%90%E8%A9%95%E4%BE%A1",
    "system/big_run_strategy.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%83%93%E3%83%83%E3%82%B0%E3%83%A9%E3%83%B3/%E6%94%BB%E7%95%A5"
}

base_path = ".sisyphus/raw_sources/"

for filename, url in urls.items():
    full_path = os.path.join(base_path, filename)
    print(f"Fetching {url} -> {full_path}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        time.sleep(1) # Be polite
    except Exception as e:
        print(f"Error fetching {url}: {e}")

print("Done.")
