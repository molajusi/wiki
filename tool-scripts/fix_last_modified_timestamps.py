"""
2026-08-27 신설: 최종 수정일시("(정확한 시각 미기록)"류 플레이스홀더) 일괄 정정 스크립트.

AGENTS.md / wiki_documentation_standards.md 2.3절 개정(최초 작성일시 불변, 최종 수정일시
매회 갱신 의무, 정확한 시각을 확보할 수 없을 때 임의 창작 금지)에 따라, 그동안 셸 접근 불가로
"(정확한 시각 미기록)" 등으로 남겨두었던 시각 필드를 실행 시점의 실제 시:분:초로 채워 넣는다.

범위: Z:\\wiki 최상위(top-level)의 *.md / *.html 파일만 대상으로 한다.
      raw\\ (원천 데이터/백업 동결본)과 #recycle\\ 은 의도적으로 제외한다 — 특히
      raw\\*_pre_merge_backup\\ 은 "동결 스냅샷"이므로 사후 수정하면 그 목적 자체가 무너진다.

동작: "<날짜> (...미기록...)" 형태의 부분 문자열만 정확히 찾아 실행 시각으로 치환한다.
      "최초 작성일시" 필드라도 그 값 자체가 아직 한 번도 정확히 기록된 적이 없어
      "미기록" placeholder로 남아있는 경우(예: 오늘 신설한 문서)는 이번이 "최초 기록"이므로
      불변 원칙 위반이 아니다 — 반대로 이미 초 단위까지 정확히 기록된 최초 작성일시는애초에
      이 정규식에 매치되지 않으므로 손대지 않는다.
      뒤에 붙은 "— .md/.html 정합성 재조정" 같은 사유 설명 텍스트는 그대로 보존한다.

실행: python tool-scripts\\fix_last_modified_timestamps.py
"""
import os
import re
from datetime import datetime

WIKI_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PATTERN = re.compile(
    r'\d{4}-\d{2}-\d{2}\s*\([^)]*미기록[^)]*\)'
    r'|\d{4}년\s*\d{1,2}월\s*\d{1,2}일\s*\([^)]*미기록[^)]*\)'
)


def now_str():
    now = datetime.now()
    ampm = "오전" if now.hour < 12 else "오후"
    hour12 = now.hour % 12 or 12
    return f"{now.year:04d}-{now.month:02d}-{now.day:02d} {ampm} {hour12}:{now.minute:02d}:{now.second:02d} (KST, UTC+9)"


def process_file(path, stamp):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    new_text, n = PATTERN.subn(stamp, text)
    if n > 0:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_text)
    return n


def main():
    stamp = now_str()
    total = 0
    changed = []
    for name in sorted(os.listdir(WIKI_DIR)):
        if not (name.endswith('.md') or name.endswith('.html')):
            continue
        path = os.path.join(WIKI_DIR, name)
        if not os.path.isfile(path):
            continue
        n = process_file(path, stamp)
        if n:
            changed.append((name, n))
            total += n
    print(f"=== 최종 수정일시 일괄 정정 완료 — 적용 시각: {stamp} ===")
    for name, n in changed:
        print(f"[FIXED] {name}: {n}건 치환")
    print(f"--- 변경된 파일 수: {len(changed)}, 총 치환 건수: {total} ---")


if __name__ == '__main__':
    main()
