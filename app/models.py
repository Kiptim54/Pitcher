from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    about_me =db.Column(db.String(140))
    last_seen=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'User{self.username}'

class Post(db.Model):
    __tablename__='posts'
    id = db.Column(db.Integer,primary_key = True)
    post = db.Column(db.String(225), primary_key=True)
    category = db.Column(db.String(140))

    def __repr__(self):
        return f'Post{self.post}'