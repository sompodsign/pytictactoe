import os, bs4, requests, sys

def imgurDownload(ext):

    url = 'https://imgur.com/search?q=' + ext
    os.makedirs('imgur', exist_ok=True)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    imageElem = soup.select('.post > .image-list-link img')

    for i in range(len(imageElem)):
         # convert image URL thumbnail size to fullsize version
        image_url_s = 'https:' + imageElem[i].get('src')

        print('Donloading image {}.'.format(image_url_s))
        res = requests.get(image_url_s)
        res.raise_for_status()

        imageFile = open(os.path.join('imgur', os.path.basename(image_url_s)),'wb')

        for chunk in res.iter_content(100000):
             imageFile.write(chunk)
        imageFile.close()
    print('Done')

imgurDownload(sys.argv[1])
