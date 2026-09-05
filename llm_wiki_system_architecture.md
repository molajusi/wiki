---
title: "LLM 위키 시스템 아키텍처 및 자가 유지 지식 관리"
subtitle: "LLM Wiki System Architecture & Self-Maintaining Knowledge Base"
created: "2026-09-03 오후 08:39:10 (KST, UTC+9)"
updated: "2026-09-04 오후 02:54:30 (KST, UTC+9)"
category: "기술 및 학술 (Technology & Science)"
tags: ["LLM Wiki", "Knowledge Graph", "Wiki-RAG", "Self-Maintaining", "Two-Layer Wiki", "Andrej Karpathy", "GraphRAG", "Incremental Compilation"]
html_view: "llm_wiki_system_architecture.html"
---

# LLM 위키 시스템 아키텍처 및 자가 유지 지식 관리
*LLM Wiki System Architecture & Self-Maintaining Knowledge Base*

**카테고리**: 기술 및 학술 (Technology & Science)  
*최초 작성일시: 2026-09-03 오후 08:39:10 (KST, UTC+9) | 최종 수정일시: 2026-09-04 오후 02:54:30 (KST, UTC+9)*

P26-09-04 오후 02:35:45 (KST, UTC+9) — 카테고리 체계 표준화 반영*

<context>
본 문서는 거대 언어 모델(LLM) 기반의 지식 저장소 구축, 전통적 RAG의 한계 극복을 위한 위키-RAG(Wiki-RAG) 패러다임, 안드레이 카파시(Andrej Karpathy)가 제안한 개인·조직 지식베이스 컴파일러 원형, 양방향 백링크 기반 지식 그래프 순회, 자가 유지(Self-Maintaining) 파이프라인 및 환각 오염 차단 거버넌스를 포괄하는 단일 진실 공급원(SSOT) 기술 종합 명세서입니다.
</context>

## 1. 개요 및 목적
*Overview & Purpose*

거대 언어 모델(LLM)의 컨텍스트 윈도우 확장은 작업 메모리의 확장을 의미할 뿐, 장기적인 지식의 축적과 영속화를 보장하지 못합니다. 일회성 대화 인터페이스는 대화 세션 종료와 함께 문맥이 증발하며, 컨텍스트가 임계치에 도달할 때 모델의 주의 집중력 저하 및 지시 불이행을 유발하는 문맥 부패(Context Rot)를 필연적으로 초래합니다.

또한 텍스트를 기계적으로 500~1,000 토큰 단위로 잘라 임베딩하는 전통적인 청크 기반 RAG(Chunk-based RAG)는 개별 단락 간의 인과관계, 시간적 선후 맥락, 상호 모순을 구조적으로 해결하지 못하여 파편화된 검색 노이즈를 양산하는 근본적 한계를 지닙니다.

본 문서는 이러한 RAG의 단편성과 대화형 메모리의 휘발성을 극복하기 위해, **LLM을 단순 질의응답기가 아닌 지식 베이스의 지능형 컴파일러(Compiler)이자 사서(Librarian)**로 운용하는 **LLM 위키 시스템 아키텍처(LLM Wiki System Architecture)**를 규정합니다. 원천 데이터의 수집부터 원자적 정제, 종합 위키 페이지 합성, 백링크 기반 지식 그래프 순회, 그리고 기계적 감사(Auditing)를 통한 환각 방어까지 자가 유지 지식 체계의 전 수명주기를 정립하는 데 목적이 있습니다.

## 2. 핵심 개념 및 아키텍처 원리
*Core Concepts & Architecture*

### 2.1 안드레이 카파시 설계 원형과 3단계 지식 증류
*Karpathy Archetype & Three-Tier Knowledge Distillation*

2024년과 2025년에 걸쳐 안드레이 카파시(Andrej Karpathy)는 인간의 두뇌가 작업 기억(단기 기억)과 서적/외장하드(장기 기억)를 엄격히 분리하여 운용하듯, 인공지능 에이전트 역시 전용 **LLM 위키(LLM-Maintained Personal Wiki)**를 갖추어야 한다고 역설했습니다. 이 설계 원형의 핵심은 원시 데이터를 점진적으로 고도화하는 **3단계 지식 증류(Three-Tier Knowledge Distillation)**에 있습니다.

1. **원천 데이터 덤프 계층 (Raw Data Layer)**: 사용자의 거친 메모, 대화 기록, 웹 기사, 학술 논문, 업무 로그 등 가공되지 않은 자유 형식의 원문을 무변형 상태로 보존합니다(`Z:\wiki\raw\*`).
2. **원자적 사실 추출 계층 (Atomic Extraction Layer)**: 유입된 원천 데이터로부터 핵심 개체(Entity), 주장, 수치, 인용문 등 파편화된 원자적 지식을 1차 스크리닝하고 사실관계를 검증합니다.
3. **종합 위키 합성 계층 (Synthesized Wiki Layer)**: 추출된 원자적 사실들을 단편 청크로 방치하지 않고, 기존의 관련 주제 위키 문서로 합성(Synthesize)하거나 신규 주제 문서로 컴파일하여 단일 진실 공급원(SSOT)으로 영구 적재합니다.

### 2.2 이중 지식 구조와 2계층 위키 파이프라인
*Dual Representation & Two-Layer Knowledge Pipeline*

LLM 위키 시스템은 기계의 검색·추론 정밀도와 인간의 가독성·검토 편의성을 동시에 만족시키기 위해 **2계층(Markdown SSOT + HTML5 View)** 이중 지식 구조를 핵심 파이프라인으로 채택합니다.

<div class="diagram-container">
<h4>[LLM 위키 자가 유지 수명주기 파이프라인]</h4>
<svg viewBox="0 0 800 230" style="width: 100%; height: auto;">
    <defs>
        <marker id="arrow-blue" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#0d6efd" />
        </marker>
    </defs>
    <!-- Stage 1 -->
    <rect x="15" y="35" width="170" height="160" rx="6" fill="#f8f9fa" stroke="#6c757d" stroke-width="1.5" />
    <text x="100" y="60" font-size="12" font-weight="bold" text-anchor="middle" fill="#212529">1. 원천 데이터 수집</text>
    <text x="100" y="80" font-size="10" text-anchor="middle" fill="#495057">Z:\wiki\raw\*</text>
    <text x="100" y="110" font-size="9.5" text-anchor="middle" fill="#6c757d">• 자유 평문 / 논문 / 로그</text>
    <text x="100" y="130" font-size="9.5" text-anchor="middle" fill="#6c757d">• 무가공 스냅샷 보존</text>
    <text x="100" y="150" font-size="9.5" text-anchor="middle" fill="#6c757d">• 출처 추적성 확보</text>
    <text x="100" y="175" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#0d6efd">[입력: Zero-Friction]</text>

    <line x1="185" y1="115" x2="215" y2="115" stroke="#0d6efd" stroke-width="2" marker-end="url(#arrow-blue)" />

    <!-- Stage 2 -->
    <rect x="220" y="35" width="175" height="160" rx="6" fill="#fff3cd" stroke="#ffc107" stroke-width="1.5" />
    <text x="307" y="60" font-size="12" font-weight="bold" text-anchor="middle" fill="#856404">2. 지식 컴파일러 (LLM)</text>
    <text x="307" y="80" font-size="10" text-anchor="middle" fill="#856404">Compiler & Librarian</text>
    <text x="307" y="110" font-size="9.5" text-anchor="middle" fill="#664d03">• 개체 및 인과관계 추출</text>
    <text x="307" y="130" font-size="9.5" text-anchor="middle" fill="#664d03">• 기존 위키 탐색 & Diff 생성</text>
    <text x="307" y="150" font-size="9.5" text-anchor="middle" fill="#664d03">• 양방향 백링크([[ ]]) 형성</text>
    <text x="307" y="175" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#ffc107">[처리: Incremental Merge]</text>

    <line x1="395" y1="115" x2="425" y2="115" stroke="#0d6efd" stroke-width="2" marker-end="url(#arrow-blue)" />

    <!-- Stage 3 -->
    <rect x="430" y="35" width="175" height="160" rx="6" fill="#d1e7dd" stroke="#198754" stroke-width="1.5" />
    <text x="517" y="60" font-size="12" font-weight="bold" text-anchor="middle" fill="#0f5132">3. 2계층 영구 저장소</text>
    <text x="517" y="80" font-size="10" text-anchor="middle" fill="#0f5132">*.md (SSOT) / *.html (View)</text>
    <text x="517" y="110" font-size="9.5" text-anchor="middle" fill="#0f5132">• 기계 메모리: Pure Markdown</text>
    <text x="517" y="130" font-size="9.5" text-anchor="middle" fill="#0f5132">• 인간 뷰: HTML5 인터랙티브</text>
    <text x="517" y="150" font-size="9.5" text-anchor="middle" fill="#0f5132">• 메인 색인 index.html 동기화</text>
    <text x="517" y="175" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#198754">[저장: Dual Representation]</text>

    <line x1="605" y1="115" x2="635" y2="115" stroke="#0d6efd" stroke-width="2" marker-end="url(#arrow-blue)" />

    <!-- Stage 4 -->
    <rect x="640" y="35" width="145" height="160" rx="6" fill="#cfe2ff" stroke="#0d6efd" stroke-width="1.5" />
    <text x="712" y="60" font-size="12" font-weight="bold" text-anchor="middle" fill="#084298">4. 고정밀 추론 인출</text>
    <text x="712" y="80" font-size="10" text-anchor="middle" fill="#084298">Wiki-RAG Engine</text>
    <text x="712" y="110" font-size="9.5" text-anchor="middle" fill="#495057">• 단편 청크 노이즈 0%</text>
    <text x="712" y="130" font-size="9.5" text-anchor="middle" fill="#495057">• 종합 위키 단위 즉시 인출</text>
    <text x="712" y="150" font-size="9.5" text-anchor="middle" fill="#495057">• 그래프 순회 문맥 확장</text>
    <text x="712" y="175" font-size="9.5" font-weight="bold" text-anchor="middle" fill="#0d6efd">[활용: Low-Latency QA]</text>
</svg>
</div>

## 3. 위키-RAG 대조 분석 및 토큰 경제학
*Wiki-RAG Comparative Analysis & Token Economics*

### 3.1 청크 기반 RAG 대 그래프RAG 대 위키-RAG 3자 비교
*Chunk RAG vs GraphRAG vs Wiki-RAG*

지식 검색 아키텍처는 데이터의 인덱싱 방식과 저장 구조에 따라 **전통적 청킹 RAG**, **마이크로소프트 GraphRAG**, 그리고 **LLM Wiki 기반 RAG(Wiki-RAG)**의 세 가지 패러다임으로 분화됩니다.

<table>
<thead>
<tr>
<th>비교 차원</th>
<th>전통적 청크 기반 RAG (Chunk-based)</th>
<th>마이크로소프트 GraphRAG</th>
<th>LLM 위키 기반 RAG (Wiki-RAG)</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>인덱싱 방식</b></td>
<td>고정 길이 토큰 분할 및 단순 벡터 임베딩</td>
<td>LLM 엔티티/관계 추출 후 그래프 클러스터링</td>
<td><b>LLM 컴파일러에 의한 사전 주제 종합 및 백링크 연결</b></td>
</tr>
<tr>
<td><b>저장소 형태</b></td>
<td>벡터 데이터베이스 (Pinecone, Chroma 등)</td>
<td>그래프 DB (Neo4j) + 벡터 DB + 커뮤니티 요약</td>
<td><b>순수 파일 시스템 (*.md SSOT + *.html View)</b></td>
</tr>
<tr>
<td><b>글로벌 질의 대응력</b><br>(전체 요약, 트렌드)</td>
<td><b>매우 취약</b> (개별 청크 유사도만 계산하여 거시 맥락 파악 불가)</td>
<td><b>우수</b> (계층적 커뮤니티 요약 인출)</td>
<td><b>우수</b> (상위 허브 위키 페이지 및 메인 색인 탐색)</td>
</tr>
<tr>
<td><b>증분 갱신 난이도</b><br>(Incremental Update)</td>
<td>보통 (신규 청크 임베딩 추가)</td>
<td><b>극도로 어려움</b> (그래프 재색인 및 클러스터링 재계산 필요)</td>
<td><b>우수</b> (Git diff 방식의 특정 위키 문서 섹션 편집)</td>
</tr>
<tr>
<td><b>인덱싱 토큰 비용</b></td>
<td><b>최소</b> (임베딩 모델 비용만 소모)</td>
<td><b>극대</b> (수십~수백 배의 LLM 프롬프트 토큰 소모)</td>
<td><b>적정</b> (신규 유입 데이터 증분 처리 시에만 LLM 호출)</td>
</tr>
<tr>
<td><b>추론 시점 토큰 소모</b></td>
<td>높음 (관련성 낮은 중복 청크 다수 유입)</td>
<td>보통~높음 (커뮤니티 요약문 크기 과다)</td>
<td><b>최소 (이미 정제·구조화된 핵심 섹션만 타겟 인출)</b></td>
</tr>
<tr>
<td><b>인간 검토 가능성</b></td>
<td>불가능 (벡터 임베딩 공간의 블랙박스화)</td>
<td>제한적 (복잡한 그래프 시각화 도구 필요)</td>
<td><b>100% 투명 (웹 브라우저 및 마크다운 리더 즉시 열람)</b></td>
</tr>
</tbody>
</table>

### 3.2 추론 시점 토큰 예산 및 검색 레이턴시 최적화
*Inference-Time Token Budget & Latency Optimization*

전통적 RAG는 질문이 인입되는 추론 시점(Inference Time)에 수많은 단편 청크를 검색하여 모델의 컨텍스트 윈도우에 밀어 넣습니다. 이로 인해 쿼리당 8,000~16,000 토큰 이상의 컨텍스트가 낭비되고, 모델은 모순된 정보 사이에서 혼란을 겪으며 추론 레이턴시가 급증합니다.

반면 Wiki-RAG는 **지식의 종합과 모순 해결을 사전에 완료하는 사전 컴파일(Pre-compilation) 전략**을 취합니다.
1. **토큰 절감 효과**: 질문에 대해 사전에 구조화된 위키의 단일 섹션(500~1,500 토큰)만 주입하므로 추론 컨텍스트 토큰을 최대 70~85% 절감합니다.
2. **주의 집중력 극대화**: 노이즈가 제거된 단일 진실 공급원(SSOT) 문맥을 전달받으므로 환각 발생률이 통제되고 지시 준수율이 향상됩니다.
3. **결정론적 검색**: 벡터 유사도의 불확실성에 의존하지 않고 고유명사 및 위키 백링크를 통해 신속하게 정밀 문맥에 도달합니다.

## 4. 지식 컴파일 및 자가 유지 메커니즘
*Knowledge Compilation & Self-Maintenance Mechanisms*

### 4.1 컴파일러로서의 거대 언어 모델과 증분 갱신
*LLM as Compiler & Incremental Updating*

LLM 위키 시스템에서 에이전트는 작성자가 아닌 **'컴파일러'**로 동작합니다. 전통적 소프트웨어 공학에서 소스코드가 목적 코드로 빌드되듯, 에이전트는 비정형 원천 데이터를 구조화된 지식 베이스로 컴파일합니다.

- **파괴적 덮어쓰기 금지 (Non-Destructive Compilation)**: 신규 정보 유입 시 전체 문서를 재생성하여 기존 지식을 망실하지 않고, 기존 문서의 단락과 표를 보존하면서 추가 변경 사항만 `diff` 형태로 병합(Merge)합니다.
- **원자적 분할 및 합성 (Deconstruct & Synthesize)**: 단일 원천 파일에 여러 주제가 혼재된 경우, 각 주제를 분해하여 관련된 개별 위키 문서들에 분산 반영하고 상호 참조 링크를 생성합니다.

### 4.2 양방향 백링크 기반 지식 그래프 순회
*Bidirectional Wikilinks & Knowledge Graph Traversal*

LLM 위키는 파일 시스템 기반이면서도 지식 그래프의 연결망 기능을 온전히 수행합니다. 그 핵심 동력은 **양방향 백링크([[wikilinks]]) 네트워크**입니다.

- **전진 링크와 역링크**: 문서 A가 `[[문서 B]]`를 참조하면, 문서 B의 하단 또는 메타데이터에 문서 A로부터의 참조 관계가 기록됩니다.
- **그래프 순회**: 에이전트가 단일 위키 문서를 읽은 후 연관 개념을 파악해야 할 때, 백링크 목록을 순회하여 상위 개념, 하위 분과, 인접 사례로 문맥을 동적으로 확장합니다.
- **고립 노드 방지 (Orphan Prevention)**: 새로 생성된 모든 문서는 메인 색인(`index.html`) 및 상위 허브 문서와 1개 이상의 유효한 백링크로 결속되어 지식의 단절을 방지합니다.

### 4.3 로컬 마크다운 생태계 및 표준 포맷 연동
*Local Markdown Ecosystem & Open Knowledge Format*

특정 상용 SaaS 플랫폼에 종속되지 않는 영속성을 확보하기 위해 오픈 지식 포맷(Open Knowledge Format, OKF)과 로컬 파일 시스템 표준을 준수합니다.

- **YAML Frontmatter 표준**: 최상단에 `title`, `created`, `updated`, `category`, `tags`, `html_view` 등의 기계 판독용 메타데이터를 정형 배치합니다.
- **도구 독립성**: 순수 마크다운(`.md`) 파일 구조를 유지함으로써 Obsidian, Logseq, Foam, VS Code 등 광범위한 오픈소스 개인 지식 관리(PKM) 생태계와 즉시 연동됩니다.

## 5. 신뢰성 거버넌스 및 엔트로피 방어 프로토콜
*Reliability Governance & Entropy Defense Protocols*

자가 유지 위키 시스템의 가장 큰 위협은 시간이 흐름에 따라 지식의 일관성이 무너지고 거짓 정보가 누적되는 **정보 엔트로피(Information Entropy)의 증가**입니다. 이를 차단하기 위해 세 가지 거버넌스 방어선을 구축합니다.

### 5.1 환각 연쇄 차단 및 실시간 근거 정박
*Hallucination Cascade Prevention & Evidence Grounding*

에이전트가 임의로 창작한 환각(Hallucination)이 위키 문서에 기록될 경우, 이후 모든 세션의 에이전트들이 그 거짓 명제를 사실로 인용하여 위키 전체가 오염되는 **환각 연쇄(Hallucination Cascading)** 현상이 발생합니다.

- **원천 데이터 강제 정박 (Mandatory Grounding)**: 모든 핵심 주장, 설계 분석, 이론적 명제는 반드시 `raw/` 원천 텍스트 파일 경로 및 외부 공식 웹링크(URL)와 1:1로 매핑되어야 합니다.
- **모름의 명시**: 원천 데이터에 없는 정보나 교차 검증되지 않은 사실은 추측하지 않고 '모름' 또는 '미기록'으로 명시하여 잠재적 오염원을 원천 차단합니다.

### 5.2 지식 모순 방지를 위한 기계적 전수 감사
*Contradiction Drift Prevention & Automated Auditing*

문서의 수가 수십~수백 편으로 증가하면 과거에 작성된 문서와 최근 작성된 문서 간에 데이터 수치나 정책이 상충하는 **지식 모순(Contradiction Drift)**이 발생합니다.

- **자동화 감사 스크립트 운용**: [tool-scripts/audit_wiki.py](file:///Z:/wiki/tool-scripts/audit_wiki.py)와 같은 기계적 스크립트를 주기적으로 실행하여 이중 파일(.md/.html) 간 소제목·링크 불일치, 깨진 링크(Broken Link), 타임스탬프 누락 등을 전수 검증합니다.
- **정량적 감사 지표 보고**: 감사 완료 시 주관적 확언을 배제하고 통과/실패 문서 수, 바이트 크기, 일치율 등 정량적 데이터만을 객관적으로 제시합니다.

### 5.3 1인 주도형 거버넌스에서의 인간 개입 검증
*Human-In-The-Loop Verification in Single-Driven Governance*

에이전트에게 완전한 무감독 자율 쓰기 권한을 부여하지 않고, 최종 결정권자인 사용자(아저씨)의 승인 단계를 결합합니다.

- **Diff 기반 변경 보고**: 문서를 대규모로 수정하거나 분할할 때 변경 전후 섹션 매핑 표와 단락 수 증감 데이터를 보고합니다.
- **무손실 스냅샷 백업**: 대형 문서 재편 전에는 반드시 `raw/YYYYMMDD_[주제]_pre_split_backup.txt` 형태로 스냅샷을 동결하여 만약의 롤백 사태에 대비합니다.

## 6. 용어 정리 및 정의
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
<td><b>거대 언어 모델 위키</b></td>
<td><b>LLM Wiki</b>. 거대 언어 모델이 단순 질의응답기가 아닌 지식의 사서이자 컴파일러로 기능하며 직접 읽고, 합성하고, 백링크를 갱신하는 자가 유지형 장기 지식 저장소 체계.</td>
</tr>
<tr>
<td><b>위키 기반 검색 증강 생성</b></td>
<td><b>Wiki-RAG</b>. 파편화된 원시 청크 대신 사전 종합·컴파일된 위키 페이지를 검색 단위로 활용하여 추론 토큰을 절감하고 맥락 완성도를 극대화하는 검색 증강 패러다임.</td>
</tr>
<tr>
<td><b>사전 컴파일 지식</b></td>
<td><b>Pre-compiled Knowledge</b>. 쿼리 유입 시점에 정보를 종합하지 않고, 데이터 유입 시점에 에이전트가 미리 모순 해결과 요약을 완료해 둔 구조화 지식.</td>
</tr>
<tr>
<td><b>양방향 백링크</b></td>
<td><b>Bidirectional Wikilinks</b>. 문서 간 전진 링크와 역링크를 상호 추적 가능하게 구성하여 파일 시스템 내에서 지식 그래프 순회를 지원하는 하이퍼링크 구조.</td>
</tr>
<tr>
<td><b>환각 연쇄</b></td>
<td><b>Hallucination Cascading</b>. 에이전트가 잘못 생성한 명제가 위키에 한 번 영속화되면 후속 에이전트들이 이를 진실로 신뢰하고 재참조하여 오염이 기하급수적으로 확산되는 현상.</td>
</tr>
<tr>
<td><b>문맥 부패</b></td>
<td><b>Context Rot</b>. 컨텍스트 윈도우 내에 불필요한 태그 노이즈나 과도한 비구조화 정보가 누적되어 모델의 주의 집중력이 분산되고 지시 불이행이 발생하는 현상.</td>
</tr>
<tr>
<td><b>지식 증류</b></td>
<td><b>Knowledge Distillation</b>. 방대한 원천 텍스트로부터 노이즈를 제거하고 원자적 핵심 사실과 개념적 인과관계를 단계적으로 응축하는 정제 과정.</td>
</tr>
<tr>
<td><b>단일 진실 공급원</b></td>
<td><b>Single Source of Truth, SSOT</b>. 동일한 주제에 대해 복수의 모순된 사본을 두지 않고 모든 파생 뷰와 추론이 기준점으로 삼는 단일한 원본 데이터.</td>
</tr>
</tbody>
</table>

## 7. 참고 자료 및 원천 데이터 출처
*References & Raw Sources*

- **로컬 원천 데이터**:
  - [`raw/20260903_llm_wiki_system_architecture_raw.txt`](file:///Z:/wiki/raw/20260903_llm_wiki_system_architecture_raw.txt) (LLM 위키 시스템 아키텍처 원천 데이터 덤프 및 기술 명세)
  - [`raw/20260822_raw_data_management_strategy_raw.txt`](file:///Z:/wiki/raw/20260822_raw_data_management_strategy_raw.txt) (위키 3단계 데이터 저장 계층 원천 덤프)
  - [`raw/20260822_llm_wiki_format_debate_raw.txt`](file:///Z:/wiki/raw/20260822_llm_wiki_format_debate_raw.txt) (LLM 위키 포맷 논쟁 원천 덤프)
- **외부 학술 및 기술 출처**:
  - [Andrej Karpathy: Software 2.0 and Personal Knowledge Systems](https://x.com/karpathy) — 안드레이 카파시 공식 논의 아카이브
  - [Microsoft Research: From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130) — 마이크로소프트 GraphRAG 아키텍처 및 커뮤니티 서머리 논문
  - [Anthropic Research: Contextual Retrieval Architecture](https://www.anthropic.com/news/contextual-retrieval) — 앤트로픽 문맥 기반 인출 및 청크 오염 방지 표준
  - [Open Knowledge Format (OKF) Specification](https://github.com/) — YAML Frontmatter 기반 마크다운 지식 포맷 명세
- **사내 위키 연계 문서**:
  - [2계층 위키 문서 작성 및 관리 표준](file:///Z:/wiki/wiki_documentation_standards.html) ([.md](file:///Z:/wiki/wiki_documentation_standards.md))
  - [LLM 위키 원천·참고자료 적재 및 활용 전략](file:///Z:/wiki/raw_data_management_strategy.html) ([.md](file:///Z:/wiki/raw_data_management_strategy.md))
  - [LLM 위키 작성 포맷 논쟁: HTML5 vs Markdown 최신 현황](file:///Z:/wiki/llm_wiki_format_debate.html) ([.md](file:///Z:/wiki/llm_wiki_format_debate.md))
  - [LLM 위키 구축 및 지식 구조화 실무 가이드](file:///Z:/wiki/llm_wiki_construction_guide.html) ([.md](file:///Z:/wiki/llm_wiki_construction_guide.md))
  - [에이전트 가이드 (AGENTS.md)](file:///Z:/wiki/AGENTS.md)
  - [메인 인덱스 (index.html)](file:///Z:/wiki/index.html)
