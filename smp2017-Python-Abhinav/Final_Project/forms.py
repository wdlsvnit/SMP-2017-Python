#TODO: WTForms
from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField, SubmitField, PasswordField



class LoginForm(FlaskForm):
    '''Login form'''
    username = StringField("Name", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    submit = SubmitField('Submit')
