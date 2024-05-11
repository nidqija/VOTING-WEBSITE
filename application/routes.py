from flask import render_template , flash , redirect , url_for 
from application.form import RegistrationForm , Loginform , QuestionForm , VotingForm , CandidateForm
from application.models import User , Post , Vote, Admin
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



@app.route('/candidates/new' , methods = ['POST' , 'GET'])
@login_required

def candidates():
     voting = Vote.query.all()
     form = VotingForm()
     if form.validate_on_submit():
          vote = Vote(studentName = form.studentName.data , studentId = form.studentId.data , otherFaculty = form.otherFaculties.data , reasonCandidate = form.reasonCandidate.data ,  author = current_user )
          db.session.add(vote)
          db.session.commit()
          flash('Voting Successful!' , 'success')
          return redirect(url_for('candidates'))
     return render_template('candidates.html' , form = form , voting = voting)

     







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
     return render_template('admin_homepage.html')


@app.route('/update_announcement')
def updateAnnouncement():
     return render_template('update_announcement.html')


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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        admin = Admin(username=form.username.data , email = form.email.data , password = hashed_password)
        db.session.add(admin)
        db.session.commit()
        flash(f'Account created for {form.username.data} !' , 'success!')
        return redirect(url_for('login'))
    return render_template('register.html' , form = form)    