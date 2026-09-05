# -*- coding: utf-8 -*-
import os
import re

wiki_dir = 'Z:/wiki'
html_files = [f for f in os.listdir(wiki_dir) if f.endswith('.html')]

updated_count = 0
for fname in sorted(html_files):
    fpath = os.path.join(wiki_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'wiki.js' not in html:
        # Insert <script src="wiki.js" defer></script> right after style.css link
        if 'style.css' in html:
            html = re.sub(
                r'(<link\s+rel=["\']stylesheet["\']\s+href=["\']style\.css["\'][^>]*>)',
                r'\1\n    <script src="wiki.js" defer></script>',
                html,
                count=1
            )
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(html)
            updated_count += 1
            print(f'Injected wiki.js into {fname}')
        else:
            print(f'Warning: style.css not found in {fname}')
    else:
        print(f'wiki.js already in {fname}')

print(f'Total updated HTML files: {updated_count} / {len(html_files)}')
