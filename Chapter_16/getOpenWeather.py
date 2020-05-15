import sys, json, requests

APPID = 'edbd059d790f3b34c1538cbd07439d40'

# Compute location from command line
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name 2_letter_country_code')
city = ' '.join(sys.argv[1:])


#Download JSON data from OpenWeathermap.org's API
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={APPID}'
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)
w = weatherData
print(w)


print(f"Current weather in {city}: ")
print(f"Current temp: {w['main']['temp']} degree F.")
print(f"current feel: {w['main']['feels_like']} degree F.")