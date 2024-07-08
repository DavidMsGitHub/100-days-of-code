import requests

natural_language_endpoint = "v2/natural/exercise"

n_api_key = "2ed1af5c8277c96712e93b8b10b7f213"
n_user_id = "66278872"

nutritionix_endpoint = "https://trackapi.nutritionix.com/"


headers = {
    "x-app-key": n_api_key,
    "x-app-id": n_user_id
}

parameters = {
    "query": "I ran 5 mile",
    "weight_kg": 81,
    "height_cm": 184,
    "age": 17
}

request = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
request.raise_for_status()
gela = request.json()
print(gela)