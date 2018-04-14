from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(225))
    pass_secure = db.Column(db.String(225))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User{self.username}'