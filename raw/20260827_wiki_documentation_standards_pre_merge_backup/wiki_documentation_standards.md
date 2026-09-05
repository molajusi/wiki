---
title: "2계층 위키 문서 작성 및 관리 표준"
subtitle: "Two-Layer Wiki Documentation & Governance Standards"
created: "2026-08-22 오후 01:12:00 (KST, UTC+9)"
updated: "2026-08-27 (KST, UTC+9, 시각 미기록)"
category: "위키 지식 관리 (Wiki Governance)"
tags: ["Documentation Standards", "Two-Layer Wiki", "Markdown SSOT", "HTML5 View", "CSS Specs", "Visual Standards", "style.css", "Terminology Standards", "Evidence and Grounding", "Raw Sources", "Dual-File Parity", "Markdown Escaping"]
html_view: "wiki_documentation_standards.html"
---

# 2계층 위키 문서 작성 및 관리 표준
*Two-Layer Wiki Documentation & Governance Standards*

**카테고리**: 위키 지식 관리 (Wiki Governance)  
*최초 작성일시: 2026-08-22 오후 01:43:35 (KST, UTC+9) | 최종 수정일시: 2026-08-27 (KST, UTC+9, 시각 미기록) — 3.8~3.10절 추가*

<context>
본 문서는 지식위키 저장소(Z:\wiki) 내에 축적되는 모든 지식 문서의 2계층 이중 파일 구조(Markdown SSOT + HTML5 View), 제목/영문부제목 표기 규정, 카테고리/일시 표기법, 공통 스타일시트(style.css) 전체 코드셋, 5대 필수 섹션 구조, 원천 데이터 및 참고 문헌 명시 규정, 용어 정리 및 정의 표 표기 표준, 시맨틱 태그 구조 및 관리 원칙을 규정한 단일 진실 공급원(SSOT) 기술 명세서입니다.
</context>

## 1. 개요 및 목적 (Overview & Purpose)
"마크다운을 기본 골격(기계 메모리/SSOT)으로 하고, 필요한 곳에만 HTML5(인간 시각화/UI)를 결합한다"는 핵심 철학을 바탕으로, LLM의 토큰 소비 최소화와 인간 브라우징 가독성을 동시에 달성하는 2계층 위키 표준을 정의합니다.

## 2. 핵심 개념 및 원리 (Core Concept & Architecture)

### 2.1 문서 제목 및 영문 부제목 표기 규정 (Bilingual Title Display Rules)
1. **한국어 제목**: 최상단 대표 제목(`<h1>`, `#`)에 괄호 없이 단독 표기.
2. **영문 제목**: **한국어 제목 아랫줄에 괄호 없이** 표기.
3. **시각적 스타일(HTML5)**: 한국어 제목보다 상대적으로 작은 크기(`font-size: 1.05rem`)와 덜 인지적인 색상(`color: #ced4da` / `#adb5bd`)의 `<div class="subtitle">` 태그로 표시.
4. **마크다운(`*.md`)**: 한국어 `# 제목` 바로 아랫줄에 `*English Title*` 형태로 괄호 없이 배치.

### 2.2 카테고리 및 일시 표기 규정 (Category & Datetime Display Rules)
- **카테고리 독립 배치**: 카테고리는 일시(작성일시/수정일시) 윗줄에 독립 배치하여 식별성을 극대화함.
- 최상단 `<header>` 내 `<div class="category">` 및 `<div class="meta">` 영역에 초단위 `(KST, UTC+9)` 명시.

### 2.3 공통 스타일시트 연동
*Shared Stylesheet Integration*
- 모든 위키 HTML5 문서는 중복 인라인 `<style>` 태그 작성을 전면 금지하며, 반드시 루트의 공통 스타일시트 `<link rel="stylesheet" href="style.css">`를 단일 진실 공급원(SSOT)으로 링크하여 사용합니다.

## 3. 상세 기술 규격 및 시각 스타일
*Detailed Style Specifications*

### 3.1 표준 공용 스타일시트 전체 명세
*Shared CSS Style SSOT (style.css)*
```css
:root {
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
header {
    background-color: #343a40;
    color: #ffffff;
    padding: 1.5rem 2rem;
    border-bottom: 3px solid var(--primary-color);
}
header h1 {
    margin: 0 0 0.25rem 0;
    font-size: 1.8rem;
    font-weight: 700;
}
header .subtitle {
    font-size: 1.05rem;
    color: #ced4da;
    margin: 0 0 0.6rem 0;
    font-weight: 400;
}
header .category {
    font-size: 0.9rem;
    font-weight: 600;
    color: #6ea8fe; /* 일반: #6ea8fe, 관리: #9ec5fe */
    margin: 0 0 0.3rem 0;
}
header .meta {
    font-size: 0.85rem;
    color: #adb5bd;
}
.btn-md-source {
    background-color: #343a40;
    color: #ffffff !important;
    padding: 0.35rem 0.75rem;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
}
```

### 3.2 문서 및 섹션 제목, 영문 부제목 표기 규정
1. **최상단 대표 제목 (`<h1>`, `#`)**: 순수 한국어 단독 표기(괄호 없음), 영문 부제목은 바로 아랫줄에 괄호 없이 상대적으로 작고 흐린 색상(`.subtitle`)으로 독립 배치.
2. **본문 섹션 제목 (`<h2>`/`##`, `<h3>`/`###`)**:
   - 제목 본문은 **순수 한국어 단독 표기(괄호 및 영문 병기 금지)**.
   - 영문 부제목/명칭은 제목 윗줄 또는 옆에 괄호로 병기하지 않고, **제목 바로 아랫줄에 괄호 없이 더 작고 흐린 색상(HTML `.section-subtitle`, 마크다운 이탤릭/작은 글씨)으로 독립 배치**.

### 3.3 주제 위키 섹션 구조 규정 (대섹션 분할 원칙)
1. **필수 골격 섹션**:
   - `1. 개요 및 목적`: 수집 배경, 추진 목적, 핵심 의도 및 기대 효과
   - `2. 핵심 개념 및 원리`: 기본 정의, 작동 메커니즘, 아키텍처 다이어그램
   - `[N-1]. 용어 정리 및 정의`: 기술 용어, 고유명사, 약어 정의 표
   - `[N]. 참고 자료 및 원천 데이터 출처`: 로컬 원천 텍스트 경로, 외부 공식 웹링크/문서 목록 표 및 하이퍼링크
2. **주제별 전문 본문 대섹션 분할 원칙**:
   - 지식의 과밀화 및 시각적 평탄화를 방지하기 위해 실질 본문을 단일 섹션('3. 상세 분석')에 몰아넣지 않고, **주제의 성격에 따라 독립적인 1급 대섹션(`<h2>`, `##`)으로 2개 이상 복수 분할·승격**합니다 (예: `3. 역사적 계보 및 상호 진화`, `4. 게임 메커니즘 및 보상 철학`, `5. 지도 설계 및 공간 인지공학`).

### 3.4 용어 정리 및 정의 표 표기 규정
1. **'용어' 열(좌측)**: **순수 한국어 단독 표기(괄호 및 영문 병기 금지)**를 원칙으로 합니다.
2. **'정의' 열(우측)**: 영문 및 외국어 원문 표기가 필요한 경우, **'영문 표기' 등의 부가 접두사 없이 굵은 글씨로 단독 명시**합니다. (예: `용어: 체화된 인지 | 정의: **Embodied Cognition**. 컨트롤러 조작과...` / HTML `<b>Embodied Cognition</b>. 컨트롤러 조작과...`).

### 3.5 독립된 원천 자료(Raw Data) 및 참고 문헌 섹션 연동 규정
1. 원천 데이터 수신 시 `Z:\wiki\raw\YYYYMMDD_[주제]_raw.txt` 또는 서브 폴더로 정형 보존.
2. 문서 하단에 `[N]. 참고 자료 및 원천 데이터 출처` 섹션을 독립 구성하여 로컬 원천 데이터 파일 경로와 공식 웹링크 목록을 체계적으로 명시.
3. 정제 위키 `<footer>` 영역에 해당 `raw/` 원시 데이터 경로 링크 및 `.md` 원본 링크 포함.
4. 메인 색인 페이지 `Z:\wiki\index.html` 카테고리 목록에 링크 등록.

### 3.6 주장 및 정보의 근거/웹링크/출처 명시 규정 (Evidence & Grounding Standards)
1. **학술 및 이론적 근거**: 인지과학, 심리학, 게임 디자인 이론 인용 시 학자명 및 핵심 저서/이론명(예: Edward Tolman의 Cognitive Map, Kevin Lynch의 The Image of the City 등)을 명확히 명시하고 관련 웹링크(DOI, 논문 링크)를 연결.
2. **설계자 및 비평가 인터뷰 근거**: 게임 디자이너(사카모토 요시오, 이가라시 코지, Team Cherry 등) 및 게임 비평 매체(GMTK, GDC 등)의 발언 및 분석을 공식 인터뷰 기사/영상 웹링크(URL)와 함께 인용.

### 3.7 대형 위키 문서 분할 및 무손실 이관 프로토콜 (Lossless Document Splitting Protocol)
1. **파괴적 요약 덮어쓰기 전면 금지 (No Destructive Summary Overwrite)**: 대형 위키를 복수의 분과 문서로 분할할 때, 기억이나 요약 프롬프트에 의존해 템플릿 요약본을 새로 작성하여 기존 파일을 덮어쓰는 행위를 엄격히 금지합니다.
2. **분할 전 원본 동결 스냅샷 백업 (Pre-Split Freeze Backup)**: 분할 착수 전, 반드시 원본 파일(`.html`/`.md`) 전체를 `raw/YYYYMMDD_[주제]_pre_split_backup.txt`에 동결 보존하고 원본의 총 줄 수, 바이트, 섹션 구조 목록을 기록합니다.
3. **무손실 절단 및 이관 (Lossless Cut & Migrate)**: 원본에 존재하던 모든 단락, 표, 학술 인용, 각주, SVG 다이어그램을 한 글자도 누락하지 않고 각 분과 대상 파일로 온전히 오려내어 이관합니다.
4. **기계적 전수 대조 감사(Automated Lossless Audit)**: 분할 완료 후, 원본의 모든 소제목(`<h2>`/`<h3>`/`<h4>`), 표 행 수, 각주 번호(`ref-*`), 핵심 학술 개념 키워드가 분할된 하위 문서들의 총합과 일치하는지 자동화 스크립트로 전수 검증합니다.
5. **근거 없는 완전성 주장 금지 및 정량적 매핑 대조표 제시**: "100% 복원", "완벽 반영" 등의 주관적 확언을 금지하고, 반드시 **[분할 전 원본 섹션 ➔ 분할 후 파일명 및 위치 매핑 표]**와 정량적 수치 데이터를 보고서에 명시합니다.
3. **시각적 출처 표기 (HTML5)**: 출처 배지(`<span class="badge badge-blue"><a href="..." target="_blank">출처: ...</a></span>`) 또는 각주 및 하단 참고자료 링크 형태로 표시.

### 3.7 콜아웃 박스(Callout Box) 절제 및 시맨틱 태그 준수 규정
1. **콜아웃 박스 사용의 엄격한 제한**: 콜아웃 박스(`<div class="callout-box">`)는 문서 전체에서 **1~2개의 '핵심 결론/주의 요약(Key Takeaways)'에만 제한적으로 사용**하며, 본문의 일반적 레이아웃으로 남용하지 않습니다.
2. **시맨틱 요소 환원**: 학술 이론, 개발자 인터뷰, 데이터 분석 등 핵심 지식 본문은 콜아웃 내부에 가두지 않고 일반 소제목(`<h3>`/`<h4>`), 단락(`<p>`), 블록인용(`<blockquote>`), 리스트(`<ul>`/`<ol>`), 표(`<table>`) 등 표준 시맨틱 태그로 구성합니다.

### 3.8 본문 구성요소 분류 — 무엇을 마크다운으로 쓰고 무엇을 HTML로 남기는가
*Prose vs. Structured-Widget Boundary*

`.md`를 "기계 메모리/SSOT"로 삼는 목적은 토큰 절감과 grep 가독성이다. 그런데 표·콜아웃처럼 칸 안에
서식·링크·강조가 섞이는 요소를 억지로 마크다운 표/목록 문법으로 옮기면 오히려 무손실 변환이 깨지거나
가독성이 떨어진다(칸 안에 여러 문단·중첩 목록이 들어가는 순간 마크다운 표 문법으로는 표현 자체가 안
된다). 아래 기준으로 나눈다.

| 구분 | 처리 방식 | 예 |
| :--- | :--- | :--- |
| 산문(문단·소제목·목록·인라인 강조·링크) | **실제 마크다운 문법**으로 쓴다 | `## 소제목`, `- 목록`, `**강조**`, `` `코드` ``, `[텍스트](URL)` |
| 표·콜아웃 박스·인용 배지·복사용 코드블록 | **원시 HTML을 `.md` 파일 안에 그대로 둔다** | `<table>...</table>`, `<div class="callout-box">...</div>` |

유효한 마크다운 문서 안에 원시 HTML 블록을 그대로 두는 것은 마크다운 명세의 표준 동작이다 —
렌더링 시(또는 `.html` 파생본을 만들 때) 그 블록은 그대로 통과된다. 이 규정 덕분에 "표를 마크다운
표 문법으로 바꿔야 하나"를 고민할 필요가 없다 — **표는 항상 원시 HTML로 둔다.**

### 3.9 마크다운 이스케이프 함정 (Markdown Escaping Pitfalls)

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

### 3.10 이중 파일(.md/.html) 정합성 검증 규정 (Dual-File Parity Verification)

"동시 생성"은 두 파일을 각각 손으로(또는 모델이) 써낸다는 뜻이지, 한쪽이 다른 쪽에서 기계적으로
파생된다는 뜻이 아니다. 즉 **두 파일이 실제로 같은 내용을 담고 있다는 보장이 자동으로 생기지
않는다.** 문서를 신설하거나 고친 직후 다음을 대조한다(`tool-scripts/audit_wiki.py`가 자동 수행):

- **소제목 목록**: `.md`의 `##`/`###`과 `.html`의 `<h2>`/`<h3>`를 순서·개수·텍스트 기준으로 대조한다.
- **링크 목록**: `.md`의 `[텍스트](URL)`과 `.html`의 `<a href="...">`를 URL 기준으로 대조한다.

둘 중 하나라도 어긋나면 **한쪽에만 반영하고 잊은 것**이다 — 신설 도구는 AGENTS.md 4절 10항 원칙에
따라 `tool-scripts/`에 재사용 가능한 형태로 둔다. "정합성을 확인했다"는 진술은 이 대조를 실제로
돌린 뒤에만 쓴다(AGENTS.md 2절 근거 없는 완전성 주장 금지와 같은 원칙).

<definitions>
## 4. 용어 정리 및 정의 (Terminology & Definitions)
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
</definitions>

<references>
## 5. 참고 자료 및 원천 데이터 출처 (References & Raw Sources)
- **로컬 원천 데이터**: [`raw/20260822_wiki_documentation_standards_raw.txt`](file:///home/molajusi/home-nas/wiki/raw/20260822_wiki_documentation_standards_raw.txt)
- **3.8~3.10절 출처**: 별도 raw 파일 없음 — 다른 프로젝트(HyEMR)의 2계층 위키를 실제로 HTML→Markdown
  이관하며 얻은 경험을 일반화한 것이다(구조 지문 대조 검증 방식으로 41개 문서 전수 이관, 이관 중
  실제로 겪은 백틱/링크 오인 버그 포함). 이 저장소의 게임 디자인 도메인과는 무관한, 위키 아키텍처
  차원의 교훈만 반영했다.
- **관련 표준 문서**:
  - [에이전트 가이드 (AGENTS.md)](file:///home/molajusi/home-nas/wiki/AGENTS.md)
  - [메인 인덱스 (index.html)](file:///home/molajusi/home-nas/wiki/index.html)
  - [공통 스타일시트 (style.css)](file:///home/molajusi/home-nas/wiki/style.css)
</references>
