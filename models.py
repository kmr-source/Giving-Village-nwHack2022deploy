from enum import unique
from app import db
from sqlalchemy.sql import func 



class Shelter(db.Model):
    phoneNumber = db.Column(db.Integer, unique = True)
    location = db.Column(db.String(200), unique = True)
    hours = db.Column(db.Integer)

class Pantry(db.Model):
    location = db.Column(db.String(200), unique = True)
    hours = db.Column(db.Integer)
    