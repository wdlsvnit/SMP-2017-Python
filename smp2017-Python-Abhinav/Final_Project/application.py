#TODO: Main application
from flask import Flask
from flask_script import Manager
from sql import SQL
from flask_bootstrap import Bootstrap
from flask_session import Session
from flask_mail import Mail

APP = Flask(__name__)

APP.config.from_pyfile('config.py')

MAIL = Mail(APP)
MANAGER = Manager(APP)
BOOTSTRAP = Bootstrap(APP)
SESSION = Session(APP)

if APP.config["DEBUG"]:
    @APP.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

db = SQL("sqlite:///fproj.db")

from views import *


if __name__=='__main__':
    #MANAGER.run()
    APP.run(debug=True)
