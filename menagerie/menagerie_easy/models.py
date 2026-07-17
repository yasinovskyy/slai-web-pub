#!/usr/bin/env python3
"""
Menagerie data models

@author: Roman Yasinovskyy
@version: 2025.7
"""

from flask_login import UserMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from menagerie_easy import db


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]


class Animal(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    species: Mapped[str]
    location: Mapped[str]


class Adoption(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    animal_id: Mapped[int] = mapped_column(ForeignKey("animal.id"))
