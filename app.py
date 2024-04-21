from flask import Flask , render_template , flash , redirect , url_for
from form import RegistrationForm , Loginform
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)



class User(db.Model):
        id = db.Column(db.Integer , primary_key = True)
        username = db.Column(db.String(20) , unique = True , nullable = False)
        email = db.Column(db.String(120) , unique = True , nullable = False)
        password = db.Column(db.String(120) , nullable = False)
   
        def __repr__(self):
           return f'User("{self.username}" , {self.email})'
        
        with app.app_context(): db.create_all()


  




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
        flash(f'Account created for {form.username.data} !')
        return redirect(url_for('home'))
    return render_template('register.html' , form = form)



if __name__ == '__main__':
    app.run(debug=True)