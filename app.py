import json
import requests

from flask import Flask, render_template
from config_keys import api_key as api_key
from flask_sqlalchemy import SQLAlchemy
from os import path

db =SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    address = "89 Nelson Street"
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/json?key={api_key}&address={address}"
    req = requests.get(endpoint)
    data = json.loads(req.content)
    return render_template('map.html', api_key=api_key)


@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    json_data = requests.get.args('json')
    return json_data



if __name__ == '__main__':
    app.run(debug=True)
    #app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from models import Fridge, Pantry, Shelter

    db.create_all()

