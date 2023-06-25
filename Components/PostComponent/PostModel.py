from Database.database import db


class Post(db.Model):
    __tablename__ = 'post'

    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_title = db.Column(db.String(64))
    post_content = db.Column(db.Text)
    post_author = db.Column(db.String(64))
   
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=None)

    def __init__(self, post_title, post_content, post_author, user_id=None):
        self.post_title = post_title
        self.post_content = post_content
       # self.blog_comments = blog_comments
        self.post_author = post_author
       # self.blog_upvote = blog_upvote
        self.user_id = user_id

    def json(self):
        return {
        'post_info': {
            'post_id': self.post_id,
            'user_id': self.user_id,
            'post_title': self.post_title,
            'post_content': self.post_content,
            'post_author': self.post_author
        }
    }