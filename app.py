import os

from flask import Flask, render_template
from config_keys import api_key as api_key
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

# connecting host to heroku
post = int(os.environ.get('Port', 5000))

DB_NAME = "database.db"
app = Flask(__name__)
# app.secret_key = "epic haxxxxx"
app.config['SQLACHEMY_DATABASE_URI'] = 'postgresql:///{DB_NAME}'
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

db = SQLAlchemy(app)


class Resource(db.Model):
    """
    A resource that is 100% free.
    """
    __abstract__ = True
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    id_key = db.Column(db.String(100), unique=True, primary_key=True)
    img = db.Column(db.String(100))
    hrs = db.Column(db.String)
    description = db.Column(db.String(1000))

    # isFreeLibrary, bool

    def __init__(self, location, name=None, img=None, hrs="24/7", description=None):
        self.name = name
        self.location = location
        self.id_key = uuid4()
        self.img = img
        self.hrs = hrs
        self.description = description

    def serialize(self):
        return {"name": self.name, "location": self.location, "description": self.description, "hrs": self.hrs}


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
    def __init__(self, facility_info, location, name=None, img=None, hrs="24/7", description=None):
        super().__init__(location, name=name, img=img, hrs=hrs, description=description)
        self.facility_info = facility_info

    def serialize(self):
        data = super().serialize()
        data["facility_info"] = self.facility_info
        return data


class Fridge(Resource):
    """
    Represents a community fridge.
    Contains information about if there is a freezer or pantry section.
    """
    fridge_info = db.Column(db.String)

    def __init__(self, fridge_info, location, name=None, img=None, hrs="24/7", description=None):
        super().__init__(location, name=name, img=img, hrs=hrs, description=description)
        self.fridge_info = fridge_info

    def serialize(self):
        data = super().serialize()
        data["fridge_info"] = self.fridge_info
        return data


class Pantry(Resource):
    """
    Represents free pantries with hygienic products or groceries.
    """
    website = db.Column(db.String)
    social_media = db.Column(db.String)

    def __init__(self, location, social_media=None, website=None, name=None, img=None, hrs="24/7", description=None):
        super().__init__(location, name=name, img=img, hrs=hrs, description=description)
        self.website = website
        self.social_media = social_media

    def serialize(self):
        data = super().serialize()
        data["website"] = self.website
        data["social_media"] = self.social_media
        return data


# db.create_all()

fridge_data = [
    Fridge("Full fridge, freezer, pantry",
           "29 West Hastings Street",
           name="Vancouver Women's Health Collective",
           hrs="11am - 7pm weekdays",
           description="Community fridge located within the building; folks have to be buzzed in"),
    Fridge("Full fridge, freezer, pantry, accepts home cooked meals",
           "29 West Hastings Street",
           name="Vancouver Women's Health Collective",
           description="This fridge is located in the alley behind the green house"),
    Fridge("Full fridge, freezer, pantry",
           "29 West Hastings Street",
           name="Vancouver Women's Health Collective",
           description="This fridge is located in the alley behind the blue house"
           ),
    Fridge("Full fridge, freezer, pantry",
           "340 West 2nd Avenue, Vancouver, BC",
           name="Food Stash Foundation",
           description="This fridge is located in the alley behind the blue house"
           ),
    Fridge("Full fridge, freezer, pantry",
           "3718 Main Street, Vancouver, BC",
           name="The Soap Dispensary & Kitchen Staples",
           description="Located in the heart of Main Street!",
           img="https://scontent-sea1-1.xx.fbcdn.net/v/t39.30808-6/215763969_288689355954978_4168483443270479323_n.jpg?"
               "_nc_cat=103&ccb=1-5&_nc_sid=a26aad&_nc_ohc=AxakfH4qk_oAX9X7fwp&_nc_ht=scontent-sea1-1.xx&oh=00_AT9WT2xN7"
               "LUFOVRY1e3RePpD1Fq2gX-igzwKqOq97zde0g&oe=61E81965"),
]

pantry_data = [
    Pantry(
        "E 6th street, Vancouver, BC",
        social_media="@van.periodpantry",
        description="Located between Commercial & Victoria. E-transfer donations to vancouver.periodpantry@gmail.com",
        name="Vancouver Period Pantry",
        website="https://linktr.ee/van.periodpantry"
    ),
    Pantry(
        "1410 W 72nd Ave, Vancouver, BC V6P 3C7",
        social_media="@freepantrymarpole",
        description="Take What You Need, Give What You Can",
        name="Marpole Little Free Pantry",
        website="https://connect4219.wixsite.com/marpolemutualaid"
    ),
    Pantry(
        "2125 Victoria Dr, Vancouver, BC V5N 5Y4",
        social_media="@little_free_pantry",
        description="Take What You Need, Give What You Can",
        name="McSpadden Little Free Pantry",
        website="https://www.flyingzucchini.ca/"
    )
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fridges')
def fridges():
    data = {"fridges": []}
    for fridge in fridge_data:
        data["fridges"].append(fridge.serialize())

    return render_template('fridge.html', api_key=api_key, data=data)


@app.route('/pantries')
def pantries():
    data = {"pantries": []}
    for pantry in pantry_data:
        data["pantries"].append(pantry.serialize())

    return render_template('pantry.html', api_key=api_key, data=data)


if __name__ == '__main__':
    # comment out orginal code to test out heroku
    # app.run()
    #  db.init_app(app)
    app.run(host='0.0.0.0', port=post, debug=True)
