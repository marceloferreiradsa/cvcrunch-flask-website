from flask import Flask
import os
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .utils.extensions import db
from flask_wtf import CSRFProtect
from flask_mail import Mail

login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
   app = Flask(__name__)
   
   app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", 'default_secret_key')
   app.config["UPLOAD_FOLDER"] = os.path.join('webappcv', 'static', 'uploads')
   app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
   app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_FLASK_URL')
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   app.config['MAIL_SERVER'] = 'smtp.hostinger.com'  # Change to your SMTP server
   app.config['MAIL_PORT'] = 465
   app.config['MAIL_USE_SSL'] = True
   app.config['MAIL_USERNAME'] = os.environ.get('MAIL_CVCRUNCH_USERNAME')  # Change to your email
   app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_CVCRUNCH_PASSWORD')  # Change to your email password
   app.config['MAIL_DEFAULT_SENDER'] = "no-reply@cvcrunch.com"  # Optional
   
      # Initialize SQLAlchemy with this Flask app
   
   db.init_app(app)
   Bootstrap(app)
   login_manager.init_app(app)
   csrf.init_app(app)
   mail.init_app(app)
   
# Import parts of our application
   from .views import main as main_blueprint
   app.register_blueprint(main_blueprint)
      
   return app