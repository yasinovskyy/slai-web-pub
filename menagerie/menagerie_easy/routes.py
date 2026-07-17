#!/usr/bin/env python3
"""
Menagerie routes

@author: Roman Yasinovskyy
@version: 2025.7
"""

from math import ceil
from flask import Blueprint, current_app, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy import func, select

from menagerie_easy import db
from menagerie_easy.forms import UpdateProfileForm
from menagerie_easy.models import Adoption, Animal, User

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def index():
    if current_user.is_authenticated:
        stmt = (
            select(Animal.id)
            .join(Adoption, Animal.id == Adoption.animal_id)
            .join(User, User.id == Adoption.user_id)
            .where(User.id == current_user.id)
        )
        adopted_by_user = db.session.execute(stmt).scalars().all()
        return render_template("index.jinja", data=current_app.data, adopted=adopted_by_user)
    stmt = select(Adoption.animal_id, func.count(Adoption.user_id)).group_by(Adoption.animal_id)
    total_adoptions = {a[0]: a[1] for a in db.session.execute(stmt).all()}
    for a in current_app.data:
        if a.id not in total_adoptions:
            total_adoptions[a.id] = 0
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
@login_required
def profile():
    form = UpdateProfileForm(
        email=current_user.email, name=current_user.name, password=current_user.password
    )
    return render_template("profile.jinja", form=form)


@main.post("/adopt/<int:animal_id>")
def adopt(animal_id: int):
    form = request.form
    adoption = Adoption.query.filter_by(user_id=current_user.id, animal_id=animal_id).first()
    if not adoption and "adopt" in form:
        adoption = Adoption(user_id=current_user.id, animal_id=animal_id)
        db.session.add(adoption)
    if adoption and "reject" in form:
        db.session.delete(adoption)
    db.session.commit()
    return redirect(url_for("main.index"), 302)
