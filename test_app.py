import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200

def test_get_all_nodes(client):
    response = client.get('/nodes')
    assert response.status_code == 200

def test_get_hlr_node(client):
    response = client.get('/nodes/hlr')
    assert response.status_code == 200

def test_get_hss_node(client):
    response = client.get('/nodes/hss')
    assert response.status_code == 200

def test_get_invalid_node(client):
    response = client.get('/nodes/invalid')
    assert response.status_code == 404

def test_get_alarms(client):
    response = client.get('/alarms')
    assert response.status_code == 200