# -*- coding: utf-8 -*-
import re

with open('Z:/wiki/possession_curse_and_gossip_psychology.md', 'r', encoding='utf-8') as f:
    text = f.read()

target_pattern = r'(## 5\. 저주의 심리·사회적 파멸 기제와 결함\s*\n\*Psychological and Sociological Mechanisms and Inherent Flaws of Cursing\*\s*\n\n)(```)'
replacement = r'''\1<div class="callout">
    <strong>📌 저주 전문 독립 위키 안내:</strong><br>
    저주의 초자연적 비실재성, 발신자의 4대 마술적 사고 및 3대 역사 실례(취선당·로마·일본), 수신자의 교감신경 폭풍과 전 세계 10대 문화권 실증 사례(아이티·호주·마오리·유럽·나바호·세일럼·인도·동남아·현대의학·한국), 사회적 희생양 메커니즘 및 회복적 사법에 관한 심층 분석은 독립 위키 <strong><a href="curse_psychological_and_sociological_mechanisms.html">저주의 심리·사회·생리학적 기제와 자멸성 및 회복적 대안 모델</a></strong>을 참조하십시오.
</div>\n\n\2'''

new_text = re.sub(target_pattern, replacement, text, count=1)
if new_text != text:
    print('[성공] Section 5 콜아웃 추가 완료')
    text = new_text
else:
    print('[확인] Section 5 패턴 불일치')

text = re.sub(r'updated: ".*?"', 'updated: "2026-09-01 오전 11:10:00 (KST, UTC+9)"', text)
text = re.sub(r'최종 수정일시: .*? \(KST, UTC\+9\)', '최종 수정일시: 2026-09-01 오전 11:10:00 (KST, UTC+9)', text)

with open('Z:/wiki/possession_curse_and_gossip_psychology.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Markdown file updated.')
