#!/usr/bin/env python3
"""
Menagerie authentication routes

@author: Roman Yasinovskyy
@version: 2026.7
"""

from flask import (
    Blueprint,
    abort,
    current_app,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from menagerie_simple.crud import add_user, query_db, retrieve_by_id, update_user

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.get("/signup")
def signup():
    return render_template("signup.jinja")


@auth.post("/signup")
def signup_submitted():
    form = request.form
    email = form.get("email")
    if query_db(
        current_app.config["DATA_PATH"],
        f"{current_app.config['DB_NAME']}.db",
        "select * from user where email=?",
        (email,),
    ):
        flash("User already exists", "warning")
        return render_template("signup.jinja", form=form)
    name = form.get("name")
    if form.get("password") != form.get("confirm"):
        flash("Password do not match")
        return render_template("signup.jinja", form=form)
    password = generate_password_hash(form.get("password", ""))
    user = dict(name=name, email=email, password=password)
    add_user(
        current_app.config["DATA_PATH"],
        f"{current_app.config['DB_NAME']}.db",
        user,
    )
    return redirect(url_for("auth.login"))


@auth.get("/login")
def login():
    return render_template("login.jinja")


@auth.post("/login")
def login_submitted():
    form = request.form
    email = form.get("email")
    password = form.get("password", "")
    user = query_db(
        current_app.config["DATA_PATH"],
        f"{current_app.config['DB_NAME']}.db",
        "select * from user where email=?",
        (email,),
        firstone=True,
    )
    if not user or not check_password_hash(user["password"], password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))

    login_user(user)
    flash(f"Welcome, {user['name']}")
    return redirect(url_for("main.index"))


@auth.post("/profile")
def profile():
    form = request.form
    print(form)
    if not form:
        abort(405)
    email = form.get("email", "")
    name = form.get("name", "")
    if form.get("password") != form.get("confirm"):
        flash("Password do not match")
        return render_template("profile.jinja", form=form)
    user = query_db(
        current_app.config["DATA_PATH"],
        f"{current_app.config['DB_NAME']}.db",
        "select * from user where email=?",
        (email,),
        firstone=True,
    )
    password = generate_password_hash(form.get("password", ""))
    update_user(
        current_app.config["DATA_PATH"],
        f"{current_app.config['DB_NAME']}.db",
        user["id"],
        name,
        password,
    )
    session["current_user"]["name"] = name
    flash("Profile has been updated", category="success")
    return redirect(url_for("main.index"))


@auth.route("/logout")
def logout():
    session.pop("current_user", None)
    return redirect(url_for("main.index"))


def load_user(user_id):
    return retrieve_by_id(
        current_app.config["DATA_PATH"],
        f"{current_app.config['DB_NAME']}.db",
        "user",
        user_id,
    )


def login_user(user):
    session["current_user"] = dict(user)
