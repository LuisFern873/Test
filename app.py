from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sys

app = Flask(__name__)

URI = 'postgresql://postgres:conejowas12345@localhost:5432/test'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_added = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return "id: {}\nusername: {}\nemail: {}\ndate_added: {}\n".format(self.id, self.username, self.email, self.date_added)

db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

# HTTP methods
@app.route('/login', methods=["POST","GET"])
def login():
    return render_template('login.html', users = User.query.all())

@app.route('/login/user_added', methods=["POST","GET"])
def login_new():
    try:
        username = request.form.get('username','')
        email = request.form.get('email','')
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
    except:
        db.session.rollback()
        error = True
        print(sys.exc_info())
    finally:
        db.session.close()

    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug = True)


        




