from flask import render_template,request,abort,jsonify
from models import *
import sys

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


        




