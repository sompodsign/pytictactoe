import requests, bs4, os

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    print(f"Donwloading page {url}")
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#comic > img')

    if comicElem == []:
        print('could not found any image.')
    else:
        comicUrl = 'https://xkcd.com' + comicElem[0].get('src')
        print(f"Downloading image {comicUrl}")
        res = requests.get(comicUrl)
        res.raise_for_status()

        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')

        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('#middleContainer > ul:nth-child(2) > li:nth-child(2) > a')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done')