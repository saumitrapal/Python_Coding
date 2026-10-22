import requests
import datetime
import smtplib
import time
import dotenv
import os

dotenv.load_dotenv()

MY_LAT = 20.593683
MY_LONG = 20.593683
MY_EMAIL = os.getenv("EMAIL")
MY_EMAIL_PASSWORD = os.getenv("PASSWORD")
SEND_EMAIL = os.getenv("SENDER_EMAIL")


def is_iss_overhead():
    iss_api = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_latitude = float(iss_api.json()["iss_position"]["latitude"])
    iss_longitue = float(iss_api.json()["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitue <= MY_LONG+5:
        return True
    
def is_dark():
    my_data_dict = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    responce = requests.get(url="https://api.sunrise-sunset.org/json", params=my_data_dict)
    responce.raise_for_status()
    sunrise_hour = int(responce.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(responce.json()["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now().hour
    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead and is_dark:
        connection = smtplib.SMTP(host="smtp.gmail.com", port=587, timeout=5)
        connection.ehlo()
        connection.starttls()
        connection.ehlo()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=SEND_EMAIL,
                            msg="Subject: LOOK UP\n\n The ISS is above you in the sky."
                            )
        print("Email send successfully.")