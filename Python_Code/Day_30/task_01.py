import dotenv
import os
from newsapi import NewsApiClient
import requests
import smtplib


dotenv.load_dotenv()
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines/sources"
COMPANY_NAME = "Tesla Inc"

api_key = os.getenv("NEWS_API_KEY")
news_param = {
    "apikey": api_key,
    "aInTitle": COMPANY_NAME,
}

news_responce = requests.get(NEWS_ENDPOINT, news_param)

articles = news_responce.json()["sources"]

frist_three_articles = articles[:3]

# for article in frist_three_articles:
#     heading = article["id"]
#     description = article["description"]


#     print(heading)
#     print(description)
# print(frist_three_articles)

formated_artical = [f"Heading: {article['name']} \nBrife: {article['description']} \n\nSee for more: {article['url']}" for article in frist_three_articles]
# print(formated_artical)

with smtplib.SMTP(host="smtp.gmail.com", port=587, timeout=5) as connection:
    connection.ehlo()
    connection.starttls()
    connection.ehlo()
    connection.login(user="saumitrapal44@gmail.com", password="kovj hrxh ojgt sust ")
    for article in formated_artical:
        connection.sendmail(
            from_addr="saumitrapal44@gmail.com", 
            to_addrs="saumitra31415926@gmail.com", 
            msg=f"Subject: Stock Alert\n\n{article}",
            )
    print("email send successfully")