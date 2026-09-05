# -*- coding: utf-8 -*-
import os
import glob
import re

WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
md_files = sorted(glob.glob(os.path.join(WIKI_DIR, "*.md")))

out_lines = [f"Total MD files: {len(md_files)}"]

for mf in md_files:
    bname = os.path.basename(mf)
    if bname in ("AGENTS.md", "README.md"):
        continue
    with open(mf, "r", encoding="utf-8") as f:
        content = f.read()

    fm_c = re.search(r"^created:\s*\"?(.*?)\"?$", content, re.M)
    fm_u = re.search(r"^updated:\s*\"?(.*?)\"?$", content, re.M)
    c_val = fm_c.group(1).strip() if fm_c else "FM created 누락"
    u_val = fm_u.group(1).strip() if fm_u else "FM updated 누락"

    meta_lines = [line.strip() for line in content.split("\n") if "작성일시" in line or "수정일시" in line]

    hf = mf.replace(".md", ".html")
    h_val = "HTML 없음"
    if os.path.exists(hf):
        with open(hf, "r", encoding="utf-8") as f:
            hcontent = f.read()
        hm = re.search(r'<div class=["\']meta["\'][^>]*>(.*?)</div>', hcontent, re.S)
        h_val = hm.group(1).strip() if hm else "HTML div.meta 누락"

    out_lines.append(f"\n[{bname}]")
    out_lines.append(f"  - FM created: {c_val}")
    out_lines.append(f"  - FM updated: {u_val}")
    out_lines.append(f"  - MD lines with 일시 ({len(meta_lines)}개):")
    for ml in meta_lines:
        out_lines.append(f"      {ml}")
    out_lines.append(f"  - HTML meta: {h_val}")

out_path = os.path.join(WIKI_DIR, "tool-scripts", "timestamp_audit_report.txt")
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print(f"Report written to {out_path}")
