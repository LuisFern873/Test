## Nombre del proyecto: **Sistema de administración de empleados TAMBO**

## Integrantes:

| Código    | Nombres y Apellidos         | Correo Institucional                                          |
| --------- | --------------------------- | ------------------------------------------------------------- |
| 202110216 | Luis Fernando Méndez Lázaro | [luis.mendez.l@utec.edu.pe](mailto:luis.mendez.l@utec.edu.pe) |
| 202110394 | Jose Francisco Wong Orrillo | [jose.wong@utec.edu.pe](mailto:jose.wong@utec.edu.pe) |
| 201820010 | Pedro Ivan Renzo Lizarbe Palacios | [pedro.lizarbe.p@utec.edu.pe](mailto:pedro.lizarbe.p@utec.edu.pe) |
| 201820010 | Jean Franco Aquino Rojas | [jean.aquino@utec.udu.pe](mailto:jean.aquino@utec.udu.pe) |
## Descripción:

Hoy en día, muchas empresas están buscando herramientas que mejoren la productividad de su personal administrativo y empleados. Es por ello, que se requiere de software que organice sus recursos y se ajuste a sus necesidades. En ese marco, nace este proyecto que pretende solucionar estos problemas en aquellas organizaciones que buscan máxima eficiencia. Entre estas se encuentra la cadena de tiendas Tambo+, siendo nuestro proyecto a quien va dirigido.

![](static/images/Tambo-logo.png)

## Objetivos principales / Misión / Visión:

### Misión

- Resolver problemas de gestión de empleados y asignación de tareas
que posee la cadena de tiendas Tambo, por medio de una plataforma web.

### Visión

- Convertirse en una plataforma reconocida por su escalabilidad y gran solvencia al aumentar la productividad del personal administrativo.

### Objetivos

- Otorgar flexibilidad y eficiencia para organizar empleados.
- Proveer un servicio personalizado y herramientas de gestión a administradores.

## Librerías / frameworks / plugins utilizados en el Front-end, Back-end y Base de datos:

### Front-end:

Para el front-end se utilizaron las siguientes tecnologías:

- HTML
- CSS

### Back-end:

Para el back-end se utilizaron las siguientes tecnologías:

- flask
- SQLalchemy
- flask_migrate
- json
- models

### Base de datos:

- PostgreSQL (servidor alojado en la plataforma Heroku)

## Nombre del Script a ejecutar para iniciar la base de datos con datos:

Dado que la base de datos y su respectivo servidor se encuentran alojadas en Heroku (programa en la nube) ni se requiere de un script para ser inicilializados.

## Información acerca de los API. Requests y Responses de cada endpoint utilizado en el sistema:

## Hosts:

Para efectos de nuestro proyecto, utilizamos el localhost.

## Forma de autenticación:

Para la autenticación de administradores se hizo uso del conocido módulo flask_login. Este permite que el acceso a los datos de empleados y tareas este restringido solo para los administradores que hayan iniciado sesión (logeados). A continuación, se presenta el código que realiza el proceso de autenticación mediante el formulario "login". En este se verifica que el dni ingresado pertenezca a un usuario registrado en la base de datos y que la contraseña ingresada coincida con la contraseña encriptada registrada como atributo de ese mismo usuario. Si esto se cumple, se procede a iniciar la sesión.

```python
@app.route('/login/log_admin', methods=["POST"])
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
```

## Manejo de errores HTTP:
- 500: Errores en el Servidor

Si los datos introducidos por el usuario en el formulario de registro no cumplen con el esquema o restricciones de la base de datos, se levanta una excepción y los datos no se persisten, arrojando un abort(500):

```python
if error:
    abort(500)
else:
    return jsonify(response)
```

Para manejar este error en el servidor, el usuario es notificado con un mensaje invitandolo a realizar modificaciones en sus datos.

- 400: Errores en el Clientes

Si el usuario no tiene acceso a un determinado endpoint se le notifica sobre esta restricción.

- 300: Redirección
- 200: Exitoso
- 100: Informacional
