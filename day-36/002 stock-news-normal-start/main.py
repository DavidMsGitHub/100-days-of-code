import requests
from datetime import datetime, timedelta
from twilio.rest import Client

#-----#---------#-----------#-----#
def check_price():
    if day_yesterday_close > day_b_yesterday_close:
        return f"{STOCK_NAME} 🔺{percent_difference}%"
    else:
        return f"{STOCK_NAME} 🔻{percent_difference}%"
#-----#---------#-----------#-----#

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key_stock = "DM2FIBI716YLDNF7"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


parameters = {
    "function": "TIME_SERIES_DAILY",
    "apikey": api_key_stock,
    "symbol": STOCK_NAME,

}
stocksy_api = requests.get(STOCK_ENDPOINT, params=parameters)
stocks = stocksy_api.json()

day_now = datetime.now()
day_yest_full = day_now - timedelta(days=1)
day_before_yest_full = day_yest_full - timedelta(days=1)

day_yesterday = day_yest_full.strftime("%Y-%m-%d")
day_b_yesterday = day_before_yest_full.strftime("%Y-%m-%d")

day_yesterday_close = stocks["Time Series (Daily)"][day_yesterday]["4. close"]
day_b_yesterday_close = stocks["Time Series (Daily)"][day_b_yesterday]["4. close"]

pos_diff = float(day_yesterday_close) - float(day_b_yesterday_close)
pos_diff_abs = abs(pos_diff)

percent_difference = round((pos_diff/float(day_b_yesterday_close))*100, 3)



# news nawili

api_key_news = "5c06174138434417b9fd04a6a93e95b0"

parameters = {
    "apikey": api_key_news,
    "sortBy": "relevancy",
    "from": day_b_yesterday,
    "to": day_yesterday,
    "pageSize": 3,
    "q": "Tesla Inc.",
}
response = requests.get(NEWS_ENDPOINT, params=parameters)
response.raise_for_status()

if percent_difference >= 2:
    get_data = response.json()
    first_three_articles = get_data["articles"][:3]

    list_of_news = [f"HeadLine: {article["title"]}\n\nBrief: {article["description"]}" for article in first_three_articles]

    account_sid = 'AC68fb2ed945063898a8b833ce6723cfd3'
    auth_token = '29fb9bccd6fef386293c11261f9c91aa'
    client = Client(account_sid, auth_token)
    price_checker = check_price()

    for i in range(0, 3):
        message = client.messages.create(
          from_='+12255905385',
          body = f"{check_price()}\n\n"
                 f"{list_of_news[i]}",
          to='+995599544130'
        )
