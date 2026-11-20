import dotenv
import os
import requests

dotenv.load_dotenv()

SHEETY_API = os.getenv("SHETTY_API_KEY")

HEADERS = {
    'Authorization': '',
    'Content-Type': 'application/json'
}


SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_API}/price/flighPrice"
responce = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS)
print(responce.json())



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass