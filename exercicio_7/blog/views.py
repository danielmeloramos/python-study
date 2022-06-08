# http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates
from flask import render_template

from blog import app


@app.route("/", methods=["GET"])
def blog():
    return render_template("blog.html", content="Daniel Melo Ramos")
