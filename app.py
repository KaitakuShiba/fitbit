from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, current_user
from modules.fitbit_token import FitbitToken
from modules.signup import Signup
from modules.signin import Signin
import pdb

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI = "sqlite:///fitbit.db",
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    SECRET_KEY = 'sample' #環境変数にする
)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# https://github.com/maxcountryman/flask-login#usage
@login_manager.user_loader
def user_loader(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return
    
    return user

@app.route("/", methods=["GET"])
def render_signin_html():
    return render_template('signin.html')

@app.route("/signin", methods=["POST"])
def signin():
    return Signin().call()

@app.route("/signup", methods=["GET"])
def render_signup_html():
    return render_template('signup.html')

@app.route("/signup", methods=["POST"])
def signup():
    return Signup().call()

@app.route("/fitbit_registration", methods=["GET"])
@login_required
def fitbit_registration():
    return render_template('fitbit_registration.html', user=current_user)

@app.route("/fitbit/users", methods=["GET"])
@login_required
def fitbit():
    return FitbitToken().call()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    hashed_password = db.Column(db.BINARY(60), nullable=False)
    client_id = db.Column(db.String, nullable=False)
    client_secret = db.Column(db.String, nullable=False)
    target_distance = db.Column(db.Integer, nullable=True)
    access_token = db.Column(db.Text, nullable=True)
    refresh_token = db.Column(db.String, nullable=True)

    def __init__(self, email, hashed_password, client_id, client_secret, access_token=None, refresh_token=None):
        self.email = email
        self.hashed_password = hashed_password
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token
