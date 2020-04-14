import re


def strip(text):

    stripStartRegex = re.compile(r'(^\s*)')
    stripEndRegex = re.compile(r'\s*$')


    a = stripStartRegex.sub('',text)
    b = stripEndRegex.sub('',a)

    return b

text = '      amar sonar bangla ami tomay valobasi    '

print(strip(text))