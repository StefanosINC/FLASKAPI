from flask import Blueprint, jsonify
from Models.UserModel import User
from Database.database import db
from Models.PuppyModel import Puppy
from flask_jwt import jwt_required
user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/user/<string:username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(user.json())
    else:
        return jsonify({'name': None}), 404
    
@user_blueprint.route('/user/create/<string:email>/<string:username>/<string:password>', methods=['POST'])
def register_account_with_Puppy(email, username, password):
    user = User(email=email, username=username, password=password)
    #puppy = Puppy(name=puppy_name)
    #user.puppy_name.append(puppy)

    db.session.add(user)
    db.session.commit()

    return jsonify(user.json()), 201

@user_blueprint.route('/users/<string:puppy_name>/<string:puppy_type>', methods=['POST'])
def add_puppy_to_users(puppy_name, puppy_type):
    # Find the puppy by its name
    puppy = Puppy.query.filter_by(puppy_name=puppy_name).first()

    if puppy:
        # Set the puppy's type
        puppy.puppy_type = puppy_type

        # Retrieve all users
        users = User.query.all()

        for user in users:
            # Check if the user already owns the puppy
            if puppy not in user.puppy_name:
                # Add the puppy to the user's puppy_name relationship
                user.puppy_name.append(puppy)

        db.session.commit()
        return jsonify({'message': 'Puppy added to users successfully.'}), 201
    else:
        return jsonify({'message': 'Puppy not found.'}), 404
