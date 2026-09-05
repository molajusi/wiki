# -*- coding: utf-8 -*-
import os, re

WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
UPDATE_TIME = "2026-09-04 오후 02:35:45 (KST, UTC+9)"
REASON = "카테고리 체계 표준화 반영"

# 1. 게임 디자인 문서 (10건)
game_docs = [
    "alwa_series_analysis",
    "game_controller_input_design_and_standards",
    "game_gating_mechanisms",
    "metroidvania_and_cartography_game_design",
    "metroidvania_death_and_respawn_mechanics",
    "metroidvania_genre_analysis",
    "metroidvania_map_and_spatial_cognition",
    "metroidvania_mechanics_and_level_design",
    "roguelike_genre_characteristics",
    "shantae_series_analysis",
]

# 2. 고립 인문 문서 (1건)
folklore_docs = [
    "korean_traditional_non_shamanic_magic",
]

# 3. 기술/학술 문서 (4건)
tech_docs = [
    "llm_wiki_system_architecture",
    "llm_wiki_format_debate",
    "llm_wiki_construction_guide",
    "library_book_request_prompt",
]

def update_doc(basename, new_cat, add_tags=None):
    md_path = os.path.join(WIKI_DIR, basename + ".md")
    html_path = os.path.join(WIKI_DIR, basename + ".html")
    
    # MD 업데이트
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # frontmatter category
    md_text = re.sub(r'^(category:\s*)\"[^\"]+\"', r'\1"' + new_cat + '"', md_text, flags=re.M)
    md_text = re.sub(r'^(category:\s*)[^\n\"\']+$', r'\1' + new_cat, md_text, flags=re.M)

    # frontmatter updated
    md_text = re.sub(r'^(updated:\s*)\"[^\"]+\"', r'\1"' + UPDATE_TIME + ' — ' + REASON + '"', md_text, flags=re.M)

    # frontmatter tags 추가 (필요시)
    if add_tags:
        for t in add_tags:
            if f'"{t}"' not in md_text:
                md_text = re.sub(r'^(tags:\s*\[)(.*?)(\])', r'\1\2, "' + t + r'"\3', md_text, flags=re.M)

    # 본문 서두의 **카테고리**: ...
    md_text = re.sub(r'^\*\*카테고리\*\*:\s*.*$', r'**카테고리**: ' + new_cat + '  ', md_text, flags=re.M)

    # 본문 서두의 *최초 작성일시... | 최종 수정일시: ...*
    md_text = re.sub(r'(\*최초 작성일시: [^|]+ \|\s*최종 수정일시: )[^*]+(\*)', r'\1' + UPDATE_TIME + ' — ' + REASON + r'\2', md_text)

    with open(md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(md_text)

    # HTML 업데이트
    with open(html_path, "r", encoding="utf-8") as f:
        html_text = f.read()

    # header category
    html_text = re.sub(r'<div class="category">[^<]+</div>', f'<div class="category">카테고리: {new_cat}</div>', html_text)

    # header meta updated
    html_text = re.sub(r'(최초 작성일시: [^|]+ \|\s*최종 수정일시: )[^<—]+( — [^<]+)?', r'\1' + UPDATE_TIME + ' — ' + REASON, html_text)

    with open(html_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(html_text)

    print(f"[OK] {basename} -> {new_cat}")

# 실행
print("=== 카테고리 일괄 표준화 시작 ===")
for b in game_docs:
    update_doc(b, "게임 디자인 및 분석 (Game Design & Taxonomy)")

for b in folklore_docs:
    update_doc(b, "인문 및 서사학 (Humanities & Narratology)", add_tags=["한국역사민속학", "인류학"])

for b in tech_docs:
    update_doc(b, "기술 및 학술 (Technology & Science)")

print("=== 완료 ===")
