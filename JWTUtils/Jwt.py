from flask_jwt_extended import JWTManager
from Services.UserService import UserService
jwt = JWTManager()


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, jwt_data):
    jti = jwt_data['jti']
    return jti in UserService.blacklisted_tokens

def initialize_jwt(app):
    jwt.init_app(app)
    jwt.token_in_blocklist_loader(check_if_token_in_blacklist)