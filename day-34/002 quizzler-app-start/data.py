import json
import requests

paramaters = {
    "type": "boolean",
    "amount": 10

}
api = requests.get("https://opentdb.com/api.php", params=paramaters)
api.raise_for_status()

question_data = api.json()["results"]
