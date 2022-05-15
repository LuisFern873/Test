## Nombre del proyecto: **Sistema de administración de empleados TAMBO**

## Integrantes:

| Código    | Nombres y Apellidos         | Correo Institucional                                          |
| --------- | --------------------------- | ------------------------------------------------------------- |
| 202110216 | Luis Fernando Méndez Lázaro | [luis.mendez.l@utec.edu.pe](mailto:luis.mendez.l@utec.edu.pe) |
| 202110394 | Jose Francisco Wong Orrillo | [jose.wong@utec.edu.pe](mailto:jose.wong@utec.edu.pe) |
| 201820010 | Pedro Ivan Renzo Lizarbe Palacios | [pedro.lizarbe.p@utec.edu.pe](mailto:pedro.lizarbe.p@utec.edu.pe) |
| 201820010 | Jean Franco Aquino Rojas | [jean.aquino@utec.udu.pe](mailto:jean.aquino@utec.udu.pe) |
## Descripción:

Hoy en día, muchas empresas están buscando herramientas que mejoren la productividad de su personal administrativo y empleados. En ese marco, que se requiere de software que organice sus recursos y se ajuste a sus necesidades. Es por ello que nace este proyecto que pretende solucionar estos problemas en aquellas organizaciones que buscan máxima eficiencia. Entre estas se encuentra la cadena de tiendas Tambo+, siendo nuestro proyecto a quien va dirigido.

## Objetivos principales / Misión / Visión:

Misión

- Ayudar a administradores de tiendas Tambo a asignar tareas en un espacio web.

Visión

- 

El presente proyecto tiene como objetivos:

- Ayudar a administradores de tiendas Tambo a asignar tareas en un espacio web.
- Otorgar flexibilidad y eficiencia para organizar empleados.

## Librerías / frameworks / plugins utilizados en el Front-end, Back-end y Base de datos:

### Front-end:

Para el front-end se utilizaron las siguientes tecnologías:

- HTML
- CSS

### Back-end:

Para el back-end se utilizaron las siguientes tecnologías:

- 
- SQLalchemy
- flask_migrate

### Base de datos:

- PostgreSQL (servidor alojado en la plataforma Heroku)

## Nombre del Script a ejecutar para iniciar la base de datos con datos:

## Información acerca de los API. Requests y Responses de cada endpoint utilizado en el sistema:

## Hosts:

Para efectos de nuestro proyecto, utilizamos el localhost.

## Forma de autenticación:

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
