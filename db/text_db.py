from flask import jsonify

from db import db_handler


def text_all():
    sql="select * from menu where menu_level='1'"
    data=db_handler.select(sql)
    return jsonify(data)