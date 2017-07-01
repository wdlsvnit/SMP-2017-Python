#TODO: Main application
from flask import Flask
from flask_script import Manager
from sql import SQL
from flask_bootstrap import Bootstrap

APP = Flask(__name__)
MANAGER = Manager(APP)
BOOTSTRAP = Bootstrap(APP)
APP.config.from_pyfile('config.py')

db = SQL("sqlite:///fproj.db")

from views import *


if __name__=='__main__':
    #MANAGER.run()
    APP.run(debug=True)

#pylint: disable=invalid-name
'''disables pylint constant name error'''

'''import os
from flask import Flask, redirect, session, render_template, url_for, flash
from flask_bootstrap import Bootstrap
from helpers import init, SQL
from flask_mail import Mail


init()
app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
app.config['SECRET_KEY'] = os.environ['secret_key']
db = SQL("sqlite:///fproj.db")

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    docstring
    form = forms()
    if form.validate_on_submit():
        if session.get('name') != form.name.data:
            flash("Name changed")
        session['name'] = form.name.data
        db.execute("INSERT INTO test VALUES (:name)", name=form.name.data)
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template("index.html", form=form, name=session.get('name'))

if __name__ == "__main__":
    manager.run()
    #app.run(debug=True)
 '''