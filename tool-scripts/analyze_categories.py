# -*- coding: utf-8 -*-
import os
import glob
import re
from bs4 import BeautifulSoup

WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def run():
    md_files = sorted(glob.glob(os.path.join(WIKI_DIR, "*.md")))
    docs = []
    for md_path in md_files:
        basename = os.path.basename(md_path)
        if basename in ("AGENTS.md", "README.md"):
            continue
        with open(md_path, "r", encoding="utf-8") as f:
            content = f.read()

        fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.S)
        title = ""
        category_md = ""
        tags = ""
        if fm_match:
            fm = fm_match.group(1)
            tm = re.search(r"^title:\s*[\"']?(.*?)[\"']?$", fm, re.M)
            if tm:
                title = tm.group(1).strip("\"'")
            cm = re.search(r"^category:\s*[\"']?(.*?)[\"']?$", fm, re.M)
            if cm:
                category_md = cm.group(1).strip("\"'")
            tg = re.search(r"^tags:\s*\[(.*?)\]", fm, re.M)
            if tg:
                tags = tg.group(1).strip()

        # HTML 파일에서 category 추출
        html_path = os.path.join(WIKI_DIR, basename.replace(".md", ".html"))
        category_html = ""
        if os.path.exists(html_path):
            with open(html_path, "r", encoding="utf-8") as f:
                hcontent = f.read()
            hcm = re.search(r'<div class=["\']category["\']>(.*?)</div>', hcontent)
            if hcm:
                category_html = hcm.group(1).strip()

        docs.append({
            "file": basename,
            "title": title,
            "category_md": category_md,
            "category_html": category_html,
            "tags": tags,
        })

    # index.html 파싱
    index_path = os.path.join(WIKI_DIR, "index.html")
    index_cards = {}
    doc_to_card = {}
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        for sec in soup.find_all("section"):
            sec_title_el = sec.find(class_="section-title")
            sec_title = sec_title_el.get_text(strip=True) if sec_title_el else "미지정 섹션"

            for card in sec.find_all(class_="category-card"):
                h3_el = card.find("h3")
                card_title = h3_el.get_text(strip=True) if h3_el else "미지정 카드"
                card_key = f"{sec_title} > {card_title}"
                index_cards[card_key] = []

                for a in card.find_all("a", class_="doc-link"):
                    href = a.get("href", "")
                    doc_text = a.get_text(strip=True)
                    index_cards[card_key].append((href, doc_text))
                    doc_to_card[href] = card_key

    # 결과 리포트 작성
    report = []
    report.append("=" * 80)
    report.append(f"Z:\\wiki 카테고리 분류 체계 적절성 분석 리포트 (총 {len(docs)}개 문서)")
    report.append("=" * 80)

    # 1. 문서 메타데이터 카테고리 현황
    cat_groups = {}
    for d in docs:
        c = d["category_md"] or "(카테고리 누락)"
        cat_groups.setdefault(c, []).append(d)

    report.append("\n[1] 문서별 category 메타데이터 현황 (.md 기준)")
    report.append("-" * 80)
    for cat, items in sorted(cat_groups.items(), key=lambda x: len(x[1]), reverse=True):
        report.append(f"\n■ [{cat}] — 총 {len(items)}건")
        for it in items:
            hfile = it["file"].replace(".md", ".html")
            card_info = doc_to_card.get(hfile, "index.html 미등록")
            report.append(f"   - {it['file']}: {it['title']}")
            report.append(f"     * HTML 카테고리: {it['category_html']}")
            report.append(f"     * index.html 배치: {card_info}")

    # 2. index.html 카테고리 카드별 현황
    report.append("\n\n" + "=" * 80)
    report.append("[2] index.html 상의 카테고리 카드별 배치 현황")
    report.append("-" * 80)
    for card_key, docs_in_card in sorted(index_cards.items()):
        report.append(f"\n■ {card_key} — 총 {len(docs_in_card)}건")
        for href, dtext in docs_in_card:
            report.append(f"   - {href}: {dtext}")

    # 3. 불일치 및 정합성 문제 분석
    report.append("\n\n" + "=" * 80)
    report.append("[3] 카테고리 분류 정합성 및 구조적 문제점 분석")
    report.append("-" * 80)

    # (1) index.html 미등록 문서
    unindexed = [d for d in docs if d["file"].replace(".md", ".html") not in doc_to_card]
    report.append(f"\n(1) index.html 미등록 문서: {len(unindexed)}건")
    for u in unindexed:
        report.append(f"   - {u['file']} ({u['title']})")

    # (2) .md 카테고리와 .html 카테고리 불일치
    mismatched_cats = []
    for d in docs:
        hcat = d["category_html"].replace("카테고리: ", "").replace("구분: ", "").strip()
        mcat = d["category_md"].strip()
        if hcat and mcat != hcat:
            mismatched_cats.append((d["file"], mcat, hcat))
    report.append(f"\n(2) .md vs .html 카테고리 표기 불일치: {len(mismatched_cats)}건")
    for f, mc, hc in mismatched_cats:
        report.append(f"   - {f}: MD=[{mc}] vs HTML=[{hc}]")

    # (3) 메타데이터 카테고리와 index.html 카드명 불일치 분석
    report.append("\n(3) 메타데이터 카테고리와 index.html 카드 분류 대조:")
    for d in docs:
        hfile = d["file"].replace(".md", ".html")
        card = doc_to_card.get(hfile, "미등록")
        mcat = d["category_md"]
        report.append(f"   - {d['file']}: 메타데이터=[{mcat}] ➔ index.html=[{card}]")

    report_text = "\n".join(report)
    out_path = os.path.join(WIKI_DIR, "tool-scripts", "category_audit.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report_text)
    print("Report written to:", out_path)

if __name__ == "__main__":
    run()

