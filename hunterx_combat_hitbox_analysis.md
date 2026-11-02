---
title: "HunterX 전투 판정 구조와 밀착 공격 무효화 버그 분석"
subtitle: "HunterX: Combat Hit-Detection Architecture and the Point-Blank Attack-Miss Bug"
created: "2026-11-02 오후 08:08:04 (KST, UTC+9)"
updated: "2026-11-02 오후 08:39:19 (KST, UTC+9)"
category: "게임 디자인 및 분석 (Game Design & Taxonomy)"
tags: ["HunterX", "Orange Popcorn", "Metroidvania", "Souls-like", "Hitbox", "Collision Detection", "Combat Design", "Game Critique"]
html_view: "hunterx_combat_hitbox_analysis.html"
parent_hub: "metroidvania_genre_analysis.html"
---

# HunterX 전투 판정 구조와 밀착 공격 무효화 버그 분석
*HunterX: Combat Hit-Detection Architecture and the Point-Blank Attack-Miss Bug*

**카테고리**: 게임 디자인 및 분석 (Game Design & Taxonomy)  
*최초 작성일시: 2026-11-02 오후 08:08:04 (KST, UTC+9) | 최종 수정일시: 2026-11-02 오후 08:39:19 (KST, UTC+9)*

<context>
본 문서는 한국 인디 스튜디오 오렌지팝콘(Orange Popcorn)의 2D 메트로이드배니아·소울라이크 《HunterX》(2022)에서 아저씨가 직접 플레이 중 제보한 "적과 바짝 붙으면 공격이 무효화되고 서로 밀리기만 하는" 버그 증상을 분석합니다. 웹 조사 결과 이 게임·스튜디오를 특정하는 데는 성공했으나, 이 구체적 버그를 다룬 1차 자료(공식 패치노트·개발자 확인·버그 트래커)는 확보하지 못했습니다(원문: `raw/20261102_hunterx_combat_hitbox_analysis_raw.txt`). 본 문서의 원인 분석은 동일 장르(2D 액션·소울라이크)에서 일반적으로 보고되는 히트박스/콜라이더 설계 결함 패턴에 기반한 추정이며, 그 설계 원칙은 자매 문서 [영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획](cinematic_library_metroidvania_game_design.html) 7.1.2절에도 예방 지침으로 반영되었습니다.
</context>

**관련 문서**: [메트로이드배니아 장르 개요 및 계보학](metroidvania_genre_analysis.html)(상위 허브) · [알와 시리즈 게임 디자인 및 비평적 분석](alwa_series_analysis.html)·[샨테 시리즈 게임 디자인 및 비평적 분석](shantae_series_analysis.html)(같은 "분과 비평" 계열 문서) · [영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획](cinematic_library_metroidvania_game_design.html)(이 분석에서 도출한 설계 원칙이 반영된 문서)

<overview>
## 1. 개요 및 목적
*Overview & Purpose*

《HunterX》는 오렌지팝콘이 개발해 2022년 4월 28일 스팀(Steam App ID 1918450)에 출시한 2D 메트로이드배니아·소울라이크·다크 판타지 게임으로, 이후 닌텐도 스위치로도 출시되었습니다. [[1]](#ref-1)[[2]](#ref-2) 평가는 혼재되어 있으며, 반응 좋은 지점(경쾌하고 스타일리시한 전투, 주인공 커스터마이징 자유도)과 비판 지점(장르 공통 요소의 단순 조합, 일부 프러스트레이션)이 함께 보고됩니다. [[1]](#ref-1)[[3]](#ref-3)

이 게임은 "HunterX" 명의의 또 다른 별개 타이틀인 **《HunterX: code name T》(2023, Steam App ID 2680330)**와 혼동하지 않아야 합니다 — 본 문서는 2022년 본편(App ID 1918450)만을 대상으로 합니다. [[1]](#ref-1)

본 문서는 아저씨가 제보한 "적과 밀착 시 공격이 먹히지 않고 비비적대는" 증상을 계기로, ① 이 게임·버그의 실제 자료 확보 가능 여부를 조사하고 ② 자료가 불충분할 경우 동일 장르의 일반적인 히트박스/콜라이더 설계 결함 패턴에 근거한 원인 추정을 제시하는 것을 목적으로 합니다.
</overview>

<theory>
## 2. 핵심 개념 및 원리 — 근접 공격 판정의 3대 구성 요소
*Core Concepts — Three Components of Melee Hit Detection*

2D 액션 게임의 근접 공격은 보통 다음 세 가지 독립적인 판정 레이어가 동시에 작동하는 구조로 구현됩니다. 이 레이어들이 서로 다른 타이밍·기준으로 계산되면서 상호 충돌하는 것이 본 문서가 다루는 버그 유형의 공통 근원입니다.

### 2.1 히트박스(공격 판정)와 허트박스(피격 판정)
**Hitbox**(공격자가 내는 피해 판정 영역)와 **Hurtbox**(피격자가 맞을 수 있는 영역)는 서로 다른 콜라이더로 구현되는 것이 일반적입니다. 둘이 겹치는 프레임에만 피격이 성립합니다.

### 2.2 바디 콜라이더(몸체 충돌)
캐릭터끼리 서로 통과하지 않도록 하는 별도의 물리 충돌체입니다. 많은 2D 액션 게임은 두 캐릭터의 바디 콜라이더가 겹치면 매 프레임 서로를 밀어내는 **분리력(separation force)**을 적용합니다.

### 2.3 방향(facing) 판정
캐릭터가 공격을 어느 방향으로 내보낼지 결정하는 로직으로, 흔히 "상대방이 내 오른쪽/왼쪽에 있는가"를 매 프레임 재계산하는 방식으로 구현됩니다.

<div class="callout">
<p><strong>신뢰도 안내</strong>: 2장의 세 구성 요소 설명은 HunterX의 실제 소스코드가 아니라 2D 액션 게임 개발 전반에서 널리 쓰이는 일반적인 구현 패턴입니다. HunterX가 정확히 이 구조를 따르는지는 확인하지 못했습니다.</p>
</div>
</theory>

<analysis>
## 3. 밀착 공격 무효화 버그의 원인 추정
*Root-Cause Hypotheses for the Point-Blank Attack-Miss Bug*

웹 조사(원문: `raw/20261102_hunterx_combat_hitbox_analysis_raw.txt`)로는 이 증상을 직접 다룬 1차 자료를 확보하지 못했습니다. 유일하게 근접한 간접 근거는 ConFreaks & Geeks 리뷰가 "일부 히트박스가 기묘(funky)하고 일부 적 밸런스가 이상하다"고 지적한 것인데, 사소한 문제로 취급되며 "밀착 시 무효화"라는 구체적 패턴을 서술하지는 않습니다. [[3]](#ref-3) 따라서 아래 표는 **확인된 사실이 아니라 2장의 세 레이어가 상호 경쟁할 때 흔히 나타나는 일반적 원인 패턴**입니다.

| 원인 | 메커니즘 | "비비적댐"으로 체감되는 이유 |
| :--- | :--- | :--- |
| **히트박스의 전방 고정 오프셋** | 공격 판정이 캐릭터 몸체가 아니라 "전방 N 거리"에 생성되어, 적이 그 N보다 더 가까이 들어오면 히트박스가 허트박스를 지나쳐 뒤쪽 빈 공간에 그려짐(판정에 도넛형 데드존 발생) | 공격은 매번 나가지만 판정 지점에 적이 없어 피격 처리가 안 됨 |
| **바디 콜라이더 분리력과 공격 판정의 경쟁** | 2.2절의 분리력이 공격의 활성 프레임 동안에도 계속 작동해 두 캐릭터가 서로 밀고 밀리며 진동(jitter) | 사용자가 묘사한 "비비적댄다"는 표현과 가장 직접적으로 일치 |
| **방향 판정의 매 프레임 재계산** | 거리가 0에 가까울 때 좌우 위치가 미세하게 엎치락뒤치락하며 공격 방향이 프레임마다 반전 | 공격은 나가지만 매번 반대쪽으로 나가 맞지 않음 |

### 3.1 HunterX 리뷰에서 확인되는 간접 정황

- Capsule Computers 리뷰는 전투가 빠르고 조작감이 좋다고 평가합니다. [[4]](#ref-4)
- 한 스팀 유저 리뷰는 전투를 "그럭저럭(generic)"하다고 평가합니다. [[3]](#ref-3)
- 또 다른 스팀 유저 리뷰는 보스가 "방에 들어가는 순간 이미 히트박스가 대기 중"이라고 언급합니다 — 보스 판정의 타이밍 문제를 시사하나, 본 문서가 다루는 일반 몹 근접전 버그와는 별개 사안입니다. [[3]](#ref-3)

이 세 평가는 서로 다른 방향(빠름/그럭저럭/보스 판정 이슈)을 가리켜 일관된 결론을 주지 않으며, 사용자 제보 증상을 직접 뒷받침하거나 반박하지 않습니다.

### 3.2 다른 게임의 확인된 선례

HunterX 자체의 1차 자료는 못 찾았으나, 같은 유형(근접 거리에서 공격이 빗나가는 버그)이 다른 게임에서 공식적으로 확인·수정된 사례를 추가 조사했습니다(원문: `raw/20261102_similar_hitbox_platform_bugs_other_games_raw.txt`). 이 선례들은 1절의 원인 추정이 HunterX만의 특이 현상이 아니라 장르 공통의 설계 함정이라는 정황을 뒷받침합니다.

| 게임 | 확인 수준 | 내용 |
| :--- | :--- | :--- |
| **《스트리트 파이터 V》(캡콤)** | 공식 패치노트(2020년 3월, Champion Edition CE202003) | 상대가 너무 가까우면 여러 기술이 빗나가는(whiff) 문제를 캡콤이 공식 인정, 해당 기술들의 히트박스를 안쪽·아래쪽으로 확장해 수정 [[5]](#ref-5) |
| **《Ginger's Wrath》(인디)** | 패치노트(버전 0.2) | "Hitbox has been fixed"(플레이어), "Increased attack hitbox for enemy AI"(적) — 히트박스 확대로 근접 판정 문제를 수정 [[6]](#ref-6) |
| **개발 블로그 사례(ehe.gamedev.net, 2018)** | 개발자 1차 서술 | "플레이어의 근접 타격 시스템에, 적이 너무 가까워지면 맞출 수 없게 되는 버그가 있었다"고 직접 서술하며 수정 [[7]](#ref-7) |
| **《Fallout》 커뮤니티(베데스다)** | 유저 제보 단계(devtracker) | "근접 빌드가 피해를 보는 근접 판정 버그를 인지하고 있는지" 묻는 커뮤니티 글 — 개발사의 공식 수정 확인까지는 이르지 못함 [[7]](#ref-7) |

이 중 스트리트 파이터 V 사례는 공식 패치노트로 재구성 가능한 수준의 확인된 1차 사례이며, "히트박스가 몸체보다 좁거나 전방에 치우쳐 근접 거리에서 허트박스를 벗어난다"는 원인(1절의 "판정 데드존")과 "히트박스를 안쪽으로 확장한다"는 수정 방향이 1절의 예방 원칙 1번과 구조적으로 일치합니다.

### 3.3 예방적 설계 원칙(일반화)

위 원인 추정에서 도출되는 예방 원칙은 다음과 같습니다 — 이는 HunterX를 고치는 방법이 아니라, 같은 버그 유형을 **신규 설계 단계에서 피하는 방법**입니다.

1. 공격 판정을 "전방 고정 거리"가 아니라 캐릭터 몸체를 감싸는 원형·캡슐형으로 설계해 근접 데드존을 없앤다.
2. 공격의 활성 프레임 동안 바디 콜라이더의 분리력을 일시적으로 약화하거나, 판정 계산을 분리력 계산과 다른 단계(pass)에서 수행해 두 로직이 같은 프레임에서 경쟁하지 않게 한다.
3. 공격 방향을 매 프레임 재계산하지 않고 공격 개시 시점에 고정(락)해, 밀착 거리에서의 위치 진동이 공격 방향을 흔들지 않게 한다.

이 세 원칙은 이 위키의 자매 프로젝트 문서인 [영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획](cinematic_library_metroidvania_game_design.html) 7.1.2절에 예방 지침으로 반영되어 있습니다.
</analysis>

<definitions>
## 4. 용어 정리 및 정의
*Glossary & Definitions*

| 용어 | 정의 |
| :--- | :--- |
| **HunterX** | 오렌지팝콘이 개발해 2022년 4월 28일 스팀에 출시한 2D 메트로이드배니아·소울라이크·다크 판타지 게임(Steam App ID 1918450). "HunterX: code name T"(2023, 별개 게임)와 혼동 주의. |
| **오렌지팝콘** | **Orange Popcorn**. HunterX를 개발한 한국 인디 게임 스튜디오. |
| **히트박스** | **Hitbox**. 공격자가 피해를 입히는 판정 영역을 정의하는 콜라이더. |
| **허트박스** | **Hurtbox**. 피격자가 피해를 입을 수 있는 영역을 정의하는 콜라이더. 히트박스와 겹쳐야 피격이 성립. |
| **바디 콜라이더** | **Body Collider**. 캐릭터끼리 서로 통과하지 않도록 하는 물리 충돌체. 히트박스/허트박스와는 별개의 판정 레이어. |
| **분리력** | **Separation Force**. 두 바디 콜라이더가 겹칠 때 매 프레임 서로를 밀어내는 힘. 공격 판정과 경쟁하면 캐릭터가 진동하는 버그를 일으킬 수 있음. |
| **판정 데드존** | 공격 히트박스가 전방 고정 오프셋에 생성되어, 그 오프셋보다 더 가까운 적에게는 판정이 닿지 않는 근접 사각지대. |
| **방향 락** | **Facing Lock**. 공격 방향을 매 프레임 재계산하지 않고 공격 개시 시점의 방향으로 고정하는 설계. |
</definitions>

<references>
## 5. 참고 자료 및 원천 데이터 출처
*References & Raw Sources*

<div class="callout">
    <strong>📁 로컬 원천 데이터 보존 경로:</strong><br>
    본 위키 문서는 로컬 원천 텍스트 저장소 <code><a href="raw/20261102_hunterx_combat_hitbox_analysis_raw.txt">raw/20261102_hunterx_combat_hitbox_analysis_raw.txt</a></code>와 <code><a href="raw/20261102_similar_hitbox_platform_bugs_other_games_raw.txt">raw/20261102_similar_hitbox_platform_bugs_other_games_raw.txt</a></code>(3.2절 타 게임 선례 조사)의 데이터와 교차 검증을 거쳐 작성되었습니다. HunterX 자체의 1차 자료(개발사 공식 확인·패치노트)는 확보하지 못했으며, 원인 분석은 추정임을 재차 명시합니다.
</div>

<ol class="reference-list">
    <li id="ref-1">[1] WebSearch 종합 결과(2026). <em>HunterX Steam game metroidvania — 게임 식별 조사</em>. 검색 결과 요약 기반, 원문 직접 대조 없음. <a href="https://steambase.io/games/hunterx/info" target="_blank">steambase.io/games/hunterx</a></li>
    <li id="ref-2">[2] Game Developer(2022). <em>HunterX Now Live on Nintendo Switch</em>(보도자료). <a href="https://www.gamedeveloper.com/press-release/hunterx-now-live-on-nintendo-switch" target="_blank">gamedeveloper.com</a></li>
    <li id="ref-3">[3] Steam 커뮤니티 유저 리뷰 및 ConFreaks & Geeks 리뷰(검색 스니펫 기반, 원문 미대조). <a href="https://www.confreaksandgeeks.com/hunterx-review/" target="_blank">confreaksandgeeks.com/hunterx-review</a></li>
    <li id="ref-4">[4] Capsule Computers(2022). <em>HunterX Review</em>. <a href="https://www.capsulecomputers.com.au/2022/05/hunterx-review/" target="_blank">capsulecomputers.com.au</a></li>
    <li id="ref-5">[5] EventHubs(2020). <em>What Exactly Does "Extended Hitbox Inward" Mean? — Street Fighter 5 Champion Edition's New Update</em>. <a href="https://www.eventhubs.com/news/2020/mar/25/what-exactly-does-extended-hitbox-inward-mean-street-fighter-5-champion-editions-new-update" target="_blank">eventhubs.com</a> — 3.2절 타 게임 선례(스트리트 파이터 V)의 근거.</li>
    <li id="ref-6">[6] Ginger's Wrath 개발자(itch.io). <em>Patch Notes 0.2</em>. <a href="https://daibreaker501.itch.io/gingers-wrath/devlog/581209/patch-notes-02" target="_blank">daibreaker501.itch.io</a> — 3.2절 인디 게임 선례의 근거.</li>
    <li id="ref-7">[7] WebSearch 종합 결과(2026). <em>melee attack fails when too close to enemy — 타 게임 선례 조사</em>. 검색 결과 요약 기반(gamedev.net 개발 블로그, Fallout 커뮤니티 devtracker 포함), 원문 직접 대조 없음. 원문: <code>raw/20261102_similar_hitbox_platform_bugs_other_games_raw.txt</code></li>
</ol>
</references>
