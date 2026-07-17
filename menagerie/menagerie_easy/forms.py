#!/usr/bin/env python3
"""
Menagerie forms

@author: Roman Yasinovskyy
@version: 2025.7
"""

from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = EmailField(
        "Email", validators=[DataRequired()], render_kw={"placeholder": "Email", "size": 32}
    )
    password = PasswordField(
        "Password", validators=[DataRequired()], render_kw={"placeholder": "Password", "size": 32}
    )


class SignupForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()], render_kw={"placeholder": "Email"})
    name = StringField("Name", validators=[DataRequired()], render_kw={"placeholder": "Full name"})
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={"placeholder": "Password"},
    )
    confirm = PasswordField(
        "Confirm password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
        render_kw={"placeholder": "Confirm password"},
    )


class UpdateProfileForm(SignupForm):
    email = EmailField(
        "Email",
        validators=[DataRequired()],
        render_kw={"readonly": True, "aria-label": "Read-only", "aria-invalid": "false"},
    )
