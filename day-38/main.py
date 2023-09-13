import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT = "50"
HEIGHT = "164.5"
AGE = "21"
exercise_text = input("Tell me which exercises you did ")

APP_ID = os.environ['APP_ID']
API_KEY = os.environ["API_KEY"]
nutrition_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ['sheety_endpoint']

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_config = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=nutrition_endpoint, json=exercise_config, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=())
    print(response.json())
