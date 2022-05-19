from http.client import ResponseNotReady
from tkinter.messagebox import RETRY
from urllib import response
from flask import render_template, request, abort,jsonify, redirect,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required, logout_user
from models import *

app.config['SECRET_KEY'] = "12345"

# Controllers

@login_admin.user_loader
def admin_loader(dni):
    return Administrador.query.get(str(dni))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register/register_admin', methods=["POST","GET"])
def register_admin():
    error = False
    response = {}

    try:
        dni_admin = request.get_json()["dni_admin"]
        nombres = request.get_json()["nombres"]
        apellidos = request.get_json()["apellidos"]
        correo = request.get_json()["correo"]
        password = request.get_json()["password"]
        confirm_password = request.get_json()["confirm_password"]

        if dni_admin.isspace() == True or len(dni_admin)==0:
            response['mensaje_error'] = "Introduzca un dni valido"

        elif nombres.isspace() == True or len(nombres)==0:
            response['mensaje_error'] = "Introduzca un nombre valido"
        
        elif apellidos.isspace() == True or len(apellidos)==0:
            response['mensaje_error'] = "Introduzca un apellido valido valido"

        elif correo.isspace() == True or len(correo)==0:
            response['mensaje_error'] = "Introduzca un correo valido"

        elif password.isspace() == True or len(password)==0:
            response['mensaje_error'] = "Introduzca una clave valida"                            

        else:

            hashed = generate_password_hash(password)

            if check_password_hash(hashed, confirm_password):
                admin = Administrador(
                    dni_admin = dni_admin,
                    nombres = nombres,
                    apellidos = apellidos,
                    correo = correo,
                    password = hashed)

                db.session.add(admin)
                db.session.commit()

                response['mensaje'] = 'success'
                response['nombres'] = admin.nombres

            else:
                response['mensaje'] = '¡Confirme correctamente su contraseña!'

    except Exception as exp:
        db.session.rollback()
        error = True
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(exp).__name__, exp.args)
        print(message)
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify(response)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login/log_admin', methods=["POST","GET"])
def log_admin():
    response = {}
    error = False

    dni_admin = request.get_json()["dni_admin_login"]
    password = request.get_json()["password_login"]

    try:
        admin = Administrador.query.filter_by(dni_admin = dni_admin).first()
        
        if admin is not None and check_password_hash(admin.password, password):
            response['mensaje'] = 'success'
            login_user(admin)
        else:
            response['mensaje'] = '¡Combinación DNI/contraseña inválida!'

    except Exception as exp:
        error = True
        response['mensaje'] = 'Exception is raised'
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(exp).__name__, exp.args)
        print(message)
    if error:
        abort(500)
    else:
        return jsonify(response)

# Endpoint donde se muestra la lista de empleados

@app.route('/empleados')
@login_required
def empleados():
    empleados = Empleado.query.order_by('fecha_anadido').all()
    return render_template('empleados.html', empleados = empleados, name = current_user.nombres)

# Endpoint para agregar a un empleado

@app.route('/empleados/new_empleado', methods=["POST","GET"])
def new_empleado():
    error = False
    response = {}
    try:
        dni_empleado = request.get_json()["dni_empleado"]
        nombres = request.get_json()["nombres"]
        apellidos = request.get_json()["apellidos"]
        genero = request.get_json()["genero"]

        if dni_empleado.isspace() == True or len(dni_empleado) == 0:
            response['mensaje_error'] = 'El empleado debe tener un dni valido'
        
        elif nombres.isspace() == True or len(nombres) == 0:
            response['mensaje_error'] = 'El empleado debe tener un nombre valido'
    
        elif apellidos.isspace() == True or len(apellidos) == 0:
            response['mensaje_error'] = 'El empleado debe tener un apellido valido'
        
        elif genero.isspace() == True or len(genero) == 0:
            response['mensaje_error'] = 'No se ha seleccionado un genero para el empleado'
        
        else:
            empleado = Empleado(
                dni_empleado = dni_empleado,
                nombres = nombres,
                apellidos = apellidos,
                genero = genero)

            db.session.add(empleado)
            db.session.commit()

            response['mensaje'] = 'success'
            response['dni_empleado'] = empleado.dni_empleado
            response['nombres'] = empleado.nombres
            response['apellidos'] = empleado.apellidos
            response['genero'] = empleado.genero

    except Exception as exp:
        db.session.rollback()
        error = True
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(exp).__name__, exp.args)
        print(message)
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify(response)

# Endpoint para eliminar a un empleado a partir de su DNI

@app.route('/empleados/delete_empleado/<dni>', methods=['DELETE'])
def delete_empleado(dni):
    error = False
    response = {}
    try:
        Tarea.query.filter_by(asignado = dni).delete()
        Empleado.query.filter_by(dni_empleado = dni).delete()

        db.session.commit()
        response['mensaje'] = 'success'
        response['dni_empleado'] = dni

    except Exception as exp:
        db.session.rollback()
        error = True
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(exp).__name__, exp.args)
        print(message)
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify(response)

# Endpoint para actualizar los datos de un empleado a partir de su DNI

@app.route('/empleados/update_empleado/<dni>', methods=['PUT'])
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
        else:
            response['mensaje_error'] = 'Ingrese un dni valido'
        
        if edit_nombres != "":
            empleado.update({'nombres': edit_nombres})
        else:
            response['mensaje_error'] = 'Ingrese un nombre valido'            
        
        if edit_apellidos != "":
            empleado.update({'apellidos': edit_apellidos})
        else:
            response['mensaje_error'] = 'Ingrese un apellido valido'            
        
        empleado.update({'fecha_modificado': datetime.now()})
        
        db.session.commit()

        response['dni_empleado'] = dni

    except Exception as exp:
        db.session.rollback()
        error = True
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(exp).__name__, exp.args)
        print(message)
    finally:
        db.session.close()

    if error:
        abort(500)
    else:
        return jsonify(response)

@app.route('/tareas')
@login_required
def tareas():
    tareas = Tarea.query.all()
    return render_template("tareas.html", tareas = tareas)

@app.route('/empleados/asignar_tarea/<dni>', methods = ['POST','GET'])
def asignar_tarea(dni):

    response = {}

    # Recuperar datos de la tarea
    titulo = request.get_json()["titulo"]
    descripcion = request.get_json()["descripcion"]

    if titulo != "":
        response['mensaje_error'] = 'Ingrese un titulo valido'
        return response
    elif descripcion != "":
        response['mensaje_error'] = 'Ingrese un titulo valido'
        return response
    else:
        # Empleado al que le vamos a asignar la tarea
        empleado = Empleado.query.filter_by(dni_empleado = dni).first()

        # Creamos la tarea
        tarea = Tarea(
            titulo = titulo,
            descripcion = descripcion,
            completo = False,
            empleado = empleado
        )
        # Añadimos la tarea
        db.session.add(tarea)
        db.session.commit()

        return jsonify({'titulo': titulo, 'descripcion': descripcion})

@app.route('/tareas/update_tarea/<id>', methods = ['PUT'])
def update_tarea(id):
    # Tarea que va ser completada
    tarea = Tarea.query.filter_by(id_tarea = id)
    # Tarea marcada como completa
    tarea.update({'completo': True})
    db.session.commit()

    return redirect(url_for('tareas'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug = True)
