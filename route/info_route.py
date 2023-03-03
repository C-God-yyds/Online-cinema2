from flask import Blueprint
from core import info_core

info = Blueprint("info", __name__)


@info.route("/all", methods=["GET", "POST"])
def select_all():
    res = info_core.select_all()
    print(res.json)
    return res

@info.route("/classification", methods=["GET", "POST"])
def classification():
    res = info_core.classification()
    print(res.json)
    return res

@info.route("/language", methods=["GET", "POST"])
def language():
    res = info_core.language()
    print(res.json)
    return res

@info.route("/type", methods=["GET", "POST"])
def type():
    res = info_core.type()
    print(res.json)
    return res

@info.route("/district", methods=["GET", "POST"])
def district():
    res = info_core.district()
    print(res.json)
    return res
