# 📁 Project Structure

```
flask-lab-project/
│
├── 📄 README.md                          # Main project documentation
├── 📄 QUICKSTART.md                      # Quick start guide
├── 📄 GITHUB_SETUP.md                    # GitHub setup instructions
├── 📄 SUBMISSION_CHECKLIST.md            # Submission requirements
├── 📄 .gitignore                         # Git ignore rules
├── 📄 docker-compose.yml                 # Docker Compose configuration
├── 📄 run.sh                             # Convenience run script
│
├── 📁 main/                              # Main application directory
│   ├── 📄 app.py                         # Flask application (CORE FILE)
│   ├── 📄 requirements.txt               # Python dependencies
│   ├── 📄 Dockerfile                     # Docker configuration
│   ├── 📄 .dockerignore                  # Docker ignore rules
│   ├── 📄 pytest.ini                     # Pytest configuration
│   │
│   ├── 📁 tests/                         # Test suite
│   │   ├── 📄 __init__.py
│   │   └── 📄 test_app.py                # Unit tests (10+ tests)
│   │
│   ├── 📁 templates/                     # HTML templates
│   │   └── 📄 index.html                 # Homepage template
│   │
│   ├── 📁 static/                        # Static files
│   │   ├── 📄 style.css                  # Stylesheet
│   │   └── 📄 script.js                  # Frontend JavaScript
│   │
│   └── 📁 .github/                       # GitHub Actions
│       └── 📁 workflows/
│           └── 📄 ci-cd.yml              # CI/CD pipeline
│
├── 📁 member1_backend/                   # Backend Lead workspace
│   └── 📄 README.md                      # Backend member guide
│
├── 📁 member2_frontend/                  # Frontend Lead workspace
│   └── 📄 README.md                      # Frontend member guide
│
└── 📁 member3_devops/                    # DevOps workspace
    └── 📄 README.md                      # DevOps member guide
```

## 📋 File Count Summary

| Category | Count | Files |
|----------|-------|-------|
| Python Files | 2 | app.py, test_app.py |
| HTML Templates | 1 | index.html |
| CSS Files | 1 | style.css |
| JavaScript Files | 1 | script.js |
| Configuration Files | 6 | requirements.txt, Dockerfile, docker-compose.yml, pytest.ini, .dockerignore, .gitignore |
| CI/CD Files | 1 | ci-cd.yml |
| Documentation Files | 8 | README.md files and guides |
| Shell Scripts | 1 | run.sh |
| **TOTAL** | **21** | **Complete project** |

## 🎯 Key Files Overview

### Core Application Files
- **app.py** - Main Flask application with all routes
- **requirements.txt** - Python package dependencies
- **Dockerfile** - Container configuration

### Frontend Files
- **templates/index.html** - Main HTML page
- **static/style.css** - Styling (responsive design)
- **static/script.js** - Frontend interactivity

### Testing & CI/CD
- **tests/test_app.py** - Comprehensive unit tests
- **.github/workflows/ci-cd.yml** - Automated pipeline

### Documentation
- **README.md** - Complete project documentation
- **QUICKSTART.md** - Fast setup guide
- **GITHUB_SETUP.md** - Repository setup
- **SUBMISSION_CHECKLIST.md** - Submission guide

### Member Workspaces
- **member1_backend/** - Backend development area
- **member2_frontend/** - Frontend development area
- **member3_devops/** - DevOps work area

## 📊 Lines of Code

| File | Approximate Lines |
|------|-------------------|
| app.py | ~100 lines |
| test_app.py | ~120 lines |
| index.html | ~110 lines |
| style.css | ~280 lines |
| script.js | ~40 lines |
| ci-cd.yml | ~130 lines |
| Dockerfile | ~30 lines |
| **Total Code** | **~810 lines** |

## 🔍 What Each Directory Contains

### `/main` - Production Code
All application code that runs in production:
- Flask backend
- HTML/CSS/JS frontend
- Tests
- Docker configuration
- CI/CD pipeline

### `/member1_backend` - Backend Workspace
Working area for backend developer:
- Backend development guidelines
- Task checklist
- Git workflow instructions

### `/member2_frontend` - Frontend Workspace
Working area for frontend developer:
- Frontend development guidelines
- Design specifications
- Integration instructions

### `/member3_devops` - DevOps Workspace
Working area for DevOps engineer:
- Docker guidelines
- CI/CD configuration help
- Deployment procedures

## 📦 Dependencies

### Python Packages (requirements.txt)
```
Flask==3.0.0          # Web framework
Werkzeug==3.0.1       # WSGI utilities
pytest==7.4.3         # Testing framework
pytest-cov==4.1.0     # Code coverage
gunicorn==21.2.0      # Production server
```

## 🚀 Entry Points

### Development
```bash
python main/app.py
```

### Production (Docker)
```bash
docker run -p 5000:5000 flask-lab-project
```

### Testing
```bash
pytest main/tests/
```

## 🔗 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Homepage |
| `/health` | GET | Health check |
| `/data` | POST | Submit data |
| `/api/info` | GET | API information |

---

**Last Updated:** October 2025
**Version:** 1.0.0
