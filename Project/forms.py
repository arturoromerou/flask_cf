from wtforms import Form # formularios de flask
from wtforms import StringField, TextField, PasswordField, DateField # formato para nuestros inputs
from wtforms.fields.html5 import EmailField # formato de correo electronico para input
from wtforms import HiddenField # oculta los campos que deseemos
from wtforms import validators # esto valida los campos que deseemos
from models import User

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('el campo debe estar vacio')

class CommentForm(Form):
    comment = TextField('Comentario')

class LoginForm(Form):
    username = StringField('Username',
                        [ 
                            validators.Required(message='el username es requerido'),
                            validators.length(min=4, max=25, message='ingresa un username valido!.')
                        ]
                        )
    password = PasswordField('Password', 
                            [
                                validators.Required(message='El password es requerido')
                            ]
                            )

class CreateForm(Form):
    username = StringField('Username',
                        [ 
                            validators.Required(message='el username es requerido'),
                            validators.length(min=4, max=25, message='ingresa un username valido!.')
                        ]
                        )

    password = PasswordField('Password', 
                            [
                                validators.Required(message='El password es requerido')
                            ]
                            )

    email = EmailField('Correo Electronico',
                    [
                        validators.Required(message='el email es requerido'),
                        validators.Email(message='ingresa un email valido'),
                        validators.length(min=4, max=50, message='ingrese un email valido')
                    ]
                    )

    honeypot = HiddenField('', [length_honeypot])

    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.ValidationError('el username ya existe! :(')
