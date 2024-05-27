from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed , FileRequired
from flask_login import current_user
from application import db , app
from wtforms import StringField , PasswordField , SubmitField , BooleanField , TextAreaField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError
from application.models import  User , Admin , Candidate





class RegistrationForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    email = StringField('email' , validators=[DataRequired() , Email()])
    mmu_id = StringField('Admin ID')
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
    mmu_id = StringField('Admin ID')
    password = PasswordField('password' , validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class ProfileForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    email = StringField('email' , validators=[DataRequired() , Email()])
    submit = SubmitField('Enter')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken , please choose another username!')
        
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken , please choose another email!')
        


class QuestionForm(FlaskForm):
    titles = TextAreaField('Title' , validators=[DataRequired()])
    question = TextAreaField('Question' , validators=[DataRequired()])
    submit = SubmitField('Post')


class AdminRegistrationForm(FlaskForm):
    username2 = StringField('Admin name' , validators=[DataRequired() , Length(min=2 , max= 20)])
    email2 = StringField('Admin email' , validators=[DataRequired() , Email()])
    mmu_id = StringField('Admin ID' , validators=[DataRequired() , Length(min=2 , max=20)])
    password2 = PasswordField('Password' , validators=[DataRequired()])
    confirmpassword2 = PasswordField('Confirm Password' , validators=[DataRequired() , EqualTo('password2')])
    submit2 = SubmitField('register')

    def validate_username2(self, username2):
        admin = Admin.query.filter_by(username2=username2.data).first()
        if admin:
            raise ValidationError('That username is taken , please choose another username!')

    def validate_email2(self, email2):
        admin = Admin.query.filter_by(email2=email2.data).first()
        if admin:
            raise ValidationError('That email is taken , please choose another email!')


class DescriptionForm(FlaskForm):
    self_description = TextAreaField('Description')
    submit = SubmitField('Submit')



class AdminLoginform(FlaskForm):
    username2 = StringField('username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    password2 = PasswordField('password' , validators=[DataRequired()])
    mmu_id = StringField('Admin ID' , validators=[DataRequired() , Length(min=2 , max=20)])
    remember2 = BooleanField('Remember me')
    submit2 = SubmitField('Login')

class AdminLoginform(FlaskForm):
    username2 = StringField('username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    password2 = PasswordField('password' , validators=[DataRequired()])
    mmu_id = StringField('Admin ID', validators=[DataRequired(), Length(min=2, max=20)])
    remember2 = BooleanField('Remember me')
    submit2 = SubmitField('Login')


class AnnouncementForm(FlaskForm):
    titles = StringField('Announcement Title' , validators=[DataRequired()])
    description = StringField('Announcement Description' , validators=[DataRequired()])
    submit = SubmitField('Submit')


class CandidateForm(FlaskForm):
    candidate_name = StringField('Candidate Name', validators=[DataRequired(), Length(min=2, max=100)])
    candidate_age = StringField('Candidate Age', validators=[DataRequired()])
    candidate_id = StringField('Candidate ID', validators=[DataRequired()])
    candidate_faculty = StringField('Candidate Faculty', validators=[DataRequired()])
    candidate_level = StringField('Candidate Academic Level', validators=[DataRequired()])
    candidate_quote = TextAreaField('Candidate Quote', validators=[DataRequired(), Length(max=500)])
    candidate_photo = FileField('Candidate Photo', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Only images are allowed!')])
    submit = SubmitField('Submit')

    def validate_candidate_name(self, candidate_name):
        candidate = Candidate.query.filter_by(candidate_name=candidate_name.data).first()
        if candidate:
            raise ValidationError('This candidate is already registered!')

    def validate_candidate_id(self, candidate_id):
        candidate = Candidate.query.filter_by(candidate_id=candidate_id.data).first()
        if candidate:
            raise ValidationError('This candidate ID is already registered!')