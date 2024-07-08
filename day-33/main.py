import requests
import datetime


parameters = {
    "lat": 41.786201,
    "lng": 44.802193,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise[11:19])

time_now = datetime.datetime.now()

print(time_now)