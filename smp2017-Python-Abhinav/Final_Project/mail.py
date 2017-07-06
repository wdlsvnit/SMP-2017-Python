#TODO : Make class to send Emails via Python
from application import APP,MAIL
from flask_mail import Message
from flask import render_template

def send_email(to, subject, template, **kwargs):
    msg = Message(APP.config['APP_NAME'] + subject, sender=APP\
    .config['MAIL_USERNAME'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    MAIL.send(msg)
 