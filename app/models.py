from . import db
from flask_login import UserMixin

class Pitch(db.Model):
    id = db.Column(db.String,primary_key = True) 
    title = db.Column(db.String,nullable = False)
    category = db.Column(db.String,nullable = False)
    content = db.Column(db.String,nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    # comments = db.relationship('Comment',backref = 'pitch',lazy = 'dynamic')
    # upvotes = db.relationship('Upvote',backref = 'pitch',lazy = 'dynamic')
    # downvotes = db.relationship('Downvote',backref = 'pitch',lazy = 'dynamic')
     


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    pitches = db.relationship('Pitch',backref = 'user',lazy = 'dynamic')
    
    
