import dotenv
import os
import requests
import smtplib

dotenv.load_dotenv()

api_key = os.getenv("API_KEY")
my_latitude = os.getenv("MY_LATITUDE")
my_longitude = os.getenv("MY_LONGITUDE")

my_email = os.getenv("MY_EMAIL")
my_email_password = os.getenv("MY_EMAIL_PASSWORD")
to_email = os.getenv("TO_EMAIL")


url_parameter = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": api_key,
    "cnt": 4,
}

responce = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=url_parameter)

# print(responce.json())
# print(responce.json()["list"][2]["weather"][0])
# print(responce.json()["list"][2]["weather"][0]["description"])

weather_word = 'weather'
id_list = []
will_rain = False
number = 700
weather_data = responce.json()

for i in range(0, 4):
    for weather_word in weather_data['list'][i]['weather']:
        id_list.append(weather_word['id'])
        for id in id_list:
            if id < number:
                will_rain = True
if will_rain:
    # print("Bring An Umbrella.")
    connection = smtplib.SMTP(host="smtp.gmail.com", port=587, timeout=5)
    connection.ehlo()
    connection.starttls()
    connection.ehlo()
    connection.login(user=my_email, password=my_email_password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=to_email, 
                        msg=f"Subject: Weather Update\n\nIt's going to rain today.\nRemember to bring an umbrella."
                        )
    print("Email send successfully.")
    


# print(type(responce.json()["list"]))
# print(responce.json()['list'][2]["weather"])