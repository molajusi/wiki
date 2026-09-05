import re, collections

md_text = open('wiki_documentation_standards.md', encoding='utf-8').read()
html_text = open('wiki_documentation_standards.html', encoding='utf-8').read()
body_m = re.search(r'<main[^>]*>(.*?)</main>', html_text, re.S)
html_body = body_m.group(1) if body_m else html_text

href_shape = r'(?:https?://|file:///|mailto:|#|\.\./|\./)[^)]*|[^)]*\.(?:html|md)(?:#[^)]*)?'
md_links = sorted(re.findall(r'\]\((' + href_shape + r')\)', md_text) + re.findall(r'href="([^"]+)"', md_text))
html_links = sorted(re.findall(r'href="([^"]+)"', html_body))

print('MD diff:', collections.Counter(md_links) - collections.Counter(html_links))
print('HTML diff:', collections.Counter(html_links) - collections.Counter(md_links))
