# sql schema for 'Note' and 'User'

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# (child) all notes must be associated with a user
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # store the ForeignKey of the child object that reference their parent
    # must pass a valid id of an existing user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# (parent) a user can have more than one note
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # the User primary key is their id
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') # link this user to their notes
