from exts import db


class SignIn(db.Model):

    __tablename__ = 'signin'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255), unique=True)
    datetime = db.Column(db.DATETIME, nullable=False)

class Comment(db.Model):

    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255), unique=True)
    videoName = db.Column(db.String(255), unique=True)
    text = db.Column(db.String(255), unique=False)
    datetime = db.Column(db.DATETIME, unique=False)

