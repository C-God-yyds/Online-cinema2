from flask import jsonify

from db import db_handler


def all():
    sql="select * from video_info"
    a=db_handler.select(sql)
    return jsonify(a)

def classification(params={}):
    sql="select * from video_info where classification_id = ''"
    return db_handler.select(sql,params)

def language(params={}):
    sql="select * from video_info where language_id = ''"
    return db_handler.select(sql,params)

def type(params={}):
    sql="select * from video_info where video_type_id = ''"
    return db_handler.select(sql,params)

def district(params={}):
    sql="select * from video_info where district_id = ''"
    return db_handler.select(sql,params)