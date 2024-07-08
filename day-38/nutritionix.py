import requests
import sheetsy
import datetime

n_api_key = "2ed1af5c8277c96712e93b8b10b7f213"
n_user_id = "66278872"

player_query = input("what you did today?: ")


headers = {
    "x-app-key": n_api_key,
    "x-app-id": n_user_id,
    "Content-Type": "application/json"
}

parameters = {
    "query": player_query,
    "weight_kg": 81,
    "height_cm": 184,
    "age": 17
}

request = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
request.raise_for_status()
gela = request.json()
print(gela)


the_workout_data = {
    "workout": {
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.datetime.now().strftime("%H:%M"),
        "exercise": (gela["exercises"][0]["user_input"]).title(),
        "duration": f"{gela["exercises"][0]["duration_min"]} minutes",
        "calories": gela["exercises"][0]["nf_calories"]
    }
}


post_endpoint = "https://api.sheety.co/baa35ba46d9a518aa8cbd06376d3727d/exercises/workouts"
workouts = requests.post(post_endpoint, json=the_workout_data)
workouts.raise_for_status()
print(workouts.text)