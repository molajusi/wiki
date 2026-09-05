import os
import argparse
from datetime import datetime

WIKI_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW_DIR = os.path.join(WIKI_DIR, "raw")

def get_kst_time_str():
    # Format: 2026-08-22 오후 10:25:00 (KST, UTC+9)
    now = datetime.now()
    ampm = "오전" if now.hour < 12 else "오후"
    hour12 = now.hour if now.hour <= 12 else now.hour - 12
    if hour12 == 0:
        hour12 = 12
    return f"{now.strftime('%Y-%m-%d')} {ampm} {hour12:02d}:{now.strftime('%M:%S')} (KST, UTC+9)"

def get_raw_date_prefix():
    return datetime.now().strftime("%Y%m%d")

def create_wiki_page(slug, title, subtitle, category="일반 지식 및 게임 디자인 (Game Design & Taxonomy)", tags=""):
    os.makedirs(RAW_DIR, exist_ok=True)
    time_str = get_kst_time_str()
    date_prefix = get_raw_date_prefix()
    
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else ["Game Design", "Analysis"]
    tag_str = ", ".join([f'"{t}"' for t in tag_list])

    raw_filename = f"{date_prefix}_{slug}_raw.txt"
    raw_path = os.path.join(RAW_DIR, raw_filename)
    md_path = os.path.join(WIKI_DIR, f"{slug}.md")
    html_path = os.path.join(WIKI_DIR, f"{slug}.html")

    # 1. Raw Source Template
    raw_content = f"""================================================================================
원천 데이터: {title}
수집 일시: {time_str}
수집 대상: {slug} 관련 원천 데이터 및 비평 자료
================================================================================

1. 수집 자료 요약
- 

2. 참고 문헌 및 링크
- 
================================================================================
"""

    # 2. Markdown SSOT Template
    md_content = f"""---
title: "{title}"
subtitle: "{subtitle}"
created: "{time_str}"
updated: "{time_str}"
category: "{category}"
tags: [{tag_str}]
html_view: "{slug}.html"
---

# {title}
*{subtitle}*

**카테고리**: {category}  
*최초 작성일시: {time_str} | 최종 수정일시: {time_str}*

<context>
본 문서는 {title}에 대한 체계적인 분석 및 지식 정리를 담은 위키 문서입니다.
</context>

<overview>
## 1. 개요 및 목적
*Overview & Purpose*

본 문서는 {title}의 핵심 개념과 목적을 기술합니다.
</overview>

<theory>
## 2. 핵심 개념 및 원리
*Core Concepts & Principles*

### 2.1 주요 메커니즘
- 
</theory>

<analysis>
## 3. 상세 분석 및 비평
*Detailed Analysis & Critique*

### 3.1 심층 평가
- 
</analysis>

## 4. 용어 정리 및 정의
*Glossary & Definitions*

| 용어 | 정의 |
| :--- | :--- |
| **{title}** | **{subtitle}**. 본 문서의 핵심 주제 정의. |

## 5. 참고 자료 및 원천 데이터 출처
*References & Raw Sources*

<div class="callout">
    <strong>📁 로컬 원천 데이터 보존 경로:</strong><br>
    본 위키 문서는 로컬 원천 텍스트 저장소 <code><a href="raw/{raw_filename}">raw/{raw_filename}</a></code>의 데이터와 교차 검증을 거쳐 작성되었습니다.
</div>

<ol class="reference-list">
    <li id="ref-1">[1] 출처 저자 (2026). <em>참고 문헌 제목</em>. <a href="#" target="_blank">웹링크</a></li>
</ol>
"""

    # 3. HTML5 View Template (Links to style.css)
    html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Two-Layer Knowledge Wiki</title>
    <link rel="stylesheet" href="style.css">
    <script src="wiki.js" defer></script>
</head>
<body>
    <header>
        <h1>{title}</h1>
        <div class="subtitle">{subtitle}</div>
        <div class="category">카테고리: {category}</div>
        <div class="meta">최초 작성일시: {time_str} | 최종 수정일시: {time_str}</div>
    </header>
    <nav>
        <div class="nav-links">
            <a href="index.html">← 메인 인덱스로 돌아가기</a>
            <a href="AGENTS.md">에이전트 가이드</a>
        </div>
        <a href="{slug}.md" class="btn-md-source">📄 순수 마크다운 원본(.md) 보기</a>
    </nav>
    <main>
        <article>
            <section>
                <h2>1. 개요 및 목적</h2>
                <div class="section-subtitle">Overview & Purpose</div>
                <p>
                    본 문서는 {title}의 핵심 개념과 목적을 기술합니다.
                </p>
            </section>

            <section>
                <h2>2. 핵심 개념 및 원리</h2>
                <div class="section-subtitle">Core Concepts & Principles</div>
                
                <h3>2.1 주요 메커니즘</h3>
                <p>
                    핵심 개념 상세 내용...
                </p>
            </section>

            <section>
                <h2>3. 상세 분석 및 비평</h2>
                <div class="section-subtitle">Detailed Analysis & Critique</div>
                
                <h3>3.1 심층 평가</h3>
                <p>
                    상세 분석 내용...
                </p>
            </section>

            <section>
                <h2>4. 용어 정리 및 정의</h2>
                <div class="section-subtitle">Glossary & Definitions</div>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 25%;">용어</th>
                            <th style="width: 75%;">정의</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>{title}</b></td>
                            <td><b>{subtitle}</b>. 본 문서의 핵심 주제 정의.</td>
                        </tr>
                    </tbody>
                </table>
            </section>

            <section>
                <h2>5. 참고 자료 및 원천 데이터 출처</h2>
                <div class="section-subtitle">References & Raw Sources</div>
                <div class="callout">
                    <strong>📁 로컬 원천 데이터 보존 경로:</strong><br>
                    본 위키 문서는 로컬 원천 텍스트 저장소 <code><a href="raw/{raw_filename}">raw/{raw_filename}</a></code>의 데이터와 교차 검증을 거쳐 작성되었습니다.
                </div>
                <ol class="reference-list">
                    <li id="ref-1">[1] 출처 저자 (2026). <em>참고 문헌 제목</em>. <a href="#" target="_blank">웹링크</a></li>
                </ol>
            </section>
        </article>
    </main>
    <footer>
        <p>
            Two-Layer Knowledge Wiki System | 원천 데이터: <a href="raw/{raw_filename}">raw/{raw_filename}</a> | 마크다운 SSOT: <a href="{slug}.md">{slug}.md</a><br>
            <a href="index.html">메인 색인 (Index)으로 돌아가기</a>
        </p>
    </footer>
</body>
</html>
"""

    # Write files if not exist
    for p, content in [(raw_path, raw_content), (md_path, md_content), (html_path, html_content)]:
        if not os.path.exists(p):
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(content.strip() + "\n")
            print(f"Created: {os.path.basename(p)}")
        else:
            print(f"Already exists: {os.path.basename(p)}")

    print(f"Successfully initialized 2-layer wiki templates for '{slug}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create standard 2-layer wiki templates.")
    parser.add_argument("--slug", required=True, help="Filename slug (e.g. metroidvania_boss_design)")
    parser.add_argument("--title", required=True, help="Pure Korean title without parentheses")
    parser.add_argument("--subtitle", required=True, help="English subtitle without parentheses")
    parser.add_argument("--category", default="일반 지식 및 게임 디자인 (Game Design & Taxonomy)", help="Wiki category")
    parser.add_argument("--tags", default="", help="Comma separated tags")
    args = parser.parse_args()

    create_wiki_page(args.slug, args.title, args.subtitle, args.category, args.tags)
