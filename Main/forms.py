from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import DataRequired,  ValidationError, Email, EqualTo


class findCandidate(FlaskForm):
    job_post = StringField('Enter Job Post', validators=[DataRequired()])
    submit = SubmitField("Login")