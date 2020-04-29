import bs4, requests, sys, webbrowser

print('searching...')
page = requests.get('https://imgur.com/search?q=' + ' '.join(sys.argv[1:]))
page.raise_for_status()
soup = bs4.BeautifulSoup(page.content, 'html.parser')

linkElems = soup.select('.post')
print(linkElems)
# openNum = min(5, len(linkElems))
#
# for i in range(openNum):
#     urlToOpen = 'https://imgur.com' + linkElems[i].get('href')
#     print('Opening...')
#     webbrowser.open(urlToOpen)