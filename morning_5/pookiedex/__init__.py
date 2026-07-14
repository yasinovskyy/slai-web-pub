import random

from flask import Flask

from pookiedex.crud import init_db, populate_db, query_db


def create_app():
    app = Flask(__name__)
    init_db("pookiedex/data/pookiedex.db", "allpokemon")
    populate_db("pookiedex/data/pookiedex.db", "allpokemon", "pookiedex/data/pokemon.csv")
    # extract primary types from the dataset
    app.config["primary_types"] = query_db(
        "pookiedex/data/pookiedex.db",
        "select distinct `Primary Typing` from allpokemon order by `Primary Typing`;",
    )
    app.config["secondary_types"] = query_db(
        "pookiedex/data/pookiedex.db",
        "select distinct `Secondary Typing` from allpokemon where `Secondary Typing`<>? order by `Secondary Typing`;",
        "",
    )
    # extract generations from the dataset
    app.config["generation"] = query_db(
        "pookiedex/data/pookiedex.db",
        "select distinct Generation from allpokemon order by Generation;",
    )
    app.config["poke_id"] = random.randint(1, 1025)
    from pookiedex.routes import main

    app.register_blueprint(main)

    return app
