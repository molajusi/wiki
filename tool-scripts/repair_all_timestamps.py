# -*- coding: utf-8 -*-
import os
import glob
import re

WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CURRENT_TIME = "2026-09-04 오후 02:54:30 (KST, UTC+9)"

md_files = sorted(glob.glob(os.path.join(WIKI_DIR, "*.md")))

repaired_count = 0

for mf in md_files:
    bname = os.path.basename(mf)
    if bname in ("AGENTS.md", "README.md"):
        continue

    with open(mf, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. frontmatter 추출
    fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.S)
    if not fm_match:
        print(f"[SKIP] {bname}: No frontmatter")
        continue

    fm = fm_match.group(1)
    cm = re.search(r"^created:\s*\"?(.*?)\"?$", fm, re.M)
    cat_m = re.search(r"^category:\s*\"?(.*?)\"?$", fm, re.M)

    created_time = cm.group(1).strip() if cm else ""
    category_str = cat_m.group(1).strip() if cat_m else ""

    if not created_time:
        print(f"[WARN] {bname}: created_time empty!")
        continue

    updated_time = CURRENT_TIME

    # frontmatter updated 갱신
    content = re.sub(r'^(updated:\s*)\"[^\"]+\"', r'\1"' + updated_time + '"', content, flags=re.M)

    # 2. MD 본문 서두 정리
    body_part = content[fm_match.end():].lstrip("\n")
    lines = body_part.split("\n")

    idx = 0
    title_line = None
    sub_line = None

    while idx < len(lines):
        line_s = lines[idx].strip()
        if not line_s:
            idx += 1
            continue
        if line_s.startswith("# ") and title_line is None:
            title_line = lines[idx]
            idx += 1
            continue
        if line_s.startswith("*") and line_s.endswith("*") and not line_s.startswith("*최초") and sub_line is None:
            sub_line = lines[idx]
            idx += 1
            continue
        if line_s.startswith("**카테고리**:"):
            idx += 1
            continue
        if line_s.startswith("*최초 작성일시:") or line_s.startswith("*최초작성일시:"):
            idx += 1
            continue
        break

    rest_body = "\n".join(lines[idx:]).lstrip("\n")

    header_block = []
    if title_line:
        header_block.append(title_line)
    if sub_line:
        header_block.append(sub_line)
    header_block.append("")
    header_block.append(f"**카테고리**: {category_str}  ")
    header_block.append(f"*최초 작성일시: {created_time} | 최종 수정일시: {updated_time}*")
    header_block.append("")

    new_fm_part = content[:fm_match.end()]
    new_md = new_fm_part + "\n\n" + "\n".join(header_block) + "\n" + rest_body
    if not new_md.endswith("\n"):
        new_md += "\n"

    with open(mf, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_md)

    # 3. HTML meta 태그 완벽 복원
    hf = mf.replace(".md", ".html")
    if os.path.exists(hf):
        with open(hf, "r", encoding="utf-8") as f:
            hcontent = f.read()

        new_meta_div = f'<div class="meta">최초 작성일시: {created_time} | 최종 수정일시: {updated_time}</div>'
        hcontent = re.sub(r'<div class=["\']meta["\'][^>]*>.*?</div>', new_meta_div, hcontent, flags=re.S)

        with open(hf, "w", encoding="utf-8", newline="\n") as f:
            f.write(hcontent)

    repaired_count += 1
    print(f"[REPAIRED] {bname} (created: {created_time})")

# 4. index.html meta 갱신
index_path = os.path.join(WIKI_DIR, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        icontent = f.read()
    new_imeta = f'<div class="meta" style="font-size: 0.85rem; color: #adb5bd; margin-top: 0.2rem;">최초 작성일시: 2026-08-22 오후 12:55:07 (KST, UTC+9) | 최종 수정일시: {CURRENT_TIME}</div>'
    icontent = re.sub(r'<div class=["\']meta["\'][^>]*>.*?</div>', new_imeta, icontent, flags=re.S)
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(icontent)
    print("[REPAIRED] index.html")

print(f"Total repaired: {repaired_count} documents")
