import pytest, os, pdb, bcrypt
from app import app, db, User, fitbit
from flask_login import login_user
import modules.gather_keys_oauth2
from flask import Flask

DB_NAME = 'fitbit.db'
name = 'foo'
password = 'password'

def test_fitbit_token(mocker):
    app.config['TESTING'] = True
    client = app.test_client()
    user = User.query.filter_by(name=name).first()
    data = {'name': name, 'password': password }
    client.post('/signin', data=data, follow_redirects=False)
    result = client.get('/auth_fitbit', query_string={'user_id': user.id})
    assert b'Registered! Close browser.' == result.data

@pytest.fixture(autouse=True)
def setup():
    app.config['LOGIN_DISABLED'] = True
    __create_db()
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User(name=name, hashed_password=hashed_password, client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'))
    db.session.add(user)
    db.session.commit()
    # login_user(user)

def teardown():
    # app.config['LOGIN_DISABLED'] = False
    __drop_db()

def __create_db():
    db.create_all()

def __drop_db():
    file_path = os.path.join(os.getcwd(), DB_NAME)
    os.remove(file_path)
