import pytest
from app import app

def test_hello():
    app.config['TESTING'] = True
    client = app.test_client()
    result = client.get('/')
    assert b'Hello, World!' == result.data
