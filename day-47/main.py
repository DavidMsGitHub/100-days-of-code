import requests
import bs4
import smtplib
import datetime
import time


my_email = "dato2006213@gmail.com"
password = "beun zvmh vbmj rlvl"
price_wanted = float(input("Input price you want it to be: "))
product_link = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

#EMAIL THING
connection = smtplib.SMTP('smtp.gmail.com', port=587)
connection.starttls()
connection.login(user=my_email, password=password)
###########----_-----_-_-_-_--_-__--_-_--#


while True:
    now = datetime.datetime.now()
    time.sleep(1)

    if now.hour == 14:
        headers = {
            "Accept-Language": "en-US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
        }

        response = requests.get(url=product_link, headers=headers)
        html = response.text

        soup = bs4.BeautifulSoup(html, "html.parser")

        product_name = soup.find(name="span", class_= ["a-size-large", "product-title-word-break"]).getText().strip()
        print(product_name)
        price_whole = soup.find(name= "span", class_="a-price-whole")
        price_fraction = soup.find(name= "span", class_="a-price-fraction")

        full_price = float(f"{price_whole.getText()}{price_fraction.getText()}")
        if full_price < price_wanted:
            connection.sendmail(from_addr=my_email, to_addrs="iceobladey21@gmail.com",
                                msg=f"Subject: Amazon Price Tracker Alert\n\n Hey I want to tell you that price on \n {product_name} \n is below ${price_wanted}\n Check it out here: {product_link}".encode('utf-8'))

        print(full_price)
    else:
        print(f" Not yet it's: {now.hour}:{now.minute}:{now.second}")


