import dotenv
from pokesearch.logic import read_csv
from flask import Flask


def create_app():
    inner_app = Flask(__name__)
    dotenv.load_dotenv(".flaskenv")
    inner_app.config.from_prefixed_env()
    inner_app.data = read_csv("pokesearch/data/pokemon.csv")
    poke_types = set()
    for record in inner_app.data:
        poke_types.add(record["Type 1"])
        if record["Type 2"]:
            poke_types.add(record["Type 2"])
    inner_app.poke_types = sorted(poke_types)
    poke_gens = set()
    for record in inner_app.data:
        poke_gens.add(record["Generation"])
    inner_app.poke_gens = sorted(poke_gens)

    from pokesearch.routes import main
    from pokesearch.auth import auth

    inner_app.register_blueprint(main)
    inner_app.register_blueprint(auth)

    return inner_app
