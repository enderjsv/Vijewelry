
from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy import text
from urllib.parse import quote_plus
from azure.appconfiguration import AzureAppConfigurationClient, ConfigurationSetting

import sqlalchemy
import os

app = Flask(__name__)
config_file = open("config.txt", "r")

os.environ['AZURE_APP_CONFIG_CONNECTION_STRING'] = config_file.read()

connection_string = os.getenv('AZURE_APP_CONFIG_CONNECTION_STRING')
# app_config_client = AzureAppConfigurationClient.from_connection_string(
#    connection_string)
# params = quote_plus(app_config_client.get_configuration_setting(
#    key='db_connection_string').value)

#db = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))


@app.route("/")
def index():

    #sql = text("select * from test_table")
    #result = db.execute(sql)
    #result_string = ""

    # for row in result:
    #    result_string += row[0] + " "

    return "The connection string is " + connection_string
    # return (db.table_names()[0]+" "+result_string)
    # return render_template("index.html")


@app.route("/helloTest/")
def helloTest():
    return "HELLO"
