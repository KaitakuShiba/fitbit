import pytest, sqlite3, os, pdb, bcrypt
from app import app, db, User
from modules.check_distance import CheckDistanceJob

DB_NAME = 'fitbit.db'

def test_check_distance():
    app.config['TESTING'] = True
    result = CheckDistanceJob().call()
    assert 'updated' == result

@pytest.fixture(autouse=True)
def setup():
    __create_db()
    email = 'sample@emxample.com'
    hashed_password = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
    db.session.add(User(
        email=email, hashed_password=hashed_password,
        client_id='client_id', client_secret='client_secret', target_distance=2,
        access_token='access_token',
        refresh_token='refresh_token'
    ))
    db.session.commit()

def teardown():
    __drop_db()

def __create_db():
    db.create_all()

def __drop_db():
    file_path = os.path.join(os.getcwd(), DB_NAME)
    os.remove(file_path)
