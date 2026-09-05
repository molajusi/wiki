---
title: "메트로이드배니아 및 카토그래피 게임 디자인 종합 연구 아카이브"
subtitle: "Metroidvania & Cartography Game Design Comprehensive Research Archive"
created: "2026-08-24 오후 12:26:56 (KST, UTC+9)"
updated: "2026-08-24 오후 12:26:56 (KST, UTC+9)"
category: "일반 지식 및 게임 디자인 (Game Design & Taxonomy)"
tags: ["Metroidvania", "Cartography", "Level Design", "Metroidbrainia", "Game Taxonomy", "Academic Research"]
html_view: "metroidvania_and_cartography_game_design.html"
---

# 메트로이드배니아 및 카토그래피 게임 디자인 종합 연구 아카이브
*Metroidvania & Cartography Game Design Comprehensive Research Archive*

**카테고리**: 일반 지식 및 게임 디자인 (Game Design & Taxonomy)  
*최초 작성일시: 2026-08-24 오후 12:26:56 (KST, UTC+9) | 최종 수정일시: 2026-08-24 오후 12:26:56 (KST, UTC+9)*

<context>
본 문서는 메트로이드배니아 장르와 비디오 게임 내 지도 제작학(Cartography), 공간 인지 및 레벨 디자인 구조, 2차원 사이드뷰와 축척 지도의 위상 불일치 해결 기제, 비(非)중세 판타지 배경의 던전 대체 설계 및 지식 기반 탐험(Metroidbrainia)에 관한 학술 문헌과 개발 사례를 체계적으로 집대성한 지식 아카이브입니다.
</context>

## 1. 개요 및 목적
*Overview & Purpose*

본 아카이브는 전통적인 메트로이드배니아(Metroidvania) 장르의 잠금-해제 구조 및 레벨 위상학(Topology) 연구와 더불어, 비디오 게임 지도 인터페이스(In-Game Cartography)가 플레이어의 인지 및 탐험 경험에 미치는 영향을 다학제적으로 분석하는 것을 목적으로 합니다.

물리적 이동 능력의 확장에 기반한 전통적 능력 게이팅(Ability Gating)뿐만 아니라, 플레이어의 순수 인지적 지식 축적을 핵심 동력으로 삼는 메트로이드브레이니아(Metroidbrainia)의 설계 원리를 분석합니다. 아울러 2D 사이드뷰 공간과 맵 축척 간의 기하학적 왜곡을 해소하는 4대 개발 패러다임과 현대적·SF·신화적 배경에서의 던전 대체 구조를 정리합니다.

## 2. 핵심 개념 및 원리
*Core Concepts & Principles*

메트로이드배니아와 게임 지도학의 상호작용은 다음 3가지 핵심 축을 중심으로 전개됩니다:

1. **위상 그래프 기반 진행 구조 (Graph-Based Progression):** 메트로이드배니아의 본질은 특정 테마의 던전이 아닌, '진입 장벽(Lock)'과 '해제 기제(Key)'가 비선형적 루프로 연결된 상호 연결형 공간 그래프(Interconnected Spatial Graph)에 있습니다.
2. **외장화된 작업 기억으로서의 지도 (Cartography as External Working Memory):** 게임 내 지도는 단순한 길찾기 UI를 넘어, 플레이어의 공간적 작업 기억(Working Memory)을 보조하고 탐색의 미완결 영역을 시각화하여 내적 탐구 동기를 유발하는 핵심 매커니즘입니다.
3. **지식과 물리 능력의 게이팅 이원화 (Knowledge vs. Physical Gating):** 물리적 조작 능력 획득(이단 점프, 대시 등)을 통한 잠금 해제와, 세계의 규칙 및 암호 해독을 통한 지식 기반 잠금 해제(Ending-From-Beginning 구조)의 공존 및 차별화가 장르의 외연을 확장합니다.

```
[메트로이드배니아의 핵심 구조적 루프]
  접근 불가 (Inaccessible Barrier) 
       │
       ▼
  신규 기제 획득 (Acquisition: 능력 / 장비 / 지식)
       │
       ▼
  재접근 및 경로 개방 (Bypass / Unlock / Short-cut)
```

## 3. 학술 문헌 및 장르론 연구
*Academic Literature & Genre Theory*

### 3.1. 메트로이드배니아 및 지식 기반 탐험 장르론
*Metroidvania & Knowledge-Based Exploration Genre Theory*

최근 게임학 및 인간-컴퓨터 상호작용(HCI) 연구에서는 메트로이드배니아의 공간 구조와 지식 기반 탐험 양식에 대한 이론적 정형화가 활발히 진행되고 있습니다.

#### 지식 기반 탐험 게임의 장르론적 범주화
Maleki(2025)는 《Metroidbrainia: A Genre Analysis of Knowledge-Based Exploration Games》를 통해 물리적 능력 획득(Ability Gating)에 의존하는 전통적 메트로이드배니아와 달리, 플레이어가 습득하는 '지식 게이트(Knowledge Gate)'를 중심으로 전개되는 게임군을 **'메트로이드브레이니아(Metroidbrainia)'**로 정의하고 학술적으로 범주화하였습니다.

* **지식 게이트(Knowledge Gate) 3분류:**
  * **명시적 지식 (Clear Knowledge):** 인터페이스나 명확한 텍스트를 통해 플레이어에게 직접 전달되는 규칙 체계.
  * **모호한 지식 (Cryptic Knowledge):** 환경 곳곳에 흩어진 단서의 파편을 수집하고 조합해야만 해독할 수 있는 은닉 규칙.
  * **숨겨진 지식 (Hidden Knowledge):** 세계관의 근본 물리 법칙이나 UI상에 드러나지 않는 비가시적 시스템 메커니즘.
* **핵심 설계 철학:** 게임 시작 시점부터 최종 도달 지점이나 엔딩 구역으로 통하는 물리적 경로가 이미 개방되어 있는 **'Ending-From-Beginning'** 구조를 가집니다. 플레이어는 물리적 차단이 아니라 작동 규칙에 대한 무지(Ignorance)로 인해 진입하지 못합니다.
* **분석 대상 타이틀 (13종):** *Animal Well*, *The Witness*, *Myst*, *Castlevania: Symphony of the Night (SotN)*, *Outer Wilds*, *Metroid*, *Super Metroid*, *Return of the Obra Dinn*, *Chants of Sennaar*, *Tunic*, *Hollow Knight*, *Blue Prince*, *Toki Tori 2+* (참고문헌 72편 수록).

#### 구조적 구성 요소 및 프레임워크 연구
Oliveira et al.(2020)은 《A Framework for Metroidvania Games》(SBGames)에서 메트로이드배니아의 구조적 구성 요소를 다음 3가지 핵심 영역으로 분해하여 체계화하였습니다:
1. **레벨 디자인 (Topology):** 방들의 상호 연결성, 루프 구조, 수직/수평 이동 경로의 배치.
2. **진행 제어 (Progression):** 잠금과 해제 메커니즘, 능력 획득 순서의 트리 구조.
3. **플레이어 피드백 (Feedback):** 미개방 통로의 인지, 맵 갱신, 환경적 시각 단서 제공.
* *분석 대상 타이틀:* *Metroid*, *Super Metroid*, *Castlevania: SotN*, *Chasm*, *Axiom Verge*, *Celeste*.

#### 절차적 생성 및 진화 연산 적용 연구
Rodríguez, Cotta & Leiva(2018)는 《An Evolutionary Approach to Metroidvania Videogame Design》을 통해 유전 알고리즘(Evolutionary Algorithms)을 활용한 메트로이드배니아 레벨의 절차적 생성(Procedural Generation) 및 자동화된 잠금-해제 그래프 생성 기법을 연구하였습니다.

#### 학술 인용 지표 (Semantic Scholar 기준)
* Apperley (2006): 506회 인용 (디지털 게임 장르론의 기초 문헌).
* Arsenault (2009): 189회 인용 (비디오 게임 장르 진화론).
* 메트로이드배니아 전용 세부 논문군(Oliveira et al., Rodríguez et al., Maleki 등)은 현재 학술적 개념 형성 및 확장 초기 단계로 인용 지수가 0~수십 회 수준에 분포합니다.

### 3.2. 비디오 게임 지도학 및 인터페이스 분류
*Video Game Cartography & Interface Classification*

Dormann, Pötscher & Wallner(2023)는 《A Classification of Video Game Cartographic Maps》(DiGRA)에서 게임 내 지도를 5개 카테고리로 분류하고 장르별 지도 설계 철학을 비교 분석하였습니다.

#### 게임 내 지도 카테고리 5분류
1. **월드 맵 (World Map):** 전체 세계의 거시적 지리 정보 및 대륙 간 연결망 제공.
2. **에어리어 맵 (Area Map):** 특정 구역/지역 내 세부 연결 구조 및 세부 경로 표시.
3. **시티 맵 (City Map):** 인구 밀집 구역, 시설물, 상점 및 NPC 위치 중심 정보 제공.
4. **청사진 맵 (Blueprint Map):** 건축물 내부, 배관망, 던전의 상세 평면 구조도.
5. **미니맵 (Minimap):** 화면 한구석에 실시간 탐색 및 위험 요소 보조를 위해 상시 표시되는 국소 UI.

#### 장르별 지도 설계 철학 비교

| 장르 | 지도의 기능적 역할 | 설계 철학 및 특징 |
| :--- | :--- | :--- |
| **RPG** | 정보 인터페이스 (Information Interface) | 퀘스트, 상점, NPC 등 시스템 데이터의 종합 브라우저 역할 수행 |
| **액션 어드벤처** | 공간감 전달 (Spatial Sense) | 플레이어 이동 궤적 시각화 및 경로 탐색 보조 |
| **MMORPG** | 전략 정보 (Strategic Data) | 레이드 경로, 파티원 위치, 자원 분포의 실시간 동기화 |
| **오픈 월드** | 임무 관리 (Task Management) | 수많은 관심 지점(POI)과 퀘스트 웨이포인트의 계층적 관리 |
| **호러 / 잠입** | 의도적 불완전성 (Intentional Incompleteness) | 지도 정보를 제한하여 미지의 공포 및 취약성(Vulnerability) 극대화 |
| **SF** | 다이어제틱 오브젝트 (Diegetic Object) | 3D 홀로그램, 슈트 헬멧 HUD 등 세계관 내 실존 장비로 연출 |
| **워킹 시뮬레이터** | 몰입형 촉각 지도 (Tactile Map) | UI 오버레이를 배제하고 종이 지도, 나침반 등 물리적 소품 활용 |

* **《Hollow Knight》의 특수 사례 분석:** 지도를 기본 UI로 제공하지 않고, 미지의 구역을 탐험하여 지도 제작자(코니퍼)를 찾아 지도를 구매한 뒤, 휴식처(벤치)에서 깃펜으로 직접 갱신하게 설계되었습니다. 이를 통해 '지도 획득 및 완성 자체를 탐험의 직접적 인게임 보상'으로 승화시킨 대표 사례로 평가받습니다.

#### 마커 시스템 분류 체계
Toups et al.(2019)은 《Making Maps Available for Play: Analyzing the Design of Game Cartography Interfaces》(ACM TOCHI)에서 플레이어 지도 인터페이스의 마커 시스템을 4가지로 정형화하였습니다:
1. **단일 웨이포인트형 (Single Waypoint):** 나침반 또는 HUD 상에 단 하나의 목표 지점만을 강조.
2. **다중 핀형 (Multi-Pin):** 색상이나 심볼 아이콘으로 여러 지점을 구분 표기.
3. **드로잉형 (Drawing):** 맵 위에 선이나 도형, 자유 메모를 직접 기입.
4. **협업 핑형 (Collaborative Ping):** 멀티플레이 환경에서 팀원 간 위치 정보를 실시간 공유.

### 3.3. 마커 텍스트 입력 및 플랫폼 인터페이스 제약
*Marker Text Input & Platform Interface Constraints*

Kyzrati(《Cogmind》 개발자, 2021)는 'Map Comments and Log Notes' 연구를 통해 자유 텍스트 맵 코멘트 시스템의 구현 과정과 한계를 밝혔습니다:
* **역할:** 플레이어의 공간적 작업 기억(Working Memory)을 보조하는 강력한 외부 저장소 기능 수행.
* **위험 요소:** 마커 작성 요구가 과도해질 경우, 게임플레이가 메모 관리 및 정리 작업으로 변질되어 최적화 압박에 따른 인지 피로도(Tedium)가 급격히 증가함.

#### 플랫폼별 텍스트 입력 인터페이스 비교
* **PC (키보드):** 물리 키보드를 통한 자유 텍스트 입력이 즉각적입니다 (예: *Skyrim*의 "Multiple Custom Markers with Notes" 모드 등).
* **콘솔 (컨트롤러):** 가상 화상 키보드(Hunt-and-peck), 자이로 틸트, 방사형/계층형 인터페이스 모두 입력 속도가 현저히 느립니다 (Charlie Deck 2017 분석 기준, 듀얼스틱 기반 가상 키보드도 입력 속도 개선율이 약 10%에 불과). 이 하드웨어 제약으로 인해 대다수 콘솔 기반 메트로이드배니아는 자유 텍스트 대신 사전 정의된 아이콘 핀(Icon Pin) 시스템을 채택하는 설계 우선주의를 따릅니다.
* **핸드헬드 / 모바일:** 터치스크린 가상 키보드 및 전용 컨트롤러 입력을 병행 지원하는 구조를 취합니다.

## 4. 2차원 사이드뷰 공간과 지도의 위상 불일치 해결 기제
*Resolving Scale & Topology Mismatch in 2D Side-View Spaces*

### 4.1. 문제 공간 정의
*Problem Space Definition*

2차원 횡스크롤(Side-View) 액션 게임의 실제 레벨 공간과 2차원 평면 축척 지도 사이에는 기하학적·인지적 불일치가 발생합니다:

1. **공간 왜곡 (Spatial Distortion):** 사이드뷰 액션은 캐릭터의 점프 궤적, 대시 관성, 카메라 시야각(FOV) 확보를 위해 **수평 방향으로 길게 늘어지는 룸(Room)** 구조를 요구합니다. 반면 전체 월드 맵은 상하좌우 연결성과 거시적 파악(Overview)을 위해 **정방형 또는 균등 압축 격자**를 요구합니다.
2. **비유클리드적 위상 충돌 (Non-Euclidean Topology Conflict):** 좌우로 긴 방을 통과한 후 하층으로 내려가 반대 방향으로 이동할 때, 실제 룸의 픽셀 스케일과 맵의 타일 수가 정합되지 않으면 지도상에서 방과 방이 겹치거나(Overlap) 연결 통로의 좌표가 어긋나는 기하학적 오류가 발생합니다.
3. **인지적 부조화 (Cognitive Dissonance):** 화면상에서 장시간 이동했음에도 지도상 커서의 이동량이 미미하거나, 화면 전환 시 실제 이동 거리와 맵의 축척 비율이 일정하지 않을 때 플레이어가 공간 지각 혼란을 겪게 됩니다.

```
[2D 사이드뷰 공간과 맵 불일치 해결 패러다임]
 ├── 1. 타일 기반 엄격한 모듈화 (Grid-Locked Modular Design)
 │      └── Super Metroid, Castlevania SotN, Axiom Verge
 ├── 2. 벡터/콜리전 정밀 축소 투영 (True-to-Scale Vector Mapping)
 │      └── Metroid Dread, Prince of Persia: The Lost Crown
 ├── 3. 다이어제틱 약도화 (Abstract / Diegetic Cartography)
 │      └── Hollow Knight
 └── 4. 운동성 보존 심리스 뷰 (Kinematic Seamless Mapping)
        └── Ori and the Blind Forest, Ori and the Will of the Wisps
```

### 4.2. 개발자들의 4대 해결 접근 방식
*Four Major Developer Approaches*

#### 타일 기반 엄격한 모듈화
*Grid-Locked Modular Design*

* **구현 방식:** 모든 레벨 룸의 규격을 단일 화면 단위($1 \times 1$ 블록, 예: $256 \times 224$ 픽셀) 또는 그 정수배($1 \times 2$, $3 \times 1$, $2 \times 2$ 등)로 강제 제한하고, 맵 1칸과 실제 게임 화면 1스크린을 $1:1$ 대응시킵니다.
* **대표 타이틀:** 《슈퍼 메트로이드(Super Metroid)》(1994), 《캐슬바니아: 밤의 야상곡(Castlevania: Symphony of the Night)》(1997), 《액시엄 버지(Axiom Verge)》(2015)
* **설계 의의:**
  * **탐색의 정량화 (Measurability):** 미지의 영역을 밝힐 때 맵 1칸이 명확한 맵 달성률(Completion Percentage)로 치환됩니다.
  * **논리적 추론 가능성:** 맵 그리드의 비어 있는 칸을 통해 숨겨진 통로나 비밀 방(Secret Room)의 물리적 존재 가능성을 플레이어가 연역적으로 추론할 수 있습니다.

#### 벡터 및 충돌체 정밀 축소 투영
*True-to-Scale Vector Mapping*

* **구현 방식:** 맵을 격자 타일로 단순화하지 않고, 게임 내 레벨의 2D/3D 충돌체 외곽선(Collision Geometry)을 $1:N$ 비율로 직접 축소하여 UI에 실시간 벡터 렌더링합니다.
* **대표 타이틀:** 《메트로이드 드레드(Metroid Dread)》(2021), 《페르시아의 왕자: 잃어버린 왕관(Prince of Persia: The Lost Crown)》(2024)
* **설계 의의:**
  * **마이크로 레벨 디테일 보존:** 사이드뷰 특유의 좁은 환기 덕트, 슬라이딩 통로, 일방통행 문, 파괴 가능한 블록의 위치와 형태가 지도에 정확히 보존됩니다.
  * **즉각적 상황 판별:** 플레이어가 맵만 보고도 진입 불가의 원인(문 유형, 점프 높이 부족 등)을 즉시 판별할 수 있습니다.

#### 다이어제틱 약도화
*Abstract & Diegetic Cartography*

* **구현 방식:** 물리 엔진 상의 픽셀 단위 정합성을 배제하고, 지도를 인게임 캐릭터(코니퍼)가 손으로 스케치한 '약도(Topological Sketch)' 형태로 제공합니다. 주요 벤치, 상점, 트램 등 랜드마크 중심의 상대적 위상 관계만 표현하고 방 사이의 여백(Negative Space)을 의도적으로 방치합니다.
* **대표 타이틀:** 《할로우 나이트(Hollow Knight)》(2017)
* **설계 의의:**
  * **공간의 신비감 및 몰입 유지:** 맵 UI의 수치에 의존하지 않고, 플레이어가 게임 내 배경 아트, 시각적 랜드마크, 환경 음향에 집중하여 길을 찾도록 유도합니다.

#### 운동성 보존 심리스 뷰
*Kinematic Seamless Mapping*

* **구현 방식:** 격자 분할 없는 거대한 단일 씬(Seamless World)을 구성하고, 맵을 열었을 때 플레이어의 현재 위치를 중심으로 부드러운 줌아웃/줌인 렌더링을 적용합니다.
* **대표 타이틀:** 《오리와 눈먼 숲(Ori and the Blind Forest)》(2015), 《오리와 도깨비불(Ori and the Will of the Wisps)》(2020)
* **설계 의의:**
  * **운동 흐름의 연속성:** 사이드뷰 특유의 고속 관성 이동(대시, 바시, 활강) 흐름을 끊지 않으면서 전체 세계를 유기적인 하나의 거대 생태계로 인지시킵니다.

## 5. 비판타지 환경에서의 던전 대체 및 공간 게이팅
*Non-Fantasy Dungeon Substitution & Spatial Gating*

메트로이드배니아의 구조적 본질은 중세 판타지 양식의 석조 지하 감옥이 아니라, 능력 및 지식 획득 기반의 잠금-해제와 비선형적 공간 루프라는 그래프 위상 구조(Graph Topology)에 있습니다.

### 5.1. 공간 유형별 던전 대체 및 게이팅 기제
*Dungeon Substitution & Gating Mechanisms by Space Type*

| 대체 공간 유형 | 구현 및 배경 설정 | 게이팅 메커니즘 (진입 장벽 및 해제 도구) | 대표 적용 사례 |
| :--- | :--- | :--- | :--- |
| **자연 생태계 및 외계 환경** | 가혹한 기후, 독성 식생, 심해, 용암 지대 등 자연물로 구성된 유기적 지형 | **환경 저항력 및 생존 장비:**<br>- 고온 구역 $\rightarrow$ 방열복(Varia Suit)<br>- 심해 수압/저항 $\rightarrow$ 중력복(Gravity Suit)<br>- 유독성 늪지 $\rightarrow$ 수질 정화 기믹 또는 공중 활강 스킬 | 《메트로이드 시리즈(Metroid Series)》(1986~), 《오리 시리즈(Ori Series)》(2015/2020) |
| **기능성 인공 구조물** | 본래 실용적 목적(연구, 군사, 생산)이 있었으나 사고로 봉쇄된 시설 | **보안 및 산업 인프라 제어:**<br>- 잠긴 방화벽 $\rightarrow$ 보안 인가 카드(Keycard)<br>- 작동 중단 구역 $\rightarrow$ 발전기 재가동 및 전력망 복구<br>- 붕괴된 통로 $\rightarrow$ 산업용 폭약(C4), 배관 덕트 해킹 | 《섀도우 컴플렉스(Shadow Complex)》(2009), 《더 미이라 디마스터드(The Mummy Demastered)》(2017), 《고스트 송(Ghost Song)》(2022), 《하이쿠 더 로봇(Haiku, the Robot)》(2022) |
| **문화적·신화적 공간** | 서구 판타지를 탈피한 비서구권 토착 신화 및 종교관 기반 공간 | **영적 상태 전환 및 전통 무예:**<br>- 도교 사당/연금술 시설 $\rightarrow$ 부적(Talisman), 기(Chi) 조작<br>- 저승/이승 차원 분리 $\rightarrow$ 차원 전환 기믹, 루차 리브레 기술 | 《나인 솔즈(Nine Sols)》(2024), 《과카밀레!(Guacamelee!)》(2013) |
| **개념적·인지적 도메인** | 물리적 건축물이 아닌 텍스트, 규칙, 생체 네트워크 자체를 탐색 공간화 | **플레이어의 지식 축적 및 정보 해독:**<br>- 숨겨진 커맨드 발견 $\rightarrow$ 미지의 조작법 입력<br>- 암호 체계 해독 $\rightarrow$ 환경 내 상호작용 규칙 갱신 | 《튜닉(Tunic)》(2022), 《애니멀 웰(Animal Well)》(2024), 《액시엄 버지 2(Axiom Verge 2)》(2021) |

## 6. 용어 정리 및 정의
*Glossary & Definitions*

| 용어 | 정의 |
| :--- | :--- |
| **게이팅** | **Gating**. 게임 디자인 및 레벨 설계에서 플레이어의 공간 이동이나 콘텐츠 접근을 특정 조건 달성 시점까지 구조적으로 통제·차단하는 메커니즘. |
| **능력 게이팅** | **Ability Gating**. 캐릭터 자체의 물리적·운동학적 이동 스킬(이단 점프, 공중 대시, 벽 타기, 모프볼 변신 등)을 **'능력 획득'**함으로써 조작 레퍼토리가 영구 확장되어 공간의 물리적 장벽을 돌파하는 메트로이드배니아의 표준 구조. |
| **아이템 게이팅** | **Item Gating**. 캐릭터의 기본 조작 메커니즘을 변경하지 않고, 인벤토리에 특정 열쇠, 보안 인가 카드(Keycard), 퀘스트 도구, 방호 장비 등을 **'아이템 획득'**하여 소지 여부 조건 판정(Key-Lock Check)을 통해 잠긴 문이나 특정 구역을 통과하는 구조. |
| **지식 게이팅** | **Knowledge Gating**. 캐릭터의 물리적 스펙 상승 없이, 플레이어가 세계관의 규칙, 조작 커맨드, 언어 암호를 학습하여 돌파하는 구조 (메트로이드브레이니아의 핵심). |
| **깃팅 및 깃 구드** | **Git Gud / Gitting**. "Get good(실력을 길러라)"을 왜곡한 인터넷 밈에서 유래한 용어로, 캐릭터의 스탯 상승이나 장비에 의존하지 않고 플레이어 자신의 순수한 조작 정밀도, 반사 신경, 보스 패턴 숙달만으로 장애물을 돌파하는 플레이 행위 및 설계 양식. |
| **메트로이드브레이니아** | **Metroidbrainia**. Metroidvania와 Brain의 합성어. 메트로이드배니아 특유의 비선형적 맵 탐색과 잠금-해제 구조를 차용하되, 캐릭터의 물리적 능력 확장 대신 플레이어 자신의 인지적 지식 축적을 유일한 진행 도구로 사용하는 서브장르. Ending-From-Beginning 구조, 1회성 탐험 경험, 외부 기억 매체 의존성이 핵심 특징임. |
| **지도학** | **Cartography**. 게임 내 공간 정보를 평면, 벡터, 다이어제틱 소품 등으로 시각화하여 플레이어의 인지 및 길찾기를 보조하는 인터페이스 설계 분야. |

## 7. 참고 자료 및 원천 데이터 출처
*References & Raw Sources*

<div class="callout">
    <strong>📁 로컬 원천 데이터 보존 경로:</strong><br>
    본 위키 문서는 로컬 원천 텍스트 저장소 <code><a href="raw/20260824_metroidvania_and_cartography_game_design_raw.txt">raw/20260824_metroidvania_and_cartography_game_design_raw.txt</a></code>의 데이터와 교차 검증을 거쳐 작성되었습니다.
</div>

<ol class="reference-list">
    <li id="ref-1">[1] Maleki, M. (2025). <em>Metroidbrainia: A Genre Analysis of Knowledge-Based Exploration Games</em>. <a href="https://scholar.google.com" target="_blank">Google Scholar</a></li>
    <li id="ref-2">[2] Oliveira, M. et al. (2020). <em>A Framework for Metroidvania Games</em>. SBGames 2020. <a href="https://sbgames.org" target="_blank">SBGames Official Repository</a></li>
    <li id="ref-3">[3] Rodríguez, A., Cotta, C., & Leiva, A. J. (2018). <em>An Evolutionary Approach to Metroidvania Videogame Design</em>. IEEE Congress on Evolutionary Computation. <a href="https://doi.org" target="_blank">IEEE Xplore</a></li>
    <li id="ref-4">[4] Dormann, C., Pötscher, G., & Wallner, G. (2023). <em>A Classification of Video Game Cartographic Maps</em>. DiGRA 2023. <a href="http://www.digra.org/digital-library/" target="_blank">DiGRA Digital Library</a></li>
    <li id="ref-5">[5] Toups, P. D. et al. (2019). <em>Making Maps Available for Play: Analyzing the Design of Game Cartography Interfaces</em>. ACM Transactions on Computer-Human Interaction (TOCHI). <a href="https://dl.acm.org/journal/tochi" target="_blank">ACM Digital Library</a></li>
    <li id="ref-6">[6] Kyzrati (2021). <em>Map Comments and Log Notes</em>. Grid Sage Games DevBlog. <a href="https://www.gridsagegames.com/blog/" target="_blank">Grid Sage Games DevBlog</a></li>
    <li id="ref-7">[7] Apperley, T. H. (2006). <em>Genre and game studies: Toward a critical approach to video game genres</em>. Simulation & Gaming, 37(1), 6-23.</li>
    <li id="ref-8">[8] Arsenault, D. (2009). <em>Video game genre, evolution and innovation</em>. Eludamos. Journal for Computer Game Culture, 3(2), 149-176.</li>
</ol>
