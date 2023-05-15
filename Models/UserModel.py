from Database.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    puppy_id = db.relationship('Puppy', backref='user', lazy='dynamic')

    def __init__(self, email, username, password, puppy_id=None):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        if puppy_id is not None:
            self.puppy_id = puppy_id

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def json(self):
        return {
            'user_id': self.id,
            'email': self.email,
            'username': self.username,
            'password_hash': self.password_hash,
            'puppy_id': [puppy.json() for puppy in self.puppy_id]
        }