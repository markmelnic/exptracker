from api import db
from api.models import *

def get_people():
    return [{
    'id': p.id,
    'name': p.name,
    'share': p.share,
    } for p in People.query.all()]
