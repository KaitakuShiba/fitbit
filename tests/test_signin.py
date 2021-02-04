import pytest, sqlite3, os, pdb, bcrypt
from app import app, db, User
from flask import request, url_for

DB_NAME = 'fitbit.db'

def test_signup():
    app.config['TESTING'] = True
    client = app.test_client()
    data = {'email': 'sample@emxample.com', 'password': 'password' }
    result = client.post('/signin', data=data, follow_redirects=True)
    pdb.set_trace()
    assert b'hello' == result.data

@pytest.fixture(autouse=True)
def setup():
    __create_db()
    email = 'sample@emxample.com'
    hashed_password = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
    db.session.add(User(email=email, hashed_password=hashed_password, client_id='client_id', client_secret='client_secret'))

def teardown():
    __drop_db()

def __create_db():
    db.create_all()

def __drop_db():
    file_path = os.path.join(os.getcwd(), DB_NAME)
    os.remove(file_path)
