from validate_email import validate_email
import re
from Models.UserModel import User
from flask import jsonify, abort
from Database.database import db
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
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
        
        except (ValueError, NoResultFound, IntegrityError) as error:
            
            abort(400, str(error))

    def is_valid_email(email):
        if not validate_email(email):
            raise ValueError('Invalid Email. This does not exist.')
        else:
            return email
    def is_valid_username(username):
        if len(username) > 12:
            raise ValueError('Invalid Username. Maximum length exceeded.')
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
    
    