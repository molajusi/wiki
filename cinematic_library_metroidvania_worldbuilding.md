---
title: "영상 연출 라이브러리 메트로이드배니아의 세계관과 정치 체제"
subtitle: "Worldbuilding and the Political-System Duality of the Cinematic-Library Metroidvania"
created: "2026-09-30 오후 05:10:40 (KST, UTC+9)"
updated: "2026-09-30 오후 05:10:40 (KST, UTC+9)"
category: "게임 디자인 및 분석 (Game Design & Taxonomy)"
tags: ["Goryeo Fantasy", "Metroidvania", "Worldbuilding", "Class System", "Political System", "Hojang", "Munbeol"]
html_view: "cinematic_library_metroidvania_worldbuilding.html"
---

# 영상 연출 라이브러리 메트로이드배니아의 세계관과 정치 체제
*Worldbuilding and the Political-System Duality of the Cinematic-Library Metroidvania*

**카테고리**: 게임 디자인 및 분석 (Game Design & Taxonomy)  
*최초 작성일시: 2026-09-30 오후 05:10:40 (KST, UTC+9) | 최종 수정일시: 2026-09-30 오후 05:10:40 (KST, UTC+9)*

<context>
본 문서는 [영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획](cinematic_library_metroidvania_game_design.html)의 3장 "세계관 및 정치 체제 설계"를 분리 이전한 문서입니다. 아저씨의 질문("세계관은 게임 기술적 구성 — 아키텍처나 기반기술, 스크립팅에서 영향이 분리되는가?")에 대해, 원 문서의 2장(아키텍처)·4장(감정표현)·5장(엔진)·6장(아트스타일)·7장(레벨·시퀀스 디자인)이 이 세계관의 구체적 내용(고려풍 판타지, 6단 신분 계층, 정치 체제)에 기술적으로 의존하지 않는다는 점을 확인했고, 이에 따라 세계관 콘텐츠를 별도 문서로 분리했습니다. 원 문서는 3장 자리에 요약과 이 문서로의 링크만 남깁니다. 원문은 `raw/20260923_cinematic_library_metroidvania_game_design_raw.txt`(기획 브리핑 전체)를 원천으로 하며, 이 위키의 고려풍 판타지 세계관 문서 및 고려 호족·향리 고증 문서와 교차 참조합니다.
</context>

**관련 문서**: [영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획](cinematic_library_metroidvania_game_design.html)(이 세계관이 원래 속해 있던 기술 기획 문서, 3장에서 분리됨) · [고려 중세풍 수평적 판타지 세계관과 아동 서사 모델](goryeo_horizontal_fantasy_worldbuilding.html)(설계 철학이 상반되는 자매 세계관) · [고려 호족·향리와 지방세력가 호칭 고증](goryeo_hojok_hyangni_terminology.html)(지방세력가 계층의 역사적 원형 상세 근거) · [아동 서사의 정치철학과 권력 구조 비판](children_narrative_politics_and_power_structures.html)(신분제 서사 선택의 배경 이론)

<overview>
## 1. 개요 및 목적
*Overview & Purpose*

이 문서는 [영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획](cinematic_library_metroidvania_game_design.html)의 세계관·정치 체제 설계를 다룹니다. 핵심은 정치 체제를 **게임 레이어(공화체제로 고정)와 연출 레이어(체제에 구애받지 않는 자유 소재)로 분리**하는 설계이며, 그 위에 연출 레이어가 다루는 소재 예시로서 고려풍 6단 신분 계층을 정의합니다.

<div class="callout">
<p><strong>분리 이전 배경</strong>: 원래 이 세계관은 게임 기획 문서의 3장이었습니다. 아저씨가 "세계관은 게임 기술적 구성(아키텍처·기반기술·스크립팅)에서 영향이 분리되는가?"라고 물었고, 검토 결과 2장(이중 목적 아키텍처)·4장(감정표현 및 대사풍선 시스템)·5장(Godot 엔진 채택)·6장(아트스타일과 렌더링 파이프라인)·7장(레벨·시퀀스 디자인)은 모두 장르·설정에 무관한 범용 기술 설계이며, 이 세계관의 구체적 내용(고려풍 신분 계층 명칭, 정치 체제 등)에 대한 기술적 의존이 없다는 점이 확인되었습니다. 유일한 결합은 1장·2장에서 정의한 "연출 레이어 vs 게임 레이어"라는 개념적 어휘를 이 세계관도 함께 쓴다는 점뿐이며, 이는 구현 의존이 아니라 공유 용어 수준입니다. 이에 따라 세계관 콘텐츠를 이 별도 문서로 분리했습니다.</p>
</div>
</overview>

<world>
## 2. 시대 분위기와 이 위키의 기존 고려풍 세계관과의 관계
*Setting and Relationship to This Wiki's Existing Goryeo-Style Worldbuilding*

세계관은 마법(주술·도술)과 냉병기(칼·창·활)가 공존하는 중세 고려시대풍 가상 판타지입니다. 실제 고려사를 배경으로 삼지 않고 질감만 차용하는 방식은, 이 위키에 이미 존재하는 `goryeo_horizontal_fantasy_worldbuilding.html`의 2.1절 "고전풍 공화주의와 미학·체제의 분리" 원칙과 방법론적으로 동일합니다. 다만 이 기획은 정치 체제를 **게임 레이어(공화체제로 고정)와 연출 레이어(체제에 구애받지 않는 자유 소재)로 분리**해 다룹니다.

<div class="callout">
<p><strong>연출 레이어는 정치 체제에 고정되지 않는 범용 무대</strong>: 연출 레이어(쇼츠/지식영상)는 신분제 하나에 묶이지 않습니다. 다룰 수 있는 소재는 최소 세 갈래입니다 — ① <b>현실 역사</b>(신분제 사회를 포함한 임의의 시대), ② <b>게임이 실제로 채택한 공화체제 세계 그 자체</b>, ③ <b>그 공화체제 세계 안팎에 존재할 수 있는 왕정적 소재</b>(예: 공화정 수립 이전의 역사, 국경 너머 이웃 왕국, 몰락한 옛 왕조 등). 게임의 정식 세계관이 공화체제라 해도, 연출 레이어는 그 세계의 과거나 주변국으로 왕정을 얼마든지 무대에 올릴 수 있습니다.</p>
<p>이렇게 설계하는 이유는 연출 라이브러리/API가 특정 한 편의 영상 전용 도구가 아니라, 임의의 시대·체제·인물 구성을 기록·재생할 수 있는 범용 세트 라이브러리(원 문서 2장 아키텍처)이기 때문입니다. 3장의 6단 신분 계층 구조는 그 다양한 소재 중 <b>신분제를 다룰 때 쓰는 데이터셋 하나</b>일 뿐이며, 연출 레이어가 항상 따라야 하는 고정 설정은 아닙니다.</p>
<p>반면 <b>플레이어블 게임 본편</b>이 실제로 진행되는 정식 세계·정치 체제는 여전히 <b>공화체제 하나로 고정</b>합니다. 게임 시스템(세력 관계, 진행 동기, 능력 게이팅의 서사적 근거)이 여러 체제를 동시에 지원하도록 설계하면 범위가 지나치게 커지므로, 게임 자체의 정치 체제는 단일하게 유지하는 편이 합리적입니다. 이 점에서 게임 레이어는 <code>goryeo_horizontal_fantasy_worldbuilding.html</code>의 "혈통 군주정 거부" 노선과 방향은 같아지지만, 그 문서와 세계관을 공유하는 것은 아니며 이 프로젝트만의 별도 공화체제입니다.</p>
<p>정리하면: <b>게임 레이어는 공화체제로 고정, 연출 레이어는 체제 무관하게 자유</b>입니다. 연출 레이어가 다루는 왕정 소재(신분제 사회 등)가 게임 세계의 과거사로 시간적으로 연결되는지, 완전히 별개의 역사·세계선으로 다뤄지는지는 아직 미확정이며 다음 단계에서 결정이 필요한 항목입니다.</p>
</div>

## 3. 6단 신분 계층 구성(연출 레이어가 다루는 신분제 소재 데이터셋 예시, 1차 정의, 세부 미확정)
*Six-Tier Class Hierarchy*

| 계층 | 호칭 | 비고(에이전트 해석, 확정 아님) |
| :--- | :--- | :--- |
| 왕 | **왕(王)** | 국가 최고 권위. 등장 빈도·직접 조작 가능 여부 미정. |
| 중앙관료 | **문벌(門閥)** | 고려 전기 중앙 정계를 장악한 가문·관료 집단. 흔히 "문벌귀족"이라 불리나, 고려가 실제로 "귀족사회"였는지(음서 근거) "관료사회"였는지(과거 근거)는 학계 논쟁이 있고, 세습 작위(봉작) 자체도 없었다는 학설이 있어 "귀족"이라는 표현을 빼고 "문벌"만 쓰는 쪽을 채택(2015 개정 교과서 표기와 일치). **대중적으로는 "양반(兩班)"으로도 흔히 불리나**, 양반은 원래 조회 시 국왕을 기준으로 동편에 선 문반(文班)과 서편에 선 무반(武班)을 합친 관제 용어로 고려 성종대 등장했고, 이 시기엔 세습 신분 개념이 아니라 재직자 지칭이었음(세습 신분화는 후대 조선의 현상). 세계관 정식 호칭은 "문벌", "양반"은 구어적 별칭으로 병용 가능. 지방세력가와의 긴장 관계 설정 여지. |
| 지방세력가 | **호장(戶長)** | 성종 2년(983) 12목 설치·외관 파견과 함께 종전 신라식 호칭(당대등)을 개칭해 제도화된 향리의 우두머리. 세습적이나 법제적으로는 귀족이 아님 — 부와 문화자본(자제의 과거 응시 자격 등)은 있으나 공식 특권은 없는 애매한 위치. 역사적 근거는 아래 3.1절 참조. 갈등의 주요 발화점으로 활용 가능. |
| 지방관료 | **외관(外官)** — 목사(牧使) 등 | 중앙 조정에서 지방에 파견한 관료의 총칭. 고려 8목·12목에는 정3품 목사가 파견됨(이 위키의 한국 도시 행정단위 계보 문서 참조). 중앙-지방 권력 구조의 실무 접점이며, 호장(향리)과 구조적으로 긴장 관계. |
| 양인 | **양인(良人)** | 평민. 지식영상 속 등장인물 출신으로 활용. |
| 천민 | **천민(賤民)** | 최하층. 지식영상 속 신분 갈등·저항 서사의 자연스러운 소재. |

"호칭" 열은 원 브리핑이 이미 그 단어를 쓴 왕·양인·천민을 제외하면 모두 에이전트가 역사 조사로 덧붙인 해석입니다(중앙관료→양반, 지방관료→외관/목사는 이번에 보강, 지방세력가→호장은 아저씨가 직접 지정). 실제 설정 확정 전 별도 검토가 필요합니다. 특히 "지방세력가"는 원문에서 유일하게 상세 정의가 주어진 계층이라, 이 기획에서 서사적 비중이 가장 클 가능성이 있습니다(문화·예술 혜택이라는 설정 자체가 "화려한 무대/의상/대사"를 요구하므로 원 문서 4장 감정표현·연출 시스템과 직결).

### 3.1 지방세력가의 역사적 원형(요약)

"지방세력가"는 고려 호족(豪族) — 정확히는 그 후예 중 개경 진출에 실패하고 지방에 남아 세습적 지배층이 된 계열(제도명 **호장 戶長**/향리 鄕吏) — 에 대응합니다. 이들은 귀족은 아니되 사유지·지방민의 존숭·과거 응시 자격 등 실질적 특권을 누렸고, 성종 2년(983) 이후 중앙에서 파견된 목사(牧使) 등 외관과 구조적으로 긴장 관계에 있었습니다. 다만 "호족"이라는 단어 자체는 1차 사료(삼국사기·고려사)에 없는 현대 학계의 소급 조어이며, 사료상의 실제 용어는 시기에 따라 성주(城主)·장군(將軍, 건국 전후) 또는 호장·향리(제도화 이후)로 갈립니다. 유럽식 "영주"와의 동일시도 학계에서는 신중히 다뤄집니다.

상세 근거·용어 논쟁·시기별 호칭 비교표는 별도 문서 [고려 호족·향리와 지방세력가 호칭 고증](goryeo_hojok_hyangni_terminology.html)으로 분리되어 있습니다.

## 4. 마법 체계 재사용 검토
*Reviewing Magic System Reuse*

`goryeo_horizontal_fantasy_worldbuilding.html` 5장에는 이미 "통합 도술 체계"(공학·염원·대가 3대 원동력, 목화토금수 오행 4대 원소 변환술)가 설계되어 있습니다. 신분 구조는 다르지만 마법 체계 자체는 세계관 공유 자산으로 재사용하거나 변형해 쓰는 편이 처음부터 새로 설계하는 것보다 효율적입니다. 이 기획에서 별도 마법 체계를 새로 만들 필요가 있는지, 위 체계를 차용할지는 아직 결정되지 않았습니다.
</world>

<open_issues>
## 5. 미확정 설계 항목(오픈 이슈)
*Open Design Decisions*

다음 항목은 이번 논의에서 언급되지 않았으며, 근거 없이 임의로 확정하지 않고 목록으로만 남깁니다.

- **연출 레이어 왕정 소재의 시간적 연결 여부**: 연출 레이어가 다루는 왕정 소재(신분제 사회 등)가 게임 세계의 과거사로 시간적으로 연결되는지, 완전히 별개의 역사·세계선으로 다뤄지는지 미확정.
- **플레이어 캐릭터 구성과의 연계**: 원 기획 문서(게임 본편)에서 단일 캐릭터인지 신분별 복수 캐릭터인지가 미정이며, 이 문서 3장의 계층 구조를 살리려면 신분별 복수 캐릭터가 유리함.
- **마법 체계 차용 여부**: `goryeo_horizontal_fantasy_worldbuilding.html`의 통합 도술 체계를 그대로 차용할지, 변형할지, 별도로 새로 설계할지 미결정.
</open_issues>

<definitions>
## 6. 용어 정리 및 정의
*Terminology & Definitions*

| 용어 | 정의 |
| :--- | :--- |
| **지방세력가** | 귀족은 아니나 양인보다 문화·예술적 혜택을 누리는 호화 가문. 세계관 내 호칭은 **호장(戶長)**. 역사적 원형은 별도 문서 [고려 호족·향리와 지방세력가 호칭 고증](goryeo_hojok_hyangni_terminology.html) 참조. |
| **문벌** | **Munbeol**(門閥). 세계관 내 중앙관료의 정식 호칭. 고려 전기 중앙 정계를 장악한 가문·관료 집단. "귀족" 표현은 학계 귀족제/관료제 논쟁과 세습 작위 부재 학설을 반영해 배제(2015 개정 교과서 표기와 일치). 대중적 별칭은 양반(兩班, 원래 문반·무반을 합친 관제 용어). |
| **외관** | **Oegwan**(外官). 세계관 내 지방관료의 호칭. 중앙 조정이 지방에 파견한 관료의 총칭이며, 대표 직위는 목사(牧使, 8목·12목 정3품). |
| **연출 레이어 / 게임 레이어** | **Cinematic Layer / Game Layer**. [영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획](cinematic_library_metroidvania_game_design.html) 2장에서 정의된 이중 목적 아키텍처의 두 축. 이 문서에서는 정치 체제 설계를 이 두 축으로 분리하는 데 그 어휘를 그대로 차용함(구현 의존이 아닌 개념 공유). |
</definitions>

<references>
## 7. 참고 자료 및 원천 데이터 출처
*References & Raw Sources*

<div class="callout">
<p><strong>📁 로컬 원천 데이터 보존 경로:</strong> 본 문서는 원래 <a href="cinematic_library_metroidvania_game_design.html">영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획</a> 문서의 3장이었으며, 2026-09-30에 별도 문서로 분리되었습니다. 원 기획 브리핑 원문은 <code><a href="raw/20260923_cinematic_library_metroidvania_game_design_raw.txt">raw/20260923_cinematic_library_metroidvania_game_design_raw.txt</a></code>에 보존되어 있고, 지방세력가의 역사적 근거(고려 호족·향리 웹 조사)는 별도 문서 <a href="goryeo_hojok_hyangni_terminology.html">고려 호족·향리와 지방세력가 호칭 고증</a>과 그 자신의 원천데이터(<code>raw/20260923_goryeo_hojok_local_power_research_raw.txt</code>)를 참조합니다. 분할 전 원본 전문은 <code><a href="raw/20260930_cinematic_library_metroidvania_game_design_pre_split_backup.md">raw/20260930_cinematic_library_metroidvania_game_design_pre_split_backup.md</a></code>에 동결 보존되어 있습니다.</p>
</div>

<ol class="reference-list">
    <li id="ref-1">[1] 이 위키. 〈영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획〉. <a href="cinematic_library_metroidvania_game_design.html">cinematic_library_metroidvania_game_design.html</a> — 이 세계관이 분리되어 나온 원 기술 기획 문서.</li>
    <li id="ref-2">[2] 이 위키. 〈고려 중세풍 수평적 판타지 세계관과 아동 서사 모델〉. <a href="goryeo_horizontal_fantasy_worldbuilding.html">goryeo_horizontal_fantasy_worldbuilding.html</a> — 미학·체제 분리 방법론 및 통합 도술 체계 재사용 후보.</li>
    <li id="ref-3">[3] 이 위키. 〈아동 서사의 정치철학과 권력 구조 비판〉. <a href="children_narrative_politics_and_power_structures.html">children_narrative_politics_and_power_structures.html</a> — 신분제 서사 채택의 배경 대조 이론.</li>
    <li id="ref-4">[4] 이 위키. 〈고려 호족·향리와 지방세력가 호칭 고증〉. <a href="goryeo_hojok_hyangni_terminology.html">goryeo_hojok_hyangni_terminology.html</a> — 3.1절 지방세력가 역사적 원형의 상세 근거(호족 용어 적절성 논쟁, 시기별 호칭 비교, 목사와의 갈등 구도).</li>
    <li id="ref-5">[5] 위키백과. 〈양반〉 항목. <a href="https://ko.wikipedia.org/wiki/%EC%96%91%EB%B0%98" target="_blank">양반</a> — 3장 중앙관료 별칭(양반=문반·무반)의 근거.</li>
    <li id="ref-6">[6] 이 위키. 〈한국 도시 행정단위의 역사적 계보와 계층 체계〉. <a href="korean_urban_administrative_hierarchy_evolution.html">korean_urban_administrative_hierarchy_evolution.html</a> — 3장 지방관료 호칭(외관·목사)의 근거.</li>
    <li id="ref-7">[7] 우리역사넷(국사편찬위원회). 〈귀족·귀족제의 개념〉·〈귀족제사회설의 논거〉·〈관료제 및 가산관료제설과 그에 대한 비판〉. <a href="https://contents.history.go.kr/mobile/nh/view.do?levelId=nh_012_0020_0040_0020" target="_blank">https://contents.history.go.kr/mobile/nh/view.do?levelId=nh_012_0020_0040_0020</a> — 3장 "문벌" 채택 근거(귀족제/관료제 논쟁).</li>
    <li id="ref-8">[8] 나무위키. 〈문벌귀족〉 항목. <a href="https://namu.wiki/w/%EB%AC%B8%EB%B2%8C%EA%B7%80%EC%A1%B1" target="_blank">문벌귀족</a> — 2015 개정 교과서의 "문벌" 단독 표기 전환 서술의 근거.</li>
</ol>
</references>
