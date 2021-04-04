from flask import jsonify, request

from . import app
from api import db
from api.models import *
from api.utils import *

@app.route("/")
def main():
    return jsonify({"status": "Whatever"})

@app.route("/people", methods=['GET', 'POST', 'DELETE'])
def add_user():
    method = request.method
    if method == "POST": 
        person = request.get_json()
        entry = People(
            name = person['name'],
            share = person['share']
        )
        db.session.add(entry)
        db.session.commit()
    elif method == "DELETE":
        People.query.filter_by(id=request.get_json()["id"]).delete()
        db.session.commit()

    return jsonify(get_people())
