import os
import sys
import enum
from sqlalchemy import ForeignKey, Integer, String
from eralchemy2 import render_er
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class Planets(db.Model):
    __tablename__ = 'Planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)

class Films(db.Model):
    __tablename__ = 'Films'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    episode_id = db.Column(db.String(250), nullable=False)
    release_date = db.Column(db.String(250), nullable=False)
    director = db.Column(db.String(250), nullable=False)
    producer = db.Column(db.String(250), nullable=False)


class People(db.Model):
    __tablename__ = 'People'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    species = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    hair_color = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    homeworld = db.Column(db.String(250), ForeignKey(Planets.ID), nullable=False)


class Users(db.Model):
    __tablename__ = 'Users'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    username = db.Column(db.String(250), nullable=False, unique=True)

class FavoriteTypeEnum(enum.Enum):
    Planet= "Planet"
    People = "People"
    Films = "Films"

class Favorites(db.Model):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = db.Column(db.Integer, primary_key=True, unique=True)
    User_id = db.Column(db.Integer, ForeignKey(Users.ID), nullable=False)
    external_ID = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    type = db.Column(db.Enum(FavoriteTypeEnum), nullable=False, unique=True)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e