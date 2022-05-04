from flask import Flask
from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from connectflow.users.models import User

# 로그인 폼
class LoginForm(FlaskForm): 
    number_ktis = StringField('아이디(사번)', validators=[DataRequired()])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    submit = SubmitField('로그인')

# 회원가입 폼
class RegisterationForm(FlaskForm): 
    number_ktis = StringField('아이디(사번)', validators=[DataRequired()])
    name = StringField('성명', validators=[DataRequired()])
    email = StringField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password_confirm', message='비밀번호가 일치하지 않습니다.')])
    password_confirm = PasswordField('비밀번호 확인', validators=[DataRequired()])
    submit = SubmitField('회원가입')
    