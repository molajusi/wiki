import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")  # Windows 콘솔 cp949에서 한글·이모지 출력 깨짐/크래시 방지

WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EXCLUDED_FILES = {"AGENTS.md", "README.md"}

def check_file_integrity(filepath):
    errors = []
    with open(filepath, "rb") as f:
        raw = f.read()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        errors.append(f"UTF-8 decode error: {e}")
        return errors
    
    # 1. HTML Specific CSS & Tag Checks
    if filepath.endswith(".html"):
        # Check for style.css link
        if "style.css" not in text:
            errors.append("Missing <link rel=\"stylesheet\" href=\"style.css\"> (Style SSOT violation)")
        
        # Check for inline <style> tags (Forbidden)
        if re.search(r"<style[^>]*>", text, re.IGNORECASE):
            errors.append("Forbidden inline <style> tag detected. Must use shared style.css")

        # Check for trailing junk after </html>
        if "</html>" in text:
            pos = text.rfind("</html>") + len("</html>")
            if len(text[pos:].strip()) > 0:
                errors.append(f"Trailing bytes found after </html> ({len(text[pos:])} chars)")
                
        h2_matches = re.findall(r"<h2[^>]*>(.*?)</h2>", text)

    # 2. Markdown Specific Checks
    elif filepath.endswith(".md"):
        # Check for trailing junk after </references>
        if "</references>" in text:
            pos = text.rfind("</references>") + len("</references>")
            if len(text[pos:].strip()) > 0:
                errors.append(f"Trailing bytes found after </references> ({len(text[pos:])} chars)")
                
        h2_matches = re.findall(r"^##\s+(.*)$", text, re.M)

    # 3. Pure Korean H2 Heading Rule Check
    for h2 in h2_matches:
        clean_h2 = re.sub(r"<[^>]+>", "", h2).strip()
        if re.search(r"\(.*[a-zA-Z]+.*\)", clean_h2) and not clean_h2.startswith("📌"):
            errors.append(f"H2 heading contains English parentheses (Policy violation: pure Korean only): {clean_h2}")

    return errors

def check_pair_parity(basename):
    """AGENTS.md 4절 11항 / wiki_documentation_standards.md 3.10절 —
    .md/.html이 "동시 생성"일 뿐 기계적 파생이 아니므로, 소제목·링크 목록이
    실제로 일치하는지 대조한다. 둘 다 있는 파일 쌍에만 적용."""
    md_path = os.path.join(WIKI_DIR, basename + ".md")
    html_path = os.path.join(WIKI_DIR, basename + ".html")
    if not (os.path.exists(md_path) and os.path.exists(html_path)):
        return []

    errors = []
    with open(md_path, "rb") as f:
        md_text = f.read().decode("utf-8", errors="replace")
    with open(html_path, "rb") as f:
        html_text = f.read().decode("utf-8", errors="replace")

    def clean(s):
        return re.sub(r"[*_`]", "", re.sub(r"<[^>]+>", "", s)).strip()

    # .html의 <nav>/<header>/<footer>는 렌더러가 안 건드리는 챙(사이트 전역 메뉴 등)이라 .md에는
    # 애초에 대응물이 없다 — 그대로 두면 항상 챙 링크 개수만큼 오탐이 난다. 그래서 <article>(또는
    # 구버전 템플릿의 <main>) 안쪽만 비교 대상으로 자른다.
    body_m = re.search(r"<article[^>]*>(.*)</article>", html_text, re.S) \
        or re.search(r"<main[^>]*>(.*)</main>", html_text, re.S)
    html_body = body_m.group(1) if body_m else html_text

    md_h2 = [clean(h) for h in re.findall(r"^##\s+(.*)$", md_text, re.M)]
    html_h2 = [clean(h) for h in re.findall(r"<h2[^>]*>(.*?)</h2>", html_body, re.S)]
    if md_h2 != html_h2:
        errors.append(
            f"h2 heading mismatch (.md {len(md_h2)}개 vs .html {len(html_h2)}개): "
            f"{md_h2} vs {html_h2}"
        )

    # .md의 링크는 두 가지 형태로 존재한다 — 산문 안 마크다운 `[텍스트](url)`과, 표/콜아웃/각주
    # 처럼 원문 그대로 둔 통과 블록 안의 raw `<a href="url">`. 마크다운 문법만 세면 통과 블록의
    # 링크가 전부 빠져 오탐이 난다(실제로 문서 전부가 그렇게 오탐났었다) — 그래서 둘 다 센다.
    # href 모양 제한(render_md.py의 href_shape와 동일)도 똑같이 걸어야 한다 — 안 그러면 예시 텍스트로
    # 쓴 "[텍스트](URL)"·"[텍스트](괄호주석)" 같은 문장(마크다운 이스케이프 함정 절 등)까지 링크로
    # 잘못 세어 렌더러는 안 만든 링크를 감사만 있다고 우기는 자기모순이 생긴다.
    href_shape = r"(?:https?://|file:///|mailto:|#|\.\./|\./)[^)]*|[^)]*\.(?:html|md)(?:#[^)]*)?"
    md_links = sorted(re.findall(r"\]\((" + href_shape + r")\)", md_text) + re.findall(r'href="([^"]+)"', md_text))
    html_links = sorted(re.findall(r'href="([^"]+)"', html_body))
    if md_links != html_links:
        errors.append(
            f"link mismatch (.md {len(md_links)}개 vs .html {len(html_links)}개)"
        )

    # 3. 일시 정합성(Timestamp Parity) 검증 (2026-09-04 신설)
    # .md frontmatter, .md 본문 서두, .html <div class="meta">의 일시 포맷 및 일치 여부 전수 검증
    fm_m = re.search(r"^---\s*\n(.*?)\n---", md_text, re.S)
    if fm_m:
        fm = fm_m.group(1)
        cm = re.search(r'^created:\s*\"?(.*?)\"?$', fm, re.M)
        um = re.search(r'^updated:\s*\"?(.*?)\"?$', fm, re.M)
        c_time = cm.group(1).strip() if cm else ""
        u_time = um.group(1).strip() if um else ""

        if not c_time:
            errors.append("MD frontmatter created timestamp missing")
        if not u_time:
            errors.append("MD frontmatter updated timestamp missing")

        if "—" in c_time or "—" in u_time:
            errors.append("timestamp reason suffix prohibited (순수 일시 단독 표기 원칙 위반: '—' 발견)")

        # MD 본문 서두 메타 대조
        md_body_meta_m = re.search(r'\*최초 작성일시:\s*([^*|]+)\|\s*최종 수정일시:\s*([^*]+)\*', md_text)
        if not md_body_meta_m:
            errors.append("MD body '*최초 작성일시: ... | 최종 수정일시: ...*' format missing or broken")
        else:
            mb_c = md_body_meta_m.group(1).strip()
            mb_u = md_body_meta_m.group(2).strip()
            if mb_c != c_time:
                errors.append(f"MD body created ({mb_c}) != FM created ({c_time})")
            if mb_u != u_time:
                errors.append(f"MD body updated ({mb_u}) != FM updated ({u_time})")

        # HTML <div class="meta"> 대조
        html_meta_m = re.search(r'<div class=["\']meta["\'][^>]*>최초 작성일시:\s*([^<|]+)\|\s*최종 수정일시:\s*([^<]+)</div>', html_text)
        if not html_meta_m:
            errors.append("HTML '<div class=\"meta\">최초 작성일시: ... | 최종 수정일시: ...</div>' format missing or broken")
        else:
            hm_c = html_meta_m.group(1).strip()
            hm_u = html_meta_m.group(2).strip()
            if hm_c != c_time:
                errors.append(f"HTML meta created ({hm_c}) != FM created ({c_time})")
            if hm_u != u_time:
                errors.append(f"HTML meta updated ({hm_u}) != FM updated ({u_time})")

    return errors

def audit_all():
    print(f"=== Starting Wiki Integrity & Style Audit on {WIKI_DIR} ===")
    files = [f for f in os.listdir(WIKI_DIR) if (f.endswith(".html") or f.endswith(".md")) and f not in EXCLUDED_FILES]
    total_errors = 0
    fail_count = 0
    pass_count = 0
    for f in sorted(files):
        fpath = os.path.join(WIKI_DIR, f)
        errs = check_file_integrity(fpath)
        if errs:
            print(f"[FAIL] {f}:")
            for e in errs:
                print(f"   - {e}")
            total_errors += len(errs)
            fail_count += 1
        else:
            size = os.path.getsize(fpath)
            print(f"[PASS] {f:<45} ({size:>6,} bytes)")
            pass_count += 1

    print(f"--- Dual-File (.md/.html) Parity Check ---")
    basenames = sorted({os.path.splitext(f)[0] for f in files})
    parity_fail = 0
    for b in basenames:
        errs = check_pair_parity(b)
        if errs:
            print(f"[PARITY FAIL] {b}:")
            for e in errs:
                print(f"   - {e}")
            total_errors += len(errs)
            parity_fail += 1

    print(f"=== Audit Complete. Passed: {pass_count}, Failed: {fail_count}, "
          f"Parity mismatches: {parity_fail}, Total issues: {total_errors} ===")
    return total_errors

if __name__ == "__main__":
    err_count = audit_all()
    sys.exit(0 if err_count == 0 else 1)
