#Todo Implement basic settings required by an app instance

import os
DEBUG = True
SECRET_KEY = "sjdasdjas"
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
SQLALCHEMY_DATABASE_URI = "sqlite:///fproj.db"
