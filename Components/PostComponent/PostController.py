from flask import Blueprint, jsonify
from flask_jwt import jwt_required
from ..PostComponent.PostService import ServicePost

post_Blueprint = Blueprint('post', __name__)

@post_Blueprint.route('/post/<int:post_id>', methods=['GET'])
def return_blog_post(blog_id):
   return ServicePost.return_blog_post(blog_id)
# You would have the asasociated user_ID be tied into the blog post. You 

@post_Blueprint.route('/post/create/<string:post_title>/<string:post_content>/<string:post_author>/<int:user_id>', methods=['POST'])
def create_blog_post(blog_title, blog_content, blog_author, user_id):
    return ServicePost.create_blog_post(blog_title, blog_content, blog_author, user_id)

@post_Blueprint.route('/post/delete/<int:post_id>', methods=['DELETE'])
def delete_blog_post(blog_id):
   return ServicePost.delete_blog_post(blog_id)


@post_Blueprint.route('/posts', methods=['GET'])
def return_all_blog_posts():
    return ServicePost.return_all_blog_posts()


@post_Blueprint.route('/post/update/<string:post_title>/<string:post_content>/<string:post_author>/<int:post_id>', methods=['PUT'])
def update_user_information(id, email, username, password):
    return ServicePost.update_user_information(id, email, username, password)