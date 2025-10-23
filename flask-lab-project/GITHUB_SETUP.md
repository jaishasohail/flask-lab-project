# GitHub Repository Setup Instructions

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon in the top right
3. Select **"New repository"**
4. Fill in:
   - **Repository name**: `flask-lab-project`
   - **Description**: "Collaborative Flask Application with CI/CD & Docker"
   - **Visibility**: Public (or Private if preferred)
   - **DO NOT** initialize with README (we already have one)
5. Click **"Create repository"**

## Step 2: Add Team Members as Collaborators

1. Go to your repository page
2. Click **"Settings"** tab
3. Click **"Collaborators"** in the left sidebar
4. Click **"Add people"**
5. Enter each team member's GitHub username:
   - Member 1 (Backend Lead)
   - Member 2 (Frontend/API Integration)
   - Member 3 (DevOps Engineer)
6. Each member will receive an email invitation

## Step 3: Push Your Code

From your local project directory:

```bash
cd flask-lab-project

# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: Complete Flask lab project setup"

# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/flask-lab-project.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 4: Set Up Branch Protection (Optional but Recommended)

1. Go to **Settings** → **Branches**
2. Click **"Add rule"** under Branch protection rules
3. Branch name pattern: `main`
4. Enable:
   - ✅ Require a pull request before merging
   - ✅ Require approvals (at least 1)
   - ✅ Require status checks to pass before merging
   - ✅ Require conversation resolution before merging
5. Click **"Create"**

## Step 5: Enable GitHub Actions (if not auto-enabled)

1. Go to **"Actions"** tab
2. If prompted, click **"I understand my workflows, go ahead and enable them"**
3. GitHub Actions should now be enabled

## Step 6: (Optional) Set Up Docker Hub Integration

To enable automatic Docker Hub pushes:

1. Create a [Docker Hub](https://hub.docker.com/) account if you don't have one
2. Generate an access token:
   - Go to Account Settings → Security → Access Tokens
   - Click "New Access Token"
   - Name it "GitHub Actions"
   - Copy the token
3. Add secrets to your GitHub repository:
   - Go to **Settings** → **Secrets and variables** → **Actions**
   - Click **"New repository secret"**
   - Add two secrets:
     - Name: `DOCKER_USERNAME`, Value: Your Docker Hub username
     - Name: `DOCKER_PASSWORD`, Value: Your Docker Hub access token

## Step 7: Verify CI/CD Pipeline

1. After pushing code, go to **"Actions"** tab
2. You should see a workflow run starting
3. Click on it to view progress
4. Ensure all jobs complete successfully:
   - ✅ Test
   - ✅ Build
   - ✅ (Optional) Docker Hub Push
   - ✅ Deployment Summary

## Team Member Workflow

Each team member should:

1. **Accept the collaboration invitation** (check email)

2. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/flask-lab-project.git
   cd flask-lab-project
   ```

3. **Create their feature branch:**
   ```bash
   # Backend Lead
   git checkout -b backend
   
   # Frontend Lead
   git checkout -b frontend
   
   # DevOps Engineer
   git checkout -b devops
   ```

4. **Make changes and push:**
   ```bash
   git add .
   git commit -m "descriptive commit message"
   git push origin your-branch-name
   ```

5. **Create Pull Request:**
   - Go to repository on GitHub
   - Click "Pull requests" → "New pull request"
   - Select your branch
   - Add title and description
   - Click "Create pull request"
   - Request reviews from team members

6. **Review and merge:**
   - Team members review the PR
   - Address any comments
   - Once approved, merge to main
   - CI/CD pipeline runs automatically

## Troubleshooting

### Issue: Push rejected
```bash
# Pull latest changes first
git pull origin main
# Resolve any conflicts
# Then push again
git push origin your-branch
```

### Issue: CI/CD not running
- Check if Actions are enabled in Settings
- Ensure `.github/workflows/ci-cd.yml` exists
- Check workflow file syntax

### Issue: Tests failing in CI/CD
- Run tests locally first: `pytest tests/ -v`
- Check the Actions logs for specific errors
- Fix issues and push again

## Best Practices

1. **Always pull before starting work:**
   ```bash
   git checkout main
   git pull origin main
   git checkout your-branch
   git merge main
   ```

2. **Keep commits small and focused**

3. **Write descriptive commit messages**

4. **Review PRs thoroughly**

5. **Keep your branch updated with main:**
   ```bash
   git checkout your-branch
   git merge main
   ```

6. **Never commit directly to main** (use PRs)

7. **Delete branches after merging** (keeps repo clean)

## Useful Git Commands

```bash
# See current branch and status
git status

# See all branches
git branch -a

# Switch branches
git checkout branch-name

# Pull latest changes
git pull origin main

# View commit history
git log --oneline

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard local changes
git checkout -- filename
```

## Additional Resources

- [GitHub Docs - Collaborating](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Hub Documentation](https://docs.docker.com/docker-hub/)

---

**Need Help?** Ask your team members or check the repository Issues tab!
