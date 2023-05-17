from flask import Blueprint, jsonify
from Models.BlogModel import Blog
from Models.UserModel import User
from Database.database import db
from flask_jwt import jwt_required
from Services.BlogService import BlogService
blog_Blueprint = Blueprint('blog', __name__)

@blog_Blueprint.route('/blog/<int:blog_id>', methods=['GET'])
def return_blog_post(blog_id):
   return BlogService.return_blog_post(blog_id)
# You would have the asasociated user_ID be tied into the blog post. You 

@blog_Blueprint.route('/blog/create/<string:blog_title>/<string:blog_content>/<string:blog_author>/<int:user_id>', methods=['POST'])
def create_blog_post(blog_title, blog_content, blog_author, user_id):
    return BlogService.create_blog_post(blog_title, blog_content, blog_author, user_id)

@blog_Blueprint.route('/blog/delete/<int:blog_id>', methods=['DELETE'])
def delete_blog_post(blog_id):
   return BlogService.delete_blog_post(blog_id)


@blog_Blueprint.route('/blogs', methods=['GET'])
def return_all_blog_posts():
    return BlogService.return_all_blog_posts()


@blog_Blueprint.route('/blog/update/<string:blog_title>/<string:blog_content>/<string:blog_author>/<int:blog_id>', methods=['PUT'])
def update_user_information(id, email, username, password):
    return BlogService.update_user_information(id, email, username, password)