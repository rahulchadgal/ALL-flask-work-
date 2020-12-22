from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired, Email ,EqualTo
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password =PasswordField('password',validators=[DataRequired()])
    submit =SubmitField('login')

class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    username =StringField('username',validators=[DataRequired()])
    password =PasswordField('password',validators=[DataRequired(),EqualTo('pass_confirm',message='password must be same')])
    pass_confirm =PasswordField('confirm password',validators=[DataRequired()])
    submit =SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')
    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been registered')







    def validate_email(self, email):
        if email.data != current_user.email:
            if User.query.filter_by(email=email.data).first():
                raise ValidationError('Email has been registered')
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username=username.data).first():
                raise ValidationError('Username has been registered')
