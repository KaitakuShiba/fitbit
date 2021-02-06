import pytest, os, pdb, fitbit, bcrypt
from app import app, db, User
from modules.check_distance import CheckDistanceJob
from datetime import datetime, timedelta, date
import slack_sdk

DB_NAME = 'fitbit.db'

def test_check_distance(mocker):
    app.config['TESTING'] = True
    # mock_distance_km: 1.60km
    mocker.patch('fitbit.api.Fitbit.intraday_time_series').return_value = {'activities-distance': [{'dateTime': '2000-01-01', 'value': '1.00'}]}
    res_mock = mocker.Mock()
    mocker.patch('slack_sdk.web.client.WebClient.chat_postMessage').return_value = res_mock
    spy = mocker.spy(slack_sdk.web.client.WebClient, 'chat_postMessage')
    CheckDistanceJob().call()
    # slackのmockが1回呼ばれていること
    assert spy.call_count == 1

@pytest.fixture(autouse=True)
def setup():
    __create_db()
    hashed_password = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
    user_1 = User(
        name='foo', hashed_password=hashed_password, target_distance=1,
        client_id='client_id', client_secret='client_secret',
        access_token='access_token',
        refresh_token='refresh_token'
    )
    yesterday = datetime.combine(date.today(), datetime.min.time()) - timedelta(seconds=1)
    user_1.created_at = yesterday
    user_1.updated_at = yesterday
    db.session.add(user_1)

    user_2 = User(
        name='bar', hashed_password=hashed_password, target_distance=1,
        client_id='client_id', client_secret='client_secret',
        access_token='access_token',
        refresh_token='refresh_token'
    )
    today = datetime.combine(date.today(), datetime.min.time())
    user_2.created_at = today
    user_2.updated_at = today
    db.session.add(user_2)

    db.session.commit()

def teardown():
    __drop_db()

def __create_db():
    db.create_all()

def __drop_db():
    file_path = os.path.join(os.getcwd(), DB_NAME)
    os.remove(file_path)
