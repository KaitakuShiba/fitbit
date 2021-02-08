import pytest, sqlite3, os, pdb
from app import app, db
from app import User

DB_NAME = 'fitbit.db'

def test_signup():
    app.config['TESTING'] = True
    client = app.test_client()
    name = 'foo'
    data = {'name': name, 'password': 'password', 'client_id':'client_id', 'client_secret': 'client_secret' }
    result = client.post('/signup', data=data)
    assert User.query.first().name == name

@pytest.fixture(autouse=True)
def setup():
    __create_db()

def teardown():
    __drop_db()

def __create_db():
    db.create_all()

def __drop_db():
    file_path = os.path.join(os.getcwd(), DB_NAME)
    os.remove(file_path)
