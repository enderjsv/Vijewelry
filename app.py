
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy import text
from urllib.parse import quote_plus

import sqlalchemy

app = Flask(__name__)

try:
    config = open("config.txt")
    params = quote_plus(config.read())

    db = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

except OSError:
    pass


@app.route("/")
def index():

    sql = text("select * from test_table")
    result = db.execute(sql)
    result_string = ""

    for row in result:
        result_string += row[0] + " "

    return (db.table_names()[0]+" "+result_string)
    # return render_template("index.html")
