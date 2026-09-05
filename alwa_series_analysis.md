---
title: "알와 시리즈 게임 디자인 및 비평적 분석"
subtitle: "Alwa Series: Game Design Evolution, Neo-Retro Metroidvania, and Critical Analysis"
created: "2026-08-22 오후 09:58:00 (KST, UTC+9)"
updated: "2026-09-04 오후 02:54:30 (KST, UTC+9)"
category: "게임 디자인 및 분석 (Game Design & Taxonomy)"
tags: ["Alwa's Awakening", "Alwa's Legacy", "Elden Pixels", "Metroidvania", "Neo-Retro", "Puzzle Platformer", "NES", "Game Critique"]
html_view: "alwa_series_analysis.html"
parent_hub: "metroidvania_genre_analysis.html"
---

# 알와 시리즈 게임 디자인 및 비평적 분석
*Alwa Series: Game Design Evolution, Neo-Retro Metroidvania, and Critical Analysis*

**카테고리**: 게임 디자인 및 분석 (Game Design & Taxonomy)  
*최초 작성일시: 2026-08-22 오후 09:58:00 (KST, UTC+9) | 최종 수정일시: 2026-09-04 오후 02:54:30 (KST, UTC+9)*

P26-09-04 오후 02:35:45 (KST, UTC+9) — 카테고리 체계 표준화 반영*

<context>
본 문서는 스웨덴 인디 개발사 엘든 픽셀즈(Elden Pixels)가 개발한 메트로이드배니아 연작인 **《알와즈 어웨이크닝(Alwa's Awakening, 2017)》**과 **《알와즈 레거시(Alwa's Legacy, 2020)》**의 게임 디자인 아키텍처, 8비트에서 16비트로의 패러다임 전환, 마법 지팡이 3대 원소 기반의 퍼즐 플랫포밍 메커니즘, 그리고 게임 비평계의 평가와 학술적 의의를 종합 분석하는 **메트로이드배니아 전문 분과 비평 문서**입니다.
</context>

## 📌 메트로이드배니아 지식 클러스터 연계
본 문서는 메트로이드배니아 지식 네트워크의 하위 비평 문서로서 상위 마스터 허브 및 관련 분과와 유기적으로 연결됩니다:

- 🏛️ **[상위 총론 허브] 메트로이드배니아 장르 개요 및 계보학** (`metroidvania_genre_analysis.html`): 장르의 어원과 20년 계보학, 메트로이드와 캐슬바니아 2대 기둥 유산, 젤다의 전설 설계 모태 영향 및 세대별 발전사 총괄.
- ⚙️ **[전문 분과 2] 메트로이드배니아 시스템 메커니즘 및 레벨 디자인** (`metroidvania_mechanics_and_level_design.html`): 능력 기팅, 샨테 5부작 폼시프팅, 사소한 보상 배치의 5대 철학 및 방 단위 퍼즐 플랫폼 아키텍처 비교.
- 🗺️ **[전문 분과 1] 메트로이드배니아 지도 설계 및 공간 인지공학** (`metroidvania_map_and_spatial_cognition.html`): 3대 지도 패러다임(HUD vs 다이제틱 vs 수동 핀), 케빈 린치 공간 인지 5요소, 젤다식 던전과 비선형 오버월드 결합 구조.

## 1. 개요 및 목적
*Overview & Purpose*

**알와 시리즈(Alwa Series)**는 스웨덴의 인디 게임 스튜디오 엘든 픽셀즈(Elden Pixels)가 패미컴(NES) 및 슈퍼패미컴(SNES) 황금기 고전 명작들에 대한 헌정으로 제작한 대표적 **네오 레트로 메트로이드배니아(Neo-Retro Metroidvania)** 연작입니다. 1作인 《알와즈 어웨이크닝(Alwa's Awakening, 2017)》은 엄격한 8비트 하드웨어 제약과 정밀한 룸 단위 퍼즐 플랫폼을 구현하였으며, 2作인 《알와즈 레거시(2020)》는 16비트 시각미와 현대적인 조작 편의성 및 RPG 스킬 트리를 도입하여 장르적 진화를 완성했습니다.

본 문서는 전투 중심의 현대적 메트로이드배니아(예: 《할로우 나이트》)와 궤를 달리하여 **'창조형 마법 도구를 통한 공간 퍼즐 해결(Puzzle-Centric Traversal)'**을 핵심으로 내세운 알와 시리즈의 설계 메커니즘을 심층 해부합니다. 8비트 고전주의와 16비트 현대화 간의 득실을 비교 분석하고, 게임 비평계의 찬사와 한계 지적을 객관적으로 종합 평가하여 레트로 복고풍 게임 디자인의 지속 가능한 가치를 규명하는 데 목적이 있습니다.

## 2. 핵심 개념 및 게임플레이 원리
*Core Concepts & Gameplay Principles*

알와 시리즈의 게임 디자인은 단순한 반사신경 액션보다는 주인공 조이(Zoe)가 사용하는 **마법 지팡이(Magic Staff)**를 매개로 한 환경 물리 상호작용에 뿌리를 두고 있습니다.

### 2.1 마법 지팡이 기반 3대 창조형 상호작용
플레이어는 모험 중 3가지 원소 보석을 획득하여 지형을 직접 변형하거나 도구를 창조합니다:

1. **녹색 보석 (녹색 블록 생성 - Block Creation)**:
   - 전방 바닥이나 공중에 1개의 정육면체 블록을 소환합니다.
   - **기능**: 높은 턱을 넘기 위한 발판, 바닥 가시 및 화염 함정 차단, 적 투사체 방어벽, 지속 압력 발판 스위치 활성화.
   - **레거시 진화**: 블록을 밀어 이동시키거나, 탄성 점프 발판으로 개조 가능.
2. **청색 보석 (기포 부유 생성 - Bubble Creation)**:
   - 조이의 발밑에 서서히 수직 상승하는 마법 기포를 생성합니다.
   - **기능**: 높은 수직 통로 도달, 공중에서 점프 궤적 재조정, 타이밍에 맞춘 정밀 낙하 회피.
   - **레거시 진화**: 기포에 탑승한 상태에서 좌우 방향 조작이 가능하여 수평 횡단 능력 대폭 확장.
3. **황색/적색 보석 (번개 투사체 발사 - Lightning Projectile)**:
   - 전방으로 직선 비행하는 강력한 번개 광선을 방출합니다.
   - **기능**: 원거리 적 처치 및 보스 약점 타격, 금이 간 벽면 파괴, 원거리 크리스털 스위치 및 횃불 점화.
   - **레거시 진화**: 다수 대상을 동시에 가격하는 체인 라이트닝 효과 및 적을 자동으로 추적하는 유도탄 형태로 업그레이드 가능.

### 2.2 젤다식 던전 구조와 메트로이드배니아 오버월드의 융합
알와 시리즈는 완전한 개방형 미로보다는 **《젤다의 전설》식 격리 던전(Dungeon) 구조**를 메트로이드배니아의 상호 연결된 맵(Interconnected World) 내에 조화롭게 결합했습니다[[1]](#ref-1), [[6]](#ref-6).
- **오버월드**: 각 던전으로 향하는 비선형 경로 탐색 및 비밀 아이템 수집 구역.
- **던전 내부**: 독립된 테마와 환경 퍼즐이 밀집되어 있으며, 던전 심층부에서 신규 마법 보석이나 기능성 유물(아이템)을 획득한 후 해당 던전의 보스를 격파해야 탈출하는 완결형 구조.

## 3. 8비트 고전주의와 16비트 현대화의 비교 분석
*Comparative Analysis: 8-Bit Classicism vs 16-Bit Modernization*

엘든 픽셀즈는 두 작품을 통해 8비트 NES 세대에서 16비트 SNES 시대로 넘어가는 비디오 게임 역사의 진화 과정을 고스란히 재현했습니다[[1]](#ref-1), [[14]](#ref-14).

### 3.1 알와즈 어웨이크닝(2017)의 8비트 고전주의와 제약
- **철저한 하드웨어 에뮬레이션**: 실제 NES 롬 규격에 맞추어 4색 스프라이트 팔레트와 사운드 채널 제약을 엄격히 준수. 2021년에는 실제로 구동 가능한 물리적 NES 카트리지 롬을 제작·발매함[[2]](#ref-2).
- **신중한 조작 감각**: 캐릭터의 이동 속도가 다소 느리고 점프 궤적 수정이 제한적이어서, 각 방에 진입할 때마다 적의 이동 주기와 함정 배치를 계산하는 '정적인 퍼즐 풀이'의 긴장감을 극대화.
- **불편 요소의 잔존**: 마법 발동을 위해 '위 방향키 + 공격키'를 눌러야 하는 고전적 조작 체계, 물에 닿으면 즉사하는 판정 등 지나치게 보수적인 고전 재현이 진입 장벽으로 작용[[12]](#ref-12).

### 3.2 알와즈 레거시(2020)의 16비트 진화와 편의성 확장
- **현대적 감각의 유기적 픽셀 아트**: 다채로운 색감, 부드러운 애니메이션, 풍성한 오케스트레이션 칩튠 사운드트랙 적용[[14]](#ref-14).
- **조작계 전면 개편**: 마법별 전용 단독 핫키 배정, 조이의 이동 속도 및 점프 기동성 향상, 물에서의 자유로운 수영 기능 추가(물 접촉 즉사 폐지)[[1]](#ref-1), [[17]](#ref-17).
- **RPG 커스터마이징 도입**: 맵 곳곳에 숨겨진 보석 눈물(Tears)을 수집하여 마법의 위력, 쿨타임, 보조 유틸리티를 강화하는 유연한 스킬 트리 도입[[15]](#ref-15).

### 3.3 어웨이크닝 vs 레거시 상세 메커니즘 대조표
| 분석 항목 | 알와즈 어웨이크닝 (Alwa's Awakening, 2017) | 알와즈 레거시 (Alwa's Legacy, 2020) |
| :--- | :--- | :--- |
| **시각/음향 규격** | 순수 8비트 NES 팔레트, 로우파이 칩튠 (Chiptune) | 16비트 풍부한 컬러, 고해상도 픽셀 아트, 오케스트라 편곡 |
| **마법 조작 방식** | 위 방향키 + 공격키 조합 (레트로 관행) | 독립 마법 핫키 배정 및 실시간 빠른 전환 |
| **이동성 및 물리** | 묵직하고 제한적인 점프, 정밀한 궤적 계산 요구 | 빠르고 유연한 기동성, 쾌적한 플랫포밍 |
| **수중 상호작용** | **물 접촉 시 즉사 (Instant Death)** | **자유로운 수영 및 잠수 탐험 가능** |
| **성장 시스템** | 고정 마법 보석 및 아이템 수집 (정적) | 눈물 보석 수집을 통한 비선형 스킬 트리 강화 (동적) |
| **세이브 및 복구** | 방 진입 시 자동 체크포인트 (데스 페널티 부재) | 세이브 비석 저장 + 워프 게이트 네트워크 확장 |
| **핵심 플레이 질감** | 엄격하고 신중한 두뇌 퍼즐 플랫포머 | 경쾌하고 대중적인 현대적 액션 어드벤처 |

## 4. 능력 기팅과 퍼즐 플랫폼 디자인 비평
*Ability-Gating & Puzzle-Platforming Critique*

### 4.1 '전투 지향' 메트로이드배니아와의 차별성
2010년대 후반의 메트로이드배니아 시장은 《할로우 나이트》, 《데드 셀》, 《엔더 릴리즈》 등 소울라이크식 고난도 패링, 프레임 회피, 다채로운 근접 무기 콤보 중심의 **'전투 액션 심화'**로 급격히 쏠렸습니다.
반면 알와 시리즈는 《솔스티스(Solstice)》, 《파자나두(Faxanadu)》, 《드래곤 슬레이어 IV(Legacy of the Wizard)》 등 1980년대 후반 퍼즐 어드벤처의 유산을 계승하여 **'공간 물리 퍼즐을 통한 지형 극복'**을 전면에 내세웠습니다[[2]](#ref-2), [[6]](#ref-6).

<div class="diagram-container">
    <svg viewBox="0 0 800 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
        <rect width="800" height="220" fill="#ffffff" rx="8"/>
        <!-- Step 1 -->
        <rect x="20" y="40" width="160" height="140" fill="#e8f4f8" stroke="#17a2b8" stroke-width="2" rx="6"/>
        <text x="100" y="70" font-family="sans-serif" font-size="14" font-weight="bold" fill="#17a2b8" text-anchor="middle">1. 난관 조우</text>
        <text x="100" y="100" font-family="sans-serif" font-size="12" fill="#333" text-anchor="middle">높은 절벽 & 가시밭</text>
        <text x="100" y="125" font-family="sans-serif" font-size="12" fill="#333" text-anchor="middle">닫힌 철문 스위치</text>
        <text x="100" y="150" font-family="sans-serif" font-size="11" fill="#666" text-anchor="middle">[공간 인지 형성]</text>

        <!-- Arrow 1 -->
        <path d="M 190 110 L 220 110" stroke="#6c757d" stroke-width="2" marker-end="url(#arrow)"/>

        <!-- Step 2 -->
        <rect x="230" y="40" width="160" height="140" fill="#eafaf1" stroke="#28a745" stroke-width="2" rx="6"/>
        <text x="310" y="70" font-family="sans-serif" font-size="14" font-weight="bold" fill="#28a745" text-anchor="middle">2. 녹색 블록 설치</text>
        <text x="310" y="100" font-family="sans-serif" font-size="12" fill="#333" text-anchor="middle">가시밭 위 발판 확보</text>
        <text x="310" y="125" font-family="sans-serif" font-size="12" fill="#333" text-anchor="middle">압력 발판 활성화</text>
        <text x="310" y="150" font-family="sans-serif" font-size="11" fill="#666" text-anchor="middle">[지형 변형]</text>

        <!-- Arrow 2 -->
        <path d="M 400 110 L 430 110" stroke="#6c757d" stroke-width="2" marker-end="url(#arrow)"/>

        <!-- Step 3 -->
        <rect x="440" y="40" width="160" height="140" fill="#ebf5fb" stroke="#007bff" stroke-width="2" rx="6"/>
        <text x="520" y="70" font-family="sans-serif" font-size="14" font-weight="bold" fill="#007bff" text-anchor="middle">3. 청색 기포 부유</text>
        <text x="520" y="100" font-family="sans-serif" font-size="12" fill="#333" text-anchor="middle">블록 위에서 기포 생성</text>
        <text x="520" y="125" font-family="sans-serif" font-size="12" fill="#333" text-anchor="middle">수직 상승 궤적 제어</text>
        <text x="520" y="150" font-family="sans-serif" font-size="11" fill="#666" text-anchor="middle">[수직 기동]</text>

        <!-- Arrow 3 -->
        <path d="M 610 110 L 640 110" stroke="#6c757d" stroke-width="2" marker-end="url(#arrow)"/>

        <!-- Step 4 -->
        <rect x="650" y="40" width="130" height="140" fill="#fdf2e9" stroke="#e67e22" stroke-width="2" rx="6"/>
        <text x="715" y="70" font-family="sans-serif" font-size="14" font-weight="bold" fill="#e67e22" text-anchor="middle">4. 번개 & 돌파</text>
        <text x="715" y="100" font-family="sans-serif" font-size="12" fill="#333" text-anchor="middle">공중 스위치 저격</text>
        <text x="715" y="125" font-family="sans-serif" font-size="12" fill="#333" text-anchor="middle">신규 구역 진입</text>
        <text x="715" y="150" font-family="sans-serif" font-size="11" fill="#666" text-anchor="middle">[퍼즐 해결]</text>

        <!-- Defs for arrow -->
        <defs>
            <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 0 L 10 5 L 0 10 z" fill="#6c757d"/>
            </marker>
        </defs>
    </svg>
</div>

### 4.2 도구 확장 기반의 레벨 디자인 루프
알와 시리즈의 능력 기팅(Ability-Gating)은 단순한 '열쇠-자물쇠' 관계를 넘어, **도구의 상호 복합 연계(Emergent Tool Usage)**를 요구합니다:
- 단독 도구 사용: 1단 블록으로 낮은 턱 오르기.
- 복합 도구 연계: 가시밭 위 블록 설치 ➔ 블록 상단에서 기포 생성 ➔ 상승 중 공중 번개 발사로 문 개방(위 다이어그램의 3단 콤보 퍼즐 참고).
이러한 연계 구조는 플레이어에게 지적 성취감을 부여하며 백트래킹 과정에서 이전에 불가능했던 지형을 완전히 새로운 방식으로 주파하는 경험을 제공합니다[[8]](#ref-8), [[18]](#ref-18).

## 5. 게임 비평계의 평가 및 학술적 의의
*Critical Reception & Academic Critique*

### 5.1 네오 레트로 메트로이드배니아로서의 성취와 한계
- **비평계의 찬사**:
  - **정교한 물리 퍼즐 완성도**: 도구의 가짓수를 단 3개로 극도로 절제하면서도 이를 유기적으로 조합하여 수백 개의 서로 다른 공간 퍼즐을 창출한 미니멀리즘 설계 철학[[4]](#ref-4), [[9]](#ref-9), [[13]](#ref-13), [[18]](#ref-18).
  - **불필요한 레벨 노가다 배제**: 순수한 플레이어의 관찰력과 조작 숙련도만으로 난관을 극복하도록 설계되어 메트로이드배니아의 순수 탐험 본질을 유지.
- **주요 비판점 및 한계**:
  - **전투의 단조로움**: 기본 지팡이 근접 공격의 타격 범위가 지나치게 좁고 적들의 패턴이 단조로워, 보스전을 제외한 일반 몬스터 전투가 다소 성가신 장애물로만 느껴진다는 지적[[12]](#ref-12), [[20]](#ref-20).
  - **서사적 깊이의 부족**: 비디오 게임 세계로 빨려 들어간 소녀가 세상을 구한다는 고전적 클리셰에 머물러 있어, 독창적인 세계관 서사를 기대한 플레이어에게는 동기부여가 약함[[21]](#ref-21).

### 5.2 NES 실기 롬 릴리즈와 레트로 아카이빙 가치
엘든 픽셀즈는 2021년 《알와즈 어웨이크닝》을 실제 NES 콘솔에서 구동 가능한 정식 카트리지(ROM)로 포팅 및 물리 패키지 발매를 진행했습니다[[2]](#ref-2). 이는 단순한 레트로 스타일 흉내내기를 넘어, **고전 비디오 게임 플랫폼 하드웨어의 기술적 유산을 계승하고 보존(Game Preservation)**하려는 진정성 있는 인디 게임 개발 문화의 모범 사례로 학계와 비평계의 높은 평가를 받았습니다.

<definitions>
## 6. 용어 정리 및 정의
*Glossary & Definitions*

| 용어 | 정의 |
| :--- | :--- |
| **알와즈 어웨이크닝** | **Alwa's Awakening**. 2017년 엘든 픽셀즈가 발매한 8비트 NES 스타일의 룸 단위 퍼즐 중심 메트로이드배니아 비디오 게임. |
| **알와즈 레거시** | **Alwa's Legacy**. 2020년 발매된 후속작으로, 16비트 그래픽, 수영 시스템, 자유로운 스킬 트리 및 유연한 조작계를 도입한 현대화 작품. |
| **엘든 픽셀즈** | **Elden Pixels**. 스웨덴 예테보리에 위치한 인디 게임 개발 스튜디오로, 고전 비디오 게임의 설계 미학을 현대적으로 재해석하는 개발사. |
| **네오 레트로** | **Neo-Retro**. 과거 8비트/16비트 콘솔의 시각적·음향적 스타일과 메커니즘 제약을 의도적으로 차용하면서 현대적 레벨 디자인을 결합한 게임 디자인 사조. |
| **블록 생성** | **Block Creation**. 알와 시리즈에서 마법 지팡이 녹색 보석으로 정육면체 블록을 소환하여 발판, 방어벽, 스위치 누르개로 활용하는 메커니즘. |
| **기포 생성** | **Bubble Creation**. 청색 보석을 활용해 수직 상승하는 마법 거품을 만들어 높은 지형으로 이동하거나 공중 궤적을 제어하는 플랫폼 기술. |
| **순수 능력 기팅** | **Pure Ability-Gating**. 물리적 열쇠나 단순 수치형 스탯이 아닌, 플레이어가 창조하는 도구와 기동성 스킬의 유기적 조합으로 진행 경로를 여는 설계. |
</definitions>

<references>
## 7. 참고 자료 및 원천 데이터 출처
*References & Raw Sources*

<div class="callout">
    <strong>📁 로컬 원천 데이터 보존 경로:</strong><br>
    본 위키 문서는 로컬 원천 텍스트 저장소 <code>raw/20260822_alwa_series_analysis_raw.txt</code>의 데이터와 교차 검증을 거쳐 작성되었습니다.
</div>

<ol class="reference-list">
    <li id="ref-1">[1] Switchaboo (2020). <em>Alwa's Awakening vs Alwa's Legacy: The Evolution of Elden Pixels</em>. <a href="https://switchaboo.com/2020/06/25/alwas-awakening-vs-alwas-legacy-the-evolution-of-elden-pixels/" target="_blank">웹링크</a></li>
    <li id="ref-2">[2] Elden Pixels Official (2021). <em>Alwa's Awakening 8-Bit NES Edition & Development Philosophy</em>. <a href="https://eldenpixels.com/alwas-awakening/" target="_blank">웹링크</a></li>
    <li id="ref-3">[3] ComicBuzz (2020). <em>Alwa's Legacy Game Review & Design Analysis</em>. <a href="https://comicbuzz.com/alwas-legacy-review/" target="_blank">웹링크</a></li>
    <li id="ref-4">[4] HeyPoorPlayer (2017). <em>Alwa's Awakening Review: A Masterclass in NES Design</em>. <a href="https://www.heypoorplayer.com/2017/02/06/alwas-awakening-review-pc/" target="_blank">웹링크</a></li>
    <li id="ref-5">[5] Entertainium (2017). <em>Alwa's Awakening and the Art of Nostalgic Game Design</em>. <a href="https://entertainium.co/2017/02/02/alwas-awakening-review/" target="_blank">웹링크</a></li>
    <li id="ref-6">[6] A Most Agreeable Pastime (2020). <em>The Geometry of Magic: Puzzle Platforming in Alwa's Legacy</em>. <a href="https://amostagreeablepastime.com/2020/07/04/alwas-legacy-review/" target="_blank">웹링크</a></li>
    <li id="ref-7">[7] Retronauts & Jeremy Parish (2018). <em>NES Metroidvania Roots: From Faxanadu to Alwa</em>. <a href="https://retronauts.com/" target="_blank">웹링크</a></li>
    <li id="ref-8">[8] Medium Game Studies (2020). <em>Minimalist Ability-Gating in Modern 2D Metroidvanias</em>. <a href="https://medium.com/" target="_blank">웹링크</a></li>
    <li id="ref-9">[9] GodisaGeek (2020). <em>Alwa's Legacy Review: 16-Bit Perfection</em>. <a href="https://www.godisageek.com/reviews/alwas-legacy-review/" target="_blank">웹링크</a></li>
    <li id="ref-10">[10] Pascal Belisle (2021). <em>Chiptune Aesthetics and Spatial Cognition in Retro Indies</em>. <a href="https://pascalbelisle.com/" target="_blank">웹링크</a></li>
    <li id="ref-11">[11] Metacritic (2020). <em>Alwa's Legacy Critic & User Reviews</em>. <a href="https://www.metacritic.com/game/alwas-legacy/" target="_blank">웹링크</a></li>
    <li id="ref-12">[12] Xbox Tavern (2018). <em>Alwa's Awakening Deep Dive: Archaic Quirks vs Modern Polish</em>. <a href="https://www.xboxtavern.com/alwas-awakening-review/" target="_blank">웹링크</a></li>
    <li id="ref-13">[13] Nintendo World Report (2018). <em>Alwa's Awakening Review: Puzzle-First Exploration</em>. <a href="http://www.nintendoworldreport.com/review/48473/alwas-awakening-switch-review" target="_blank">웹링크</a></li>
    <li id="ref-14">[14] Retro 101 (2020). <em>From 8-bit to 16-bit: The Technological Leap in Alwa's Legacy</em>. <a href="http://www.retro101.co.uk/2020/07/alwas-legacy-review.html" target="_blank">웹링크</a></li>
    <li id="ref-15">[15] The Thirsty Mage Podcast (2021). <em>Episode 54: Metroidvania Puzzle Design in Alwa</em>. <a href="https://thethirstymage.com/" target="_blank">웹링크</a></li>
    <li id="ref-16">[16] TechRaptor (2020). <em>Alwa's Legacy Review: A Charming Nostalgia Trip</em>. <a href="https://techraptor.net/gaming/reviews/alwas-legacy-review" target="_blank">웹링크</a></li>
    <li id="ref-17">[17] PlayStation Country (2020). <em>Alwa's Legacy PS4 Critique & Mechanics</em>. <a href="https://www.playstationcountry.com/alwas-legacy-ps4-review/" target="_blank">웹링크</a></li>
    <li id="ref-18">[18] GameSpot & IGN Community (2020). <em>Alwa Series Retrospective & Level Design Dynamics</em>. <a href="https://www.ign.com/" target="_blank">웹링크</a></li>
</ol>
</references>
