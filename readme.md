## Nombre del proyecto

**Administrador ponte las pilas**

## Integrantes

| Código    | Nombres y Apellidos         | Correo Institucional                                          |
| --------- | --------------------------- | ------------------------------------------------------------- |
| 202110216 | Luis Fernando Méndez Lázaro | [luis.mendez.l@utec.edu.pe](mailto:luis.mendez.l@utec.edu.pe) |

## Descripción

Hoy en día, muchas empresas están buscando herramientas que mejoren la productividad de su personal administrativo y empleados. En ese marco, que se requiere de software que organice sus recursos y se ajuste a sus necesidades. Es por ello que nace este proyecto que pretende solucionar estos problemas en aquellas organizaciones que buscan eficiencia.


## Objetivos principales / Misión / Visión

El presente proyecto tiene como objetivos:

- Ayudar a administradores a asignar tareas en un espacio web.
- Otorgar flexibilidad para organizar empleados.

## Librerías / frameworks / plugins utilizados en el Front-end, Back-end y Base de datos

## Nombre del Script a ejecutar para iniciar la base de datos con datos

## Información acerca de los API. Requests y Responses de cada endpoint utilizado en el sistema

## Hosts

## Forma de autenticación

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
