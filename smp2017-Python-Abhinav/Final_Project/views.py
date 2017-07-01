#TODO: Views
import sys
from application import APP, BOOTSTRAP
from flask import redirect, session, request, render_template, url_for, flash
from form import LoginForm, SignupForm
from application import db
from werkzeug.security import generate_password_hash, check_password_hash


@APP.route('/login', methods = ['GET','POST'])
def login():
    '''index'''
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            flash("Submitted") #{}".formatfile(form.username.data))
            password = form.password.data
            email = form.email.data
            row = db.execute("SELECT passhash from test4 where email=:email",email=email)
            if check_password_hash(row[0]['passhash'],password):
                #LOGIN
                form.email.data = ''
                form.password.data = ''
                form.checkbox.data = ''
                return render_template('main.html')
            else:
                form.email.data = ''
                form.password.data = ''
                form.checkbox.data = ''
                return redirect(url_for("login"))
        return redirect(url_for("signup"))
    
    if request.method == "GET":
        return render_template('login.html', form=form)

@APP.route('/', methods = ['GET'])
def index():
    return render_template("main.html")

@APP.route('/signup', methods = ['GET','POST'])
def signup():
    '''index'''
    form = SignupForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if(form.passworda.data == form.passwordb.data):
                flash("Submitted") #{}".formatfile(form.username.data))
                passhash = generate_password_hash(form.passworda.data)
                email = form.email.data
                hostel = form.hostel.data
                rollno = form.rollno.data
                db.execute("INSERT INTO TEST4('email','passhash','hostel','rollno') \
                values (:email, :passw, :hostel, :rollno)", \
                email=email, \
                passw=passhash, hostel=hostel, rollno=rollno)
                form.email.data = ''
                form.passworda.data = ''
                form.passwordb.data = ''
                form.hostel.data = ''
                form.rollno.data = ''
                return render_template('main.html')
        return redirect(url_for(signup))
    if request.method == "GET":
        return render_template("signup.html", form = form)