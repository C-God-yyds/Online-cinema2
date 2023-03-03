from flask import Blueprint
from core import text_core

text = Blueprint("text", __name__)


@text.route("/1", methods=["GET", "POST"])
def text_all():
    res = text_core.text_all()
    print(res.json)
    return res
