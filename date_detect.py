import re


dateRegex = re.compile(r'\d{1,2}\/\d{1,2}\/\d{4}$')

x = dateRegex.search('my birthday is 22/12/1995')
print('birthday: ' + x.group())