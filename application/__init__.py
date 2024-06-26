from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOADED_FOLDER'] = 'application/static/candidate_profile_pics'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'png', 'jpeg'}
app.config['UPLOAD_FOLDER'] = 'application/static/candidate_resume'
app.config['UPLOAD_USER_PROFILE'] = 'application/static/user_profile_photo'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app , db)
login_manager = LoginManager(app)

from application import routes