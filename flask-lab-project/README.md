# 🧪 Flask Lab Project - Collaborative Application with CI/CD & Docker

[![CI/CD Pipeline](https://github.com/YOUR_USERNAME/flask-lab-project/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/YOUR_USERNAME/flask-lab-project/actions)
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)

A collaborative Flask web application demonstrating modern DevOps practices including containerization with Docker and automated CI/CD with GitHub Actions.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Team Structure](#team-structure)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Testing](#testing)
- [Docker Deployment](#docker-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)

## 🎯 Project Overview

This project demonstrates a complete development workflow for a modern web application, including:

- **Backend Development**: RESTful API with Flask
- **Frontend Development**: Responsive HTML/CSS/JavaScript interface
- **DevOps**: Docker containerization and GitHub Actions CI/CD
- **Testing**: Automated unit tests with pytest
- **Collaboration**: Git workflow with branches and pull requests

## 👥 Team Structure

### Member 1 - Backend Lead
**Responsibilities:**
- Implement core Flask routes and application logic
- Create and maintain API endpoints
- Handle data processing and business logic
- Write backend unit tests

**Branch:** `backend`

### Member 2 - Frontend/API Integration Lead
**Responsibilities:**
- Design and implement HTML templates
- Create CSS styling and responsive design
- Develop JavaScript for API interaction
- Integrate frontend with backend APIs

**Branch:** `frontend`

### Member 3 - DevOps Engineer
**Responsibilities:**
- Create and maintain Dockerfile
- Set up and manage CI/CD pipeline
- Configure automated testing
- Document deployment procedures

**Branch:** `devops`

## ✨ Features

- **Homepage**: User-friendly landing page with project information
- **Health Check**: Monitoring endpoint for application status (`/health`)
- **Data Submission**: POST endpoint for data handling (`/data`)
- **API Information**: Endpoint documenting available APIs (`/api/info`)
- **Error Handling**: Comprehensive 404 and 500 error handlers
- **Responsive Design**: Mobile-friendly interface
- **Docker Support**: Containerized deployment
- **CI/CD Pipeline**: Automated testing and building

## 📁 Project Structure

```
flask-lab-project/
│
├── main/                          # Main application directory
│   ├── app.py                     # Flask application
│   ├── requirements.txt           # Python dependencies
│   ├── Dockerfile                 # Docker configuration
│   ├── .dockerignore             # Docker ignore rules
│   │
│   ├── tests/                     # Test suite
│   │   ├── __init__.py
│   │   └── test_app.py           # Unit tests
│   │
│   ├── templates/                 # HTML templates
│   │   └── index.html            # Homepage
│   │
│   ├── static/                    # Static files
│   │   ├── style.css             # Stylesheet
│   │   └── script.js             # JavaScript
│   │
│   └── .github/                   # GitHub Actions
│       └── workflows/
│           └── ci-cd.yml         # CI/CD pipeline
│
├── member1_backend/               # Backend lead workspace
│   └── README.md
│
├── member2_frontend/              # Frontend lead workspace
│   └── README.md
│
├── member3_devops/                # DevOps workspace
│   └── README.md
│
└── README.md                      # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Docker (optional, for containerization)
- Git
- pip (Python package manager)

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/flask-lab-project.git
   cd flask-lab-project
   ```

2. **Navigate to main directory:**
   ```bash
   cd main
   ```

3. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Access the application:**
   Open your browser and navigate to `http://localhost:5000`

## 🔄 Development Workflow

### For All Team Members

1. **Clone and setup:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/flask-lab-project.git
   cd flask-lab-project
   ```

2. **Create your feature branch:**
   ```bash
   git checkout -b your-branch-name
   # Backend lead: git checkout -b backend
   # Frontend lead: git checkout -b frontend
   # DevOps: git checkout -b devops
   ```

3. **Make your changes:**
   - Backend Lead: Work in `main/app.py` and related files
   - Frontend Lead: Work in `main/templates/` and `main/static/`
   - DevOps: Work on `main/Dockerfile` and `.github/workflows/`

4. **Test your changes locally:**
   ```bash
   cd main
   python app.py
   # Or run tests: pytest tests/
   ```

5. **Commit and push:**
   ```bash
   git add .
   git commit -m "descriptive message about your changes"
   git push origin your-branch-name
   ```

6. **Create Pull Request:**
   - Go to GitHub repository
   - Click "Pull Requests" → "New Pull Request"
   - Select your branch
   - Add description of changes
   - Request review from team members

7. **Merge after approval:**
   - Once approved, merge to `main`
   - CI/CD pipeline will automatically run

## 🧪 Testing

### Run Tests Locally

```bash
cd main
pytest tests/ -v
```

### Run Tests with Coverage

```bash
pytest tests/ --cov=. --cov-report=term-missing
```

### Test Individual Files

```bash
pytest tests/test_app.py -v
```

### Available Tests

- `test_home`: Tests homepage route
- `test_health`: Tests health check endpoint
- `test_api_info`: Tests API information endpoint
- `test_post_data_success`: Tests successful data submission
- `test_post_data_no_data`: Tests error handling
- `test_404_error`: Tests 404 error handler
- And more...

## 🐳 Docker Deployment

### Build Docker Image

```bash
cd main
docker build -t flask-lab-project:latest .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 --name flask-app flask-lab-project:latest
```

### Access Logs

```bash
docker logs flask-app
```

### Stop Container

```bash
docker stop flask-app
docker rm flask-app
```

### Docker Commands Reference

```bash
# Build image
docker build -t flask-lab-project:latest .

# Run container (detached)
docker run -d -p 5000:5000 --name flask-app flask-lab-project:latest

# Run container (interactive)
docker run -it -p 5000:5000 flask-lab-project:latest

# View running containers
docker ps

# Execute command in container
docker exec -it flask-app /bin/bash

# View logs
docker logs -f flask-app

# Stop and remove
docker stop flask-app && docker rm flask-app

# Remove image
docker rmi flask-lab-project:latest
```

## 🔄 CI/CD Pipeline

### Pipeline Stages

The GitHub Actions pipeline runs automatically on push to `main` or pull requests:

1. **Test Job**
   - Sets up Python environment
   - Installs dependencies
   - Runs pytest with coverage
   - Generates test reports

2. **Build Job**
   - Builds Docker image
   - Tests Docker image health
   - Saves image as artifact

3. **Docker Hub Push (Optional)**
   - Pushes image to Docker Hub
   - Only on main branch pushes
   - Requires Docker Hub credentials

4. **Deployment Summary**
   - Generates summary of all jobs
   - Shows test and build status

### Setting Up CI/CD

1. **No additional setup needed** - Pipeline runs automatically on push

2. **(Optional) Set up Docker Hub integration:**
   - Go to repository Settings → Secrets and variables → Actions
   - Add secrets:
     - `DOCKER_USERNAME`: Your Docker Hub username
     - `DOCKER_PASSWORD`: Your Docker Hub password/token
   - Pipeline will automatically push to Docker Hub

### Viewing Pipeline Results

1. Go to repository on GitHub
2. Click "Actions" tab
3. Select the workflow run to view details
4. Check individual job logs for details

## 📡 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Homepage
```http
GET /
```
Returns the main HTML homepage.

**Response:** HTML page

---

#### 2. Health Check
```http
GET /health
```
Returns application health status.

**Response:**
```json
{
  "status": "OK",
  "message": "Application is running successfully"
}
```

---

#### 3. Submit Data
```http
POST /data
Content-Type: application/json

{
  "name": "John Doe",
  "message": "Hello World"
}
```

**Success Response (201):**
```json
{
  "status": "success",
  "message": "Data received successfully",
  "received_data": {
    "name": "John Doe",
    "message": "Hello World"
  }
}
```

**Error Response (400):**
```json
{
  "status": "error",
  "message": "No data provided"
}
```

---

#### 4. API Information
```http
GET /api/info
```

**Response:**
```json
{
  "application": "Flask Lab Project",
  "version": "1.0.0",
  "endpoints": {
    "/": "Homepage",
    "/health": "Health check",
    "/data": "POST endpoint for data submission",
    "/api/info": "API information"
  }
}
```

### Testing with cURL

```bash
# Health check
curl http://localhost:5000/health

# Submit data
curl -X POST http://localhost:5000/data \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","message":"Hello from cURL"}'

# API info
curl http://localhost:5000/api/info
```

## 🤝 Contributing

### Branch Naming Convention

- `backend` - Backend development
- `frontend` - Frontend development
- `devops` - DevOps and infrastructure
- `feature/feature-name` - New features
- `bugfix/bug-name` - Bug fixes
- `hotfix/issue-name` - Urgent fixes

### Commit Message Convention

```
feat: add new feature
fix: fix a bug
docs: update documentation
style: formatting changes
refactor: code restructuring
test: add or update tests
chore: maintenance tasks
ci: CI/CD changes
```

### Pull Request Process

1. Create feature branch from `main`
2. Make your changes
3. Run tests locally
4. Commit with descriptive message
5. Push to GitHub
6. Create Pull Request
7. Request review from team members
8. Address review comments
9. Merge after approval

## 🔧 Troubleshooting

### Common Issues

**Issue: Port 5000 already in use**
```bash
# Find process using port 5000
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# Kill the process or use different port
export PORT=5001
python app.py
```

**Issue: Module not found**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

**Issue: Docker build fails**
```bash
# Clear Docker cache
docker system prune -a
# Rebuild
docker build --no-cache -t flask-lab-project:latest .
```

**Issue: Tests failing**
```bash
# Check Python path
export PYTHONPATH="${PYTHONPATH}:${PWD}"
pytest tests/ -v
```

### Getting Help

- Check the GitHub Issues tab
- Review CI/CD logs in Actions tab
- Consult team members' README files in their directories
- Review Flask documentation: https://flask.palletsprojects.com/
- Review Docker documentation: https://docs.docker.com/

## 📝 Submission Requirements

For lab submission, ensure you have:

- ✅ GitHub repository link
- ✅ Screenshot of successful CI/CD run
- ✅ Screenshot of application running via Docker
- ✅ This README.md with all sections completed
- ✅ All team members listed with their roles
- ✅ Instructions for building, testing, and running

## 📄 License

This project is created for educational purposes as part of a lab assignment.

## 👏 Acknowledgments

- Flask Framework
- Docker
- GitHub Actions
- pytest

---

**Built with ❤️ by Team Flask Lab**

*Last Updated: October 2025*
