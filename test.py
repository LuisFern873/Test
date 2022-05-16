import os
import unittest
import json
from app import app, db

TEST_DB = 'test.db'

class Testeo(unittest.TestCase):

    # Ejecutar antes de cada test #
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ucyhwjueiddyap:d4b568b45f2d21b0d5439543ea3fe7d3560f75ec2799e780897de62bb3752379@ec2-3-224-164-189.compute-1.amazonaws.com:5432/d3kru7fbguascq'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ejecutar despues de cada test #
    def tearDown(self):
        pass      

    # TESTS #

    def test_index(self):
        tester = app.test_client(self)
        respuesta = tester.get('/', follow_redirects=True)
        self.assertEqual(respuesta.status_code, 200)

    # Probando el registro de la aplicacion #    

    def test_1a_register_wrong_DNI(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            data = json.dumps(dict(dni_admin='', nombres='Alfonso', apellidos='Perez', correo='alfon.perez@gmail.com', password='12345', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b"Introduzca un dni valido", respuesta.data)
    
    def test_1b_register_wrong_nombres(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            data = json.dumps(dict(dni_admin='63578380', nombres='', apellidos='Perez', correo='alfon.perez@gmail.com', password='12345', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b"Introduzca un nombre valido", respuesta.data)
    
    def test_1c_register_wrong_apellidos(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            data = json.dumps(dict(dni_admin='63578380', nombres='Alfonso', apellidos='', correo='alfon.perez@gmail.com', password='12345', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b"Introduzca un apellido valido valido", respuesta.data)
    
    def test_1d_register_wrong_correo(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            data = json.dumps(dict(dni_admin='63578380', nombres='Alfonso', apellidos='Perez', correo='', password='12345', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b"Introduzca un correo valido", respuesta.data)    

    def test_1e_register_wrong_password(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            data = json.dumps(dict(dni_admin='63578380', nombres='Alfonso', apellidos='Perez', correo='alfon.perez@gmail.com', password='', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b"Introduzca una clave valida", respuesta.data)

    def test_1f_register_wrong_password_confirmation(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            data = json.dumps(dict(dni_admin='63578380', nombres='Alfonso', apellidos='Perez', correo='alfon.perez@gmail.com', password='12345', confirm_password='')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertNotIn(b'success', respuesta.data)
    
    # Probando el login de la aplicacion #

    def test_2a_login_right(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/login/log_admin', 
            data = json.dumps(dict(dni_admin='63578380', password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b'false', respuesta.data)

    def test_2b_login_wrong_DNI(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/login/log_admin', 
            data = json.dumps(dict(dni_admin='', password='cinco')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b'DNI invalido', respuesta.data)

    def test_2c_login_wrong_password(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/login/log_admin', 
            data = json.dumps(dict(dni_admin='12345678', password='')),
            content_type = 'application/json',
            follow_redirects = True)
        self.assertIn(b'Clave invalida', respuesta.data)

    # Probando la creacion de empleados #

    def test_3a_newEmpleado_wrong_DNI(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/empleados/new_empleado',
            data = json.dumps(dict(dni_empleado = '', nombres='Sara', apellidos='Flores', genero='F')),
            content_type = 'application/json',
            follow_redirects = True)
        self.assertIn(b'El empleado debe tener un dni valido', respuesta.data)
    
    def test_3b_newEmpleado_wrong_nombre(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/empleados/new_empleado',
            data = json.dumps(dict(dni_empleado = '85790502', nombres='', apellidos='Flores', genero='F')),
            content_type = 'application/json',
            follow_redirects = True)
        self.assertIn(b'El empleado debe tener un nombre valido', respuesta.data)

    def test_3c_newEmpleado_wrong_apellido(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/empleados/new_empleado',
            data = json.dumps(dict(dni_empleado = '85790502', nombres='Sara', apellidos='', genero='F')),
            content_type = 'application/json',
            follow_redirects = True)
        self.assertIn(b'El empleado debe tener un apellido valido', respuesta.data)

    def test_3d_newEmpleado_wrong_genero(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/empleados/new_empleado',
            data = json.dumps(dict(dni_empleado = '85790502', nombres='Sara', apellidos='Flores', genero='')),
            content_type = 'application/json',
            follow_redirects = True)
        self.assertIn(b'No se ha seleccionado un genero para el empleado', respuesta.data)

if __name__ == "__main__":
    unittest.main()
