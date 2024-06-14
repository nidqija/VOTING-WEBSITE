from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField , PasswordField , SubmitField , BooleanField , TextAreaField , URLField , SelectField
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError
from application.models import  User





class RegistrationForm(FlaskForm):
    username = StringField('Username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    email = StringField('Email' , validators=[DataRequired() , Email()])
    mmu_id = StringField('Admin ID')
    faculty = SelectField('Faculty', choices=[('FAC', 'FAC'), ('FCA', 'FCA'), ('FCI', 'FCI'), ('FCM', 'FCM'), ('FOE', 'FOE'), ('FOM', 'FOM')])
    password = PasswordField('Password' , validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password' , validators=[DataRequired() , EqualTo('password')])
    user_profile_photo =FileField('Profile Photo' , validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Only images are allowed!')])
    submit = SubmitField('Register')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken , please choose another username!')
        
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken , please choose another email!')
        


class Loginform(FlaskForm):
    username = StringField('Username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    mmu_id = StringField('Admin ID')
    password = PasswordField('Password' , validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class ProfileForm(FlaskForm):
    username = StringField('Username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    email = StringField('Email' , validators=[DataRequired() , Email()])
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


class DescriptionForm(FlaskForm):
    self_description = TextAreaField('Description')
    submit = SubmitField('Submit')


class AnnouncementForm(FlaskForm):
    titles = StringField('Announcement Title' , validators=[DataRequired()])
    description = StringField('Announcement Description' , validators=[DataRequired()])
    submit = SubmitField('Submit')


class CandidateForm(FlaskForm):
    candidate_name = StringField('Candidate Name', validators=[DataRequired(), Length(min=2, max=100)])
    candidate_age = StringField('Candidate Age', validators=[DataRequired(), Length(min=1, max=2)])
    candidate_id = StringField('Candidate ID', validators=[DataRequired(), Length(min=10, max=10)])
    candidate_faculty = SelectField('Candidate Faculty', choices=[('General', 'General'), ('FAC', 'FAC'), ('FCA', 'FCA'), ('FCI', 'FCI'), ('FCM', 'FCM'), ('FOE', 'FOE'), ('FOM', 'FOM')])
    candidate_level = SelectField('Candidate Academic Level', choices=[('Foundation', 'Foundation'), ('Diploma', 'Diploma'), ('Degree', 'Degree')])
    candidate_quote = TextAreaField('Candidate Quote', validators=[DataRequired(), Length(max=500)])
    candidate_photo = FileField('Candidate Photo', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Only images are allowed!')])
    candidate_resume = FileField('Candidate Resume' , validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Only images are allowed!')])
    candidate_manifesto = URLField('Candidate Manifesto (Embed Video URL)')
    submit = SubmitField('Submit')


class CandidateIDForm(FlaskForm):
    candidate_entrance_form = StringField('MMU ID')
    submit = SubmitField('submit')

