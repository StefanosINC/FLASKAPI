from Database.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
  #  puppy_name = db.relationship('Puppy', backref='user', lazy='dynamic')

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        #self.puppy_name = puppy_name

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def json(self):
        return {'username': self.username}