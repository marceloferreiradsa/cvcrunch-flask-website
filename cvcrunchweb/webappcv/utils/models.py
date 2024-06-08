import uuid
from sqlalchemy.dialects.postgresql import UUID
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from webappcv import login_manager
from flask_login import UserMixin
from .extensions import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Define a model for the 'users' table
class User(db.Model, UserMixin):
    __tablename__= 'users'
    user_id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def get_id(self):
        return str(self.user_id)
    
    def __repr__(self):
        return f'< Email {self.email}>'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

