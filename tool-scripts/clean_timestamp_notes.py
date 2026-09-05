# -*- coding: utf-8 -*-
import os, glob, re

WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

md_files = glob.glob(os.path.join(WIKI_DIR, "*.md"))
html_files = glob.glob(os.path.join(WIKI_DIR, "*.html"))

cleaned_count = 0

# 1. MD 파일 정리
for mf in md_files:
    with open(mf, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content
    # frontmatter: updated: "2026-09-04 오후 02:35:45 (KST, UTC+9) — ..." -> updated: "2026-09-04 오후 02:35:45 (KST, UTC+9)"
    content = re.sub(r'^(updated:\s*\"[^\"]+?)\s*—\s*[^\"]*(\")', r'\1\2', content, flags=re.M)
    
    # 본문: *최초 작성일시: ... | 최종 수정일시: 2026-09-04 오후 02:35:45 (KST, UTC+9) — ...*
    content = re.sub(r'(\*최초 작성일시:[^*|]+\|\s*최종 수정일시:[^*]+?)\s*—\s*[^*]*(\*)', r'\1\2', content)

    if content != orig:
        with open(mf, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        cleaned_count += 1
        print(f"[CLEAN MD] {os.path.basename(mf)}")

# 2. HTML 파일 정리
for hf in html_files:
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content
    # header meta: 최초 작성일시: ... | 최종 수정일시: 2026-09-04 오후 02:35:45 (KST, UTC+9) — ...</div>
    content = re.sub(r'(최초 작성일시:[^<|]+\|\s*최종 수정일시:[^<]+?)\s*—\s*[^<]*(</div>)', r'\1\2', content)

    if content != orig:
        with open(hf, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        cleaned_count += 1
        print(f"[CLEAN HTML] {os.path.basename(hf)}")

print(f"Total cleaned files: {cleaned_count}")
