# -*- coding: utf-8 -*-
with open('Z:/wiki/possession_curse_and_gossip_psychology.md', 'rb') as f:
    raw_bytes = f.read()

# Try decoding with utf-8 replacing errors, or cp949
try:
    text = raw_bytes.decode('utf-8')
    print('Decoded as utf-8 successfully')
except UnicodeDecodeError:
    # Try decoding with cp949 or utf-8 with replace
    text = raw_bytes.decode('utf-8', errors='replace')
    print('Decoded with utf-8 (replaced invalid bytes)')

with open('Z:/wiki/possession_curse_and_gossip_psychology.md', 'w', encoding='utf-8') as f:
    f.write(text)
print('Saved cleanly as utf-8')
