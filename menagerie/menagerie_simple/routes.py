#!/usr/bin/env python3
"""
Menagerie routes

@author: Roman Yasinovskyy
@version: 2026.7
"""

from math import ceil

from flask import Blueprint, current_app, redirect, render_template, request, session, url_for

from menagerie_simple.crud import add_adoption, query_db, remove_adoption

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def index():
    # authenticated
    if "current_user" in session:
        statement = """
    select animal.id
    from animal
    join adoption on animal.id=adoption.animal_id
    join user on user.id=adoption.user_id
    where user.id=?;
        """
        adopted_by_user = [
            record["id"]
            for record in query_db(
                current_app.config["DATA_PATH"],
                f"{current_app.config['DB_NAME']}.db",
                statement,
                (session["current_user"]["id"],),
            )
        ]
        return render_template("index.jinja", data=current_app.data, adopted=adopted_by_user)
    # anonymous
    statement = """
select adoption.animal_id, count(adoption.user_id)
from adoption
group by adoption.animal_id
"""
    adoptions = query_db(
        current_app.config["DATA_PATH"], f"{current_app.config['DB_NAME']}.db", statement
    )
    print(adoptions)
    total_adoptions = {
        a[0]: a[1]
        for a in query_db(
            current_app.config["DATA_PATH"], f"{current_app.config['DB_NAME']}.db", statement
        )
    }
    for a in current_app.data:
        if a["id"] not in total_adoptions:
            total_adoptions[a["id"]] = 0
    least_adopted, most_adopted = min(total_adoptions.values()), max(total_adoptions.values())
    if least_adopted == most_adopted:
        most_adopted = least_adopted + 1
    # normalize adoptions to the 1--5 range
    min_favs, max_favs = 1, 5
    return render_template(
        "index.jinja",
        data=current_app.data,
        admired={
            key: int(
                ceil(
                    (min_favs + (max_favs - min_favs) * (value - least_adopted))
                    / (most_adopted - least_adopted)
                )
            )
            for key, value in total_adoptions.items()
        },
    )


@main.get("/profile")
def profile():
    return render_template("profile.jinja")


@main.post("/adopt/<int:animal_id>")
def adopt(animal_id: int):
    form = request.form
    adoption = query_db(
        current_app.config["DATA_PATH"],
        f"{current_app.config['DB_NAME']}.db",
        "select * from adoption where user_id=? and animal_id=?;",
        params=(session["current_user"]["id"], animal_id),
        firstone=True,
    )
    if not adoption and "adopt" in form:
        add_adoption(
            current_app.config["DATA_PATH"],
            f"{current_app.config['DB_NAME']}.db",
            session["current_user"]["id"],
            animal_id,
        )
    if adoption and "reject" in form:
        remove_adoption(
            current_app.config["DATA_PATH"],
            f"{current_app.config['DB_NAME']}.db",
            session["current_user"]["id"],
            animal_id,
        )
    return redirect(url_for("main.index"), 302)
