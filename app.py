import json
import requests

from flask import Flask, render_template
from config_keys import api_key as api_key

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    address = "89 Nelson Street"
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/json?key={api_key}&address={address}"
    req = requests.get(endpoint)
    data = json.loads(req.content)
    return render_template('map.html', data=data)


@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    json_data = requests.get.args('json')
    return json_data


if __name__ == '__main__':
    app.run(debug=True)
