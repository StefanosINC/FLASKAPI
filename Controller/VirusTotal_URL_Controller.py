from flask import Blueprint, jsonify, request
from VirusTotalAPI.VirusTotalApI import VirusTotalAPI
from urllib.parse import quote, unquote
from flask_jwt import jwt_required
virustotal_blueprint = Blueprint('VtAPi', __name__)

@virustotal_blueprint.route('/virustotal/<path:input_string>', methods=['GET'])
def retrieve_url_data(input_string):
    decoded_string = unquote(input_string)
    return VirusTotalAPI.retrieveURLs(decoded_string)


@jwt_required()
@virustotal_blueprint.route('/virustotal/file/<filehash>', methods=['GET'])
def retrieveProcess(filehash):
    return VirusTotalAPI.retrieveProcess(filehash)