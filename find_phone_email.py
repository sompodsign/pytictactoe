# python 3
# find_phone_email.py

import pyperclip, re

# Phone Regex
phoneRegex = re.compile(r'''
        (\d{3}|\(\d{3}\))    #first three-digit
        (\s|-|\.)?           #separator or space
        (\d{3}|\(\d{3}\))    #second three-digits
        (\s|-|\.)?           #separator or space
        (\d{4}|\(\d{4}\))    #last four-digits
    ''', re.VERBOSE)


# Email Regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-z.-]+                     # domain name
    (\.[a-zA-z]{2,4})               # dot-something
)''', re.VERBOSE)

# find phone numbers and email addresses on on the clipboard
text = str(pyperclip.paste())

matches = []
for phone in phoneRegex.findall(text):
    phoneNum = '-'.join([phone[0], phone[2], phone[4]])
    matches.append(phoneNum)

for emails in emailRegex.findall(text):
    matches.append(emails[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')