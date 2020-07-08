from flask import Flask

app = Flask(__name__) # nuevo objeto

@app.route('/') # decorador
def hello(): # funcion
    return 'chao!'

if __name__ == '__main__':
    ''' debug actualiza cada vez que se haga un cambio en el archivo'''
    app.run(debug=True, port=8000) # se encarga de ejecutar el servidor por default poort=5000