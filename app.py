from flask import Flask
from flask_jwt_extended import JWTManager
from Database.database import initialize_db
from Components.PostComponent.PostController import post_Blueprint
from Components.UserComponent.UserController import user_blueprint
from Components.VirusTotalComponent.VirusTotal_URL_Controller import virustotal_blueprint
from Components.HomeComponent.HomeController import home_blueprint
from JWTUtils.Jwt import initialize_jwt

app = Flask(__name__, static_folder='static')  # Set the static folder

# Register blueprints
app.register_blueprint(home_blueprint)
app.register_blueprint(user_blueprint)
# app.register_blueprint(post_Blueprint)
app.register_blueprint(virustotal_blueprint)

# Initialize the database
initialize_db(app)

# Set up JWT manager
jwt = JWTManager(app)
initialize_jwt(app)

if __name__ == '__main__':
    app.run(debug=True)
