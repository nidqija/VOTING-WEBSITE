from flask_wtf import FlaskForm
from flask_login import current_user
from application import db
from wtforms import StringField , PasswordField , SubmitField , BooleanField , TextAreaField 
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError
from application.models import  User, Admin




class RegistrationForm(FlaskForm):
    username = StringField('username' , validators=[DataRequired() , Length(min=2 , max= 20)])
    email = StringField('email' , validators=[DataRequired() , Email()])
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


class VotingForm(FlaskForm):
      studentName= StringField('StudentName' , validators=[DataRequired()])
      studentId = StringField('StudentID' , validators=[DataRequired()])
      otherFaculties = StringField('OtherFaculty' , validators=[DataRequired()])
      reasonCandidate = StringField('ReasonCandidate' , validators=[DataRequired()])
      submit = SubmitField('Vote')


class Candidate(db.Model):
      id = db.Column(db.Integer , primary_key = True)
      candidate_name = db.Column(db.String(100))
      
def candidate_query():
      return Candidate.query

class CandidateForm(FlaskForm):
      candidates = QuerySelectField(query_factory = candidate_query, allow_blank=True)


class RegistrationForm(FlaskForm):
    username = StringField('Admin name' , validators=[DataRequired() , Length(min=2 , max= 20)])
    email = StringField('Admin email' , validators=[DataRequired() , Email()])
    password = PasswordField('password' , validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password' , validators=[DataRequired() , EqualTo('password')])
    submit = SubmitField('register')

    def validate_adminname(self,username):
        admin = Admin.query.filter_by(username=username.data).first()
        if admin:
            raise ValidationError('That admin name is taken , please choose another username!')
        
    def validate_email(self,email):
        admin = Admin.query.filter_by(email=email.data).first()
        if admin:
            raise ValidationError('That admin email is taken , please choose another email!')