import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Logitech-Orion-Mechanical-Gaming-Keyboard/dp/B00N3OELPU/ref=sr_1_1?dchild=1&keywords=logitech+keyboard&qid=1587919640&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup.prettify(), 'html.parser')
title = soup2.find(id='productTitle').get_text()
print(title)