from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired


class CreateSignInForm(FlaskForm):
    ip = StringField('Ip', validators=[DataRequired()])
    datetime = TextAreaField('Datetime', validators=[DataRequired()])

class CreateCommentForm(FlaskForm):
    ip = StringField('Ip', validators=[DataRequired()])
    video = StringField('videoName', validators=[DataRequired()])
    text = StringField('text', validators=[DataRequired()])
    datetime = TextAreaField('Datetime', validators=[DataRequired()])


