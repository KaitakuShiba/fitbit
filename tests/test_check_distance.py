import pytest, os, pdb, fitbit, bcrypt
from app import app, db, User
from modules.check_distance import CheckDistanceJob
import slack_sdk

DB_NAME = 'fitbit.db'

def test_check_distance(mocker):
    app.config['TESTING'] = True
    # mock_distance_km: 1.60km
    mocker.patch('fitbit.api.Fitbit.intraday_time_series').return_value = {'activities-distance': [{'dateTime': '2000-01-01', 'value': '1.00'}]}
    res_mock = mocker.Mock()
    mocker.patch('slack_sdk.web.client.WebClient.chat_postMessage').return_value = res_mock
    result = CheckDistanceJob().call()
    assert 'updated!' == result

@pytest.fixture(autouse=True)
def setup():
    __create_db()
    hashed_password = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
    db.session.add(User(
        name='foo', hashed_password=hashed_password, target_distance=1,
        client_id='client_id', client_secret='client_secret',
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
