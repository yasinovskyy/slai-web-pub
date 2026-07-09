from flask import Flask
import random
from pookiedex.data_exploration import read_csv_file


def create_app():
    app = Flask(__name__)
    app.config["data"] = read_csv_file("pookiedex/data/pokemon.csv")
    # TODO: extract types from the dataset
    # TODO: extract generations from the dataset
    app.config["poke_id"] = random.randint(1, 1025)
    from pookiedex.routes import main

    app.register_blueprint(main)

    return app
