from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from werkzeug.security import check_password_hash
from sqlalchemy import text
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form.get('user').upper()
        password = request.form.get('password')

        if len(username) == 0:
            flash("Please enter Username", category="error")

        elif len(password) == 0:
            flash("Please enter Password", category="error")

        else:

            sql = text("select * from users where username = '"+username+"'")
            result = db.execute(sql)

            user_row = result.first()

            if user_row and check_password_hash(user_row["password"], password):
                session["username"] = user_row["username"]
                return redirect(url_for('views.adminPage'))
            else:
                flash("User Name/Password Not Found", category="error")

    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "logout"
