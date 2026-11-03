import requests
import os
import dotenv
import datetime
from newsapi import NewsApiClient
import smtplib

dotenv.load_dotenv()

stock_api_key = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines/sources"
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
COMPANY_NAME = "Tesla Inc"

stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": stock_api_key,
}
news_parameter = {
    "apikey": news_api_key,
    "aInTitle": COMPANY_NAME,
}

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
responce = requests.get(STOCK_ENDPOINT, params=stock_parameter)
data = responce.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_data = data_list[1]
day_before_data_closing_price = day_before_data["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_data_closing_price))
difference_percentages = (difference / float(yesterday_closing_price)) * 100
# print(difference_percentages)

if difference_percentages > 1:
    news_responce = requests.get(NEWS_ENDPOINT, news_parameter)
    articles = news_responce.json()["sources"]
    frist_three_articles = articles[:3]
    formated_artical = [f"Heading: {article['name']} \nBrife: {article['description']} \n\nSee for more: {article['url']}" for article in frist_three_articles]

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

