from flask import Flask
import os

def create_app():
    
    app = Flask(__name__)
    
    app.secret_key = os.environ.get("FLASK_SECRET_KEY")
    app.config["UPLOAD_FOLDER"] = os.path.join('webappcv', 'static', 'uploads')
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_FLASK_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    with app.app_context():
       from . import views
        
    return app