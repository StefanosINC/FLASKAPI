from Database.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    post_id = db.relationship('Post', backref='user', lazy='dynamic')

    def __init__(self, email, username, password, post_id=None):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
        if post_id is not None:
            self.blog_id = post_id

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def json(self):
        return {
        'user_info': {
            'user_id': self.id,
            'email': self.email,
            'username': self.username,
            'password_hash': self.password_hash,
            'posts': [post.json() for post in self.post_id]
        },
        
    }
    def __str__(self):
        return f"user ID: {self.id}"
    
    
