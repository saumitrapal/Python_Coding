import requests

APP_ENDPOINT="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
APP_ID=""
NUTRITION_API_KEY=""
SHETTY_API_KEY=f"https://api.sheety.co/{SHETTY_API_KEY}/exerciseTracker/sheet1"

shetty_data = {
  "sheet1": {
	"name": "Syed K",
	"email": "syed@gmail.com"
  }
} 

# responce = requests.post(url=SHETTY_API_KEY,data="POST", json=shetty_data)
# print(responce.text)

# print(responce.status_code)



data_parameter = {
  "query": input("Tell me which exercises you did: "),
  "weight_kg": 70,                  # Optional: Weight in kg (1-500)
  "height_cm": 175,                 # Optional: Height in cm (1-300)
  "age": 30,                        # Optional: Age (1-150)
  "gender": "male"                  # Optional: "male" or "female"
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITION_API_KEY,
}

responce = requests.post(url=APP_ENDPOINT, json=data_parameter, headers=header)
responce_dict = responce.json()

print(responce_dict)

query_text = responce_dict['exercises'][0]['user_input']
weight_text = responce_dict['exercises'][0]['duration_min']
height_text = responce_dict['exercises'][0]['nf_calories']
movement_text = responce_dict['exercises'][0]['name']

print(query_text)
print(weight_text)
print(height_text)
print(movement_text)

