from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand	 

app = Flask(__name__)
app.config['DEBUG'] = 'True'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'
app.config['SECRET_KEY'] = 'bazinga'
db = SQLAlchemy(app)
Migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
from app.models import tables
from app.controllers import default
  