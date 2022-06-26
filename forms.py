
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, NumberRange
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField


class UserForm(FlaskForm):
    username = StringField("Enter your name", validators=[
                           DataRequired(), Length(min=2, max=10)])
    email_id = StringField("Email address", validators=[
                           DataRequired(), Email()])
    submit = SubmitField("Submit")


class TwitterSearchForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    number_of_tweets = IntegerField("Number of Tweets", validators=[DataRequired(),
                                    NumberRange(min=1, max=200)])
    submit = SubmitField("Submit")
