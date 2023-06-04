from flask import Flask
from flask_jwt_extended import JWTManager
from Services.UserService import UserService
from Database.database import initialize_db
from Controller.BlogController import blog_Blueprint
from Controller.UserController import user_blueprint
from Controller.VirusTotal_URL_Controller import virustotal_blueprint
from JWTUtils.Jwt import initialize_jwt
app = Flask(__name__)

# Initialize the database
app.register_blueprint(blog_Blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(virustotal_blueprint)

initialize_db(app)
jwt = JWTManager(app)
initialize_jwt(app)
if __name__ == '__main__':
    app.run(debug=False)
