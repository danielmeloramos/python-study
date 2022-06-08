# PEP8
# Agrupado em 3 blocos e separados com uma linha de espaçamento entre cada
# - Primeiro bloco: Pacotes padrões do python
# - Segundo bloco: Pacotes instalados
# - Terceiro bloco: Pacotes do projeto


import json

from flask import render_template, request, redirect, url_for

from feed import app

# URL da API que contém as notícias
API_URL = "https://apis.backstage.qa.globoi.com/api/v2/python-workshop/globocom?filter[perPage]=1000"


# A API retorna a seguinte estrutura quando é acessado via GET:
# {
#   "items": [
#       {
#           "author": "author",
#           "title": "titulo",
#           "description": "descrição",
#           "url": "url da noticia",
#           "urlToImage": "url da imagem"
#       },
#       {...},
#       ...
#   ]
# }
@app.route("/", methods=["GET"])
def feed():
    # Pega os dados da API
    response = app.config["CLIENT"].get(API_URL)
    # TODO: Tente utilizar o ipdb para descobrir como acessar os itens das notícias (Dica: dir(response))

    # TODO: Troque os dados pelo que vem da API
    feeds = response.json()["items"]
    #feeds = [
    #    {
    #       "author": "author",
    #        "title": "titulo",
    #        "description": "descrição",
    #        "url": "url da noticia",
    #        "urlToImage": "url da imagem",
    #    }
    #]
    return render_template("feed.html", feeds=feeds)


@app.route("/register", methods=["GET", "POST"])
def register():
    # Envia os dados para a API.
    if request.method == "POST":
        data = {
            "author": request.form["author"],
            "title": request.form["title"],
            "description": request.form["description"],
            "urlToImage": request.form["urlToImage"],
            "url": request.form["url"]
        }

        # Envia a notícia para a API
        response = app.config["CLIENT"].post(
            API_URL, data=json.dumps(data), headers={"content-type": "application/json"}
        )

        # Redireciona para a pagina '/' após cadastrado com sucesso
        return redirect(url_for("feed"))

    # TODO: Substitua para renderizar a página de formulário
    return render_template("register.html")
