import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('SompoD.txt', 'wb')
for chr in res.iter_content(100000):
    playFile.write(chr)
playFile.close()