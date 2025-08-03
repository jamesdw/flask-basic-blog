import uuid
from datetime import datetime
from app.utils import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "fwk_act_accounts"

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    num = db.Column(db.Integer, unique=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    display_name = db.Column(db.String(100), nullable=True)
    tenant_id = db.Column(db.String(36), nullable=True)
    pass_hash = db.Column(db.String(255), nullable=False)
    pass_salt = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_special = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<User {self.username}>"

