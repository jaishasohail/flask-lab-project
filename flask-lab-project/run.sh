#!/bin/bash

# Flask Lab Project - Run Script
# This script helps you quickly start the application

echo "🧪 Flask Lab Project - Launcher"
echo "================================"
echo ""

# Check if we're in the right directory
if [ ! -f "main/app.py" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    echo "   Current directory: $(pwd)"
    exit 1
fi

# Menu
echo "Choose how to run the application:"
echo ""
echo "1) Run with Python (Development mode)"
echo "2) Run with Docker"
echo "3) Run with Docker Compose"
echo "4) Run tests"
echo "5) Build Docker image only"
echo "6) Exit"
echo ""
read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo ""
        echo "🐍 Starting with Python..."
        cd main
        if [ ! -d "venv" ]; then
            echo "Creating virtual environment..."
            python3 -m venv venv
        fi
        echo "Activating virtual environment..."
        source venv/bin/activate
        echo "Installing dependencies..."
        pip install -r requirements.txt -q
        echo ""
        echo "✅ Starting Flask application..."
        echo "🌐 Access at: http://localhost:5000"
        echo "Press Ctrl+C to stop"
        echo ""
        python app.py
        ;;
    
    2)
        echo ""
        echo "🐳 Starting with Docker..."
        cd main
        echo "Building Docker image..."
        docker build -t flask-lab-project:latest .
        echo ""
        echo "Starting container..."
        docker run --rm -p 5000:5000 --name flask-lab-project flask-lab-project:latest
        ;;
    
    3)
        echo ""
        echo "🐳 Starting with Docker Compose..."
        docker-compose up
        ;;
    
    4)
        echo ""
        echo "🧪 Running tests..."
        cd main
        if [ ! -d "venv" ]; then
            python3 -m venv venv
            source venv/bin/activate
            pip install -r requirements.txt -q
        else
            source venv/bin/activate
        fi
        echo ""
        pytest tests/ -v --cov=. --cov-report=term-missing
        ;;
    
    5)
        echo ""
        echo "🔨 Building Docker image..."
        cd main
        docker build -t flask-lab-project:latest .
        echo ""
        echo "✅ Image built successfully!"
        echo "Run with: docker run -p 5000:5000 flask-lab-project:latest"
        ;;
    
    6)
        echo "Goodbye! 👋"
        exit 0
        ;;
    
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac
