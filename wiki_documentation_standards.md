---
title: "2계층 위키 문서 작성 및 관리 표준"
subtitle: "Two-Layer Wiki Documentation & Governance Standards"
created: "2026-08-22 오후 01:12:00 (KST, UTC+9)"
updated: "2026-09-04 오후 02:54:30 (KST, UTC+9)"
category: "위키 지식 관리 (Wiki Governance)"
tags: ["Documentation Standards", "Two-Layer Wiki", "Markdown SSOT", "HTML5 View", "CSS Specs", "Visual Standards", "style.css", "Terminology Standards", "Evidence and Grounding", "Raw Sources", "Dual-File Parity", "Markdown Escaping", "Timestamp Immutability", "Framework Card", "Cross-Platform Portability", "Knowledge Ingestion Boundary", "Semantic Contradiction", "Pure Timestamp"]
html_view: "wiki_documentation_standards.html"
---

# 2계층 위키 문서 작성 및 관리 표준
*Two-Layer Wiki Documentation & Governance Standards*

**카테고리**: 위키 지식 관리 (Wiki Governance)  
*최초 작성일시: 2026-08-22 오후 01:12:00 (KST, UTC+9) | 최종 수정일시: 2026-09-04 오후 02:54:30 (KST, UTC+9)*

<context>
본 문서는 지식위키 저장소(Z:\wiki) 내에 축적되는 모든 지식 문서의 2계층 이중 파일 구조(Markdown SSOT + HTML5 View), 제목/영문부제목 표기 규정, 카테고리/일시 표기법, 공통 스타일시트(style.css) 전체 코드셋, 5대 필수 섹션 구조, 원천 데이터 및 참고 문헌 명시 규정, 용어 정리 및 정의 표 표기 표준, 시맨틱 태그 구조 및 관리 원칙을 규정한 단일 진실 공급원(SSOT) 기술 명세서입니다.
</context>

## 1. 개요 및 목적
*Overview & Purpose*

본 표준 문서는 지식 관리 및 정보 보좌 에이전트 **jane(자네)**가 `Z:\wiki` 디렉터리에 지식 자산을 등록, 정제, 시각화할 때 준수해야 하는 **2계층 위키 문서 작성 및 거버넌스 기술 표준**을 정의합니다.

"마크다운을 기본 골격(기계 메모리/SSOT)으로 하고, 필요한 곳에만 HTML5(인간 시각화/UI)를 결합한다"는 핵심 철학을 바탕으로, LLM의 토큰 소비 최소화와 인간 브라우징 가독성을 동시에 달성하는 2계층 위키 표준을 정의합니다.

## 2. 핵심 개념 및 원리
*Core Concept & Architecture*

### 2.1 2계층 이중 파일 아키텍처
*Dual Representation Architecture*

<div class="diagram-container">
<h4>[2계층 위키 표준 아키텍처 매핑]</h4>
<svg viewBox="0 0 800 180" style="width: 100%; height: auto;">
    <defs>
        <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#0d6efd" />
        </marker>
    </defs>
    <rect x="30" y="30" width="330" height="120" rx="6" fill="#d1e7dd" stroke="#198754" stroke-width="2" />
    <text x="195" y="60" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f5132">1. 기계 저장용 마크다운 (*.md)</text>
    <text x="195" y="80" font-size="11" text-anchor="middle" fill="#0f5132">YAML Frontmatter + XML 태그 (SSOT)</text>
    <text x="195" y="105" font-size="10" text-anchor="middle" fill="#495057">• 디자인 태그 0% (토큰 오버헤드 0%)</text>
    <text x="195" y="125" font-size="10" text-anchor="middle" fill="#495057">• LLM의 초고속 검색 및 RAG 색인 메모리</text>
    <line x1="360" y1="90" x2="430" y2="90" stroke="#0d6efd" stroke-width="2" marker-end="url(#arrow)" />
    <rect x="440" y="30" width="330" height="120" rx="6" fill="#cfe2ff" stroke="#0d6efd" stroke-width="2" />
    <text x="605" y="60" font-size="13" font-weight="bold" text-anchor="middle" fill="#084298">2. 인간 브라우징용 HTML5 (*.html)</text>
    <text x="605" y="80" font-size="11" text-anchor="middle" fill="#084298">인터랙티브 웹 표준 뷰 (View Layer)</text>
    <text x="605" y="105" font-size="10" text-anchor="middle" fill="#495057">• SVG 다이어그램, &lt;details&gt; 아코디언</text>
    <text x="605" y="125" font-size="10" text-anchor="middle" fill="#495057">• 반응형 비교 테이블 및 상단 .md 직행 버튼</text>
</svg>
</div>

### 2.2 문서 제목 및 영문 부제목 표기 규정
*Bilingual Title Display Rules*
1. **한국어 제목**: 최상단 대표 제목(`<h1>`, `#`)에 괄호 없이 단독 표기.
2. **영문 제목**: **한국어 제목 아랫줄에 괄호 없이** 표기.
3. **시각적 스타일(HTML5)**: 한국어 제목보다 상대적으로 작은 크기(`font-size: 1.05rem`)와 덜 인지적인 색상(`color: #ced4da` / `#adb5bd`)의 `<div class="subtitle">` 태그로 표시.
4. **마크다운(`*.md`)**: 한국어 `# 제목` 바로 아랫줄에 `*English Title*` 형태로 괄호 없이 배치.

### 2.3 카테고리 및 일시 표기 규정
*Category & Datetime Display Rules*
- **카테고리 독립 배치**: 카테고리는 일시(작성일시/수정일시) 윗줄에 독립 배치하여 식별성을 극대화함.
- **표기 위치**: 최상단 `<header>` 내 `<div class="category">` 및 `<div class="meta">` 영역.
- **필수 표기 항목**: 카테고리, 최초 작성일시, 최종 수정일시.
- **시간 표기법**: 한국 표준시 기준 12시간 표기법(오전/오후 hh:mm:ss)으로 **시·분·초를 예외 없이 모두** 기재. 분·초를 생략하거나 "시각 미기록"류 문구로 대체하는 것을 금지한다.
- **타임존 명시**: `(KST, UTC+9)` 필수 명시.
- **(2026-08-27 추가) 최초 작성일시 불변 원칙(Immutability)**: 최초 작성일시는 문서가 처음 생성되는 시점에 단 1회만 기록한다. 이후 그 문서를 아무리 여러 번 수정하더라도 이 값은 **절대 변경하지 않는다** — 최초 작성일시는 "이 문서가 태어난 시점"을 가리키는 불변 값이며, 갱신 대상은 오직 최종 수정일시뿐이다.
- **(2026-08-27 추가) 최종 수정일시 갱신 의무(Update-on-Every-Edit)**: 문서 내용을 한 글자라도 고칠 때마다, 그 수정이 실제로 이루어지는 시점의 시·분·초까지 정확히 반영하여 최종 수정일시를 **매번** 갱신한다. "(정확한 시각 미기록)"처럼 시각 기재를 생략·유예하는 플레이스홀더 문구의 사용을 금지한다 — 이 문구는 2026-08-27 이전 다수 문서에서 반복 사용된 관행이었으나, 본 개정으로 폐기한다.
- **(2026-08-27 추가) 정확한 시각을 확보할 수 없을 때의 처리**: 에이전트가 실시간 시계에 접근할 수 있는 도구(예: 셸 `date`/`Get-Date`)를 이 세션에서 쓸 수 없어 정확한 시·분·초를 확인하지 못하는 경우, 임의의 시각을 추정하거나 창작하여 기재하지 않는다. 대신 **사용자에게 현재 정확한 시각을 직접 확인 요청**하고, 답변을 받기 전까지는 해당 문서의 갱신을 보류하거나 그 사실을 명시적으로 알린다. 이는 AGENTS.md 2절의 "근거 없는 완전성 주장 및 과장 금지" 원칙을 일시 표기에 그대로 적용한 것이다.

## 3. 상세 기술 규격 및 시각 스타일
*Detailed Style Specifications*

### 3.1 표준 공용 스타일시트 단일 출처(CSS SSOT) 및 참조 규정
*CSS Style SSOT & External Link Mandate*

모든 위키 HTML5 문서는 개별 인라인 `<style>` 블록 작성을 전면 금지하며, 반드시 공용 스타일시트 `<link rel="stylesheet" href="style.css">`를 단일 진실 공급원(SSOT)으로 링크하여 전체 위키의 시각적 통일성을 100% 보장합니다.

<details>
<summary>▶ 표준 공용 스타일시트(style.css) 코드 명세</summary>
<pre><code>:root {
    --bg-color: #f8f9fa;
    --text-color: #212529;
    --primary-color: #0d6efd;
    --admin-color: #495057;
    --border-color: #dee2e6;
    --card-bg: #ffffff;
    --code-bg: #e9ecef;
    --badge-green: #198754;
    --badge-blue: #0d6efd;
    --badge-red: #dc3545;
}
html {
    scroll-behavior: smooth;
    scroll-padding-top: 140px;
}
header {
    background-color: #343a40;
    color: #ffffff;
    padding: 1.5rem 0;
    border-bottom: 3px solid var(--primary-color);
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}
.header-container,
header h1,
header .subtitle,
header .category,
header .meta {
    max-width: 1000px;
    margin-left: auto;
    margin-right: auto;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
    box-sizing: content-box;
}
.diagram-container {
    background: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1.8rem 0;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
}
.framework-card {
    background: #f8f9fa;
    border: 1px solid #e9ecef;
    border-left: 4px solid var(--primary-color);
    border-radius: 6px;
    padding: 1.2rem 1.5rem;
}
.framework-list {
    list-style: none;
    padding-left: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
}
.framework-list li {
    font-size: 0.95rem;
    line-height: 1.6;
    color: #343a40;
    padding-bottom: 0.6rem;
    border-bottom: 1px dashed #dee2e6;
}
.framework-list li:last-child {
    border-bottom: none;
    padding-bottom: 0;
}
.diagram-ascii {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 6px;
    padding: 1.2rem;
    overflow-x: auto;
    font-family: monospace;
    font-size: 0.88rem;
    line-height: 1.5;
}
header h1 {
    margin-top: 0;
    margin-bottom: 0.25rem;
    font-size: 1.8rem;
    font-weight: 700;
}
header .subtitle {
    font-size: 1.05rem;
    color: #ced4da;
    margin-top: 0;
    margin-bottom: 0.6rem;
    font-weight: 400;
}
header .category {
    font-size: 0.9rem;
    font-weight: 600;
    color: #6ea8fe; /* 일반: #6ea8fe, 관리: #9ec5fe */
    margin-top: 0;
    margin-bottom: 0.3rem;
}
header .meta {
    font-size: 0.85rem;
    color: #adb5bd;
    margin-top: 0;
    margin-bottom: 0;
}
.section-subtitle {
    font-size: 0.85rem;
    color: #6c757d;
    font-weight: 400;
    margin-top: 0;
    margin-bottom: 1rem;
    letter-spacing: 0.02em;
}
.btn-md-source {
    background-color: #343a40;
    color: #ffffff !important;
    padding: 0.35rem 0.75rem;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
}</code></pre>
</details>

### 3.2 문서 및 섹션 제목, 영문 부제목 표기 규정
1. **최상단 대표 제목 (`<h1>`, `#`)**: 순수 한국어 단독 표기(괄호 없음), 영문 부제목은 바로 아랫줄에 괄호 없이 상대적으로 작고 흐린 색상(`.subtitle`)으로 독립 배치.
2. **본문 섹션 제목 (`<h2>`/`##`, `<h3>`/`###`)**:
   - 제목 본문은 **순수 한국어 단독 표기(괄호 및 영문 병기 금지)**.
   - 영문 부제목/명칭은 제목 윗줄 또는 옆에 괄호로 병기하지 않고, **제목 바로 아랫줄에 괄호 없이 더 작고 흐린 색상(HTML `.section-subtitle`, 마크다운 이탤릭/작은 글씨)으로 독립 배치**.

### 3.3 주제 위키 섹션 구조 규정 (대섹션 분할 원칙)

지식의 과밀화 및 시각적 평탄화를 방지하기 위해 실질 본문을 단일 섹션('3. 상세 분석')에 몰아넣지 않고, **주제의 성격에 따라 독립적인 1급 대섹션(`<h2>`, `##`)으로 2개 이상 복수 분할·승격**합니다 (예: `3. 역사적 계보 및 상호 진화`, `4. 게임 메커니즘 및 보상 철학`, `5. 지도 설계 및 공간 인지공학`).

<details>
<summary><strong>주제 위키 섹션 구조 규정표</strong></summary>
<table>
<thead>
<tr><th>섹션 번호 및 구분</th><th>주요 내용 및 작성 목적</th><th>구조적 성격</th></tr>
</thead>
<tbody>
<tr><td><b>1. 개요 및 목적</b><br><small>Overview &amp; Purpose</small></td><td>수집 배경, 추진 목적, 해당 주제를 정리하는 핵심 의도 및 기대 효과</td><td>필수 서론(도입부)</td></tr>
<tr><td><b>2. 핵심 개념 및 원리</b><br><small>Core Concepts &amp; Principles</small></td><td>해당 주제의 기본 정의, 작동 메커니즘, 아키텍처 다이어그램</td><td>필수 본론 1(개념/메커니즘)</td></tr>
<tr><td><b>3~N. 주제별 전문 본문 대섹션</b><br><small>Domain Major Sections</small></td><td>지식 과밀화를 방지하기 위해 역사/계보, 시스템 메커니즘, 심층 비평 등을 독립된 1급 대섹션(h2)으로 복수 분할</td><td>전문 본론(자율 대분할)</td></tr>
<tr><td><b>[N-1]. 용어 정리 및 정의</b><br><small>Terminology &amp; Definitions</small></td><td>기술 용어, 고유명사, 약어 및 관련 매개변수의 명확한 정의 표</td><td>필수 결론 및 부록</td></tr>
<tr><td><b>[N]. 참고 자료 및 원천 데이터 출처</b><br><small>References &amp; Raw Sources</small></td><td>로컬 원천 데이터 파일(raw/) 경로, 외부 공식 웹링크(URL), 개발자 인터뷰/학술 논문 목록</td><td>필수 출처 및 검증</td></tr>
</tbody>
</table>
</details>

### 3.4 용어 정리 및 정의 표 표기 규정
1. **'용어' 열(좌측)**: **순수 한국어 단독 표기(괄호 및 영문 병기 금지)**를 원칙으로 합니다.
2. **'정의' 열(우측)**: 영문 및 외국어 원문 표기가 필요한 경우, **'영문 표기' 등의 부가 접두사 없이 굵은 글씨로 단독 명시**합니다. (예: `용어: 체화된 인지 | 정의: **Embodied Cognition**. 컨트롤러 조작과...` / HTML `<b>Embodied Cognition</b>. 컨트롤러 조작과...`).

### 3.5 독립된 원천 자료(Raw Data) 및 참고 문헌 섹션 연동 규정
1. 원천 데이터 수신 시 `Z:\wiki\raw\YYYYMMDD_[주제]_raw.txt` 또는 서브 폴더로 정형 보존.
2. 문서 하단에 `[N]. 참고 자료 및 원천 데이터 출처` 섹션을 독립 구성하여 로컬 원천 데이터 파일 경로와 공식 웹링크 목록을 체계적으로 명시.
3. 정제 위키 `<footer>` 영역에 해당 `raw/` 원시 데이터 경로 링크 및 `.md` 원본 링크 포함.
4. 작성 완료 후 메인 색인 페이지 `Z:\wiki\index.html` 카테고리 목록에 링크 등록.

### 3.6 주장 및 정보의 근거/웹링크/출처 명시 규정
*Evidence & Grounding Standards*
1. **학술 및 이론적 근거**: 인지과학, 심리학, 게임 디자인 이론 인용 시 학자명 및 핵심 저서/이론명(예: Edward Tolman의 Cognitive Map, Kevin Lynch의 The Image of the City 등)을 명확히 명시하고 관련 웹링크(DOI, 논문 링크)를 연결.
2. **설계자 및 비평가 인터뷰 근거**: 게임 디자이너(사카모토 요시오, 이가라시 코지, Team Cherry 등) 및 게임 비평 매체(GMTK, GDC 등)의 발언 및 분석을 공식 인터뷰 기사/영상 웹링크(URL)와 함께 인용.
3. **시각적 출처 표기 (HTML5)**: 출처 배지(`<span class="badge badge-blue"><a href="..." target="_blank">출처: ...</a></span>`) 또는 각주 및 하단 참고자료 링크 형태로 표시.

### 3.7 콜아웃 박스(Callout Box) 절제 및 시맨틱 태그 준수 규정
1. **콜아웃 박스 사용의 엄격한 제한**: 콜아웃 박스(`<div class="callout-box">`)는 문서 전체에서 **1~2개의 '핵심 결론/주의 요약(Key Takeaways)'에만 제한적으로 사용**하며, 본문의 일반적 레이아웃으로 남용하지 않습니다.
2. **시맨틱 요소 환원**: 학술 이론, 개발자 인터뷰, 데이터 분석 등 핵심 지식 본문은 콜아웃 내부에 가두지 않고 일반 소제목(`<h3>`/`<h4>`), 단락(`<p>`), 블록인용(`<blockquote>`), 리스트(`<ul>`/`<ol>`), 표(`<table>`) 등 표준 시맨틱 태그로 구성합니다.

### 3.8 대형 위키 문서 분할 및 무손실 이관 프로토콜 (Lossless Document Splitting Protocol)
1. **파괴적 요약 덮어쓰기 전면 금지 (No Destructive Summary Overwrite)**: 대형 위키를 복수의 분과 문서로 분할할 때, 기억이나 요약 프롬프트에 의존해 템플릿 요약본을 새로 작성하여 기존 파일을 덮어쓰는 행위를 엄격히 금지합니다.
2. **분할 전 원본 동결 스냅샷 백업 (Pre-Split Freeze Backup)**: 분할 착수 전, 반드시 원본 파일(`.html`/`.md`) 전체를 `raw/YYYYMMDD_[주제]_pre_split_backup.txt`에 동결 보존하고 원본의 총 줄 수, 바이트, 섹션 구조 목록을 기록합니다.
3. **무손실 절단 및 이관 (Lossless Cut & Migrate)**: 원본에 존재하던 모든 단락, 표, 학술 인용, 각주, SVG 다이어그램을 한 글자도 누락하지 않고 각 분과 대상 파일로 온전히 오려내어 이관합니다.
4. **기계적 전수 대조 감사(Automated Lossless Audit)**: 분할 완료 후, 원본의 모든 소제목(`<h2>`/`<h3>`/`<h4>`), 표 행 수, 각주 번호(`ref-*`), 핵심 학술 개념 키워드가 분할된 하위 문서들의 총합과 일치하는지 자동화 스크립트로 전수 검증합니다.
5. **근거 없는 완전성 주장 금지 및 정량적 매핑 대조표 제시**: "100% 복원", "완벽 반영" 등의 주관적 확언을 금지하고, 반드시 **[분할 전 원본 섹션 ➔ 분할 후 파일명 및 위치 매핑 표]**와 정량적 수치 데이터를 보고서에 명시합니다.

### 3.9 본문 구성요소 분류 — 무엇을 마크다운으로 쓰고 무엇을 HTML로 남기는가
*Prose vs. Structured-Widget Boundary*

`.md`를 "기계 메모리/SSOT"로 삼는 목적은 토큰 절감과 grep 가독성이다. 그런데 표·콜아웃처럼 칸 안에
서식·링크·강조가 섞이는 요소를 억지로 마크다운 표/목록 문법으로 옮기면 오히려 무손실 변환이 깨지거나
가독성이 떨어진다(칸 안에 여러 문단·중첩 목록이 들어가는 순간 마크다운 표 문법으로는 표현 자체가 안
된다). 아래 기준으로 나눈다.

| 구분 | 처리 방식 | 예 |
| :--- | :--- | :--- |
| 산문(문단·소제목·목록·인라인 강조·링크) | **실제 마크다운 문법**으로 쓴다 | `## 소제목`, `- 목록`, `**강조**`, `` `코드` ``, `[텍스트](URL)` |
| 표·콜아웃 박스·인용 배지·복사용 코드블록·SVG 다이어그램 | **원시 HTML을 `.md` 파일 안에 그대로 둔다** | `<table>...</table>`, `<div class="callout-box">...</div>`, `<svg>...</svg>` |

유효한 마크다운 문서 안에 원시 HTML 블록을 그대로 두는 것은 마크다운 명세의 표준 동작이다 —
렌더링 시(또는 `.html` 파생본을 만들 때) 그 블록은 그대로 통과된다. 이 규정 덕분에 "표를 마크다운
표 문법으로 바꿔야 하나"를 고민할 필요가 없다 — **표는 항상 원시 HTML로 둔다.**

### 3.10 마크다운 이스케이프 함정 (Markdown Escaping Pitfalls)

산문 안에 다음 두 패턴이 리터럴로 등장하면, `.md`를 마크다운으로 렌더링하는 순간(또는 `.md`만 읽는
도구·뷰어에서) 의도와 다르게 해석될 수 있다. 실측 사례로 확인된 문제들이다.

1. **리터럴 백틱을 인용부호처럼 쓰는 습관** — 예: `` 원문에서 `_ID`가 이렇게 쓰였다 `` 처럼 백틱으로
   용어를 감싸는 습관은 코드스팬(인라인 코드)으로 오인된다. **따옴표(`"..."`)를 대신 쓴다.** 정말
   코드/식별자를 가리킬 때만 백틱을 쓴다.
2. **`[텍스트](괄호주석)` 모양의 산문** — 예: "[이 개념](Tolman, 1948 참조)"처럼 대괄호 바로 뒤에
   괄호가 오는 인용·부연 표기는 마크다운 링크 문법 `[텍스트](URL)`으로 오인된다. **각주 번호
   (`[^1]`)나 "— 저자, 연도" 형태의 인라인 표기로 대체한다.** 대괄호+괄호를 나란히 쓸 일이 있으면
   괄호 안이 실제 URL/경로일 때만 그렇게 쓴다.

두 문제 다 렌더링 후 시각적으로 확인하면 바로 티가 난다(원치 않는 코드 서식이 걸리거나, 이상한
링크가 생김) — 새 문서를 쓴 뒤에는 한 번 렌더링해서 확인한다.

### 3.11 이중 파일(.md/.html) 정합성 검증 규정 (Dual-File Parity Verification)

"동시 생성"은 두 파일을 각각 손으로(또는 모델이) 써낸다는 뜻이지, 한쪽이 다른 쪽에서 기계적으로
파생된다는 뜻이 아니다. 즉 **두 파일이 실제로 같은 내용을 담고 있다는 보장이 자동으로 생기지
않는다.** 문서를 신설하거나 고친 직후 다음을 대조한다(`tool-scripts/audit_wiki.py`가 자동 수행):

- **소제목 목록**: `.md`의 `##`/`###`과 `.html`의 `<h2>`/`<h3>`를 순서·개수·텍스트 기준으로 대조한다.
- **링크 목록**: `.md`의 `[텍스트](URL)`과 `.html`의 `<a href="...">`를 URL 기준으로 대조한다.

둘 중 하나라도 어긋나면 **한쪽에만 반영하고 잊은 것**이다 — 신설 도구는 AGENTS.md 4절 10항 원칙에
따라 `tool-scripts/`에 재사용 가능한 형태로 둔다. "정합성을 확인했다"는 진술은 이 대조를 실제로
돌린 뒤에만 쓴다(AGENTS.md 2절 근거 없는 완전성 주장 금지와 같은 원칙). 이 문서 자신이 2026-08-27
감사에서 헤딩 번호("3. 상세 기술 규격 및 시각 스타일" vs "3. 상세 분석 및 규격")와 항목 배치
("3. 시각적 출처 표기"가 엉뚱하게 3.8절에 끼어 있던 것)가 `.md`/`.html` 사이에 어긋나 있던 걸
발견하고 이번에 병합하며 고쳤다 — 규정을 정의한 문서 자신도 예외가 아니었다는 뜻이다.

### 3.12 증분 병합 판단 및 무손실 패치 프로토콜
*Incremental Merge & Non-Destructive Patching*

정보 수집 및 데이터 유입 시, 기존 위키 검색(Grep/Find)을 선행하여 완전히 독립된 신규 주제가 아닌 한 새 문서를 무분별하게 신설하지 않는다. 기존 주제 문서의 하위 섹션이나 분과에 포섭될 수 있는 내용은 기존 `.md` 파일의 특정 섹션을 찾아 `diff` 단위로 증분 병합(Merge)한 후 `render_md.py`로 재컴파일한다.

### 3.13 양방향 백링크 및 지식 그래프 결속 규정
*Bidirectional Linking & Knowledge Graph Cohesion*

모든 문서는 메인 색인(`index.html`) 및 상위 허브 문서와 1개 이상의 양방향 링크(Forward & Backlinks)를 필수적으로 맺어야 하며, 단독 고립 노드(Orphan Page)를 형성하는 것을 엄격히 금지한다. 메인 허브 문서는 하위 분과 문서들을 전진 링크하고, 모든 분과 문서는 서두 문맥, 상단 `<nav>`, 본문 인라인 인용, 하단 제5섹션에서 상위 허브 및 연관 분과로 되돌아가는 역링크(Backlink)를 배치한다.

### 3.14 4단계 표준 수명주기 툴체인
*Standard Four-Stage Lifecycle Toolchain*

당 위키의 모든 신설 및 정비 작업은 다음 4단계 도구 체인을 기본 작업 프로토콜로 준수한다:
1. **골격 초기화**: `python tool-scripts/create_page.py --slug [slug] --title "..." --subtitle "..." ...`
2. **정본 편집 및 증분 병합 (SSOT)**: 마크다운(`.md`) 파일에 산문 및 표준 원시 HTML(표/다이어그램) 작성/병합.
3. **파생 뷰 자동 컴파일**: `python tool-scripts/render_md.py [slug]` (`.html` 자동 파생 및 메타 동기화)
4. **기계적 정합성 감사**: `python tool-scripts/audit_wiki.py` (이중 파일 소제목·링크 목록 100% 전수 검증)

### 3.15 크로스플랫폼 이식성 및 무결성 규정
*Cross-Platform Portability & Integrity Standards*

위키 저장소가 Windows, Linux, macOS, NAS, 모바일 브라우저, 로컬 HTTP 웹서버 등 어떤 이기종 환경으로 이관되거나 동기화되더라도 데이터 파손과 링크 깨짐 없이 완벽히 동작하도록 다음 5대 기술 규격을 강제한다:
1. **웹 표준 상대 경로 강제 (Zero-Hardcoded Absolute Paths)**: 위키 내부 문서(`a.html`), 원천 자료(`raw/...`), 공용 스타일(`style.css`) 등을 참조할 때 `file:///Z:/...`나 `file:///home/...`, `C:\...` 같은 특정 OS 드라이브 문자 및 절대경로 사용을 전면 금지하며, 반드시 '[문서명](상대경로)' 또는 '<a href="상대경로">' 형태의 웹 표준 상대 경로만을 사용한다.
2. **파일명 소문자 및 언더스코어 단일화**: 대소문자를 엄격히 구분하는 POSIX/Linux 파일 시스템에서의 404 링크 에러를 원천 차단하기 위해, 모든 파일명과 경로 타겟은 영문 소문자와 언더스코어(`_`)만 허용한다.
3. **경로 구분자 포워드 슬래시(`/`) 통일**: Windows 백슬래시(`\`)를 하이퍼링크나 스크립트 인자에 사용하지 않고 일관된 웹 표준 슬래시(`/`)를 적용한다.
4. **인코딩 및 개행 표준 (UTF-8 No BOM & LF 호환)**: BOM 없는 UTF-8 인코딩을 의무화하여 도구 간 인코딩 찌꺼기를 방지하고, LF(`\n`) 개행을 표준으로 유지한다.
5. **도구 스크립트의 OS 비종속성**: `tool-scripts/` 내의 모든 유틸리티는 OS 종속적인 셸(cmd, powershell, bash)에 의존하지 않고, 파이썬 표준 라이브러리(`pathlib`, `os.path`)만을 사용하여 어떤 플랫폼에서든 단일 명령(`python` 또는 `python3`)으로 동일하게 실행되도록 유지보수한다.

### 3.16 위키 수록 데이터 선별 및 지식 경계 거버넌스
*Knowledge Ingestion & Boundary Governance*

세상의 모든 원시 데이터를 위키 정본으로 편입하려 하지 않고, 저장소의 가치와 수명에 따라 철저히 이원화(Two-Tier Hybrid Split)한다:
- **위키 정본 수록 대상 (고가치 정형 자산)**: 장기 지속성이 요구되는 핵심 개념, 시스템 아키텍처, 설계 철학, 사내 거버넌스, 학술·비평 이론 등 정제된 마크다운(`.md`)과 HTML5(`.html`)로 편입.
- **위키 수록 배제 대상 (단기 휘발성 데이터)**: 일회성 회의록, 단순 질답 스크랩, 개발 작업 로그, 임시 버그 티켓, 원시 코드 조각 등은 위키 정본 페이지로 만들지 않고 `raw/` 원천 데이터 덤프로 격리 보존하거나 폐기.

### 3.17 신규 지식 증분 시 의미적 모순 대조 보고 규정
*Semantic Contradiction Verification*

신규 데이터 유입 및 기존 문서 증분 병합 시, 에이전트는 작성 전 연관된 기존 위키 문서를 사전 검색(Grep/Find)하여 기존에 기술된 핵심 명제·수치·타임라인과의 **논리적·의미론적 모순(Semantic Contradiction) 발생 여부를 필수 점검**한다. 작업 완료 보고 시 형식적 수치(줄 수, 바이트)뿐만 아니라 **[기존 문서와의 의미적 모순 대조 결과]**를 보고 항목에 필수로 포함하여 명시한다.

### 3.18 최종 수정일시 개정 내역 부기 금지 규정
*Prohibition of Modification Notes in Timestamp*

최종 수정일시를 갱신할 때, 수정일시 뒤에 하이픈/대시(`—`)나 괄호 등을 덧붙여 무엇을 수정했는지 사유나 개정 내역(예: `— 카테고리 체계 표준화 반영`)을 부기하는 것을 엄격히 금지한다. 최종 수정일시는 순수한 한국 표준시 12시간 표기 일시(예: `최종 수정일시: YYYY-MM-DD 오후 hh:mm:ss (KST, UTC+9)`)만을 단독으로 표기한다. 구체적인 수정 내용과 변경 이력은 커밋 메시지, 에이전트 작업 보고, 또는 본문 내부의 독립 변경 이력에서 다루며 일시 메타데이터 필드에 섞지 않는다.

### 3.19 3계층 일시 메타데이터 동기화 및 전수 감사 규정
*Three-Tier Timestamp Synchronization & Automated Audit*

문서 내 일시 정보는 다음 3개 계층에 동시 존재하며, 셋 사이에 단 1초의 오차나 누락 없이 100% 완전 일치해야 한다:
1. **마크다운 프론트매터 (Machine SSOT)**: `created: "...", updated: "..."`
2. **마크다운 본문 서두 (Human Readable Text)**: `*최초 작성일시: ... | 최종 수정일시: ...*`
3. **HTML 헤더 메타 태그 (HTML5 View)**: `<div class="meta">최초 작성일시: ... | 최종 수정일시: ...</div>`

어느 한 계층이라도 일시 라인이 누락되거나, 문자열이 파손(예: `P26-...`)되거나, 일시 값이 어긋나는 결함을 원천 차단하기 위해, 문서 편집 후 반드시 `tool-scripts/audit_wiki.py`의 자동화 일시 정합성 전수 감사(`check_pair_parity`) 통과를 의무화한다.

<definitions>
## 4. 용어 정리 및 정의
*Terminology & Definitions*
- **2계층 위키 구조**: **Two-Layer Wiki Architecture**. 기계 저장용 Markdown SSOT와 인간 검토용 HTML5 View를 분리하여 운영하는 2단계 지식 관리 구조.
- **단일 진실 공급원**: **Single Source of Truth, SSOT**. 지식 데이터를 단일 마크다운 포맷으로 관리하고 타 시각화 뷰는 자동 파생시키는 관리 방식.
- **대섹션 분할 원칙**: **Major Section Partitioning Rule**. 지식 과밀화를 방지하기 위해 실질 본문을 주제별 1급 대섹션(h2/##)으로 복수 분할하여 정보 계층을 입체화하는 구조 규정.
- **콜아웃 절제 규정**: **Callout Moderation Rule**. 콜아웃 박스를 핵심 요약에만 제한하고 일반 본문은 표준 시맨틱 요소(p, h3, blockquote, table)로 작성하는 가독성 보존 규정.
- **이중 언어 제목 및 섹션 부제목 표기 규칙**: **Bilingual Title & Subtitle Display Rules**. 최상단 제목 및 모든 섹션 제목은 순수 한국어로 단독 표기하고, 영문 부제목은 괄호 없이 바로 아랫줄에 더 작고 흐린 색상으로 독립 배치하는 제목 스타일 표준.
- **한국 표준시 12시간 표기 규격**: **KST 12-Hour Time Format**. 'YYYY-MM-DD 오전/오후 hh:mm:ss (KST, UTC+9)' 형식의 초단위 타임스탬프 규격.
- **용어 정의 표기 규정**: 용어 열은 순수 한국어로만 표기하고 영문 원문은 정의 열 서두에 '영문 표기' 접두사 없이 굵은 글씨로 단독 배치하는 기술 표기 표준.
- **근거 및 웹링크 명시 규정**: **Evidence & Web Link Standards**. 위키 내 주장과 설계 분석에 대해 학술 이론, 개발자 공식 발언, 전문 비평 자료 등의 객관적 출처 및 유효한 웹링크(URL)를 명기하는 신뢰성 보증 표준.
- **독립 원천 자료 섹션**: **Dedicated Raw Sources Section**. 위키 문서 하단에 로컬 원천 텍스트 및 외부 참조 링크를 독립된 제5섹션으로 체계화하여 보존하는 구조 표준.
- **산문-위젯 경계 규정**: **Prose vs. Structured-Widget Boundary**. 문단·목록·소제목 등 산문은 마크다운 문법으로, 표·콜아웃처럼 칸 안에 서식이 섞이는 구조화 위젯은 원시 HTML 그대로 `.md`에 남기는 본문 구성요소 분류 표준.
- **마크다운 이스케이프 함정**: **Markdown Escaping Pitfalls**. 리터럴 백틱을 인용부호로 쓰거나 `[텍스트](괄호주석)` 형태의 산문을 쓰면 코드스팬·링크로 오인되는, 실측으로 확인된 마크다운 저작 위험 두 가지.
- **이중 파일 정합성 검증**: **Dual-File Parity Verification**. "동시 생성"이 기계적 파생을 뜻하지 않으므로, `.md`/`.html` 두 파일의 소제목·링크 목록을 문서 신설·수정 직후 대조하는 검증 규정.
- **증분 병합 프로토콜**: **Incremental Merge Protocol**. 신규 지식 유입 시 새 파일을 남발하지 않고 기존 문서의 특정 섹션을 탐색하여 diff 단위로 패치·병합하는 지식 갱신 원칙.
- **양방향 지식 결속**: **Bidirectional Knowledge Cohesion**. 메인 색인, 상위 허브, 하위 분과 문서 간에 전진 링크와 역링크를 교차 결속하여 고립 노드를 방지하는 지식 그래프 연결망 규정.
- **표준 수명주기 툴체인**: **Standard Lifecycle Toolchain**. `create_page.py` ➔ `.md` 편집 ➔ `render_md.py` ➔ `audit_wiki.py`로 이어지는 4단계 위키 자동화 작업 파이프라인.
- **크로스플랫폼 이식성 규격**: **Cross-Platform Portability Standards**. 특정 OS의 절대경로를 전면 배제하고 웹 표준 상대 경로, 소문자 파일명, 슬래시(/) 구분자, UTF-8 No BOM을 강제하여 이기종 환경 간 100% 호환성을 보장하는 위키 운영 표준.
- **지식 경계 거버넌스**: **Knowledge Boundary Governance**. 장기 지속성이 요구되는 고가치 개념·설계 자산만 위키로 컴파일하고 일회성 단기 로그는 원천 덤프로 격리하는 수록 선별 기준.
- **의미적 모순 대조 규정**: **Semantic Contradiction Verification**. 신규 지식 추가 시 기존 문서들의 명제·수치와의 논리적 충돌 여부를 교차 검증하여 보고서에 명시하는 지식 정합성 관리 표준.
- **순수 일시 단독 표기 규정**: **Pure Timestamp Standard**. 최종 수정일시 메타데이터 필드에 개정 사유나 작업 내역 등의 텍스트 부기를 금지하고 순수 일시 문자열만을 단독 기재하도록 강제하는 메타데이터 정합성 표준.
- **3계층 일시 동기화 규정**: **Three-Tier Timestamp Synchronization**. 마크다운 frontmatter, 마크다운 본문 서두, HTML 메타 태그의 최초 작성일시 및 최종 수정일시를 100% 동일하게 일치시키고 기계적 감사를 강제하는 데이터 보전 표준.
</definitions>

<references>
## 5. 참고 자료 및 원천 데이터 출처
*References & Raw Sources*
- **로컬 원천 데이터**: [`raw/20260822_wiki_documentation_standards_raw.txt`](file:///Z:/wiki/raw/20260822_wiki_documentation_standards_raw.txt)
- **3.9~3.11절 출처**: 별도 raw 파일 없음 — 다른 프로젝트(HyEMR)의 2계층 위키를 실제로 HTML→Markdown
  이관하며 얻은 경험을 일반화한 것이다(구조 지문 대조 검증 방식으로 41개 문서 전수 이관, 이관 중
  실제로 겪은 백틱/링크 오인 버그 포함). 이 저장소의 게임 디자인 도메인과는 무관한, 위키 아키텍처
  차원의 교훈만 반영했다.
- **2026-08-27 정합성 재조정 근거**: 이 문서 자신의 `.md`/`.html`을 대조해 2.1절(이중 파일 아키텍처
  SVG 다이어그램), 3.1절(CSS 코드 명세를 접이식 `<details>`로 통합), 3.3절(섹션 구조 규정표),
  3.6절(시각적 출처 표기 항목 누락) 차이를 발견해 병합했다. 원본은
  `raw/20260827_wiki_documentation_standards_pre_merge_backup/`에 보존돼 있다.
- **2026-08-27 일시 표기 규정 강화 근거**: 사용자가 "최초 작성일시·최종 수정일시에 시·분·초까지
  기재하고, 최종 수정일시는 수정할 때마다 갱신하며, 최초 작성일시는 불변으로 두라"고 직접 지시했다.
  2.3절에 최초 작성일시 불변 원칙과 최종 수정일시 매회 갱신 의무, 그리고 정확한 시각을 확보할 수
  없을 때 임의로 창작하지 않고 사용자에게 확인을 요청하는 절차를 추가했다. 이 문서 자신의 상단
  메타데이터("2026-08-27, 시각 미기록")가 바로 이 새 규정이 금지하는 패턴의 실례이며, 세션이 이
  세션 내에서 정확한 시:분:초를 확보할 수단(셸 시계 접근)이 없어 사용자 확인을 기다리는 중이다.
- **관련 표준 문서**:
  - [에이전트 가이드 (AGENTS.md)](file:///Z:/wiki/AGENTS.md)
  - [메인 인덱스 (index.html)](file:///Z:/wiki/index.html)
  - [공통 스타일시트 (style.css)](file:///Z:/wiki/style.css)
  - [LLM 위키 시스템 아키텍처 및 자가 유지 지식 관리](file:///Z:/wiki/llm_wiki_system_architecture.html)
</references>
