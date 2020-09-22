from . import db
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password = db.Column(db.String(255))
    

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    product = db.Column(db.String(255))
    price = db.Column(db.Integer)
    market = db.Column(db.String(255))
    product_info = db.Column(db.Text())
    votes = db.Column(db.Integer)
    
    def __repr__(self):
        return f'Product {self.product}'