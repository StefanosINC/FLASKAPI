from Database.database import db


class Blog(db.Model):
    __tablename__ = 'blog'

    blog_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blog_title = db.Column(db.String(64))
    blog_content = db.Column(db.Text)
   #blog_comments = db.Column(db.string(150))
    blog_author = db.Column(db.String(64))
   # blog_upvote = db.Column(db.Integer)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=None)

    def __init__(self, blog_title, blog_content, blog_author, user_id=None):
        self.blog_title = blog_title
        self.blog_content = blog_content
       # self.blog_comments = blog_comments
        self.blog_author = blog_author
       # self.blog_upvote = blog_upvote
        self.user_id = user_id

    def json(self):
        return {
        'blog_info': {
            'blog_id': self.blog_id,
            'user_id': self.user_id,
            'blog_title': self.blog_title,
            'blog_content': self.blog_content,
            'blog_author': self.blog_author
        }
    }