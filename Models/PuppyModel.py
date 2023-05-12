from Database.database import db

class Puppy(db.Model):
    __tablename__ = 'puppies'
    name = db.Column(db.String(80), primary_key=True)
    users = db.relationship('users', backref='puppy', lazy='dynamic')
    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name': self.name}

# Additional models can be defined here
