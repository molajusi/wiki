# -*- coding: utf-8 -*-
"""index.md(카드 그리드 레이아웃 전용 SSOT)를 index.html로 렌더링하는 전용 스크립트.

render_md.py는 일반 주제 문서(1.개요~N.참고자료 골격)를 렌더링하며 index는 카드 그리드
레이아웃이 달라 명시적으로 제외한다(render_md.py EXCLUDE_BASENAMES). 이 스크립트가 그 대신
index.md → index.html 변환을 전담한다.

index.md 구조 규약:
- frontmatter + 제목/부제/카테고리/일시 4줄 복창(다른 문서와 동일, build_header가 재생성) 다음에
  오는 산문 단락은 최상단 개요(.index-overview)로 렌더링된다.
- `##` 섹션은 카드 그리드 대분류 하나에 대응한다. 문서상 첫 번째 `##`는 admin-section(관리
  카드 테마)으로, 그 뒤는 모두 knowledge-section(일반 카테고리 카드)으로 렌더링된다.
- `##` 섹션 안의 `###`는 카드 하나(category-card, 첫 섹션이면 admin-card)에 대응한다. `###`
  제목 바로 다음 줄이 목록이 아니면 카드 설명(.category-desc)으로 렌더링된다.
- `- [라벨](href)` 목록은 doc-list로 렌더링된다. 실제 중첩 <ul>은 만들지 않고(원본 관례),
  들여쓰기 2칸당 한 단계씩 padding-left/font-size 인라인 스타일로 시각적 위계만 표현한다.

<nav>/<footer>는 render_md.py와 동일하게 기존 index.html에서 그대로 가져오되, footer에는
다른 문서처럼 "마크다운 정본" 버튼을 추가한다(index.md 신설 이전에는 없었음).

실행: python render_index.py
검증: audit_wiki.py의 check_pair_parity가 index.md/index.html의 h2·링크 목록 정합성을 대조한다.
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from render_md import inline_md_to_html, read_frontmatter, strip_title_restatement, build_header  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def parse_doc_items(lines):
    """`- [라벨](href)` 줄만 뽑아 (들여쓰기 칸수, 라벨, href) 목록으로 만들고,
    실제 등장한 들여쓰기 칸수 집합을 0부터 순서대로 depth 0/1/2...로 정규화한다."""
    raw = []
    for line in lines:
        m = re.match(r"^(\s*)-\s+\[(.+?)\]\(([^)]+)\)\s*$", line)
        if m:
            raw.append((len(m.group(1)), m.group(2), m.group(3)))
    indents = sorted(set(i for i, _, _ in raw))
    depth_of = {ind: d for d, ind in enumerate(indents)}
    return [(depth_of[ind], label, href) for ind, label, href in raw]


def render_doc_list(lines):
    items = parse_doc_items(lines)
    li_html = []
    for depth, label, href in items:
        style = ""
        if depth == 1:
            style = ' style="padding-left: 1rem; font-size: 0.9rem;"'
        elif depth >= 2:
            style = ' style="padding-left: 1.5rem; font-size: 0.85rem;"'
        li_html.append(
            '                        <li>\n'
            '                            <a class="doc-link" href="%s"%s>%s</a>\n'
            '                        </li>' % (href, style, inline_md_to_html(label))
        )
    return '                    <ul class="doc-list">\n%s\n                    </ul>' % "\n".join(li_html)


def split_sections(lines, marker):
    """lines를 정확히 `marker`(예: "## ")로 시작하는 줄 기준으로 (제목, 본문줄들) 목록으로 분리한다.
    첫 marker 등장 이전의 줄들은 preface로 별도 반환한다."""
    preface = []
    sections = []
    current_title = None
    current_lines = []
    for line in lines:
        if line.startswith(marker):
            if current_title is None:
                preface = current_lines
            else:
                sections.append((current_title, current_lines))
            current_title = line[len(marker):].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_title is not None:
        sections.append((current_title, current_lines))
    elif not sections:
        preface = current_lines
    return preface, sections


def render_card(h3_title, body_lines, is_admin):
    desc_lines = []
    list_start = 0
    for idx, line in enumerate(body_lines):
        if not line.strip():
            continue
        if re.match(r"^\s*-\s+\[", line):
            list_start = idx
            break
        desc_lines.append(line.strip())
    else:
        list_start = len(body_lines)

    badge = ' <span class="badge-admin">System Admin</span>' if is_admin else ""
    desc_html = ""
    if desc_lines:
        desc_html = '\n                    <p class="category-desc">%s</p>' % inline_md_to_html(" ".join(desc_lines))
    list_html = render_doc_list(body_lines[list_start:])

    card_class = "category-card admin-card" if is_admin else "category-card"
    return (
        '                <article class="%s">\n'
        '                    <h3>%s%s</h3>%s\n'
        '%s\n'
        '                </article>'
    ) % (card_class, inline_md_to_html(h3_title), badge, desc_html, list_html)


def render_body(body_md):
    lines = body_md.split("\n")
    preface_lines, h2_sections = split_sections(lines, "## ")

    overview_paras = [p.strip() for p in "\n".join(preface_lines).split("\n\n") if p.strip()]
    overview_html = "\n".join(
        '        <p class="index-overview">%s</p>' % inline_md_to_html(" ".join(p.split("\n")))
        for p in overview_paras
    )

    section_htmls = []
    for sec_idx, (h2_title, h2_lines) in enumerate(h2_sections):
        is_admin_section = (sec_idx == 0)
        _, h3_sections = split_sections(h2_lines, "### ")
        cards = [render_card(h3_title, h3_lines, is_admin_section) for h3_title, h3_lines in h3_sections]
        sec_class = "admin-section" if is_admin_section else "knowledge-section"
        section_htmls.append(
            '        <section class="%s">\n'
            '            <h2 class="section-title">%s</h2>\n'
            '            <div class="wiki-grid">\n'
            '%s\n'
            '            </div>\n'
            '        </section>'
            % (sec_class, inline_md_to_html(h2_title), "\n".join(cards))
        )

    return overview_html + "\n\n" + "\n\n".join(section_htmls)


def build_footer():
    return (
        '    <footer>\n'
        '        <div class="footer-container">\n'
        '            <div class="footer-brand">\n'
        '                <span class="footer-title">지식 위키 메인 색인 (Knowledge Wiki Index)</span>\n'
        '                <span class="footer-desc">2계층 지식 아키텍처 (Markdown SSOT + HTML5 View)</span>\n'
        '            </div>\n'
        '            <div class="footer-nav">\n'
        '                <a href="index.html" class="footer-btn">\n'
        '                    <span class="footer-btn-icon">🏠</span>\n'
        '                    <span class="footer-btn-text">메인 색인</span>\n'
        '                </a>\n'
        '                <a href="index.md" class="footer-btn">\n'
        '                    <span class="footer-btn-icon">📄</span>\n'
        '                    <span class="footer-btn-text">마크다운 정본</span>\n'
        '                </a>\n'
        '                <a href="AGENTS.md" class="footer-btn">\n'
        '                    <span class="footer-btn-icon">🤖</span>\n'
        '                    <span class="footer-btn-text">에이전트 가이드</span>\n'
        '                </a>\n'
        '                <a href="wiki_documentation_standards.html" class="footer-btn">\n'
        '                    <span class="footer-btn-icon">📐</span>\n'
        '                    <span class="footer-btn-text">위키 작성 표준</span>\n'
        '                </a>\n'
        '                <a href="#" class="footer-btn">\n'
        '                    <span class="footer-btn-icon">⬆️</span>\n'
        '                    <span class="footer-btn-text">맨 위로</span>\n'
        '                </a>\n'
        '            </div>\n'
        '            <div class="footer-meta">\n'
        '                <span>지식 저장소: <code>Z:\\wiki</code></span>\n'
        '                <span>•</span>\n'
        '                <span>보좌 에이전트: <code>jane (Antigravity CLI)</code></span>\n'
        '            </div>\n'
        '        </div>\n'
        '    </footer>'
    )


def render_index():
    md_path = os.path.join(WIKI_DIR, "index.md")
    html_path = os.path.join(WIKI_DIR, "index.html")
    md_text = io.open(md_path, encoding="utf-8").read()
    fm, body_md = read_frontmatter(md_text)
    body_md = strip_title_restatement(body_md)

    old_html = io.open(html_path, encoding="utf-8").read()

    header_m = re.search(r"[ \t]*<header([^>]*)>.*?</header>", old_html, re.S)
    if not header_m:
        print("[FAIL] index.html — <header> 블록을 못 찾음")
        return False
    new_header = build_header(fm, header_m.group(1))
    new_html = old_html[:header_m.start()] + new_header + old_html[header_m.end():]

    main_m = re.search(r"[ \t]*<main([^>]*)>.*?</main>", new_html, re.S)
    if not main_m:
        print("[FAIL] index.html — <main> 블록을 못 찾음")
        return False
    main_inner = render_body(body_md)
    new_main = "    <main%s>\n%s\n    </main>" % (main_m.group(1), main_inner)
    new_html = new_html[:main_m.start()] + new_main + new_html[main_m.end():]

    footer_m = re.search(r"[ \t]*<footer([^>]*)>.*?</footer>", new_html, re.S)
    if footer_m:
        new_html = new_html[:footer_m.start()] + build_footer() + new_html[footer_m.end():]

    io.open(html_path, "w", encoding="utf-8", newline="\n").write(new_html)
    print("[완료] index.html 재생성 (본문 %d자 -> HTML %d자)" % (len(body_md), len(main_inner)))
    return True


if __name__ == "__main__":
    ok = render_index()
    sys.exit(0 if ok else 1)



