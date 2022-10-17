from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():

    response = requests.get(
        'https://www.st1.se/fuel/stationPrices/pricesPerStation/'
    )

    data = response.text

    parsed = json.loads(data)["data"]["station_prices"]
    updated_at = json.loads(data)["data"]["updated_at"]

    stations = {}

    for keys in parsed:
        newName = parsed[keys]["name"].strip("St1")
        stations[parsed[keys]["name"]] = newName,[parsed[keys]["prices"]["b95"]["price_with_tax"],parsed[keys]["prices"]["diesel"]["price_with_tax"],parsed[keys]["prices"]["e85"]["price_with_tax"]]

    return render_template('index.html', stations=stations, updated_at=updated_at)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
