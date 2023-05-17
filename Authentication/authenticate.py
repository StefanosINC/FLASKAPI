
from Models.UserModel import User
from Controller.UserController import return_all_users
from sqlalchemy.exc import SQLAlchemyError

class Auth: 
    def authenticate(username, password):
    ## check if exists 
    # if so return user
     try:
         user = User.query.filter_by(username=username).first()
         if user and user.password == password:
            return user
     except SQLAlchemyError as e:
        # Handle database errors
        print(e)
     return None

    def identity(payload):
     user_id = payload['identity']
     try:
        user = User.query.get(user_id)
        if user:
            return user
     except SQLAlchemyError as e:
        # Handle database errors
        print(e)
     return None

