import requests
import datetime

USERNAME = "user1"
TOKEN = "asdfasdndsujfef"
GRAPH_ID = "graph-1"

current_time = datetime.datetime.now()
# current data in the format of 20261105
current_date = current_time.strftime("%Y%m%d")


PIXELA_USERS_ENDPOINT = "https://pixe.la/api/v1/users"
PIXELA_GRAPHS_ENDPOINT = f"{PIXELA_USERS_ENDPOINT}/{USERNAME}/graphs"
PIXELA_CREATION_ENDPOINT = f"{PIXELA_USERS_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PIXELA_EDIT_ENDPOINT = f"{PIXELA_USERS_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{current_date}"
PIXELA_DELETE_ENDPOINT = f"{PIXELA_USERS_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{current_date}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "kilogram",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_data_params = {
    "date": current_date,
    "quantity": input("How many kilometer did you cycle today? ")
}

pixel_edit_params = {
    "quantity": "9.54",
    "optionData": None
}

# responce = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(responce.text)

# responce = requests.post(url=PIXELA_GRAPHS_ENDPOINT, json=graph_params, headers=headers)
# print(responce.text)

# responce = requests.post(url=  PIXELA_CREATION_ENDPOINT, json=pixel_data_params, headers=headers)
# print(responce.text)

# responce = requests.put(url=PIXELA_EDIT_ENDPOINT, json=pixel_edit_params, headers=headers)
# print(responce.text)

responce = requests.delete(url=PIXELA_DELETE_ENDPOINT, headers=headers)
print(responce.text)

