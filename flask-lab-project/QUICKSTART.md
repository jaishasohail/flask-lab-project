# 🚀 Quick Start Guide

## Get Running in 5 Minutes!

### Option 1: Run with Python (Development)

```bash
# 1. Navigate to main directory
cd flask-lab-project/main

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py

# 4. Open browser
# Visit: http://localhost:5000
```

### Option 2: Run with Docker (Production-like)

```bash
# 1. Navigate to main directory
cd flask-lab-project/main

# 2. Build Docker image
docker build -t flask-lab-project .

# 3. Run container
docker run -p 5000:5000 flask-lab-project

# 4. Open browser
# Visit: http://localhost:5000
```

### Option 3: Run with Docker Compose (Easiest)

```bash
# 1. From project root
cd flask-lab-project

# 2. Start everything
docker-compose up

# 3. Open browser
# Visit: http://localhost:5000

# 4. Stop when done
# Press Ctrl+C, then run:
docker-compose down
```

## Test the Application

### Run Tests
```bash
cd flask-lab-project/main
pytest tests/ -v
```

### Test API with cURL

```bash
# Health check
curl http://localhost:5000/health

# Submit data
curl -X POST http://localhost:5000/data \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","message":"Hello"}'
```

## Common Commands

### Docker
```bash
# View running containers
docker ps

# View logs
docker logs flask-lab-project

# Stop container
docker stop flask-lab-project

# Remove container
docker rm flask-lab-project
```

### Git Workflow
```bash
# Create your branch
git checkout -b your-branch-name

# Make changes, then:
git add .
git commit -m "your message"
git push origin your-branch-name

# Then create Pull Request on GitHub
```

## Need Help?

- Check main README.md for detailed documentation
- Review your team member directory README
- Check GitHub Issues tab
- Ask your team members!

## Team Setup Checklist

- [ ] Clone repository
- [ ] Create your feature branch
- [ ] Install dependencies
- [ ] Run application locally
- [ ] Make your first change
- [ ] Run tests
- [ ] Create Pull Request
- [ ] Review team member's code

---

**You're all set! Happy coding! 🎉**
