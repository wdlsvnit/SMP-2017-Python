#TODO: WTForms
from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField, SubmitField, PasswordField, BooleanField



class LoginForm(FlaskForm):
    '''Login form'''
    email = StringField("Name", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    checkbox = BooleanField("Remember Me")
    submit = SubmitField("Submit")
    
class SignupForm(FlaskForm):
    '''Signup form'''
    email = StringField("Email", validators=[Required()])
    passworda = PasswordField("Password", validators=[Required()])
    passwordb = PasswordField("Password", validators=[Required()])
    hostel = StringField("Hostel Name", validators=[Required()])
    rollno = StringField("SVNIT Roll number", validators=[Required()])
    submit = SubmitField("Submit")