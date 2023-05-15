from Database.database import db


class Puppy(db.Model):
    __tablename__ = 'puppies'

    puppy_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    puppy_name = db.Column(db.String(64))
    puppy_type = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=None)

    def __init__(self, puppy_name, puppy_type, user_id=None):
        self.puppy_name = puppy_name
        self.puppy_type = puppy_type
        self.user_id = user_id

    def json(self):
        return {'puppy_id': self.puppy_id,'puppy_name': self.puppy_name, 'puppy_type': self.puppy_type, 'user_id': self.user_id}
