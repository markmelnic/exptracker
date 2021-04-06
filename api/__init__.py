import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)

db = SQLAlchemy(app)

from .models import *

db.create_all()
db.session.commit()

from . import routes
