import json
import requests

from flask import Flask, render_template
from config_keys import api_key as api_key
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "database.db"
app = Flask(__name__)
app.secret_key = "epic haxxxxx"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

db = SQLAlchemy(app)


class Resource(db.Model):
    """
    A resource that is 100% free.
    """
    __abstract__ = True
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    id = db.Column(db.String(100), unique=True)
    img = db.Column(db.String(100))
    hrs = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    # isFreeLibrary, bool


class Shelter(Resource):
    """
    Represents free shelter. This resource is to be taken from the opendata api.
    https://opendata.vancouver.ca/explore/dataset/homeless-shelter-locations/api/
    """
    facility_info = db.Column(db.PickleType)
    # ^ PICKLE TYPE: Holds Python objects, which are serialized using pickle.
    # PickleType builds upon the Binary type to apply Python’s pickle.dumps() to incoming objects,
    # and pickle.loads() on the way out, allowing any pickleable Python object to be stored as a
    # serialized binary field.
    # https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.PickleType


class Fridge(Resource):
    """
    Represents a community fridge.
    Contains information about if there is a freezer or pantry section.
    """
    fridge_info = db.Column(db.ARRAY)


class Pantry(Resource):
    """
    Represents free pantries with groceries.
    """
    website = db.Column(db.String)
    social_media = db.Column(db.String)


db.create_all()


# TEST CODE - example usage
# class users(db.Model):
#     _id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     email = db.Column(db.String(100))
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#
# @app.route('/dbtest')
# def testing():
#     tester_user = users("kat", "potato")
#     db.session.add(tester_user)
#     db.session.commit()
#     return f'<h1> added a test user </h1>'
#
#
# @app.route('/dbverifying')
# def verifying():
#     verified_username = "kat"
#     found = users.query.filter_by(name=verified_username).first()
#     return f'<h1> {found.email} </h1>'
#

@app.route('/', methods=['GET'])
def index():
    address = "89 Nelson Street"
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/json?key={api_key}&address={address}"
    req = requests.get(endpoint)
    data = json.loads(req.content)
    return render_template('index.html', api_key=api_key)


@app.route('/fridges')
def fridges():
    return render_template('map.html', api_key=api_key)


if __name__ == '__main__':
    app.run()
    # db.init_app(app)
