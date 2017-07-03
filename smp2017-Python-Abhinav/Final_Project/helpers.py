from flask import session, redirect, url_for, request, render_template
from functools import wraps
from application import APP,MAIL
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer 
from flask_mail import Message
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.11/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("email_id") is None:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def send_conf(email,id):
    s = Serializer(APP.config['SECRET_KEY'], 3600)
    token = s.dumps({'confirm': id})
    send_email(email,"Verification", 'templates/template', token = token)
 

def send_email(to, subject, template, **kwargs):
     msg = Message(APP.config['APP_NAME'] + subject, sender=APP\
     .config['MAIL_SENDER'], recipients=[to])
     msg.body = render_template(template + '.txt', **kwargs)
     msg.html = render_template(template + '.html', **kwargs)
     MAIL.send(msg) 