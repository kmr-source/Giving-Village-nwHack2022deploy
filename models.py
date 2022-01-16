from enum import unique
from app import db
from sqlalchemy.sql import func 



class Shelter(db.Model):
    shelterName = db.Column(db.String(1000))
    phoneNumber = db.Column(db.Integer, unique = True)
    location = db.Column(db.String(200), unique = True)
    hours = db.Column(db.Integer)

class Pantry(db.Model):
    location = db.Column(db.String(200), unique = True)
    hours = db.Column(db.Integer)

class Fridge(db.Model):
    location = db.Column(db.String(200), unique =True)
    hours = db.Column(db.Integer)

    