import json
import requests

from flask import Flask, render_template
from config_keys import api_key as api_key
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db =SQLAlchemy()
#DB_NAME = "database.db"

#engine = create_engine("http://127.0.0.1:5000/")
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

def init_db():
    with app.open_resource('schema.sql', model ="r") as f:
        db.cursor().executescript(f.read())
    db.commit()


if __name__ == '__main__':
    app.run(debug=True)
    #app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from models import Fridge, Pantry, Shelter

    db.create_all()
    db.session.commit()

