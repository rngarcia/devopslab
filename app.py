from flask import Flask
import os

app = Flask(__name__)

csrf = CSRFProtect(app)    

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

if __name__ == '__main__':
    app.run('0.0.0.0', port=port)