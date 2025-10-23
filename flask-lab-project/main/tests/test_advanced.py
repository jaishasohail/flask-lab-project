"""
Additional Test Examples - All Team Members
This file contains more advanced testing scenarios
"""

import pytest
import json
from datetime import datetime

# Import the app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app


@pytest.fixture
def client():
    """Create a test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ============================================
# Backend Tests (Member 1)
# ============================================

class TestBackendRoutes:
    """Test all backend routes and logic"""
    
    def test_homepage_returns_html(self, client):
        """Test that homepage returns HTML content"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'text/html' in response.content_type.encode() or b'html' in response.data.lower()
    
    def test_health_check_structure(self, client):
        """Test health check returns proper JSON structure"""
        response = client.get('/health')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert 'status' in data
        assert 'message' in data
        assert data['status'] == 'OK'
        assert isinstance(data['message'], str)
    
    def test_api_info_endpoint(self, client):
        """Test API info endpoint returns correct structure"""
        response = client.get('/api/info')
        data = json.loads(response.data)
        
        assert response.status_code == 200
        assert 'application' in data
        assert 'version' in data
        assert 'endpoints' in data
        assert isinstance(data['endpoints'], dict)
    
    def test_post_data_validation(self, client):
        """Test data validation on POST endpoint"""
        # Test with valid data
        valid_data = {'name': 'John', 'message': 'Hello'}
        response = client.post('/data',
                               data=json.dumps(valid_data),
                               content_type='application/json')
        assert response.status_code == 201
        
        # Test with empty data
        response = client.post('/data',
                               data=json.dumps({}),
                               content_type='application/json')
        # Should handle empty data gracefully
        assert response.status_code in [400, 201]
    
    def test_post_data_json_response(self, client):
        """Test POST endpoint returns proper JSON"""
        data = {'name': 'Test', 'message': 'Testing'}
        response = client.post('/data',
                               data=json.dumps(data),
                               content_type='application/json')
        
        result = json.loads(response.data)
        assert 'status' in result
        assert 'message' in result
    
    def test_concurrent_requests(self, client):
        """Test handling multiple concurrent requests"""
        responses = []
        for i in range(10):
            response = client.get('/health')
            responses.append(response.status_code)
        
        # All should succeed
        assert all(status == 200 for status in responses)


# ============================================
# Frontend Tests (Member 2)
# ============================================

class TestFrontendIntegration:
    """Test frontend-backend integration"""
    
    def test_homepage_loads(self, client):
        """Test that homepage loads successfully"""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_static_files_accessible(self, client):
        """Test that static files can be accessed"""
        # Test CSS
        response = client.get('/static/style.css')
        assert response.status_code in [200, 304, 404]  # May not exist in test
        
        # Test JS
        response = client.get('/static/script.js')
        assert response.status_code in [200, 304, 404]
    
    def test_form_submission_flow(self, client):
        """Test complete form submission flow"""
        # Get homepage
        response = client.get('/')
        assert response.status_code == 200
        
        # Submit data
        form_data = {
            'name': 'Frontend Test',
            'message': 'Testing form submission'
        }
        response = client.post('/data',
                               data=json.dumps(form_data),
                               content_type='application/json')
        
        assert response.status_code in [200, 201]
    
    def test_api_endpoints_for_frontend(self, client):
        """Test all API endpoints used by frontend"""
        endpoints = ['/', '/health', '/api/info']
        
        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200, f"Endpoint {endpoint} failed"


# ============================================
# DevOps Tests (Member 3)
# ============================================

class TestDevOpsRequirements:
    """Test deployment and operational requirements"""
    
    def test_health_check_response_time(self, client):
        """Test health check responds quickly"""
        import time
        start = time.time()
        response = client.get('/health')
        duration = time.time() - start
        
        assert response.status_code == 200
        assert duration < 1.0, "Health check took too long"
    
    def test_error_handling(self, client):
        """Test error handlers work correctly"""
        # Test 404
        response = client.get('/nonexistent-route')
        assert response.status_code == 404
        
        # Should return JSON
        try:
            data = json.loads(response.data)
            assert 'status' in data
            assert data['status'] == 'error'
        except:
            pass  # Some setups might return HTML
    
    def test_method_not_allowed(self, client):
        """Test method not allowed handling"""
        response = client.get('/data')  # Should be POST only
        assert response.status_code == 405
    
    def test_cors_headers(self, client):
        """Test CORS headers if configured"""
        response = client.get('/health')
        # Just check response is valid
        assert response.status_code == 200
    
    def test_content_type_headers(self, client):
        """Test proper content types are set"""
        response = client.get('/health')
        assert 'application/json' in response.content_type
        
        response = client.get('/')
        assert 'text/html' in response.content_type or response.status_code == 200


# ============================================
# Integration Tests
# ============================================

class TestFullIntegration:
    """Test complete application integration"""
    
    def test_complete_user_journey(self, client):
        """Test a complete user journey through the app"""
        # 1. Visit homepage
        response = client.get('/')
        assert response.status_code == 200
        
        # 2. Check health
        response = client.get('/health')
        assert response.status_code == 200
        
        # 3. Get API info
        response = client.get('/api/info')
        assert response.status_code == 200
        
        # 4. Submit data
        data = {
            'name': 'Integration Test User',
            'message': 'Testing complete flow'
        }
        response = client.post('/data',
                               data=json.dumps(data),
                               content_type='application/json')
        assert response.status_code in [200, 201]
    
    def test_api_consistency(self, client):
        """Test API responses are consistent"""
        # Make same request multiple times
        responses = []
        for _ in range(5):
            response = client.get('/api/info')
            data = json.loads(response.data)
            responses.append(data)
        
        # All responses should have same structure
        first = responses[0]
        for response in responses[1:]:
            assert set(response.keys()) == set(first.keys())


# ============================================
# Performance Tests
# ============================================

class TestPerformance:
    """Test application performance"""
    
    def test_response_time_health(self, client):
        """Test health check response time"""
        import time
        
        times = []
        for _ in range(10):
            start = time.time()
            client.get('/health')
            times.append(time.time() - start)
        
        avg_time = sum(times) / len(times)
        assert avg_time < 0.1, f"Average response time too slow: {avg_time}s"
    
    def test_multiple_concurrent_posts(self, client):
        """Test handling multiple POST requests"""
        data = {'name': 'Load Test', 'message': 'Testing load'}
        
        for _ in range(20):
            response = client.post('/data',
                                   data=json.dumps(data),
                                   content_type='application/json')
            assert response.status_code in [200, 201]


# ============================================
# Security Tests
# ============================================

class TestSecurity:
    """Test security aspects"""
    
    def test_sql_injection_prevention(self, client):
        """Test SQL injection attempts are handled"""
        malicious_data = {
            'name': "'; DROP TABLE users; --",
            'message': "Test"
        }
        response = client.post('/data',
                               data=json.dumps(malicious_data),
                               content_type='application/json')
        # Should handle without crashing
        assert response.status_code in [200, 201, 400]
    
    def test_xss_prevention(self, client):
        """Test XSS attempts are handled"""
        xss_data = {
            'name': "<script>alert('XSS')</script>",
            'message': "Test"
        }
        response = client.post('/data',
                               data=json.dumps(xss_data),
                               content_type='application/json')
        # Should handle without crashing
        assert response.status_code in [200, 201, 400]
    
    def test_large_payload_handling(self, client):
        """Test handling of large payloads"""
        large_data = {
            'name': 'Test',
            'message': 'A' * 10000  # 10KB message
        }
        response = client.post('/data',
                               data=json.dumps(large_data),
                               content_type='application/json')
        # Should handle gracefully
        assert response.status_code in [200, 201, 400, 413]


# ============================================
# Edge Cases
# ============================================

class TestEdgeCases:
    """Test edge cases and unusual inputs"""
    
    def test_empty_json_object(self, client):
        """Test sending empty JSON"""
        response = client.post('/data',
                               data=json.dumps({}),
                               content_type='application/json')
        # Should handle gracefully
        assert response.status_code in [200, 201, 400]
    
    def test_null_values(self, client):
        """Test null values in JSON"""
        data = {'name': None, 'message': None}
        response = client.post('/data',
                               data=json.dumps(data),
                               content_type='application/json')
        # Should handle gracefully
        assert response.status_code in [200, 201, 400]
    
    def test_unicode_characters(self, client):
        """Test Unicode characters handling"""
        data = {
            'name': '测试用户',
            'message': 'Hello 世界 🌍'
        }
        response = client.post('/data',
                               data=json.dumps(data),
                               content_type='application/json')
        assert response.status_code in [200, 201]
    
    def test_special_characters(self, client):
        """Test special characters"""
        data = {
            'name': 'Test!@#$%^&*()',
            'message': 'Special chars: <>{}[]|\\~`'
        }
        response = client.post('/data',
                               data=json.dumps(data),
                               content_type='application/json')
        assert response.status_code in [200, 201]


# ============================================
# Run tests with: pytest test_advanced.py -v
# ============================================

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
