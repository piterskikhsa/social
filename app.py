import os
from datetime import datetime
from flask_script import Manager
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand


# def send_mail(to, subject, template, **kwargs):
#     mail_message = Message(app.config['SOCIAL_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['SOCIAL_MAIL_SENDER'],
#                            recipients=[to])
#     mail_message.body = render_template(template + '.txt', **kwargs)
#     mail_message.html = render_template(template + '.html', **kwargs)
#     mail.send(mail_message)
