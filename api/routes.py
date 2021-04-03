from flask import jsonify

from . import app

@app.route("/")
def main():
    return jsonify({"status": "Whatever"})
