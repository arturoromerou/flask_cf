from flask import Flask # importa flask
from flask import render_template # renderiza los templates
from flask import request #
from flask import make_response
from flask import session

from flask import url_for
from flask import redirect

from flask_wtf.csrf import CSRFProtect # evita los ataques csrf con un secret key
import forms

app = Flask(__name__)
app.secret_key = 'Ar2098'
csrf = CSRFProtect(app)

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        print(username)
    title = 'Index'
    return render_template('index.html', title = title)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    title = 'Login'
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        session['username'] = login_form.username.data

    return render_template('login.html', title = title, form = login_form)

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

if __name__ == '__main__':
    app.run(debug=True, port=8000)