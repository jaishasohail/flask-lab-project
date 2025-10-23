"""
Unit tests for Flask Lab Project
Tests all routes and functionality
"""

import pytest
import json
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app


@pytest.fixture
def client():
    """Create a test client for the app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the homepage route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Flask Lab Project' in response.data or response.status_code == 200


def test_health(client):
    """Test the health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'OK'
    assert 'message' in data


def test_api_info(client):
    """Test the API info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'application' in data
    assert 'version' in data
    assert 'endpoints' in data


def test_post_data_success(client):
    """Test POST endpoint with valid data"""
    test_data = {
        'name': 'Test User',
        'message': 'Hello from tests'
    }
    response = client.post(
        '/data',
        data=json.dumps(test_data),
        content_type='application/json'
    )
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['status'] == 'success'
    assert 'received_data' in data


def test_post_data_no_data(client):
    """Test POST endpoint with no data"""
    response = client.post(
        '/data',
        data=json.dumps(None),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['status'] == 'error'


def test_post_data_invalid_json(client):
    """Test POST endpoint with invalid JSON"""
    response = client.post(
        '/data',
        data='invalid json',
        content_type='application/json'
    )
    # Should return 400 or 500 depending on Flask version
    assert response.status_code in [400, 415, 500]


def test_404_error(client):
    """Test 404 error handler"""
    response = client.get('/nonexistent')
    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['status'] == 'error'


def test_health_response_format(client):
    """Test health endpoint response structure"""
    response = client.get('/health')
    data = json.loads(response.data)
    assert isinstance(data, dict)
    assert 'status' in data
    assert 'message' in data


def test_post_endpoint_methods(client):
    """Test that /data only accepts POST"""
    response = client.get('/data')
    assert response.status_code == 405  # Method Not Allowed
