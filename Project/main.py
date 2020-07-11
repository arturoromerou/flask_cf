from flask import Flask # importa flask
from flask import render_template # renderiza los templates
from flask import request 
from flask import make_response 
from flask import session # aplica sesiones 
from flask import flash # muestra mensajes en pantalla
from flask import g # me permite trabajar con cualquie variable dentro de una misma peticion (variable global)
from flask import url_for
from flask import redirect

from config import DevelopmentConfig

from models import db
from models import User

from flask_wtf.csrf import CSRFProtect # evita los ataques csrf con un secret key
import forms
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404

@app.before_request
def before_request():
    g.test = 'test1'

@app.route('/')
def index():
    print(g.test)
    if 'username' in session:
        username = session['username']
        print(username)
    title = 'Index'
    return render_template('index.html', title = title)

@app.after_request
def after_request(response):
    print(g.test)
    return response

@app.route('/login', methods = ['GET', 'POST'])
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password = login_form.password.data
        
        user = User.query.filter_by(username = username).first()
        if user is not None and user.verify_password(password):
            success_message = 'Bienvenido {}'.format(username)
            flash(success_message)
            
            session['username'] = username
            session['user_id'] = user.id
            
            return redirect( url_for('index') )
            
        else:
            error_message= 'Usuario o password no validos!'
            print(User.query.filter_by(username = username).first())
            flash(error_message)
            
        session['username'] = login_form.username.data
    return render_template('login.html', form = login_form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

@app.route('/cookie')
def method_name():
    title = 'Cookies'
    response = make_response(render_template('cookie.html', title = title))
    response.set_cookie('custom_cookie', 'Arturo')
    return response

@app.route('/comment', methods = ['GET', 'POST'])
def comment():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print('error en el formulario')

    title = "Comment"
    return render_template('comment.html', title = title, form = comment_form)

@app.route('/create', methods=['GET', 'POST'])
def create():
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        user = User(username = create_form.username.data,
                    password = create_form.password.data,
                    email = create_form.email.data)
        
        db.session.add(user) # necesita un objeto que herede de model
        db.session.commit() # nos aseguramos que se guarde en la base de datos

        success_message = 'Usuario registrado en la base de datos'
        flash(success_message)
    
    title = "Create"
    return render_template('create.html', form = create_form, title = title)

@app.route('/ajax-login', methods = ['POST'])
def ajax_login():
    print(request.form)
    username = request.form['username']
    response = {'status':200, 'username': username, 'id':1}
    return json.dumps(response)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app) # obtenemos las configuraciones de la base de datos


    with app.app_context(): # sincroniza la base de datos con la aplicacion
        db.create_all() # crea todas las tablas que no esten creadas

    app.run(port=8000)