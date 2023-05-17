from flask import Blueprint, jsonify
from Models.UserModel import User
from Database.database import db
from Models.BlogModel import Blog
from flask_jwt import jwt_required
import re
from Services.UserService import UserService
user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/user/<int:id>', methods=['GET'])
def get_userById(id):
    return UserService.get_userById(id)

@user_blueprint.route('/user/create/<string:email>/<string:username>/<string:password>', methods=['POST'])
def register_user_account(email, username, password, blog_id = None):
    return UserService.register_user_account(email,username,password, blog_id)


@user_blueprint.route('/users', methods=['GET'])
def return_all_users():
    return UserService.return_all_users()

@user_blueprint.route('/user/delete/<int:id>', methods=['DELETE'])
def delete_user_by_Id(id):
    return UserService.delete_user_by_Id(id)

@user_blueprint.route('/user/update/<int:id>/<string:email>/<string:username>/<string:password>', methods=['PUT'])
def update_user_information(id, email, username, password):
    return UserService.update_user_information(id, email, username, password)

@user_blueprint.route('/user/<string:username>/<string:password>', methods= ['POST'])
def login_user(username, password):
    return UserService.login(username, password)


