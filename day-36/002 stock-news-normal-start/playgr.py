import datetime
from datetime import timedelta
import requests

day_now = datetime.datetime.now()
day_yest = day_now - timedelta(days=1)
day_b_yest = day_yest - timedelta(days=1)
day_yest = day_yest.strftime("%Y-%m-%d")
day_b_yest = day_b_yest.strftime("%Y-%m-%d")


api_key_news = "5c06174138434417b9fd04a6a93e95b0"

parameters = {
    "apikey": api_key_news,
    "sortBy": "popularity",
    "from": day_b_yest,
    "to": day_yest,
    "pageSize": 3,
    "q": "Tesla Inc.",
}


response = requests.get('https://newsapi.org/v2/everything', params=parameters)
response.raise_for_status()

get_data = response.json()
for i in range (0, 3):
    print(get_data["articles"][i]["titles"])
    print("\n\n")

