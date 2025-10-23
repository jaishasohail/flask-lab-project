# 📑 Flask Lab Project - File Index

## 🎯 Start Here

**New to this project?** → Read `GET_STARTED.md` first!

**Setting up GitHub?** → Follow `GITHUB_SETUP.md`

**Ready to submit?** → Check `SUBMISSION_CHECKLIST.md`

## 📚 Documentation Files (Read in Order)

1. **GET_STARTED.md** ⭐ START HERE
   - First steps
   - Quick overview
   - How to run the project

2. **README.md**
   - Complete documentation
   - Technical details
   - API reference

3. **QUICKSTART.md**
   - Fast setup commands
   - Quick testing
   - Common commands

4. **GITHUB_SETUP.md**
   - Repository setup
   - Team collaboration
   - Git workflow

5. **SUBMISSION_CHECKLIST.md**
   - What to submit
   - Verification steps
   - Screenshots guide

6. **PROJECT_STRUCTURE.md**
   - File organization
   - Directory layout
   - Code statistics

## 💻 Application Files

### Core Backend
- `main/app.py` - Flask application (main file)
- `main/requirements.txt` - Dependencies
- `main/pytest.ini` - Test configuration

### Frontend
- `main/templates/index.html` - Homepage
- `main/static/style.css` - Styling
- `main/static/script.js` - JavaScript

### Testing
- `main/tests/test_app.py` - Unit tests
- `main/tests/__init__.py` - Test module init

### DevOps
- `main/Dockerfile` - Docker configuration
- `main/.dockerignore` - Docker ignore rules
- `main/.github/workflows/ci-cd.yml` - CI/CD pipeline
- `docker-compose.yml` - Compose configuration

## 👥 Team Member Guides

- `member1_backend/README.md` - Backend Lead guide
- `member2_frontend/README.md` - Frontend Lead guide
- `member3_devops/README.md` - DevOps Engineer guide

## 🛠️ Utility Files

- `run.sh` - Convenience script to run project
- `.gitignore` - Git ignore rules

## 📂 Directory Structure

```
flask-lab-project/
├── 📘 Documentation (9 files)
│   ├── GET_STARTED.md ⭐
│   ├── README.md
│   ├── QUICKSTART.md
│   ├── GITHUB_SETUP.md
│   ├── SUBMISSION_CHECKLIST.md
│   ├── PROJECT_STRUCTURE.md
│   └── INDEX.md (this file)
│
├── 🐍 Application Code (main/)
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── templates/
│   ├── static/
│   └── tests/
│
└── 👥 Team Workspaces
    ├── member1_backend/
    ├── member2_frontend/
    └── member3_devops/
```

## 🎯 Quick Actions

### I want to...

**Run the application**
```bash
cd main
pip install -r requirements.txt
python app.py
```

**Run tests**
```bash
cd main
pytest tests/ -v
```

**Build Docker image**
```bash
cd main
docker build -t flask-lab-project .
```

**Use the run script**
```bash
./run.sh
```

**Push to GitHub**
- Follow `GITHUB_SETUP.md`

**Prepare submission**
- Check `SUBMISSION_CHECKLIST.md`

## 📊 Project Statistics

- **Total Files**: 23
- **Code Files**: 7 (Python, HTML, CSS, JS)
- **Test Files**: 1 (with 10+ tests)
- **Config Files**: 7
- **Documentation**: 9 files
- **Archive Size**: ~19KB (compressed)

## 🔗 Important Links in README

All web resources and references are documented in `README.md`:
- Flask documentation
- Docker documentation
- GitHub Actions documentation
- pytest documentation

## 🎓 Learning Path

### Day 1: Setup
1. Read `GET_STARTED.md`
2. Extract/clone project
3. Run locally
4. Test Docker

### Day 2: Development
1. Read your team member README
2. Create your branch
3. Make changes
4. Test locally

### Day 3: Collaboration
1. Push to GitHub
2. Create Pull Request
3. Review team code
4. Merge changes

### Day 4: CI/CD
1. Watch pipeline run
2. Fix any issues
3. Take screenshots
4. Prepare submission

### Day 5: Submit
1. Follow `SUBMISSION_CHECKLIST.md`
2. Verify everything works
3. Submit project

## 🆘 Troubleshooting Guide

**Problem → Solution File**

- Can't start app → `README.md` (Troubleshooting)
- Git issues → `GITHUB_SETUP.md`
- Docker issues → `member3_devops/README.md`
- Test failures → `README.md` (Testing section)
- CI/CD problems → `member3_devops/README.md`

## ✅ File Purposes at a Glance

| File | Purpose | Who Reads |
|------|---------|-----------|
| GET_STARTED.md | Initial setup | Everyone first |
| README.md | Main docs | Everyone |
| QUICKSTART.md | Fast reference | During development |
| GITHUB_SETUP.md | GitHub config | Before pushing |
| SUBMISSION_CHECKLIST.md | Submission | Before submitting |
| member1_backend/README.md | Backend guide | Backend lead |
| member2_frontend/README.md | Frontend guide | Frontend lead |
| member3_devops/README.md | DevOps guide | DevOps engineer |
| app.py | Application | All (to understand) |
| test_app.py | Tests | All (to verify) |
| Dockerfile | Container | DevOps mainly |
| ci-cd.yml | Pipeline | DevOps mainly |

## 🎯 Success Checklist

- [ ] Read GET_STARTED.md
- [ ] Application runs locally
- [ ] Tests pass
- [ ] Docker works
- [ ] Pushed to GitHub
- [ ] Team members added
- [ ] CI/CD succeeds
- [ ] Screenshots taken
- [ ] Ready to submit

## 📞 Quick Help

- **Stuck?** → Read README.md troubleshooting
- **Need commands?** → Check QUICKSTART.md
- **Submitting?** → Follow SUBMISSION_CHECKLIST.md
- **Team questions?** → See your member README

---

**Welcome to the Flask Lab Project! 🚀**

*This index helps you navigate the project. Start with GET_STARTED.md!*

---

Last Updated: October 2025
