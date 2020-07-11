from flask_sqlalchemy import SQLAlchemy # orm SQLAlchemy
from flask_bcrypt import Bcrypt
import datetime # importa la fecha actual

db = SQLAlchemy()
bcrypt = Bcrypt()

# clase que crea una base de datos
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(40))
    password = db.Column(db.String(66))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.__create_pasword(password)

    def __create_pasword(self, password):
        return bcrypt.generate_password_hash(password).decode ('utf-8')

    '''esta funcion recibe el password en plano y lo compara con el password encriptado en la bd'''
    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
