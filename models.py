from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# from flask_login import (
#     UserMixin, 
#     login_user, 
#     LoginManager, 
#     login_required, 
#     logout_user)

# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import InputRequired, Length, ValidationError

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

URI = 'postgresql://ovfoduuadfenjt:6dd56e6cfa5db2ee89e46ee354ad19f976c4f22e77c14e912a6f27e15592ba24@ec2-3-224-164-189.compute-1.amazonaws.com:5432/d7n72srrj4b45g'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Administrador(db.Model):
    dni_admin = db.Column(db.String(8), primary_key = True)
    nombres = db.Column(db.String(100), nullable = False)
    apellidos = db.Column(db.String(100), nullable = False)
    correo = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(300), nullable = False)
    fecha_anadido = db.Column(db.DateTime(), default = datetime.now)

    def __repr__(self):
        return "Administrador: {}".format(self.dni_admin)

class Empleado(db.Model):
    dni_empleado = db.Column(db.String(8), primary_key = True)
    nombres = db.Column(db.String(50), nullable = False)
    apellidos = db.Column(db.String(50), nullable = False)
    genero = db.Column(db.String(1), nullable = False)
    fecha_anadido = db.Column(db.DateTime(), default = datetime.now)
    fecha_modificado = db.Column(db.DateTime(), nullable = True)
    tareas = db.relationship('Tarea', backref = 'empleado')

    def __repr__(self):
        return "Empleado: {}".format(self.dni_empleado)

class Tarea(db.Model):
    id_tarea = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(50), nullable = True)
    descripcion = db.Column(db.String(500), nullable = True)
    completo = db.Column(db.Boolean, nullable = False)
    asignado = db.Column(db.String(8), db.ForeignKey('empleado.dni_empleado'))

    def __repr__(self):
        return "Tarea: {}".format(self.id_tarea)

db.create_all()