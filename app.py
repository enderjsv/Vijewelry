
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy import text
from urllib.parse import quote_plus
from azure.appconfiguration import AzureAppConfigurationClient, ConfigurationSetting

import sys
import sqlalchemy
import os
import pyodbc

errfile = open("error_log.txt", "r+")
errfile.truncate(0)
errfile.close

app = Flask(__name__)
config_file = open("config.txt", "r")

os.environ['AZURE_APP_CONFIG_CONNECTION_STRING'] = config_file.read()

connection_string = os.getenv('AZURE_APP_CONFIG_CONNECTION_STRING')
app_config_client = AzureAppConfigurationClient.from_connection_string(
    connection_string)
params = quote_plus(app_config_client.get_configuration_setting(
    key='db_connection_string').value)

db = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))


@app.route("/")
def index():

    try:
        sql = text("select * from test_table")
        result = db.execute(sql)
    except:
        e = sys.exc_info()[0]

        file1 = open("error_log.txt", "a")  # append mode
        file1.write("<p>Error: %s</p>" % e)
        file1.close()

    #result_string = ""

    # for row in result:
    #    result_string += row[0] + " "

    return "The params string is " + params
    # return (db.table_names()[0]+" "+result_string)
    # return render_template("index.html")


@app.route("/helloTest/")
def helloTest():
    sql = text("select * from test_table")
    result = db.execute(sql)
    return "HELLO"
