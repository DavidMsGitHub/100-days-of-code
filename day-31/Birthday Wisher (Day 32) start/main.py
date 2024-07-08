import smtplib
import random as r
import datetime as dt

my_email = "dato2006213@gmail.com"
password = "beun zvmh vbmj rlvl"

connection = smtplib.SMTP('smtp.gmail.com', port=587)
connection.starttls()
connection.login(user=my_email, password=password)




time = dt.datetime.now()
if time.weekday() == 5:
    print("It is Tuesday")

    with open("quotes.txt", "r") as quotes:
        line = quotes.readlines()
        quote_to_send = line[r.randint(0, 101)]

    connection.sendmail(from_addr=my_email, to_addrs="iceobladey21@gmail.com", msg=f"Subject: Motivational Quote App\n\n {quote_to_send}")
    print(f"sent message")









# connection.close()
