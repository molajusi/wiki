# -*- coding: utf-8 -*-
with open('Z:/wiki/possession_curse_and_gossip_psychology.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith('## '):
        print(f"Line {i+1}: {line.strip()}")
