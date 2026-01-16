import urllib.request
import os
import time

urls = {
    "enemies/bosses.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%AA%E3%82%AA%E3%83%A2%E3%83%8E%E3%82%B7%E3%83%A3%E3%82%B1",
    "stages/marooners_bay.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E9%9B%A3%E7%A0%B4%E8%88%B9%E3%83%89%E3%83%B3%E3%83%BB%E3%83%96%E3%83%A9%E3%82%B3",
    "stages/gone_fission.md": "https://wikiwiki.jp/splatoon3mix/%E3%82%B5%E3%83%BC%E3%83%A2%E3%83%B3%E3%83%A9%E3%83%B3/%E3%82%B9%E3%83%86%E3%83%BC%E3%82%B8/%E3%83%A0%E3%83%8B%EF%BD%A5%E3%82%A8%E3%83%BC%E3%83%AB%E6%B5%B7%E6%B4%8B%E7%99%BA%E9%9B%BB%E6%89%80"
}

base_path = ".sisyphus/raw_sources/"

for filename, url in urls.items():
    full_path = os.path.join(base_path, filename)
    print(f"Retrying {url} -> {full_path}")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
        time.sleep(1)
    except Exception as e:
        print(f"Error fetching {url}: {e}")

print("Done.")
