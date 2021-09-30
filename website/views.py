from flask import Blueprint, render_template, request, flash
from sqlalchemy import text, Table, MetaData, Column, Integer
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Users

import website.file_upload

views = Blueprint('views', __name__)


@views.route("/")
def index():
    return render_template("index.html")


@views.route("/testingGround/")
def testingGround():
    """admin = Users(user="admin", password=generate_password_hash(
        '1048', method='sha256'))
    guest = Users(user="guest", password=generate_password_hash(
        '1048', method='sha256'))

    db.session.add(admin)
    db.session.add(guest)
    db.commit"""

    sql = text("select * from users")
    result = db.execute(sql)
    return render_template("testingGround.html", result=result)


"""@views.route("/uploadFile")
def uploadFile():
    return render_template("file_upload.html")


@views.route("/saveFile", methods=['GET', 'POST'])
def saveFile():
    return file_upload.upload_file()


"""
