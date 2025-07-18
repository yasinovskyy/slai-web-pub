from flask import Blueprint, flash, redirect, request, session, url_for


auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.post("/login")
def login():
    user_password = request.form["password"]
    if user_password != "slai":
        flash("Incorrect password")
        return redirect(url_for("main.index"))

    session["name"] = request.form["username"]
    return redirect(url_for("main.index"), code=303)


@auth.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("main.index"), code=303)
