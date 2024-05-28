from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
# from flask_uploads import UploadSet, IMAGES, configure_uploads



app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOADED_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'png', 'jpeg'}
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app , db)
login_manager = LoginManager(app)
# photos = UploadSet('photos', IMAGES)
# configure_uploads(app, photos)


from application import routes