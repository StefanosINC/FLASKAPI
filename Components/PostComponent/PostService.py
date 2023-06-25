
from ..PostComponent.PostModel import Post
from flask import jsonify
from ..UserComponent.UserModel import User
from Database.database import db
import requests

class ServicePost: 
    def return_blog_post(blog_id):
        post = Post.query.filter_by(blog_id=blog_id).first() # Query for the Blog ID
        if post: ## if post exists
            return jsonify(post.json())
        else:
            return jsonify({'name': None}), 404
    
    def create_blog_post(blog_title, blog_content, blog_author, user_id):
        Validate_User_Id = User.query.filter_by(id=user_id).first()
        if Validate_User_Id:
            post = Post(blog_title=blog_title, blog_content=blog_content,blog_author=blog_author, user_id=user_id)
            db.session.add(post)
            db.session.commit()
            return jsonify({'post': post.json()})
        else:
            return jsonify({'message': 'User ID does not exist cant create blog post'})

    def delete_blog_post(blog_id):
        post = Post.query.filter_by(blog_id=blog_id).first()
        if post:
            db.session.delete(post)
            db.session.commit()
            return jsonify({'note': 'delete success'})
        else:
            return jsonify({'note': 'post not found'}), 404
    
    def update_user_information(id, email, username, password):
        user = Post.query.get(id)
        if user:
            user.email = email
            user.username = username
            user.password_hash = password
            db.session.commit()
            return jsonify({'message': 'User information updated successfully'})
        else:
            return jsonify({'message': 'User not found'})

    def return_all_blog_posts():
        posts = Post.query.all()
        if posts:    
            post_list = [posts.json() for posts in posts]
            return jsonify(post_list)
        else:
            return jsonify({'name': None}), 404


