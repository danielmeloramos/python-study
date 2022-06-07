# import Flask
from flask import Flask


# Configuração do Flask
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    """Rota

    Através do decorator app.route é definido uma rota `/`
    que aceita o método GET e retorna o texto `Hello, World`
    """
    return "Hello, World"
