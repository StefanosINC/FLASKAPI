from flask import Blueprint, jsonify
from Models.UserModel import User
from Database.database import db
from flask_jwt import jwt_required
user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/user/<string:username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(user.json())
    else:
        return jsonify({'name': None}), 404

@user_blueprint.route('/user/create/<string:email>/<string:username>/<string:password>/<string:puppy_name>', methods=['POST'])
def register_user(email, username, password,puppy_name):
    user = User(email=email, username=username, password=password, puppy_name=puppy_name)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.json())

@user_blueprint.route('/users', methods=['GET'])
def return_user_info():
     
     ### Remember to watch the users stuff
     users = User.query.all()
     if users:
        user_list = [{'id': user.id, 'email': user.email, 'username': user.username, 'password': user.password_hash} for user in users]
        return jsonify(user_list)
     else:
        return jsonify({'name': None}), 404
