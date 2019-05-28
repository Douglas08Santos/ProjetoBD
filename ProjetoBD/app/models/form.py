from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired


class  LoginForm(Form):
	login = StringField("login", validators=[DataRequired()])
	senha = PasswordField("senha", validators=[DataRequired()])
	remember_me = BooleanField("remember_me")


class RegisterForm(Form):
	"""docstring for RegisterForm"""
	fname = StringField("fname", validators=[DataRequired()])
	lname = StringField("lname", validators=[DataRequired()])
	nascimento = DateField("nascimento", validators=[DataRequired()])
	idade = IntegerField("idade")
	login = StringField("login", validators=[DataRequired()])
	senha = StringField("senha", validators=[DataRequired()])
		