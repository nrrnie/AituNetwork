from aituNetwork import db

from datetime import datetime
from random import randint


def random_id():
    mn = 1000000
    mx = 9999999

    rand = randint(mn, mx)
    while Users.query.filter_by(id=rand).first() is not None:
        rand = randint(mn, mx)

    return rand


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(255), unique=True, nullable=False, default=random_id)
    barcode = db.Column(db.Integer, nullable=False, unique=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    about_me = db.Column(db.String(255), nullable=False, default='Hi there! I\'m using AITU Network!')
    password = db.Column(db.String(255), nullable=False)
    registered = db.Column(db.DATETIME, nullable=False, default=datetime.now)
    is_activated = db.Column(db.Boolean, nullable=False, default=False)


class ProfilePictures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), unique=True, nullable=False)
    added = db.Column(db.DATETIME, nullable=False, default=datetime.now)


class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True, nullable=False)
    friend_id = db.Column(db.Integer, index=True, nullable=False)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, index=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, nullable=False, default=0)
    created = db.Column(db.DATETIME, nullable=False, default=datetime.now)
