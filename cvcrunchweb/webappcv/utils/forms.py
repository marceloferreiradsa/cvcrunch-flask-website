from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from .models import User

class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    conf_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password', message="Passwords Must Match")])
    submit = SubmitField('Sign Up')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email already in use!")
        
    def check_username(self, field):
        if User.query.filter_by(user_name=field.data).first():
            raise ValidationError("Your username has been already used!")
        
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class ResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Token')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    conf_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password', message="Passwords Must Match")])
    submit = SubmitField('Reset Password')
