from application import db , login_manager
from sqlalchemy.sql import func 
from flask_login import UserMixin


@login_manager.user_loader      
def load_user(user_id):
      return User.query.get(int(user_id))
      

class User(db.Model , UserMixin ):
        id = db.Column(db.Integer , primary_key = True)
        username = db.Column(db.String(20) , unique = True , nullable = False)
        mmu_id = db.Column(db.String(150) , unique = True , nullable = True)
        email = db.Column(db.String(120) , unique = True , nullable = False)
        password = db.Column(db.String(120) , nullable = False)
        createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
        #image_file = db.Column((db.String(20)), nullable=False, default='candidate_image.jpg')
        faculty = db.Column(db.String(5) , nullable = False)
        user_profile_photo = db.Column(db.String() , default = 'user_image.jpg')
        post = db.relationship('Post' , backref = 'author' , lazy = True)
        vote1 = db.relationship('Vote1' , backref = 'user' , lazy = True)
        candidate_entrance = db.relationship('CandidateID' , backref = 'author' , lazy = True)

        
        def _repr_(self):
           return f'User("{self.username}" , {self.email} , {self.mmu_id})'
        

class Post(db.Model , UserMixin):
       id = db.Column(db.Integer , primary_key = True)
       titles = db.Column(db.String(500) , unique = True , nullable = False)
       createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
       question = db.Column(db.Text, nullable = False)
       user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)

       def _repr_(self):
           return f'User("{self.titles}" , {self.question})'
       


class Vote1(db.Model):
      id = db.Column(db.Integer , primary_key = True)
      createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
      author = db.Column(db.Integer , db.ForeignKey('user.id') , nullable=False)
      candidate_id = db.Column(db.Integer , db.ForeignKey('candidate.id') , nullable = False)



class Candidate(db.Model):
      id = db.Column(db.Integer , primary_key = True)
      candidate_name = db.Column(db.String(100) , nullable=False)
      candidate_age = db.Column(db.String(100) , nullable=False)
      candidate_id = db.Column(db.Integer , nullable=False)
      candidate_faculty = db.Column(db.String(100) , nullable=False)
      candidate_level = db.Column(db.String(100) , nullable=False)
      candidate_quote = db.Column(db.String(500) , nullable=False)
      candidate_photo_filename = db.Column(db.String(), default='candidate_image.jpg' , nullable = True)
      candidate_id = db.Column(db.Integer , db.ForeignKey('candidate.id') , nullable = False)
      vote = db.relationship('Vote1' , backref = 'candidate' , lazy = True)
      candidate_resume = db.Column(db.String(), default = 'None')
      candidate_manifesto = db.Column(db.String(500) , nullable=True)

      def _repr_(self):
           return f'Candidate("{self.candidate_name}" ," {self.candidate_id}" ," {self.candidate_age}" , {self.candidate_faculty} ,  {self.candidate_level} , {self.candidate_quote} , {self.candidate_photo_filename} , {self.candidate_resume} , {self.candidate_manifesto})'

       
class Announcement(db.Model , UserMixin):
       id = db.Column(db.Integer , primary_key = True)
       titles = db.Column(db.String(500) , unique = True , nullable = False)
       createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
       description = db.Column(db.Text, nullable = False)

       def _repr_(self):
           return f'User("{self.titles}" , {self.description})'


class SelfDescription(db.Model):
      id = db.Column(db.Integer , primary_key = True)
      user_description = db.Column(db.Text , unique = True , nullable = True)
      user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)


class CandidateID(db.Model):
      id = db.Column(db.Integer , primary_key = True)
      candidate_entrance = db.Column(db.Text , unique = True , nullable = False)
      user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)

