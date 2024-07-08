import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 41.786201 # Your latitude
MY_LONG = 44.802193 # Your longitude


#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def check():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    my_email = "dato2006213@gmail.com"
    password = "beun zvmh vbmj rlvl"
    connection = smtplib.SMTP('smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    if iss_latitude >= MY_LAT -5 and iss_latitude <= MY_LAT+5 and iss_longitude >= MY_LONG-5 and iss_longitude <= MY_LONG+5:
        if time_now.hour > sunset and time_now.hour < sunrise:
            print("Here we go ISS is near, sending email...")
            connection.sendmail(from_addr=my_email, to_addrs="iceobladey21@gmail.com", msg=f"Subject: ISS Arrived\n\n Look Up bro ISS is near you <3 ")
        else:
            print("ISS Is near but it's not night time so not sending")
    else:
        print("ISS Is not near bro")
        print(f"ISS Longitude: {iss_longitude} Your Longitude: {MY_LONG}\n ISS Latitude: {iss_latitude} Your Latitude: {MY_LAT}")

while True:
    check()