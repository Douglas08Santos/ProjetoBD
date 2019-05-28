from flask import render_template
from app import app

from app.models.form import LoginForm
from app.models.form import RegisterForm

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		print(form.login.data)
		print(form.senha.data)
	else:
		print(form.errors)
	
	return render_template('login.html', form = form)

@app.route("/register", methods=["GET","POST"])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		print(form.login.data)
		print(form.senha.data)
	return render_template('register.html', form = form)	 


 