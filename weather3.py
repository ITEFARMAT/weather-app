import pyowm


owm = pyowm.OWM('0ee2901c608957da0c713e92d1429b71')
observation = owm.weather_at_place('Poznań,PL')
weather = observation.get_weather()
temperature = weather.get_temperature('fahrenheit')['temp']

fahrenheitAfterConversation = (int(temperature) - 32) * 5/9

print(
    f'Aktualna temepratura w Poznaniu to: {int(fahrenheitAfterConversation)}°C ')
