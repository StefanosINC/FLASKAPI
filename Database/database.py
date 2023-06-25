from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
## here

db = SQLAlchemy()
migrate = Migrate()

def initialize_db(app):
    app.config['SECRET_KEY'] = 'mysecretkey'
    basedir = os.path.abspath(os.path.dirname(__name__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

app = Flask(__name__)
initialize_db(app)

# Other app configurations and routes...

if __name__ == '__main__':
    app.run(debug=True)
