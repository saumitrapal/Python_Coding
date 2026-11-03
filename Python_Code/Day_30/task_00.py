import requests
import os
import dotenv
import datetime

dotenv.load_dotenv()

api_key = os.getenv("STOCK_API_KEY")

stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": api_key,
}

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo


url = 'https://www.alphavantage.co/query'
responce = requests.get(url, params=stock_parameter)
data = responce.json()['Time Series (Daily)']
# print(responce.json())

data_list = [value for (key, value) in data.items()]

# print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_data = data_list[1]
day_before_data_closing_price = day_before_data["4. close"]
print(day_before_data_closing_price)


difference = abs(float(yesterday_closing_price) - float(day_before_data_closing_price))


difference_percentages = (difference / float(yesterday_closing_price)) * 100
print(difference_percentages)


if difference_percentages > 5:
    print('get_news')