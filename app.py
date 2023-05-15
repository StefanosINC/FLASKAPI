from flask import Flask
from flask_jwt import JWT
from Authentication.secure_check import authenticate, identity
from Database.database import initialize_db
from Controller.BlogController import blog_Blueprint
from Controller.UserController import user_blueprint

app = Flask(__name__)

# Initialize the database
app.register_blueprint(blog_Blueprint)
app.register_blueprint(user_blueprint)


initialize_db(app)
jwt = JWT(app, authenticate, identity)

if __name__ == '__main__':
    app.run(debug=False)
