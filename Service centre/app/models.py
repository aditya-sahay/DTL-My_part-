from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    vehicle_number = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
