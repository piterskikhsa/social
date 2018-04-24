import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = False
    SECRET_KEY = 'hard to guess string'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    SOCIAL_MAIL_SUBJECT_PREFIX = '[Social]'
    SOCIAL_MAIL_SENDER = 'Social Admin <social@example.com>'
    SOCIAL_ADMIN = os.environ.get('SOCIAL_ADMIN')

    @staticmethod
    def __init__(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class TestingConfig(Config):
    TESTING = True

    SQLALCHEMY_DATABASE_URL = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}