# -*- coding: utf-8 -*-
from flask import Flask
from flask import request

app = Flask(__name__) # nuevo objeto

@app.route('/') # decorador
def hello(): # funcion
    return 'chao!'

@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name = 'valor por default', num = 'nada'):
   return 'El parametro es: {} {}'.format(name, num)

if __name__ == '__main__':
    # debug actualiza cada vez que se haga un cambio en el archivo
    app.run(debug=True, port=8000) # se encarga de ejecutar el servidor por default poort=5000