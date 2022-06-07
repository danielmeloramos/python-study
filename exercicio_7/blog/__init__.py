from flask import Flask  # import do Flask


app = Flask(__name__)  # configurando a app


import blog.views  # noqa:importando as views
