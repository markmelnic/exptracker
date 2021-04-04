from api import db

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, default="")
    share = db.Column(db.Integer, default="")
