import json
import requests
import datetime
from os.path import exists, expanduser

conf_dir = expanduser("~/.config/weather_conf.json")

if exists(conf_dir):
    with open(conf_dir, "r") as f:
        data = json.load(f)
    zipcode = data["zipcode"]
    key = data["key"]
else:
    x = {"zipcode": input("Enter a zip code: "), "key": input("Enter an OpenWeatherMap api key: ")}
    with open(conf_dir, "w") as f:
        json.dump(x, f)
    zipcode = x["zipcode"]
    key = x["key"]

j = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={key}&units=imperial")
j = j.json()

x = datetime.datetime.now()
date = "Today is " + x.strftime("%A") + ", " + x.strftime("%B") + " " + x.strftime("%d")

temp = j["main"]["temp"]
weatherId = j["weather"][0]["id"]
wid = j["weather"][0]["id"]
description = j["weather"][0]["description"]

weather_group = int(weatherId/100)

if weather_group == 2:
    weatherId = ""
elif weather_group == 3:
    weatherId = "殺"
elif weather_group == 5:
    weatherId = ""
elif weather_group == 6:
    weatherId = ""
elif weather_group == 7:
    weatherId = ""
elif weatherId == 800:
    weatherId = ""
elif (weatherId >= 801) and (weatherId < 805):
    weatherId = ""

print(f"{date}, it is currently {temp}°F, with a {description} {weatherId}.")
