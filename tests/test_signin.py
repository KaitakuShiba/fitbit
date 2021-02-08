import pytest, sqlite3, os, pdb, bcrypt
from app import app, db, User
from flask import request, url_for

DB_NAME = 'fitbit.db'
name = 'foo'

def test_signup():
    app.config['TESTING'] = True
    client = app.test_client()
    data = {'name': name, 'password': 'password' }
    result = client.post('/signin', data=data, follow_redirects=False)
    assert result.status_code == 302

@pytest.fixture(autouse=True)
def setup():
    __create_db()
    hashed_password = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
    db.session.add(User(name=name, hashed_password=hashed_password, client_id='client_id', client_secret='client_secret'))
    db.session.commit()

def teardown():
    __drop_db()

def __create_db():
    db.create_all()

def __drop_db():
    file_path = os.path.join(os.getcwd(), DB_NAME)
    os.remove(file_path)
