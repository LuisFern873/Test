from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

from flask_login import UserMixin, LoginManager

app = Flask(__name__)

URI = 'postgresql://ucyhwjueiddyap:d4b568b45f2d21b0d5439543ea3fe7d3560f75ec2799e780897de62bb3752379@ec2-3-224-164-189.compute-1.amazonaws.com:5432/d3kru7fbguascq'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_admin = LoginManager()
login_admin.init_app(app)

class Administrador(db.Model, UserMixin):
    dni_admin = db.Column(db.String(8), primary_key = True)
    nombres = db.Column(db.String(100), nullable = False)
    apellidos = db.Column(db.String(100), nullable = False)
    correo = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(300), nullable = False)
    fecha_anadido = db.Column(db.DateTime(), default = datetime.now)
    empleados = db.relationship('Empleado', backref = 'administrador')

    def get_id(self):
        return (self.dni_admin)

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
    admin = db.Column(db.String(8), db.ForeignKey('administrador.dni_admin'))


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