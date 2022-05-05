from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

from flask_login import (
    UserMixin, 
    login_user, 
    LoginManager, 
    login_required, 
    logout_user)

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

URI = 'postgresql://postgres:conejowas12345@localhost:5432/dbproyecto'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Administrador(db.Model):
    __tablename__ = 'Administradores'
    
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String(100), nullable = False)
    username = db.Column(db.String(80), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    mobile_phone = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(200), nullable = False)
    date_added = db.Column(db.DateTime(), default = datetime.now)

    def __repr__(self):
        return "Administrador: {}".format(self.username)

class Empleado(db.Model):
    __tablename__ = 'Empleados'

    dni_empleado = db.Column(db.Integer, primary_key = True)
    nombres = db.Column(db.String(50), nullable = False)
    apellidos = db.Column(db.String(50), nullable = False)
    genero = db.Column(db.String(1), nullable = False)

    def __repr__(self):
        return "Empleado: {}".format(self.dni_empleado)

class Tarea(db.Model):
    __tablename__ = 'Tareas'

    id_tarea = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50), nullable = True)
    descripcion = db.Column(db.String(500), nullable = True)
    completo = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return "Tarea: {}".format(self.id_tarea)
