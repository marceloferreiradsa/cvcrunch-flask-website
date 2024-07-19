from flask import Flask
import os
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .utils.extensions import db
from flask_wtf import CSRFProtect
from flask_mail import Mail
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.DEBUG)

login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()
migrate = Migrate()  # Initialize Flask-Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    # Get the absolute path to the templates directory
    template_dir = os.path.abspath('webappcv/templates')

    app = Flask(__name__, template_folder=template_dir)
    print(f"Flask is looking for templates in: {app.template_folder}")

    app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY", 'default_secret_key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_FLASK_URL')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_CVCRUNCH_USERNAME')  # Change to your email
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_CVCRUNCH_PASSWORD')  # Change to your email password
    app.config['MAIL_DEFAULT_SENDER'] = "no-reply@cvcrunch.com"  # Optional
    app.config["UPLOAD_FOLDER"] = os.path.join('webappcv', 'static', 'uploads')
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.hostinger.com'  # Change to your SMTP server
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True

    db.init_app(app)
    migrate.init_app(app, db)  # Bind Flask-Migrate to your app and database
    Bootstrap(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)

    # Import and register the blueprint
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
