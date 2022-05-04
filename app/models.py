from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# create db and db migration objects
db = SQLAlchemy()

class user_account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sc_username = db.Column(db.String(128), nullable=False, unique=True)
    dc_username = db.Column(db.String(128), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=True)
    time_created = db.Column(db.TIMESTAMP, server_default=func.now())
    time_updated = db.Column(db.TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())
    def __repr__(self):
        return '<user_account {}>'.format(self.email)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)