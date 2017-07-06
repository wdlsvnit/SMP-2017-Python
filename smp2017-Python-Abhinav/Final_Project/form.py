#TODO: WTForms
from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms import StringField, SubmitField, PasswordField, BooleanField



class LoginForm(FlaskForm):
    '''Login form'''
    email = StringField("Name", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    checkbox = BooleanField("Remember Me")
    submit = SubmitField("Login")
    
class SignupForm(FlaskForm):
    '''Signup form'''
    email = StringField("Email", validators=[Required()])
    passworda = PasswordField("Password", validators=[Required()])
    passwordb = PasswordField("Password", validators=[Required()])
    hostel = StringField("Hostel Name", validators=[Required()])
    rollno = StringField("SVNIT Roll number", validators=[Required()])
    firstname = StringField("First Name", validators=[Required()])
    lastname = StringField("Last name", validators=[Required()])
    submit = SubmitField("Sign Up")
    
class ResendForm(FlaskForm):
    '''Resend conf form '''
    email = StringField("Email", validators=[Required()])
    submit = SubmitField("Submit")

class PostForm(FlaskForm):
    '''Post form'''
    title = StringField("Title", validators=[Required()])
    post = StringField("Gossip", validators=[Required()])
    hostel = StringField("Hostel Name", validators=[Required()])
    submit = SubmitField("Post")