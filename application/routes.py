from flask import render_template , flash , redirect , url_for
from application.form import RegistrationForm , Loginform
from application.models import User
from application import app , db , bcrypt


@app.route('/')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login' , methods = ['POST' , 'GET'])
def login():
    form = Loginform()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash(f'Login Successful !')
            return redirect(url_for('home'))
        else:
            flash(f'Login Failed' , 'danger')
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