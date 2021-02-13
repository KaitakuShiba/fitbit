import pytest, os, pdb, bcrypt
from app import app, db, User, fitbit
from flask_login import login_user
import modules.gather_keys_oauth2

DB_NAME = 'fitbit.db'
name = 'foo'

def test_fitbit_token(mocker):
    app.config['TESTING'] = True
    client = app.test_client()
    user = User.query.filter_by(name=name).first()
    # res_mock = mocker.Mock()
    # mocker.patch('modules.gather_keys_oauth2.OAuth2Server.browser_authorize').return_value = res_mock
    # TODO:with mocker.patch('modules.gather_keys_oauth2.OAuth2Server.browser_authorize.fitbit.client.session.token', new_callable=mocker.PropertyMock) as mock_foo:
    # TODO:上記は後でモックできたら直す
    result = client.get('/fitbit/users', query_string={'user_id': user.id, 'target_distance': 3})
    assert b'Registered! Close browser.' == result.data

pytest.fixture(autouse=True)
def setup():
    app.config['LOGIN_DISABLED'] = True
    __create_db()
    hashed_password = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
    db.session.add(User(name=name, hashed_password=hashed_password, client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET')))
    db.session.commit()

def teardown():
    app.config['LOGIN_DISABLED'] = False
    __drop_db()

def __create_db():
    db.create_all()

def __drop_db():
    file_path = os.path.join(os.getcwd(), DB_NAME)
    os.remove(file_path)
