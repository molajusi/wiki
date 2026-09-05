---
title: "LLM 위키 원천·참고자료 적재 및 활용 전략"
subtitle: "Raw Data Ingestion & Utilization Strategy for LLM Wiki"
created: "2026-08-22 오후 01:19:58 (KST, UTC+9)"
updated: "2026-08-22 오후 02:47:20 (KST, UTC+9)"
category: "위키 지식 관리 (Wiki Governance)"
tags: ["Wiki Management", "Raw Data", "Accumulation Protocol", "Utilization Protocol", "3-Tier Storage"]
html_view: "raw_data_management_strategy.html"
---

# LLM 위키 원천·참고자료 적재 및 활용 전략
*Raw Data Ingestion & Utilization Strategy for LLM Wiki*

**카테고리**: 위키 지식 관리 (Wiki Governance)  
*최초 작성일시: 2026-08-22 오후 01:19:58 (KST, UTC+9) | 최종 수정일시: 2026-08-22 오후 02:47:20 (KST, UTC+9)*

<context>
본 문서는 LLM 지식베이스(LLM Wiki) 내에 수집되는 원천 자료(Raw Data), 논문/기사 원문, 텍스트 덤프 및 참고 데이터를 효율적으로 적재하고 활용하기 위한 시스템 구조 및 프로토콜을 규정한 기계/인간 공용 단일 진실 공급원(SSOT) 문서입니다.
</context>

## 1. 개요 및 목적 (Overview & Purpose)
인간 사용자(아저씨)의 수동 분류 및 서식 가공 부담을 0으로 제거하고, 에이전트(자네)의 토큰 소비 최적화와 팩트 검증 정밀도를 동시에 달성하는 3단계 데이터 관리 모델과 프로토콜을 수립합니다.

## 2. 핵심 개념 및 원리 (Core Concept & Architecture)

### 2.1 3단계 데이터 저장 계층 (3-Tier Storage Architecture)
| 계층 | 저장 위치 및 포맷 | 담당 역할 및 특징 | 주요 활용 주체 |
| :--- | :--- | :--- | :--- |
| **[1계층] 메인 인덱스** | `Z:\wiki\index.html` | 전체 카테고리 및 주제 문서 색인 맵 | 인간 탐색 및 에이전트 엔트리 포인트 |
| **[2계층] 원천 데이터** | `Z:\wiki\raw\*` (TXT, JSON, Raw) | 원문 텍스트 덤프, 논문/기사 데이터, 파싱용 원시 데이터 | 에이전트 정밀 파싱 및 팩트 검증용 |
| **[3계층] 정제 위키** | `Z:\wiki\*.md` (SSOT) / `*.html` (View) | 요약, 비교표, 4대 필수 섹션 적용 구조화 문서 | 기계 메모리 및 인간 가독성 확보 |

## 3. 상세 분석 및 데이터 (Detailed Analysis & Data)

### 3.1 적재 프로토콜 (Accumulation Protocol)
1. **단일 파일 적재**: 대화창 평문이나 단일 파일 전달 시 `Z:\wiki\raw\YYYYMMDD_[주제]_raw.txt`로 개별 보존.
2. **다중 파일 그룹 적재 (Multi-File Ingestion)**: 자료가 다수일 경우 `Z:\wiki\raw\YYYYMMDD_[주제명]\` 서브 폴더를 생성하여 일괄 저장.
3. **위키 정제 생성 및 메타데이터 작성**: 에이전트는 원천 데이터를 분석하여 `*.md`(SSOT)와 `*.html`(View) 문서를 동시 파생 생성하며, 최상단에 12시간 표기법 타임존 메타데이터(`최초 작성일시`, `최종 수정일시`)를 필수 명시.
4. **상호 출처 추적 (Source Tracking)**: 주제 위키 `<footer>`에 `raw/` 원시 파일 또는 서브 폴더 경로를 링크로 명시.

### 3.2 활용 프로토콜 (Utilization Protocol)
| 구분 | 인간 (아저씨) 활용 방식 | 기계 (자네 에이전트) 활용 방식 |
| :--- | :--- | :--- |
| **일상적 조회** | `index.html`에서 정제 위키(`.html`)만 빠르게 브라우징하여 요약 확인 | 정제 위키(`.md`)만 참조하여 컨텍스트 토큰 소비 최소화 및 고속 응답 |
| **정밀 검증/상세 분석** | 주제 문서 하단 `raw/` 링크 클릭하여 원문 직접 교차 확인 | `raw/` 폴더 내 원문 파일만 지정하여 정밀 파싱 후 고정밀 답변 작성 |

<definitions>
## 4. 용어 정리 및 정의 (Terminology & Definitions)
- **Raw Data Layer**: 가공되지 않은 원문 기사, 논문 텍스트, 수집 덤프가 저장되는 `Z:\wiki\raw\` 하위 데이터 계층.
- **Processed Wiki Layer**: 원천 데이터를 바탕으로 4대 필수 섹션을 적용하여 정제한 `Z:\wiki\*.md` 및 `*.html` 지식 문서 계층.
- **Accumulation Protocol**: 원시 데이터 접수부터 `raw/` 저장, 위키 정제, 출처 링크 추적까지의 일련의 데이터 적재 절차.
- **Utilization Protocol**: 인간 및 에이전트가 토큰 효율성과 데이터 정확도에 맞춰 1계층/2계층/3계층 데이터를 선택적으로 사용하는 조회 규칙.
</definitions>
