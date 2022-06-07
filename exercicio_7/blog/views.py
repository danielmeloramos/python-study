# http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates
from flask import render_template

from blog import app


@app.route("/", methods=["GET"])
def blog():
    """Blog

    Registrando uma rota `/` que aceita GET e renderiza o template
    `blog.html` e passa para a variável `content` do template o valor
    `Hello, World`
    """
    return render_template("blog.html", content="Hello, World")
