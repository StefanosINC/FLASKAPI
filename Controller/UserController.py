from flask import Blueprint, jsonify
from Models.UserModel import User
from Database.database import db
from Models.BlogModel import Blog
from flask_jwt import jwt_required
import re
from Services.UserService import UserService

user_blueprint = Blueprint('users', __name__)

#****************************

#***** GET USERS BY ID  ***** 
# *****  CREATE AN ACCOUNT  ***** 
# ***** RETURN ALL USERS ***** 
# ***** DELETE USER BY ID *****

#*************************************


#***** REGEX **********

###^ indicates the start of the string.
#\d represents any digit character.
#+ specifies that the previous element (digit) can occur one or more times.
#$ denotes the end of the string.
#*********************************************

@user_blueprint.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    return UserService.get_userById(id)

@user_blueprint.route('/user/create/<string:email>/<string:username>/<string:password>', methods=['POST'])
def register_user_account(email, username, password, blog_id = None):
    return UserService.register_user_account(email,username,password, blog_id)

@user_blueprint.route('/users', methods=['GET'])
def return_all_users():
    users = User.query.all()
    if users:
        user_list = [user.json() for user in users]
        return jsonify(user_list)
    else:
        return jsonify({'name': None}), 404


@user_blueprint.route('/user/delete/<int:id>', methods=['DELETE'])
def delete_user_by_Id(id):
    user = User.query.filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'note': 'delete success'})
    else:
        return jsonify({'note': 'user not found'}), 404

@user_blueprint.route('/user/update/<int:id>/<string:email>/<string:username>/<string:password>', methods=['PUT'])
def update_user_information(id, email, username, password):
    user = User.query.get(id)
    if user:
        user.email = email
        user.username = username
        user.password_hash = password
        db.session.commit()
        return jsonify({'message': 'User information updated successfully'})
    else:
        return jsonify({'message': 'User not found'})

    #email=email, username=username, password=password


