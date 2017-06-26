#pylint: disable=invalid-name
'''disables pylint constant name error'''

from flask import Flask, redirect, session , render_template, url_for,flash
#from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 
from wtforms.validators import Required
from helpers import init, SQL
import os

init()
app = Flask(__name__)
bootstrap = Bootstrap(app)
#manager = Manager(app)
app.config['SECRET_KEY'] = os.environ['secret_key']
db = SQL("sqlite:///fproj.db")

class forms(FlaskForm):
    '''a form'''
    name =StringField("Name", validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    '''docstring'''
    form=forms()
    if form.validate_on_submit():
        if session.get('name') != form.name.data:
            flash("Name changed")
        session['name'] = form.name.data
        db.execute("INSERT INTO test VALUES (:name)",name = form.name.data)
        form.name.data=''
        return redirect(url_for('index')) 
    return render_template("index.html",form=form,name=session.get('name'))

if __name__ == "__main__":
    #manager.run()
    app.run(debug=True)
