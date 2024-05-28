from flask import render_template , flash , redirect , url_for , abort , request
from application.form import RegistrationForm , Loginform , QuestionForm, AnnouncementForm, AdminRegistrationForm, AdminLoginform , CandidateForm
from application.models import User , Post , Candidate , Vote1 , Admin, Announcement
from application import app , db , bcrypt
import os
from flask_login import login_user , current_user , logout_user, login_required
from werkzeug.utils import secure_filename



@app.route('/')


@app.route('/home')
def home():
    announcements = Announcement.query.all()
    return render_template('home.html' , announcements = announcements )


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
        user = User(username=form.username.data , email = form.email.data , faculty = form.faculty.data , password = hashed_password)
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
     candidate2 = Candidate.query.all()
     return render_template('candidates.html' , candidate2 = candidate2)



@app.route('/vote-candidate2/<candidate_id>')
@login_required

def vote2(candidate_id):
     candidate2 = Candidate.query.filter_by(id = candidate_id)
     votes2 = Vote1.query.filter_by( author = current_user.id , candidate_id = candidate_id).first()

     if not candidate2:
          flash('Candidate does not exist' , category='error')

     else:
          votes2 = Vote1(author = current_user.id , candidate_id = candidate_id)
          db.session.add(votes2)
          db.session.commit()

     return redirect(url_for('candidate3'))




@app.route('/candidates/third/' , methods = [ 'GET' , 'POST'])
@login_required

def candidate3():
     candidate3 = Candidate.query.all()
     return render_template('candidates.html' , candidate3 = candidate3)





@app.route('/vote-candidate3/<candidate_id>')
@login_required

def vote3(candidate_id):
     candidate2 = Candidate.query.filter_by(id = candidate_id)
     votes3 = Vote1.query.filter_by( author = current_user.id , candidate_id = candidate_id).first()

     if not candidate2:
          flash('Candidate does not exist' , category='error')

     else:
          votes3 = Vote1(author = current_user.id , candidate_id = candidate_id)
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
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     return render_template('admin_homepage.html' , candidate1 = candidate1)


@app.route('/update_announcement' , methods = ['POST' , 'GET'])
def updateAnnouncement():
         
         
    form = AnnouncementForm()

    if form.validate_on_submit():
        announcement = Announcement(titles = form.titles.data , description = form.description.data , author = current_user)
        db.session.add(announcement)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update_announcement.html', form=form)


@app.route('/info_candidates' , methods = ['POST' , 'GET']) 
def candidatesInfo():
     candidate1 = Candidate.query.all()
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
     return render_template('info_candidates.html', candidate1=candidate1, image_file=image_file)


@app.route('/createpoll')
def createVote():
     return render_template('create_a_vote.html')


@app.route('/admin_register' , methods = ['POST' , 'GET'])

def adminregister():
    
         
    form = AdminRegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password2.data).decode('utf-8')
        admin = Admin(username2=form.username2.data , email2 = form.email2.data , mmu_id = form.mmu_id.data , password2 = hashed_password)
        db.session.add(admin)
        db.session.commit()
        flash(f'Account created for {form.username2.data} !' , 'success!')
        return redirect(url_for('adminlogin'))
    return render_template('admin_register.html' , form = form)
    


@app.route('/admin_login' , methods = ['POST' , 'GET'])
def adminlogin():
    if current_user.is_authenticated:
         return redirect(url_for('adminHomepage'))
    
    form = AdminLoginform()
    if form.validate_on_submit():
            flash(f'Login Successful !')
            admin = Admin.query.filter_by(username2 = form.username2.data).first()
            if admin and bcrypt.check_password_hash(admin.password2 , form.password2.data):
                 # login_user(admin , remember=form.remember2.data)(got problem)
                 return redirect(url_for('adminHomepage'))
            else:
                 flash(f'Login Failed . Please check admin name and password' , 'danger')
    return render_template('admin_login.html', form = form)



@app.route('/submitvote')
def submitvote():
     return render_template('submitvote.html')


@app.route('/viewusers')
@login_required

def viewUsers():
     users = User.query.all()
     return render_template('view_users.html' , users = users)


@app.route('/candidate_form' , methods = ['POST' , 'GET']) 
def candidatesform():

     form = CandidateForm()

     if form.validate_on_submit():
          photo_filename = None
          if form.candidate_photo.data:
               photo = form.candidate_photo.data
               photo_filename = secure_filename(photo.filename)
               photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_filename))

          candidate = Candidate(candidate_name = form.candidate_name.data, candidate_age = form.candidate_age.data, candidate_id = form.candidate_id.data, candidate_faculty = form.candidate_faculty.data, candidate_level = form.candidate_level.data, candidate_quote = form.candidate_quote.data, candidate_position = form.candidate_position.data, image_file = photo_filename)
          db.session.add(candidate)
          db.session.commit()
          flash('Candidate information has been filled up successfully!', 'success')
          return redirect(url_for('adminHomepage'))

     return render_template('candidate_form.html', form=form)



@app.route('/candidate_biodata/<int:candidate_id>')
@login_required
def candidate_biodata(candidate_id):
   candidate = Candidate.query.get_or_404(candidate_id)
   return render_template('candidate_biodata.html' , candidate_name = candidate.candidate_name, candidate = candidate)