from validate_email import validate_email
import re
from Models.UserModel import User
from flask import jsonify, abort, request
from Database.database import db
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
import sqlite3
import json
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask import Flask
from flask_jwt import JWT

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Set your own secret key

jwt = JWTManager(app)

class UserService: 
    def get_userById(id):
        try:
            RegexValidation = r'^\s*\d+\s*$'
            if re.match(RegexValidation, str(id)): ## This here 
                user = User.query.filter_by(id=id).first()
            if user:
                return jsonify({'The user was found': user.json()})
                # Convert the set to a list before returning
            else:
                raise TypeError(f'The requested ID {id} was not found in the database')
        except (TypeError) as error:
            return jsonify(str(error))
    
    def register_user_account(email, username, password, blog_id=None):
        try:
            UserService.is_valid_email(email)
            UserService.is_valid_username(username)
            UserService.is_valid_password(password)

            if blog_id is not None: 
                user = User(email=email, username=username, password=password, blog_id=blog_id)
            else:
                user = User(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'id': user.id, 'user': user.json()})
        
        except (NoResultFound, IntegrityError) as error:
            if isinstance(error, IntegrityError):
                if 'sqlite3.IntegrityError) UNIQUE constraint failed: users.username' in error_message:
                    abort(400, "Username already exists. Please choose a different username.")
                if '(sqlite3.IntegrityError) UNIQUE constraint failed: users.email' in error_message:
                    abort(400, 'That email already exists. Please choose a different email')
        except (ValueError) as valueError:
            abort(400, str(valueError))
        except (NoResultFound) as res:
            abort(400, str(res))
        abort(400, str(error))
       


    def is_valid_email(email):
        if not validate_email(email):
            raise ValueError('Invalid Email. This does not exist.')
        else:
            return email
    def is_valid_username(username):
        if len(username) > 12:
            raise ValueError('Invalid Username. Maximum length exceeded.')
        if len(username) < 6:
            raise ValueError('Username must exceed 6 charachters')
        return username
    
    def is_valid_password(password):
    # Check minimum length of 8 characters
        if len(password) < 8:
            raise ValueError('Invalid Password. Minimum length is 8 characters.')
    
    # Check for at least one uppercase letter
        if not re.search(r'[A-Z]', password):
            raise ValueError('Invalid Password. At least one uppercase letter is required.')
    
    # Check for at least one lowercase letter
        if not re.search(r'[a-z]', password):
            raise ValueError('Invalid Password. At least one lowercase letter is required.')
    
    # Check for at least one digit
        if not re.search(r'\d', password):
            raise ValueError('Invalid Password. At least one digit is required.')
    
    # Check for at least one special character
        if not re.search(r'[^a-zA-Z0-9]', password):
            raise ValueError('Invalid Password. At least one special character is required.')
    
    # All conditions met, password is strong
        return password

    def return_all_users():

        try:
            users = User.query.all()
            if users:
                user_list = [user.json() for user in users]
                
                return jsonify(user_list)
            else:
                raise NoResultFound('You attempted to query an empty database of users')
        except NoResultFound as error:
            abort(400, str(error))
    def delete_user_by_Id(id):
        try:
            user = User.query.filter_by(id=id).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                return jsonify({'note': 'delete success'})
            else:
                raise NoResultFound('Attempted to delete a non existant id')
        except NoResultFound as error:
            abort(400, str(error))
    
    def update_user_information(id, email, username, password):
        try:
            user = User.query.get(id)
            if user:
                user.email = UserService.is_valid_email(email)
                user.username = UserService.is_valid_username(username)
                user.password_hash = UserService.is_valid_password(password)
                db.session.commit()
                return jsonify({'message': 'User information updated successfully'})
            else:
                raise NoResultFound('Attempted to update a non existent user')
        except (NoResultFound, ValueError) as error:
            abort(400, str(error))
    
    def AccountCredentials():
        UserData = UserService.return_all_users()
        formatted_data = json.loads(UserData.data)
        credentialsKey = []
        for item in formatted_data:
            username = item["user_info"]["username"]
            password = item["user_info"]["password_hash"]
            credentialsKey.append({"username": username, "password": password})
        return credentialsKey
    
    def login(username, password):
       
        try:
            UserService.is_valid_username(username)
            UserService.is_valid_password(password)
            user = UserService.authenticate(username, password)
            if user:
        # Generate the JWT token
                access_token = create_access_token(identity=user.id)
                return jsonify({'access_token': access_token})
            else:
                return jsonify({'message': 'Invalid credentials'}), 401
        except(ValueError) as error:
            abort(400, str(error))
    def authenticate(username, password):
    ## check if exists 
    # if so return user
     try:
        user = User.query.filter_by(username=username).first()
        if user is not None:
            if check_password_hash(user.password_hash, password):
                return user
            else:
                raise ValueError("Invalid password")
        else:
            raise ValueError("Invalid username")
     except (SQLAlchemyError, ValueError) as error:
        abort(400, str(error))

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
    
