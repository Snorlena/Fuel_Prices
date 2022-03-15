import requests
import json

response = requests.get(
    'https://www.st1.se/fuel/stationPrices/pricesPerStation/'
)

data = response.text

parsed = json.loads(data)["data"]["station_prices"]
updated_at = json.loads(data)["data"]["updated_at"]

for keys in parsed:
    print()
    print(parsed[keys]["name"])
    print("E10", parsed[keys]["prices"]["b95"]["price_with_tax"],
    "    Diesel", parsed[keys]["prices"]["diesel"]["price_with_tax"],
    "    E85", parsed[keys]["prices"]["e85"]["price_with_tax"])

print()
print("Updated at",updated_at)