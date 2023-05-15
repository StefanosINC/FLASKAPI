from flask import Blueprint, jsonify
from Models.UserModel import User
from Database.database import db
from Models.PuppyModel import Puppy
from flask_jwt import jwt_required
user_blueprint = Blueprint('users', __name__)

# Works
@user_blueprint.route('/user/<string:username>', methods=['GET'])
def get_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(user.json())
    else:
        return jsonify({'name': None}), 404

#Works
@user_blueprint.route('/user/create/<string:email>/<string:username>/<string:password>', methods=['POST'])
def register_account_with_Puppy(email, username, password, puppy_id = None):
   
    #puppy = Puppy(name=puppy_name)
    #user.puppy_name.append(puppy)
    if puppy_id is not None:
         user = User(email=email, username=username, password=password, puppy_id=puppy_id)
    else:
        user =   user = User(email=email, username=username, password=password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id, 'user': user.json()})

@user_blueprint.route('/users/<string:puppy_id>/<int:id>', methods=['POST'])
def add_puppy_to_users(puppy_id,id):
    # Find the puppy by its name
    puppy = Puppy.query.filter_by(puppy_id=puppy_id).first()

    if puppy:
        # Set the puppy's type
        puppy.puppy_id = puppy_id

        # Retrieve requested USER ID
        users = User.query.filter_by(id=id).first()
            # Check if the user already owns the puppy
        if puppy not in users.puppy_id:
                # Add the puppy to the user's puppy_name relationship
            users.puppy_id.append(puppy)

        db.session.commit()
        user_list = [user.json() for user in users]
        return jsonify(user_list)
    else:
        return jsonify({'message': 'Puppy not found.'}), 404
    

@user_blueprint.route('/users', methods=['GET'])
def return_all_users():
    users = User.query.all()
    if users:
        user_list = [user.json() for user in users]
        return jsonify(user_list)
    else:
        return jsonify({'name': None}), 404


#Works