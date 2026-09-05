---
title: "LLM 위키 원천·참고자료 적재 및 활용 전략"
subtitle: "Raw Data Ingestion & Utilization Strategy for LLM Wiki"
created: "2026-08-22 오후 01:19:58 (KST, UTC+9)"
updated: "2026-09-04 오후 02:54:30 (KST, UTC+9)"
category: "위키 지식 관리 (Wiki Governance)"
tags: ["Wiki Management", "Raw Data", "Accumulation Protocol", "Utilization Protocol", "3-Tier Storage"]
html_view: "raw_data_management_strategy.html"
---

# LLM 위키 원천·참고자료 적재 및 활용 전략
*Raw Data Ingestion & Utilization Strategy for LLM Wiki*

**카테고리**: 위키 지식 관리 (Wiki Governance)  
*최초 작성일시: 2026-08-22 오후 01:19:58 (KST, UTC+9) | 최종 수정일시: 2026-09-04 오후 02:54:30 (KST, UTC+9)*

<context>
본 문서는 LLM 지식베이스(LLM Wiki) 내에 수집되는 원천 자료(Raw Data), 논문/기사 원문, 텍스트 덤프 및 참고 데이터를 효율적으로 적재하고 활용하기 위한 시스템 구조 및 프로토콜을 규정한 기계/인간 공용 단일 진실 공급원(SSOT) 문서입니다. 상위 아키텍처에 관한 포괄적 설계는 [LLM 위키 시스템 아키텍처 및 자가 유지 지식 관리](llm_wiki_system_architecture.html)를 참조하십시오.
</context>

## 1. 개요 및 목적
*Overview & Purpose*

인간 사용자(아저씨)의 인지적 부담과 수동 분류·서식 가공 부담을 0으로 제거하고, 에이전트(자네)의 토큰 소비 최적화와 팩트 검증 정밀도를 동시에 달성하는 3단계 데이터 관리 모델과 프로토콜을 수립합니다.

## 2. 핵심 개념 및 원리
*Core Concepts & Principles*

### 2.1 삼단계 데이터 저장 계층
*Three-Tier Data Storage Architecture*

<div class="diagram-container">
<h4>[3단계 데이터 저장 및 파이프라인 흐름도]</h4>
<svg viewBox="0 0 800 180" style="width: 100%; height: auto;">
    <defs>
        <marker id="arrow-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#0d6efd" />
        </marker>
    </defs>

    <!-- Tier 1 -->
    <rect x="20" y="40" width="220" height="100" rx="6" fill="#e9ecef" stroke="#6c757d" stroke-width="2" />
    <text x="130" y="70" font-size="13" font-weight="bold" text-anchor="middle" fill="#212529">1단계: 원천 데이터</text>
    <text x="130" y="90" font-size="11" text-anchor="middle" fill="#495057">Z:\wiki\raw\*</text>
    <text x="130" y="115" font-size="10" text-anchor="middle" fill="#6c757d">• 기사/논문 텍스트 원문 덤프</text>
    <text x="130" y="130" font-size="10" text-anchor="middle" fill="#6c757d">• 에이전트 정밀 팩트 검증용</text>

    <line x1="240" y1="90" x2="280" y2="90" stroke="#0d6efd" stroke-width="2" marker-end="url(#arrow-blue)" />

    <!-- Tier 2 -->
    <rect x="290" y="30" width="260" height="120" rx="6" fill="#d1e7dd" stroke="#198754" stroke-width="2" />
    <text x="420" y="60" font-size="13" font-weight="bold" text-anchor="middle" fill="#0f5132">2단계: 정제 위키</text>
    <text x="420" y="80" font-size="11" text-anchor="middle" fill="#0f5132">*.md (SSOT) &amp; *.html (View)</text>
    <text x="420" y="105" font-size="10" text-anchor="middle" fill="#495057">• 기계: Pure Markdown 메모리</text>
    <text x="420" y="125" font-size="10" text-anchor="middle" fill="#495057">• 인간: HTML5 인터랙티브 뷰</text>
    <text x="420" y="140" font-size="10" text-anchor="middle" fill="#495057">• footer 상호 출처 역링크</text>

    <line x1="550" y1="90" x2="590" y2="90" stroke="#0d6efd" stroke-width="2" marker-end="url(#arrow-blue)" />

    <!-- Tier 3 -->
    <rect x="600" y="40" width="180" height="100" rx="6" fill="#cfe2ff" stroke="#0d6efd" stroke-width="2" />
    <text x="690" y="70" font-size="13" font-weight="bold" text-anchor="middle" fill="#084298">3단계: 메인 인덱스</text>
    <text x="690" y="90" font-size="11" text-anchor="middle" fill="#084298">index.html</text>
    <text x="690" y="115" font-size="10" text-anchor="middle" fill="#495057">• 전체 주제 맵핑</text>
    <text x="690" y="130" font-size="10" text-anchor="middle" fill="#495057">• 시스템 관리/지식 시각 분리</text>
</svg>
</div>

<table>
<thead>
<tr>
<th>계층</th>
<th>저장 위치 및 포맷</th>
<th>담당 역할 및 특징</th>
<th>주요 활용 주체</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>1단계: 원천 데이터</b></td>
<td><code>Z:\wiki\raw\*</code> (TXT, JSON, Raw)</td>
<td>원문 텍스트 덤프, 논문/기사 데이터, 파싱용 원시 데이터</td>
<td>에이전트 정밀 파싱 및 팩트 검증용</td>
</tr>
<tr>
<td><b>2단계: 정제 위키</b></td>
<td><code>Z:\wiki\*.md</code> (SSOT) / <code>*.html</code> (View)</td>
<td>요약, 비교표, 5대 필수 섹션 적용 구조화 문서</td>
<td>기계 메모리 및 인간 가독성 확보</td>
</tr>
<tr>
<td><b>3단계: 메인 인덱스</b></td>
<td><code>Z:\wiki\index.html</code></td>
<td>전체 카테고리 및 주제 문서 색인 맵</td>
<td>인간 탐색 및 에이전트 엔트리 포인트</td>
</tr>
</tbody>
</table>

## 3. 적재 및 활용 프로토콜 상세 규격
*Ingestion & Utilization Protocols*

### 3.1 적재 프로토콜
*Ingestion Protocol*

<details open>
<summary>▶ 세부 적재 절차 (단일 파일 및 다중 파일 그룹)</summary>
<ol style="margin-top: 0.5rem;">
    <li><b>단일 파일 적재</b>: 대화창 평문이나 단일 파일 전달 시 <code>Z:\wiki\raw\YYYYMMDD_[주제]_raw.txt</code>로 개별 보존.</li>
    <li><b>다중 파일 그룹 적재 (Multi-File Ingestion)</b>: 자료가 다수일 경우, <code>Z:\wiki\raw\YYYYMMDD_[주제명]\</code> 형태의 서브 폴더를 생성하여 일괄 저장 후 "해당 폴더 읽고 위키 작성하라" 지시.</li>
    <li><b>위키 정제 생성 및 메타데이터 작성</b>: 에이전트는 원천 데이터를 분석하여 <code>*.md</code>(SSOT)와 <code>*.html</code>(View) 문서를 동시 파생 생성하며, 최상단에 12시간 표기법 타임존 메타데이터(<code>최초 작성일시</code>, <code>최종 수정일시</code>)를 필수 명시.</li>
    <li><b>상호 출처 추적 (Source Tracking)</b>: 주제 위키 <code>&lt;footer&gt;</code>에 <code>raw/</code> 원시 파일 또는 서브 폴더 경로를 링크로 명시.</li>
</ol>
</details>

### 3.2 활용 프로토콜
*Utilization Protocol*

<details open>
<summary>▶ 역할별 활용 가이드 (인간 vs 기계 에이전트)</summary>
<table style="margin-top: 0.5rem;">
    <thead>
        <tr>
            <th>구분</th>
            <th>인간 (아저씨) 활용 방식</th>
            <th>기계 (자네 에이전트) 활용 방식</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>일상적 조회</th>
            <td><code>index.html</code>에서 정제 위키(<code>.html</code>)만 빠르게 브라우징하여 요약 확인</td>
            <td>정제 위키(<code>.md</code>)만 참조하여 컨텍스트 토큰 소비 최소화 및 고속 응답</td>
        </tr>
        <tr>
            <th>정밀 검증/상세 분석</th>
            <td>주제 문서 하단 <code>raw/</code> 링크 클릭하여 원문 직접 교차 확인</td>
            <td><code>raw/</code> 폴더 내 원문 파일만 지정하여 정밀 파싱 후 고정밀 답변 작성</td>
        </tr>
    </tbody>
</table>
</details>

<definitions>
## 4. 용어 정리 및 정의
*Terminology & Definitions*

<table>
<thead>
<tr>
<th>용어</th>
<th>정의</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>원천 데이터 계층</b></td>
<td><b>Raw Data Layer</b>. 가공되지 않은 원문 기사, 논문 텍스트, 수집 덤프가 영구 보존되는 <code>Z:\wiki\raw\</code> 하위 데이터 계층.</td>
</tr>
<tr>
<td><b>정제 위키 계층</b></td>
<td><b>Processed Wiki Layer</b>. 원천 데이터를 바탕으로 5대 필수 섹션을 적용하여 정제한 <code>Z:\wiki\*.md</code> 및 <code>*.html</code> 지식 문서 계층.</td>
</tr>
<tr>
<td><b>적재 프로토콜</b></td>
<td><b>Accumulation Protocol</b>. 원시 데이터 접수부터 <code>raw/</code> 저장, 위키 정제, 출처 링크 추적까지의 일련의 데이터 적재 절차.</td>
</tr>
<tr>
<td><b>활용 프로토콜</b></td>
<td><b>Utilization Protocol</b>. 인간 및 에이전트가 토큰 효율성과 데이터 정확도에 맞춰 원천/정제/인덱스 데이터를 선택적으로 사용하는 조회 규칙.</td>
</tr>
</tbody>
</table>
</definitions>

<references>
## 5. 참고 자료 및 원천 데이터 출처
*References & Raw Sources*

- **로컬 원천 데이터**:
  - [`raw/20260822_raw_data_management_strategy_raw.txt`](file:///Z:/wiki/raw/20260822_raw_data_management_strategy_raw.txt) (원천자료 적재 및 활용 체계 설계 덤프)
- **외부 학술 및 기술 출처**:
  - [Andrej Karpathy 공식 논의 아카이브](https://x.com/karpathy) — LLM 기반 지식베이스 및 원천 데이터 파이프라인
  - [Open Knowledge Format 명세](https://github.com/) — YAML Frontmatter 기반 마크다운 지식 포맷
- **사내 위키 연계 문서**:
  - [LLM 위키 시스템 아키텍처 및 자가 유지 지식 관리](file:///Z:/wiki/llm_wiki_system_architecture.html) ([.md](file:///Z:/wiki/llm_wiki_system_architecture.md)) [종합 메인 허브]
  - [LLM 위키 작성 포맷 논쟁: HTML5 vs Markdown 최신 현황](file:///Z:/wiki/llm_wiki_format_debate.html) ([.md](file:///Z:/wiki/llm_wiki_format_debate.md))
  - [2계층 위키 문서 작성 및 관리 표준](file:///Z:/wiki/wiki_documentation_standards.html) ([.md](file:///Z:/wiki/wiki_documentation_standards.md))
  - [에이전트 가이드 (AGENTS.md)](file:///Z:/wiki/AGENTS.md)
  - [메인 인덱스 (index.html)](file:///Z:/wiki/index.html)
</references>
