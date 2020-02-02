from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired,  ValidationError, Email, EqualTo


class findCandidate(FlaskForm):
    job_post = StringField('', validators=[DataRequired()],  render_kw={"placeholder": "Search Job Posts"})
    submit = SubmitField("Login")
    myChoices = [("date","Filter by date"), ("profession", "Filter by profession"),( "mood","Filter by mood")]
    filters = SelectField("Select Filters", choices = myChoices, render_kw={"text":"Add Filters"})
