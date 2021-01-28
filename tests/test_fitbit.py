import pytest
from app import app

def test_hello():
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/fitbit')
    assert b'Hello, Fitbit!' == result.data
