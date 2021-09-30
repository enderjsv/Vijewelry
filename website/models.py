from . import db


class Users(db.Model):
    user = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(150), nullable=False)
