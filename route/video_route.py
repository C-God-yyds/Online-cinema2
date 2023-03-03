# -*- coding: utf-8 -*-
# author lby
import os
from uuid import uuid4

from flask import Blueprint, send_from_directory, request, send_file, render_template

from core import video_core
from demo.main import exccute_cmd

video = Blueprint("video", __name__)


@video.route("/index.html")
def index_html():
    return send_from_directory("static","index.html")


@video.route("/type/id", methods=["GET", "POST"])
def type_id():
    # ajax的请求参数，request.form，是dict
    res = video_core.type_id(request.form)
    # res 是menu_core返回的，是用jsonify转换的json，里面不光是json，还有response对象
    print(res.json)
    return res


@video.route("/pic/<pic>")
def pic_path(pic):
    print(pic)
    return send_file(pic)




BASE_DIR = os.path.dirname(os.path.abspath(__file__)).replace("route", "")


# 上传影音文件
@video.route("/receive_audio", methods=["POST"])
def receive_audio():
    file = request.files.get("audio")
    if file:
        filename = "1.m4a"#uuid4()
        filepath = os.path.join(BASE_DIR, "data", filename)
        file.save(filepath)
        print(filepath)
        return {"code": 200, "filename": filename}
    return {"code": 201, "msg": "上传失败"}

# @video.route("/a", methods=["POST"])
# def show():
#     return render_template('demo.html')
# 加载影音文件
@video.route("/get_audio/<filename>")
def get_audio(filename):
    print(os.path.join(BASE_DIR, "data", filename))
    return send_file(os.path.join(BASE_DIR, "data", filename))

@video.route("/1")
def video1():
    return send_from_directory("static", "demo.html")

@video.route("/2", methods=['GET', 'POST'])
def Hello():
    #message = "hello"
    return exccute_cmd()


