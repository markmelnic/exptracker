from flask import jsonify, request

from . import app
from api import db
from api.models import *
from api.utils import *

@app.route("/")
def main():
    return jsonify({"status": "Whatever"})

@app.route("/people")
def people():
    return jsonify(get_people())

@app.route("/add_user", methods=['POST'])
def add_user():
    person = request.get_json()
    entry = People(
        name = person['name'],
        share = person['share']
    )
    db.session.add(entry)
    db.session.commit()
    return jsonify(get_people())
