import bs4, requests


url = input('Enter the URL that you would like to verify the links for: ')
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
links = soup.select('a')
fof =[] # list of links that lead to 404 page

for link in links:
    try:
        unmade_url = link['href']
        if unmade_url.startswith('http'):
            to_check = unmade_url
        elif unmade_url.startswith('//'):
            to_check = 'https:' + unmade_url
        elif unmade_url.startswith('#'):
            to_check = url + unmade_url

        result = requests.get(unmade_url)

        if result.raise_for_status() == 404:
            fof.append(to_check)
    except:
        pass

print('Links processed these '+ str(len(fof)) + ' returned error 404: ')
print('\n'.join(fof))
