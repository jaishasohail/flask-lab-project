"""
Flask Lab Project - Main Application
A collaborative Flask application with CI/CD and Docker support
"""

from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'


@app.route('/')
def home():
    """Homepage route - displays welcome message"""
    return render_template('index.html')


@app.route('/health')
def health():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'OK',
        'message': 'Application is running successfully'
    }), 200


@app.route('/data', methods=['POST'])
def receive_data():
    """POST endpoint to receive and process data"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'status': 'error',
                'message': 'No data provided'
            }), 400
        
        # Process the data (simple echo for now)
        response = {
            'status': 'success',
            'message': 'Data received successfully',
            'received_data': data
        }
        
        return jsonify(response), 201
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error processing data: {str(e)}'
        }), 500


@app.route('/api/info')
def api_info():
    """API information endpoint"""
    return jsonify({
        'application': 'Flask Lab Project',
        'version': '1.0.0',
        'endpoints': {
            '/': 'Homepage',
            '/health': 'Health check',
            '/data': 'POST endpoint for data submission',
            '/api/info': 'API information'
        }
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Resource not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=app.config['DEBUG'])
