from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    fullname = db.Column(db.String(150))
    username = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone = True), default = func.now())
    posts = db.relationship("Post", backref="user", passive_deletes=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(150), nullable=False)
    image = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone = True), default = func.now())
    author = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)