from flask import jsonify

from . import app

@app.route("/")
def main():
    return jsonify({"status": "Whatever"})

@app.route("/people")
def people():
    people = [
        {
        "id": 1,
        "name": "Mark",
        "share": 50
        },
        {
        "id": 2,
        "name": "Traian",
        "share": 50
        }
    ]
    return jsonify(people)
