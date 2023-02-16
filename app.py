from flask import Flask
#import os
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Desafio: Custom Message"

if __name__ == '__main__':
    app.run()
#    port = os.getenv('PORT')
#    app.run('0.0.0.0', port=port)

#removidos ajustes do Heroku