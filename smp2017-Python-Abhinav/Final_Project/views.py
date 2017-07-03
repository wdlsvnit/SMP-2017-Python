#TODO: Views
import sys
from application import APP, BOOTSTRAP, SESSION
from flask import redirect, session, request, render_template, url_for, flash
from form import LoginForm, SignupForm, ResendForm
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from helpers import login_required, send_conf, acc_confirm

@APP.route('/login', methods = ['GET','POST'])
def login(*kwargs):
    '''index'''
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            password = form.password.data
            email = form.email.data
            row = db.execute("SELECT passhash,confirmed from test4 where email=:email",email=email)
            if row == []:
                flash("Invalid ID/Password")
                return redirect(url_for("login"))
            if check_password_hash(row[0]['passhash'],password):
                #LOGIN
                if row[0]['confirmed']== 'false' :
                    flash("Account not confirmed")
                    return redirect(url_for('index'))
                rows=db.execute("SELECT id from TEST4 where email=:email",email=email)
                form.email.data = ''
                form.password.data = ''
                form.checkbox.data = ''
                session["id"] = rows[0]['id']
                return render_template('secret.html')
            else:
                form.email.data = ''
                form.password.data = '' 
                form.checkbox.data  = ''
                flash("Invalid ID/Password")
                if(next==None):
                    return redirect(url_for("login"))
                else:
                    return redirect(url_for(next))
        else:
            return redirect(url_for("signup"))
    
    if request.method == "GET":
        return render_template('login.html', form=form)

@APP.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@APP.route('/signup', methods = ['GET','POST'])
def signup():
    '''index'''
    form = SignupForm()
    if request.method == "POST":
        if form.validate_on_submit():
            if(form.passworda.data == form.passwordb.data):
                passhash = generate_password_hash(form.passworda.data)
                email = form.email.data
                hostel = form.hostel.data
                rollno = form.rollno.data
                firstname=form.firstname.data
                lastname=form.lastname.data
                rows = db.execute("SELECT 'email' from TEST4 where email=:email",email=email)
                if rows == []:
                    db.execute("INSERT INTO TEST4('email','passhash','hostel','rollno','firstname','lastname') \
                    values (:email, :passw, :hostel, :rollno, :firstname, :lastname)", \
                    email=email, \
                    passw=passhash, hostel=hostel, rollno=rollno, firstname= firstname, lastname=lastname)
                    form.email.data = ''
                    form.passworda.data = ''
                    form.passwordb.data = ''
                    form.hostel.data = ''
                    form.rollno.data = ''
                    form.firstname.data=''
                    form.lastname.data=''
                    id = db.execute("SELECT id from test4 where email =  :email",email=email)
                    send_conf(email,id[0]['id'])
                    flash("Confirmation sent. Expires in 1 hour")
                    return render_template('index.html')
                else:
                    flash("E-Mail already has exisiting account!")
                    return redirect(url_for('signup'))
            else:
                return redirect(url_for('signup'))

    if request.method == "GET":
        return render_template("signup.html", form = form)

@APP.route('/secret', methods = ['GET'])
@login_required
def secret():
    flash("Logged in")
    render_template('secret.html')

@APP.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    flash("Logged Out")
    return render_template('index.html')


@APP.route('/confirm/<token>')
def confirm(token):
    if acc_confirm(token):
        flash("Account Confirmed!")
        return redirect(url_for('secret'))
    else:
        flash("Confirmation Failed!, Enter Email to resend confirmation.")
        return redirect(url_for('resend_conf'))

@APP.route('/resend_conf', methods=['GET','POST'])
def resend_conf():
    form = ResendForm()
    if form.validate_on_submit():
        rows = db.execute("SELECT id from test4 where email =  :email",email=form.email.data)
        if rows==[]:
            flash("Email id doesnt match")
            return redirect(url_for('resend_conf'))
        else:
            send_conf(form.email.data,rows[0]['id'])
            flash("Confirmation Resent, Expires in 1 hour")
            return render_template('index.html')
    else:
        return render_template("resend_conf.html",form = form)