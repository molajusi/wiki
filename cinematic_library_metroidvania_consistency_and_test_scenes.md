---
title: "영상 연출 라이브러리 메트로이드배니아의 일관성 개념과 최소 테스트 씬 설계"
subtitle: "Defining Consistency Layers and a Minimal Three-Scene Test for the Cinematic-Library Metroidvania"
created: "2026-11-06 오후 02:57:19 (KST, UTC+9)"
updated: "2026-11-09 오후 07:30:56 (KST, UTC+9)"
category: "게임 디자인 및 분석 (Game Design & Taxonomy)"
tags: ["Metroidvania", "Cinematic Direction", "Consistency", "Single Source of Truth", "Data Schema", "Prototype", "Godot", "Ability Gating"]
html_view: "cinematic_library_metroidvania_consistency_and_test_scenes.html"
---

# 영상 연출 라이브러리 메트로이드배니아의 일관성 개념과 최소 테스트 씬 설계
*Defining Consistency Layers and a Minimal Three-Scene Test for the Cinematic-Library Metroidvania*

**카테고리**: 게임 디자인 및 분석 (Game Design & Taxonomy)  
*최초 작성일시: 2026-11-06 오후 02:57:19 (KST, UTC+9) | 최종 수정일시: 2026-11-09 오후 07:30:56 (KST, UTC+9)*

<context>
본 문서는 [영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획](cinematic_library_metroidvania_game_design.html)의 9장 오픈 이슈 중 "연출 스크립트 데이터 포맷 세부 설계"와 "게이팅 능력 목록" 항목에 선행해, 아저씨가 요구한 "일관성"이 구체적으로 무엇을 의미하는지 정의하고, 완성된 게임이 아니라 **플레이 가능성과 연출 API 가능성만 검증하는 최소 3씬(마을→필드→마을) 테스트**를 설계합니다. 원 기획 문서의 아키텍처(2장)·레벨 디자인(7장) 이론을 그대로 적용하되, 그중 "게이팅 설계 패턴이 이후 전체 게임의 템플릿으로 고착되는 효과"는 아저씨의 명시적 지시로 이번 테스트 범위에서 배제합니다(3.4절 참조).
</context>

**관련 문서**: [영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획](cinematic_library_metroidvania_game_design.html)(2장 아키텍처·7장 레벨 디자인의 원 설계) · [영상 연출 라이브러리 메트로이드배니아의 세계관과 정치 체제](cinematic_library_metroidvania_worldbuilding.html)(같은 프로젝트의 세계관 분과 문서)

<overview>
## 1. 개요 및 목적
*Overview & Purpose*

아저씨는 완성된 게임이 아니라 **① 플레이 가능성**(이동·게이팅이 실제로 작동하는가)과 **② 영상 연출 API의 구성·가능성**(연출 라이브러리가 실제로 설계될 수 있는가)만 확인하고자 합니다. 다만 그 과정에서 "일관성"을 유지하고 싶으나 그 의미를 모른다고 밝혔습니다. 본 문서는 이 "일관성"을 세 개의 서로 다른 층위로 분해해 정의하고(2장), 그중 이번 테스트에 포함할 층위와 명시적으로 배제할 층위를 구분한 뒤(3.4절), 마을A→필드→마을B 3개 씬으로 구성된 최소 테스트를 설계합니다(3장).
</overview>

<theory>
## 2. 핵심 개념 및 원리 — "일관성"의 세 층위
*Core Concepts — Three Layers of "Consistency"*

"일관성"은 단일 개념이 아니라 서로 다른 성격의 세 문제를 가리킵니다. 이 구분이 본 문서 전체의 전제입니다.

### 2.1 연출 데이터 스키마 일관성 — 데이터 구조 문제

[원 기획 문서](cinematic_library_metroidvania_game_design.html) 2.2절은 "연출 스크립트 경로"(사람이 Godot 에디터에서 `Animation` 리소스로 직접 저작)와 "레코더 경로"(실제 플레이 세션 중 상태를 자동 채집해 `CinematicSequence` Resource로 저장)라는 두 개의 서로 다른 **생성 경로**를 정의합니다. 두 경로는 만드는 방법이 다르지만, 재생 결과는 **같은 `CinematicPlayer` 노드가 추상화해 재생**해야 합니다(2.4.2절). 즉 쇼츠용으로 레코더 경로에서 뽑은 장면이 게임 본편 컷신(스크립트 경로 전용 영역)에서도 재생될 수 있어야 하며, 이것이 깨지면 1장의 원래 목적("한쪽 자산이 다른 쪽에서도 재생됨")이 성립하지 않습니다.

MonoGame 커뮤니티의 지침은 "컷신 코드를 쓰기 전에 컷신 스펙(데이터 스키마)을 먼저 쓰라"는 것이며, 이렇게 하면 게임을 켜보지 않고도 스키마 수준에서 검증 가능해진다고 설명합니다 [[1]](#ref-1). Unity(PlayableDirector/TimelineAsset), Unreal(LevelSequence/MovieScene), 닌텐도 내부 포맷(BFEVFL "TLIN": 배우·클립·트리거·서브타임라인·컷)이 서로 독립적으로 같은 뼈대로 수렴했다는 사례는, 이 기획이 요구하는 "두 경로의 데이터 스키마 통일"이 업계에서 반복 검증된 요구임을 뒷받침합니다 [[1]](#ref-1).

**이 층위의 일관성 = `CinematicSequence`를 읽는 재생기가 그 데이터의 출신(레코더/스크립트)을 구분할 필요가 없는 것.** 이는 명확히 **데이터 구조 문제**입니다.

### 2.2 플레이 상태 일관성 — 데이터 구조이자 아키텍처 문제

"사실 하나에는 소유자 하나(single owner per fact)"가 업계 공통 원칙으로 확인됩니다 — 대부분의 게임플레이 버그는 같은 데이터의 사본 두 개가 서로 어긋나는 것에서 발생합니다 [[2]](#ref-2). 구체적 구현 패턴은 다음과 같이 확인됩니다.

| 패턴 | 설명 | 출처 |
| :--- | :--- | :--- |
| **Redux식 단일 전역 상태** | 단일 소스 + 순수 리듀서로만 상태 변경. VR 개발사 A-Frame 팀이 적용 | [[3]](#ref-3) |
| **명시적 상태 전이** | 메뉴→플레이, 생존→사망 같은 전환을 작은 상태 머신으로 모델링해 "불법 상태 조합"을 막음 | [[2]](#ref-2) |
| **Godot Resource 기반 세이브** | 커스텀 `Resource` 클래스에 `@export` 변수로 상태를 담아 `.tres`로 직렬화. 세이브 리소스가 런타임에 이미 쓰는 아이템·퀘스트 리소스를 그대로 참조하면 상태의 이중 사본이 생기지 않음 | [[4]](#ref-4) |
| **Unity ScriptableObject** | 여러 오브젝트가 런타임에 읽는 공유 데이터 컨테이너로, 인스턴스별 사본을 피함(다만 독립 실행 빌드에서는 런타임 변경이 디스크에 자동 저장되지 않아 별도 세이브 시스템 필요) | [[5]](#ref-5) |

**이 층위의 일관성 = "필드에서 능력을 얻었다"는 사실이 마을A·필드·마을B 세 씬 중 어느 한 곳에만 존재하고, 나머지는 그걸 읽기만 하는 것.** 이것도 **데이터 구조(또는 그 보관 위치의 아키텍처) 문제**입니다.

### 2.3 게이팅 설계 일관성 — 데이터 구조가 아닌 설계·지각 문제

메트로이드배니아 설계 경험칙은 "자물쇠가 열쇠보다 먼저 보여야 한다"(플레이어가 명백히 통과 못 하는 장애물을 먼저 제시), "능력 하나는 최소 2개 이상의 이미 본 공간을 열어야 한다"는 원칙을 공통으로 제시합니다 [[6]](#ref-6). 찰머스 대학 석사논문(학술 자료)은 "폼 기능이 명확하고 환경 신호가 일관적일 때" 백트래킹이 실제로 성립함을 확인했습니다 [[7]](#ref-7).

**이 층위의 일관성 = 장애물이 "이건 이 능력으로 뚫린다"는 시각적 신호를 모순 없이 일관되게 주는 것.** 이는 코드상 자료형이 없어도 성립·붕괴할 수 있는 **플레이어 체감·설계 문제**이며, 2.1·2.2절과는 성격이 다릅니다.

<div class="callout">
<p><strong>세 층위의 분류 요약</strong>: 2.1절(스키마)·2.2절(상태)은 <b>데이터 구조 문제</b>이고, 2.3절(게이팅)은 <b>설계·지각 문제</b>입니다. 또한 2.3절의 "자물쇠-열쇠 신호 패턴"은 한 번 확립되면 이후 게임 전체 게이트가 그 패턴을 복사하게 되는 경향이 있어("every other gate in your game is a copy of this one" <sup class="citation"><a href="#ref-6">[6]</a></sup>), 콘텐츠 하나(구체적 능력·장애물 모양)보다 되돌리기 비용이 훨씬 큽니다. 이 비대칭이 3.4절에서 2.3절을 이번 테스트 범위에서 배제하는 근거입니다.</p>
</div>
</theory>

<analysis>
## 3. 최소 테스트 씬 설계 — 마을 A → 필드 → 마을 B
*Minimal Test Scene Design*

### 3.1 용어 정정 — 버티컬 슬라이스가 아니라 프로토타입/MVP

버티컬 슬라이스는 "투자자·퍼블리셔에게 자금 지원 전 증명하는, 거의 완성품 품질의 플레이 가능 조각"으로 정의되며 [[8]](#ref-8), "게임이 작동한다는 증명"이 아니라 "이 팀이 완성작을 만들 수 있다는 증명"이라는 점에서 용도 자체가 다릅니다. "데모·베타로 취급되어서는 안 된다"는 경고도 확인됩니다. 아저씨가 요구한 것은 완성도 전제가 없는 **MVP(실제로 뭔가를 배울 수 있는 최소 버전)**[[8]](#ref-8)에 해당하므로, 이하 "테스트 씬"이라는 명칭을 그대로 쓰되 버티컬 슬라이스 수준의 완성도를 목표로 삼지 않습니다.

### 3.2 3씬 구성

| 씬 | 역할 | 검증 대상(2장 층위) | 구체적 구성 |
| :--- | :--- | :--- | :--- |
| **마을 A** (출발) | 연출 스크립트 경로 검증 | 2.1절(스키마, 스크립트 경로 쪽) | NPC 1명과의 짧은 대화 — `AnimationPlayer`에 감정 태그·대사풍선 메서드 트랙을 심어 미리 저작. `CinematicSequence` 최소 스키마(3.3절)로 기술됨을 확인하는 최초 사례. |
| **필드** (경유) | 레코더 경로 검증 + 상태 플래그 기능 검증 | 2.1절(스키마, 레코더 경로 쪽), 2.2절(상태) | `required_ability` 플래그 체크만으로 열리고 닫히는 **기능 검증용 게이트** 1개(3.4절 참조). 통과 과정 전체를 레코더 경로로 채집해, 마을A와 같은 `CinematicPlayer`가 재생할 수 있는지 확인. |
| **마을 B** (도착) | 상태 일관성 검증 | 2.2절(상태) | 도착 시 짧은 연출 1개(구현됨). NPC가 능력 획득 플래그를 참조하는 대사 분기를 둬서, 오토로드/Resource에 저장된 상태가 씬 경계를 넘어 올바르게 읽히는지 확인(3.6절, 확인됨). |

### 3.3 최소 데이터 스키마 초안 (미확정, 이번 테스트 전용)

[원 기획 문서](cinematic_library_metroidvania_game_design.html) 9장 오픈 이슈의 "연출 스크립트 데이터 포맷 세부 설계"는 이 테스트의 선행 조건이므로, 전체를 확정하지 않고 이 3씬에 필요한 최소 필드만 초안으로 제시합니다.

```
CinematicSequence (연출 데이터, 원 기획서 2.4.1절):
  character_id: String
  timeline: Array[{ time: float, position: Vector2?, emotion_tag: String?,
                     dialogue_key: String?, camera_target: String? }]
  # 레코더 경로는 상태 변화 시점만 기록(원 기획서 2.4.4절 델타 인코딩)
  # 스크립트 경로는 AnimationPlayer 메서드 트랙이 이와 동일한 필드를 호출

SequenceModeConfig (게임 로직 데이터, 원 기획서 2.4.1절):
  rule_set_flags: int  # 이 3씬 테스트는 추격 시퀀스(규칙 세트 A/B) 불필요, 0(비활성)으로 고정
  required_ability: String  # 필드 씬 게이트 전용, 예: "double_jump"
```

### 3.4 범위에서 명시적으로 배제한 것 — 게이팅 설계 일관성(2.3절)

아저씨의 지시("되돌리기 어려운 것은 이번 테스트 구현에서는 적용하고 싶지 않다")에 따라, 2.3절의 "자물쇠-열쇠 신호 설계"는 이번 테스트에서 **의도적으로 구현하지 않습니다**. 구체적으로:

- 장애물을 능력 획득 전에 미리 보여주는 "프리뷰 기법"[[9]](#ref-9) 적용하지 않음.
- "능력 하나가 최소 2개 공간을 열어야 한다"는 설계 기준 적용하지 않음.
- 장애물의 시각적 암시(이게 어떤 능력으로 뚫리는지 미리 알려주는 디자인) 설계하지 않음.

대신 필드 씬의 게이트는 `required_ability` 플래그 유무만으로 열리고 닫히는 **기능 검증용 최소 구현**으로 축소합니다. 이렇게 하면 게이트의 생김새·신호 방식을 이후 전혀 다른 설계로 교체해도 다른 어떤 부분에도 영향이 없습니다 — 지금 단계에서는 되돌릴 수 없는 결정이 발생하지 않습니다.

### 3.5 일관성 검증 체크리스트

3씬을 구현한 뒤 아래를 통과하면 2.1·2.2절의 일관성이 유지됐다고 판단할 수 있습니다(2.3절은 3.4절에 따라 검증 대상에서 제외).

- [x] 마을A의 `CinematicSequence`(스크립트 경로)와 필드의 `CinematicSequence`(레코더 경로)가 같은 `CinematicPlayer` 노드로 재생되는가 — **확인됨**(3.6절)
- [x] 필드에서 얻은 능력 플래그가 마을B 씬 로드 시 중복 저장 없이 하나의 소스(오토로드 또는 Resource)에서 읽히는가 — **확인됨**(3.6절)
- [x] `SequenceModeConfig`만 수정했을 때 `CinematicSequence`가 영향받지 않는가(원 기획서 2.4.1절 리소스 이원화 원칙의 실제 검증) — **확인됨**(3.6절)

<div class="callout">
<p><strong>범위 표시</strong>: 이 설계는 플레이 가능성과 연출 API 가능성만 검증하는 최소 테스트이며, 전투·세계관·다국어·추격 시퀀스 등 <a href="cinematic_library_metroidvania_game_design.html">원 기획 문서</a> 9장의 나머지 오픈 이슈는 이 테스트 범위에 포함되지 않습니다.</p>
</div>

### 3.6 구현 경과 — 3씬 전체 완료(ajusine.game1)

구현 저장소(`ajusine.game1`, Godot 4.7.2)에서 마을A·필드·마을B 세 씬이 모두 완료되어, **이 문서가 설계한 최소 테스트의 원래 목표(플레이 가능성 + 연출 API 가능성 검증)가 달성되었습니다.** 상세 수치·테스트 로그는 구현 저장소의 보고서 [[10]](#ref-10)에 있으며, 본 절은 설계 차원에서 의미가 있는 결론만 요약합니다(AGENTS.md 3.15절 — 작업 로그는 위키 정본에 수록하지 않음).

- **체크리스트 1번(스키마 일관성) 확인됨**: 마을A·마을B는 `CinematicPlayer.play_scripted()`(스크립트 경로), 필드는 `CinematicPlayer.play_sequence()`(레코더 경로)로 각각 재생되며, 셋 다 같은 `CinematicPlayer` 클래스가 처리합니다.
- **체크리스트 3번(리소스 이원화) 확인됨**: `SequenceModeConfig`(`field_gate_config.tres`) 값을 바꿔도 `CinematicSequence`(레코더가 채집한 타임라인)에는 영향이 없음이 테스트로 확인되었습니다.
- **체크리스트 2번(상태 일관성) 확인됨**: 필드에서 능력을 획득한 뒤 씬을 전환해 마을B에 진입해도 `PlayerState` 오토로드 하나만 참조해 대사 분기가 결정됨을 확인했습니다 — 마을B 쪽 소스에 능력 상태의 사본 변수가 없다는 점까지 직접 검사했습니다.
- **9장 오픈 이슈 중 일부가 임시로 메워짐**(최종 확정 아님, 구현 저장소 수준의 임시 결정):
  - `CinematicPlayer`의 추상화 인터페이스 — `register_actor(character_id, node)`로 재생 대상을 등록하고, 레코더 경로 재생 시 `position`은 이전 항목까지 선형 보간하는 방식으로 구현됨.
  - 레코더 경로의 샘플링 간격 — 0.1초, 상태 변화 시에만 기록(델타 인코딩). 이번 테스트는 `position`만 채집하며 감정·대사·카메라는 채집 대상이 없습니다.
  - 필드 게이트의 능력 ID — `double_jump`(플래그 검사만, 이중 점프 물리 자체는 미구현).
- **범위 준수 확인**: 게이트는 3.4절 배제 원칙대로 "단색 블록, 시각적 신호 없음"으로 구현되어, 2.3절(게이팅 설계 일관성)에 손대지 않았다는 설계 의도가 그대로 지켜졌습니다.
- **5.3절 관련 후속 조치 완료**: `ajusine.game1`의 `project.godot`가 설치된 Godot 버전(4.7.2)에 맞춰 `config/features`를 `"4.7"`로 갱신했습니다 — [원 기획 문서](cinematic_library_metroidvania_game_design.html) 5.3절에서 남겨 둔 버전 정합성 점검 과제가 해소되었습니다.
- **남은 작업**: 레코더의 감정·대사·카메라 채집 미구현, 능력 상태의 세이브·로드(영속화) 미구현(세션 메모리 범위로만 검증).
- **해상도 파이프라인 적용 및 설계 문서 오류 수정 유발**: 구현 세션이 [원 기획 문서](cinematic_library_metroidvania_game_design.html) 6.1·6.6.1절의 내부 렌더 해상도(320×224)를 실제로 적용하는 과정에서, 그 수치가 16:9(1920×1080)와 산술적으로 맞지 않는다는 원 문서 자체의 오류를 발견·보고했습니다 [[12]](#ref-12). 이에 따라 원 문서 6.6.1절의 내부 렌더 해상도를 **480×270**(16:9 네이티브, 1080p에서 정수 4배)으로 교정했습니다.
- **축별 환산 규칙(설계적 결정, 구현 세션이 교차 기록 요청)**: 320×224→480×270은 가로 ×1.5, 세로 ×1.2054로 두 축의 배율이 다릅니다(10:7→16:9로 비율 자체가 바뀌기 때문). 구현 세션은 월드 요소를 세 범주로 나눠 각기 다른 기준을 적용했습니다 — ① 세로 화면 비율 요소(지면 높이·카메라 하한·배경 산)는 **화면 높이 비율 유지** 기준, ② 가로 화면 비율 요소(월드 폭·랜드마크 좌표·카메라 가로 한계)는 **화면 폭 대비 레벨 길이 유지**(×1.5) 기준, ③ 캐릭터 크기 의존 요소(충돌 영역·이동/점프/중력 수치·게이트 크기)는 **캐릭터 픽셀 크기가 안 변하므로 불변** 기준. 이 구분은 이후 해상도가 또 바뀔 때도 적용할 수 있는 일반 원칙입니다.
- **이동 속도 트레이드오프(미해결, 9장 오픈 이슈와 연결)**: 월드 폭을 ×1.5로 넓히면서 이동 속도는 유지해, 화면 한 폭을 횡단하는 시간이 3.2초→4.8초로 늘었습니다. 조작감 수치(7.1.1절)가 설계 문서에 아직 명세되지 않아 구현 세션이 임의로 속도를 올리지 않고 그대로 보류했습니다.
- **캐릭터 화면 비율 — 정수 배율 원칙과의 충돌, 재조정 결정**: 할로우 나이트 교차검증(11~12%)에 맞춰 11.2% 비율을 유지하려면 스프라이트에 비정수 배율(약 1.2054배)을 걸어야 했으나, 이는 6.6.1절의 정수 배율 원칙과 충돌합니다. 구현 세션은 정수 배율 원칙을 우선해 스프라이트를 1배로 유지했고, 그 결과 캐릭터 화면 비율이 **9.26%**로 낮아져 할로우 나이트 범위보다 2~3%p 낮은 상태가 되었습니다 [[13]](#ref-13). 이 간극을 아저씨가 검토한 결과, **실루엣 약 30px(프레임 약 38px)의 새 스프라이트로 교체해 11~12% 목표를 다시 맞추는 쪽으로 결정**했고, 구현 저장소가 기존 CC0 러너를 도트 단위로 기계적 확대해(새 아트 제작이 아님) 실루엣 30px·화면 비율 11.11%를 달성했습니다 [[14]](#ref-14).
- **캐릭터 스킨 교체(Shantae/Rottytops/Sky) 및 내부 해상도 640×360 재교정(2026-11-09)**: 아저씨가 주인공 스프라이트를 《Shantae and the Pirate's Curse》 도트 시트 기반 스킨으로 교체 요청했습니다. 이 시트의 실루엣(약 41px)을 480×270에서 1배로 쓰면 화면 비율이 15.2%(목표 11~12% 초과)가 되어, 구현 세션은 **내부 해상도를 480×270 → 640×360**으로 다시 바꿔 비율을 11.4%로 맞췄습니다(1920×1080에서 정수 3배 유지) [[15]](#ref-15). [원 기획 문서](cinematic_library_metroidvania_game_design.html) 6.1·6.6.1절을 이 수치로 교정했습니다. 해당 스킨 에셋은 재사용 허가를 확인하지 못해 `local_only/`(저장소 미포함)로만 적용되며, 공개 저장소를 그대로 내려받으면 앞 문단의 CC0 30px 러너로 자동 대체(폴백)됩니다 — 이번 테스트의 체크리스트 통과 여부와는 무관한 저작권 확인 미결 사항입니다.

<div class="callout">
<p><strong>의미적 모순 대조 — "애셋 없이 진행" 범위의 일부 변경</strong>: 필드 보고서 이후 구현 저장소에 <code>assets/characters/runner/</code>(OpenGameArt "Runner character", CC0 라이선스, 출처·SHA-256 체크섬이 기록된 <code>SOURCE.txt</code> 동봉 <sup class="citation"><a href="#ref-11">[11]</a></sup>)가 추가되어, 플레이어·NPC·고스트가 실제 스프라이트 애니메이션(idle/run/jump)으로 표현됩니다. 이는 "이미지나 사운드 같은 에셋 없이도 진행할 수 있는가?"라는 이전 논의에서 합의한 그레이박싱(단순 도형) 원칙의 <b>일부 수정</b>입니다. 다만 2.3·3.4절이 명시적으로 배제한 "자물쇠-열쇠 시각적 신호 설계"는 게이트 자체가 여전히 "단색 블록, 시각적 신호 없음"으로 유지되어 있어 영향받지 않습니다 — 변경된 것은 캐릭터 표현 수단(스프라이트 유무)이고, 배제된 게이팅 설계 원칙은 그대로입니다.</p>
</div>
</analysis>

## 4. 용어 정리 및 정의
*Glossary & Definitions*

| 용어 | 정의 |
| :--- | :--- |
| **연출 데이터 스키마 일관성** | 연출 스크립트 경로와 레코더 경로가 생성한 데이터를 같은 재생기(`CinematicPlayer`)가 구분 없이 재생할 수 있어야 한다는 요구. 데이터 구조 문제. 2.1절 참조. |
| **플레이 상태 일관성** | 특정 사실(능력 획득 여부 등)이 하나의 소스에만 존재하고 나머지는 그것을 읽기만 해야 한다는 요구("단일 진실 공급원"). 데이터 구조·아키텍처 문제. 2.2절 참조. |
| **게이팅 설계 일관성** | 장애물이 "이건 이 능력으로 뚫린다"는 시각적 신호를 매번 같은 규칙으로 전달해야 한다는 요구. 설계·지각 문제이며 데이터 구조가 아님. 2.3절 참조. |
| **단일 진실 공급원** | **Single Source of Truth**. 특정 사실을 저장하는 소유자를 하나로 한정하고 나머지는 파생시키는 아키텍처 원칙. 2.2절 참조. |
| **버티컬 슬라이스** | **Vertical Slice**. 거의 완성품 품질로 만들어 완성작의 모습을 보여주는, 투자자 설득용 플레이 가능 조각. 이번 테스트와는 완성도 전제가 다름. 3.1절 참조. |
| **프로토타입/MVP** | 실제로 플레이해 무언가를 배울 수 있는 최소 버전. 버티컬 슬라이스와 달리 완성도를 전제하지 않음. 3.1절 참조. |
| **자물쇠-열쇠 신호 패턴** | 장애물(자물쇠)을 능력(열쇠) 획득 전에 미리 보여주는 메트로이드배니아 게이팅 설계 경험칙. 한 번 확립되면 이후 모든 게이트의 암묵적 템플릿이 되는 경향이 있어 되돌리기 비용이 큼. 2.3·3.4절 참조. |
| **기능 검증용 게이트** | 자물쇠-열쇠 신호 설계 없이 플래그 유무만으로 열리고 닫히는 최소 구현 게이트. 이번 테스트가 2.3절 대신 채택한 축소형 구현. 3.4절 참조. |

## 5. 참고 자료 및 원천 데이터 출처
*References & Raw Sources*

<div class="callout">
    <strong>📁 로컬 원천 데이터 보존 경로:</strong><br>
    본 위키 문서는 로컬 원천 텍스트 저장소 <code><a href="raw/20261106_cinematic_library_metroidvania_consistency_and_test_scenes_raw.txt">raw/20261106_cinematic_library_metroidvania_consistency_and_test_scenes_raw.txt</a></code>의 데이터와 교차 검증을 거쳐 작성되었습니다. Godot/Unity 공식 문서는 1차 출처로, GDQuest·찰머스 대학 석사논문은 상대적으로 신뢰도가 높은 보조 출처로, sorceress.games·summerengine.com·bugnet.io·dragonflydb.io FAQ·dev.to 블로그는 튜토리얼/실무 블로그 수준의 보조 출처로 구분해 기록합니다. "레코더 경로 vs 스크립트 경로"라는 이 기획 고유의 구분에 정확히 부합하는 선행 사례는 확보하지 못했음을 명시합니다.
</div>

<ol class="reference-list">
    <li id="ref-1">[1] MonoGame Community. 〈Write the Cutscene Spec Before You Write the Cutscene Code〉. <a href="https://community.monogame.net/t/write-the-cutscene-spec-before-you-write-the-cutscene-code/21593" target="_blank">community.monogame.net</a> — 2.1절 스펙 선행 원칙, 타임라인 스키마 수렴 사례(Unity/Unreal/닌텐도)의 근거.</li>
    <li id="ref-2">[2] bugnet.io. 〈How to Manage Game State Without Losing Your Mind〉. <a href="https://bugnet.io/blog/how-to-manage-game-state-without-losing-your-mind" target="_blank">bugnet.io</a> — 2.2절 "사실 하나당 소유자 하나" 원칙 및 명시적 상태 전이의 근거.</li>
    <li id="ref-3">[3] A-Frame(Mozilla VR). 〈GameState〉 블로그. <a href="https://aframe.io/blog/gamestate/" target="_blank">aframe.io</a> — 2.2절 Redux식 단일 전역 상태 적용 사례의 근거.</li>
    <li id="ref-4">[4] GDQuest. 〈Saving and Loading Games in Godot 4 (with resources)〉. <a href="https://www.gdquest.com/library/save_game_godot4" target="_blank">gdquest.com</a> — 2.2절 Godot Resource 기반 단일 진실 공급원 구현의 근거.</li>
    <li id="ref-5">[5] Unity 공식 문서. 〈ScriptableObject data assets〉. <a href="https://docs.unity.com/en-us/engine/6000.7/manual/scripting/get-started/fundamental-unity-types/class-scriptable-object" target="_blank">docs.unity.com</a> — 2.2절 ScriptableObject 공유 데이터 컨테이너 패턴의 근거.</li>
    <li id="ref-6">[6] Summerengine.com. 〈How to Make a Metroidvania With AI〉. <a href="https://www.summerengine.com/blog/make-a-metroidvania-with-ai.md" target="_blank">summerengine.com</a> / Sorceress.games. 〈Sprawl: How to Make a Metroidvania (Map + Ability Gates)〉. <a href="https://sorceress.games/blog/sprawl-how-to-make-a-metroidvania-map-ability-gates" target="_blank">sorceress.games</a> — 2.3절 자물쇠-열쇠 신호 패턴 및 "모든 게이트는 복사본" 서술의 근거(튜토리얼/블로그 수준).</li>
    <li id="ref-7">[7] Chalmers University of Technology. 〈Designing Multi-Mode Player Abilities to Enhance Backtracking in Metroidvania Levels〉(석사논문). <a href="https://odr.chalmers.se/items/d79d64a8-8f42-4b85-a4f8-5b1b259962b0" target="_blank">odr.chalmers.se</a> — 2.3절 환경 신호 일관성과 백트래킹 성립 조건의 학술 근거.</li>
    <li id="ref-8">[8] Dragonfly DB FAQ. 〈What is a vertical slice in game development〉. <a href="https://www.dragonflydb.io/faq/what-is-vertical-slice-in-game-development" target="_blank">dragonflydb.io</a> / Juego Studio. 〈Vertical Slice vs Prototype vs MVP〉. <a href="https://www.juegostudio.com/blog/vertical-slice-vs-prototype-vs-mvp" target="_blank">juegostudio.com</a> — 3.1절 버티컬 슬라이스/프로토타입/MVP 구분의 근거.</li>
    <li id="ref-9">[9] 이 위키. 〈영상 연출 라이브러리 병행 플레이어블 메트로이드배니아 게임 기획〉. <a href="cinematic_library_metroidvania_game_design.html">cinematic_library_metroidvania_game_design.html</a> — 3.4절 프리뷰 기법 등 원 기획서 7.2.2절 참조.</li>
    <li id="ref-10">[10] 구현 저장소 <code>ajusine.game1</code>(별도 git 저장소, 이 위키 바깥). <code>reports/20261106_field_scene_report.md</code>, <code>reports/20261106_village_b_report.md</code> — 3.6절 마을A·필드·마을B 구현 및 체크리스트 검증 결과의 상세 로그. 본 위키는 원문을 그대로 가져오지 않고 설계적으로 의미 있는 결론만 요약함(AGENTS.md 3.15절).</li>
    <li id="ref-11">[11] 구현 저장소 <code>ajusine.game1</code>. <code>assets/characters/runner/SOURCE.txt</code> — 3.6절 CC0 러너 스프라이트의 출처·라이선스·체크섬 기록(OpenGameArt, 작가 David Harrington, 2026-11-06 확인).</li>
    <li id="ref-12">[12] 구현 저장소 <code>ajusine.game1</code>. <code>reports/20261106_resolution_pipeline_report.md</code>, <code>reports/20261106_resolution_480x270_report.md</code> — 3.6절 해상도 파이프라인 적용, 원 기획 문서 6.6.1절 오류 발견, 480×270 축별 환산 규칙의 근거.</li>
    <li id="ref-13">[13] 구현 저장소 <code>ajusine.game1</code>. <code>reports/20261106_hollow_knight_scale_research.md</code> — 3.6절 캐릭터 화면 비율 교차검증의 근거. AtomechLLC/game-animation-library PR #40(히트박스 데이터, 신뢰도 비교적 높음) 및 Steam 공식 스크린샷 측정(신뢰도 중간) 기반.</li>
    <li id="ref-14">[14] 구현 저장소 <code>ajusine.game1</code>. <code>reports/20261106_sprite_30px_report.md</code> — 3.6절 CC0 러너 30px 확대 스프라이트 교체(화면 비율 11.11% 달성)의 근거.</li>
    <li id="ref-15">[15] 구현 저장소 <code>ajusine.game1</code>. <code>reports/20261109_shantae_skin_640x360_report.md</code> — 3.6절 Shantae/Rottytops/Sky 스킨 교체 및 내부 해상도 640×360 재교정의 근거. 라이선스 미확인으로 <code>local_only/</code>(저장소 미포함) 적용.</li>
</ol>
