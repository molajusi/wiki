import urllib.request
import ssl
import os

raw_dir = r"Z:\wiki\raw"
os.makedirs(raw_dir, exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def download_file(url, target_name):
    target_path = os.path.join(raw_dir, target_name)
    print(f"Downloading: {target_name} from {url}", flush=True)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            content = resp.read()
            if content.startswith(b"%PDF"):
                with open(target_path, "wb") as f:
                    f.write(content)
                print(f"[OK] Saved {target_name} ({len(content):,} bytes)", flush=True)
                return True
            else:
                print(f"[WARN] {target_name}: Content is not PDF ({len(content)import urllib.request
import ssl
import os

raw_dir = r"Z:\wiki\raw"
os.makedirs(raw_dir, exist_ok=True)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def download_file(url, target_name):
    target_path = os.path.join(raw_dir, target_name)
    print(f"Downloading: {target_name} from {url}", flush=True)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            content = resp.read()
            if content.startswith(b"%PDF"):
                with open(target_path, "wb") as f:
                    f.write(content)
                print(f"[OK] Saved {target_name} ({len(content):,} bytes)", flush=True)
                return True
            else:
                print(f"[WARN] {target_name}: Content is not PDF ({len(content)} bytes).", flush=True)
                return False
    except Exception as e:
        print(f"[ERR] {target_name}: {e}", flush=True)
        return False

if __name__ == "__main__":
    download_file("https://www.diva-portal.org/smash/get/diva2:1043332/FULLTEXT01.pdf", "2013_Zagal_Dark_Patterns_in_the_Design_of_Games.pdf")
    download_file("https://www.sbgames.org/proceedings2020/IndustriaFull/209692.pdf", "2020_Oliveira_A_Framework_for_Metroidvania_Games.pdf")
    download_file("https://dl.digra.org/index.php/dl/article/download/1943/1943", "2023_Dormann_A_Classification_of_Video_Game_Cartographic_Maps.pdf")
    download_file("https://dl.digra.org/index.php/dl/article/download/702/702", "2014_Alha_Free_to_Play_Games_Professionals_Perspectives.pdf")
r/article/JAKO202035864115162.pdf", "2020_Kim_Mobile_Game_Battle_Pass_Case_Analysis.pdf")
except Exception as e:
    print("Battle pass error:", e)
