import os

class Config(object):
    SECRET_KEY = 'Ar2098'
    POSTS_PER_PAGE = 3

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Ar2098urd@localhost/flask?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False