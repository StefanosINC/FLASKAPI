from flask import Blueprint, jsonify
from Models.PuppyModel import Puppy
from Database.database import db
from flask_jwt import jwt_required
puppy_blueprint = Blueprint('puppy', __name__)

@puppy_blueprint.route('/puppies/<string:name>', methods=['GET'])
def get_puppy(name):
    pup = Puppy.query.filter_by(name=name).first()
    if pup:
        return jsonify(pup.json())
    else:
        return jsonify({'name': None}), 404
    
@puppy_blueprint.route('/puppies/create/<string:puppy_name>/<string:puppy_type>', methods=['POST'])
def create_puppy(puppy_name, puppy_type, user_id=None):
    if user_id is not None:
        pup = Puppy(puppy_name=puppy_name, puppy_type=puppy_type, user_id=user_id)
    else:
        pup = Puppy(puppy_name=puppy_name, puppy_type=puppy_type)
    
    db.session.add(pup)
    db.session.commit()
    
    return jsonify({'id': pup.puppy_id, 'puppy': pup.json()})



@puppy_blueprint.route('/puppies/delete/<string:name>', methods=['DELETE'])
def delete_puppy(name):
    pup = Puppy.query.filter_by(name=name).first()
    if pup:
        db.session.delete(pup)
        db.session.commit()
        return jsonify({'note': 'delete success'})
    else:
        return jsonify({'note': 'Puppy not found'}), 404


@puppy_blueprint.route('/puppies', methods=['GET'])
def get_all_puppies():
    puppies = Puppy.query.all()
    if puppies:    
        puppyies_list = [puppies.json() for puppies in puppies]
        return jsonify(puppyies_list)
    else:
        return jsonify({'name': None}), 404


