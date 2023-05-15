from flask import Blueprint, jsonify
from Models.BlogModel import Blog
from Models.UserModel import User
from Database.database import db
from flask_jwt import jwt_required
blog_Blueprint = Blueprint('blog', __name__)

@blog_Blueprint.route('/blog/<int:blog_id>', methods=['GET'])
def return_blog_post(blog_id):
    post = Blog.query.filter_by(blog_id=blog_id).first() # Query for the Blog ID
    if post: ## if post exists
        return jsonify(post.json())
    else:
        return jsonify({'name': None}), 404
    
# You would have the asasociated user_ID be tied into the blog post. You 
@blog_Blueprint.route('/blog/create/<string:blog_title>/<string:blog_content>/<string:blog_author>/<int:user_id>', methods=['POST'])
def create_blog_post(blog_title, blog_content, blog_author, user_id):
    ## Add a search for the user ID 
    Validate_User_Id = User.query.filter_by(id=user_id).first()
    if Validate_User_Id:
            post = Blog(blog_title=blog_title, blog_content=blog_content,blog_author=blog_author, user_id=user_id)
            db.session.add(post)
            db.session.commit()
    else:
        return jsonify({'message': 'User ID does not exist cant create blog post'})

    return jsonify({'post': post.json()})



@blog_Blueprint.route('/blog/delete/<int:blog_id>', methods=['DELETE'])
def delete_blog_post(blog_id):
    post = Blog.query.filter_by(blog_id=blog_id).first()
    if post:
        db.session.delete(post)
        db.session.commit()
        return jsonify({'note': 'delete success'})
    else:
        return jsonify({'note': 'post not found'}), 404


@blog_Blueprint.route('/blogs', methods=['GET'])
def return_all_blog_posts():
    posts = Blog.query.all()
    if posts:    
        post_list = [posts.json() for posts in posts]
        return jsonify(post_list)
    else:
        return jsonify({'name': None}), 404


@blog_Blueprint.route('/blog/update/<string:blog_title>/<string:blog_content>/<string:blog_author>/<int:blog_id>', methods=['PUT'])
def update_user_information(id, email, username, password):
    user = Blog.query.get(id)
    if user:
        user.email = email
        user.username = username
        user.password_hash = password
        db.session.commit()
        return jsonify({'message': 'User information updated successfully'})
    else:
        return jsonify({'message': 'User not found'})