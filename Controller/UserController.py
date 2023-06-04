from flask import Blueprint, jsonify
from Models.UserModel import User
from Database.database import db
from Models.BlogModel import Blog
from flask_jwt import jwt_required
import re
from Services.UserService import UserService
from flask_jwt_extended import jwt_required

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/user/<int:id>', methods=['GET'])
@jwt_required()
def get_userById(id):
    return UserService.get_userById(id)

@user_blueprint.route('/user/create/<string:email>/<string:username>/<string:password>', methods=['POST'])
def register_user_account(email, username, password, blog_id = None):
    return UserService.register_user_account(email,username,password, blog_id)


@user_blueprint.route('/users', methods=['GET'])
@jwt_required()
def return_all_users():
    return UserService.return_all_users()

@user_blueprint.route('/user/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user_by_Id(id):
    return UserService.delete_user_by_Id(id)

@user_blueprint.route('/user/update/<int:id>/<string:email>/<string:username>/<string:password>', methods=['PUT'])
@jwt_required()
def update_user_information(id, email, username, password):
    return UserService.update_user_information(id, email, username, password)

@user_blueprint.route('/user/login/<string:username>/<string:password>', methods= ['POST'])
def login_user(username, password):
    return UserService.login(username, password)

@user_blueprint.route('/logout', methods=['POST'])
@jwt_required()  # Ensure a valid token is provided
def logout():
    return UserService.logout()

@user_blueprint.route('/personal/info', methods=['GET'])
@jwt_required()
def retrieveAccountInfo():
    return UserService.retrieveAccountInfo()

