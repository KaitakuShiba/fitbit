import pytest, sqlite3, os
from app import app

DB_NAME = 'fitbit.db'

def test_registration():
    app.config['TESTING'] = True
    client = app.test_client()
    data = {'client_id': 'client_id', 'client_secret': 'client_secret', 'target_distance': 2 }
    result = client.post('/registration', data=data)

    assert b'success' == result.data

@pytest.fixture(autouse=True)
def setup():
    __create_db()

def teardown():
    __drop_db()

def __create_db():
    conn = sqlite3.connect(DB_NAME).cursor()
    conn.execute('''CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT, client_id STRING, client_secret STRING, target_distance INTEGER)'''
    )

def __drop_db():
    file_path = os.path.join(os.getcwd(), DB_NAME)
    os.remove(file_path)
