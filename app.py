from cmath import exp
from flask import render_template,request,abort,jsonify,url_for,redirect
from models import *
import sys

# Controller

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=["POST","GET"])
def register():
    return render_template('register.html')

@app.route('/login', methods=["POST","GET"])
def login():
    return render_template('login.html')

@app.route('/addemply', methods=["POST","GET"])
def addemply():
    return render_template('addemply.html')

@app.route('/login/log_user', methods=["GET"])
def log_user():
    error = False
    response = {}
    username = request.args.get("username")
    password = request.args.get("password")

    admin = Administrador.query.filter_by(username = username).first()
    if admin != None and admin.password == password:
            print('A')      
    else:
        user = Empleado.query.filter_by(dni_empleado = username).first()
        if user != None and user.password == password:
            print('A')
        else:
            error = True
            print(exp)
    
    if error:
        abort(500)
    else:
        return jsonify(response)

@app.route('/administradores')
def administradores():
    return render_template('administradores.html', users = Administrador.query.all())

@app.route('/register/register_user', methods=["POST","GET"])
def register_user():
    error = False
    response = {}
    try:
        dni_admin = request.get_json()["dni_admin"]
        nombres = request.get_json()["nombres"]
        apellidos = request.get_json()["apellidos"]
        correo = request.get_json()["correo"]
        password = request.get_json()["password"]
        confirm_password = request.get_json()["confirm_password"]

        if password == confirm_password:
            admin = Administrador(
                dni_admin = dni_admin,
                nombres = nombres,
                apellidos = apellidos,
                correo = correo,
                password = password)

            db.session.add(admin)
            db.session.commit()

            response['dni_admin'] = admin.dni_admin
            response['nombres'] = admin.nombres
            response['apellidos'] = admin.apellidos
            response['correo'] = admin.correo
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

@app.route('/empleados', methods=["POST","GET"])
def empleados():
    empleados = Empleado.query.order_by('fecha_anadido').all()
    return render_template('empleados.html', empleados = empleados)

@app.route('/empleados/new_empleado', methods=["POST","GET"])
def new_empleado():
    error = False
    response = {}
    try:
        dni_empleado = request.get_json()["dni_empleado"]
        nombres = request.get_json()["nombres"]
        apellidos = request.get_json()["apellidos"]
        genero = request.get_json()["genero"]

        empleado = Empleado(
            dni_empleado = dni_empleado,
            nombres = nombres,
            apellidos = apellidos,
            genero = genero)

        db.session.add(empleado)
        db.session.commit()

        response['dni_empleado'] = empleado.dni_empleado
        response['nombres'] = empleado.nombres
        response['apellidos'] = empleado.apellidos
        response['genero'] = empleado.genero

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

@app.route('/empleados/delete_empleado/<dni>', methods=['DELETE'])
def delete_empleado(dni):
    error = False
    response = {}
    try:
        Empleado.query.filter_by(dni_empleado = dni).delete()
        db.session.commit()

        response['dni_empleado'] = dni

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

@app.route('/empleados/update_empleado/<dni>', methods=['GET','POST'])
def update_empleado(dni):
    error = False
    response = {}
    
    try:
        edit_dni_empleado = request.get_json()["edit_dni_empleado"]
        edit_nombres = request.get_json()["edit_nombres"]
        edit_apellidos = request.get_json()["edit_apellidos"]

        empleado = Empleado.query.filter_by(dni_empleado = dni)
        
        if edit_dni_empleado != "":
            empleado.update({'dni_empleado': edit_dni_empleado})
        if edit_nombres != "":
            empleado.update({'nombres': edit_nombres})
        if edit_apellidos != "":
            empleado.update({'apellidos': edit_apellidos})
        
        db.session.commit()

        response['dni_empleado'] = dni

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

@app.route('/tareas', methods = ['POST','GET'])
def tareas():
    return render_template("emplytasks.html")


if __name__ == "__main__":
    app.run(debug = True)


        




