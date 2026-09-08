# -*- coding: utf-8 -*-
"""Z:\\wiki 2계층 위키 — Markdown(.md) 본문을 HTML5(.html)로 렌더링하는 간이 엔진.

배경: AGENTS.md 4절 1항의 "동시 생성"은 .md/.html을 각각 손으로(모델이) 써낸다는 뜻이라
기계적 파생 관계가 아니었다. 2026-08-27 감사에서 20쌍 중 16쌍이 실제로 어긋나 있는 게
확인됐다(소제목 텍스트 자체가 다른 경우 포함). 이 스크립트는 .md를 진짜 정본으로 만들어
.html을 그 .md에서 매번 다시 만들도록 하기 위한 최소 렌더러다.

무엇을 바꾸는가:
- <header> 블록(h1/subtitle/category/meta)은 .md의 frontmatter에서 다시 만든다.
- <article> 안쪽 본문은 .md 본문(frontmatter 뒤, 프론트매터를 사람이 읽기 좋게 반복한
  "# 제목/*부제*/**카테고리**.../*일시*" 4줄은 건너뛰고 <context> 블록부터)을 렌더링해 채운다.
- <footer> 블록은 2계층 위키 표준 UI(메인 색인, 마크다운 정본, 원천 데이터, 에이전트 가이드,
  맨 위로 이동 버튼 및 원천 데이터 파일 경로)로 자동 생성·동기화한다.
- <nav>는 건드리지 않는다 — 문서마다 다른 고유 상호 참조 링크망을 보존하기 위함이다.

무엇이 마크다운 문법이고 무엇이 원시 HTML 그대로인가(wiki_documentation_standards.md 3.9절):
- 변환: `#`~`######` 헤딩(섹션은 `<section>`으로 묶는다), 문단, 목록(중첩 지원), 파이프 표,
  인라인 `**굵게**`→`<b>`(AGENTS.md 4절 5항 관례), `*기울임*`→`<i>`, `` `코드` ``→`<code>`,
  `[텍스트](URL)`→`<a href>`, 각주식 인용 `[[N]](#ref-N)`→`<sup class="citation"><a>...</a></sup>`.
- 그대로 통과(원문 한 글자도 안 건드림): **표준 HTML5 태그**로 시작하는 블록 전부
  (`<div>`·`<table>`·`<ul>`/`<ol>`(class 있든 없든 원시로 쓴 것)·`<blockquote>`·`<pre>`·
  `<details>`·`<svg>`·`<header>`/`<nav>`/`<footer>` 등, `KNOWN_HTML_TAGS` 참조).
- 투명 래퍼(태그만 벗기고 내용은 재귀적으로 렌더링): **표준 HTML5 태그가 아닌 모든 태그**
  (`<context>`·`<definitions>`·`<references>`뿐 아니라 문서마다 지어낸 `<theory>`·`<overview>`
  같은 것도 포함) — 표준 태그 목록에 없으면 자동으로 이렇게 처리된다. 최종 HTML에는 이런
  커스텀 태그 자체가 남지 않는다.

한계(알려진 단순화, 필요해지면 보강):
- 파이프 표 셀 안의 이스케이프된 파이프 문자(백슬래시+세로줄)는 지원하지 않는다(현재 위키에 그런 사례 없음).
- frontmatter 뒤 "# 제목/*부제*/**카테고리**.../*일시*" 4줄은 정확히 그 4가지 패턴에 매칭될 때만
  건너뛴다 — 그 사이에 실제 문장(예: 관련 문서 링크)이 끼어 있으면 정상적으로 본문에 남는다.
- `<nav>`는 문서 고유 링크망 보호를 위해 수동 관리하며, `<header>`/`<article>`/`<footer>`는 렌더러가 자동 관리한다.

실행: python render_md.py <이름, 확장자 없이>   예) python render_md.py llm_wiki_format_debate
      python render_md.py --all   (index.html 자신은 카드 그리드 레이아웃이라 제외)

검증: `tool-scripts/audit_wiki.py`가 렌더링 직후 .md/.html의 소제목·링크 목록 정합성을
자동 대조한다(`check_pair_parity`). 새 기능을 추가했으면 반드시 돌려서 0건인지 확인한다.
"""
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXCLUDE_BASENAMES = {"index"}  # index.html은 카드 그리드 레이아웃이라 이 렌더러 대상이 아니다

# 2026-08-27 병합 작업 중 실제로 겪은 버그: 화이트리스트에 없는 태그(예: <ol class="reference-list">)로
# 시작하는 줄은 문단 수집 루프가 "<tag로 시작하니 다른 분기가 처리했겠지"라며 건너뛰는데, 정작 그 분기가
# 화이트리스트에 없어 아무도 처리하지 않으면 커서가 전진하지 못해 무한 루프에 빠졌다(alwa_series_analysis
# 문서로 재현·진단). 그래서 화이트리스트 방식을 버리고 "표준 HTML5 태그는 통과, 그 외(이 위키가
# 지어낸 시맨틱 마커)는 투명 래퍼"로 바꿨다 — 새 태그가 나와도 항상 커서가 전진한다는 걸 구조적으로 보장한다.
VOID_TAGS = {"br", "hr", "img", "input", "meta", "link"}  # 닫는 태그가 없어 깊이 추적이 안 되는 태그

# 2026-08-27 추가 발견: <context>/<definitions>/<references> 외에도 <overview>/<theory>/<mechanics>/
# <preservation>/<comparison>/<critique> 같은 문서별 커스텀 시맨틱 태그가 실제로 쓰이고 있었다(shantae_
# series_analysis 등). 이런 태그를 하나하나 화이트리스트에 추가하는 대신, "실제 HTML5 표준 태그면
# 원문 그대로 통과, 표준에 없는(=이 위키가 지어낸) 태그면 투명 래퍼로 벗기고 안쪽을 재귀 렌더링"으로
# 일반화했다 — 새 커스텀 태그가 또 나와도 렌더러를 매번 고칠 필요가 없다.
KNOWN_HTML_TAGS = {
    "div", "span", "p", "a", "b", "i", "strong", "em", "code", "pre", "blockquote",
    "ul", "ol", "li", "table", "thead", "tbody", "tfoot", "tr", "td", "th",
    "details", "summary", "svg", "header", "nav", "main", "article", "section",
    "footer", "aside", "figure", "figcaption", "dl", "dt", "dd", "small", "sup",
    "sub", "del", "ins", "mark", "button", "label", "form", "select", "option",
    "h1", "h2", "h3", "h4", "h5", "h6",
}
TOKEN_RE = re.compile(r"<(/?)(\w+)\b[^>]*>")


# ── 공용: 태그 짝 맞춰 블록 끝 찾기 ──────────────────────────────────

def _find_block_end(text, start, tagname):
    depth = 1
    for m in TOKEN_RE.finditer(text, start):
        if m.group(2).lower() != tagname:
            continue
        if m.group(1) == "/":
            depth -= 1
            if depth == 0:
                return m.end()
        else:
            depth += 1
    return len(text)


def _inner(block_text, tag):
    m = re.match(r"<" + tag + r"\b[^>]*>(.*)</" + tag + r">\s*$", block_text, re.S)
    return m.group(1) if m else block_text


# ── 인라인 변환 (마크다운 → HTML) ───────────────────────────────────

def inline_md_to_html(text):
    codes = []
    text = re.sub(r"`([^`]+)`", lambda m: codes.append(m.group(1)) or "\x00C%d\x00" % (len(codes) - 1), text)

    # 각주식 인용 표기 [[N]](#ref-N) — 겹대괄호라 일반 링크 정규식([텍스트](url))이 못 잡는다
    # (안쪽 대괄호를 텍스트로 오인해 짝이 안 맞는다). style.css의 sup.citation 관례에 맞춘다.
    text = re.sub(r"\[\[(\d+)\]\]\(([^)]+)\)", r'<sup class="citation"><a href="\2">[\1]</a></sup>', text)

    links = []
    href_shape = r"(?:https?://|file:///|mailto:|#|\.\./|\./|raw/)[^)]*|[^)]*\.(?:html|md|txt)(?:#[^)]*)?"
    text = re.sub(r"\[([^\]]*)\]\((" + href_shape + r")\)",
                  lambda m: links.append((m.group(1), m.group(2))) or "\x00L%d\x00" % (len(links) - 1), text)

    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text, flags=re.S)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", text, flags=re.S)

    def restore_link(m):
        label, href = links[int(m.group(1))]
        label = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", label, flags=re.S)
        return '<a href="%s">%s</a>' % (href, label)
    text = re.sub(r"\x00L(\d+)\x00", restore_link, text)

    def restore_code(m):
        raw = codes[int(m.group(1))]
        escaped = raw.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return "<code>%s</code>" % escaped
    text = re.sub(r"\x00C(\d+)\x00", restore_code, text)
    return text


# ── 목록 (중첩 지원) ─────────────────────────────────────────────────

def _parse_list_entries(lines):
    entries = []  # [indent, type, text, [continuation lines]]
    for line in lines:
        m = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        om = re.match(r"^(\s*)\d+\.\s+(.*)$", line)
        if m:
            entries.append([len(m.group(1)), "ul", m.group(2), []])
        elif om:
            entries.append([len(om.group(1)), "ol", om.group(2), []])
        elif entries and line.strip():
            entries[-1][3].append(line.strip())
    return entries


def _render_list_entries(entries):
    if not entries:
        return ""
    base_indent = entries[0][0]
    base_type = entries[0][1]
    out = []
    i, n = 0, len(entries)
    while i < n:
        indent, typ, text, extra = entries[i]
        if indent != base_indent:
            i += 1
            continue
        j = i + 1
        children = []
        while j < n and entries[j][0] > base_indent:
            children.append(entries[j])
            j += 1
        full_text = " ".join([text] + extra)
        html_text = inline_md_to_html(full_text)
        nested = _render_list_entries(children)
        out.append("<li>%s%s</li>" % (html_text, nested))
        i = j
    return "<%s>\n%s\n</%s>" % (base_type, "\n".join(out), base_type)


def render_list_block(lines):
    return _render_list_entries(_parse_list_entries(lines))


# ── 반응형 표 및 모바일 정의 목록 (<dl>/<dt>/<dd>) 변환 ─────────────

def build_responsive_table(headers, rows, raw_table_html=None):
    """표(table)를 데스크톱용 HTML5 <table> 및 모바일용 시맨틱 정의 목록(<dl>/<dt>/<dd>)으로 구성된
    반응형 이중 구조(.table-responsive-wrapper)로 렌더링한다.
    - 2열 표: 용어/정의 또는 키/값 구조의 <dt class="mobile-table-term"> + <dd class="mobile-table-desc">
    - 3열 이상 다열 표: 첫 열(대표 엔티티) <dt> + 각 컬럼별 라벨(<dt>)과 값(<dd>)으로 구성된 카드
    """
    # 1. 데스크톱 뷰 (HTML5 <table>)
    if raw_table_html:
        desktop_table = raw_table_html.strip()
    else:
        thead = "<tr>" + "".join("<th>%s</th>" % inline_md_to_html(h) for h in headers) + "</tr>"
        tr_list = []
        for r in rows:
            padded = r + [""] * max(0, len(headers) - len(r))
            tr_list.append("<tr>" + "".join("<td>%s</td>" % inline_md_to_html(c) for c in padded) + "</tr>")
        desktop_table = "<table>\n<thead>%s</thead>\n<tbody>\n%s\n</tbody>\n</table>" % (thead, "\n".join(tr_list))

    # 2. 모바일 뷰 (<dl class="mobile-table-list">)
    dl_cards = []
    col_count = len(headers)

    if col_count <= 2:
        for r in rows:
            term = r[0] if len(r) > 0 else ""
            desc = r[1] if len(r) > 1 else ""
            term_html = inline_md_to_html(term) if not raw_table_html else term
            desc_html = inline_md_to_html(desc) if not raw_table_html else desc
            dl_cards.append(
                '        <div class="mobile-table-card">\n'
                '            <dt class="mobile-table-term">%(term)s</dt>\n'
                '            <dd class="mobile-table-desc">%(desc)s</dd>\n'
                '        </div>' % {"term": term_html, "desc": desc_html}
            )
    else:
        for r in rows:
            term = r[0] if len(r) > 0 else ""
            term_html = inline_md_to_html(term) if not raw_table_html else term
            fields = []
            for col_idx in range(1, max(len(headers), len(r))):
                h_name = headers[col_idx] if col_idx < len(headers) else "항목 %d" % (col_idx + 1)
                val = r[col_idx] if col_idx < len(r) else ""
                h_html = inline_md_to_html(h_name) if not raw_table_html else h_name
                val_html = inline_md_to_html(val) if not raw_table_html else val
                fields.append(
                    '            <div class="mobile-field-row">\n'
                    '                <dt class="mobile-field-label">%(lbl)s</dt>\n'
                    '                <dd class="mobile-field-value">%(val)s</dd>\n'
                    '            </div>' % {"lbl": h_html, "val": val_html}
                )
            fields_html = "\n".join(fields)
            dl_cards.append(
                '        <div class="mobile-table-card">\n'
                '            <dt class="mobile-table-term">%(term)s</dt>\n'
                '%(fields)s\n'
                '        </div>' % {"term": term_html, "fields": fields_html}
            )

    mobile_dl = '<dl class="mobile-table-list">\n' + "\n".join(dl_cards) + '\n    </dl>'

    return (
        '<div class="table-responsive-wrapper">\n'
        '    <div class="desktop-table-view">\n'
        '        %(table)s\n'
        '    </div>\n'
        '    <div class="mobile-table-view">\n'
        '        %(dl)s\n'
        '    </div>\n'
        '</div>'
    ) % {"table": desktop_table, "dl": mobile_dl}


def parse_html_table(table_html):
    """원시 HTML <table>에서 thead/th 및 tbody/tr/td 셀 데이터를 파싱한다."""
    headers = []
    thead_m = re.search(r"<thead[^>]*>(.*?)</thead>", table_html, re.S)
    if thead_m:
        headers = [re.sub(r"^\s*<th[^>]*>(.*?)</th>\s*$", r"\1", th, flags=re.S).strip()
                   for th in re.findall(r"<th[^>]*>.*?</th>", thead_m.group(1), re.S)]
    else:
        first_tr = re.search(r"<tr[^>]*>(.*?)</tr>", table_html, re.S)
        if first_tr and "<th" in first_tr.group(1):
            headers = [re.sub(r"^\s*<th[^>]*>(.*?)</th>\s*$", r"\1", th, flags=re.S).strip()
                       for th in re.findall(r"<th[^>]*>.*?</th>", first_tr.group(1), re.S)]

    rows = []
    tbody_m = re.search(r"<tbody[^>]*>(.*?)</tbody>", table_html, re.S)
    body_content = tbody_m.group(1) if tbody_m else table_html
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", body_content, re.S):
        if "<th" in tr and not tbody_m:
            continue
        cells = [re.sub(r"^\s*<td[^>]*>(.*?)</td>\s*$", r"\1", td, flags=re.S).strip()
                 for td in re.findall(r"<td[^>]*>.*?</td>", tr, re.S)]
        if cells:
            rows.append(cells)

    if headers and rows:
        return headers, rows
    return None, None


def render_table_block(lines):
    def cells(line):
        return [c.strip() for c in line.strip().strip("|").split("|")]

    header = cells(lines[0])
    body_lines = [l for l in lines[2:] if l.strip()]
    rows = [cells(line) for line in body_lines]
    return build_responsive_table(header, rows)



# ── 코드 블록 및 아스키 구조도 / 개념 프레임워크 변환 ────────────────────

def _parse_ascii_table_or_card(raw_code):
    """아스키/유니코드 박스(┌─┐, +---+ 등)를 분석하여 표(table) 또는 단일 카드(card) 구조로 분해한다."""
    lines = [l.rstrip() for l in raw_code.strip("\n").splitlines()]
    if not lines:
        return None

    # 1. 박스 시작과 끝 경계 탐색
    box_start_idx = -1
    for idx, l in enumerate(lines):
        if any(c in l for c in "┌╔+") and any(c in l for c in "─═-"):
            box_start_idx = idx
            break

    box_end_idx = -1
    for idx in range(len(lines) - 1, box_start_idx if box_start_idx != -1 else 0, -1):
        if any(c in lines[idx] for c in "└╚+") and any(c in lines[idx] for c in "─═-"):
            box_end_idx = idx
            break

    if box_start_idx == -1 or box_end_idx == -1:
        return None

    # 박스 상단 바깥에 타이틀이 있는 경우
    title = ""
    for idx in range(box_start_idx):
        t = lines[idx].strip()
        if t:
            title = t
            break

    inner_lines = lines[box_start_idx + 1:box_end_idx]
    parsed_items = []  # list of ('divider', None) or ('row', [cell1, cell2, ...])

    for l in inner_lines:
        # 가로 구분선인지 확인
        if (any(c in l for c in "├╠+") and any(c in l for c in "─═-")) or set(l.strip()).issubset(set("─═-+|├╠┼╬")):
            parsed_items.append(("divider", None))
            continue

        # 세로선 구분자 확인
        if not any(c in l for c in "│║|"):
            continue

        raw_cells = re.split(r"[│║|]", l)
        # 앞뒤 테두리 제거
        if len(raw_cells) >= 2:
            cells = [c.strip() for c in raw_cells[1:-1]]
        else:
            cells = [c.strip() for c in raw_cells if c.strip()]

        if not any(cells):  # 빈 행 제외
            continue

        parsed_items.append(("row", cells))

    content_rows = [item[1] for item in parsed_items if item[0] == "row"]
    if not content_rows:
        return None

    max_cols = max(len(r) for r in content_rows)

    # 2열 이상이면 무조건 HTML5 <table> 구조로 처리
    if max_cols >= 2:
        table_title = title
        header_cells = None
        body_rows = []

        is_first_banner = (len(content_rows[0]) == 1 and max_cols >= 2)
        if is_first_banner:
            if not table_title:
                table_title = content_rows[0][0]

        for item_type, item_data in parsed_items:
            if item_type == "row":
                if is_first_banner and item_data == content_rows[0]:
                    continue  # 상단 타이틀 배너 건너뜀
                if header_cells is None:
                    header_cells = item_data
                else:
                    body_rows.append(item_data)

        return {
            "type": "table",
            "title": table_title,
            "header": header_cells or [],
            "body": body_rows
        }

    # 1열이면 framework-card 또는 단일 카드
    card_title = title
    items = []
    if not card_title and len(content_rows) > 1 and not re.match(r"^\d+\.", content_rows[0][0]):
        card_title = content_rows[0][0]
        items = [r[0] for r in content_rows[1:]]
    else:
        items = [r[0] for r in content_rows]

    return {
        "type": "card",
        "title": card_title,
        "items": items
    }


def render_code_fence_block(raw_code, lang=""):
    """마크다운 코드 펜스(```...```)를 렌더링한다.
    - 표 형태의 아스키/유니코드 박스(┌─┬─┐, ├─┼─┤, └─┴─┘, 2열 이상)는 HTML5 <table>로 자동 변환.
    - 1열 박스 프레임워크는 .diagram-container + .framework-card로 렌더링.
    - 아스키 플로우차트/트리 다이어그램(──▶, ┌─ 등)은 .diagram-container 안의 .diagram-ascii 뷰로 렌더링.
    - 언어 지정 코드 블록은 <pre><code class="language-...">로 렌더링.
    """
    lines = [l.rstrip() for l in raw_code.strip("\n").splitlines()]
    if not lines:
        return "<pre><code></code></pre>"

    has_box_border = any(any(c in l for c in "┌╔+") and any(c in l for c in "─═-") for l in lines)
    has_diagram_chars = any(c in raw_code for c in "┌─┐│└┘├┤┼╔═╗║╚╝╠╣▶➔▲▼")

    if has_box_border and not lang:
        parsed = _parse_ascii_table_or_card(raw_code)
        if parsed:
            title = parsed.get("title", "")
            title_html = f"    <h4>{inline_md_to_html(title)}</h4>\n" if title else ""

            if parsed["type"] == "table":
                header = parsed["header"]
                body = parsed["body"]

                table_html = build_responsive_table(header, body)

                return (
                    '<div class="diagram-container">\n'
                    f'{title_html}'
                    f'{table_html}\n'
                    '</div>'
                )

            elif parsed["type"] == "card":
                items = parsed["items"]
                li_elements = []
                for item in items:
                    m_item = re.match(r"^(?:(\d+\.)\s*)?(\[[^\]]+\])?\s*([^:]+?)\s*:\s*(.*)$", item)
                    m_badge = re.match(r"^(?:(\d+\.)\s*)?\[([^\]]+)\]\s*(.*)$", item)
                    if m_item:
                        num = m_item.group(1) or ""
                        tag = m_item.group(2) or ""
                        key = m_item.group(3).strip()
                        val = m_item.group(4).strip()
                        prefix_parts = [p for p in [num, tag, key] if p]
                        prefix = f"<b>{' '.join(prefix_parts)}</b>"
                        li_elements.append(f"<li>{prefix} : {inline_md_to_html(val)}</li>")
                    elif m_badge:
                        num = m_badge.group(1) or ""
                        tag = m_badge.group(2).strip()
                        val = m_badge.group(3).strip()
                        prefix_parts = [p for p in [num, f'[{tag}]'] if p]
                        prefix = f"<b>{' '.join(prefix_parts)}</b>"
                        li_elements.append(f"<li>{prefix} {inline_md_to_html(val)}</li>")
                    else:
                        li_elements.append(f"<li>{inline_md_to_html(item)}</li>")

                return (
                    '<div class="diagram-container">\n'
                    f'{title_html}'
                    '    <div class="framework-card">\n'
                    '        <ul class="framework-list">\n'
                    + "\n".join(f"            {li}" for li in li_elements) + "\n"
                    '        </ul>\n'
                    '    </div>\n'
                    '</div>'
                )

    if has_diagram_chars and not lang:
        escaped_code = raw_code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return (
            '<div class="diagram-container">\n'
            f'    <pre class="diagram-ascii"><code>{escaped_code}</code></pre>\n'
            '</div>'
        )

    escaped_code = raw_code.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    if lang:
        return f'<pre><code class="language-{lang}">{escaped_code}</code></pre>'
    return f'<pre><code>{escaped_code}</code></pre>'


# ── 최상위 블록 분리 + 렌더링 ────────────────────────────────────────

def _is_table_start(lines, i):
    if i + 1 >= len(lines):
        return False
    if not re.match(r"^\s*\|.*\|\s*$", lines[i]):
        return False
    return bool(re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]))


def _is_list_start(line):
    return bool(re.match(r"^\s*[-*]\s+", line) or re.match(r"^\s*\d+\.\s+", line))


def render_blocks(md_text):
    """마크다운 본문(투명 래퍼 안쪽 포함 재귀 호출됨)을 HTML 조각들의 리스트로 렌더링한다."""
    lines = md_text.strip("\n").split("\n")
    out = []
    i, n = 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue

        tag_m = re.match(r"^\s*<(\w+)\b", line)
        if tag_m:
            tag = tag_m.group(1).lower()
            if tag in VOID_TAGS:
                out.append(line.strip())
                i += 1
                continue
            # 표준 HTML5 태그가 아니면(=이 위키가 지어낸 시맨틱 마커) 투명 래퍼로 다룬다.
            # 어느 쪽이든 항상 블록 전체를 통째로 소비하므로 커서가 못 움직이는 일은 없다.
            whole_rest = "\n".join(lines[i:])
            open_m = re.match(r"\s*<" + tag + r"\b[^>]*>", whole_rest)
            end = _find_block_end(whole_rest, open_m.end(), tag)
            block_text = whole_rest[:end]
            consumed = block_text.count("\n") + 1
            if tag == "table":
                headers, rows = parse_html_table(block_text)
                if headers and rows:
                    out.append(build_responsive_table(headers, rows, raw_table_html=block_text))
                else:
                    out.append(block_text)
            elif tag in KNOWN_HTML_TAGS:
                out.append(block_text)
            else:
                inner_html = "\n\n".join(render_blocks(_inner(block_text, tag)))
                out.append(inner_html)
            i += consumed
            continue

        hm = re.match(r"^(#{1,6})\s+(.*)$", line)
        if hm:
            level = len(hm.group(1))
            out.append("<h%d>%s</h%d>" % (level, inline_md_to_html(hm.group(2).strip()), level))
            i += 1
            continue

        # 코드 블록 (``` 또는 ~~~)
        code_fence_m = re.match(r"^\s*(```+|~~~+)(.*)$", line)
        if code_fence_m:
            fence = code_fence_m.group(1)
            lang = code_fence_m.group(2).strip()
            fence_char = fence[0]
            fence_len = len(fence)
            j = i + 1
            code_lines = []
            while j < n:
                close_m = re.match(r"^\s*" + re.escape(fence_char) + r"{" + str(fence_len) + r",}\s*$", lines[j])
                if close_m:
                    j += 1
                    break
                code_lines.append(lines[j])
                j += 1
            raw_code = "\n".join(code_lines)
            out.append(render_code_fence_block(raw_code, lang))
            i = j
            continue

        # 수평 구분선 (---, ***, ___)
        if re.match(r"^\s*([-*_])(?:\s*\1){2,}\s*$", line):
            out.append("<hr>")
            i += 1
            continue

        # 네이티브 마크다운 인용문(`> `)도 지원한다 — 안 그러면 인식 못 한 줄이 문단으로 흘러들어가
        # "> " 표시가 그대로 텍스트에 남는 사고가 난다(실제로 두 문서에서 발생, 원인 확인 후 추가).
        if re.match(r"^>\s?", line):
            j = i
            quote_lines = []
            while j < n and re.match(r"^>\s?", lines[j]):
                quote_lines.append(re.sub(r"^>\s?", "", lines[j]))
                j += 1
            out.append("<blockquote>\n<p>%s</p>\n</blockquote>" % inline_md_to_html(" ".join(quote_lines)))
            i = j
            continue

        if _is_table_start(lines, i):
            j = i
            while j < n and re.match(r"^\s*\|.*\|\s*$", lines[j]):
                j += 1
            out.append(render_table_block(lines[i:j]))
            i = j
            continue

        if _is_list_start(line):
            j = i
            while j < n and (lines[j].strip() == "" and False):  # placeholder, real stop below
                break
            while j < n and (_is_list_start(lines[j]) or (lines[j].strip() and not _is_table_start(lines, j)
                              and not re.match(r"^(#{1,6})\s+", lines[j])
                              and not re.match(r"^\s*<(\w+)\b", lines[j])
                              and not re.match(r"^\s*(?:```+|~~~+)", lines[j])
                              and not re.match(r"^\s*([-*_])(?:\s*\1){2,}\s*$", lines[j]))):
                j += 1
            out.append(render_list_block(lines[i:j]))
            i = j
            continue

        j = i
        para = []
        while j < n and lines[j].strip() and not _is_list_start(lines[j]) \
                and not re.match(r"^(#{1,6})\s+", lines[j]) \
                and not re.match(r"^\s*<(\w+)\b", lines[j]) \
                and not _is_table_start(lines, j) \
                and not re.match(r"^\s*(?:```+|~~~+)", lines[j]) \
                and not re.match(r"^\s*([-*_])(?:\s*\1){2,}\s*$", lines[j]) \
                and not re.match(r"^>\s?", lines[j]):
            para.append(lines[j])
            j += 1
        out.append("<p>\n    %s\n</p>" % inline_md_to_html(" ".join(l.strip() for l in para)))
        i = j

    return out


def read_frontmatter(md_text):
    md_text = md_text.lstrip("\ufeff")
    m = re.match(r"^---\s*\n(.*?)\n---+\s*\n(.*)$", md_text, re.S)
    if not m:
        return {}, md_text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            v = v.strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            fm[k.strip()] = v
    return fm, m.group(2)


def strip_title_restatement(body_md):
    """frontmatter 뒤에 오는 "# 제목 / *부제* / **카테고리**... / *일시*" 4줄은
    frontmatter를 사람이 읽기 좋게 반복한 것뿐이라 <header>가 이미 만드므로 본문에서는 건너뛴다.
    ⚠️ "<context>(또는 첫 heading)까지 전부 버린다"는 예전 방식은, 이 4줄 뒤에 실제 내용
    (예: "관련 지식 클러스터: [...](...)" 같은 진짜 링크)이 끼어든 문서에서 그 내용을 통째로
    삭제해버렸다(game_controller_input_design_and_standards.md 실사례). 그래서 **정확히 이
    4줄 패턴만** 한 줄씩 확인하며 건너뛰고, 그 외의 줄은 무엇이든 본문으로 남긴다."""
    lines = body_md.split("\n")
    i, n = 0, len(lines)

    def skip_blank():
        nonlocal i
        while i < n and not lines[i].strip():
            i += 1

    skip_blank()
    if i < n and re.match(r"^#\s+", lines[i]):
        i += 1
    skip_blank()
    if i < n and re.match(r"^\*.+\*\s*$", lines[i]):
        i += 1
    skip_blank()
    if i < n and lines[i].startswith("**카테고리**"):
        i += 1
    skip_blank()
    if i < n and re.match(r"^\*.*작성일시.*\*", lines[i]):
        i += 1

    return "\n".join(lines[i:]).lstrip("\n")


def build_header(fm, header_attrs=""):
    """header_attrs: 기존 <header ...> 열는 태그의 속성 부분(예: ' class="admin-theme"').
    admin-theme 같은 클래스는 문서마다 다른 시각 테마라 렌더러가 지어내지 않고 원본 그대로 보존한다."""
    return (
        '    <header%(attrs)s>\n'
        '        <h1>%(title)s</h1>\n'
        '        <div class="subtitle">%(subtitle)s</div>\n'
        '        <div class="category">카테고리: %(category)s</div>\n'
        '        <div class="meta">최초 작성일시: %(created)s | 최종 수정일시: %(updated)s</div>\n'
        '    </header>'
    ) % {
        "attrs": header_attrs,
        "title": fm.get("title", ""),
        "subtitle": fm.get("subtitle", ""),
        "category": fm.get("category", ""),
        "created": fm.get("created", ""),
        "updated": fm.get("updated", ""),
    }


def resolve_raw_paths(basename, md_text, old_html):
    """문서에 연관된 로컬 원천 데이터(raw/*) 상대 경로 목록을 수집·검증한다.
    1) md_text 본문(특히 참고자료 섹션)에서 명시적으로 링크·언급된 raw/ 경로 우선 수집 (SSOT)
    2) old_html 안의 기존 raw 링크 (이전 버전 호환)
    3) md_text/html 어디에도 raw 경로가 명시되지 않은 경우에만 Z:\\wiki\\raw 디렉터리 내 basename 기반 fallback 탐색
    실제 파일시스템에 존재하는 유효한 상대 경로만 중복 없이 반환한다."""
    candidates = []

    def add_candidate(path):
        clean = path.replace("\\", "/").strip().rstrip(".,;:)\"\'")
        clean = re.sub(r'[^\w\./\-]', '', clean)
        clean_no_slash = clean.rstrip("/")
        if not clean or clean_no_slash == "raw":
            return
        if clean_no_slash.endswith("_backup") or "backup" in clean_no_slash:
            return
        if clean_no_slash.startswith("raw/YYYY"):
            return
        if clean not in candidates and clean_no_slash not in candidates:
            candidates.append(clean)

    # 1) md_text 본문 우선 탐색 (SSOT)
    if md_text:
        # 참고자료 섹션 우선 탐색
        ref_m = re.search(r'##\s+\d+\.\s+참고\s*자료.*', md_text, re.S)
        scope = ref_m.group(0) if ref_m else md_text
        for m in re.finditer(r'raw/[a-zA-Z0-9_\-\./]+', scope):
            add_candidate(m.group(0))

    # 2) old_html 안의 기존 raw 링크
    if old_html:
        for m in re.finditer(r'href=[\'"](raw/[^\'"]+)[\'"]', old_html):
            add_candidate(m.group(1))

    # 3) md나 html 어디에도 명시된 raw가 없을 때만 디렉터리 폴백 탐색
    if not candidates:
        raw_dir = os.path.join(WIKI_DIR, "raw")
        if os.path.exists(raw_dir):
            for f in os.listdir(raw_dir):
                if f.endswith("_raw.txt") and basename in f:
                    add_candidate(f"raw/{f}")

    valid_paths = []
    for rel in candidates:
        clean_rel = rel.rstrip("/")
        full = os.path.join(WIKI_DIR, clean_rel)
        if os.path.exists(full):
            if clean_rel not in valid_paths:
                valid_paths.append(clean_rel)

    valid_paths.sort(key=lambda p: (0 if basename in p else 1, 0 if p.endswith("_raw.txt") else 1))
    return valid_paths


def build_footer(basename, old_html="", md_text="", footer_attrs=""):
    """위키 표준 2계층 바닥글 UI를 생성한다 (방안 A: 네비게이션 버튼 1개로 원천 데이터 완전 통합).
    - 메인 색인, 마크다운 정본(.md), 원천 데이터(#references 섹션 이동), 에이전트 가이드, 맨 위로 네비게이션 버튼
    - 저장소 식별자 및 보좌 에이전트 메타데이터
    - 하단의 중복된 footer-raw-info 블록은 제거하고, 네비게이션 바의 [📁 원천 데이터] 단일 버튼으로 통합한다.
      (클릭 시 본문 '참고 자료 및 원천 데이터 출처' 섹션 #references 로 부드럽게 스크롤 이동)"""
    raw_paths = resolve_raw_paths(basename, md_text, old_html)
    has_ref_section = bool(re.search(r"참고\s*자료|원천\s*데이터|References", md_text))

    raw_btns_html = ""
    # 원천 데이터 경로가 존재하거나 문서에 참고자료 섹션이 있는 경우 버튼 노출
    if raw_paths or has_ref_section:
        raw_btns_html = (
            '\n                <a href="#references" class="footer-btn">\n'
            '                    <span class="footer-btn-icon">📁</span>\n'
            '                    <span class="footer-btn-text">원천 데이터</span>\n'
            '                </a>'
        )

    return (
        '    <footer%(attrs)s>\n'
        '        <div class="footer-container">\n'
        '            <div class="footer-brand">\n'
        '                <span class="footer-title">Knowledge Wiki System</span>\n'
        '                <span class="footer-desc">2계층 지식 아키텍처 (Markdown SSOT + HTML5 View)</span>\n'
        '            </div>\n'
        '            <div class="footer-nav">\n'
        '                <a href="index.html" class="footer-btn">\n'
        '                    <span class="footer-btn-icon">🏠</span>\n'
        '                    <span class="footer-btn-text">메인 색인</span>\n'
        '                </a>\n'
        '                <a href="%(basename)s.md" class="footer-btn">\n'
        '                    <span class="footer-btn-icon">📄</span>\n'
        '                    <span class="footer-btn-text">마크다운 정본</span>\n'
        '                </a>%(raw_btns)s\n'
        '                <a href="AGENTS.md" class="footer-btn">\n'
        '                    <span class="footer-btn-icon">🤖</span>\n'
        '                    <span class="footer-btn-text">에이전트 가이드</span>\n'
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
    ) % {
        "attrs": footer_attrs,
        "basename": basename,
        "raw_btns": raw_btns_html,
    }


def group_into_sections(html_pieces):
    """h2로 시작하는 묶음마다 <section>으로 감싼다(기존 관행과 맞춤).
    참고 자료 및 원천 데이터 출처 섹션에는 id="references" 앵커를 부여한다.
    첫 h2 이전에 나온 조각(있다면)은 감싸지 않고 그대로 둔다."""
    out = []
    current = None

    def wrap_section(pieces):
        if not pieces:
            return ""
        first = pieces[0]
        # 참고 자료 및 원천 데이터 출처 섹션 판별
        if re.search(r"참고\s*자료|원천\s*데이터|References", first):
            sec_tag = '<section id="references">'
        else:
            sec_tag = '<section>'
        return f"            {sec_tag}\n                " + "\n                ".join(pieces) + "\n            </section>"

    for piece in html_pieces:
        if re.match(r"^<h2[ >]", piece):
            if current is not None:
                out.append(wrap_section(current))
            current = [piece]
        elif current is not None:
            current.append(piece)
        else:
            out.append(piece)
    if current is not None:
        out.append(wrap_section(current))
    return out


def render_page(basename):
    md_path = os.path.join(WIKI_DIR, basename + ".md")
    html_path = os.path.join(WIKI_DIR, basename + ".html")
    if not os.path.exists(md_path):
        print("[없음] %s.md" % basename)
        return False
    if not os.path.exists(html_path):
        print("[없음] %s.html — 기존 html이 없으면 nav/footer를 가져올 데가 없어 건너뜀" % basename)
        return False

    md_text = io.open(md_path, encoding="utf-8").read()
    fm, body_md = read_frontmatter(md_text)
    body_md = strip_title_restatement(body_md)

    pieces = render_blocks(body_md)
    sectioned = group_into_sections(pieces)
    article_inner = "\n".join(sectioned)

    old_html = io.open(html_path, encoding="utf-8").read()

    # 줄 앞의 들여쓰기까지 매치에 포함시킨다 — 안 그러면 build_header()가 넣는 고정 들여쓰기가
    # 매번 누적돼서(재실행할 때마다 공백이 늘어나서) 멱등성이 깨진다.
    header_m = re.search(r"[ \t]*<header([^>]*)>.*?</header>", old_html, re.S)
    if not header_m:
        print("[FAIL] %s.html — <header> 블록을 못 찾음" % basename)
        return False
    new_header = build_header(fm, header_m.group(1))
    new_html = old_html[:header_m.start()] + new_header + old_html[header_m.end():]

    # 문서 템플릿이 <article> 없이 <main> 바로 아래 내용을 두는 경우가 있다(구버전 템플릿).
    article_m = re.search(r"<article([^>]*)>.*?</article>", new_html, re.S)
    if article_m:
        new_article = "<article%s>\n%s\n        </article>" % (article_m.group(1), article_inner)
        new_html = new_html[:article_m.start()] + new_article + new_html[article_m.end():]
    else:
        main_m = re.search(r"<main([^>]*)>.*?</main>", new_html, re.S)
        if not main_m:
            print("[FAIL] %s.html — <article>도 <main>도 못 찾음" % basename)
            return False
        new_main = "<main%s>\n%s\n        </main>" % (main_m.group(1), article_inner)
        new_html = new_html[:main_m.start()] + new_main + new_html[main_m.end():]

    # 줄 앞의 들여쓰기 포함 매칭으로 footer 갱신 (멱등성 보장)
    footer_m = re.search(r"[ \t]*<footer([^>]*)>.*?</footer>", new_html, re.S)
    if footer_m:
        new_footer = build_footer(basename, old_html, md_text, footer_m.group(1))
        new_html = new_html[:footer_m.start()] + new_footer + new_html[footer_m.end():]

    io.open(html_path, "w", encoding="utf-8", newline="\n").write(new_html)
    print("[완료] %s.html 재생성 (본문 %d자 -> HTML %d자)" % (basename, len(body_md), len(article_inner)))
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python render_md.py <이름> | --all")
        sys.exit(1)
    if sys.argv[1] == "--all":
        names = sorted({
            os.path.splitext(f)[0] for f in os.listdir(WIKI_DIR)
            if f.endswith(".md") and os.path.splitext(f)[0] not in EXCLUDE_BASENAMES
            and f not in ("AGENTS.md", "README.md")
        })
        ok = sum(render_page(n) for n in names)
        print("=== 총 %d / %d 페이지 재생성 ===" % (ok, len(names)))
    else:
        render_page(sys.argv[1])
