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
        image_file = db.Column((db.String(20)), nullable=False, default='candidate_image.jpg')
        faculty = db.Column(db.String(5) , nullable = False)
        post = db.relationship('Post' , backref = 'author' , lazy = True)
        vote1 = db.relationship('Vote1' , backref = 'user' , lazy = True)
        #vote2 = db.relationship('Vote2' , backref = 'user' , lazy = True)
        #vote3 = db.relationship('Vote3' , backref = 'user' , lazy = True)
        announcement = db.relationship('Announcement' , backref = 'author' , lazy = True)       

        
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
      # candidate_type = db.Column(db.String(100) , nullable=False)
      candidate_level = db.Column(db.String(100) , nullable=False)
      candidate_quote = db.Column(db.String(500) , nullable=False)
      candidate_photo_filename = db.Column(db.String(100), default='candidate_image.jpg')
      candidate_id = db.Column(db.Integer , db.ForeignKey('candidate.id') , nullable = False)
      candidate_position = db.Column(db.String(500) , nullable=False)
      vote = db.relationship('Vote1' , backref = 'candidate' , lazy = True)
      image_file = db.Column((db.String(20)), nullable=False, default='candidate_image.jpg')
      candidate_resume = db.Column(db.String(), default = 'None')

      def _repr_(self):
           return f'Candidate("{self.candidate_name}" , {self.candidate_id})'



#class Vote2(db.Model):
#      id = db.Column(db.Integer , primary_key = True)
#      createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
#      author = db.Column(db.Integer , db.ForeignKey('user.id') , nullable=False)
#      candidate2_id = db.Column(db.Integer , db.ForeignKey('candidate2.id') , nullable = False)



#class Candidate2(db.Model):
#      id = db.Column(db.Integer , primary_key = True)
#      candidate_name = db.Column(db.String(100))
#      candidate_age = db.Column(db.String(100))
#      candidate_description = db.Column(db.String(500))
#      vote2 = db.relationship('Vote2' , backref = 'candidate2' , lazy = True)
#      image_file = db.Column((db.String(20)), nullable=False, default='candidate_image.jpg')


#class Vote3(db.Model):
#      id = db.Column(db.Integer , primary_key = True)
#      createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
#      author = db.Column(db.Integer , db.ForeignKey('user.id') , nullable=False)
#      candidate3_id = db.Column(db.Integer , db.ForeignKey('candidate3.id') , nullable = False)


#class Candidate3(db.Model):
#      id = db.Column(db.Integer , primary_key = True)
#      candidate_name = db.Column(db.String(100))
#      candidate_age = db.Column(db.String(100))
#      candidate_description = db.Column(db.String(500))
#      vote3 = db.relationship('Vote3' , backref = 'candidate3' , lazy = True)
#      image_file = db.Column((db.String(20)), nullable=False, default='candidate_image.jpg')

       
class Announcement(db.Model , UserMixin):
       id = db.Column(db.Integer , primary_key = True)
       titles = db.Column(db.String(500) , unique = True , nullable = False)
       createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
       description = db.Column(db.Text, nullable = False)
       user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)

       def _repr_(self):
           return f'User("{self.titles}" , {self.description})'

    

class Admin(db.Model , UserMixin ):
        id2 = db.Column(db.Integer , primary_key = True)
        username2 = db.Column(db.String(20) , unique = True , nullable = False)
        email2 = db.Column(db.String(120) , unique = True , nullable = False)
        mmu_id = db.Column(db.String(150) , unique = True , nullable = False)
        password2 = db.Column(db.String(120) , nullable = False)
        createdAt2 = db.Column(db.DateTime(timezone=True) , server_default=func.now())

        def _repr_(self):
           return f'Admin("{self.username2}" , {self.email2} , {self.mmu_id})'


class SelfDescription(db.Model):
      id = db.Column(db.Integer , primary_key = True)
      user_description = db.Column(db.Text , unique = True , nullable = True)
      user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)