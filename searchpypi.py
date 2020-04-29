#! python3
# searchpypi.py - Opens several search results.

import requests, sys, webbrowser, bs4

print('Searching...') # Display the text while downloading the search result page
res = requests.get('https://pypi.org/search/?q=' + '+'.join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# open a browser tab for each result.
linkElems = soup.select('.package-snippet')
print(linkElems)

# open a browser tab for each result.
# numOpen = min(5, len(linkElems))
# for i in range(numOpen):
#     urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
#     print('Opening', urlToOpen)
#     webbrowser.open(urlToOpen)