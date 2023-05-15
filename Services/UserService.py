from validate_email import validate_email
import re
from Models.UserModel import User
from flask import jsonify, abort
from Database.database import db

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
            is_valid_email(email)
            is_valid_username(username)
            is_valid_password(password)

            if blog_id is not None: 
                user = User(email=email, username=username, password=password, blog_id=blog_id)
            else:
                user = User(email=email, username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify({'id': user.id, 'user': user.json()})
        except ValueError as error:
            abort(400, str(error))

def is_valid_email(email):
    if not validate_email(email):
        raise ValueError('Invalid Email. This does not exist.')

def is_valid_username(username):
    if len(username) > 12:
        raise ValueError('Invalid Username. Maximum length exceeded.')

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
    return True