#TODO: Views
from application import APP
from flask import redirect, session, render_template, url_for, flash
from flask_bootstrap import Bootstrap
from forms import LoginForm

bootstrap = Bootstrap(APP)

@APP.route('/', methods = ['GET','POST'])
def index():
    '''index'''
    form = LoginForm()
    if form.validate_on_submit():
        flash("Submitted") #{}".format(form.username.data))
        return render_template("index.html")
    return render_template('login.html', form = form)
