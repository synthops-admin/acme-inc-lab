import pytest
import json
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_endpoint(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert data['version'] == '1.0.0'

def test_home_endpoint(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['service'] == 'web-application'
    assert data['version'] == '1.0.0'
    assert 'endpoints' in data

def test_info_endpoint(client):
    """Test the info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['application'] == 'ACME Web Application'
    assert data['version'] == '1.0.0'
    assert 'environment' in data
    assert 'uptime' in data

def test_nonexistent_endpoint(client):
    """Test that nonexistent endpoints return 404"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
