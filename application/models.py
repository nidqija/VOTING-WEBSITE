from application import db , login_manager
from sqlalchemy.sql import func 
from flask_login import UserMixin


@login_manager.user_loader      
def load_user(user_id):
      return User.query.get(int(user_id))
      

class User(db.Model , UserMixin ):
        id = db.Column(db.Integer , primary_key = True)
        username = db.Column(db.String(20) , unique = True , nullable = False)
        email = db.Column(db.String(120) , unique = True , nullable = False)
        password = db.Column(db.String(120) , nullable = False)
        createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
        wonders = db.relationship('Post' , backref = 'author' , lazy = True)
        wonders2 = db.relationship('Vote' , backref = 'author' , lazy = True)
        
        def __repr__(self):
           return f'User("{self.username}" , {self.email})'
        
class Post(db.Model , UserMixin):
       id = db.Column(db.Integer , primary_key = True)
       titles = db.Column(db.String(500) , unique = True , nullable = False)
       createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
       question = db.Column(db.Text, nullable = False)
       user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)

       def __repr__(self):
           return f'User("{self.titles}" , {self.question})'
       

class Vote(db.Model , UserMixin):
       id = db.Column(db.Integer , primary_key = True)
       studentName = db.Column(db.String(500) , unique = True , nullable = False)
       studentId = db.Column(db.String(20) , unique = True , nullable = False)
       createdAt = db.Column(db.DateTime(timezone=True) , server_default=func.now())
       otherFaculty = db.Column(db.String(30) , nullable = False)
       reasonCandidate = db.Column(db.Text ,  nullable = False)
       user_id = db.Column(db.Integer , db.ForeignKey('user.id') , nullable = False)
       candidate_name = db.Column(db.String(100))

       
       def vote_query():
             return Vote.query
       

       def __repr__(self):
             return f'User("{self.studentName}" , {self.studentId} ,  {self.otherFaculty} ,  {self.reasonCandidate} , {self.candidate_name})'
       

class Admin(db.Model , UserMixin ):
        id2 = db.Column(db.Integer , primary_key = True)
        username2 = db.Column(db.String(20) , unique = True , nullable = False)
        email2 = db.Column(db.String(120) , unique = True , nullable = False)
        password2 = db.Column(db.String(120) , nullable = False)
        createdAt2 = db.Column(db.DateTime(timezone=True) , server_default=func.now())
        
        def __repr__(self):
           return f'Admin("{self.username2}" , {self.email2})'
      

      

       
      


              
        
       


