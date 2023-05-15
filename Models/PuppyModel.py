from Database.database import db


class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    puppy_name = db.Column(db.String(64))
    puppy_type = db.Column(db.String(64))
   # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, puppy_name, puppy_type):
        self.puppy_name = puppy_name
        self.puppy_type = puppy_type

    def json(self):
        return {'puppy_name': self.puppy_name, 'puppy_type': self.puppy_type}

# Additional models can be defined here
