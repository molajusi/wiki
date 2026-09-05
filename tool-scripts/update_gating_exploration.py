# -*- coding: utf-8 -*-
"""
Update game_gating_mechanisms.md, game_gating_mechanisms.html, and raw text file
with comprehensive exploration genre gating analysis.
"""
import os

MD_PATH = r"Z:\wiki\game_gating_mechanisms.md"
HTML_PATH = r"Z:\wiki\game_gating_mechanisms.html"
RAW_PATH = r"Z:\wiki\raw\20260824_game_gating_mechanisms_raw.txt"

# 1. Update Markdown
with open(MD_PATH, 'r', encoding='utf-8') as f:
    md_content = f.read()

sec4_md = """## 4. 탐색 중심 장르에서의 게이팅 정합성과 불협화음
*Gating Harmony & Dissonance in Exploration Genres*

메트로이드배니아(Metroidvania)와 메트로이드브레이니아(Metroidbrainia)는 모두 '비선형적 미지의 세계를 탐험하고 미완결 장벽을 돌파한다'는 공통의 코어 루프를 공유하지만, 장벽을 구성하고 해제하는 **'게이팅의 존재론적 성격'**에서 근본적인 차이를 보입니다.

### 4.1. 메트로이드배니아에 최적화된 게이팅과 신체 현상학
*Harmonious Gating in Metroidvania & Body Phenomenology*

메트로이드배니아의 본질은 플레이어가 가상 세계 속 아바타의 신체적 한계를 극복하며 공간의 도달 범위를 확장하는 데 있습니다.

* **최적 게이팅 기제:** **능력 게이팅(Ability Gating)** 및 **환경 적응형 다이어제틱 아이템 게이팅(Diegetic Environmental Gating)**.
* **철학적·인지적 근거 (메를로-퐁티의 신체 현상학):**
  * 프랑스 현상학자 모리스 메를로-퐁티(Maurice Merleau-Ponty)는 저서 《지각의 현상학》에서 인간이 공간을 기하학적 좌표계가 아니라 자신의 신체가 행할 수 있는 **'운동 가능성(I can / Je peux)'**의 지평으로 지각한다고 보았습니다.
  * 플레이어가 《슈퍼 메트로이드(Super Metroid)》(1994)에서 '모프볼'이나 '스페이스 점프'를 얻거나, 《할로우 나이트(Hollow Knight)》(2017)에서 '사마귀 갈고리(벽 타기)'를 획득하는 순간, 아바타의 운동 능력 확장은 플레이어 자신의 **신체 도식(Body Schema, Schéma Corporel)** 내부로 체화(Embodiment)됩니다.
  * 이전에 지나쳤던 "도달할 수 없는 높은 절벽"은 단순한 데이터가 아니라 "나의 신체가 도약하여 밟고 오를 수 있는 발판"으로 지각의 존재론적 전환(Ontological Shift)을 겪습니다.
* **내러티브와의 유기적 융합 (루도내러티브 공명):**
  * 《오리와 도깨비불(Ori and the Will of the Wisps)》(2020)에서 숲의 정령이 새로운 빛의 힘을 각성하거나, 《나인 솔즈(Nine Sols)》(2024)에서 도교적 기(Chi) 조작 기술을 체득하는 과정은 주인공의 서사적 성장 및 각성과 공간의 물리적 개방이 1:1로 일치하는 강력한 **루도내러티브 공명(Ludonarrative Resonance)**을 형성합니다.

### 4.2. 메트로이드브레이니아에 최적화된 게이팅과 인식론적 비가역성
*Harmonious Gating in Metroidbrainia & Epistemological Irreversibility*

메트로이드브레이니아는 캐릭터의 물리적 스펙이나 조작 스킬의 확장이 아니라, 오직 플레이어 자신의 두뇌 속에 축적되는 '규칙의 이해와 지식'으로 장벽을 돌파하는 지적 탐험 장르입니다.

* **최적 게이팅 기제:** **순수 지식 게이팅(Knowledge Gating)** 및 **환경 기호/규칙 해독(Semiotic Decryption)**.
* **철학적·인지적 근거 (인식론적 전환과 지식의 비가역성):**
  * **Ending-From-Beginning 구조:** 《아우터 와일즈(Outer Wilds)》(2019)나 《튜닉(Tunic)》(2022)에서 플레이어의 인게임 캐릭터 능력치는 게임 시작 1초부터 엔딩 크레딧까지 1바이트도 증가하지 않습니다.
  * **지식의 비가역성(Irreversibility of Knowledge):** 지식은 한 번 깨닫고 나면 결코 '모르던 상태'로 되돌릴 수 없는 비가역적 속성을 지닙니다. 플레이어가 우주의 물리 법칙(양자 관측 고정, 역방향 토네이도 잠수)이나 숨겨진 조작 체계(D-패드 커맨드)를 이해하는 순간, 장벽은 시스템의 물리적 잠금 해제가 아니라 플레이어의 **'인식론적 자각(Epistemological Awakening)'**에 의해 허물어집니다.
  * **앤디 클라크(Andy Clark)의 확장된 인지(Extended Mind):** 플레이어는 인게임 메모, 환경 텍스트, 현실의 수첩/노트를 두뇌 밖의 외현적 인지 보조 도구로 적극 활용하여 복잡한 퍼즐 구조를 통합적으로 재구성합니다.
* **내러티브와의 유기적 융합:**
  * 《아우터 와일즈(Outer Wilds)》(2019)에서 멸망한 고대 노마이 종족의 학술 기록을 번역하고 태양계 루프의 원리를 밝혀내는 과정 자체가 게임의 메인 스토리이자 유일한 진행 동력입니다. 지식을 얻는 행위가 곧 세계관의 진실과 직접 결합합니다.

### 4.3. 탐색 장르를 파괴하는 불협화음 게이팅과 루도내러티브 붕괴
*Dissonant Gating & Ludonarrative Collapse in Exploration Genres*

메트로이드배니아 및 메트로이드브레이니아에 부적절한 게이팅이 도입될 경우, 장르의 핵심 정체성인 **'공간적 주도권(Spatial Agency)'**과 **'탐색의 흐름(Flow)'**이 파괴되며 심각한 루도내러티브 불협화가 발생합니다:

1. **서사적 구두 승인 및 인위적 통제 게이팅 (Authoritarian Narrative Gating):**
   * **사례:** 《메트로이드 아더 엠(Metroid: Other M)》(2010)의 방열복 미승인 사태.
   * **불협화음 메커니즘:** 캐릭터가 이미 강력한 장비를 몸에 지니고 있음에도, 상사나 내레이션의 자의적 '구두 승인' 전까지 사용을 금지당합니다. 용암 지대에서 불에 타면서도 허가가 없어 방열복을 켜지 못하는 상황은 플레이어의 상식적 개연성과 주도권을 완전히 파괴합니다.
2. **인위적 수치·레벨 게이팅 (Artificial Stat/Level Gating):**
   * **사례:** 《어쌔신 크리드: 오디세이(Assassin's Creed: Odyssey)》(2018)의 고레벨 적 암살 무력화.
   * **불협화음 메커니즘:** 플레이어가 완벽한 피지컬 조작으로 적의 공격을 피하고 은신 암살을 성공시켜도, 수치적 레벨 차이로 인해 데미지가 들어가지 않고 즉사합니다. 이는 "조작과 환경 분석을 통한 극복"이라는 장르적 약속을 배신하고 게임을 지루한 '수치 반복 파밍(Grinding) 노동'으로 전락시킵니다.
3. **시간 게이팅 및 과금 페이월 게이팅 (Time & Monetization Gating):**
   * **사례:** 모바일 F2P식 쿨다운 타이머, 행동력(스태미나) 제한, 유료 결제 즉시 개방창.
   * **불협화음 메커니즘:** 탐색 장르의 생명인 '몰입의 마법원(Magic Circle)'과 호기심의 연속성을 인위적으로 절단합니다. 미지의 던전 문 앞에서 "24시간 뒤에 열립니다" 혹은 "유료 재화 10개를 소모하여 여세요"라는 알림을 마주하는 순간, 탐험의 예술적 긴장감은 상업적 착취감으로 치환됩니다.
4. **단순 자물쇠-열쇠(Keycard) 남용에 의한 형식적 아이템 게이팅 (Key-Lock Overload):**
   * **불협화음 메커니즘:** 새로운 이동 역학의 획득이나 지적 유레카 없이, 단순히 "빨간 열쇠로 빨간 문 열기", "청동 열쇠로 청동 문 열기"만 무한 반복될 경우, 공간 탐색은 의미 있는 지형 극복이 아니라 '지루한 우체부 배달 심부름(Fetch Quest)'으로 전락합니다.

### 4.4. 게이팅 유형별 탐색 장르 정합성 및 철학적 분석 매트릭스
*Genre Harmony & Philosophical Framework Matrix*

| 게이팅 유형 | 메트로이드배니아 정합도 | 메트로이드브레이니아 정합도 | 핵심 철학적 / 인지적 기반 | 장르적 내러티브 융합 효과 |
| :--- | :--- | :--- | :--- | :--- |
| **능력 게이팅 (Ability)** | **최적 (Essential)** | **부적합 / 보조** | 메를로-퐁티의 신체 도식(Body Schema) 확장 | 주인공의 육체적/영적 성장과 공간 개방의 1:1 일치 |
| **지식 게이팅 (Knowledge)** | **보조 (Supplementary)** | **최적 (Essential)** | 인식론적 전환 및 지식의 비가역성 (Epistemological Shift) | 세계의 미스터리 해독과 플레이어 지적 자각의 일체화 |
| **다이어제틱 환경 장비** | **정합 (Harmonious)** | **정합 (Harmonious)** | 하이데거의 도구 분석(Zuhandenheit)과 환경 적응 | 극한 환경(심해/용암) 생존과 서사적 탐험 당위성 부여 |
| **단순 열쇠 (Keycard)** | **주의 (Caution / 최소화)** | **주의 (Caution / 최소화)** | 불리언 조건 판정 (Boolean State Check) | 과도할 시 우체부 심부름으로 전락, 단기 목표 부여용으로 제한 필요 |
| **수치 / 레벨 게이팅** | **불협화음 (Dissonant)** | **치명적 불협화 (Fatal)** | 정량적 조건화 (Operant Conditioning) | 조작 숙련과 지적 추론을 무력화하고 반복 노가다 강제 |
| **시간 / 쿨다운 게이팅** | **치명적 불협화 (Fatal)** | **치명적 불협화 (Fatal)** | 행동경제학적 인위적 희소성 (Artificial Scarcity) | 탐색의 몰입 흐름(Flow) 절단 및 상업적 피로감 유발 |
| **과금 / 페이월 게이팅** | **치명적 불협화 (Fatal)** | **치명적 불협화 (Fatal)** | 착취적 다크 패턴 (Monetary Dark Pattern) | 마법원(Magic Circle) 파괴 및 게임의 예술적 가치 훼손 |

"""

if '## 4. 탐색 중심 장르에서의 게이팅 정합성과 불협화음' not in md_content:
    md_content = md_content.replace('## 8. 참고 자료 및 원천 데이터 출처', '## 9. 참고 자료 및 원천 데이터 출처')
    md_content = md_content.replace('## 7. 용어 정리 및 정의', '## 8. 용어 정리 및 정의')
    md_content = md_content.replace('## 6. 인지적 효과와 설계의 윤리적 딜레마', '## 7. 인지적 효과와 설계의 윤리적 딜레마')
    md_content = md_content.replace('### 6.1. 플레이어 주도권과 구조적 통제의 긴장', '### 7.1. 플레이어 주도권과 구조적 통제의 긴장')
    md_content = md_content.replace('### 6.2. 패키지 게임과 무료 게임의 가치관 대립', '### 7.2. 패키지 게임과 무료 게임의 가치관 대립')

    md_content = md_content.replace('## 5. 게이팅 유형별 비교 및 설계 분석', '## 6. 게이팅 유형별 비교 및 설계 분석')
    md_content = md_content.replace('### 5.1. 능력 게이팅', '### 6.1. 능력 게이팅')
    md_content = md_content.replace('### 5.2. 아이템 게이팅', '### 6.2. 아이템 게이팅')
    md_content = md_content.replace('### 5.3. 지식 게이팅', '### 6.3. 지식 게이팅')
    md_content = md_content.replace('### 5.4. 시간 게이팅', '### 6.4. 시간 게이팅')
    md_content = md_content.replace('### 5.5. 과금 게이팅', '### 6.5. 과금 게이팅')
    md_content = md_content.replace('### 5.6. 수치 게이팅', '### 6.6. 수치 게이팅')
    md_content = md_content.replace('### 5.7. 숙련 게이팅', '### 6.7. 숙련 게이팅')

    md_content = md_content.replace('## 4. 무료 게임 및 서비스형 게임의 경제적 게이팅', sec4_md + '## 5. 무료 게임 및 서비스형 게임의 경제적 게이팅')
    md_content = md_content.replace('### 4.1. 시간적 및 금전적 다크 패턴', '### 5.1. 시간적 및 금전적 다크 패턴')
    md_content = md_content.replace('### 4.2. 리텐션 제어와 핀치 포인트', '### 5.2. 리텐션 제어와 핀치 포인트')
    md_content = md_content.replace('### 4.3. 국내 학술 연구의 피로도 및 부분유료화 분석', '### 5.3. 국내 학술 연구의 피로도 및 부분유료화 분석')

    with open(MD_PATH, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print('MD updated successfully')
else:
    print('MD already has Section 4')

# 2. Update HTML
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html_content = f.read()

sec4_html = """            <section>
                <h2>4. 탐색 중심 장르에서의 게이팅 정합성과 불협화음</h2>
                <div class="section-subtitle">Gating Harmony & Dissonance in Exploration Genres</div>
                <p>
                    메트로이드배니아(Metroidvania)와 메트로이드브레이니아(Metroidbrainia)는 모두 '비선형적 미지의 세계를 탐험하고 미완결 장벽을 돌파한다'는 공통의 코어 루프를 공유하지만, 장벽을 구성하고 해제하는 <strong>'게이팅의 존재론적 성격'</strong>에서 근본적인 차이를 보입니다.
                </p>

                <h3>4.1. 메트로이드배니아에 최적화된 게이팅과 신체 현상학</h3>
                <div class="section-subtitle">Harmonious Gating in Metroidvania & Body Phenomenology</div>
                <p>
                    메트로이드배니아의 본질은 플레이어가 가상 세계 속 아바타의 신체적 한계를 극복하며 공간의 도달 범위를 확장하는 데 있습니다.
                </p>
                <ul>
                    <li><strong>최적 게이팅 기제:</strong> <b>능력 게이팅(Ability Gating)</b> 및 <b>환경 적응형 다이어제틱 아이템 게이팅(Diegetic Environmental Gating)</b>.</li>
                    <li>
                        <strong>철학적·인지적 근거 (메를로-퐁티의 신체 현상학):</strong>
                        <br>프랑스 현상학자 <strong>모리스 메를로-퐁티(Maurice Merleau-Ponty)</strong>는 저서 <em>《지각의 현상학》</em>에서 인간이 공간을 기하학적 좌표계가 아니라 자신의 신체가 행할 수 있는 <strong>'운동 가능성(I can / Je peux)'</strong>의 지평으로 지각한다고 보았습니다.
                        <br>플레이어가 《슈퍼 메트로이드(Super Metroid)》(1994)에서 '모프볼'이나 '스페이스 점프'를 얻거나, 《할로우 나이트(Hollow Knight)》(2017)에서 '사마귀 갈고리(벽 타기)'를 획득하는 순간, 아바타의 운동 능력 확장은 플레이어 자신의 <strong>신체 도식(Body Schema, Schéma Corporel)</strong> 내부로 체화(Embodiment)됩니다.
                        <br>이전에 지나쳤던 "도달할 수 없는 높은 절벽"은 단순한 데이터가 아니라 "나의 신체가 도약하여 밟고 오를 수 있는 발판"으로 지각의 존재론적 전환(Ontological Shift)을 겪습니다.
                    </li>
                    <li>
                        <strong>내러티브와의 유기적 융합 (루도내러티브 공명):</strong>
                        <br>《오리와 도깨비불(Ori and the Will of the Wisps)》(2020)에서 숲의 정령이 새로운 빛의 힘을 각성하거나, 《나인 솔즈(Nine Sols)》(2024)에서 도교적 기(Chi) 조작 기술을 체득하는 과정은 주인공의 서사적 성장 및 각성과 공간의 물리적 개방이 1:1로 일치하는 강력한 <strong>루도내러티브 공명(Ludonarrative Resonance)</strong>을 형성합니다.
                    </li>
                </ul>

                <h3>4.2. 메트로이드브레이니아에 최적화된 게이팅과 인식론적 비가역성</h3>
                <div class="section-subtitle">Harmonious Gating in Metroidbrainia & Epistemological Irreversibility</div>
                <p>
                    메트로이드브레이니아는 캐릭터의 물리적 스펙이나 조작 스킬의 확장이 아니라, 오직 플레이어 자신의 두뇌 속에 축적되는 '규칙의 이해와 지식'으로 장벽을 돌파하는 지적 탐험 장르입니다.
                </p>
                <ul>
                    <li><strong>최적 게이팅 기제:</strong> <b>순수 지식 게이팅(Knowledge Gating)</b> 및 <b>환경 기호/규칙 해독(Semiotic Decryption)</b>.</li>
                    <li>
                        <strong>철학적·인지적 근거 (인식론적 전환과 지식의 비가역성):</strong>
                        <br><strong>Ending-From-Beginning 구조:</strong> 《아우터 와일즈(Outer Wilds)》(2019)나 《튜닉(Tunic)》(2022)에서 플레이어의 인게임 캐릭터 능력치는 게임 시작 1초부터 엔딩 크레딧까지 1바이트도 증가하지 않습니다.
                        <br><strong>지식의 비가역성(Irreversibility of Knowledge):</strong> 지식은 한 번 깨닫고 나면 결코 '모르던 상태'로 되돌릴 수 없는 비가역적 속성을 지닙니다. 플레이어가 우주의 물리 법칙(양자 관측 고정, 역방향 토네이도 잠수)이나 숨겨진 조작 체계(D-패드 커맨드)를 이해하는 순간, 장벽은 시스템의 물리적 잠금 해제가 아니라 플레이어의 <strong>'인식론적 자각(Epistemological Awakening)'</strong>에 의해 허물어집니다.
                        <br><strong>앤디 클라크(Andy Clark)의 확장된 인지(Extended Mind):</strong> 플레이어는 인게임 메모, 환경 텍스트, 현실의 수첩/노트를 두뇌 밖의 외현적 인지 보조 도구로 적극 활용하여 복잡한 퍼즐 구조를 통합적으로 재구성합니다.
                    </li>
                    <li>
                        <strong>내러티브와의 유기적 융합:</strong>
                        <br>《아우터 와일즈(Outer Wilds)》(2019)에서 멸망한 고대 노마이 종족의 학술 기록을 번역하고 태양계 루프의 원리를 밝혀내는 과정 자체가 게임의 메인 스토리이자 유일한 진행 동력입니다. 지식을 얻는 행위가 곧 세계관의 진실과 직접 결합합니다.
                    </li>
                </ul>

                <h3>4.3. 탐색 장르를 파괴하는 불협화음 게이팅과 루도내러티브 붕괴</h3>
                <div class="section-subtitle">Dissonant Gating & Ludonarrative Collapse in Exploration Genres</div>
                <p>
                    메트로이드배니아 및 메트로이드브레이니아에 부적절한 게이팅이 도입될 경우, 장르의 핵심 정체성인 <strong>'공간적 주도권(Spatial Agency)'</strong>과 <strong>'탐색의 흐름(Flow)'</strong>이 파괴되며 심각한 루도내러티브 불협화가 발생합니다:
                </p>
                <ul>
                    <li>
                        <strong>서사적 구두 승인 및 인위적 통제 게이팅 (Authoritarian Narrative Gating):</strong>
                        <br><em>사례: 《메트로이드 아더 엠(Metroid: Other M)》(2010)의 방열복 미승인 사태.</em>
                        <br>캐릭터가 이미 강력한 장비를 몸에 지니고 있음에도, 상사나 내레이션의 자의적 '구두 승인' 전까지 사용을 금지당합니다. 용암 지대에서 불에 타면서도 허가가 없어 방열복을 켜지 못하는 상황은 플레이어의 상식적 개연성과 주도권을 완전히 파괴합니다.
                    </li>
                    <li>
                        <strong>인위적 수치·레벨 게이팅 (Artificial Stat/Level Gating):</strong>
                        <br><em>사례: 《어쌔신 크리드: 오디세이(Assassin's Creed: Odyssey)》(2018)의 고레벨 적 암살 무력화.</em>
                        <br>플레이어가 완벽한 피지컬 조작으로 적의 공격을 피하고 은신 암살을 성공시켜도, 수치적 레벨 차이로 인해 데미지가 들어가지 않고 즉사합니다. 이는 "조작과 환경 분석을 통한 극복"이라는 장르적 약속을 배신하고 게임을 지루한 '수치 반복 파밍(Grinding) 노동'으로 전락시킵니다.
                    </li>
                    <li>
                        <strong>시간 게이팅 및 과금 페이월 게이팅 (Time & Monetization Gating):</strong>
                        <br><em>사례: 모바일 F2P식 쿨다운 타이머, 행동력(스태미나) 제한, 유료 결제 즉시 개방창.</em>
                        <br>탐색 장르의 생명인 '몰입의 마법원(Magic Circle)'과 호기심의 연속성을 인위적으로 절단합니다. 미지의 던전 문 앞에서 "24시간 뒤에 열립니다" 혹은 "유료 재화 10개를 소모하여 여세요"라는 알림을 마주하는 순간, 탐험의 예술적 긴장감은 상업적 착취감으로 치환됩니다.
                    </li>
                    <li>
                        <strong>단순 자물쇠-열쇠(Keycard) 남용에 의한 형식적 아이템 게이팅 (Key-Lock Overload):</strong>
                        <br>새로운 이동 역학의 획득이나 지적 유레카 없이, 단순히 "빨간 열쇠로 빨간 문 열기", "청동 열쇠로 청동 문 열기"만 무한 반복될 경우, 공간 탐색은 의미 있는 지형 극복이 아니라 '지루한 우체부 배달 심부름(Fetch Quest)'으로 전락합니다.
                    </li>
                </ul>

                <h3>4.4. 게이팅 유형별 탐색 장르 정합성 및 철학적 분석 매트릭스</h3>
                <div class="section-subtitle">Genre Harmony & Philosophical Framework Matrix</div>
                <table>
                    <thead>
                        <tr>
                            <th style="width: 18%;">게이팅 유형</th>
                            <th style="width: 17%;">메트로이드배니아 정합도</th>
                            <th style="width: 17%;">메트로이드브레이니아 정합도</th>
                            <th style="width: 24%;">핵심 철학적 / 인지적 기반</th>
                            <th style="width: 24%;">장르적 내러티브 융합 효과</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><b>능력 게이팅 (Ability)</b></td>
                            <td><span class="badge badge-green">최적 (Essential)</span></td>
                            <td><span class="badge badge-orange">부적합 / 보조</span></td>
                            <td>메를로-퐁티의 신체 도식(Body Schema) 확장</td>
                            <td>주인공의 육체적/영적 성장과 공간 개방의 1:1 일치</td>
                        </tr>
                        <tr>
                            <td><b>지식 게이팅 (Knowledge)</b></td>
                            <td><span class="badge badge-blue">보조 (Supplementary)</span></td>
                            <td><span class="badge badge-green">최적 (Essential)</span></td>
                            <td>인식론적 전환 및 지식의 비가역성</td>
                            <td>세계의 미스터리 해독과 플레이어 지적 자각의 일체화</td>
                        </tr>
                        <tr>
                            <td><b>다이어제틱 환경 장비</b></td>
                            <td><span class="badge badge-green">정합 (Harmonious)</span></td>
                            <td><span class="badge badge-green">정합 (Harmonious)</span></td>
                            <td>하이데거의 도구 분석(Zuhandenheit)과 환경 적응</td>
                            <td>극한 환경(심해/용암) 생존과 서사적 탐험 당위성 부여</td>
                        </tr>
                        <tr>
                            <td><b>단순 열쇠 (Keycard)</b></td>
                            <td><span class="badge badge-orange">주의 (Caution / 최소화)</span></td>
                            <td><span class="badge badge-orange">주의 (Caution / 최소화)</span></td>
                            <td>불리언 조건 판정 (Boolean State Check)</td>
                            <td>과도할 시 우체부 심부름으로 전락, 단기 목표 부여용 제한</td>
                        </tr>
                        <tr>
                            <td><b>수치 / 레벨 게이팅</b></td>
                            <td><span class="badge badge-red">불협화음 (Dissonant)</span></td>
                            <td><span class="badge badge-red">치명적 불협화 (Fatal)</span></td>
                            <td>정량적 조건화 (Operant Conditioning)</td>
                            <td>조작 숙련과 지적 추론을 무력화하고 반복 노가다 강제</td>
                        </tr>
                        <tr>
                            <td><b>시간 / 쿨다운 게이팅</b></td>
                            <td><span class="badge badge-red">치명적 불협화 (Fatal)</span></td>
                            <td><span class="badge badge-red">치명적 불협화 (Fatal)</span></td>
                            <td>행동경제학적 인위적 희소성 (Artificial Scarcity)</td>
                            <td>탐색의 몰입 흐름(Flow) 절단 및 상업적 피로감 유발</td>
                        </tr>
                        <tr>
                            <td><b>과금 / 페이월 게이팅</b></td>
                            <td><span class="badge badge-red">치명적 불협화 (Fatal)</span></td>
                            <td><span class="badge badge-red">치명적 불협화 (Fatal)</span></td>
                            <td>착취적 다크 패턴 (Monetary Dark Pattern)</td>
                            <td>마법원(Magic Circle) 파괴 및 게임의 예술적 가치 훼손</td>
                        </tr>
                    </tbody>
                </table>
            </section>"""

if '<h2>4. 탐색 중심 장르에서의 게이팅 정합성과 불협화음</h2>' not in html_content:
    html_content = html_content.replace('<h2>8. 참고 자료 및 원천 데이터 출처</h2>', '<h2>9. 참고 자료 및 원천 데이터 출처</h2>')
    html_content = html_content.replace('<h2>7. 용어 정리 및 정의</h2>', '<h2>8. 용어 정리 및 정의</h2>')
    html_content = html_content.replace('<h2>6. 인지적 효과와 설계의 윤리적 딜레마</h2>', '<h2>7. 인지적 효과와 설계의 윤리적 딜레마</h2>')
    html_content = html_content.replace('<h3>6.1. 플레이어 주도권과 구조적 통제의 긴장</h3>', '<h3>7.1. 플레이어 주도권과 구조적 통제의 긴장</h3>')
    html_content = html_content.replace('<h3>6.2. 패키지 게임과 무료 게임의 가치관 대립</h3>', '<h3>7.2. 패키지 게임과 무료 게임의 가치관 대립</h3>')

    html_content = html_content.replace('<h2>5. 게이팅 유형별 비교 및 설계 분석</h2>', '<h2>6. 게이팅 유형별 비교 및 설계 분석</h2>')
    html_content = html_content.replace('<h3>5.1. 능력 게이팅</h3>', '<h3>6.1. 능력 게이팅</h3>')
    html_content = html_content.replace('<h3>5.2. 아이템 게이팅</h3>', '<h3>6.2. 아이템 게이팅</h3>')
    html_content = html_content.replace('<h3>5.3. 지식 게이팅</h3>', '<h3>6.3. 지식 게이팅</h3>')
    html_content = html_content.replace('<h3>5.4. 시간 게이팅</h3>', '<h3>6.4. 시간 게이팅</h3>')
    html_content = html_content.replace('<h3>5.5. 과금 게이팅</h3>', '<h3>6.5. 과금 게이팅</h3>')
    html_content = html_content.replace('<h3>5.6. 수치 게이팅</h3>', '<h3>6.6. 수치 게이팅</h3>')
    html_content = html_content.replace('<h3>5.7. 숙련 게이팅</h3>', '<h3>6.7. 숙련 게이팅</h3>')

    html_content = html_content.replace('<h2>4. 무료 게임 및 서비스형 게임의 경제적 게이팅</h2>', '<h2>5. 무료 게임 및 서비스형 게임의 경제적 게이팅</h2>')
    html_content = html_content.replace('<h3>4.1. 시간적 및 금전적 다크 패턴</h3>', '<h3>5.1. 시간적 및 금전적 다크 패턴</h3>')
    html_content = html_content.replace('<h3>4.2. 리텐션 제어와 핀치 포인트</h3>', '<h3>5.2. 리텐션 제어와 핀치 포인트</h3>')
    html_content = html_content.replace('<h3>4.3. 국내 학술 연구의 피로도 및 부분유료화 분석</h3>', '<h3>5.3. 국내 학술 연구의 피로도 및 부분유료화 분석</h3>')

    target = '<section>\n                <h2>5. 무료 게임 및 서비스형 게임의 경제적 게이팅</h2>'
    html_content = html_content.replace(target, sec4_html + '\n            ' + target)

    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print('HTML updated successfully')
else:
    print('HTML already has Section 4')

# 3. Update Raw text file
with open(RAW_PATH, 'r', encoding='utf-8') as f:
    raw_content = f.read()

raw_addition = """
================================================================================
# 6. 탐색 중심 장르(메트로이드배니아·메트로이드브레이니아)의 게이팅 정합성과 불협화음 심층 연구
================================================================================

## 6.1. 메트로이드배니아의 신체 현상학과 능력 게이팅 (Merleau-Ponty's Body Schema)
- **핵심 기제:** 캐릭터의 물리적 조작 레퍼토리(이단 점프, 공중 대시, 벽 타기, 모프볼 등) 영구 확장.
- **현상학적 원리:**
  * 모리스 메를로-퐁티(Maurice Merleau-Ponty)의 《지각의 현상학》: 인간은 공간을 기하학적 좌표가 아닌 '신체가 행할 수 있는 운동 가능성(I can)'으로 지각함.
  * 아바타의 새로운 이동 스킬 획득은 플레이어의 '신체 도식(Body Schema)'으로 편입됨.
  * 이전의 '불가능한 장벽'이 '도약하여 밟을 수 있는 발판'으로 존재론적 전환(Ontological Shift)을 이룸.
- **루도내러티브 공명:** 《슈퍼 메트로이드(Super Metroid)》(1994)(파워슈트 복원), 《할로우 나이트(Hollow Knight)》(2017)(영혼/기술 체화), 《오리와 도깨비불(Ori and the Will of the Wisps)》(2020)(빛의 각성) 등 내러티브적 각성과 공간 개방의 1:1 일치.

## 6.2. 메트로이드브레이니아의 인식론적 전환과 지식 게이팅 (Epistemological Shift)
- **핵심 기제:** 캐릭터 스펙/아이템 불변(Ending-From-Beginning), 플레이어 두뇌 속 규칙/언어/법칙 해독.
- **인식론적 원리:**
  * 지식의 비가역성(Irreversibility of Knowledge): 한 번 알게 된 규칙은 다시 모르는 상태로 되돌릴 수 없음 (1회성 피크 경험).
  * 앤디 클라크(Andy Clark)의 '확장된 인지(Extended Mind)': 인게임 텍스트, 메모, 노트를 외현적 인지 도구로 활용.
- **루도내러티브 공명:** 《아우터 와일즈(Outer Wilds)》(2019)(노마이 문명 기록 해독), 《튜닉(Tunic)》(2022)(매뉴얼 속 고대 언어/커맨드 해독).

## 6.3. 탐색 장르를 파괴하는 불협화음 게이팅 (4대 파괴 기제)
1. **서사적 구두 승인 게이팅 (Authoritarian Narrative Gating):**
   * 《메트로이드 아더 엠(Metroid: Other M)》(2010): 이미 방열복을 입고 있으나 상사의 명령이 없어 불타 죽는 극단적 루도내러티브 불협화.
2. **인위적 수치·레벨 게이팅 (Artificial Stat Gating):**
   * 《어쌔신 크리드: 오디세이(Assassin's Creed: Odyssey)》(2018): 완벽한 컨트롤/암살을 성공시켜도 레벨 수치 부족으로 즉사, 탐색을 노가다로 퇴색.
3. **시간 및 과금 게이팅 (Time & Monetization Gating):**
   * F2P 쿨다운 타이머, 행동력 소모, 페이월: 탐색의 몰입 흐름(Flow)과 마법원(Magic Circle)을 상업적으로 절단.
4. **단순 자물쇠-열쇠(Keycard) 남용 (Key-Lock Overload):**
   * 이동 역학 확장 없는 단순 키카드 남발: 탐색을 '우체부 배달 심부름(Fetch Quest)'으로 전락.
"""

if '# 6. 탐색 중심 장르' not in raw_content:
    raw_content = raw_content.rstrip() + '\n' + raw_addition
    with open(RAW_PATH, 'w', encoding='utf-8') as f:
        f.write(raw_content)
    print('Raw file updated successfully')
else:
    print('Raw file already has Section 6')
