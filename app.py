from flask import Flask,render_template,request,abort,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import sys

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

URI = 'postgresql://postgres:conejowas12345@localhost:5432/test'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class User(db.Model):
    __tablename__ = 'user'

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
        return "Username: {}".format(self.username)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=["POST","GET"])
def login():
    return render_template('login.html')

@app.route('/users', methods=["POST","GET"])
def users():
    return render_template('users.html', users = User.query.all())


@app.route('/login/user_added', methods=["POST","GET"])
def login_new():
    error = False
    response = {}
    try:
        full_name = request.get_json()["fullname"]
        username = request.get_json()["username"]
        email = request.get_json()["email"]
        mobile_phone = request.get_json()["phone"]
        password = request.get_json()["password"]

        user = User(
            full_name = full_name,
            username = username, 
            email = email,
            mobile_phone = mobile_phone,
            password = password)

        db.session.add(user)
        db.session.commit()
        # Esta acaa

        response['fullname'] = user.full_name
        response['username'] = user.username
        response['email'] = user.email
        response['phone'] = user.mobile_phone
        response['password'] = user.password

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


        




