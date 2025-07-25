#!/usr/bin/env python3
"""
College navigator authentication routes

@author: Roman Yasinovskyy
@version: 2025.7
"""

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from navigator import db, login_manager
from navigator.forms import LoginForm, SignupForm
from navigator.models import User

auth = Blueprint("auth", __name__, url_prefix="/")

user = User()


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("User already exists")
            return redirect(url_for("auth.signup"))
        new_user = User(
            email=email,
            name=name,
            password=generate_password_hash(password),
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("signup.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.")
            return redirect(url_for("auth.login"))

        login_user(user)
        flash(f"Welcome, {user.name}")
        return redirect(url_for("main.index"))
    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()
