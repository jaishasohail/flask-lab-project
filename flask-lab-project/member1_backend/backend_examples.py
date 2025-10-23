"""
Member 1 - Backend Lead
Additional backend functionality examples

This file demonstrates backend features that Member 1 can implement.
Copy relevant code to main/app.py or create separate modules.
"""

from flask import Flask, jsonify, request
from datetime import datetime
import json

# Example 1: User Management Routes
def create_user_routes(app):
    """User management endpoints"""
    
    # In-memory storage (for demo - use database in production)
    users = []
    
    @app.route('/api/users', methods=['GET'])
    def get_users():
        """Get all users"""
        return jsonify({
            'status': 'success',
            'count': len(users),
            'users': users
        }), 200
    
    @app.route('/api/users', methods=['POST'])
    def create_user():
        """Create a new user"""
        data = request.get_json()
        
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Name and email are required'
            }), 400
        
        user = {
            'id': len(users) + 1,
            'name': data['name'],
            'email': data['email'],
            'created_at': datetime.now().isoformat()
        }
        users.append(user)
        
        return jsonify({
            'status': 'success',
            'message': 'User created successfully',
            'user': user
        }), 201
    
    @app.route('/api/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        """Get specific user by ID"""
        user = next((u for u in users if u['id'] == user_id), None)
        
        if not user:
            return jsonify({
                'status': 'error',
                'message': 'User not found'
            }), 404
        
        return jsonify({
            'status': 'success',
            'user': user
        }), 200


# Example 2: Data Processing Functions
class DataProcessor:
    """Backend business logic for data processing"""
    
    @staticmethod
    def validate_data(data):
        """Validate incoming data"""
        required_fields = ['name', 'message']
        
        for field in required_fields:
            if field not in data:
                return False, f"Missing required field: {field}"
        
        if len(data['name']) < 2:
            return False, "Name must be at least 2 characters"
        
        if len(data['message']) < 5:
            return False, "Message must be at least 5 characters"
        
        return True, "Valid"
    
    @staticmethod
    def process_data(data):
        """Process and transform data"""
        processed = {
            'original': data,
            'processed': {
                'name': data['name'].strip().title(),
                'message': data['message'].strip(),
                'word_count': len(data['message'].split()),
                'char_count': len(data['message']),
                'timestamp': datetime.now().isoformat()
            }
        }
        return processed
    
    @staticmethod
    def calculate_statistics(data_list):
        """Calculate statistics from data"""
        if not data_list:
            return {
                'total': 0,
                'average_length': 0,
                'longest': None,
                'shortest': None
            }
        
        messages = [item.get('message', '') for item in data_list]
        lengths = [len(msg) for msg in messages]
        
        return {
            'total': len(data_list),
            'average_length': sum(lengths) / len(lengths),
            'longest': max(messages, key=len),
            'shortest': min(messages, key=len),
            'total_words': sum(len(msg.split()) for msg in messages)
        }


# Example 3: Advanced API Routes with Processing
def create_advanced_routes(app):
    """Advanced backend routes with business logic"""
    
    # Storage
    messages = []
    processor = DataProcessor()
    
    @app.route('/api/messages', methods=['GET'])
    def get_messages():
        """Get all messages with statistics"""
        stats = processor.calculate_statistics(messages)
        
        return jsonify({
            'status': 'success',
            'count': len(messages),
            'statistics': stats,
            'messages': messages
        }), 200
    
    @app.route('/api/messages', methods=['POST'])
    def create_message():
        """Create a new message with validation and processing"""
        data = request.get_json()
        
        # Validate
        is_valid, message = processor.validate_data(data)
        if not is_valid:
            return jsonify({
                'status': 'error',
                'message': message
            }), 400
        
        # Process
        processed = processor.process_data(data)
        processed['id'] = len(messages) + 1
        messages.append(processed)
        
        return jsonify({
            'status': 'success',
            'message': 'Message created and processed',
            'data': processed
        }), 201
    
    @app.route('/api/messages/<int:message_id>', methods=['DELETE'])
    def delete_message(message_id):
        """Delete a message"""
        global messages
        original_count = len(messages)
        messages = [m for m in messages if m.get('id') != message_id]
        
        if len(messages) == original_count:
            return jsonify({
                'status': 'error',
                'message': 'Message not found'
            }), 404
        
        return jsonify({
            'status': 'success',
            'message': 'Message deleted successfully'
        }), 200
    
    @app.route('/api/messages/search', methods=['GET'])
    def search_messages():
        """Search messages by keyword"""
        keyword = request.args.get('q', '').lower()
        
        if not keyword:
            return jsonify({
                'status': 'error',
                'message': 'Search query required'
            }), 400
        
        results = [
            msg for msg in messages 
            if keyword in msg['processed']['message'].lower() or 
               keyword in msg['processed']['name'].lower()
        ]
        
        return jsonify({
            'status': 'success',
            'query': keyword,
            'count': len(results),
            'results': results
        }), 200


# Example 4: Database Helper (for future expansion)
class DatabaseHelper:
    """Helper class for database operations (placeholder for real DB)"""
    
    def __init__(self):
        self.data = {}
    
    def save(self, collection, data):
        """Save data to collection"""
        if collection not in self.data:
            self.data[collection] = []
        
        data['id'] = len(self.data[collection]) + 1
        data['created_at'] = datetime.now().isoformat()
        self.data[collection].append(data)
        return data
    
    def find_all(self, collection):
        """Get all items from collection"""
        return self.data.get(collection, [])
    
    def find_by_id(self, collection, item_id):
        """Find item by ID"""
        items = self.data.get(collection, [])
        return next((item for item in items if item['id'] == item_id), None)
    
    def update(self, collection, item_id, updates):
        """Update an item"""
        item = self.find_by_id(collection, item_id)
        if item:
            item.update(updates)
            item['updated_at'] = datetime.now().isoformat()
            return item
        return None
    
    def delete(self, collection, item_id):
        """Delete an item"""
        if collection in self.data:
            self.data[collection] = [
                item for item in self.data[collection] 
                if item['id'] != item_id
            ]
            return True
        return False


# Example 5: Authentication Middleware (simple example)
def require_api_key(f):
    """Decorator to require API key for routes"""
    from functools import wraps
    
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        
        # Simple API key check (use proper auth in production)
        if api_key != 'your-secret-api-key':
            return jsonify({
                'status': 'error',
                'message': 'Invalid or missing API key'
            }), 401
        
        return f(*args, **kwargs)
    return decorated_function


# Example usage in routes:
def create_protected_routes(app):
    """Example of protected routes"""
    
    @app.route('/api/admin/stats', methods=['GET'])
    @require_api_key
    def admin_stats():
        """Protected admin endpoint"""
        return jsonify({
            'status': 'success',
            'message': 'This is a protected endpoint',
            'data': {
                'total_requests': 1000,
                'active_users': 50
            }
        }), 200


# Integration Example: How to add to main app.py
"""
To integrate these features into main/app.py:

1. Copy the functions you want to use
2. Add to your app.py file
3. Call the setup functions:

from flask import Flask
app = Flask(__name__)

# Add user routes
create_user_routes(app)

# Add advanced routes
create_advanced_routes(app)

# Add protected routes
create_protected_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
"""


# Example 6: Error Handler Extensions
def setup_error_handlers(app):
    """Extended error handling"""
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'status': 'error',
            'message': 'Bad request',
            'error': str(error)
        }), 400
    
    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'status': 'error',
            'message': 'Unauthorized access'
        }), 401
    
    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'status': 'error',
            'message': 'Forbidden'
        }), 403
    
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'status': 'error',
            'message': 'Method not allowed'
        }), 405


# Example 7: Logging Helper
class Logger:
    """Simple logging helper"""
    
    @staticmethod
    def log_request(endpoint, method, data=None):
        """Log API request"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'endpoint': endpoint,
            'method': method,
            'data': data
        }
        print(f"[{log_entry['timestamp']}] {method} {endpoint}")
        return log_entry
    
    @staticmethod
    def log_error(error, context=None):
        """Log error"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'error': str(error),
            'context': context
        }
        print(f"[ERROR] {log_entry['timestamp']}: {error}")
        return log_entry


if __name__ == '__main__':
    print("Backend Examples - Member 1 (Backend Lead)")
    print("=" * 50)
    print("\nThis file contains example backend code.")
    print("Copy relevant sections to main/app.py to implement.")
    print("\nFeatures included:")
    print("- User management routes")
    print("- Data processing and validation")
    print("- Advanced API routes")
    print("- Database helper class")
    print("- Authentication middleware")
    print("- Error handlers")
    print("- Logging utilities")
