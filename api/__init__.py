import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

db = SQLAlchemy(app)

from .models import *

db.create_all()
db.session.commit()

from . import routes
