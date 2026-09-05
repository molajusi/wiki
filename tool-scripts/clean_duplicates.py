# -*- coding: utf-8 -*-
with open('Z:/wiki/possession_curse_and_gossip_psychology.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Find the second occurrence of "## 7. 아동·청소년 서사에서의 배제 및 안전 대체 모델"
first_pos = text.find('## 7. 아동·청소년 서사에서의 배제 및 안전 대체 모델')
second_pos = text.find('## 7. 아동·청소년 서사에서의 배제 및 안전 대체 모델', first_pos + 10)

if second_pos != -1:
    print(f"Found duplicate section 7 at index {second_pos}, truncating...")
    clean_text = text[:second_pos].rstrip() + "\n"
    with open('Z:/wiki/possession_curse_and_gossip_psychology.md', 'w', encoding='utf-8') as f:
        f.write(clean_text)
    print("Cleaned up duplicate sections.")
else:
    print("No second occurrence found.")
