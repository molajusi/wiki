# Wiki Tool Scripts (Z:\wiki\tool-scripts)

이 디렉터리는 위키 문서 생성, 서식 렌더링, 정합성 감사, 무손실 검증에 반복 활용되는 공식 도구 스크립트 저장소입니다.

---

## 4단계 표준 수명주기 툴체인 (Standard Lifecycle Workflow)

당 저장소(`Z:\wiki`)의 모든 위키 작업은 아래의 4단계 툴체인을 기본 작업 프로토콜로 준수합니다:

```
[1단계: 골격 초기화]   python tool-scripts/create_page.py --slug [slug] --title "..." --subtitle "..."
         ↓
[2단계: 정본 편집/병합] *.md 파일에 마크다운 산문 및 표준 원시 HTML(표/다이어그램) 정밀 작성 및 증분 병합 (SSOT)
         ↓
[3단계: 자동 컴파일]   python tool-scripts/render_md.py [slug] (HTML5 자동 파생 및 메타 동기화)
         ↓
[4단계: 전수 정합 감사] python tool-scripts/audit_wiki.py (이중 파일 정합성 및 규정 100% 검증)
```

---

## 주요 도구 목록

### 1. `create_page.py` (위키 페이지 및 원천 덤프 템플릿 초기화)
- **기능**:
  - `raw/YYYYMMDD_[slug]_raw.txt` 원천 덤프 템플릿 자동 생성
  - YAML Frontmatter 및 5대 필수 섹션 구조가 갖추어진 `[slug].md` 생성
  - 공용 `style.css` 및 `wiki.js`가 링크된 초기 `[slug].html` 생성
- **옵션**:
  - `--slug`: 파일명 식별자 (영문 소문자 및 언더스코어, 필수)
  - `--title`: 순수 한국어 제목 (괄호/영문 병기 금지, 필수)
  - `--subtitle`: 영문 부제목 (괄호 금지, 필수)
  - `--category`: 위키 카테고리 (기본값: 게임 디자인)
  - `--tags`: 쉼표로 구분된 태그 목록
- **실행 예시**:
  ```bash
  python tool-scripts/create_page.py --slug metroidvania_boss_design --title "보스 설계 및 전투 메커니즘" --subtitle "Boss Design & Combat Mechanics" --category "기술 및 학술"
  ```

### 2. `render_md.py` (Markdown SSOT 기반 HTML5 자동 컴파일러)
- **기능**:
  - `.md`를 단일 진실 공급원(SSOT)으로 삼아 `.html`을 무손실 재컴파일.
  - `<header>` 블록은 `.md`의 YAML Frontmatter에서 추출하여 갱신.
  - `<article>` 본문은 마크다운 헤딩, 목록, 인라인 강조, 파이프 표를 변환하고, 표준 HTML5 블록(`<table>`, `<div>`, `<svg>`, `<details>` 등)은 원본 그대로 통과.
  - `<nav>` 및 `<footer>`의 문서별 고유 상호 링크는 수동 보존.
- **실행**:
  ```bash
  python tool-scripts/render_md.py <파일명, 확장자 없이>
  python tool-scripts/render_md.py --all
  ```

### 3. `audit_wiki.py` (위키 무결성 및 이중 파일 정합성 전수 감사)
- **기능**:
  - 전체 `.html` 및 `.md` 문서의 UTF-8 디코딩 무결성 검증.
  - 인라인 `<style>` 태그 존재 여부 검출 (공용 CSS SSOT 위반 차단).
  - H2 섹션 제목의 순수 한국어 단독 표기 규정(영문 괄호 병기 금지) 전수 검사.
  - **이중 파일(.md/.html) 정합성 대조 (`check_pair_parity`)**: 소제목(`h2`) 목록 및 본문 링크 목록이 양쪽 파일에서 정확히 일치하는지 전수 검증.
- **실행**:
  ```bash
  python tool-scripts/audit_wiki.py
  ```

### 4. `detect_contradictions.py` (의미적 모순 및 용어 정의 충돌 감사 도구)
- **기능**:
  - 위키 내 전체 마크다운 문서의 용어 정의 표를 추출하여 동일 용어에 대한 정의 분기/충돌 검출.
  - 도메인 클러스터 단위의 서두 핵심 명제 추출 및 대조.
  - `--export-prompt` 옵션으로 LLM 정밀 검토용 압축 명제 덤프 파일(`contradiction_review_prompt.txt`) 생성.
- **실행**:
  ```bash
  python tool-scripts/detect_contradictions.py              # 전체 용어 대조
  python tool-scripts/detect_contradictions.py --cluster llm # 특정 도메인 집중 대조
  python tool-scripts/detect_contradictions.py --export-prompt # LLM 검토용 프롬프트 추출
  ```

---

## 크로스플랫폼 호환 실행 가이드 (Cross-Platform Execution)

모든 도구 스크립트는 OS 비종속적(Platform-Independent)으로 작성되어 Windows, Linux, macOS에서 동일하게 동작합니다:

- **Windows**:
  ```pwsh
  python tool-scripts/audit_wiki.py
  ```
- **Linux / macOS**:
  ```bash
  python3 tool-scripts/audit_wiki.py
  ```
- **경로 구분자 규격**: 모든 스크립트 실행 인자 및 위키 내부 하이퍼링크는 Windows 백슬래시(`\`) 대신 웹 표준 슬래시(`/`)를 사용합니다.
- **인코딩 표준**: 모든 콘솔 입출력 및 파일 IO는 UTF-8 No BOM을 강제하여 cp949/euc-kr 충돌 및 개행 깨짐을 차단합니다.
