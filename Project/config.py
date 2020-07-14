import os

class Config(object):
    SECRET_KEY = 'Ar2098'
    POSTS_PER_PAGE = 3
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'flask.arturo@gmail.com'
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_AR')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Ar2098urd@localhost/flask?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False