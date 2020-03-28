import requests
import json
import pprint
import datetime


today_date = datetime.date.today()
print("Dziś jest: " + str(today_date))


city_name = "Poznan"


complete_url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=0ee2901c608957da0c713e92d1429b71" + "&q=" + city_name

response = requests.get(
    complete_url,)

x = response.json()
pprint.pprint(x)
