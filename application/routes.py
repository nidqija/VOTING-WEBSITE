from flask import render_template , flash , redirect , url_for 
<<<<<<< HEAD
from application.form import RegistrationForm , Loginform , QuestionForm , VotingForm , CandidateForm
from application.models import User , Post , Vote, Admin
=======
from application.form import RegistrationForm , Loginform , QuestionForm
from application.models import User , Post , Candidate , Vote1 , Vote2 , Candidate2 , Vote3 , Candidate3
>>>>>>> main
from application import app , db , bcrypt
from flask_login import login_user , current_user , logout_user, login_required 


@app.route('/')


@app.route('/home')
def home():
    return render_template('home.html' )


@app.route('/login' , methods = ['POST' , 'GET'])
def login():
    if current_user.is_authenticated:
         return redirect(url_for('home'))
    form = Loginform()
    if form.validate_on_submit():
            flash(f'Login Successful !')
            user = User.query.filter_by(username = form.username.data).first()
            if user and bcrypt.check_password_hash(user.password , form.password.data):
                 login_user(user , remember=form.remember.data)
                 return redirect(url_for('home'))
            else:
                 flash(f'Login Failed . Please check username and password' , 'danger')
    return render_template('login.html', form = form)


@app.route('/register' , methods = ['POST' , 'GET'])

def register():
    
         
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data , email = form.email.data , password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data} !' , 'success!')
        return redirect(url_for('login'))
    return render_template('register.html' , form = form)


@app.route('/logout')
def logout():
     logout_user()
     return redirect(url_for('home'))


@app.route('/contact')
def contact():
     return render_template('contact.html')



@app.route('/candidates/first/' , methods = [ 'GET' , 'POST'])
@login_required

def candidates():
     candidate1 = Candidate.query.all()
     return render_template('candidates.html' , candidate1 = candidate1)
     
    



@app.route('/vote-candidate/<candidate_id>' , methods = ['GET'])
@login_required

def vote(candidate_id):
     candidate1 = Candidate.query.filter_by(id = candidate_id)
     votes1 = Vote1.query.filter_by( author = current_user.id , candidate_id = candidate_id).first()
     if not candidate1:
          flash('Candidate does not exist' , category='error')
     else:
          votes1 = Vote1(author = current_user.id , candidate_id = candidate_id)
          db.session.add(votes1)
          db.session.commit()

     return redirect(url_for('candidate2'))


@app.route('/candidates/second/' , methods = [ 'GET' , 'POST'])
@login_required

def candidate2():
     candidate2 = Candidate2.query.all()
     return render_template('candidates.html' , candidate2 = candidate2)



@app.route('/vote-candidate2/<candidate2_id>')
@login_required

def vote2(candidate2_id):
     candidate2 = Candidate2.query.filter_by(id = candidate2_id)
     votes2 = Vote2.query.filter_by( author = current_user.id , candidate2_id = candidate2_id).first()

     if not candidate2:
          flash('Candidate does not exist' , category='error')

     else:
          votes2 = Vote2(author = current_user.id , candidate2_id = candidate2_id)
          db.session.add(votes2)
          db.session.commit()

     return redirect(url_for('candidate3'))




@app.route('/candidates/third/' , methods = [ 'GET' , 'POST'])
@login_required

def candidate3():
     candidate3 = Candidate3.query.all()
     return render_template('candidates.html' , candidate3 = candidate3)





@app.route('/vote-candidate3/<candidate3_id>')
@login_required

def vote3(candidate3_id):
     candidate2 = Candidate2.query.filter_by(id = candidate3_id)
     votes3 = Vote3.query.filter_by( author = current_user.id , candidate3_id = candidate3_id).first()

     if not candidate2:
          flash('Candidate does not exist' , category='error')

     else:
          votes3 = Vote3(author = current_user.id , candidate3_id = candidate3_id)
          db.session.add(votes3)
          db.session.commit()

     return redirect(url_for('home'))







@app.route('/guidelines')
def guidelines():
     return render_template('guidelines.html')


@app.route('/service/new' ,  methods = ['POST' , 'GET'])
@login_required

def service():
     posts = Post.query.all()
     form = QuestionForm()
     if form.validate_on_submit():
          post = Post(titles = form.titles.data , question = form.question.data , author = current_user )
          db.session.add(post)
          db.session.commit()
          flash('Your question is created!' , 'success')
          return redirect(url_for('service'))
     return render_template('service.html' ,  form = form , posts = posts)



@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/about')
def about():
     return render_template('about.html')

@app.route('/admin_homepage')
def adminHomepage():
     candidate1 = Candidate.query.all()
     candidate2 = Candidate2.query.all()
     candidate3 = Candidate3.query.all()
     return render_template('admin_homepage.html' , candidate1 = candidate1 , candidate2 = candidate2 , candidate3 = candidate3)


@app.route('/update_announcement')
def updateAnnouncement():
         
         
    form = AnnouncementForm()

    if form.validate_on_submit():
        announcement = Announcement(titles=form.titles.data , description = form.description.data)
        db.session.add(announcement)
        db.session.commit()
        return redirect(url_for('update_announcement'))
    return render_template('update_announcement.html', form=form)


@app.route('/info_candidates')
def candidatesInfo():
     return render_template('info_candidates.html')


@app.route('/createpoll')
def createVote():
     return render_template('create_a_vote.html')


@app.route('/admin_register' , methods = ['POST' , 'GET'])

def adminregister():
    
         
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password2.data).decode('utf-8')
        admin = Admin(username2=form.username2.data , email2 = form.email2.data , password2 = hashed_password)
        db.session.add(admin)
        db.session.commit()
        flash(f'Account created for {form.username2.data} !' , 'success!')
        return redirect(url_for('login'))
    return render_template('admin_register.html' , form = form)    


@app.route('/submitvote')
def submitvote():
     return render_template('submitvote.html')


     
