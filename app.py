from cmath import exp
from flask import render_template,request,abort,jsonify
from models import *
import sys


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/activitiestd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




class Add(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)
    dni = db.Column(db.Integer(), nullable=False)
    def __repr__(self):
        return f'Todo: id={self.id}, description={self.description}'

db.create_all()

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

@app.route('/add', methods=["POST","GET"])
def add():
    return render_template('admin-activities.html')

@app.route('/add/newactivitie', methods=["POST"])
def add_activities():
    description= request.form.get('activitie',"")
    dni = request.form['dni']
    add = Add(description=description,dni=dni)
    db.session.add(add)
    db.session.commit()
    return render_template('admin-activities.html')

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

@app.route('/users')
def users():
    return render_template('users.html', users = Administrador.query.all())

@app.route('/register/register_user', methods=["POST","GET"])
def register_new():
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
    return render_template('empleados.html')       


@app.route('/tareas', methods = ['POST','GET'])
def tareas():
    return render_template("emplytasks.html")

if __name__ == "__main__":
    app.run(debug = True)


        




