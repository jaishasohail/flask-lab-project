# 👥 Team Member Examples & Collaboration Guide

This document shows specific code examples for each team member's responsibilities.

## 📋 Table of Contents

1. [Member 1 - Backend Lead](#member-1---backend-lead)
2. [Member 2 - Frontend Lead](#member-2---frontend-lead)
3. [Member 3 - DevOps Engineer](#member-3---devops-engineer)
4. [Integration Guide](#integration-guide)
5. [Testing Guide](#testing-guide)

---

## Member 1 - Backend Lead

### 📁 Your Files
- `main/app.py` - Main Flask application
- `member1_backend/backend_examples.py` - Additional backend examples
- `main/tests/test_app.py` - Unit tests

### 🎯 Your Responsibilities

#### 1. Core Flask Routes (in `main/app.py`)

```python
@app.route('/')
def home():
    """Homepage route"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'OK', 'message': 'Application is running'})

@app.route('/data', methods=['POST'])
def receive_data():
    """Handle POST requests"""
    data = request.get_json()
    # Process data here
    return jsonify({'status': 'success', 'received_data': data}), 201
```

#### 2. Add More Routes

Check `member1_backend/backend_examples.py` for:
- User management routes (`/api/users`)
- Data processing functions
- Database helpers
- Authentication middleware
- Error handlers

Example of adding a new route:

```python
@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Get all messages"""
    # Your logic here
    messages = []  # Fetch from storage
    return jsonify({
        'status': 'success',
        'count': len(messages),
        'messages': messages
    })
```

#### 3. Data Validation

```python
def validate_data(data):
    """Validate incoming data"""
    required_fields = ['name', 'message']
    for field in required_fields:
        if field not in data:
            return False, f"Missing field: {field}"
    return True, "Valid"
```

### ✅ Backend Checklist

- [ ] Implement all required routes (/, /health, /data, /api/info)
- [ ] Add error handling (404, 500)
- [ ] Write data validation functions
- [ ] Create unit tests for your routes
- [ ] Document your API endpoints
- [ ] Add logging for debugging

### 🧪 Testing Your Work

```bash
cd main
python app.py

# Test in another terminal:
curl http://localhost:5000/health
curl -X POST http://localhost:5000/data \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","message":"Hello"}'
```

---

## Member 2 - Frontend Lead

### 📁 Your Files
- `main/templates/index.html` - Homepage
- `main/static/style.css` - Styles
- `main/static/script.js` - JavaScript
- `member2_frontend/dashboard.html` - Dashboard page (example)
- `member2_frontend/dashboard.css` - Dashboard styles
- `member2_frontend/dashboard.js` - Dashboard logic

### 🎯 Your Responsibilities

#### 1. HTML Template (in `main/templates/index.html`)

Key sections to maintain:
```html
<!-- Form for data submission -->
<form id="dataForm">
    <input type="text" id="nameInput" placeholder="Name" required>
    <textarea id="messageInput" placeholder="Message" required></textarea>
    <button type="submit">Send Data</button>
</form>

<!-- Response display -->
<div id="response" class="response"></div>
```

#### 2. CSS Styling (in `main/static/style.css`)

Make sure you have:
- Responsive design (`@media` queries)
- Modern color scheme (gradients)
- Hover effects on buttons
- Proper spacing and typography

Example responsive code:
```css
@media (max-width: 768px) {
    .feature-grid {
        grid-template-columns: 1fr;
    }
}
```

#### 3. JavaScript Integration (in `main/static/script.js`)

Key function - Form submission:

```javascript
form.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const data = {
        name: document.getElementById('nameInput').value,
        message: document.getElementById('messageInput').value
    };
    
    try {
        const response = await fetch('/data', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (response.ok) {
            showResponse('success', '✅ Success!');
        } else {
            showResponse('error', '❌ Error: ' + result.message);
        }
    } catch (error) {
        showResponse('error', 'Network error');
    }
});
```

#### 4. Advanced Features (Optional)

Check `member2_frontend/` for:
- Dashboard with navigation
- Data visualization
- User management UI
- Settings panel
- Modal dialogs

### ✅ Frontend Checklist

- [ ] Homepage loads correctly
- [ ] Form submits data to backend
- [ ] Success/error messages display
- [ ] Responsive design works on mobile
- [ ] All buttons and links work
- [ ] CSS animations are smooth
- [ ] No JavaScript errors in console

### 🧪 Testing Your Work

1. Open browser developer tools (F12)
2. Go to http://localhost:5000
3. Test form submission
4. Check console for errors
5. Test on different screen sizes
6. Verify all API calls work

---

## Member 3 - DevOps Engineer

### 📁 Your Files
- `main/Dockerfile` - Docker configuration
- `main/.github/workflows/ci-cd.yml` - CI/CD pipeline
- `member3_devops/Dockerfile.advanced` - Advanced Docker examples
- `member3_devops/ci-cd-advanced.yml` - Advanced CI/CD
- `member3_devops/deploy.sh` - Deployment scripts
- `member3_devops/docker-compose.advanced.yml` - Docker Compose examples

### 🎯 Your Responsibilities

#### 1. Dockerfile (in `main/Dockerfile`)

Current structure:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

#### 2. CI/CD Pipeline (in `main/.github/workflows/ci-cd.yml`)

Pipeline stages:
1. **Test** - Run pytest
2. **Build** - Build Docker image
3. **Deploy** - (Optional) Deploy to cloud

Key job:
```yaml
test:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Set up Python
      uses: actions/setup-python@v5
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: pytest tests/ -v
```

#### 3. Docker Commands

Build and run:
```bash
# Build image
docker build -t flask-lab-project .

# Run container
docker run -d -p 5000:5000 --name flask-app flask-lab-project

# Check logs
docker logs flask-app

# Stop container
docker stop flask-app && docker rm flask-app
```

#### 4. Advanced Features

Check `member3_devops/` for:
- Multi-stage Docker builds
- Advanced CI/CD with security scanning
- Deployment automation scripts
- Docker Compose with multiple services
- Monitoring setup

### ✅ DevOps Checklist

- [ ] Dockerfile builds successfully
- [ ] Docker image runs without errors
- [ ] CI/CD pipeline passes all tests
- [ ] Health checks work
- [ ] Docker Hub integration (optional)
- [ ] Documentation is complete
- [ ] Deployment scripts are tested

### 🧪 Testing Your Work

```bash
# Test Docker build
cd main
docker build -t test-build .

# Test Docker run
docker run -d -p 5000:5000 --name test-run test-build
sleep 10
curl http://localhost:5000/health

# Check CI/CD
# Push to GitHub and check Actions tab

# Use deployment script
cd ../member3_devops
chmod +x deploy.sh
./deploy.sh build
```

---

## Integration Guide

### How Team Members Work Together

#### Workflow 1: Backend → Frontend

1. **Backend** creates API endpoint:
   ```python
   @app.route('/api/users', methods=['GET'])
   def get_users():
       return jsonify({'users': [...]})
   ```

2. **Frontend** consumes endpoint:
   ```javascript
   fetch('/api/users')
       .then(response => response.json())
       .then(data => displayUsers(data.users));
   ```

3. **DevOps** ensures it works in Docker:
   ```bash
   docker build -t test .
   docker run -p 5000:5000 test
   curl http://localhost:5000/api/users
   ```

#### Workflow 2: Frontend → Backend

1. **Frontend** creates form
2. **Backend** receives POST request
3. **DevOps** tests in CI/CD pipeline

#### Workflow 3: All Together

1. Backend implements endpoint
2. Frontend creates UI
3. DevOps deploys and tests
4. Team reviews Pull Request
5. Merge to main → CI/CD runs

### Git Workflow

```bash
# Member 1 (Backend)
git checkout -b backend
# Make changes to app.py
git add main/app.py
git commit -m "feat: add user management routes"
git push origin backend
# Create Pull Request

# Member 2 (Frontend)
git checkout -b frontend
# Make changes to templates/static
git add main/templates main/static
git commit -m "feat: add dashboard UI"
git push origin frontend
# Create Pull Request

# Member 3 (DevOps)
git checkout -b devops
# Make changes to Dockerfile, CI/CD
git add main/Dockerfile main/.github
git commit -m "ci: improve CI/CD pipeline"
git push origin devops
# Create Pull Request
```

---

## Testing Guide

### Running All Tests

```bash
cd main

# Run basic tests
pytest tests/test_app.py -v

# Run advanced tests
pytest tests/test_advanced.py -v

# Run all tests with coverage
pytest tests/ -v --cov=. --cov-report=term-missing

# Run specific test class
pytest tests/test_advanced.py::TestBackendRoutes -v

# Run specific test
pytest tests/test_app.py::test_health -v
```

### Test Coverage Goals

- **Backend**: 80%+ coverage of routes
- **Frontend**: All API calls tested
- **DevOps**: Docker builds and runs successfully

### Writing New Tests

Example for Backend (Member 1):
```python
def test_my_new_endpoint(client):
    response = client.get('/api/my-endpoint')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'expected_field' in data
```

---

## 🎓 Tips for Success

### For Member 1 (Backend)
- Keep routes simple and focused
- Validate all input data
- Return consistent JSON responses
- Add error handling everywhere
- Write tests for each route

### For Member 2 (Frontend)
- Make UI responsive
- Handle loading states
- Show error messages clearly
- Test on different browsers
- Keep JavaScript modular

### For Member 3 (DevOps)
- Keep Dockerfile lean
- Cache dependencies in CI/CD
- Test Docker locally first
- Document all commands
- Monitor pipeline performance

### For Everyone
- Communicate with team
- Review each other's code
- Test before pushing
- Write clear commit messages
- Update documentation
- Ask for help when stuck

---

## 📞 Getting Help

1. Check the main README.md
2. Look at examples in your member directory
3. Test locally before pushing
4. Ask team members
5. Check GitHub Issues

---

## ✅ Final Integration Checklist

Before submission, verify:

- [ ] Backend routes work
- [ ] Frontend displays correctly
- [ ] Docker builds successfully
- [ ] All tests pass
- [ ] CI/CD pipeline succeeds
- [ ] Team reviewed all code
- [ ] Documentation is complete

---

**Good luck with your project! 🚀**
