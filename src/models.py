import os
import sys
from sqlalchemy import ForeignKey, Integer, String
from eralchemy2 import render_er
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(250), nullable=False, unique=True)
    firstname= db.Column(String(250), nullable=False)
    lastname= db.Column(String(250), nullable=False)
    email= db.Column(String(250), nullable=False, unique=True)

class Post(db.Model):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('User.id'), nullable=False)

class Media(db.Model):
    __tablename__ = "Media"
    id = db.Column(Integer, primary_key=True)
    type = db.Column(String,nullable=True)
    url = db.Column(String(250), nullable=True)
    post_id= db.Column(Integer, ForeignKey("Post.id"),nullable=False)

class Comment(db.Model):
    __tablename__ = "Comment"
    id = db.Column(Integer, primary_key=True)
    comment_text= db.Column(String(250), nullable=False)
    author_id=db.Column(Integer, ForeignKey("User.id"),nullable=False)
    post_id= db.Column(Integer, ForeignKey("Post.id"),nullable=False)

class Follower(db.Model):
    __tablename__ = "Follower"
    user_from_id=db.Column(Integer, ForeignKey("User.id"), primary_key=True)
    user_to_id=db.Column(Integer, ForeignKey("User.id"),primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e