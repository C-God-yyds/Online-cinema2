from core.base_core import service
from db import info_db

def select_all():
    data = info_db.all()
    return data
@service
def classification(params={}):
    data = info_db.classification(params)
    return data
@service
def language(params={}):
    data = info_db.language(params)
    return data
@service
def type(params={}):
    data = info_db.type(params)
    return data
@service
def district(params={}):
    data = info_db.district(params)
    return data


