import requests
import time

responce = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(responce.raise_for_status)
# print(responce.json())
data = responce.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

tuple_data = (longitude, latitude)
print(tuple_data)
