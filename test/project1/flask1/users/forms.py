from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flask1.models import user


class RegistrationForm(FlaskForm):
	username= StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	confirm_password=PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Sign Up')

	def validate_username(self,username):
		user1=user.query.filter_by(username=username.data).first()

		if user1:
			raise ValidationError('User name already taken.')

	def validate_email(self,email):
		user1=user.query.filter_by(email=email.data).first()

		if user1:
			raise ValidationError('email already registered. Please use another')

class LoginForm(FlaskForm):
	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	remember=BooleanField('Remember Me')
	submit=SubmitField('Login')


class UpdateAccountForm(FlaskForm):
	username= StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	picture=FileField('update profile picture',validators=[FileAllowed(['jpg','png','jpeg'])])
	submit=SubmitField('Update')

	def validate_username(self,username):
		if username.data !=current_user.username:
			user1=user.query.filter_by(username=username.data).first()

			if user1:
				raise ValidationError('User name already taken.')

	def validate_email(self,email):
		if email.data !=current_user.email:
			user1=user.query.filter_by(email=email.data).first()

			if user1:
				raise ValidationError('email already registered. Please use another')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user1 = user.query.filter_by(email=email.data).first()
        if user1 is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')