#!/usr/bin/env python3
"""
College navigator data models

@authors: Roman Yasinovskyy
@version: 2024.7
"""

from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column

from navigator import db


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
