from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from urllib.parse import quote_plus
from azure.appconfiguration import AzureAppConfigurationClient, ConfigurationSetting

import sys
import sqlalchemy
import os
import pyodbc
import website.file_upload

db = None


def create_app():
    global db
    app = Flask(__name__)

    # The config.txt file in generated on the server through the workflow using workflow secrets
    # A copy is also retained on my local pc for dev.  In an environment with dev, test and prod servers,
    # this config file could be different on each server and generated in the same way by each servers workflow
    config_file = open("config.txt", "r")

    # For convenience, setting the connection string to an environment variable.  Not really sure this step is
    # needed but the idea is that the connection string could be reused again from the environment variable instead
    # of making another call to the config service.
    os.environ['AZURE_APP_CONFIG_CONNECTION_STRING'] = config_file.read()

    # the connection string contains the connection requirements needed to connect to azure configuration services.
    # the configuration service allows me to create configurations that could be reused on other services.
    # it also simplifies the workflow as using the configuration service means that I don't have to handle a lot of
    # configuration setup when writing the workflow.
    connection_string = os.getenv('AZURE_APP_CONFIG_CONNECTION_STRING')

    # connecting to configuration service
    app_config_client = AzureAppConfigurationClient.from_connection_string(
        connection_string)

    # connecting to database
    params = quote_plus(app_config_client.get_configuration_setting(
        key='db_connection_string').value)

    db = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

    # Setting the secret key for flask.
    secret_key_var = app_config_client.get_configuration_setting(
        key='secret_flask_key').value

    app.config['SECRET_KEY'] = secret_key_var

    # Setting up routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, urlprefix='/')
    app.register_blueprint(auth, urlprefix='/')

    return app
