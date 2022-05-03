from flask import Flask,render_template,request,abort,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import sys

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

URI = 'postgresql://postgres:conejowas12345@localhost:5432/test'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Administrador(db.Model):
    __tablename__ = 'Administradores'

    id = db.Column(
        db.Integer, 
        primary_key = True)

    full_name = db.Column(
        db.String(100),
        nullable = False)
    
    username = db.Column(
        db.String(80), 
        unique = True, 
        nullable = False)

    email = db.Column(
        db.String(120), 
        unique = True, 
        nullable = False)
    
    mobile_phone = db.Column(
        db.String(20), 
        nullable = False)

    password = db.Column(
        db.String(200),  
        nullable = False)

    date_added = db.Column(
        db.DateTime(), 
        default = datetime.now)

    def __repr__(self):
        return "Administrador: {}".format(self.username)

# class Empleado(db.Model):
#     __tablename__ = 'Empleados'

#     dni = db.Column(
#         db.Integer, 
#         primary_key = True)
    
#     nombres = db.Column(
#         db.varchar(50),
#         nullable = False
#     )

#     apellidos = db.Column(
#         db.varchar(50),
#         nullable = False
#     )

#     genero = db.Column(
#         db.varchar(1),
#         nullable = False
#     )

#     def __repr__(self):
#         return "Empleado: {}".format(self.dni)

# class Tarea(db.Model):
#     __tablename__ = 'Tareas'

#     id_tarea = db.Column(
#         db.Integer,
#         primary_key = True
#     )

#     Titulo = db.Column(
#         db.varchar(100),
#         nullable = True
#     )

#     descripcion = db.Column(
#         db.varchar(500),
#         nullable = True
#     )

#     def __repr__(self):
#         return "Tarea: {}".format(self.id_tarea)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=["POST","GET"])
def register():
    return render_template('register.html')

@app.route('/login', methods=["POST","GET"])
def login():
    return render_template('login.html')

@app.route('/users')
def users():
    return render_template('users.html', users = Administrador.query.all())


@app.route('/register/user_added', methods=["POST","GET"])
def register_new():
    error = False
    response = {}
    try:
        full_name = request.get_json()["fullname"]
        username = request.get_json()["username"]
        email = request.get_json()["email"]
        mobile_phone = request.get_json()["phone"]
        password = request.get_json()["password"]
        cpassword = request.get_json()["cpassword"]

        if cpassword == password:
            admin = Administrador(
                full_name = full_name,
                username = username, 
                email = email,
                mobile_phone = mobile_phone,
                password = password)

            db.session.add(admin)
            db.session.commit()

            response['fullname'] = admin.full_name
            response['username'] = admin.username
            response['email'] = admin.email
            response['phone'] = admin.mobile_phone
            response['password'] = admin.password

    except Exception as exp:
        db.session.rollback()
        error = True
        print(exp)
        print(sys.exc_info())
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify(response)

if __name__ == "__main__":
    app.run(debug = True)


        




