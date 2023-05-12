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

@puppy_blueprint.route('/puppies/create/<string:name>', methods=['POST'])

def create_puppy(name):
    pup = Puppy(name=name)
    db.session.add(pup)
    db.session.commit()
    return jsonify(pup.json())

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
@jwt_required()
def get_all_puppies():
    puppies = Puppy.query.all()
    return jsonify([pup.json() for pup in puppies])
