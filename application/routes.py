from flask import render_template , flash , redirect , url_for , abort , request
from application.form import RegistrationForm , Loginform , QuestionForm, AnnouncementForm, AdminRegistrationForm, AdminLoginform , CandidateForm , PrivateConvoForm
from application.models import User , Post , Candidate , Vote1 , Admin, Announcement , PrivateConvo
from application import app , db , bcrypt
import os
from flask_login import login_user , current_user , logout_user, login_required
from werkzeug.utils import secure_filename
import uuid as uuid



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

@app.route('/general_candidate_form' , methods = ['POST' , 'GET']) 
def generalcandidatesform():

     form = CandidateForm()

     if form.validate_on_submit():
          photo_filename = None
          if form.candidate_photo.data:
               photo = form.candidate_photo.data
               photo_filename = secure_filename(photo.filename)
               photo.save(os.path.join(app.config['UPLOADED_FOLDER'], photo_filename))


          if form.candidate_resume.data:
               candidate_resume = form.candidate_resume.data
               resume_filename = secure_filename(candidate_resume.filename)
               candidate_resume.save(os.path.join(app.config['UPLOAD_FOLDER'], resume_filename))
          else:
               resume_filename = None

          candidate = Candidate(candidate_name = form.candidate_name.data, candidate_age = form.candidate_age.data, candidate_id = form.candidate_id.data, candidate_faculty = form.candidate_faculty.data, candidate_level = form.candidate_level.data, candidate_quote = form.candidate_quote.data, candidate_position = form.candidate_position.data , candidate_achievements = form.candidate_achievements.data , candidate_qualifications = form.candidate_qualifications.data , candidate_resume = resume_filename)
          db.session.add(candidate)
          db.session.commit()
          flash('Candidate information has been filled up successfully!', 'success')
          return redirect(url_for('adminHomepage'))

     return render_template('general_candidate_form.html', form=form)


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


@app.route('/service/<int:post_id>')

def question(post_id):
   post = Post.query.get_or_404(post_id)
   return render_template('question.html' , titles = post.titles , post = post)


@app.route('/service/<int:post_id>/update' , methods = ['POST' , 'GET'])
@login_required
def update_question(post_id):
   post = Post.query.get_or_404(post_id)
   if post.author != current_user:
        return abort(403)
   
   form = QuestionForm()
   if form.validate_on_submit():
        post.titles = form.titles.data
        post.question = form.question.data
        db.session.commit()
        return redirect(url_for('service'))
   form.titles.data = post.titles
   form.question.data = post.question
   return render_template('service.html' , form = form)


@app.route('/service/<int:post_id>/delete' , methods = ['POST' , 'GET'])
@login_required
def delete_question(post_id):
     post = Post.query.get_or_404(post_id)
     if post.author != current_user:
        return abort(403)

     db.session.delete(post)
     db.session.commit()
     flash('Your post has been deleted!' , 'success')
     return redirect(url_for('service'))







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


@app.route('/leaderboard_general')
def leaderboard_general():
     candidate1 = Candidate.query.all()
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     return render_template('leaderboard_general.html' , candidate1 = candidate1)


@app.route('/leaderboard_FAC')
def leaderboard_FAC():
     candidate1 = Candidate.query.all()
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     return render_template('leaderboard_FAC.html' , candidate1 = candidate1)


@app.route('/leaderboard_FCA')
def leaderboard_FCA():
     candidate1 = Candidate.query.all()
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     return render_template('leaderboard_FCA.html' , candidate1 = candidate1)


@app.route('/leaderboard_FCI')
def leaderboard_FCI():
     candidate1 = Candidate.query.all()
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     return render_template('leaderboard_FCI.html' , candidate1 = candidate1)


@app.route('/leaderboard_FCM')
def leaderboard_FCM():
     candidate1 = Candidate.query.all()
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     return render_template('leaderboard_FCM.html' , candidate1 = candidate1)


@app.route('/leaderboard_FOE')
def leaderboard_FOE():
     candidate1 = Candidate.query.all()
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     return render_template('leaderboard_FOE.html' , candidate1 = candidate1)


@app.route('/leaderboard_FOM')
def leaderboard_FOM():
     candidate1 = Candidate.query.all()
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     return render_template('leaderboard_FOM.html' , candidate1 = candidate1)


@app.route('/update_announcement' , methods = ['POST' , 'GET'])
def updateAnnouncement():
         
    announcements = Announcement.query.all()     
    form = AnnouncementForm()

    if form.validate_on_submit():
        announcement = Announcement(titles = form.titles.data , description = form.description.data )
        db.session.add(announcement)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update_announcement.html', form=form, announcements=announcements)


@app.route('/service/<int:announcement_id>')

def update_announcement(announcement_id):
   announcement = Announcement.query.get_or_404(announcement_id)
   return render_template('update_announcement.html' , titles = announcement.titles , announcement=announcement)


@app.route('/update_announcement/<int:announcement_id>/edit' , methods = ['POST' , 'GET'])
def edit_announcement(announcement_id):
   announcement = Announcement.query.get_or_404(announcement_id)
   
   form = AnnouncementForm()
   if form.validate_on_submit():
        announcement.titles = form.titles.data
        announcement.description = form.description.data
        db.session.commit()
        return redirect(url_for('updateAnnouncement'))
   form.titles.data = announcement.titles
   form.description.data = announcement.description
   return render_template('update_announcement2.html' , form = form)


@app.route('/update_announcement/<int:announcement_id>/delete' , methods = ['POST' , 'GET'])

def delete_announcement(announcement_id):
     announcement = Announcement.query.get_or_404(announcement_id)

     db.session.delete(announcement)
     db.session.commit()
     flash('Your post has been deleted!' , 'success')
     return redirect(url_for('updateAnnouncement'))

@app.route('/info_candidates' , methods = ['POST' , 'GET']) 
def candidatesInfo():
     candidate1 = Candidate.query.all()
     #candidate2 = Candidate2.query.all()
     #candidate3 = Candidate3.query.all()
     #image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
     return render_template('info_candidates.html', candidate1=candidate1)


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


def viewUsers():
     users = User.query.all()
     admins = Admin.query.all()
     return render_template('view_users.html' , users = users , admins = admins)


@app.route('/candidate_form' , methods = ['POST' , 'GET']) 
def candidatesform():

     form = CandidateForm()

     if form.validate_on_submit():
     
          if form.candidate_photo.data:
               photo = form.candidate_photo.data
               photo_filename = secure_filename(photo.filename)
               photo_name = str(uuid.uuid1()) + '_' + photo_filename
               photo.save(os.path.join(app.config['UPLOADED_FOLDER'], photo_name))
          else:
               photo_name = None

          
          if form.candidate_resume.data:
               candidate_resume = form.candidate_resume.data
               resume_filename = secure_filename(candidate_resume.filename)
               resume_name = str(uuid.uuid1()) + '_' + resume_filename
               candidate_resume.save(os.path.join(app.config['UPLOAD_FOLDER'], resume_name))
          else:
               resume_name = None

          candidate = Candidate(candidate_name = form.candidate_name.data, candidate_age = form.candidate_age.data, candidate_id = form.candidate_id.data, candidate_faculty = form.candidate_faculty.data, candidate_level = form.candidate_level.data, candidate_quote = form.candidate_quote.data, candidate_position = form.candidate_position.data , candidate_resume = resume_name , candidate_photo_filename = photo_name)
          db.session.add(candidate)
          db.session.commit()
          flash('Candidate information has been filled up successfully!', 'success')
          return redirect(url_for('adminHomepage'))

     return render_template('candidate_form.html', form=form)


# @app.route('/general_candidate_form' , methods = ['POST' , 'GET']) 
# def generalcandidatesform():

#      form = CandidateForm()

#      if form.validate_on_submit():
#           photo_filename = None
#           if form.candidate_photo.data:
#                photo = form.candidate_photo.data
#                photo_filename = secure_filename(photo.filename)
#                photo.save(os.path.join(app.config['UPLOADED_FOLDER'], photo_filename))

#          if form.candidate_resume.data:
#               candidate_resume = form.candidate_resume.data
#               resume_filename = secure_filename(candidate_resume.filename)
#               resume_name = str(uuid.uuid1()) + '_' + resume_filename
#               candidate_resume.save(os.path.join(app.config['UPLOAD_FOLDER'], resume_name))
#          else:
#               resume_name = None
#
#          candidate = Candidate(candidate_name = form.candidate_name.data, candidate_age = form.candidate_age.data, candidate_id = form.candidate_id.data, candidate_faculty = form.candidate_faculty.data, candidate_level = form.candidate_level.data, candidate_quote = form.candidate_quote.data, candidate_position = form.candidate_position.data , candidate_resume = resume_name)
#          db.session.add(candidate)
#          db.session.commit()
#          flash('Candidate information has been filled up successfully!', 'success')
#          return redirect(url_for('adminHomepage'))

#      return render_template('general_candidate_form.html', form=form)


@app.route('/info_candidates/<int:candidate_id>/edit' , methods = ['POST' , 'GET'])
def edit_candidates(candidate_id):
   candidate = Candidate.query.get_or_404(candidate_id)
   
   form = CandidateForm()
   if form.validate_on_submit():
        candidate.candidate_name = form.candidate_name.data
        candidate.candidate_age = form.candidate_age.data
        candidate.candidate_id = form.candidate_id.data
        candidate.candidate_faculty = form.candidate_faculty.data
        candidate.candidate_level = form.candidate_level.data
        candidate.candidate_quote = form.candidate_quote.data
        candidate.candidate_position = form.candidate_position.data
        candidate.candidate_photo_filename = form.candidate_photo.data
        if form.candidate_resume.data:
            candidate_resume = form.candidate_resume.data
            resume_filename = secure_filename(candidate_resume.filename)
            resume_name = str(uuid.uuid1()) + '_' + resume_filename
            candidate_resume.save(os.path.join(app.config['UPLOAD_FOLDER'], resume_name))
            candidate.candidate_resume = resume_name
        db.session.commit()
        return redirect(url_for('candidatesInfo'))
   form.candidate_name.data = candidate.candidate_name
   form.candidate_age.data = candidate.candidate_age 
   form.candidate_id.data = candidate.candidate_id
   form.candidate_faculty.data = candidate.candidate_faculty 
   form.candidate_level.data = candidate.candidate_level 
   form.candidate_quote.data = candidate.candidate_quote 
   form.candidate_position.data = candidate.candidate_position 
   form.candidate_photo.data = candidate.candidate_photo_filename


   return render_template('update_candidates2.html' , form = form)




@app.route('/update_candidates/<int:candidate_id>/delete' , methods = ['POST' , 'GET'])

def delete_candidates(candidate_id):
     candidate = Candidate.query.get_or_404(candidate_id)

     db.session.delete(candidate)
     db.session.commit()
     flash('Your post has been deleted!' , 'success')
     return redirect(url_for('candidatesInfo'))



@app.route('/candidate_biodata/<int:candidate_id>')

def candidate_biodata(candidate_id):
   candidate = Candidate.query.get_or_404(candidate_id)
   return render_template('candidate_biodata.html' , candidate_name = candidate.candidate_name, candidate = candidate , candidate_resume = candidate.candidate_resume)


@app.route('/private_message_candidate/<int:user_id>' , methods = ['POST' , 'GET'])

def private_message_candidate(user_id):
     form = PrivateConvoForm()
     messages = PrivateConvo.query.all()
     users = User.query.get_or_404(user_id)


     if form.validate_on_submit():
        privateconvo = PrivateConvo( message = form.message.data)
        db.session.add(privateconvo)
        db.session.commit()
        return redirect(url_for('home'))
     return render_template('privateMessageCandidate.html' , users = users , form = form , messages = messages)