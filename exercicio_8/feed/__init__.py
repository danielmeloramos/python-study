from flask import Flask  # import do Flask
from alf.client import Client  # client para realizar requests utilizando OAuth


# Client com autorização para acessar a API python-workshops
client = Client(
    token_endpoint="https://accounts.backstage.qa.globoi.com/token",
    client_id="Kb13FBCaPuX8TP712h6hYA==",
    client_secret="vvO+k+WTTCqZQxlzdkByhQ==",
)

# Configurando a app Flask com a variável CLIENT.
# É possivel acessar essa configuração pelo app.config['CLIENT']
app = Flask(__name__)
app.config.from_mapping(CLIENT=client)


# importando todas as rotas
import feed.views  # noqa
