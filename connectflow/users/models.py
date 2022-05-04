from enum import unique
from turtle import position
from connectflow import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# 사용자가 템플릿에서 인증되었는지를 확인
@login_manager.user_loader
def load_user(user_id) : 
    return User.query.get(user_id)

class User(db.Model, UserMixin): 
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png')
    status = db.Column(db.String(10), index=True)
    name = db.Column(db.String(10), index=True)
    title = db.Column(db.String(10), index=True)
    level = db.Column(db.String(10), index=True)
    position = db.Column(db.String(10), index=True)
    number_ktis = db.Column(db.String(7), unique=True, index=True)
    number_kt = db.Column(db.String(8), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, name, number_ktis, email, password) : 
        self.name = name
        self.number_ktis = number_ktis
        self.email = email 
        self.password_hash = generate_password_hash(password)

    def check_password(self, password) : 
        return check_password_hash(self.password_hash, password)

    def __repr__(self) : 
        return f'[사용자] : {self.name}({self.number_ktis})'