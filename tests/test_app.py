import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from app import app

def test_app_is_working():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_add_task():
    client = app.test_client()
    client.post('/add', data={'content': 'Teste de QA'})
    response = client.get('/')
    assert b'Teste de QA' in response.data