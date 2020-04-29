import requests
import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=28.56604489500006&lon=-81.68864878999995#.XqVjNGgzaHs')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')

print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())

period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temps = [item.find(class_= 'temp').get_text() for item in items]

print(period_names)
print(short_description)
print(temps)

weather_stuff = pd.DataFrame(
    {'period': period_names,
     'short_descriptions': short_description,
     'temperatures': temps,
     })

print(weather_stuff)

weather_stuff.to_csv('result.csv')