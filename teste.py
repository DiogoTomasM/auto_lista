import requests
import json

id = "117667552"
url = f"https://api.opendota.com/api/players/{id}"
response = requests.get(url)
data = response.json()
player_id = data['profile']['account_id']
print(player_id)