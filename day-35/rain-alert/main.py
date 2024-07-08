import requests
import msgsender
import os

api_key = "a4bec3040dc63aae8ab6b00e9bcd9b73"
MY_LAT = 41.786201 # Your latitude
MY_LONG = 44.802193
parameters = {
    "lat": MY_LAT,
    "lon":  MY_LONG,
    "appid": api_key,
    "exclude": "daily,minutely,current"
}

weather_data = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
weather_data.raise_for_status()
weather_info = weather_data.json()

for i in range(0,13):
    amindi_status = weather_info["hourly"][i]["weather"]
    amindi_status_id = amindi_status[0]["id"]
    if amindi_status_id < 700:
        msgsender.send_rain_message()