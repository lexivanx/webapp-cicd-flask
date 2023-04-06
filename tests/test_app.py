import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    rv = client.get('/')
    assert rv.status_code == 302

def test_login_page(client):
    rv = client.get('/login')
    assert rv.status_code == 200
    assert b'Login' in rv.data

def test_register_page(client):
    rv = client.get('/register')
    assert rv.status_code == 200
    assert b'Register' in rv.data

def test_valid_login(client):
    rv = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Login requested for user testuser, password=testpassword' in rv.data

def test_invalid_login(client):
    rv = client.post('/login', data={'username': '', 'password': 'testpassword'})
    assert rv.status_code == 200
    assert b'This field is required.' in rv.data

def test_valid_registration(client):
    rv = client.post('/register', data={'username': 'testuser', 'password': 'testpassword', 'email': 'test@example.com'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Registration requested for user testuser, password=testpassword, email=test@example.com' in rv.data

def test_invalid_registration(client):
    rv = client.post('/register', data={'username': 'testuser', 'password': 'testpassword', 'email': 'invalid_email'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Invalid email address.' in rv.data
