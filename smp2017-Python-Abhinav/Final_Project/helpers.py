from flask import session, redirect, url_for, request, render_template
from functools import wraps
from application import APP,MAIL
from itsdangerous import BadSignature,TimedJSONWebSignatureSerializer as Serializer 
from application import db
from mail import send_email
def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.11/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("id") is None:
            return redirect(url_for("login", next=request.url))
        return f(*args, **kwargs)
    return decorated_function


def send_conf(email,uid,name):
    s = Serializer(APP.config['SECRET_KEY'], 3600)
    token = s.dumps({'confirm': uid})
    send_email(email,"Verification", 'template', token = token,name = name)
 
def acc_confirm(token):
    s = Serializer(APP.config['SECRET_KEY'], 3600)
    try:
        confirm_id = s.loads(token)
    except BadSignature:
        return False
    rows = db.execute("SELECT confirmed from TEST4 where id=:id",\
    id=confirm_id['confirm'])
    if rows[0]['confirmed']==True:
        return True
    else:
        db.execute("UPDATE TEST4 set confirmed = 'true' where id=:id",\
        id=confirm_id['confirm'])
        return True