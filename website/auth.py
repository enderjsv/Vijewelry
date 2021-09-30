from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash
from sqlalchemy import text
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        print(request.form)

        user = request.form.get('user')
        password = request.form.get('password')

        if len(user) == 0:
            flash("Please enter Username", category="error")

        if len(password) == 0:
            flash("Please enter Password", category="error")

        sql = text("select * from users where username = '"+user+"'")
        result = db.execute(sql)

    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "logout"
