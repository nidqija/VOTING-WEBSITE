from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField , BooleanField
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError
from application.models import User



class RegistrationForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    email = StringField('email' , vawpilidators=[DataRequired() , Email()])
    password = PasswordField('password' , validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password' , validators=[DataRequired() , EqualTo('password')])
    submit = SubmitField('register')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken , please choose another username!')
        
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken , please choose another email!')
        


class Loginform(FlaskForm):
    username = StringField('username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    password = PasswordField('password' , validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

# This is for admin
    
class AdminLoginForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    password = PasswordField('password' , validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class AdminRegistrationForm(FlaskForm):
    mmuid = StringField('MmuID' , validators=[DataRequired() , Length(min=2 , max= 20)])
    confirmmmuid = StringField('ConfirmMmuID' , validators=[DataRequired() , Length(min=2 , max= 20)])
    email = StringField('GmailInput' , vawpilidators=[DataRequired() , Email()])
    password = PasswordField('PasswordInput' , validators=[DataRequired()])
    confirmpassword = PasswordField('ComfirmPasswordInput' , validators=[DataRequired() , EqualTo('password')])
    submit = SubmitField('register')

    def validate_username(self,mmuid):
        user = User.query.filter_by(mmuid=mmuid.data).first()
        if user:
            raise ValidationError('That username is taken , please choose another username!')
        
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken , please choose another email!')