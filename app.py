import os
from datetime import datetime
from flask.ext.script import Manager
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.moment import Moment
# from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand


# def send_mail(to, subject, template, **kwargs):
#     mail_message = Message(app.config['SOCIAL_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['SOCIAL_MAIL_SENDER'],
#                            recipients=[to])
#     mail_message.body = render_template(template + '.txt', **kwargs)
#     mail_message.html = render_template(template + '.html', **kwargs)
#     mail.send(mail_message)
