from Database.database import db

class Puppy(db.Model):
    name = db.Column(db.String(80), primary_key=True)

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name': self.name}

# Additional models can be defined here
