
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy import text
from urllib.parse import quote_plus
from azure.appconfiguration import AzureAppConfigurationClient, ConfigurationSetting

import sys
import sqlalchemy
import os
import pyodbc

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
    return render_template("index.html")


@app.route("/testingGround/")
def testingGround():
    sql = text("select * from test_table")
    result = db.execute(sql)
    return render_template("testingGround.html", result=result)
