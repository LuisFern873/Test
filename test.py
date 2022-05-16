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
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ovfoduuadfenjt:6dd56e6cfa5db2ee89e46ee354ad19f976c4f22e77c14e912a6f27e15592ba24@ec2-3-224-164-189.compute-1.amazonaws.com:5432/d7n72srrj4b45g'
         
        db.drop_all()
        db.create_all()

    # Ejecutar despues de cada test #
    def tearDown(self):
        pass      

    # TESTS #

    def test_index(self):
        tester = app.test_client(self)
        respuesta = tester.get('/', follow_redirects=True)
        self.assertEqual(respuesta.status_code, 200)

    # Probando el registro de la aplicacion #    

    def test_register_wrong_DNI(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            datos = json.dumps(dict(dni_admin='', nombres='Alfonso', apellidos='Perez', correo='alfon.perez@gmail.com', password='12345', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b'Introduzca un DNI valido', respuesta.datos)
    
    def test_register_wrong_nombres(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            datos = json.dumps(dict(dni_admin='63578380', nombres='', apellidos='Perez', correo='alfon.perez@gmail.com', password='12345', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b'Introduzca un nombre(s) valido', respuesta.datos)
    
    def test_register_wrong_apellidos(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            datos = json.dumps(dict(dni_admin='63578380', nombres='Alfonso', apellidos='', correo='alfon.perez@gmail.com', password='12345', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b'Introduzca un apellido(s) valido', respuesta.datos)
    
    def test_register_wrong_correo(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            datos = json.dumps(dict(dni_admin='63578380', nombres='Alfonso', apellidos='Perez', correo='', password='12345', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b'Introduzca un correo valido', respuesta.datos)    

    def test_register_wrong_password(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            datos = json.dumps(dict(dni_admin='63578380', nombres='Alfonso', apellidos='Perez', correo='alfon.perez@gmail.com', password='', confirm_password='12345')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b'Introduzca una clave valida', respuesta.datos)

    def test_register_wrong_password_confirmation(self):
        tester = app.test_client(self)
        respuesta = tester.post(
            '/register/register_admin',
            datos = json.dumps(dict(dni_admin='63578380', nombres='Alfonso', apellidos='Perez', correo='alfon.perez@gmail.com', password='12345', confirm_password='')),
            content_type = 'application/json',
            follow_redirects=True)
        self.assertIn(b'Las claves no coinciden', respuesta.datos)

    # Probando el login de la aplicacion #

    def test_login_right(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login/log_admin', 
            data=json.dumps(dict(dni_admin='12345678', password='cinco')),
            content_type='application/json',
            follow_redirects=True)
        self.assertIn(b'false', response.data)

    def test_logIn_wrong_DNI(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login/log_admin', 
            data=json.dumps(dict(dni_admin='', password='cinco')),
            content_type='application/json',
            follow_redirects=True)
        self.assertIn(b'DNI invalido', response.data)

    def test_logIn_wrong_password(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login/log_admin', 
            data=json.dumps(dict(dni_admin='12345678', password='')),
            content_type='application/json',
            follow_redirects=True)
        self.assertIn(b'Clave invalida', response.data)
