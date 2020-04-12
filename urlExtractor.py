# Python3
# urlExtractor.py

import pyperclip, re

urlRegex = re.compile(r'''
https?://                   # http:// or https://
(?:w{3}\.)?                 # www-dot
[a-zA-z0-9_-]+              # domain name
\.                          # dot
[a-zA-Z0-9_-]+              # extension
''',re.VERBOSE)

text = pyperclip.paste()

matches = []

for url in urlRegex.findall(text):
    matches.append(url)

for url in matches:
    print('url: ' + url)