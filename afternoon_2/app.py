from flask import Flask, send_from_directory, render_template
from data_exploration import read_csv_file


def create_app():
    app = Flask(__name__)
    app.config["data"] = read_csv_file("menagerie.csv")
    return app


app = create_app()


@app.route("/")
def home():
    return render_template("home.jinja", menagerie=app.config["data"])


@app.route("/<int:animal_id>")
def details(animal_id: int):
    for animal in app.config["data"]:
        if int(animal["id"]) == animal_id:
            return render_template("details.jinja", animal=animal)
    return "Information on this animal has not been found"
