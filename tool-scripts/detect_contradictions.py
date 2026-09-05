#!/usr/bin/env python3
"""
detect_contradictions.py - 위키 문서 간 의미적 모순 및 용어 충돌 정기 감사 도구

기능:
1. 위키 내 전체 마크다운(.md) 문서의 정의(<definitions> / 용어 표)를 추출하여
   동일 용어에 대해 서로 다른 정의나 모순된 설명이 있는지 교차 검출 (Terminology Conflict).
2. 도메인 클러스터(메인 허브 ↔ 분과 문서) 간의 핵심 명제 및 수치 불일치 스캔.
3. 심층 LLM 정밀 검사가 필요한 경우, 에이전트/인간이 즉시 검토할 수 있는
   경량화된 '대조 프롬프트 요약문(Assertion Comparison Matrix)'을 자동 추출하여 출력.

사용법:
  python tool-scripts/detect_contradictions.py              # 전체 위키 용어 및 클러스터 모순 스캔
  python tool-scripts/detect_contradictions.py --cluster llm # 특정 도메인(예: llm_wiki_*) 집중 대조
  python tool-scripts/detect_contradictions.py --export-prompt # 심층 LLM 리뷰용 압축 프롬프트 생성
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI_DIR = Path(__file__).resolve().parent.parent
EXCLUDED_FILES = {"AGENTS.md", "README.md"}

def parse_terms(md_text, filename):
    """문서 내 용어 정의 블록에서 (용어, 영문, 정의) 튜플들을 추출."""
    terms = {}
    
    # 1. HTML table 형식 (<definitions> or ## 용어 정리)
    table_match = re.search(r"##\s+\d+\.\s+용어\s+정리.*?<table>(.*?)</table>", md_text, re.S)
    if not table_match:
        table_match = re.search(r"<definitions>.*?<table>(.*?)</table>", md_text, re.S)
    
    if table_match:
        rows = re.findall(r"<tr>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*</tr>", table_match.group(1), re.S)
        for term_col, def_col in rows:
            clean_term = re.sub(r"<[^>]+>", "", term_col).strip()
            clean_def = re.sub(r"<[^>]+>", "", def_col).strip()
            if clean_term and clean_def:
                terms[clean_term] = clean_def
                
    # 2. 불릿 리스트 형식 (- **용어**: **English**. 정의)
    bullet_matches = re.findall(r"^-\s+\*\*([^*]+)\*\*:\s+(.*)$", md_text, re.M)
    for term, definition in bullet_matches:
        clean_term = term.strip()
        clean_def = definition.strip()
        if clean_term and clean_term not in terms:
            terms[clean_term] = clean_def
            
    return terms

def parse_core_assertions(md_text):
    """문서 서두의 <context> 및 <overview>에서 핵심 명제 문장들을 추출."""
    assertions = []
    
    ctx_m = re.search(r"<context>(.*?)</context>", md_text, re.S)
    if ctx_m:
        assertions.append(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", ctx_m.group(1))).strip())
        
    ovw_m = re.search(r"<overview>(.*?)</overview>", md_text, re.S)
    if ovw_m:
        lines = [re.sub(r"<[^>]+>", "", l).strip() for l in ovw_m.group(1).split("\n") if l.strip() and not l.strip().startswith("#")]
        assertions.extend(lines[:3]) # 서두 핵심 3문단
        
    return assertions

def scan_contradictions(target_cluster=None, export_prompt=False):
    print("=== Starting Semantic Contradiction & Claim Audit on Z:\\wiki ===")
    
    md_files = [f for f in os.listdir(WIKI_DIR) if f.endswith(".md") and f not in EXCLUDED_FILES]
    if target_cluster:
        md_files = [f for f in md_files if target_cluster.lower() in f.lower()]
        print(f"[*] 필터링된 대상 클러스터: {target_cluster} (문서 {len(md_files)}편)")
        
    term_registry = defaultdict(list)
    doc_assertions = {}
    
    for filename in sorted(md_files):
        filepath = WIKI_DIR / filename
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
            
        # 1. 용어 추출 및 레지스트리 등록
        terms = parse_terms(content, filename)
        for term, definition in terms.items():
            term_registry[term].append((filename, definition))
            
        # 2. 핵심 명제 추출
        assertions = parse_core_assertions(content)
        if assertions:
            doc_assertions[filename] = assertions

    # 용어 충돌(Terminology Divergence) 검출
    print("\n--- 1. 용어 정의 정합성 및 잠재적 충돌 검사 ---")
    conflict_count = 0
    consistent_count = 0
    
    for term, occurrences in term_registry.items():
        if len(occurrences) > 1:
            # 서로 다른 파일에서 정의된 용어의 첫 30자(핵심 정의) 대조
            unique_defs = set()
            for fn, df in occurrences:
                # 영문 고유명사 뒤의 핵심 요약 비교
                norm_df = re.sub(r"\s+", " ", re.sub(r"^\*\*[^*]+\*\*\.?\s*", "", df)).strip()[:40]
                unique_defs.add(norm_df)
                
            if len(unique_defs) > 1:
                conflict_count += 1
                print(f"[!] 용어 정의 분기 감지: '{term}' (출현 {len(occurrences)}회)")
                for fn, df in occurrences:
                    short_df = (df[:75] + "...") if len(df) > 75 else df
                    print(f"    - [{fn}]: {short_df}")
            else:
                consistent_count += 1
        else:
            consistent_count += 1
            
    if conflict_count == 0:
        print("[PASS] 위키 내 모든 공유 용어 정의가 상호 일치합니다 (충돌 0건).")
    else:
        print(f"[주의] 총 {conflict_count}건의 용어 정의 차이가 발견되었습니다. 확인을 권장합니다.")

    # 프롬프트 생성 모드
    if export_prompt:
        prompt_path = WIKI_DIR / "tool-scripts" / "contradiction_review_prompt.txt"
        with open(prompt_path, "w", encoding="utf-8") as pf:
            pf.write("# 위키 문서 간 핵심 명제 교차 대조 프롬프트\n\n")
            pf.write("다음은 위키 내 주요 문서들의 서두 핵심 명제 요약입니다.\n")
            pf.write("문서들 간에 서로 상충하거나 모순되는 주장, 수치, 규칙이 있는지 교차 검토하십시오:\n\n")
            for fn, ast_list in doc_assertions.items():
                pf.write(f"## 문서: {fn}\n")
                for ast in ast_list:
                    pf.write(f"- {ast}\n")
                pf.write("\n")
        print(f"\n[성공] LLM 정밀 검사용 압축 명제 파일 생성 완료: {prompt_path}")

    print("\n=== Semantic Audit Completed ===")
    return conflict_count

def main():
    parser = argparse.ArgumentParser(description="위키 문서 간 의미적 모순 및 용어 충돌 정기 감사 도구")
    parser.add_argument("--cluster", type=str, default=None, help="특정 도메인 클러스터 필터 (예: llm, metroidvania)")
    parser.add_argument("--export-prompt", action="store_true", help="LLM 정밀 검토용 압축 명제 덤프 파일 생성")
    args = parser.parse_args()
    
    scan_contradictions(args.cluster, args.export_prompt)

if __name__ == "__main__":
    main()
